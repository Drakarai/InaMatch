"""Guardianas (vr-gatekeepers): las agentes de la Oficina de Administración Temporal del modo Crónica de Victory Road
(Inazuma Eleven: Eiyuutachi no Victory Road), todas chicas, con sus modelos 3D de la enciclopedia
(英雄たちのヴィクトリーロード). Cada una tiene una sola forma; ninguna coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, longhair, outline, pal, rope, strand  # noqa: F401
from heads import mirror, quad  # noqa: F401

BLACK = (28, 26, 30, 255)
WHITE = (246, 246, 246, 255)
TEAL = (40, 220, 200, 255)
GREY = (150, 152, 160, 255)
BLUSH = (230, 130, 120, 255)


# Emelia (Amara Myles, portera): pelo verde agua recogido en un turbante de rollos sobre la cabeza, con un nudo detrás
# del que cae una cola larga, y dos mechones que le bajan por las mejillas; visor oscuro que le tapa los ojos
VISOR = (40, 30, 90, 255)
CHARS['amara-myles'] = {
    'body': 'chica', 'pal': pal('#6ac8b0', '#fad8c4', shade='#4ea08c', deep='#347464'),
    'face': {'eyes': 'none', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(16, 70), (22, 60), (36, 56), (50, 60), (64, 56), (78, 60), (84, 70)]},
    'front': [L(rope((22, 60), (14, 84), (24, 102), 7)), L(rope((78, 60), (86, 84), (76, 102), 7)),
              L(outline([(16, 70), (8, 54), (6, 36), (14, 14), (30, 0), (50, -8), (70, 0), (86, 14), (94, 36), (92, 54), (84, 70), (50, 62)])),
              L(outline([(60, -2), (84, 14), (94, 40), (90, 60), (80, 40)]), 'shade', 'b', False),
              strand([(8, 40), (30, 30), (50, 32), (70, 30), (92, 40)], 'deep', 'b', 1.2), strand([(20, 16), (50, 8), (80, 16)], 'deep', 'b', 1.0),
              strand([(46, 34), (36, 46), (26, 58)], 'deep', 'b', 1.0), strand([(54, 34), (64, 46), (74, 58)], 'deep', 'b', 1.0),
              L(outline([(14, 68), (30, 66), (50, 68), (70, 66), (86, 68), (84, 80), (66, 84), (50, 82), (34, 84), (16, 80)]), WHITE, 'f'),
              L(outline([(18, 70), (34, 68), (50, 70), (66, 68), (82, 70), (80, 78), (66, 82), (50, 80), (34, 82), (20, 78)]), VISOR, 'f', False),
              L([(26, 72), (40, 71)], (120, 110, 200, 255), 'f', False, False, 1.4)],
    'side': [L(rope((18, 44), (2, 80), (4, 124), 12)),
             L(outline([(66, 60), (74, 54), (86, 50), (92, 34), (82, 8), (58, -6), (32, -4), (12, 12), (4, 36), (10, 56), (26, 62), (40, 60), (52, 58)])),
             L(outline([(6, 38), (40, 34), (70, 40), (88, 36), (82, 50), (44, 48), (10, 52)]), 'shade', 'b', False),
             L(rope((58, 58), (60, 82), (66, 100), 6)),
             L(outline([(52, 70), (80, 68), (92, 70), (90, 80), (78, 82), (52, 76)]), WHITE, 'f'),
             L(outline([(72, 70), (90, 71), (88, 79), (74, 80)]), VISOR, 'f', False)],
    'back': [L(rope((24, 60), (16, 84), (24, 102), 7)), L(rope((76, 60), (84, 84), (76, 102), 7)),
             L(outline([(46, 56), (40, 90), (44, 122, 1), (56, 122, 1), (60, 90), (54, 56)])),
             L(outline([(16, 68), (8, 52), (6, 34), (14, 12), (30, -2), (50, -8), (70, -2), (86, 12), (94, 34), (92, 52), (84, 68), (50, 64)])),
             L(outline([(58, -4), (84, 12), (94, 36), (90, 60), (66, 56)]), 'shade', 'b', False),
             strand([(8, 40), (30, 30), (50, 34), (70, 30), (92, 40)], 'deep', 'b', 1.2),
             L(ell(50, 58, 9, 6), 'mid', 'f'), strand([(42, 56), (58, 60)], 'deep', 'f', 1.0)],
}

# Vivi (Vivian Calder): piel morena y rastas negras gruesas y cortas que salen disparadas en todas direcciones, con una
# que le cruza la cara; auriculares grises con luz turquesa y una antena triangular turquesa; ojos grises afilados
CHARS['vivian-calder'] = {
    'body': 'chica', 'pal': pal('#1c1618', '#7a4a30', iris='#7a94b0', shade='#121012', deep='#060506'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'ears': False,
             'hairline': [(14, 70), (18, 56), (30, 50), (44, 54), (56, 50), (70, 52), (82, 58), (86, 70)]},
    'front': [L(outline([(16, 96), (10, 70), (-4, 64, 1), (0, 56), (8, 54), (-8, 44, 1), (-6, 36), (8, 34), (2, 22, 1), (6, 14), (18, 12), (16, 0, 1), (26, -4), (34, 2),
                         (40, -8, 1), (52, -6), (58, 2), (70, -6, 1), (78, 0), (80, 10), (96, 8, 1), (98, 16), (88, 26), (106, 30, 1), (104, 38), (92, 42),
                         (108, 52, 1), (104, 60), (92, 60), (100, 74, 1), (92, 78), (86, 74), (84, 96), (82, 62), (18, 62)])),
              L(outline([(58, 4), (78, 4), (90, 28), (96, 50), (88, 70), (78, 46)]), 'shade', 'b', False),
              strand([(30, 10), (34, 30)], (70, 60, 64, 255), 'b', 1.0), strand([(62, 8), (60, 28)], (70, 60, 64, 255), 'b', 1.0),
              L(outline([(48, 52), (58, 50), (62, 70), (60, 92), (54, 104, 1), (52, 84), (52, 66)]), 'mid', 'f'),
              L(ell(16, 80, 6, 7), GREY, 'f'), L(ell(16, 80, 2.6, 3.2), TEAL, 'f', False),
              L(outline([(12, 58), (18, 58), (16, 72, 1)]), TEAL, 'f', False)],
    'side': [L(outline([(62, 58), (72, 52), (84, 50), (92, 34), (100, 30, 1), (88, 22), (92, 8, 1), (78, 8), (74, -8, 1), (60, 0), (46, -12, 1), (40, 2), (20, -2, 1),
                        (22, 10), (4, 12, 1), (10, 24), (-10, 32, 1), (2, 40), (-12, 52, 1), (4, 58), (-6, 74, 1), (8, 76), (6, 96, 1), (20, 88), (24, 108, 1),
                        (36, 92), (44, 74), (52, 62)])),
             L(outline([(0, 40), (30, 44), (40, 72), (24, 92), (6, 76)]), 'shade', 'b', False),
             L(ell(46, 72, 8, 9), GREY, 'f'), L(ell(46, 72, 4.4, 5), WHITE, 'f', False), L(ell(46, 72, 2.4, 3), TEAL, 'f', False),
             L(outline([(42, 46), (50, 46), (46, 62, 1)]), TEAL, 'f', False)],
    'back': [L(outline([(18, 100), (12, 76), (-4, 74, 1), (0, 64), (8, 60), (-10, 50, 1), (-8, 40), (6, 36), (0, 24, 1), (4, 16), (16, 12), (14, 0, 1), (26, -4), (34, 2),
                        (40, -8, 1), (52, -6), (58, 2), (70, -6, 1), (78, 0), (82, 10), (98, 10, 1), (100, 18), (90, 28), (108, 32, 1), (106, 42), (94, 44),
                        (110, 56, 1), (104, 64), (94, 64), (102, 78, 1), (92, 82), (86, 80), (84, 104, 1), (70, 96), (60, 110, 1), (50, 98), (40, 110, 1), (32, 96)])),
             L(outline([(58, 4), (78, 4), (92, 30), (98, 54), (88, 90), (66, 96)]), 'shade', 'b', False)],
}

# Zohra (Zora Selwick): pelo gris plateado con un moño alto en lazo y raya a un lado, del que cae un mechón largo que le
# tapa el lado derecho de la cara hasta el hombro; al otro lado, corto con la oreja a la vista; ojos rosas con un
# corazón en el brillo y labios oscuros
CHARS['zora-selwick'] = {
    'body': 'chica', 'pal': pal('#b8bcc2', '#fadcca', iris='#d04070', shade='#8e9298', deep='#666a70'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 93,
             'hairline': [(14, 100), (20, 70), (30, 54), (44, 46), (60, 42), (74, 48), (82, 56), (86, 66)]},
    'front': [L(rope((40, 6), (14, -40), (66, -24), 8)), L(ell(56, -6, 12, 10)),
              L(outline([(16, 104, 1), (10, 80), (8, 54), (14, 28), (30, 10), (50, 4), (70, 8), (84, 22), (90, 40), (88, 62), (84, 70), (80, 52), (60, 42),
                         (36, 56), (26, 80), (24, 104)])),
              L(outline([(56, 6), (78, 14), (90, 40), (86, 62), (78, 46)]), 'shade', 'b', False),
              L(outline([(60, 8), (48, 24), (30, 46), (24, 76), (22, 104, 1), (14, 86), (14, 52), (26, 26)]), 'mid', 'f'),
              strand([(54, 10), (36, 36), (26, 70), (22, 100)], 'deep', 'f', 1.0), L(ell(56, -8, 6, 3), 'light', 'b', False)],
    'side': [L(rope((42, 6), (36, -40), (70, -26), 8)), L(ell(50, -4, 14, 10)),
             L(outline([(64, 56), (74, 50), (84, 48), (90, 32), (80, 10), (58, 0), (34, 2), (14, 16), (6, 40), (10, 62), (24, 72), (36, 64), (44, 56), (54, 54)])),
             L(outline([(8, 40), (34, 42), (40, 62), (24, 70)]), 'shade', 'b', False)],
    'back': [L(rope((50, 6), (40, -40), (70, -24), 8)), L(ell(50, -6, 16, 11)),
             L(outline([(18, 74), (12, 50), (18, 24), (34, 8), (50, 4), (66, 8), (82, 24), (88, 50), (90, 80), (86, 104, 1), (78, 90), (74, 70), (50, 80)])),
             L(outline([(56, 6), (82, 24), (88, 54), (86, 100), (76, 78)]), 'shade', 'b', False)],
}

# Ilvy (Ivy Celeste): pelo rubio con raya en zigzag, recogido en dos mechones enormes que le caen a los lados como
# orejas de cocker hasta el pecho; aparatos grises con luz turquesa a los lados de la cabeza y gafas de montura gruesa
# azul marino; ojos turquesa y ceño fruncido
NAVY = (40, 40, 100, 255)
CHARS['ivy-celeste'] = {
    'body': 'chica', 'pal': pal('#ecd090', '#fadcca', iris='#30d0e0', shade='#c8a868', deep='#9a7c46'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'ears': False,
             'hairline': [(14, 70), (16, 52), (26, 40), (40, 34), (50, 36), (60, 34), (74, 40), (84, 52), (86, 70)]},
    'front': [L(outline([(20, 30), (6, 50), (2, 80), (8, 104, 1), (24, 98), (24, 60)])), L(outline([(80, 30), (94, 50), (98, 80), (92, 104, 1), (76, 98), (76, 60)])),
              L(outline([(80, 30), (94, 50), (98, 80), (92, 104), (82, 80)]), 'shade', 'b', False),
              L(outline([(16, 64), (14, 36), (24, 14), (50, 4), (76, 14), (86, 36), (84, 64), (50, 40)])),
              L(outline([(60, 6), (78, 16), (86, 40), (84, 60), (74, 36)]), 'shade', 'b', False),
              L([(50, 4), (46, 10), (52, 16), (48, 24)], 'deep', 'b', False, False, 1.2),
              L(outline([(16, 26), (24, 24), (26, 64), (18, 66)]), GREY, 'f'), L(outline([(84, 26), (76, 24), (74, 64), (82, 66)]), GREY, 'f'),
              L(outline([(17, 20), (23, 20), (23, 30), (17, 30)]), TEAL, 'f'), L(outline([(83, 20), (77, 20), (77, 30), (83, 30)]), TEAL, 'f'),
              L(ell(36, 76, 10, 8.5), NAVY, 'f', False, False, 2.6), L(ell(64, 76, 10, 8.5), NAVY, 'f', False, False, 2.6),
              L([(45, 74), (55, 74)], NAVY, 'f', False, False, 2.4)],
    'side': [L(outline([(30, 30), (12, 44), (0, 80), (6, 116, 1), (24, 102), (34, 70)])),
             L(outline([(2, 70), (24, 66), (24, 102), (6, 112)]), 'shade', 'b', False),
             L(outline([(64, 56), (72, 52), (84, 50), (90, 34), (80, 12), (58, 2), (34, 4), (16, 18), (12, 40), (20, 58), (38, 62), (52, 56)])),
             L(outline([(40, 20), (56, 14), (58, 68), (44, 74)]), GREY, 'f'), L(outline([(46, 6), (54, 6), (54, 20), (46, 20)]), TEAL, 'f'),
             L(outline([(44, 50), (54, 50), (54, 60), (44, 60)]), TEAL, 'f', False),
             L(ell(82, 76, 7, 8), NAVY, 'f', False, False, 2.6), L([(58, 72), (76, 72)], NAVY, 'f', False, False, 2.4)],
    'back': [L(outline([(16, 64), (14, 36), (24, 14), (50, 4), (76, 14), (86, 36), (84, 64), (50, 70)])),
             L(outline([(20, 26), (6, 50), (2, 80), (10, 108, 1), (40, 100), (46, 60), (44, 24)])), L(outline([(80, 26), (94, 50), (98, 80), (90, 108, 1), (60, 100), (54, 60), (56, 24)])),
             L(outline([(80, 26), (94, 50), (98, 80), (90, 106), (70, 96), (64, 56)]), 'shade', 'b', False),
             strand([(50, 6), (50, 40)], 'deep', 'b', 1.0)],
}

# Juliet (Julietta Belamy): melena negra lisa muy larga, con las puntas de los lados dobladas hacia fuera a la altura de
# la barbilla; diadema plateada con piezas turquesa; ojos negros grandes y labios turquesa
SILVER = (196, 200, 210, 255)
CHARS['julietta-belamy'] = {
    'body': 'chica', 'pal': pal('#18161c', '#fadcca', iris='#141216', shade='#100e12', deep='#060508', light='#3a3640', lips='#30b0b0'),
    'face': {'eyes': 'big', 'mouth': 'none', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 90), (16, 62), (28, 52), (42, 56), (50, 48), (58, 56), (72, 52), (84, 62), (86, 90)]},
    'front': longhair('front', length=122, flare=4, top=4) + [
              L(outline([(16, 74), (-6, 84, 1), (8, 70), (12, 60)]), 'mid', 'b'), L(outline([(84, 74), (106, 84, 1), (92, 70), (88, 60)]), 'mid', 'b'),
              L(outline([(14, 64), (12, 38), (24, 14), (50, 6), (76, 14), (88, 38), (86, 64), (76, 56), (62, 50), (50, 56), (38, 50), (24, 56)]), 'mid', 'f'),
              L(quad((16, 40), (50, -6), (84, 40)), SILVER, 'f', False, False, 3.0),
              L(outline([(18, 30), (24, 22), (26, 32)]), TEAL, 'f', False), L(outline([(82, 30), (76, 22), (74, 32)]), TEAL, 'f', False),
              L(blob([(46, 93), (54, 93), (52, 95), (48, 95)], 4), 'lips', 'f', False)],
    'side': longhair('side', length=124, flare=3, top=4) + [
             L(outline([(70, 60), (86, 80, 1), (70, 74)]), 'mid', 'b'),
             L(quad((24, 8), (60, 0), (82, 26)), SILVER, 'f', False, False, 3.0), L(outline([(60, 18), (70, 12), (68, 26)]), TEAL, 'f', False)],
    'back': longhair('back', length=124, flare=4, top=4, ends=3) + [
             L(outline([(12, 70), (-8, 80, 1), (6, 64)]), 'mid', 'b'), L(outline([(88, 70), (108, 80, 1), (94, 64)]), 'mid', 'b')],
}

# Jackie (Jackie Mulligan): pelo rojo rosado con flequillo de lado, coleta baja atada con una pieza gris y un mechón
# ondulado junto a la mejilla; gafas de varilla fina trapezoidales sobre los ojos grises, cejas fruncidas y pecas
WIRE = (210, 212, 220, 255)
CHARS['jackie-mulligan'] = {
    'body': 'chica', 'pal': pal('#c86868', '#fadcca', iris='#6a6a8a', shade='#a44e52', deep='#7a383c', freckle='#e0a090'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(14, 76), (16, 56), (24, 44), (38, 50), (50, 56), (62, 58), (76, 60), (84, 66), (86, 76)]},
    'front': [L(outline([(16, 80), (10, 56), (14, 30), (30, 12), (50, 6), (70, 10), (86, 28), (90, 54), (86, 80), (82, 62), (18, 62)])),
              L(outline([(60, 8), (82, 24), (90, 52), (86, 76), (80, 50)]), 'shade', 'b', False),
              strand([(30, 14), (44, 30), (62, 52)], 'deep', 'b', 1.0), strand([(20, 30), (36, 40), (52, 54)], 'deep', 'b', 1.0),
              L(rope((84, 62), (92, 82), (84, 100), 5)),
              L(outline([(14, 70), (86, 70), (82, 82), (18, 82)]), WIRE, 'f', False, False, 1.2),
              L(ell(30, 86, 1.0, 1.0), 'freckle', 'f', False), L(ell(34, 88, 1.0, 1.0), 'freckle', 'f', False),
              L(ell(66, 88, 1.0, 1.0), 'freckle', 'f', False), L(ell(70, 86, 1.0, 1.0), 'freckle', 'f', False)],
    'side': [L(outline([(20, 64), (4, 82), (6, 108, 1), (20, 96), (30, 72)])), L(outline([(16, 64), (28, 66), (26, 72), (14, 70)]), GREY, 'b'),
             L(outline([(64, 58), (74, 54), (86, 54), (92, 36), (82, 12), (58, 2), (34, 4), (14, 18), (8, 42), (16, 62), (34, 70), (46, 62), (54, 58)])),
             L(outline([(10, 42), (34, 46), (40, 64), (18, 66)]), 'shade', 'b', False),
             L(rope((58, 58), (66, 80), (58, 98), 5)),
             L(outline([(48, 72), (90, 70), (88, 80), (52, 78)]), WIRE, 'f', False, False, 1.2)],
    'back': [L(outline([(42, 72), (36, 96), (46, 112, 1), (56, 112, 1), (64, 96), (58, 72)])),
             L(outline([(16, 76), (10, 52), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (90, 52), (84, 76), (50, 82)])),
             L(outline([(56, 8), (82, 24), (90, 52), (84, 76), (64, 80)]), 'shade', 'b', False),
             L(outline([(42, 74), (58, 74), (58, 82), (42, 82)]), GREY, 'f'),
             L(rope((18, 62), (10, 82), (18, 100), 5))],
}

# Chianti (Kendra Pierce): piel morena y pelo corto rubio ceniza despeinado, con un mechón que le cae por la frente; una
# diadema negra ancha con líneas verde neón le cruza la cabeza; ojos verdes y sonrisa enseñando los dientes
NEON = (50, 230, 100, 255)
CHARS['kendra-pierce'] = {
    'body': 'chica', 'pal': pal('#e2cbb0', '#8a5a3a', iris='#3aa060', shade='#c0a688', deep='#8e7658'),
    'face': {'eyes': 'big', 'mouth': 'grin', 'mouth_y': 93,
             'hairline': [(14, 70), (18, 56), (30, 54), (40, 60), (46, 52), (56, 66), (62, 56), (72, 54), (82, 58), (86, 70)]},
    'front': [L(outline([(16, 76), (6, 66, 1), (10, 54), (2, 40, 1), (12, 32), (10, 16, 1), (24, 12), (34, 0, 1), (46, 8), (60, 0, 1), (68, 10), (86, 12, 1), (88, 28),
                         (98, 38, 1), (90, 50), (96, 64, 1), (84, 76), (80, 60), (20, 60)])),
              L(outline([(62, 4), (84, 16), (92, 40), (88, 66), (80, 44)]), 'shade', 'b', False),
              L(outline([(12, 44), (16, 26), (32, 14), (50, 10), (68, 14), (84, 26), (88, 44), (80, 46), (68, 30), (50, 26), (32, 30), (20, 46)]), BLACK, 'f'),
              L(quad((22, 36), (50, 16), (78, 36)), NEON, 'f', False, False, 2.2),
              L(outline([(40, 40), (50, 36), (60, 44), (56, 66, 1), (50, 50), (44, 60, 1)]), 'mid', 'f')],
    'side': [L(outline([(64, 56), (74, 52), (86, 50), (94, 40, 1), (88, 28), (90, 12, 1), (76, 10), (68, -2, 1), (56, 4), (40, -4, 1), (32, 6), (16, 6, 1), (16, 18),
                        (2, 26, 1), (8, 38), (0, 50, 1), (10, 58), (8, 72, 1), (22, 70), (34, 74, 1), (42, 64), (52, 58)])),
             L(outline([(6, 38), (30, 42), (40, 62), (20, 70)]), 'shade', 'b', False),
             L(outline([(40, 4), (62, 8), (80, 22), (86, 40), (76, 44), (66, 26), (50, 18), (36, 16)]), BLACK, 'f'),
             L(quad((46, 10), (70, 16), (80, 34)), NEON, 'f', False, False, 2.2)],
    'back': [L(outline([(18, 76), (8, 66, 1), (12, 54), (4, 40, 1), (14, 30), (10, 14, 1), (26, 12), (36, 0, 1), (48, 8), (62, 0, 1), (70, 10), (88, 14, 1), (88, 30),
                        (98, 40, 1), (90, 52), (94, 66, 1), (82, 76), (66, 82), (58, 90, 1), (50, 82), (42, 90, 1), (34, 82)])),
             L(outline([(58, 6), (84, 18), (92, 44), (84, 76), (62, 82)]), 'shade', 'b', False),
             strand([(40, 30), (50, 40), (60, 30)], 'deep', 'b', 1.0), strand([(30, 56), (40, 66), (50, 56)], 'deep', 'b', 1.0)],
}

# Trixie (Trixie Bren): tupé alto gris beis peinado hacia un lado, con los lados y la nuca cortos en castaño; gafas
# cuadradas naranjas, ojos verde grisáceo y un auricular plateado en la oreja
ORANGE = (224, 122, 42, 255)
SIDEB = (138, 112, 96, 255)
CHARS['trixie-bren'] = {
    'body': 'chica', 'pal': pal('#cabeb2', '#fadcca', iris='#7a9a80', shade='#a89a8e', deep='#7a6e64'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 93,
             'hairline': [(14, 66), (18, 50), (30, 44), (44, 46), (56, 52), (70, 56), (82, 58), (86, 66)]},
    'front': [L(outline([(16, 72), (12, 50), (18, 34), (82, 34), (88, 50), (84, 72), (80, 58), (20, 58)]), SIDEB),
              L(outline([(16, 46), (12, 24), (22, 4), (40, -6), (60, -6), (78, 4), (100, 24, 1), (88, 36), (76, 44), (66, 60, 1), (60, 40), (44, 40), (28, 46), (22, 62, 1)])),
              L(outline([(58, -4), (78, 6), (96, 24), (82, 34), (66, 26)]), 'shade', 'b', False),
              strand([(28, 4), (44, 20), (62, 40)], 'deep', 'b', 1.0),
              L(outline([(22, 66), (46, 66), (46, 84), (22, 84)]), ORANGE, 'f', False, False, 2.6), L(outline([(54, 66), (78, 66), (78, 84), (54, 84)]), ORANGE, 'f', False, False, 2.6),
              L([(46, 72), (54, 72)], ORANGE, 'f', False, False, 2.0),
              L(outline([(10, 66), (16, 64), (18, 80), (12, 80)]), SILVER, 'f'), L(outline([(90, 66), (84, 64), (82, 80), (88, 80)]), SILVER, 'f')],
    'side': [L(outline([(60, 56), (70, 50), (76, 36), (60, 30), (30, 30), (12, 44), (12, 70), (28, 84), (40, 72), (44, 60)]), SIDEB),
             L(outline([(76, 40), (98, 30), (102, 16, 1), (88, 6), (64, -6), (36, -6), (14, 6), (4, 26), (8, 40), (30, 34), (56, 34)])),
             L(outline([(8, 24), (40, 22), (64, 30), (8, 38)]), 'shade', 'b', False),
             L(outline([(48, 66), (58, 60), (60, 76), (52, 80)]), SILVER, 'f'),
             L(outline([(72, 66), (90, 66), (90, 82), (72, 82)]), ORANGE, 'f', False, False, 2.6), L([(58, 70), (72, 70)], ORANGE, 'f', False, False, 2.0)],
    'back': [L(outline([(18, 76), (12, 50), (18, 30), (82, 30), (88, 50), (82, 76), (64, 86), (36, 86)]), SIDEB),
             L(outline([(14, 40), (12, 20), (24, 2), (44, -6), (64, -6), (80, 2), (102, 20, 1), (88, 36), (50, 42), (24, 44)])),
             L(outline([(56, -4), (80, 4), (100, 20), (86, 34), (60, 36)]), 'shade', 'b', False),
             L(outline([(84, 66), (90, 64), (92, 80), (86, 80)]), SILVER, 'f'), L(outline([(16, 66), (10, 64), (8, 80), (14, 80)]), SILVER, 'f')],
}

# Allik (Arwena Lark): piel tostada y una melena castaño oscuro muy abultada con raya a un lado, que cruza la frente en una
# onda grande y le cae ondulada por los lados hasta los hombros; ojos grises entornados
CHARS['arwena-lark'] = {
    'body': 'chica', 'pal': pal('#4a3a30', '#c48c64', iris='#8a8a9a', shade='#382c24', deep='#241c16'),
    'face': {'eyes': 'sharp', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 96), (16, 62), (24, 50), (34, 44), (50, 50), (64, 58), (76, 66), (84, 74), (86, 96)]},
    'front': [L(outline([(16, 104), (6, 84), (4, 56), (10, 28), (26, 8), (46, 0), (68, 4), (88, 20), (98, 46), (100, 70), (94, 92), (88, 106, 1), (80, 96), (82, 80),
                         (70, 62), (50, 52), (30, 50), (22, 76), (22, 100)])),
              L(outline([(60, 4), (86, 22), (98, 50), (96, 84), (86, 100), (84, 70), (76, 52)]), 'shade', 'b', False),
              strand([(30, 10), (26, 30), (22, 50)], 'deep', 'b', 1.0), strand([(36, 14), (56, 30), (80, 58)], 'deep', 'b', 1.0),
              strand([(12, 70), (16, 86), (12, 100)], 'deep', 'b', 1.0), strand([(90, 70), (92, 86), (88, 100)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 60), (72, 56), (86, 56), (96, 42), (90, 16), (66, 0), (36, -2), (12, 12), (-2, 40), (0, 70), (12, 92), (34, 102), (48, 90), (52, 74)])),
             L(outline([(0, 46), (30, 48), (46, 76), (34, 98), (10, 86)]), 'shade', 'b', False),
             strand([(40, 4), (62, 20), (84, 44)], 'deep', 'b', 1.0)],
    'back': [L(outline([(14, 100), (4, 80), (2, 52), (10, 24), (28, 6), (50, 0), (72, 6), (90, 24), (98, 52), (96, 80), (86, 100), (66, 96), (50, 100), (34, 96)])),
             L(outline([(58, 4), (88, 24), (98, 56), (90, 96), (66, 94)]), 'shade', 'b', False)],
}

# Lindalin (Lindalyn Berny, capitana): pelo blanco con sombras lila, redondeado arriba con raya en medio y abierto a los
# lados en dos alas en punta a la altura de la cara; adornos turquesa en las sienes que se enroscan junto a los ojos;
# ojos turquesa y labios rosados
CHARS['lindalyn-berny'] = {
    'body': 'chica', 'pal': pal('#e8eef0', '#fadcca', iris='#30b0c0', shade='#c4b4bc', deep='#a08e98', lips='#d86070'),
    'face': {'eyes': 'big', 'mouth': 'none', 'ears': False,
             'hairline': [(14, 76), (18, 54), (30, 42), (44, 38), (50, 44), (56, 38), (70, 42), (82, 54), (86, 76)]},
    'front': [L(outline([(16, 64), (-6, 80, 1), (10, 84), (18, 100, 1), (26, 84), (24, 70)])), L(outline([(84, 64), (106, 80, 1), (90, 84), (82, 100, 1), (74, 84), (76, 70)])),
              L(outline([(-6, 80), (10, 84), (18, 100), (24, 84)]), 'shade', 'b', False), L(outline([(106, 80), (90, 84), (82, 100), (76, 84)]), 'shade', 'b', False),
              L(outline([(16, 76), (12, 48), (18, 22), (34, 6), (50, 2), (66, 6), (82, 22), (88, 48), (84, 76), (80, 56), (20, 56)])),
              L(outline([(60, 6), (80, 20), (88, 48), (84, 70), (78, 44)]), 'shade', 'b', False),
              strand([(50, 4), (50, 40)], 'deep', 'b', 1.0),
              L(ell(24, 70, 3.6, 3.6), (20, 120, 130, 255), 'f', ln=True), L(ell(76, 70, 3.6, 3.6), (20, 120, 130, 255), 'f', ln=True),
              L(quad((26, 74), (24, 86), (34, 84)), TEAL, 'f', False, False, 1.6), L(quad((74, 74), (76, 86), (66, 84)), TEAL, 'f', False, False, 1.6),
              L(blob([(46, 93), (54, 93), (52, 96), (48, 96)], 4), 'lips', 'f', False)],
    'side': [L(outline([(36, 60), (2, 74, 1), (22, 78), (30, 96, 1), (42, 76)])),
             L(outline([(64, 56), (74, 52), (86, 52), (92, 34), (82, 12), (60, 2), (36, 4), (16, 18), (10, 42), (18, 62), (36, 66), (52, 58)])),
             L(outline([(12, 40), (36, 42), (42, 62), (20, 64)]), 'shade', 'b', False),
             L(ell(76, 70, 3.4, 3.4), (20, 120, 130, 255), 'f', ln=True)],
    'back': [L(outline([(16, 62), (-6, 78, 1), (14, 80), (20, 96, 1), (30, 80)])), L(outline([(84, 62), (106, 78, 1), (86, 80), (80, 96, 1), (70, 80)])),
             L(outline([(16, 80), (12, 48), (18, 22), (34, 6), (50, 2), (66, 6), (82, 22), (88, 48), (84, 80), (50, 86)])),
             L(outline([(56, 6), (80, 22), (88, 50), (84, 78), (60, 84)]), 'shade', 'b', False)],
}

# Migria (Mira Lysander): piel tostada, pelo negro verdoso con flequillo recto y mechones largos a los lados de la cara
# hasta el pecho, y una coleta alta larguísima que sale de lo alto de la cabeza y cae por la espalda con las puntas
# atadas en turquesa; ojos azul grisáceo
CHARS['mira-lysander'] = {
    'body': 'chica', 'pal': pal('#1e3434', '#d8a070', iris='#8a9ac8', shade='#142424', deep='#0a1414', light='#3c5656'),
    'face': {'eyes': 'big', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 92), (16, 62), (50, 62), (84, 62), (86, 92)]},
    'front': [L(outline([(36, 6), (34, -12), (50, -20), (66, -12), (64, 6)])),
              L(outline([(14, 112, 1), (10, 84), (10, 46), (18, 20), (34, 6), (50, 2), (66, 6), (82, 20), (90, 46), (90, 84), (86, 112, 1), (80, 90), (82, 64), (18, 64), (20, 90)])),
              L(outline([(60, 4), (80, 18), (90, 46), (88, 104), (82, 66)]), 'shade', 'b', False),
              L(outline([(16, 64), (16, 36), (30, 18), (50, 12), (70, 18), (84, 36), (84, 64), (74, 64), (72, 56, 1), (66, 64), (40, 64), (34, 56, 1), (28, 64)]), 'mid', 'f'),
              strand([(30, 20), (28, 62)], 'deep', 'f', 1.0), strand([(70, 20), (72, 62)], 'deep', 'f', 1.0),
              L(outline([(12, 104), (20, 104), (18, 112), (14, 112)]), TEAL, 'f', False), L(outline([(88, 104), (80, 104), (82, 112), (86, 112)]), TEAL, 'f', False)],
    'side': [L(outline([(30, 6), (10, -30), (-16, -20), (-14, 30), (-10, 90), (-4, 120, 1), (6, 92), (4, 40), (6, -6), (16, -10), (22, 10)])),
             L(outline([(-12, 104), (-2, 104), (-2, 112), (-8, 112)]), TEAL, 'f', False),
             L(outline([(64, 62), (74, 60), (88, 60), (92, 36), (82, 12), (60, 2), (36, 4), (16, 18), (10, 44), (16, 64), (30, 66), (40, 62), (52, 60)])),
             L(outline([(12, 44), (36, 46), (40, 64), (18, 66)]), 'shade', 'b', False),
             L(outline([(70, 60), (88, 60), (84, 104, 1), (74, 90)]), 'mid', 'f'), L(ell(34, 6, 5, 4), GREY, 'f')],
    'back': [L(outline([(16, 84), (10, 56), (14, 28), (30, 10), (50, 4), (70, 10), (86, 28), (90, 56), (84, 84), (50, 90)])),
             L(outline([(40, 0), (36, 50), (40, 116), (50, 124, 1), (60, 116), (64, 50), (60, 0)])),
             L(outline([(52, 2), (64, 4), (64, 50), (60, 116), (52, 120)]), 'shade', 'b', False),
             L(outline([(40, 104), (60, 104), (60, 112), (40, 112)]), TEAL, 'f', False),
             L(outline([(58, 10), (84, 28), (90, 56), (84, 84), (66, 88)]), 'shade', 'b', False)],
}

# Keira (Keira Donnell): piel tostada y pelo azul marino oscuro corto en pinchos revueltos, con mechones por la frente;
# ojos marrón anaranjado con anillos y sonrisa
CHARS['keira-donnell'] = {
    'body': 'chica', 'pal': pal('#252b3e', '#d09868', iris='#b06a40', shade='#1a1e2c', deep='#0e1018'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(14, 70), (16, 54), (28, 48), (34, 58), (40, 48), (50, 56), (58, 48), (66, 58), (72, 48), (84, 54), (86, 70)]},
    'front': [L(outline([(16, 76), (6, 68, 1), (10, 56), (0, 46, 1), (8, 36), (0, 22, 1), (14, 18), (10, 4, 1), (26, 8), (30, -6, 1), (42, 4), (52, -10, 1), (60, 4),
                         (74, -4, 1), (76, 10), (92, 6, 1), (88, 20), (102, 26, 1), (92, 38), (100, 48, 1), (90, 56), (94, 68, 1), (84, 76), (80, 60), (20, 60)])),
              L(outline([(60, 2), (74, 0), (78, 12), (90, 10), (88, 22), (98, 28), (90, 40), (92, 60), (80, 46)]), 'shade', 'b', False),
              strand([(34, 10), (36, 30)], (60, 70, 96, 255), 'b', 1.0), strand([(60, 8), (58, 26)], (60, 70, 96, 255), 'b', 1.0)],
    'side': [L(outline([(64, 56), (74, 52), (86, 50), (98, 44, 1), (90, 34), (98, 22, 1), (86, 16), (88, 2, 1), (72, 4), (66, -10, 1), (54, 0), (40, -10, 1), (32, 4),
                        (14, 0, 1), (16, 14), (0, 18, 1), (8, 30), (-4, 40, 1), (8, 48), (2, 62, 1), (14, 64), (18, 78, 1), (30, 70), (42, 62), (52, 58)])),
             L(outline([(4, 36), (30, 40), (40, 62), (18, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 76), (6, 70, 1), (12, 58), (0, 48, 1), (8, 38), (0, 24, 1), (14, 20), (10, 6, 1), (26, 8), (30, -6, 1), (42, 4), (52, -10, 1), (60, 4),
                        (74, -4, 1), (76, 10), (92, 6, 1), (88, 22), (102, 28, 1), (92, 40), (100, 50, 1), (90, 58), (94, 70, 1), (82, 76), (66, 82), (58, 92, 1),
                        (50, 82), (42, 92, 1), (34, 82)])),
             L(outline([(58, 4), (86, 18), (94, 44), (86, 74), (62, 84)]), 'shade', 'b', False)],
}

# Cicely (Cecily Noire): melena lisa larga color ciruela oscuro, con raya a un lado y el flequillo largo cruzando la frente
# hacia el otro lado; ojos amarillos con raya negra y cara seria
CHARS['cecily-noire'] = {
    'body': 'chica', 'pal': pal('#5a2a3c', '#fadcca', iris='#e0b030', shade='#46202e', deep='#30141e'),
    'face': {'eyes': 'big', 'mouth': 'frown', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 100), (16, 66), (26, 56), (40, 52), (56, 46), (66, 40), (76, 46), (84, 60), (86, 100)]},
    'front': longhair('front', length=118, flare=3, top=4) + [
              L(outline([(14, 70), (12, 40), (24, 16), (50, 6), (76, 14), (88, 38), (86, 62), (80, 50), (66, 40), (50, 46), (34, 54), (22, 66), (18, 84, 1)]), 'mid', 'f'),
              strand([(64, 10), (46, 30), (24, 60)], 'deep', 'f', 1.0), strand([(68, 12), (80, 30), (86, 56)], 'deep', 'f', 1.0)],
    'side': longhair('side', length=120, flare=3, top=4) + [strand([(60, 4), (80, 20), (90, 40)], 'deep', 'b', 1.0)],
    'back': longhair('back', length=120, flare=3, top=4, ends=3) + [strand([(62, 6), (56, 40), (46, 110)], 'deep', 'b', 1.0)],
}

# Norma (Norah Queensby): pelo verde menta muy esponjoso, con un pico arriba y abierto a los lados en dos bullones
# grandes a la altura de la mandíbula que se curvan hacia dentro; flequillo de lado; ojos verde grisáceo
CHARS['norah-queensby'] = {
    'body': 'chica', 'pal': pal('#aac8b2', '#fadcca', iris='#8a9a6a', shade='#86a48e', deep='#62806a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 80), (18, 62), (28, 54), (44, 56), (50, 50), (60, 56), (72, 56), (82, 62), (86, 80)]},
    'front': [L(outline([(20, 92), (2, 96, 1), (-2, 80), (6, 64), (16, 56), (24, 74)])), L(outline([(80, 92), (98, 96, 1), (102, 80), (94, 64), (84, 56), (76, 74)])),
              L(outline([(98, 96), (102, 80), (94, 64), (84, 74), (82, 90)]), 'shade', 'b', False),
              L(outline([(16, 82), (8, 54), (10, 30), (26, 10), (44, 4), (50, -2, 1), (56, 4), (74, 10), (90, 30), (92, 54), (84, 82), (80, 62), (20, 62)])),
              L(outline([(60, 6), (82, 18), (92, 48), (86, 74), (78, 46)]), 'shade', 'b', False),
              strand([(44, 6), (36, 30), (30, 54)], 'deep', 'b', 1.0), strand([(52, 4), (60, 30), (70, 54)], 'deep', 'b', 1.0)],
    'side': [L(outline([(40, 70), (14, 96, 1), (4, 82), (10, 62), (24, 58)])),
             L(outline([(64, 58), (74, 54), (86, 52), (92, 34), (80, 10), (56, 0), (32, 2), (12, 16), (2, 42), (6, 66), (22, 80), (38, 76), (50, 62)])),
             L(outline([(4, 44), (30, 46), (40, 70), (20, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(20, 80), (-2, 94, 1), (-4, 76), (6, 60), (18, 56)])), L(outline([(80, 80), (102, 94, 1), (104, 76), (94, 60), (82, 56)])),
             L(outline([(16, 84), (8, 54), (10, 28), (26, 8), (44, 4), (50, -2, 1), (56, 4), (74, 8), (90, 28), (92, 54), (84, 84), (66, 82), (50, 88), (34, 82)])),
             L(outline([(58, 6), (84, 22), (92, 54), (84, 82), (64, 80)]), 'shade', 'b', False)],
}

# Cruel (Cressida Octavia): media melena castaña ondulada hasta los hombros con las puntas abiertas en ondas; flequillo
# de lado; ojos azules con sombra rosada y raya, cara seria
CHARS['cressida-octavia'] = {
    'body': 'chica', 'pal': pal('#a07060', '#fae0d2', iris='#4a80c0', shade='#80564a', deep='#5e3e34'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 90), (16, 64), (24, 52), (36, 46), (50, 50), (64, 56), (76, 58), (84, 64), (86, 90)]},
    'front': [L(outline([(16, 100), (2, 104, 1), (6, 92), (0, 80, 1), (8, 66), (8, 44), (16, 22), (32, 6), (50, 2), (68, 6), (84, 20), (92, 44), (92, 66), (100, 80, 1),
                         (94, 92), (98, 104, 1), (84, 100), (82, 62), (18, 62)])),
              L(outline([(60, 4), (82, 18), (92, 46), (94, 90), (84, 96), (80, 56)]), 'shade', 'b', False),
              strand([(30, 8), (28, 30), (22, 52)], 'deep', 'b', 1.0), strand([(36, 10), (56, 30), (74, 56)], 'deep', 'b', 1.0),
              L(quad((26, 70), (34, 68), (44, 72)), (220, 140, 150, 255), 'f', False, False, 1.4), L(quad((74, 70), (66, 68), (56, 72)), (220, 140, 150, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(62, 58), (72, 54), (86, 54), (92, 36), (82, 12), (60, 2), (34, 4), (14, 18), (6, 44), (6, 70), (0, 86, 1), (12, 92), (10, 104, 1), (26, 98),
                        (36, 104, 1), (44, 88), (48, 70), (54, 60)])),
             L(outline([(6, 46), (32, 48), (44, 76), (34, 96), (14, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 96), (2, 102, 1), (6, 88), (0, 74, 1), (8, 62), (8, 40), (18, 18), (34, 4), (50, 0), (66, 4), (82, 18), (92, 40), (92, 62), (100, 74, 1),
                        (94, 88), (98, 102, 1), (84, 96), (68, 98), (60, 106, 1), (50, 96), (40, 106, 1), (32, 98)])),
             L(outline([(58, 4), (84, 20), (92, 48), (92, 90), (66, 96)]), 'shade', 'b', False)],
}

# Katarina (Catalina Riven, portera suplente): pelo castaño claro despeinado en mechones de punta echados hacia un lado,
# con mechones largos que le caen junto a las mejillas; ojos verdes afilados con raya negra
CHARS['catalina-riven'] = {
    'body': 'chica', 'pal': pal('#c8986a', '#fadcca', iris='#30a070', shade='#a87a50', deep='#7e5a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93,
             'hairline': [(14, 76), (18, 58), (28, 50), (40, 56), (48, 46), (58, 58), (66, 50), (78, 56), (86, 76)]},
    'front': [L(rope((18, 66), (12, 86), (22, 98), 6)), L(rope((82, 66), (88, 86), (78, 96), 6)),
              L(outline([(16, 76), (8, 64, 1), (10, 52), (-2, 40, 1), (10, 32), (6, 16, 1), (20, 12), (26, -6, 1), (40, 4), (56, -12, 1), (62, 2), (80, -2, 1), (82, 12),
                         (100, 18, 1), (90, 30), (102, 42, 1), (90, 50), (94, 64, 1), (84, 76), (80, 58), (20, 58)])),
              L(outline([(60, 0), (78, 0), (82, 14), (96, 20), (88, 32), (96, 42), (88, 54), (80, 38)]), 'shade', 'b', False),
              strand([(36, 8), (44, 26), (48, 44)], 'deep', 'b', 1.0), strand([(62, 6), (60, 26), (64, 46)], 'deep', 'b', 1.0),
              L([(20, 72), (26, 74)], BLACK, 'f', False, False, 2.2), L([(80, 72), (74, 74)], BLACK, 'f', False, False, 2.2)],
    'side': [L(outline([(62, 56), (72, 52), (86, 50), (98, 40, 1), (90, 32), (100, 18, 1), (86, 14), (88, -2, 1), (72, 2), (64, -12, 1), (52, -2), (36, -10, 1), (30, 4),
                        (12, 2, 1), (14, 16), (-2, 22, 1), (6, 34), (-6, 46, 1), (6, 54), (2, 68, 1), (16, 68), (20, 82, 1), (32, 72), (42, 62), (52, 58)])),
             L(outline([(4, 34), (30, 40), (40, 60), (18, 70)]), 'shade', 'b', False),
             L(rope((64, 56), (70, 78), (62, 94), 5))],
    'back': [L(outline([(18, 76), (8, 66, 1), (12, 54), (0, 42, 1), (10, 34), (6, 18, 1), (20, 14), (26, -4, 1), (40, 6), (56, -10, 1), (62, 4), (80, 0, 1), (82, 14),
                        (100, 20, 1), (90, 32), (102, 44, 1), (90, 52), (94, 66, 1), (82, 76), (66, 82), (58, 92, 1), (50, 82), (42, 92, 1), (34, 82)])),
             L(outline([(58, 2), (86, 18), (94, 44), (86, 74), (62, 82)]), 'shade', 'b', False)],
}
