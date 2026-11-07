"""Instituto Alpino de GO (go-hakuren-go): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y
espalda). Peinados de nieve y hielo: cristales, capuchas de nieve, setas, bufandas y gafas de esquí."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, strand  # noqa: F401
from chars_alius import WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def octa(cx, cy, r):
    import math
    return [(cx + r * math.cos(math.pi / 8 + i * math.pi / 4), cy + r * 0.9 * math.sin(math.pi / 8 + i * math.pi / 4)) for i in range(8)]


# Wolfe Whyte (portero): pelo castaño peinado hacia atrás en mechones recogidos, con un mechón largo que sale de la raya y
# se curva hacia fuera por delante de la cara y otro que baja por la mejilla; ojos gris azulado y media sonrisa
CHARS['wolfe-whyte'] = {
    'body': 'normal', 'pal': pal('#7a4a26', '#fcd4a8', iris='#5a6a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (58, 40)},
    'front': [L(outline([(16, 66), (12, 32), (24, 6), (50, -4), (76, 6), (88, 32), (84, 66), (80, 52), (20, 52)])),
              L(outline([(60, 2), (84, 14), (90, 44), (84, 62), (76, 38)]), 'shade', 'b', False),
              strand([(30, 6), (34, 36)], 'deep', 'b', 1.0), strand([(42, -2), (44, 34)], 'deep', 'b', 1.0), strand([(58, -2), (56, 34)], 'deep', 'b', 1.0),
              strand([(70, 6), (66, 36)], 'deep', 'b', 1.0),
              L(outline([(50, 30), (32, 40), (14, 52), (-8, 58, 1), (12, 46), (34, 32), (48, 24)]), 'mid', 'f', ln=True),
              L(outline([(66, 36), (84, 52), (82, 80, 1), (76, 54)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 52), (64, 40), (80, 38), (90, 24), (80, 6), (58, -6), (30, -4), (-6, 8, 1), (14, 14), (6, 30), (4, 56), (12, 74), (30, 76), (46, 64)])),
             L(outline([(8, 30), (26, 38), (28, 66), (12, 60)]), 'shade', 'b', False),
             strand([(84, 18), (50, 6), (14, 14)], 'deep', 'b', 1.0), strand([(84, 30), (50, 20), (8, 32)], 'deep', 'b', 1.0),
             L(outline([(86, 30), (92, 48), (90, 74, 1), (84, 50)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 76), (12, 36), (22, 8), (50, -4), (78, 8), (88, 36), (100, 40), (110, 34, 1), (100, 46), (86, 50), (84, 76), (50, 84)])),
             L(outline([(56, -2), (82, 10), (90, 44), (84, 72), (62, 80)]), 'shade', 'b', False),
             strand([(24, 20), (40, 40), (30, 60), (50, 76)], 'deep', 'b', 1.0), strand([(76, 20), (60, 40), (70, 60), (50, 76)], 'deep', 'b', 1.0)],
}

# Sascha Kotch: grandullón moreno de cara cuadrada, nariz enorme marrón y ojos de punto; el pelo, una corona de cristales
# de hielo celestes y grises en lo alto, y patillas largas verde oscuro que bajan por los lados de la cara
CHARS['sascha-kotch'] = {
    'body': 'corpulento', 'pal': pal('#a8dce4', '#b07a4e', iris='#2a2a2a', shade='#8a8e96', deep='#6a6e76', buzz='#2a4448', nose='#8a4a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': (40, 34), 'face_front': WIDE_FACE},
    'front': [L(outline([(12, 40), (88, 40), (88, 56), (12, 56)]), 'buzz'),
              L(outline([(4, 46), (-2, 26, 1), (12, 26), (14, 2, 1), (28, 20), (36, -6, 1), (48, 16), (58, -8, 1), (66, 16), (78, -2, 1), (82, 22), (98, 12, 1),
                         (92, 30), (104, 44, 1), (86, 42), (50, 38), (14, 42)])),
              L(outline([(14, 4), (28, 20), (20, 36)]), 'shade', 'b', False), L(outline([(36, -4), (48, 16), (40, 34)]), 'shade', 'b', False),
              L(outline([(58, -6), (66, 16), (60, 34)]), 'shade', 'b', False), L(outline([(78, 0), (82, 22), (78, 36)]), 'shade', 'b', False),
              L(outline([(12, 44), (20, 44), (20, 96), (14, 96)]), 'buzz', 'f', ln=True), L(outline([(88, 44), (80, 44), (80, 96), (86, 96)]), 'buzz', 'f', ln=True),
              L(outline([(44, 60), (56, 60), (60, 86), (40, 86)]), 'nose', 'f', ln=True)] + white_eyes(70, 12, 4.2, 4.2, 1.4),
    'side': [L(outline([(12, 40), (58, 40), (58, 62), (48, 82), (40, 96), (20, 92), (8, 70)]), 'buzz'),
             L(outline([(10, 44), (2, 22, 1), (20, 22), (24, -2, 1), (38, 16), (52, -8, 1), (62, 14), (76, -2, 1), (80, 20), (98, 14, 1), (90, 34), (70, 40), (40, 42)])),
             L(outline([(24, 0), (38, 16), (30, 34)]), 'shade', 'b', False), L(outline([(52, -6), (62, 14), (56, 34)]), 'shade', 'b', False),
             L(outline([(56, 44), (62, 44), (62, 92), (56, 92)]), 'buzz', 'f', ln=True),
             L(outline([(84, 60), (100, 70), (100, 86), (84, 86)]), 'nose', 'f', ln=True)] + side_eye(70),
    'back': [L(outline([(14, 40), (86, 40), (86, 84), (14, 84)]), 'buzz'),
             L(outline([(4, 48), (-6, 30, 1), (10, 28), (12, 2, 1), (28, 20), (38, -8, 1), (50, 16), (62, -8, 1), (72, 20), (88, 2, 1), (90, 28), (106, 30, 1), (96, 48),
                        (50, 42)])),
             L(outline([(38, -6), (50, 16), (44, 40)]), 'shade', 'b', False), L(outline([(62, -6), (72, 20), (66, 40)]), 'shade', 'b', False)],
}

# Guy L'Acier: melena larga rubio crema con raya y un mechón que le cae por delante del hombro hasta el pecho; gafas de
# esquí naranjas con montura gris tapándole los ojos y dientes apretados
CHARS['guy-l-acier'] = {
    'body': 'delgado', 'pal': pal('#eadcb4', '#fcd8b0', iris='#2a2a2a', shade='#c8b48a', frame='#8a8e96', lens='#f05a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 92), (2, 50), (6, 20), (24, 0), (50, -6), (76, 2), (92, 22), (96, 50), (94, 82), (86, 66), (84, 50), (16, 50), (14, 70)])),
              L(outline([(60, 2), (84, 16), (94, 46), (90, 76), (80, 46)]), 'shade', 'b', False),
              L(outline([(6, 56), (-4, 90), (2, 122), (14, 138, 1), (20, 112), (18, 80), (16, 62)]), 'mid', 'f', ln=True),
              fringe([(12, 62), (16, 36), (34, 20), (54, 18), (72, 26), (86, 42), (88, 58), (72, 48), (58, 46), (50, 66, 1), (46, 46), (30, 46), (20, 54)]),
              L(outline([(14, 70), (86, 70), (85, 84), (15, 84)]), 'frame', 'f', ln=True),
              L(ell(34, 77, 11, 5.6), 'lens', 'f', ln=True), L(ell(66, 77, 11, 5.6), 'lens', 'f', ln=True),
              L(quad((40, 74), (50, 70), (60, 74)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(56, 60), (62, 48), (82, 46), (92, 30), (86, 10), (64, -6), (34, -4), (12, 10), (2, 40), (-2, 80), (8, 110), (28, 124, 1), (30, 98), (40, 82),
                        (48, 68)])),
             L(outline([(2, 40), (26, 44), (32, 100), (10, 106)]), 'shade', 'b', False),
             fringe([(64, 0), (90, 16), (96, 40), (92, 60, 1), (84, 46), (74, 34)]),
             L(outline([(76, 70), (94, 70), (96, 84), (76, 84)]), 'frame', 'f', ln=True), L(ell(88, 77, 5, 5), 'lens', 'f', ln=True),
             L([(76, 76), (50, 74)], 'frame', 'f', False, False, 3)],
    'back': [L(outline([(6, 100), (2, 50), (6, 20), (24, 0), (50, -6), (76, 2), (94, 22), (96, 50), (94, 100), (70, 108), (50, 112, 1), (30, 108)])),
             L(outline([(56, -2), (84, 14), (96, 50), (94, 98), (64, 106)]), 'shade', 'b', False),
             L([(6, 74), (94, 74)], 'frame', 'f', False, False, 3)],
}

# Matther Horne: pelo rosa muy pálido, alborotado en pinchos enormes hacia arriba y a los lados con un pico en medio de la
# frente; visera de esquí verde lima con montura blanca y cara de malas pulgas
CHARS['matther-horne'] = {
    'body': 'normal', 'pal': pal('#f2dae8', '#fcd4a8', iris='#2a2a2a', shade='#c8a0b8', deep='#a87c94', visor='#a8e030', frame='#f0f0f0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 60), (14, 40), (-10, 6, 1), (16, 16), (18, -12, 1), (34, 8), (44, -18, 1), (52, 4), (62, -14, 1), (68, 8), (86, -12, 1), (82, 16),
                         (110, 2, 1), (86, 40), (82, 60), (50, 50)])),
              L(outline([(62, -10), (68, 8), (86, -8), (82, 18), (100, 8), (84, 40), (76, 30)]), 'shade', 'b', False),
              fringe([(18, 56), (22, 40), (36, 32), (50, 28), (64, 32), (78, 40), (82, 56), (68, 50), (56, 50), (50, 66, 1), (44, 50), (32, 50)]),
              L(outline([(16, 68), (84, 68), (82, 84), (18, 84)]), 'frame', 'f', ln=True),
              L(outline([(21, 70), (79, 70), (78, 82), (22, 82)]), 'visor', 'f', False),
              L(outline([(28, 76), (40, 74), (38, 79)]), OUTC, 'f', False), L(outline([(72, 76), (60, 74), (62, 79)]), OUTC, 'f', False)],
    'side': [L(outline([(56, 56), (62, 46), (80, 42), (92, 20), (100, -2, 1), (76, 6), (70, -16, 1), (52, 2), (34, -12, 1), (30, 8), (0, -4, 1), (12, 18), (-14, 30, 1),
                        (6, 40), (0, 62, 1), (14, 64), (22, 78), (40, 74)])),
             L(outline([(8, 30), (26, 40), (28, 66), (12, 60)]), 'shade', 'b', False),
             L(outline([(70, 68), (96, 68), (96, 84), (70, 84)]), 'frame', 'f', ln=True), L(outline([(76, 70), (94, 70), (94, 82), (76, 82)]), 'visor', 'f', False)],
    'back': [L(outline([(18, 76), (14, 44), (-12, 8, 1), (16, 18), (16, -10, 1), (34, 8), (46, -16, 1), (54, 6), (64, -12, 1), (70, 10), (88, -10, 1), (84, 18),
                        (112, 6, 1), (86, 44), (82, 76), (50, 84)])),
             L(outline([(56, 6), (84, 18), (88, 50), (82, 72), (62, 80)]), 'shade', 'b', False),
             L([(12, 72), (88, 72)], 'frame', 'f', False, False, 3)],
}

# Iggie Loo: pelo verde azulado oscuro en forma de seta, con el flequillo largo que le tapa media cara y un ojo; una bufanda
# rosa enorme enrollada le tapa la boca y la barbilla
CHARS['iggie-loo'] = {
    'body': 'normal', 'pal': pal('#1e7a6a', '#fcd8b4', iris='#2a2a2a', scarf='#e8c8cc', scarf_d='#c8a0a4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(-8, 64, 1), (4, 52), (10, 20), (30, 2), (50, -4), (70, 2), (90, 20), (96, 52), (108, 64, 1), (86, 60), (14, 60)])),
              L(outline([(60, 2), (84, 14), (94, 46), (100, 60), (80, 56)]), 'shade', 'b', False),
              fringe([(8, 58), (14, 30), (30, 12), (50, 6), (70, 12), (86, 30), (92, 58), (78, 58), (74, 64), (58, 64), (56, 90, 1), (40, 88), (24, 74), (14, 64)]),
              strand([(36, 12), (34, 60)], 'deep', 'f', 1.0), strand([(50, 8), (48, 70)], 'deep', 'f', 1.0), strand([(66, 12), (66, 56)], 'deep', 'f', 1.0),
              L(ell(68, 76, 4.4, 5), WHITE, 'f', ln=True), L(ell(69, 76.5, 1.8, 2.4), OUTC, 'f', False),
              L(outline([(8, 88), (50, 80), (92, 88), (96, 104), (88, 120), (50, 124), (12, 120), (4, 104)]), 'scarf', 'f', ln=True),
              L(outline([(12, 100), (50, 96), (88, 100), (86, 108), (50, 104), (14, 108)]), WHITE, 'f', False),
              L(outline([(60, 106), (90, 104), (86, 118), (60, 120)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(-12, 54, 1), (4, 42), (10, 14), (30, -4), (60, -6), (84, 6), (96, 30), (98, 52), (84, 56), (60, 50), (30, 52), (10, 56)])),
             L(outline([(0, 48), (40, 44), (80, 50), (60, 56), (20, 58)]), 'shade', 'b', False),
             strand([(30, 0), (20, 50)], 'deep', 'b', 1.0), strand([(56, -4), (52, 46)], 'deep', 'b', 1.0),
             L(outline([(20, 80), (70, 80), (100, 86), (102, 104), (90, 118), (50, 122), (24, 114), (16, 96)]), 'scarf', 'f', ln=True),
             L(outline([(24, 96), (98, 98), (96, 104), (26, 104)]), WHITE, 'f', False)],
    'back': [L(outline([(-8, 60, 1), (4, 48), (10, 20), (30, 2), (50, -4), (70, 2), (90, 20), (96, 48), (108, 60, 1), (86, 64), (50, 66), (14, 64)])),
             L(outline([(4, 50), (50, 56), (96, 50), (86, 64), (14, 64)]), 'deep', 'b', False),
             L(outline([(14, 70), (86, 70), (90, 104), (82, 118), (50, 122), (18, 118), (10, 104)]), 'scarf', 'f', ln=True),
             strand([(16, 84), (50, 88), (84, 84)], 'scarf_d', 'f', 1.2), strand([(14, 100), (50, 104), (86, 100)], 'scarf_d', 'f', 1.2)],
}

# Bob Sled: un pelo blanco enorme como una capucha de nieve que le cubre la cabeza y se abre por abajo hasta los hombros,
# con las puntas rosadas; solo asoma la cara, con un ojo rojo entre los mechones
CHARS['bob-sled'] = {
    'body': 'normal', 'pal': pal('#eef4f0', '#d8a070', iris='#c82a2a', shade='#c8aaa8', deep='#a88884'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(-16, 110, 1), (-6, 90), (4, 56), (14, 18), (32, -6), (50, -14), (70, -6), (86, 18), (96, 56), (106, 90), (116, 110, 1), (86, 112),
                         (70, 100), (66, 66), (56, 44), (38, 46), (30, 66), (28, 100), (14, 112)]), 'mid', 'f'),
              L(outline([(-16, 108), (0, 92), (26, 96), (16, 112)]), 'shade', 'f', False), L(outline([(116, 108), (100, 92), (72, 96), (86, 112)]), 'shade', 'f', False),
              L(outline([(56, -6), (70, -2), (88, 30), (100, 80), (82, 70), (74, 30)]), 'shade', 'f', False),
              L(outline([(56, 44), (66, 52), (64, 74), (56, 60)]), 'mid', 'f', ln=True),
              L(ell(52, 76, 4, 5), WHITE, 'f', ln=True), L(ell(53, 76.5, 2, 2.8), 'iris', 'f', False)],
    'side': [L(outline([(-14, 108, 1), (-4, 84), (8, 36), (28, -6), (60, -12), (86, 4), (98, 36), (104, 70), (112, 96, 1), (88, 92), (76, 68), (66, 50), (40, 52),
                        (30, 80), (24, 104), (6, 112)]), 'mid', 'f'),
             L(outline([(-14, 104), (4, 88), (26, 92), (16, 110)]), 'shade', 'f', False), L(outline([(20, 10), (40, 0), (50, 30), (30, 40)]), 'shade', 'f', False)],
    'back': [L(outline([(-16, 110, 1), (-6, 90), (4, 56), (14, 18), (32, -6), (50, -14), (70, -6), (86, 18), (96, 56), (106, 90), (116, 110, 1), (80, 116),
                        (50, 118), (20, 116)])),
             L(outline([(-12, 104), (10, 88), (50, 92), (90, 88), (112, 104), (50, 114)]), 'shade', 'b', False),
             L(outline([(56, 10), (80, 6), (88, 40), (70, 46)]), 'shade', 'b', False)],
}

# Blain Chills: pelo granate con un rizo que le cae en la frente, mechones que se abren en punta a los lados a la altura de
# las orejas y la melena hasta el cuello; piel pálida y ojos de sueño entornados
CHARS['blain-chills'] = {
    'body': 'delgado', 'pal': pal('#8a2a3e', '#fce4c4', iris='#2a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 72), (-12, 66, 1), (8, 56), (10, 24), (26, 4), (50, -4), (74, 4), (90, 24), (92, 56), (112, 66, 1), (90, 72), (88, 100), (80, 64),
                         (20, 64), (12, 100)])),
              L(outline([(60, 2), (84, 16), (92, 46), (88, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 36), (28, 18), (50, 12), (72, 18), (86, 36), (88, 62), (78, 50), (70, 40), (60, 44), (56, 34), (48, 50), (52, 60, 1), (44, 56),
                      (40, 42), (28, 42), (20, 52)]),
              L(quad((48, 22), (40, 38), (50, 44)), 'deep', 'f', False, False, 1.4)] + white_eyes(77, 15, 6, 4.6, 1.6, lid=1.5),
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (92, 34), (88, 12), (66, -2), (38, -2), (14, 10), (2, 34), (-14, 52, 1), (4, 58), (4, 90), (20, 102), (36, 96),
                        (44, 78)])),
             L(outline([(4, 36), (26, 42), (30, 92), (10, 92)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (90, 58, 1), (82, 44), (74, 32)])] + side_eye(77, lid=1),
    'back': [L(outline([(12, 96), (8, 64), (-12, 62, 1), (8, 52), (10, 24), (26, 4), (50, -4), (74, 4), (90, 24), (92, 52), (112, 62, 1), (92, 64), (88, 96), (50, 102)])),
             L(outline([(56, 2), (84, 16), (92, 50), (88, 94), (62, 100)]), 'shade', 'b', False)],
}

# Art Tundra: pelo negro azulado como un casco con la raya en medio que cae liso hasta la nuca, y por dentro mechones gris
# verdoso que le enmarcan la cara hasta la mandíbula; sonrisa amable
CHARS['art-tundra'] = {
    'body': 'normal', 'pal': pal('#1e2a34', '#fce4c4', iris='#2a2a2a', inner='#8aa0a0', inner_d='#6a8080'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (60, 40)},
    'front': [L(outline([(10, 76), (8, 32), (20, 6), (50, -2), (80, 6), (92, 32), (90, 76), (84, 56), (16, 56)])),
              L(outline([(60, 4), (84, 16), (92, 46), (88, 72), (78, 40)]), 'shade', 'b', False),
              strand([(50, -2), (50, 30)], 'deep', 'b', 1.2),
              L(outline([(10, 60), (22, 42), (40, 34), (50, 40), (36, 42), (24, 58), (22, 100), (10, 100)]), 'inner', 'f', ln=True),
              L(outline([(90, 60), (78, 42), (60, 34), (50, 40), (64, 42), (76, 58), (78, 100), (90, 100)]), 'inner', 'f', ln=True)],
    'side': [L(outline([(56, 56), (64, 44), (80, 42), (92, 28), (86, 8), (64, -4), (36, -4), (14, 10), (4, 40), (2, 80), (8, 104), (22, 112), (30, 96), (40, 78), (48, 64)])),
             L(outline([(4, 40), (26, 46), (30, 100), (10, 104)]), 'shade', 'b', False),
             L(outline([(62, 46), (82, 44), (88, 54), (76, 58), (70, 96), (62, 92)]), 'inner', 'f', ln=True)],
    'back': [L(outline([(12, 92), (8, 32), (20, 6), (50, -2), (80, 6), (92, 32), (88, 92), (50, 100)])),
             L(outline([(56, 2), (84, 16), (92, 50), (88, 90), (62, 96)]), 'shade', 'b', False),
             strand([(50, -2), (50, 96)], 'deep', 'b', 1.2)],
}

# Borel Aurora: lo alto de la cabeza azul oscuro con un pliegue en medio, y una enorme rosca de pelo gris azulado alrededor
# que le tapa los ojos y sobresale a los lados; dientes apretados
CHARS['borel-aurora'] = {
    'body': 'normal', 'pal': pal('#2e4e70', '#fcd4a8', iris='#2a2a2a', roll='#9aa0b0', roll_l='#c4e4f4', roll_d='#7a7e8e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 46), (20, 12), (38, -8), (50, 0), (62, -8), (80, 12), (84, 46)])),
              L(outline([(62, -6), (80, 12), (84, 42), (70, 40)]), 'shade', 'b', False),
              L(outline([(-12, 64), (-8, 46), (10, 38), (32, 38), (50, 50), (68, 38), (90, 38), (108, 46), (112, 64), (102, 76), (72, 78), (50, 68), (28, 78), (-2, 76)]),
                'roll', 'f', ln=True),
              L(outline([(-6, 50), (12, 42), (34, 44), (44, 52), (28, 54), (8, 54)]), 'roll_l', 'f', False),
              L(outline([(106, 50), (88, 42), (66, 44), (56, 52), (72, 54), (92, 54)]), 'roll_l', 'f', False),
              strand([(0, 66), (24, 70), (46, 64)], 'roll_d', 'f', 1.0), strand([(100, 66), (76, 70), (54, 64)], 'roll_d', 'f', 1.0)],
    'side': [L(outline([(16, 46), (20, 12), (40, -6), (66, -6), (84, 12), (88, 46)])),
             L(outline([(-10, 62), (-6, 46), (20, 38), (80, 38), (102, 46), (106, 62), (96, 74), (0, 74)]), 'roll', 'f', ln=True),
             L(outline([(-4, 50), (20, 42), (90, 42), (100, 50), (60, 54)]), 'roll_l', 'f', False),
             strand([(0, 64), (50, 66), (98, 64)], 'roll_d', 'f', 1.0)],
    'back': [L(outline([(16, 76), (14, 46), (84, 46), (84, 76), (50, 84)]), 'deep'),
             L(outline([(16, 46), (20, 12), (38, -8), (50, 0), (62, -8), (80, 12), (84, 46)])),
             L(outline([(-12, 64), (-8, 46), (12, 38), (88, 38), (108, 46), (112, 64), (102, 76), (-2, 76)]), 'roll', 'f', ln=True),
             L(outline([(-6, 50), (14, 42), (86, 42), (106, 50), (50, 54)]), 'roll_l', 'f', False)],
}

# Blake Wintry: pelo rojo en casco redondo con un flequillo castaño oscuro que cruza la frente en diagonal y una colita en la
# nuca; ojos azules muy abiertos y boca de susto
CHARS['blake-wintry'] = {
    'body': 'bajito', 'pal': pal('#c0402a', '#fcd8b0', iris='#2a8ad8', bang='#5a2e20', bang_d='#3e1e14'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 78), (8, 40), (16, 12), (50, -2), (84, 12), (92, 40), (88, 78), (84, 58), (16, 58)])),
              L(outline([(66, 6), (86, 16), (92, 44), (86, 72), (80, 46)]), 'shade', 'b', False),
              L(outline([(14, 60), (14, 40), (26, 24), (36, 40), (26, 54), (20, 70, 1)]), 'mid', 'f'),
              L(outline([(26, 22), (44, 4), (66, 0), (84, 14), (88, 36), (84, 58), (74, 44), (62, 46), (50, 60), (36, 66, 1), (34, 50)]), 'bang', 'f', ln=True),
              L(outline([(56, 4), (80, 14), (84, 40), (70, 30)]), 'bang_d', 'f', False)],
    'side': [L(outline([(54, 60), (58, 50), (80, 48), (92, 34), (88, 12), (66, -2), (40, -2), (16, 8), (4, 34), (4, 64), (14, 80), (-4, 92, 1), (24, 86), (40, 80),
                        (46, 70)])),
             L(outline([(4, 36), (28, 42), (32, 78), (10, 76)]), 'shade', 'b', False),
             L(outline([(62, 2), (88, 14), (96, 40), (94, 62, 1), (84, 44), (74, 30)]), 'bang', 'f', ln=True)],
    'back': [L(outline([(12, 80), (8, 40), (16, 12), (50, -2), (84, 12), (92, 40), (88, 80), (64, 86), (50, 98, 1), (36, 86)])),
             L(outline([(56, 2), (84, 14), (92, 46), (88, 78), (64, 84)]), 'shade', 'b', False),
             L(outline([(30, 82), (50, 86), (70, 82), (66, 98), (58, 92), (50, 102, 1), (42, 92), (34, 98)]), 'bang', 'f', ln=True)],
}

# Njord Snio (Yukimura Hyouga): pelo azul añil revuelto de puntas con un mechón que se arquea en lo alto y dos mechones finos
# que bajan junto a la cara y se curvan hacia fuera en la mandíbula; ojos celestes y cejas gruesas
CHARS['njord-snio'] = {
    'body': 'normal', 'pal': pal('#2c2a8a', '#fcdcbc', iris='#3ab0d8'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 66), (-4, 60, 1), (8, 46), (-2, 30, 1), (14, 22), (14, 4), (34, -6), (44, -18, 1), (54, -4), (74, -2), (94, 10, 1), (88, 26), (106, 32, 1),
                         (90, 44), (104, 60, 1), (84, 66), (82, 50), (18, 50)])),
              L(outline([(60, -2), (84, 8), (94, 36), (88, 60), (78, 40)]), 'shade', 'b', False),
              L(quad((44, 0), (46, -16), (58, -20)), 'mid', 'b', False, False, 3.0),
              fringe([(14, 58), (18, 36), (32, 22), (50, 18), (68, 22), (82, 36), (86, 58), (76, 48), (70, 58, 1), (64, 44), (56, 56, 1), (50, 42), (44, 58, 1),
                      (36, 44), (30, 56, 1), (22, 48)]),
              L(quad((16, 60), (14, 90), (6, 104)), 'mid', 'f', False, False, 2.6), L(quad((84, 60), (86, 90), (94, 104)), 'mid', 'f', False, False, 2.6)],
    'side': [L(outline([(58, 56), (64, 46), (82, 44), (90, 30), (84, 12), (92, -6, 1), (70, 0), (60, -18, 1), (46, -4), (22, -8, 1), (24, 8), (-6, 12, 1), (10, 24),
                        (-12, 36, 1), (6, 46), (-6, 62, 1), (12, 64), (6, 82, 1), (22, 76), (34, 80), (46, 66)])),
             L(outline([(6, 36), (24, 44), (24, 70), (8, 62)]), 'shade', 'b', False),
             fringe([(68, 2), (90, 16), (94, 38), (90, 54, 1), (82, 40), (74, 30)]),
             L(quad((66, 60), (64, 90), (56, 104)), 'mid', 'f', False, False, 2.6)],
    'back': [L(outline([(16, 80), (0, 76, 1), (8, 64), (-8, 52, 1), (8, 44), (-2, 26, 1), (14, 22), (14, 4), (34, -6), (50, -2), (70, -4), (92, 6, 1), (88, 22),
                        (106, 30, 1), (92, 44), (108, 54, 1), (92, 64), (100, 78, 1), (84, 80), (62, 86), (50, 100, 1), (38, 86)])),
             L(outline([(56, 0), (84, 10), (94, 44), (88, 76), (62, 84)]), 'shade', 'b', False),
             L(quad((20, 76), (14, 96), (4, 102)), 'mid', 'f', False, False, 2.6), L(quad((80, 76), (86, 96), (96, 102)), 'mid', 'f', False, False, 2.6)],
}

# Yule Hoarfrost: pelo celeste grisáceo erizado en muchísimos pinchos dentados, como escarcha, más gris por detrás; ojos
# afilados y cejas fruncidas
CHARS['yule-hoarfrost'] = {
    'body': 'normal', 'pal': pal('#b0d4d8', '#fce4c8', iris='#2a2a2a', shade='#8a9294', deep='#6a7072'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (62, 50)},
    'front': messy('front', 16, 13, seed=411, rx=52, ry=44, cy=40, lo=70)
             + [fringe([(14, 60), (16, 40), (28, 28), (50, 24), (72, 28), (84, 40), (86, 60), (78, 50), (74, 60, 1), (66, 46), (58, 56, 1), (52, 44), (44, 58, 1),
                        (38, 44), (30, 56, 1), (24, 46), (20, 58, 1)]),
                L(outline([(36, 26), (44, 10, 1), (52, 26)]), 'mid', 'f')],
    'side': messy('side', 16, 11, seed=412, rx=50, ry=44, cy=40, nape=90, sweep=-0.3, c='shade')
            + [fringe([(66, 4), (90, 16), (94, 38), (90, 56, 1), (82, 42), (74, 30)]), L(outline([(30, 2), (56, -6), (70, 6), (40, 14)]), 'mid', 'f', False)],
    'back': messy('back', 16, 13, seed=413, rx=52, ry=44, cy=40, nape=92, c='shade'),
}

# Suno Aisu (portero suplente): pelo blanco grisáceo en casco con el flequillo recto hasta las cejas y las puntas de los lados
# vueltas hacia fuera; gafas octogonales verde oscuro unidas por una tira blanca, y una cinta rosada por detrás
CHARS['suno-aisu'] = {
    'body': 'normal', 'pal': pal('#e0e4e4', '#fcd8b0', iris='#2a2a2a', shade='#b8b0b0', deep='#988e8e', lens='#2a4a2a', band='#d8b8b8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 90), (-4, 100, 1), (8, 82), (8, 40), (16, 12), (50, 0), (84, 12), (92, 40), (92, 82), (104, 100, 1), (88, 90), (84, 64), (16, 64)])),
              L(outline([(60, 4), (84, 14), (92, 46), (90, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 64), (12, 38), (24, 16), (50, 8), (76, 16), (88, 38), (88, 64)]),
              strand([(30, 16), (28, 62)], 'deep', 'f', 1.0), strand([(50, 8), (50, 62)], 'deep', 'f', 1.0), strand([(70, 16), (72, 62)], 'deep', 'f', 1.0),
              L(outline(octa(32, 78, 12), 2), OUTC, 'f', False), L(outline(octa(68, 78, 12), 2), OUTC, 'f', False),
              L(outline(octa(32, 78, 9), 2), 'lens', 'f', False), L(outline(octa(68, 78, 9), 2), 'lens', 'f', False),
              L(outline([(40, 74), (60, 74), (60, 80), (40, 80)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(56, 64), (60, 52), (80, 50), (92, 36), (88, 14), (66, -2), (38, -2), (14, 10), (4, 34), (4, 70), (10, 94), (-6, 104, 1), (22, 98), (36, 92),
                        (44, 76)])),
             L(outline([(4, 40), (40, 30), (56, 52), (40, 90), (8, 90)]), 'shade', 'b', False),
             L(outline([(6, 60), (60, 60), (60, 66), (6, 66)]), 'band', 'b', ln=True),
             fringe([(64, 2), (90, 14), (94, 38), (92, 62), (84, 62), (76, 40)]),
             L(outline(octa(86, 78, 8), 2), OUTC, 'f', False), L(outline(octa(86, 78, 6), 2), 'lens', 'f', False)],
    'back': [L(outline([(12, 90), (-4, 100, 1), (8, 82), (8, 40), (16, 12), (50, 0), (84, 12), (92, 40), (92, 82), (104, 100, 1), (88, 90), (66, 94), (50, 104, 1),
                        (34, 94)]), 'shade'),
             L(outline([(8, 40), (16, 12), (50, 0), (84, 12), (92, 40), (50, 34)]), 'mid', 'b', False),
             L(outline([(8, 58), (92, 58), (92, 66), (8, 66)]), 'band', 'f', ln=True)],
}

# Himesh Himalaya: piel morena, pelo negro abultado en lo alto con raya en medio y dos mechones largos y lisos que le caen
# por delante hasta el pecho; ojos celestes de mirada seria
CHARS['himesh-himalaya'] = {
    'body': 'normal', 'pal': pal('#22222c', '#a87a54', iris='#6ab0d0', under='#4a4a54'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 60), (4, 30), (18, 4), (50, -6), (82, 4), (96, 30), (90, 60), (84, 48), (16, 48)])),
              L(outline([(60, -2), (84, 8), (96, 34), (88, 56), (78, 36)]), 'shade', 'b', False),
              fringe([(10, 58), (12, 30), (28, 14), (50, 18), (72, 14), (88, 30), (90, 58), (78, 46), (60, 40), (50, 56, 1), (40, 40), (22, 46)]),
              L(outline([(14, 50), (24, 52), (24, 120), (14, 120)]), 'mid', 'f', ln=True), L(outline([(86, 50), (76, 52), (76, 120), (86, 120)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 54), (62, 42), (82, 38), (92, 24), (82, 2), (54, -8), (22, -4), (6, 14), (4, 40), (14, 50), (40, 50)])),
             L(outline([(8, 44), (40, 48), (36, 80), (14, 80)]), 'under'),
             L(outline([(64, 46), (72, 46), (72, 116), (64, 116)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 80), (12, 50), (88, 50), (86, 80), (50, 86)]), 'under'),
             L(outline([(4, 54), (4, 28), (18, 4), (50, -6), (82, 4), (96, 28), (96, 54), (70, 50), (50, 56), (30, 50)])),
             strand([(50, -6), (50, 50)], 'deep', 'b', 1.2),
             L(outline([(8, 54), (16, 54), (16, 112), (8, 112)]), 'mid', 'f', ln=True), L(outline([(92, 54), (84, 54), (84, 112), (92, 112)]), 'mid', 'f', ln=True)],
}

# Fritz Brisk: pelo rubio dorado de pinchos de punta que se levantan hacia un lado, con un pico en medio de la frente y un
# mechón largo que sale de la nuca y ondea hacia atrás; ojos afilados y gesto serio
CHARS['fritz-brisk'] = {
    'body': 'normal', 'pal': pal('#f0c840', '#fcdcbc', iris='#2a2a2a', shade='#d8a030'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (12, 40), (-6, 24, 1), (12, 16), (2, -6, 1), (26, 6), (28, -26, 1), (46, 2), (60, -12, 1), (66, 10), (86, 8, 1), (80, 24), (96, 34, 1),
                         (84, 42), (84, 66), (80, 50), (20, 50)])),
              L(outline([(56, -6), (66, 10), (84, 10), (80, 24), (92, 34), (84, 40), (76, 30)]), 'shade', 'b', False),
              L(outline([(80, 60), (94, 78), (116, 94, 1), (96, 96), (84, 86)]), 'mid', 'f', ln=True),
              fringe([(16, 56), (22, 38), (36, 30), (54, 28), (70, 32), (82, 44), (84, 56), (72, 46), (58, 42), (48, 68, 1), (42, 46), (28, 48)])],
    'side': [L(outline([(56, 56), (62, 46), (80, 44), (90, 30), (84, 14), (94, -2, 1), (72, 2), (58, -24, 1), (46, -2), (20, -6, 1), (24, 10), (0, 14, 1), (12, 26),
                        (-8, 36, 1), (6, 46), (8, 62), (-14, 74), (-40, 86, 1), (-12, 84), (14, 78), (30, 76), (46, 66)])),
             L(outline([(8, 30), (26, 40), (26, 66), (10, 60)]), 'shade', 'b', False),
             fringe([(68, 2), (90, 16), (94, 38), (90, 54, 1), (82, 40), (74, 30)])],
    'back': [L(outline([(16, 78), (12, 40), (-6, 22, 1), (12, 16), (4, -8, 1), (26, 6), (32, -26, 1), (48, 2), (62, -10, 1), (68, 10), (90, 8, 1), (84, 26), (100, 34, 1),
                        (86, 44), (84, 78), (50, 84)])),
             L(outline([(56, 4), (82, 14), (88, 50), (82, 74), (62, 82)]), 'shade', 'b', False),
             L(outline([(48, 60), (20, 72), (-20, 90, 1), (24, 82), (54, 72)]), 'mid', 'f', ln=True)],
}

# Grisley Bear: grandullón de piel clara; melena erizada azul grisáceo oscuro como la de un oso, y por delante una corona
# de pinchos crema que le enmarca la frente; ojos redondos de pupila pequeña y dientes apretados de rabia
CHARS['grisley-bear'] = {
    'body': 'corpulento', 'pal': pal('#344a5a', '#f4dcb4', iris='#2a2a2a', cream='#f2e2c0', cream_d='#d8c49a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': (60, 46), 'face_front': WIDE_FACE},
    'front': messy('front', 18, 14, seed=421, rx=60, ry=50, cy=46, lo=86)
             + [fringe([(12, 76), (6, 56), (14, 46), (10, 26, 1), (26, 34), (30, 14, 1), (42, 30), (50, 10, 1), (58, 30), (70, 14, 1), (74, 34), (90, 26, 1), (86, 46),
                        (94, 56), (88, 76), (80, 60), (72, 52), (60, 54), (50, 46), (40, 54), (28, 52), (20, 60)], 'cream'),
                L(outline([(50, 14), (58, 30), (54, 44)]), 'cream_d', 'f', False),
                L([(30, 66), (42, 70)], OUTC, 'f', False, False, 2.4), L([(70, 66), (58, 70)], OUTC, 'f', False, False, 2.4)]
             + white_eyes(77, 14, 5.4, 4.6, 1.8),
    'side': messy('side', 18, 12, seed=422, rx=56, ry=50, cy=44, nape=96, sweep=-0.3)
            + [fringe([(60, 6), (74, 0, 1), (78, 16), (96, 14, 1), (90, 30), (100, 44, 1), (88, 50), (86, 70), (78, 54), (70, 36)], 'cream')] + side_eye(77),
    'back': messy('back', 18, 14, seed=423, rx=60, ry=50, cy=46, nape=96),
}
