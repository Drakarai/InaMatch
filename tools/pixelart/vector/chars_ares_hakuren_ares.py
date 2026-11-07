"""Instituto Alpino (Ares) (ares-hakuren-ares): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de frente,
perfil y espalda).

Los del Alpino de IE2 y Someoka tienen en Ares el mismo diseño (gorros, orejeras, gafas...) y usan su dibujo de siempre.
Fubuki está rediseñado (pelo lila con dos antenitas, sin bufanda): 'ares:shawn-froste'. En el equipo juega también su
hermano Atsuya (aiden-froste), y los Shiratoya (padre e hija) y Okamine Kanna, que solo salen en Ares."""
from chars import CHARS, L, OUTC, ell, longhair, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 246, 244, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def fur_collar():
    """Cuello de piel blanco de Atsuya (asoma por encima de la camiseta)."""
    return L(outline([(12, 100), (30, 96), (50, 100), (70, 96), (88, 100), (92, 112), (72, 118), (50, 114), (28, 118), (8, 112)]), 'fur', 'f', ln=True)


# Fubuki Shirou (Ares): pelo lila hasta la nuca, abierto en puntas hacia los lados a la altura de las mejillas y más oscuro
# por abajo, dos antenitas en lo alto y un flequillo que cae en diagonal sobre la frente; ojos verde grisáceo
CHARS['ares:shawn-froste'] = {
    'body': 'normal', 'pal': pal('#9c8cd4', '#fbe0c8', iris='#3e6a5e', shade='#6c5c9c', deep='#4e4078'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(42, 4), (30, -12, 1), (46, -6), (50, 2)])), L(outline([(52, 2), (60, -8), (72, -12, 1), (58, 4)])),
              L(outline([(16, 92), (4, 98, 1), (10, 82), (-4, 74, 1), (6, 66), (-6, 52, 1), (8, 46), (10, 24), (24, 6), (44, -2), (56, -2), (76, 6), (90, 24),
                         (94, 46), (108, 52, 1), (96, 64), (106, 74, 1), (92, 82), (98, 98, 1), (84, 92), (84, 66), (16, 66)])),
              L(outline([(6, 60), (16, 66), (16, 90), (4, 96), (8, 80), (-2, 72)]), 'shade', 'b', False),
              L(outline([(94, 60), (84, 66), (84, 90), (96, 96), (92, 80), (102, 72)]), 'shade', 'b', False),
              L(outline([(60, 2), (84, 12), (94, 40), (90, 60), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 44), (24, 22), (46, 12), (70, 16), (86, 34), (88, 64), (82, 52), (78, 66, 1), (72, 44), (62, 34), (52, 42), (40, 60),
                      (32, 76, 1), (30, 56), (24, 66, 1), (18, 54)]),
              L(outline([(58, 18), (78, 26), (86, 46), (72, 38)]), 'shade', 'f', False)],
    'side': [L(outline([(48, -2), (40, -14, 1), (54, -8), (60, -2)])), L(outline([(58, -2), (66, -10), (74, -12, 1), (64, 2)])),
             L(outline([(54, 64), (58, 52), (80, 50), (92, 38), (92, 20), (82, 6), (60, -4), (36, -2), (16, 10), (4, 30), (-12, 50, 1), (2, 56), (-10, 72, 1),
                        (4, 74), (-2, 90, 1), (14, 84), (16, 100, 1), (28, 88), (40, 80), (46, 72)])),
             L(outline([(-6, 54), (2, 56), (-6, 70), (4, 74), (0, 88), (14, 84), (16, 98), (28, 88), (36, 66), (16, 54)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 18), (96, 40), (92, 66, 1), (86, 52), (82, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(42, 4), (30, -12, 1), (46, -6), (50, 2)])), L(outline([(52, 2), (60, -8), (72, -12, 1), (58, 4)])),
             L(outline([(14, 92), (2, 98, 1), (6, 84), (-6, 74, 1), (4, 64), (-8, 52, 1), (6, 46), (10, 22), (26, 4), (50, -2), (74, 4), (90, 22), (94, 46),
                        (108, 52, 1), (96, 64), (106, 74, 1), (94, 84), (98, 98, 1), (84, 92), (72, 100, 1), (62, 92), (50, 104, 1), (38, 92), (28, 100, 1)])),
             L(outline([(4, 56), (96, 56), (98, 96), (84, 92), (72, 100), (62, 92), (50, 104), (38, 92), (28, 100), (14, 92), (2, 96)]), 'shade', 'b', False),
             strand([(30, 30), (40, 50)], 'deep', 'b', 1.0), strand([(66, 24), (58, 48)], 'deep', 'b', 1.0)],
}

# Fubuki Atsuya: el hermano pequeño, pelo naranja en pinchos grandes abiertos hacia todos lados con dos antenitas arriba,
# flequillo de pinchos sobre la frente y cejas fruncidas; ojos verde grisáceo y cuello de piel blanco
CHARS['aiden-froste'] = {
    'body': 'normal', 'pal': pal('#e08a52', '#fbe0c8', iris='#3e6a5e', shade='#b4643a', deep='#8a4a2a', fur='#f2ece0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 86), (-2, 94, 1), (8, 74), (-10, 64, 1), (4, 56), (-12, 40, 1), (8, 34), (2, 10, 1), (22, 18), (30, 2), (26, -14, 1), (40, -2),
                         (50, -6), (58, -16, 1), (62, 0), (76, 4), (98, -2, 1), (88, 20), (110, 30, 1), (96, 42), (108, 58, 1), (94, 64), (104, 80, 1), (90, 82),
                         (96, 96, 1), (84, 90), (84, 66), (16, 66)])),
              L(outline([(60, 0), (86, 10), (96, 40), (92, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 72), (14, 44), (26, 24), (50, 16), (74, 24), (86, 44), (88, 72), (80, 60), (76, 70, 1), (70, 52), (60, 62, 1), (56, 46), (46, 60, 1),
                      (40, 46), (30, 62, 1), (24, 52), (18, 68, 1)]),
              L(outline([(58, 20), (78, 28), (86, 48), (72, 42)]), 'shade', 'f', False), fur_collar()],
    'side': [L(outline([(54, 64), (58, 50), (80, 50), (92, 38), (96, 20), (90, 4), (98, -8, 1), (76, -2), (68, -18, 1), (56, -4), (36, -6), (20, 4), (-8, -2, 1),
                        (6, 16), (-16, 28, 1), (2, 38), (-18, 52, 1), (2, 58), (-12, 74, 1), (6, 76), (-2, 92, 1), (16, 86), (18, 102, 1), (30, 88), (42, 82), (46, 72)])),
             L(outline([(-4, 40), (20, 46), (28, 86), (2, 84)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (98, 40), (94, 66, 1), (86, 50), (82, 62, 1), (76, 42), (66, 30)]),
             L(outline([(40, 100), (60, 96), (84, 100), (88, 112), (60, 116), (38, 112)]), 'fur', 'f', ln=True)],
    'back': [L(outline([(14, 88), (-4, 96, 1), (6, 76), (-12, 64, 1), (2, 56), (-14, 40, 1), (8, 32), (2, 10, 1), (22, 18), (30, 2), (26, -14, 1), (40, -2),
                        (50, -6), (58, -16, 1), (62, 0), (76, 4), (98, -2, 1), (88, 20), (112, 32, 1), (96, 44), (110, 60, 1), (96, 68), (104, 88, 1), (86, 90),
                        (74, 102, 1), (62, 92), (50, 106, 1), (38, 92), (26, 102, 1)])),
             L(outline([(56, 2), (86, 10), (100, 46), (92, 88), (64, 96), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (40, 60), (34, 88)], 'deep', 'b', 1.0), strand([(70, 30), (60, 60), (66, 88)], 'deep', 'b', 1.0), fur_collar()],
}

# Shiratoya Kanbee: el padre de Nae, un señor grandote de cara redonda y papada, con el pelo granate peinado hacia atrás
# en un tupé corto, ojos cerrados y un bigote espeso
_KANBEE_FACE = [(8, 50), (50, 40), (92, 50), (98, 78), (94, 102), (74, 118), (50, 122), (26, 118), (6, 102), (2, 78)]
CHARS['robert-cottontail'] = {
    'body': 'corpulento', 'pal': pal('#8a4a5a', '#eeae78', iris='#2a1e1a', shade='#6a3446', nose='#d8925e'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'none', 'hairline': False, 'face_front': outline(_KANBEE_FACE), 'big_ears': 1, 'ear_out': 6,
             'nose': (50, 80, 3.4)},
    'front': [L(outline([(10, 62), (8, 40), (18, 22), (36, 14), (52, 12), (58, 2), (66, 10), (80, 18), (90, 36), (92, 62), (84, 48), (62, 42), (40, 42),
                         (18, 48)])),
              L(outline([(60, 12), (82, 20), (90, 40), (86, 54), (78, 40)]), 'shade', 'b', False),
              strand([(30, 22), (54, 16)], 'shade', 'b', 1.2), strand([(28, 32), (60, 26)], 'shade', 'b', 1.2),
              L(outline([(28, 92), (38, 85), (50, 89), (62, 85), (72, 92), (66, 97), (57, 93), (50, 95), (43, 93), (34, 97)]), 'mid', 'f', ln=True),
              L(quad((40, 106), (50, 110), (60, 106)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(10, 66), (8, 36), (22, 14), (50, 6), (70, 4), (78, 12), (86, 26), (70, 26), (52, 32), (40, 48), (26, 58), (20, 74)])),
             L(outline([(10, 40), (26, 46), (24, 70), (12, 66)]), 'shade', 'b', False),
             L(outline([(80, 88), (94, 86), (100, 94), (90, 98), (80, 96)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 76), (10, 38), (24, 16), (50, 8), (76, 16), (90, 38), (88, 76), (70, 84), (30, 84)])),
             L(outline([(56, 12), (84, 24), (90, 50), (86, 74), (64, 82)]), 'shade', 'b', False),
             strand([(16, 62), (50, 70), (84, 62)], 'deep', 'b', 1.2)],
}

# Okamine Kanna: melena blanca como una capucha que le enmarca la cara hasta los hombros, flequillo en M y tres adornos
# romboidales azules en lo alto; de perfil, una coleta alta recogida en un lazo hacia atrás; ojos grandes azul grisáceo
_KANNA_GEMS = [L(outline([(50, -16), (58, -6), (50, 4), (42, -6)]), 'gem', 'f', ln=True),
               L(outline([(24, -4), (34, -8), (36, 2), (26, 4)]), 'gem', 'f', ln=True),
               L(outline([(76, -4), (66, -8), (64, 2), (74, 4)]), 'gem', 'f', ln=True)]
CHARS['mila-simmering'] = {
    'body': 'chica', 'pal': pal('#eeeaee', '#fce6d4', iris='#4a5a9e', shade='#c8bcca', deep='#a898ae', gem='#7a9ad0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 112), (6, 80), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (94, 80), (84, 112), (78, 96), (80, 62), (20, 62), (22, 96)])),
              L(outline([(60, 4), (84, 16), (94, 44), (92, 84), (84, 106), (80, 60)]), 'shade', 'b', False),
              fringe([(14, 58), (16, 34), (30, 18), (50, 12), (70, 18), (84, 34), (86, 58), (78, 52), (72, 60, 1), (64, 46), (56, 52), (50, 44), (44, 52),
                      (36, 46), (28, 60, 1), (22, 52)]),
              strand([(20, 66), (18, 104)], 'shade', 'f', 1.0), strand([(80, 66), (82, 104)], 'shade', 'f', 1.0)] + _KANNA_GEMS,
    'side': [L(outline([(22, 10), (6, -6), (-10, 0), (-14, 22), (-4, 38), (6, 26), (14, 8)])),
             L(outline([(-10, 4), (0, 2), (-4, 24), (-10, 26)]), 'shade', 'b', False),
             L(outline([(54, 66), (58, 54), (80, 52), (92, 38), (88, 14), (66, 0), (36, 0), (14, 14), (6, 40), (8, 76), (14, 106), (26, 96), (30, 74),
                        (46, 74)])),
             L(outline([(8, 44), (28, 48), (30, 90), (14, 100)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 16), (94, 40), (92, 60, 1), (84, 48), (76, 38)]),
             L(outline([(36, -14), (44, -6), (36, 2), (28, -6)]), 'gem', 'f', ln=True)],
    'back': [L(outline([(12, 104), (6, 70), (8, 36), (20, 12), (50, 0), (80, 12), (92, 36), (94, 70), (88, 104), (50, 110)])),
             L(outline([(56, 4), (84, 16), (94, 50), (90, 100), (64, 108), (70, 50)]), 'shade', 'b', False),
             strand([(30, 14), (22, 60), (26, 100)], 'deep', 'b', 1.0), strand([(50, 4), (50, 106)], 'deep', 'b', 1.0),
             strand([(70, 14), (78, 60), (74, 100)], 'deep', 'b', 1.0), strand([(14, 60), (50, 70), (86, 60)], 'deep', 'b', 1.0)] + _KANNA_GEMS,
}

# Shiratoya Nae: melena larga rosa y lisa hasta media espalda, con flequillo de mechones; ojos grandes verde azulado
CHARS['bunny-cottontail'] = {
    'body': 'chica', 'pal': pal('#d89aa6', '#fce4d2', iris='#2e9a8c', shade='#b47684', deep='#965a68'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': longhair('front', 120, 4, fringe=66),
    'side': longhair('side', 120, 4),
    'back': longhair('back', 120, 4, ends=5),
}
