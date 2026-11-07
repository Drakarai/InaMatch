"""Bailarines Eternos (orion-eternal-dancers): Uzbekistán en Inazuma Eleven Orion no Kokuin, con sus modelos 3D de
'イナズマイレブン オリオンの刻印' (cada uno tiene una sola forma). Tango (Dost Gales) no es el Tango de Protocol Omega:
va como 'orion-eternal-dancers:tango'."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 248, 240, 255)
GOLD = (226, 178, 52, 255)


def rows(x0, x1, ys, c='deep', z='b', w=0.8):
    """Rayas horizontales (rapados en líneas)."""
    return [strand([(x0, y), ((x0 + x1) / 2, y + 1), (x1, y)], c, z, w) for y in ys]


# Bolero Salimov (Alek Akbar, portero): pelo rosa largo peinado de lado que le tapa el ojo izquierdo (el de la derecha de la
# imagen) y le cae hasta la barbilla; el otro lado y la nuca rapados en gris con rayas; ojos castaños entornados
CHARS['bolero-salimov'] = {
    'body': 'normal', 'pal': pal('#e2708c', '#c8946a', iris='#6a3a22', shave='#9a8c98', shave_d='#6e6270'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(14, 60), (18, 40), (30, 30), (50, 34), (70, 30), (86, 40), (90, 60)]},
    'front': [L(outline([(16, 62), (14, 30), (24, 12), (40, 2), (58, 0), (76, 8), (86, 24), (88, 50), (84, 62)]), 'shave'),
              L(outline([(26, 22), (34, 6), (52, -2), (72, 4), (86, 20), (90, 46), (88, 76), (80, 96), (70, 108, 1), (66, 92), (62, 74), (52, 54), (40, 38),
                         (30, 30)]), 'mid', 'f'),
              L(outline([(70, 10), (86, 22), (90, 50), (86, 80), (74, 102, 1), (74, 78), (78, 46)]), 'shade', 'f', False),
              strand([(36, 14), (50, 34), (60, 58), (66, 84)], 'deep', 'f', 1.0), strand([(56, 6), (70, 30), (76, 64)], 'deep', 'f', 1.0),
              *rows(17, 25, [26, 32, 38, 44, 50, 56], 'shave_d', 'b')],
    'side': [L(outline([(6, 60), (4, 32), (16, 12), (40, 6), (66, 10), (82, 24), (84, 50), (74, 60), (56, 60), (40, 62), (26, 72), (12, 70)]), 'shave'),
             *rows(10, 70, [24, 32, 40, 48, 56], 'shave_d', 'b'),
             L(outline([(2, 34), (6, 12), (24, -6), (52, -10), (78, -2), (92, 14), (96, 40), (96, 68), (100, 102, 1), (90, 86), (86, 62), (84, 40), (72, 26),
                        (50, 20), (24, 24)])),
             L(outline([(70, 0), (90, 14), (96, 44), (98, 92, 1), (90, 60), (86, 36)]), 'shade', 'b', False),
             strand([(30, 2), (60, 6), (84, 22)], 'light', 'b', 1.2)],
    'back': [L(outline([(16, 78), (14, 40), (24, 14), (50, 4), (76, 14), (86, 40), (84, 78), (66, 86), (50, 88), (34, 86)]), 'shave'),
             *rows(18, 82, [36, 44, 52, 60, 68, 76], 'shave_d', 'b'),
             L(outline([(16, 40), (22, 14), (40, 0), (60, 0), (78, 12), (86, 38), (80, 44), (64, 40), (50, 56, 1), (36, 40), (22, 44)])),
             L(outline([(14, 44), (20, 50), (24, 84), (16, 90, 1), (12, 66)])),
             L(outline([(56, 2), (78, 12), (86, 38), (70, 40)]), 'shade', 'b', False)],
}

# Kizomba Zakharov (Ibrahim Abi): piel oscura; trenzas pegadas castaño oscuro arriba (dos filas que se juntan en medio) y una
# trenza larga que le cae por la espalda; los lados rapados con rayas; patillas que bajan como barba por la mandíbula;
# ojos azul grisáceo con rayas negras debajo
CHARS['kizomba-zakharov'] = {
    'body': 'normal', 'pal': pal('#4e3e2a', '#8a5a3c', iris='#8ab0c4', shave='#6a6650', shave_d='#4a4838'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 60), (18, 46), (30, 44), (50, 42), (70, 44), (82, 46), (86, 60)]},
    'front': [L(outline([(16, 64), (14, 36), (20, 22), (80, 22), (86, 36), (84, 64), (78, 50), (22, 50)]), 'shave'),
              *rows(16, 23, [34, 40, 46, 52], 'shave_d'), *rows(77, 84, [34, 40, 46, 52], 'shave_d'),
              L(outline([(20, 38), (18, 18), (26, 6), (38, 0), (48, 2), (50, 6), (52, 2), (62, 0), (74, 6), (82, 18), (80, 38), (66, 34), (50, 32), (34, 34)])),
              strand([(50, 6), (50, 30)], 'deep', 'b', 1.2), strand([(30, 6), (26, 34)], 'deep', 'b', 0.9), strand([(70, 6), (74, 34)], 'deep', 'b', 0.9),
              L(outline([(19, 64), (24, 66), (28, 90), (36, 98), (32, 100), (22, 88)]), 'mid', 'f', False),
              L(outline([(81, 64), (76, 66), (72, 90), (64, 98), (68, 100), (78, 88)]), 'mid', 'f', False),
              L([(30, 80), (27, 86)], OUTC, 'f', False, False, 1.6), L([(70, 80), (73, 86)], OUTC, 'f', False, False, 1.6)],
    'side': [L(rope((14, 24), (-14, 58), (-8, 108), 8), 'mid'),
             *[L(ell(-8 + 2 * (k % 2), 40 + k * 10, 4.4, 5.4), 'shade', 'b', False, True) for k in range(7)],
             L(outline([(4, 56), (4, 30), (14, 14), (40, 6), (66, 8), (80, 18), (82, 38), (74, 44), (60, 48), (48, 58), (34, 66), (14, 70)]), 'shave'),
             *rows(8, 76, [26, 34, 42, 50, 58], 'shave_d'),
             L(outline([(4, 30), (12, 12), (34, 2), (60, 2), (78, 12), (82, 22), (60, 18), (34, 20), (12, 28)])),
             L(outline([(70, 52), (76, 50), (78, 78), (74, 96), (68, 96), (72, 76)]), 'mid', 'f', False)],
    'back': [L(outline([(16, 78), (14, 40), (24, 18), (76, 18), (86, 40), (84, 78), (66, 86), (50, 88), (34, 86)]), 'shave'),
             *rows(16, 84, [34, 42, 50, 58, 66, 74], 'shave_d'),
             L(outline([(16, 32), (22, 10), (36, 0), (50, 2), (64, 0), (78, 10), (84, 32), (66, 28), (50, 26), (34, 28)])),
             L(rope((50, 6), (52, 70), (50, 128), 9), 'mid'),
             *[L(ell(50 + (2 if k % 2 else -2), 14 + k * 11, 4.6, 6), 'shade', 'b', False, True) for k in range(10)]],
}

# Rumba Mansurov (Muhammad Hawk): pelo de pinchos revueltos degradado, morado arriba y rojo abajo, con un mechón que baja por
# la frente; ojos azules con ojeras oscuras y sonrisa de lado
CHARS['rumba-mansurov'] = {
    'body': 'corpulento', 'pal': pal('#c8302e', '#b07850', iris='#4a6aa8', shade='#9a2224', deep='#741a1c', top='#6a5ab0', top_d='#4e4290',
                                     bags='#8a5a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 68), (16, 50), (28, 46), (40, 52), (48, 60), (56, 50), (70, 46), (84, 50), (86, 68)]},
    'front': [L(outline([(16, 70), (8, 54), (10, 30), (16, 10), (24, -2, 1), (34, 4), (42, -10, 1), (52, 0), (60, -6, 1), (68, 2), (80, -4, 1), (82, 12), (92, 30),
                         (94, 54), (84, 70), (80, 50), (20, 50)])),
              L(outline([(10, 30), (16, 10), (24, -2), (34, 4), (42, -10), (52, 0), (60, -6), (68, 2), (80, -4), (82, 12), (90, 24), (80, 20), (70, 16), (60, 22),
                         (48, 14), (36, 20), (24, 16), (14, 24)]), 'top', 'b', False),
              L(outline([(60, 2), (80, -4), (82, 12), (88, 22), (76, 16)]), 'top_d', 'b', False),
              L(outline([(70, 30), (88, 34), (92, 56), (84, 66), (80, 46)]), 'shade', 'b', False),
              L(outline([(40, 40), (46, 36), (56, 40), (50, 62, 1)]), 'mid', 'f'),
              L(outline([(28, 80), (36, 84), (44, 80), (36, 86)]), 'bags', 'f', False), L(outline([(72, 80), (64, 84), (56, 80), (64, 86)]), 'bags', 'f', False)],
    'side': [L(outline([(62, 56), (70, 44), (84, 40), (98, 30, 1), (90, 22), (96, 6, 1), (80, 4), (82, -14, 1), (66, -4), (58, -20, 1), (46, -6), (30, -16, 1), (24, 0),
                        (8, 0, 1), (10, 16), (0, 30, 1), (8, 40), (4, 60, 1), (16, 64), (22, 80), (34, 70), (40, 60), (48, 58), (56, 72), (66, 80, 1), (66, 66)])),
             L(outline([(10, 16), (8, 0), (24, 0), (30, -16), (46, -6), (58, -20), (66, -4), (82, -14), (80, 4), (96, 6), (84, 12), (66, 6), (50, 8), (34, 4), (18, 10)]), 'top', 'b', False),
             L(outline([(4, 40), (24, 46), (38, 60), (22, 78), (10, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 82), (12, 60), (6, 40), (10, 20), (18, 4, 1), (28, 8), (34, -8, 1), (44, 2), (52, -10, 1), (60, 0), (70, -6, 1), (74, 8), (86, 12, 1),
                        (88, 30), (94, 46, 1), (86, 54), (86, 80), (66, 84), (50, 86), (34, 84)])),
             L(outline([(10, 26), (18, 4), (28, 8), (34, -8), (44, 2), (52, -10), (60, 0), (70, -6), (74, 8), (86, 12), (86, 20), (70, 14), (50, 20), (30, 14), (12, 18)]),
               'top', 'b', False),
             L(outline([(56, 30), (86, 30), (88, 76), (66, 82)]), 'shade', 'b', False)],
}

# Merengue Muratov (Majid Azer): casco de metal gris con forma de calavera que le tapa toda la cabeza: un agujero negro en
# el ojo derecho de la imagen por el que asoma un ojo verde, una lente azul cian en el otro, un agujero triangular de nariz
# y la placa de la mandíbula; por debajo le cae el pelo largo color caqui hasta los hombros
HELM = (170, 170, 176, 255)
HELM_D = (128, 126, 134, 255)
CHARS['merengue-muratov'] = {
    'body': 'delgado', 'pal': pal('#a49a4c', '#f0c8a0', iris='#7a9a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'ears': False, 'hairline': False},
    'front': [L(outline([(10, 74), (2, 100), (2, 124), (16, 124), (22, 96), (24, 78)])), L(outline([(90, 74), (98, 100), (98, 124), (84, 124), (78, 96), (76, 78)])),
              strand([(10, 84), (8, 118)], 'deep', 'b', 0.8), strand([(90, 84), (92, 118)], 'deep', 'b', 0.8),
              L(outline([(10, 72), (6, 30), (14, 4), (34, -6), (66, -6), (86, 4), (94, 30), (90, 72), (72, 74), (70, 88), (30, 88), (28, 74)]), HELM, 'f'),
              L(outline([(66, -4), (86, 6), (94, 30), (90, 70), (78, 72), (82, 34)]), HELM_D, 'f', False),
              L([(10, 30), (22, 20), (30, 6)], OUTC, 'f', False, False, 1.0), L([(90, 30), (78, 20), (70, 6)], OUTC, 'f', False, False, 1.0),
              L([(32, 74), (32, 88)], OUTC, 'f', False, False, 1.0), L([(50, 74), (50, 88)], OUTC, 'f', False, False, 1.0), L([(68, 74), (68, 88)], OUTC, 'f', False, False, 1.0),
              L([(28, 74), (72, 74)], OUTC, 'f', False, False, 1.0),
              L(ell(66, 44, 12, 12), OUTC, 'f', False),
              L(outline([(58, 46), (74, 44), (72, 50), (60, 50)]), (240, 240, 230, 255), 'f', False), L(ell(66, 47, 2.6, 2.6), (122, 154, 58, 255), 'f', False),
              L([(57, 44), (75, 42)], (60, 60, 60, 255), 'f', False, False, 1.4),
              L(ell(30, 42, 8, 8), HELM_D, 'f', False, True), L(ell(30, 42, 5.2, 5.2), (64, 196, 228, 255), 'f', False, True),
              L([(50, 54), (44, 66), (56, 66)], OUTC, 'f', False)],
    'side': [L(outline([(22, 60), (6, 90), (-14, 120), (2, 124), (20, 100), (40, 76)])), strand([(14, 76), (-4, 112)], 'deep', 'b', 0.8),
             L(outline([(8, 60), (4, 30), (16, 6), (40, -6), (70, -4), (90, 10), (98, 34), (96, 60), (92, 76), (90, 88), (70, 88), (66, 72), (40, 70), (20, 70)]), HELM, 'f'),
             L(outline([(6, 34), (14, 10), (36, -4), (30, 30), (10, 60)]), HELM_D, 'f', False),
             L([(40, -4), (44, 30), (40, 70)], OUTC, 'f', False, False, 1.0), L([(10, 40), (44, 30), (96, 34)], OUTC, 'f', False, False, 1.0),
             L([(70, 72), (92, 74)], OUTC, 'f', False, False, 1.0), L([(80, 72), (80, 88)], OUTC, 'f', False, False, 1.0),
             L(ell(92, 46, 4, 6), HELM_D, 'f', False, True), L(ell(93, 46, 2.4, 3.6), (64, 196, 228, 255), 'f', False)],
    'back': [L(outline([(6, 60), (-6, 100), (-10, 126), (110, 126), (106, 100), (94, 60), (50, 70)])),
             *[strand([(x, 76), (x + (x - 50) * 0.2, 122)], 'deep', 'b', 0.9) for x in (14, 30, 70, 86)],
             L(outline([(10, 72), (6, 30), (14, 4), (34, -6), (66, -6), (86, 4), (94, 30), (90, 72), (50, 76)]), HELM, 'b'),
             L(outline([(56, -6), (86, 4), (94, 30), (90, 70), (60, 74)]), HELM_D, 'b', False),
             L([(10, 26), (30, 40), (70, 40), (90, 26)], OUTC, 'b', False, False, 1.0), L([(28, -2), (30, 40)], OUTC, 'b', False, False, 1.0),
             L([(72, -2), (70, 40)], OUTC, 'b', False, False, 1.0)],
}

# Chacha Goncharov (Zafar Gin): cresta azul oscuro con un pincho muy alto en medio que le baja en pico hasta la frente; los
# lados gris claro de pinchitos de sierra; colmillo, ojos castaño anaranjado y coloretes
CHARS['chacha-goncharov'] = {
    'body': 'bajito', 'pal': pal('#2c5490', '#f6d0a8', iris='#b86a26', shade='#203e6e', deep='#162c50', grey='#a4aab4', grey_d='#7e8490'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 66), (16, 50), (30, 42), (50, 44), (70, 42), (84, 50), (86, 66)]},
    'front': [L(outline([(16, 70), (10, 64, 1), (14, 58), (6, 52, 1), (12, 46), (4, 38, 1), (12, 32), (6, 22, 1), (16, 18), (14, 8, 1), (26, 6), (50, 0), (74, 6),
                         (86, 8, 1), (84, 18), (94, 22, 1), (88, 32), (96, 38, 1), (88, 46), (94, 52, 1), (86, 58), (90, 64, 1), (84, 70), (80, 50), (20, 50)]), 'grey'),
              L(outline([(26, 46), (24, 22), (30, 6), (40, -4, 1), (46, -4), (50, -36, 1), (56, -6), (64, -10, 1), (66, 0), (74, 8), (76, 24), (72, 44), (62, 30),
                         (54, 46), (52, 58, 1), (46, 44), (36, 30)])),
              L(outline([(56, -6), (64, -10), (66, 0), (74, 8), (76, 24), (72, 42), (62, 28)]), 'shade', 'b', False),
              L(outline([(40, 36), (46, 34), (54, 40), (52, 58, 1), (46, 46)]), 'mid', 'f'),
              L(ell(30, 86, 4, 2.6), (240, 150, 120, 255), 'f', False), L(ell(70, 86, 4, 2.6), (240, 150, 120, 255), 'f', False),
              L([(55, 93), (54, 97), (53, 93)], WHITE, 'f', False)],
    'side': [L(outline([(10, 64), (4, 40), (14, 14), (40, 6), (66, 10), (80, 24), (82, 42), (70, 50), (56, 58), (48, 58), (36, 70), (20, 72)]), 'grey'),
             L(outline([(6, 40), (14, 22), (30, 20), (26, 40), (14, 58)]), 'grey_d', 'b', False),
             L(outline([(84, 44), (78, 30), (66, 26), (44, 22), (24, 28), (10, 40), (-14, 52, 1), (2, 60), (-12, 76, 1), (6, 76), (-2, 96, 1), (14, 84), (20, 72),
                        (8, 66), (2, 50), (6, 32), (-6, 16, 1), (12, 14), (8, -4, 1), (26, 2), (34, -12, 1), (46, 0), (66, -38, 1), (64, -6), (82, -8, 1), (76, 6),
                        (96, 0, 1), (84, 16), (90, 30)])),
             L(outline([(2, 50), (6, 32), (12, 14), (26, 2), (30, 14), (12, 40), (8, 66)]), 'shade', 'b', False),
             L(ell(76, 84, 3.6, 2.4), (240, 150, 120, 255), 'f', False)],
    'back': [L(outline([(18, 80), (12, 70, 1), (14, 62), (6, 56, 1), (12, 48), (4, 40, 1), (12, 32), (6, 22, 1), (16, 16), (14, 6, 1), (30, 2), (50, -2), (70, 2),
                        (86, 6, 1), (84, 16), (94, 22, 1), (88, 32), (96, 40, 1), (88, 48), (94, 56, 1), (86, 62), (88, 70, 1), (82, 80), (50, 86)]), 'grey'),
             L(outline([(24, 4), (40, -6, 1), (44, -2), (50, -34, 1), (56, -4), (64, -8, 1), (76, 6), (74, 24), (80, 34, 1), (68, 38), (72, 54, 1), (62, 58), (64, 76, 1),
                        (56, 82), (56, 96), (50, 110, 1), (44, 96), (44, 82), (36, 76, 1), (38, 58), (28, 54, 1), (32, 38), (20, 34, 1), (26, 24)])),
             L(outline([(52, -4), (64, -8), (76, 6), (74, 24), (68, 38), (62, 58), (56, 96), (52, 60)]), 'shade', 'b', False)],
}

# Hulan Nazarova (Kumush Ize): pelo castaño muy oscuro con la raya en medio, liso hasta la mandíbula, con dos moños a los
# lados atados con aros dorados y las puntas de pincho; dos lunares en la frente, ojos naranjas grandes con pestañas y coloretes
CHARS['hulan-nazarova'] = {
    'body': 'chica', 'pal': pal('#3e3630', '#f6d4ae', iris='#c4602a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(16, 96), (20, 66), (30, 50), (44, 42), (50, 38), (56, 42), (70, 50), (80, 66), (84, 96)]},
    'front': [L(outline([(-8, 70), (-2, 66, 1), (8, 68), (18, 76), (16, 90), (6, 94), (-2, 98, 1), (0, 86), (-8, 82, 1)])),
              L(outline([(108, 70), (102, 66, 1), (92, 68), (82, 76), (84, 90), (94, 94), (102, 98, 1), (100, 86), (108, 82, 1)])),
              L(outline([(14, 102), (12, 60), (16, 30), (30, 12), (50, 6), (70, 12), (84, 30), (88, 60), (86, 102), (78, 100), (80, 60), (20, 60), (22, 100)])),
              L(outline([(56, 8), (74, 14), (86, 34), (88, 60), (78, 40)]), 'shade', 'b', False), strand([(50, 8), (50, 38)], 'deep', 'b', 1.0),
              L(ell(13, 79, 2.4, 6), GOLD, 'f', False, True), L(ell(87, 79, 2.4, 6), GOLD, 'f', False, True),
              L(ell(44, 58, 2.2, 2.2), (78, 60, 50, 255), 'f', False), L(ell(56, 58, 2.2, 2.2), (78, 60, 50, 255), 'f', False),
              L(ell(30, 86, 3.6, 2.4), (246, 160, 120, 255), 'f', False), L(ell(70, 86, 3.6, 2.4), (246, 160, 120, 255), 'f', False)],
    'side': [L(outline([(70, 62), (78, 44), (80, 24), (66, 8), (44, 4), (20, 10), (6, 30), (4, 56), (10, 74), (8, 96, 1), (18, 84), (30, 74), (40, 62), (54, 58)])),
             L(outline([(14, 70), (-6, 66, 1), (-22, 74, 1), (-10, 80), (-20, 92, 1), (-4, 92), (2, 104, 1), (8, 90), (20, 86)])),
             L(ell(12, 78, 3, 7), GOLD, 'b', False, True),
             L(outline([(60, 58), (68, 62), (70, 98, 1), (62, 84)]), 'mid', 'f'),
             L(outline([(6, 34), (20, 14), (30, 30), (14, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(-12, 70), (-4, 64, 1), (8, 70), (20, 76), (18, 90), (6, 94), (-4, 100, 1), (-2, 88), (-14, 84, 1)])),
             L(outline([(112, 70), (104, 64, 1), (92, 70), (80, 76), (82, 90), (94, 94), (104, 100, 1), (102, 88), (114, 84, 1)])),
             L(outline([(16, 98), (12, 60), (16, 30), (30, 10), (50, 4), (70, 10), (84, 30), (88, 60), (84, 98), (66, 86), (50, 88), (34, 86)])),
             L(outline([(54, 6), (72, 12), (86, 34), (86, 90), (64, 84)]), 'shade', 'b', False), strand([(50, 6), (50, 40)], 'deep', 'b', 1.0),
             L(ell(18, 82, 2.6, 6.4), GOLD, 'b', False, True), L(ell(82, 82, 2.6, 6.4), GOLD, 'b', False, True)],
}

# Polkan Ismailov (Sarybek Nahar): afro enorme granate oscuro con una cinta rosa grisácea en la frente y el pelo rizado que le
# cae largo por los lados y la espalda; pintura blanca en rayos sobre los ojos, ojos rojos afilados, nariz ancha y sonrisa
CHARS['polkan-ismailov'] = {
    'body': 'normal', 'pal': pal('#5a3042', '#c89060', iris='#b02a24', band='#d4b4b4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 60), (20, 56), (50, 54), (80, 56), (86, 60)],
             'nose': (50, 86, 4)},
    'front': [L(bumpy(10, 96, 10, 22, 6, 0.12)), L(bumpy(90, 96, 10, 22, 6, 0.12, 0.5)),
              L(bumpy(50, 26, 50, 38, 14, 0.09)), L(outline([(60, -8), (90, 8), (100, 34), (92, 60), (80, 40)]), 'shade', 'b', False),
              L(bumpy(28, 8, 10, 8, 5, 0.1), 'light', 'b', False), strand([(30, 30), (40, 40)], 'deep', 'b', 1.0), strand([(70, 28), (60, 40)], 'deep', 'b', 1.0),
              L(quad((10, 56), (50, 46), (90, 56)) + quad((90, 60), (50, 50), (10, 60)), 'band', 'f'),
              L(outline([(26, 62), (34, 64), (40, 92), (36, 90)]), WHITE, 'f', False), L(outline([(74, 62), (66, 64), (60, 92), (64, 90)]), WHITE, 'f', False)],
    'side': [L(bumpy(10, 80, 18, 32, 7, 0.12)), L(bumpy(46, 16, 54, 34, 12, 0.08)),
             L(outline([(4, 40), (30, 44), (36, 70), (20, 106), (0, 100)]), 'shade', 'b', False),
             L(quad((24, 52), (60, 30), (96, 34)) + quad((96, 38), (60, 34), (26, 56)), 'band', 'f'),
             L(outline([(80, 60), (86, 62), (84, 80), (82, 78)]), WHITE, 'f', False)],
    'back': [L(bumpy(50, 92, 36, 24, 9, 0.1)), L(bumpy(50, 30, 50, 38, 14, 0.09)),
             L(outline([(56, 0), (88, 14), (98, 44), (86, 110), (60, 112)]), 'shade', 'b', False),
             L(quad((8, 70), (50, 76), (92, 70)) + quad((92, 74), (50, 80), (8, 74)), 'band', 'b')],
}

# Jazzar Belikov (Farhad Gilik): pelo azul violeta enorme en pinchos hacia fuera, que le baja por la nuca hasta los hombros;
# ojos redondos amarillos de loco, sonrisa enseñando los dientes y pintura roja en las mejillas
CHARS['jazzar-belikov'] = {
    'body': 'normal', 'pal': pal('#4a46a8', '#e2a476', iris='#d8d84a', shade='#38348a', deep='#28266a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(14, 64), (18, 50), (32, 46), (44, 50), (50, 58), (56, 48), (70, 46), (84, 50), (86, 64)]},
    'front': [L(outline([(18, 100), (10, 92, 1), (14, 84), (2, 78, 1), (12, 70), (-6, 62, 1), (8, 54), (-12, 44, 1), (8, 38), (2, 24, 1), (16, 22), (12, 6, 1), (28, 10),
                         (36, -2, 1), (44, 8), (56, -8, 1), (62, 6), (78, 2, 1), (76, 14), (94, 18, 1), (88, 28), (108, 40, 1), (90, 46), (100, 56, 1), (88, 62),
                         (96, 72, 1), (86, 76), (92, 90, 1), (82, 92), (80, 60), (20, 60)])),
              L(outline([(62, 6), (78, 2), (76, 14), (94, 18), (88, 28), (108, 40), (90, 46), (82, 36), (70, 24)]), 'shade', 'b', False),
              L(outline([(44, 40), (52, 36), (56, 44), (48, 62, 1)]), 'mid', 'f'),
              L([(26, 84), (28, 92)], (210, 60, 60, 255), 'f', False, False, 1.6), L([(32, 84), (33, 92)], (210, 60, 60, 255), 'f', False, False, 1.6),
              L([(74, 84), (72, 92)], (210, 60, 60, 255), 'f', False, False, 1.6), L([(68, 84), (67, 92)], (210, 60, 60, 255), 'f', False, False, 1.6),
              L([(36, 64), (36, 70)], (210, 60, 60, 255), 'f', False, False, 1.4), L([(64, 64), (64, 70)], (210, 60, 60, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(60, 54), (68, 42), (84, 38), (100, 26, 1), (88, 20), (98, 4, 1), (80, 4), (86, -14, 1), (64, -4), (58, -22, 1), (44, -6), (24, -16, 1), (20, 2),
                        (0, -4, 1), (4, 14), (-14, 22, 1), (2, 32), (-18, 46, 1), (0, 52), (-16, 66, 1), (2, 70), (-10, 86, 1), (8, 88), (-2, 104, 1), (16, 98),
                        (24, 82), (36, 70), (44, 60), (52, 58)])),
             L(outline([(0, 52), (20, 40), (36, 70), (16, 98), (8, 88)]), 'shade', 'b', False),
             L(outline([(84, 38), (90, 30), (98, 34, 1), (90, 40)]), 'mid', 'f'),
             L([(78, 80), (78, 86)], (210, 60, 60, 255), 'f', False, False, 1.6)],
    'back': [L(outline([(26, 118), (20, 104, 1), (30, 96), (14, 86, 1), (16, 72), (0, 66, 1), (10, 56), (-10, 44, 1), (8, 36), (0, 20, 1), (18, 20), (16, 4, 1),
                        (32, 10), (42, -10, 1), (50, 6), (66, -2, 1), (68, 12), (86, 10, 1), (84, 24), (106, 34, 1), (90, 44), (108, 56, 1), (88, 62), (96, 74, 1),
                        (84, 76), (88, 92, 1), (70, 96), (78, 108, 1), (60, 104), (50, 120, 1), (40, 106)])),
             L(outline([(56, 6), (66, -2), (68, 12), (86, 10), (84, 24), (106, 34), (90, 44), (108, 56), (88, 62), (84, 76), (70, 96), (60, 70)]), 'shade', 'b', False)],
}

# Limbo Zakharov (Mo'habbot Zark): gorro morado con una banda de triángulos amarillo oliva y gris en la frente y una tela
# morada larga que le cae por detrás hasta los hombros; pintura gris oscura en curva bajo los ojos, ojos amarillos de rendija
# y una sonrisa ancha de labios rojos
CHARS['limbo-zakharov'] = {
    'body': 'normal', 'pal': pal('#6c3c9c', '#f0b888', iris='#c8b830', shade='#552c80', deep='#3e1e60', band_y='#b0aa44', band_g='#6e6a54'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 40), (-6, 70), (-22, 100), (-30, 124), (14, 124), (20, 100), (22, 60)])),
              L(outline([(84, 40), (106, 70), (122, 100), (130, 124), (86, 124), (80, 100), (78, 60)])),
              L(outline([(-20, 104), (-6, 90), (0, 124), (-28, 124)]), 'shade', 'b', False), L(outline([(120, 104), (106, 90), (100, 124), (128, 124)]), 'shade', 'b', False),
              L(outline([(14, 56), (12, 30), (22, 10), (38, 0), (62, 0), (78, 10), (88, 30), (86, 56), (50, 54)]), 'mid', 'f'),
              L(outline([(14, 56), (13, 34), (50, 30), (87, 34), (86, 56), (50, 54)]), 'band_g', 'f'),
              *[L([(x - 9, 55), (x, 33), (x + 9, 55)], 'band_y', 'f', False) for x in (22, 50, 78)],
              L(outline([(60, 2), (78, 10), (88, 30), (66, 32)]), 'shade', 'f', False),
              L(quad((32, 82), (26, 92), (30, 104)), (90, 86, 84, 255), 'f', False, False, 2.4), L(quad((68, 82), (74, 92), (70, 104)), (90, 86, 84, 255), 'f', False, False, 2.4),
              L(quad((44, 64), (40, 72), (36, 76)), (90, 86, 84, 255), 'f', False, False, 2.0), L(quad((56, 64), (60, 72), (64, 76)), (90, 86, 84, 255), 'f', False, False, 2.0)],
    'side': [L(outline([(20, 30), (0, 60), (-20, 100), (-26, 124), (10, 124), (12, 96), (30, 66)])),
             L(outline([(8, 50), (6, 26), (20, 8), (44, -2), (70, 2), (86, 16), (88, 44), (60, 46), (34, 50)]), 'mid', 'f'),
             L(outline([(8, 50), (8, 32), (40, 24), (88, 28), (88, 46), (60, 48), (34, 52)]), 'band_g', 'f'),
             *[L([(x - 9, 50), (x, 28), (x + 9, 50)], 'band_y', 'f', False) for x in (30, 58, 82)],
             L(outline([(-4, 70), (10, 64), (2, 110), (-16, 116)]), 'shade', 'b', False),
             L(quad((76, 82), (74, 92), (78, 102)), (90, 86, 84, 255), 'f', False, False, 2.4)],
    'back': [L(outline([(12, 56), (-14, 90), (-28, 126), (128, 126), (114, 90), (88, 56), (50, 60)])),
             L(outline([(10, 80), (40, 94), (60, 92), (90, 82), (100, 110), (0, 112)]), 'shade', 'b', False),
             L(outline([(14, 60), (12, 30), (22, 10), (38, 0), (62, 0), (78, 10), (88, 30), (86, 60), (50, 62)]), 'mid'),
             L(outline([(14, 60), (13, 36), (50, 34), (87, 36), (86, 60), (50, 62)]), 'band_g'),
             *[L([(x + 9, 37), (x, 59), (x - 9, 37)], 'band_y', 'b', False) for x in (32, 50, 68)],
             L(outline([(58, 2), (78, 10), (88, 34), (64, 34)]), 'shade', 'b', False)],
}

# Samba Sokolov (Onaxon Ims): pelo rojo largo peinado de lado que le tapa el ojo izquierdo (derecha de la imagen) y le cae
# por la espalda; el otro lado rapado castaño; ojo azul
CHARS['samba-sokolov'] = {
    'body': 'normal', 'pal': pal('#b4302a', '#c08a5e', iris='#3a8ac8', shave='#6a5242'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 60), (18, 40), (30, 30), (50, 34), (70, 30), (86, 40), (90, 60)]},
    'front': [L(outline([(82, 120), (84, 96), (90, 90), (94, 120)])),
              L(outline([(16, 62), (14, 30), (24, 12), (40, 2), (58, 0), (76, 8), (86, 24), (88, 50), (84, 62)]), 'shave'),
              L(outline([(28, 22), (34, 6), (52, -4), (72, 2), (86, 18), (92, 44), (90, 76), (88, 104), (84, 120, 1), (80, 100), (74, 92, 1), (66, 76), (58, 58),
                         (46, 40), (34, 30)]), 'mid', 'f'),
              L(outline([(70, 8), (86, 20), (92, 50), (90, 90), (84, 110, 1), (80, 80), (80, 46)]), 'shade', 'f', False),
              strand([(38, 12), (54, 34), (64, 60), (72, 84)], 'deep', 'f', 1.0), L(outline([(52, 6), (64, 6), (60, 12), (50, 12)]), 'light', 'f', False)],
    'side': [L(outline([(10, 40), (2, 80), (-2, 120), (40, 124), (30, 100), (24, 76), (20, 60)])),
             strand([(6, 70), (4, 116)], 'deep', 'b', 0.9), strand([(16, 80), (18, 118)], 'deep', 'b', 0.9),
             L(outline([(6, 60), (4, 32), (16, 12), (40, 6), (66, 10), (82, 24), (84, 50), (74, 58), (56, 58), (40, 62), (26, 72), (12, 70)]), 'shave'),
             L(outline([(4, 60), (2, 30), (12, 8), (36, -4), (62, -6), (60, -12), (74, -8), (88, 8), (94, 32), (90, 54), (84, 40), (70, 18), (40, 14), (20, 22),
                        (10, 44)])),
             L(outline([(70, -6), (88, 8), (94, 32), (88, 48), (80, 24)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 120), (12, 80), (12, 40), (22, 14), (40, 2), (60, 2), (78, 14), (88, 40), (88, 80), (92, 122), (70, 116), (50, 124), (30, 118)])),
             L(outline([(78, 30), (88, 40), (88, 80), (82, 84), (80, 50)]), 'shave', 'b', False),
             L(outline([(54, 4), (76, 14), (80, 60), (72, 118), (56, 110)]), 'shade', 'b', False),
             *[strand([(x, 70), (x + 2, 118)], 'deep', 'b', 0.9) for x in (26, 40, 62)]],
}

# Tango (Dost Gales): pelo azul marino casi negro peinado hacia atrás en una coleta altísima con una raya blanca de la frente a
# la punta y un aro dorado; pico en la frente y dos mechones largos que le enmarcan la cara hasta la barbilla con adornos
# dorados en las puntas; ojos verdes afilados, cejas fruncidas y dos rayas rojas en cada mejilla
CHARS['orion-eternal-dancers:tango'] = {
    'body': 'delgado', 'pal': pal('#2c2a4a', '#f4c8a0', iris='#4a8a2a', shade='#1e1c36', deep='#141228', light='#4a4870', streak='#e8e8ee'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(14, 70), (18, 50), (30, 42), (50, 52), (70, 42), (82, 50), (86, 70)]},
    'front': [L(outline([(14, 112), (12, 60), (16, 30), (30, 10), (44, -4), (50, -12), (56, -4), (70, 10), (84, 30), (88, 60), (86, 112), (80, 110), (80, 70),
                         (72, 50), (50, 54, 1), (28, 50), (20, 70), (20, 110)])),
              L(outline([(56, -4), (70, 10), (84, 30), (88, 60), (86, 110), (82, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(46, -10), (54, -10), (54, 44), (50, 52, 1), (46, 44)]), 'streak', 'b', False),
              L([(43, -4), (57, -4)], GOLD, 'b', False, False, 2.4),
              L(outline([(16, 108), (22, 108), (21, 118), (17, 118)]), GOLD, 'f', False, True), L(outline([(84, 108), (78, 108), (79, 118), (83, 118)]), GOLD, 'f', False, True),
              L([(30, 86), (38, 86)], (196, 70, 60, 255), 'f', False, False, 1.6), L([(30, 90), (38, 90)], (196, 70, 60, 255), 'f', False, False, 1.6),
              L([(62, 86), (70, 86)], (196, 70, 60, 255), 'f', False, False, 1.6), L([(62, 90), (70, 90)], (196, 70, 60, 255), 'f', False, False, 1.6)],
    'side': [L(outline([(54, -8), (40, -24), (20, -20), (2, 10), (-14, 60), (-22, 120), (-8, 122), (6, 70), (24, 20), (46, 0)])),
             L(outline([(40, -24), (20, -20), (2, 10), (-14, 60), (-18, 90), (-6, 50), (14, 6)]), 'streak', 'b', False),
             L(outline([(66, 54), (70, 40), (84, 34), (88, 18), (76, 2), (56, -8), (34, 0), (18, 16), (12, 38), (16, 60), (34, 62), (44, 58), (54, 56)])),
             L(outline([(56, -8), (76, 2), (88, 18), (84, 30), (66, 10)]), 'light', 'b', False),
             L([(52, -12), (58, -4)], GOLD, 'b', False, False, 3.0),
             L(outline([(54, 56), (60, 58), (62, 104), (56, 104)]), 'mid', 'f'), L(outline([(56, 104), (62, 104), (61, 114), (57, 114)]), GOLD, 'f', False, True),
             L([(80, 86), (86, 86)], (196, 70, 60, 255), 'f', False, False, 1.6)],
    'back': [L(outline([(10, 124), (14, 70), (18, 34), (30, 10), (42, -8), (50, -12), (58, -8), (70, 10), (82, 34), (86, 70), (90, 124), (50, 128)])),
             L(outline([(58, -8), (70, 10), (82, 34), (86, 70), (90, 124), (66, 124), (62, 60)]), 'shade', 'b', False),
             L(outline([(46, -10), (54, -10), (58, 40), (62, 124), (52, 124), (48, 40)]), 'streak', 'b', False),
             L([(42, -6), (58, -6)], GOLD, 'b', False, False, 2.4)],
}

# Cancan Popov (Norkul Bugen): piel oscura; melena corta gris azulado claro con dos puntas arriba como orejas de gato y mechas
# blancas en el flequillo; cejas blancas pobladas, ojos negros y ceño serio
CHARS['cancan-popov'] = {
    'body': 'bajito', 'pal': pal('#aebccb', '#7a5038', iris='#1e1a1c', shade='#8a94a4', deep='#6a7484', light='#eef2f6'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 78), (18, 56), (30, 46), (44, 50), (50, 42), (56, 50), (70, 46), (82, 56), (86, 78)]},
    'front': [L(outline([(14, 82), (10, 56), (12, 34), (4, 16, 1), (22, 22), (36, 14), (50, 12), (64, 14), (78, 22), (96, 16, 1), (88, 34), (90, 56), (86, 82),
                         (80, 70), (20, 70)])),
              L(outline([(60, 14), (78, 22), (96, 16), (88, 34), (90, 56), (86, 80), (80, 50), (70, 28)]), 'shade', 'b', False),
              L(outline([(30, 50), (24, 40), (36, 44), (34, 34), (40, 46)]), 'light', 'b', False), L(outline([(70, 50), (76, 40), (64, 44), (66, 34), (60, 46)]), 'light', 'b', False),
              L(quad((28, 64), (34, 60), (42, 64)), 'light', 'f', False, False, 3.0), L(quad((72, 64), (66, 60), (58, 64)), 'light', 'f', False, False, 3.0)],
    'side': [L(outline([(62, 54), (70, 44), (84, 40), (86, 24), (70, 10), (40, 4), (30, -4, 1), (24, 8), (12, 18), (4, 40), (6, 64), (14, 80), (24, 78), (28, 64),
                        (40, 58), (52, 56)])),
             L(outline([(4, 40), (12, 20), (24, 30), (28, 64), (14, 78), (6, 64)]), 'shade', 'b', False),
             L(outline([(56, 44), (70, 34), (68, 44), (82, 40), (64, 54)]), 'light', 'b', False),
             L(quad((72, 64), (78, 60), (86, 64)), 'light', 'f', False, False, 3.0)],
    'back': [L(outline([(14, 82), (10, 56), (12, 34), (4, 14, 1), (22, 20), (36, 12), (50, 10), (64, 12), (78, 20), (96, 14, 1), (88, 34), (90, 56), (86, 82),
                        (66, 88), (50, 90), (34, 88)])),
             L(outline([(14, 60), (30, 54), (50, 64), (70, 54), (88, 50), (86, 82), (66, 88), (50, 90), (34, 88), (14, 82)]), 'shade', 'b', False)],
}

# Ballet Burkhanov (Adam Sanchi): un viejo de pelo y barba blanco crema enormes, con el pelo abierto a los lados en dos
# puntas como cuernos; cejas pobladas, bigote y ojos amarillos de pupila pequeña
CHARS['ballet-burkhanov'] = {
    'body': 'normal', 'pal': pal('#ebe3cc', '#e8a878', iris='#2a2420', shade='#c8bea4', deep='#a89e86'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'mouth_y': 96, 'hairline': [(14, 60), (20, 50), (40, 46), (50, 52), (60, 46), (80, 50), (86, 60)]},
    'front': [L(outline([(14, 70), (12, 50), (2, 32, 1), (14, 26), (24, 12), (50, 6), (76, 12), (86, 26), (98, 32, 1), (88, 50), (86, 70), (80, 56), (20, 56)])),
              L(outline([(60, 8), (76, 12), (86, 26), (98, 32), (88, 50), (86, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(14, 70), (18, 86), (14, 104), (24, 118), (40, 122), (50, 128, 1), (60, 122), (76, 118), (86, 104), (82, 86), (86, 70), (76, 80), (66, 88),
                         (50, 86), (34, 88), (24, 80)]), 'mid', 'f'),
              L(outline([(60, 90), (76, 82), (86, 72), (84, 104), (70, 118), (60, 122)]), 'shade', 'f', False),
              L(outline([(28, 92), (40, 84), (50, 88), (60, 84), (72, 92), (62, 94), (50, 92), (38, 94)]), 'mid', 'f', True, True),
              strand([(40, 104), (44, 118)], 'deep', 'f', 0.9), strand([(60, 104), (56, 118)], 'deep', 'f', 0.9),
              L(outline([(24, 66), (36, 60), (46, 66), (36, 66)]), 'mid', 'f', True, True), L(outline([(76, 66), (64, 60), (54, 66), (64, 66)]), 'mid', 'f', True, True)],
    'side': [L(outline([(70, 56), (78, 42), (80, 26), (66, 12), (40, 8), (20, 14), (-8, 24, 1), (6, 40), (8, 64), (14, 86), (30, 92), (40, 80), (44, 62), (56, 58)])),
             L(outline([(-8, 24), (20, 30), (30, 60), (14, 86), (6, 40)]), 'shade', 'b', False),
             L(outline([(54, 80), (70, 84), (86, 92), (80, 106), (64, 124, 1), (58, 106)]), 'mid', 'f'),
             L(outline([(70, 88), (84, 86), (88, 92), (76, 94)]), 'mid', 'f', True, True), L(outline([(72, 62), (84, 60), (86, 66), (76, 66)]), 'mid', 'f', True, True)],
    'back': [L(outline([(14, 96), (12, 50), (0, 32, 1), (14, 26), (24, 12), (50, 4), (76, 12), (86, 26), (100, 32, 1), (88, 50), (86, 96), (66, 102), (50, 104),
                        (34, 102)])),
             L(outline([(18, 34), (30, 44), (50, 40), (70, 44), (82, 34), (84, 70), (50, 76), (16, 70)]), 'shade', 'b', False)],
}

# Carrie Ogrova (Sabine Nojima): un afro enorme de rizos verde oliva con rizos que le caen por la frente; sombra de ojos azul,
# ojos naranjas, aros dorados en las orejas y media sonrisa
CHARS['carrie-ogrova'] = {
    'body': 'chica', 'pal': pal('#8c8a32', '#e8b080', iris='#c47a1e', shade='#6a6824', deep='#4e4c1a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(14, 76), (18, 60), (30, 52), (40, 58), (50, 50), (60, 58), (70, 52), (82, 60), (86, 76)]},
    'front': [L(bumpy(50, 50, 52, 50, 14, 0.09)), L(outline([(62, 4), (92, 22), (102, 54), (92, 92), (80, 60)]), 'shade', 'b', False),
              L(bumpy(28, 16, 10, 8, 5, 0.1), 'light', 'b', False),
              L(outline([(30, 50), (36, 40), (44, 46), (50, 38), (56, 46), (64, 40), (70, 50), (60, 54), (50, 52, 1), (40, 54)]), 'mid', 'f'),
              L(ell(19, 86, 3, 4.4) + [ell(19, 86, 3, 4.4)[0]], GOLD, 'f', False, False, 1.4), L(ell(81, 86, 3, 4.4) + [ell(81, 86, 3, 4.4)[0]], GOLD, 'f', False, False, 1.4),
              L(outline([(28, 68), (36, 64), (44, 68), (36, 70)]), (90, 170, 220, 255), 'f', False), L(outline([(72, 68), (64, 64), (56, 68), (64, 70)]), (90, 170, 220, 255), 'f', False)],
    'side': [L(bumpy(44, 44, 50, 50, 13, 0.09)), L(outline([(0, 40), (24, 30), (40, 70), (20, 96), (2, 80)]), 'shade', 'b', False),
             L(outline([(70, 30), (86, 38), (84, 56), (76, 56)]), 'mid', 'f'),
             L(ell(46, 82, 3, 4.4) + [ell(46, 82, 3, 4.4)[0]], GOLD, 'f', False, False, 1.4),
             L(outline([(74, 68), (84, 66), (86, 70), (78, 70)]), (90, 170, 220, 255), 'f', False)],
    'back': [L(bumpy(50, 50, 52, 52, 14, 0.09)), L(outline([(56, 2), (92, 20), (102, 56), (86, 96), (60, 100)]), 'shade', 'b', False),
             L(outline([(4, 60), (50, 70), (96, 60), (90, 96), (50, 104), (10, 96)]), 'deep', 'b', False)],
}

# Bhangra Makarov (Keldi Rozel): cara redonda y ancha; pelo verde oscuro de pinchos altísimos hacia arriba y a los lados,
# cejas pobladas verdes, rayas de pintura blanca en las mejillas, nariz ancha, ojos azules y sonrisa
CHARS['bhangra-makarov'] = {
    'body': 'corpulento', 'pal': pal('#2e6a52', '#9a6a44', iris='#3a6aa0', shade='#24543e', deep='#1a3e2e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 4.4), 'hairline': [(14, 66), (16, 54), (30, 50), (50, 52), (70, 50), (84, 54), (86, 66)],
             'face_front': blob([(16, 52), (50, 44), (84, 52), (90, 76), (84, 98), (66, 108), (50, 110), (34, 108), (16, 98), (10, 76)])},
    'front': [L(outline([(16, 68), (12, 46), (14, 30), (-6, 16, 1), (16, 18), (14, -6, 1), (32, 10), (44, -4, 1), (50, 8), (60, -6, 1), (66, 10), (88, -2, 1),
                         (78, 20), (104, 18, 1), (86, 32), (88, 46), (84, 68), (78, 54), (22, 54)])),
              L(outline([(60, -6), (66, 10), (88, -2), (78, 20), (104, 18), (86, 32), (88, 50), (80, 36), (68, 22)]), 'shade', 'b', False),
              L(outline([(26, 70), (32, 64), (44, 66), (46, 72), (38, 70)]), 'mid', 'f', True, True), L(outline([(74, 70), (68, 64), (56, 66), (54, 72), (62, 70)]), 'mid', 'f', True, True),
              L(outline([(14, 86), (28, 90), (26, 96), (14, 94)]), WHITE, 'f', False), L(outline([(86, 86), (72, 90), (74, 96), (86, 94)]), WHITE, 'f', False)],
    'side': [L(outline([(64, 54), (70, 44), (82, 40), (84, 30), (100, 20, 1), (76, 22), (112, -6, 1), (70, 8), (64, -14, 1), (52, 4), (28, -14, 1), (30, 8), (6, -8, 1),
                        (14, 16), (4, 44), (8, 76), (24, 80), (36, 70), (44, 60), (54, 56)])),
             L(outline([(4, 44), (14, 20), (30, 30), (36, 70), (24, 80), (8, 76)]), 'shade', 'b', False),
             L(outline([(72, 70), (78, 64), (86, 66), (84, 72)]), 'mid', 'f', True, True),
             L(outline([(74, 84), (88, 78), (90, 86), (78, 92)]), WHITE, 'f', False)],
    'back': [L(outline([(18, 82), (14, 50), (16, 30), (-6, 14, 1), (18, 16), (16, -8, 1), (34, 8), (50, -12, 1), (60, 6), (74, -4, 1), (72, 12), (100, 10, 1),
                        (84, 28), (86, 50), (82, 82), (50, 86)])),
             L(outline([(60, 6), (74, -4), (72, 12), (100, 10), (84, 28), (86, 50), (82, 80), (64, 84)]), 'shade', 'b', False)],
}
