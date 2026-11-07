"""Gaviotas FC (vr-umi-kamome-soccer-club, 海鴎サッカークラブ): personajes propios de Victory Road, con sus modelos 3D de
英雄たちのヴィクトリーロード en la enciclopedia. Cada uno tiene una sola forma; van como 'vr:<id>'."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from chars_vr_toufuu_ikokukan import dots, fr, fre
from heads import quad  # noqa: F401

V = 'vr'
WHITE = (248, 248, 248, 255)
BLUSH = (236, 140, 130, 255)


def arcs(y=76, c=OUTC):
    """Ojos cerrados de felicidad (arcos hacia arriba)."""
    return [L(quad((28, y + 2), (36, y - 4), (44, y + 2)), c, 'f', False, False, 2.2), L(quad((56, y + 2), (64, y - 4), (72, y + 2)), c, 'f', False, False, 2.2)]


# Garrison Hayfield (portero): moreno claro, pelo castaño oscuro en un abanico ancho y plano hacia arriba (como un cepillo)
# con patillas que bajan en punta; ojos grandes y blancos con la pupila pequeña, cejas gruesas, rubor y boca en "o"
CHARS[f'{V}:garrison-hayfield'] = {
    'body': 'normal', 'pal': pal('#4a3426', '#d8a070', iris='#1e1410', shade='#38261a', deep='#281a10'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 96,
             'hairline': [(16, 72), (20, 56), (32, 52), (50, 50), (68, 52), (80, 56), (84, 72)]},
    'front': [L(outline([(16, 84), (14, 64), (10, 52), (-4, 26, 1), (2, 18), (-8, 0, 1), (10, -2), (20, -10, 1), (32, -6), (42, -12, 1), (52, -6), (62, -12, 1), (72, -6),
                         (82, -10, 1), (92, -2), (108, 0, 1), (98, 18), (104, 26, 1), (90, 52), (86, 64), (84, 84), (80, 62), (20, 62)])),
              L(outline([(60, -10), (84, -8), (98, 20), (90, 50), (78, 30)]), 'shade', 'b', False),
              strand([(24, 40), (14, 10)], 'deep', 'b', 1.0), strand([(40, 36), (36, 0)], 'deep', 'b', 1.0), strand([(60, 36), (64, 0)], 'deep', 'b', 1.0),
              strand([(76, 40), (86, 10)], 'deep', 'b', 1.0),
              L(ell(50, 96, 2.4, 2.8), (150, 70, 60, 255), 'f', False)] + dots([(28, 86), (31, 88), (72, 86), (69, 88)], BLUSH, 1.6),
    'side': [L(outline([(60, 76), (58, 56), (70, 52), (84, 46), (90, 30), (96, -2, 1), (72, 8), (40, 20), (6, 38), (-4, 50, 1), (8, 58), (20, 64), (34, 66), (44, 60),
                        (50, 68)])),
             L(outline([(6, 40), (40, 26), (60, 40), (40, 60), (10, 56)]), 'shade', 'b', False),
             strand([(20, 40), (80, 6)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 76), (14, 58), (2, 52, 1), (2, 30), (-6, 16, 1), (10, 4), (20, -4), (50, -8), (80, -4), (90, 4), (106, 16, 1), (98, 30), (98, 52, 1), (86, 58),
                        (82, 76), (50, 82)])),
             L(outline([(4, 46), (96, 46), (86, 60), (82, 76), (50, 82), (18, 76), (14, 60)]), 'shade', 'b', False)],
}

# Swae Talltree: media melena lisa gris violácea muy oscura hasta la barbilla, con un flequillo largo que le cae de lado
# sobre un ojo; ojos azules, labios rojos y un lunar junto a la boca
CHARS[f'{V}:swae-talltree'] = {
    'body': 'chica', 'pal': pal('#3a3442', '#fde2cc', iris='#4a6aa0', shade='#2a2632', deep='#1c1a22', light='#6a6478'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 104), (4, 70), (6, 34), (20, 8), (50, -2), (80, 8), (94, 34), (96, 70), (90, 104), (82, 74), (18, 74)])),
              L(outline([(60, 0), (84, 12), (96, 50), (90, 100), (82, 60)]), 'shade', 'b', False),
              fr([(12, 88), (10, 50), (22, 24), (46, 12), (70, 18), (86, 40), (88, 88), (82, 62), (74, 50), (62, 46), (56, 52), (52, 82, 1), (44, 60), (36, 58), (28, 62),
                  (20, 80)]),
              strand([(30, 14), (26, 40)], 'light', 'f', 1.2), strand([(66, 14), (70, 36)], 'light', 'f', 1.2),
              L([(45, 96), (55, 96)], (200, 50, 60, 255), 'f', False, False, 1.8), L(ell(57, 92, 0.9, 0.9), OUTC, 'f', False)],
    'side': [L(outline([(62, 82), (60, 60), (74, 54), (88, 48), (92, 28), (80, 8), (54, -2), (28, 2), (8, 20), (0, 50), (2, 84), (10, 100), (30, 102), (44, 96), (50, 76)])),
             L(outline([(2, 50), (26, 54), (40, 96), (12, 98)]), 'shade', 'b', False),
             fr([(70, 54), (88, 46), (92, 64), (84, 84, 1), (78, 64)])],
    'back': [L(outline([(10, 100), (4, 64), (6, 30), (20, 8), (50, -2), (80, 8), (94, 30), (96, 64), (90, 100), (70, 104), (50, 102), (30, 104)])),
             L(outline([(56, 0), (84, 14), (96, 60), (90, 100), (64, 102), (70, 50)]), 'shade', 'b', False),
             strand([(36, 10), (32, 60), (34, 100)], 'deep', 'b', 1.0), strand([(64, 10), (68, 60), (66, 100)], 'deep', 'b', 1.0)],
}

# Chilton Churner: grandullón con cara de señor mayor: pelo gris corto pegado al cráneo, con dos bultitos en las sienes;
# ojos caídos con ojeras, pecas en las mejillas y boca de gato en "w"
CHARS[f'{V}:chilton-churner'] = {
    'body': 'corpulento', 'pal': pal('#9aa2a8', '#fcd8c4', iris='#3a3a5a', shade='#7a8288', deep='#5e6468'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'none', 'mouth_y': 98, 'eye_y': 78,
             'hairline': [(14, 70), (18, 54), (24, 50), (30, 56), (40, 48), (50, 46), (60, 48), (70, 56), (76, 50), (82, 54), (86, 70)],
             'face_front': blob([(12, 52), (50, 36), (88, 52), (94, 78), (88, 102), (66, 112), (50, 114), (34, 112), (12, 102), (6, 78)])},
    'front': [L(outline([(14, 74), (10, 50), (14, 28), (30, 10), (50, 6), (70, 10), (86, 28), (90, 50), (86, 74), (80, 56), (20, 56)])),
              L(outline([(60, 8), (82, 20), (90, 50), (86, 70), (76, 40)]), 'shade', 'b', False),
              L(quad((28, 84), (36, 88), (44, 84)), (150, 100, 110, 255), 'f', False, False, 1.2),
              L(quad((56, 84), (64, 88), (72, 84)), (150, 100, 110, 255), 'f', False, False, 1.2),
              L(quad((42, 96), (46, 100), (50, 96)) + quad((50, 96), (54, 100), (58, 96))[1:], OUTC, 'f', False, False, 1.4)]
             + dots([(26, 92), (30, 94), (28, 90), (74, 92), (70, 94), (72, 90)]),
    'side': [L(outline([(58, 62), (60, 50), (76, 48), (84, 34), (74, 14), (50, 6), (24, 12), (8, 32), (6, 58), (18, 74), (36, 72), (46, 62)])),
             L(outline([(6, 40), (30, 30), (56, 50), (40, 70), (14, 70)]), 'shade', 'b', False),
             L(outline([(64, 50), (70, 44), (74, 52), (68, 56)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 76), (12, 50), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (88, 50), (84, 76), (50, 82)])),
             L(outline([(14, 50), (40, 40), (60, 30), (86, 34), (88, 54), (84, 76), (50, 82), (16, 76)]), 'shade', 'b', False)],
}

# Seon Gulliver: pelo plateado lila muy abultado y esponjoso, que por abajo oscurece a gris pardo, con un flequillo largo
# de lado sobre un ojo y rizos a los lados de la cara; ojos verde grisáceo serenos
CHARS[f'{V}:seon-gulliver'] = {
    'body': 'normal', 'pal': pal('#dcd8e6', '#fde4d4', iris='#4a5a5a', shade='#b4aec4', deep='#7a6a70', low='#8a7a80'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 96), (2, 76), (-4, 50), (0, 24), (18, 4), (40, -4), (50, 2), (60, -4), (82, 4), (100, 24), (104, 50), (98, 76), (88, 96), (80, 72),
                         (20, 72)])),
              L(outline([(-2, 50), (102, 50), (98, 76), (88, 96), (80, 72), (20, 72), (12, 96), (2, 76)]), 'low', 'b', False),
              L(outline([(60, -2), (86, 8), (102, 34), (96, 50), (80, 30)]), 'shade', 'b', False),
              fre([(14, 70), (14, 46), (28, 26), (50, 20), (72, 26), (86, 46), (86, 70), (80, 58), (70, 54), (62, 58), (54, 50), (46, 76, 1), (40, 56), (30, 54), (22, 64)], 7),
              L(outline([(14, 70), (20, 76), (18, 88), (24, 96), (16, 98), (10, 86)]), 'low', 'f'), L(outline([(86, 70), (80, 76), (82, 88), (76, 96), (84, 98), (90, 86)]), 'low', 'f'),
              strand([(46, 4), (50, 12), (54, 4)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 66), (62, 52), (82, 48), (96, 34), (96, 12), (76, -4), (46, -6), (18, 2), (0, 22), (-6, 48), (0, 72), (8, 90), (26, 94), (40, 86), (48, 68)])),
             L(outline([(-4, 48), (40, 50), (50, 66), (40, 86), (26, 94), (8, 90), (0, 72)]), 'low', 'b', False),
             fr([(72, 50), (88, 48), (90, 66), (82, 84, 1), (76, 64)], 'low')],
    'back': [L(outline([(10, 94), (0, 74), (-4, 48), (2, 22), (20, 4), (50, -4), (80, 4), (98, 22), (104, 48), (100, 74), (90, 94), (70, 100), (50, 96), (30, 100)])),
             L(outline([(-4, 46), (40, 52), (60, 44), (104, 46), (100, 74), (90, 94), (70, 100), (50, 96), (30, 100), (10, 94), (0, 74)]), 'low', 'b', False)],
}

# Plume Hathaway: moreno, pelo azul marino muy oscuro revuelto en mechones gruesos con una antena que sale arriba;
# flequillo en mechones sobre la frente, ojos turquesa grandes y boquita de enfado
CHARS[f'{V}:plume-hathaway'] = {
    'body': 'normal', 'pal': pal('#2a3a52', '#b07a52', iris='#4aa0a0', shade='#1e2a3e', deep='#141e2c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 80), (10, 60), (-2, 56, 1), (8, 46), (-4, 28, 1), (12, 22), (14, 4), (30, -6), (36, -24, 1), (44, -6), (60, -8), (76, -2), (92, 8, 1),
                         (88, 22), (104, 28, 1), (92, 42), (102, 56, 1), (90, 60), (86, 80), (80, 64), (20, 64)])),
              L(outline([(60, -6), (84, 4), (96, 34), (90, 76), (80, 50)]), 'shade', 'b', False),
              fr([(14, 66), (14, 42), (26, 24), (50, 18), (74, 24), (86, 42), (86, 66), (80, 52), (72, 62, 1), (66, 48), (58, 56, 1), (52, 46), (44, 60, 1), (40, 48),
                  (30, 58, 1), (24, 48), (20, 64, 1)])],
    'side': [L(outline([(58, 60), (62, 48), (82, 44), (94, 32), (102, 22, 1), (88, 16), (96, 2, 1), (74, 2), (78, -16, 1), (60, -4), (44, -12, 1), (36, 4), (14, 4, 1),
                        (14, 20), (-4, 30, 1), (6, 42), (-4, 56, 1), (8, 62), (6, 78, 1), (20, 72), (30, 80, 1), (38, 68), (48, 62)])),
             L(outline([(4, 40), (26, 46), (34, 72), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 84), (8, 62), (-4, 56, 1), (6, 46), (-6, 28, 1), (12, 22), (14, 4), (30, -6), (36, -24, 1), (44, -6), (60, -8), (76, -2), (92, 8, 1), (88, 22),
                        (106, 28, 1), (92, 44), (104, 56, 1), (92, 62), (86, 84), (72, 92, 1), (62, 84), (50, 94, 1), (40, 84), (28, 92, 1)])),
             L(outline([(56, -6), (86, 6), (98, 44), (90, 84), (64, 88), (70, 40)]), 'shade', 'b', False)],
}

# Carlton Lawstrom: moreno con el pelo verde petróleo oscuro en forma de seta (casquete redondo y corto con flequillo recto)
# y un rizo enroscado arriba; gafas redondas finas y sonrisa
CHARS[f'{V}:carlton-lawstrom'] = {
    'body': 'normal', 'pal': pal('#1e3a3c', '#b47e5a', iris='#3a7a6a', shade='#142a2c', deep='#0c1e20', light='#4a6a6a'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'glasses': (210, 200, 180, 255)},
    'front': [L(outline([(4, 56), (2, 34), (14, 10), (36, -2), (50, -4), (64, -2), (86, 10), (98, 34), (96, 56), (78, 62), (50, 60), (22, 62)])),
              L(rope((50, -2), (56, -20), (44, -18), 3.0)), L(rope((44, -18), (38, -14), (46, -10), 2.4)),
              L(outline([(60, -2), (86, 10), (98, 36), (90, 54), (76, 30)]), 'shade', 'b', False),
              strand([(10, 50), (50, 54), (90, 50)], 'light', 'b', 1.2), strand([(30, 4), (26, 40)], 'deep', 'b', 1.0), strand([(70, 4), (74, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(88, 52), (96, 36), (90, 12), (70, -2), (44, -4), (18, 6), (2, 30), (4, 52), (20, 74), (32, 82), (38, 64), (56, 56), (74, 56)])),
             L(rope((56, -2), (62, -20), (50, -18), 3.0)),
             L(outline([(4, 40), (30, 50), (36, 74), (20, 72)]), 'shade', 'b', False),
             strand([(10, 48), (50, 54), (90, 50)], 'light', 'b', 1.2)],
    'back': [L(outline([(2, 54), (2, 32), (14, 10), (50, -4), (86, 10), (98, 32), (98, 54), (80, 60), (64, 70), (50, 86, 1), (36, 70), (20, 60)])),
             L(rope((50, -2), (56, -20), (44, -18), 3.0)),
             L(outline([(56, -2), (86, 12), (98, 50), (70, 62), (66, 30)]), 'shade', 'b', False),
             strand([(6, 50), (50, 58), (94, 50)], 'light', 'b', 1.2)],
}

# Imogen Greenbourne: chica de pelo verde oliva con un flequillo de lado y dos trenzas en tirabuzón (con gomas oscuras)
# que le caen a los lados de la cara; cejas gruesas, pecas y ojos azul grisáceo
CHARS[f'{V}:imogen-greenbourne'] = {
    'body': 'chica', 'pal': pal('#9c9250', '#fde2cc', iris='#4a5a7a', shade='#7c7436', deep='#5e5626', tie='#2a2a2a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 84), (10, 56), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 56), (86, 84), (80, 66), (20, 66)])),
              L(outline([(60, 2), (82, 14), (90, 46), (86, 80), (78, 50)]), 'shade', 'b', False),
              fre([(12, 70), (12, 44), (24, 22), (46, 12), (70, 16), (86, 32), (92, 54), (84, 60), (72, 52), (60, 48), (48, 52), (36, 58), (24, 62), (18, 74)], 7),
              [L(ell(10 + 0.4 * k, 80 + 7 * k, 5.6 - 0.4 * k, 4.2)) for k in range(5)], L(ell(10, 77, 4.4, 1.6), 'tie', 'f', False),
              [L(ell(90 - 0.4 * k, 80 + 7 * k, 5.6 - 0.4 * k, 4.2)) for k in range(5)], L(ell(90, 77, 4.4, 1.6), 'tie', 'f', False)]
             + dots([(30, 86), (34, 88), (32, 90), (66, 86), (70, 88), (68, 90)]),
    'side': [L(outline([(60, 62), (62, 50), (82, 46), (92, 30), (82, 8), (58, -2), (32, 2), (12, 16), (4, 40), (6, 62), (20, 72), (40, 68), (50, 62)])),
             [L(ell(30 - 1.2 * k, 76 + 7 * k, 5.6 - 0.4 * k, 4.2)) for k in range(5)], L(ell(30, 73, 4.4, 1.6), 'tie', 'f', False),
             L(outline([(4, 40), (28, 46), (40, 66), (20, 70)]), 'shade', 'b', False),
             fr([(72, 48), (92, 40), (92, 56), (80, 58)])],
    'back': [L(outline([(16, 76), (12, 50), (14, 28), (28, 8), (50, 0), (72, 8), (86, 28), (88, 50), (84, 76), (50, 84)])),
             [L(ell(14 - 0.4 * k, 82 + 7 * k, 5.6 - 0.4 * k, 4.2)) for k in range(5)], L(ell(14, 79, 4.4, 1.6), 'tie', 'f', False),
             [L(ell(86 + 0.4 * k, 82 + 7 * k, 5.6 - 0.4 * k, 4.2)) for k in range(5)], L(ell(86, 79, 4.4, 1.6), 'tie', 'f', False),
             L(outline([(56, 2), (82, 14), (88, 50), (84, 76), (62, 80), (68, 40)]), 'shade', 'b', False)],
}

# Jewel Tremaine: chica de pelo malva tostado con dos coletas gruesas que salen hacia los lados y se curvan como cuernos;
# frente despejada con un rizo, ojos de estrella oscuros con pestañas marcadas, rubor y sonrisa
CHARS[f'{V}:jewel-tremaine'] = {
    'body': 'chica', 'pal': pal('#9a6a68', '#fde6d8', iris='#2a1e1e', shade='#7a504e', deep='#5e3a38', tie='#8a6ab8'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96,
             'hairline': [(16, 66), (20, 50), (32, 40), (44, 42), (50, 50), (56, 40), (68, 40), (80, 50), (84, 66)]},
    'front': [L(outline([(16, 80), (12, 56), (12, 32), (24, 10), (50, 2), (76, 10), (88, 32), (88, 56), (84, 80), (80, 60), (20, 60)])),
              L(outline([(14, 52), (0, 54), (-14, 64), (-20, 80), (-14, 96), (0, 106, 1), (-8, 92), (-6, 76), (4, 66), (16, 64)])),
              L(outline([(86, 52), (100, 54), (114, 64), (120, 80), (114, 96), (100, 106, 1), (108, 92), (106, 76), (96, 66), (84, 64)])),
              L(ell(13, 58, 2.6, 3.2), 'tie', 'f'), L(ell(87, 58, 2.6, 3.2), 'tie', 'f'),
              L(outline([(60, 4), (82, 16), (88, 48), (84, 74), (76, 40)]), 'shade', 'b', False),
              strand([(44, 42), (40, 36), (48, 32), (52, 38)], 'deep', 'f', 1.2)] + dots([(28, 86), (72, 86)], BLUSH, 2.4),
    'side': [L(outline([(58, 60), (60, 48), (80, 42), (88, 28), (78, 8), (56, 0), (30, 4), (12, 18), (6, 40), (8, 60), (20, 70), (40, 66), (48, 60)])),
             L(outline([(14, 40), (-4, 44), (-24, 56), (-34, 74), (-30, 90), (-18, 98, 1), (-22, 84), (-18, 70), (-4, 60), (12, 56)])),
             L(ell(14, 46, 3, 3.6), 'tie', 'f'),
             L(outline([(6, 40), (30, 44), (40, 64), (18, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 78), (12, 54), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (88, 54), (84, 78), (50, 84)])),
             L(outline([(14, 52), (0, 54), (-14, 64), (-20, 80), (-14, 96), (0, 106, 1), (-8, 92), (-6, 76), (4, 66), (16, 64)])),
             L(outline([(86, 52), (100, 54), (114, 64), (120, 80), (114, 96), (100, 106, 1), (108, 92), (106, 76), (96, 66), (84, 64)])),
             L(ell(14, 58, 2.6, 3.2), 'tie', 'f'), L(ell(86, 58, 2.6, 3.2), 'tie', 'f'),
             L(outline([(56, 2), (82, 14), (88, 50), (84, 76), (62, 82), (68, 40)]), 'shade', 'b', False),
             strand([(50, 4), (50, 80)], 'deep', 'b', 1.0)],
}

# Peridot Runehart: pelo gris oliva en forma de seta muy ancha (abultado a los lados a la altura de las sienes) con un
# mechón en forma de corazón en medio de la frente; ojos castaños redondos y sonrisa suave
CHARS[f'{V}:peridot-runehart'] = {
    'body': 'normal', 'pal': pal('#8a8a6c', '#fde4d4', iris='#5a3a1e', shade='#6c6c52', deep='#525240', low='#6a5a4a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 70), (6, 66), (-8, 56), (-10, 42), (0, 24), (20, 8), (36, -4), (50, -2), (64, -4), (80, 8), (100, 24), (110, 42), (108, 56), (94, 66),
                         (84, 70), (80, 60), (20, 60)])),
              L(outline([(60, -2), (84, 10), (106, 34), (104, 56), (90, 50), (78, 30)]), 'shade', 'b', False),
              fre([(14, 60), (16, 42), (30, 28), (50, 24), (70, 28), (84, 42), (86, 60), (76, 56), (62, 54), (56, 58), (52, 66, 1), (50, 60), (48, 66, 1), (44, 58),
                   (38, 54), (24, 56)], 7),
              strand([(26, 34), (8, 52)], 'deep', 'f', 1.0), strand([(74, 34), (92, 52)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 62), (64, 50), (84, 46), (94, 32), (86, 10), (60, -4), (30, 0), (8, 14), (-8, 36), (-6, 52), (8, 62), (24, 66), (40, 62), (50, 58)])),
             L(outline([(-6, 40), (30, 46), (44, 60), (24, 66), (4, 60)]), 'shade', 'b', False),
             fr([(76, 46), (92, 42), (94, 58), (90, 66), (84, 56)])],
    'back': [L(outline([(18, 78), (8, 66), (-8, 56), (-10, 42), (0, 24), (20, 8), (50, -4), (80, 8), (100, 24), (110, 42), (108, 56), (92, 66), (82, 78), (50, 90, 1)])),
             L(outline([(-8, 50), (30, 44), (50, 54), (70, 44), (108, 50), (92, 66), (82, 78), (50, 90), (18, 78), (8, 66)]), 'shade', 'b', False)],
}

# Summers Laughlin: moreno de cara redonda, pelo azul violáceo corto que sube en punta como una gota, con mechones cortos
# sobre la frente; cejas gruesas, ojos castaño rojizo, rubor y dos dientes de conejo
CHARS[f'{V}:summers-laughlin'] = {
    'body': 'normal', 'pal': pal('#5a5a8a', '#a8704c', iris='#7a2a1e', shade='#46466e', deep='#343456'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 96,
             'hairline': [(16, 70), (20, 56), (26, 50), (32, 56), (38, 48), (46, 54), (54, 48), (62, 54), (68, 48), (74, 56), (80, 52), (84, 70)]},
    'front': [L(outline([(16, 80), (12, 56), (16, 32), (30, 6), (50, -16, 1), (70, 6), (84, 32), (88, 56), (84, 80), (78, 60), (22, 60)])),
              L(outline([(56, -10), (72, 8), (86, 36), (84, 74), (74, 40)]), 'shade', 'b', False)] + dots([(28, 88), (72, 88)], BLUSH, 2.6),
    'side': [L(outline([(58, 62), (60, 52), (78, 48), (86, 36), (74, 10), (56, -10, 1), (34, 0), (14, 20), (6, 46), (10, 70), (24, 80), (40, 74), (48, 62)])),
             L(outline([(8, 46), (34, 40), (58, 52), (40, 74), (18, 76)]), 'shade', 'b', False),
             L(outline([(76, 46), (84, 44), (86, 54), (80, 52)]), 'mid', 'f')],
    'back': [L(outline([(16, 80), (12, 56), (16, 32), (30, 8), (50, -16, 1), (70, 8), (84, 32), (88, 56), (84, 80), (50, 88)])),
             L(outline([(14, 54), (40, 46), (60, 50), (88, 54), (84, 80), (50, 88), (16, 80)]), 'shade', 'b', False)],
}

# Kean Aimes: pelo granate abultado y revuelto con un flequillo enorme que le baja en curva sobre un ojo, y puntas cortas
# hacia fuera abajo; ojos castaños, rubor en la nariz y media sonrisa
CHARS[f'{V}:kean-aimes'] = {
    'body': 'normal', 'pal': pal('#a01e3a', '#fde2cc', iris='#5a3a2a', shade='#7e162c', deep='#5e1020', light='#c84a6a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 88), (8, 80), (-4, 84, 1), (4, 72), (2, 46), (6, 24), (20, 4), (40, -10), (62, -8), (82, 4), (96, 24), (98, 46), (94, 72), (102, 80, 1),
                         (90, 84), (84, 88), (80, 64), (20, 64)])),
              L(outline([(62, -6), (86, 8), (98, 40), (92, 80), (80, 50)]), 'shade', 'b', False),
              fre([(12, 70), (12, 40), (26, 18), (50, 10), (72, 18), (88, 38), (88, 66), (84, 56), (76, 50), (66, 52), (56, 62), (46, 74), (36, 76, 1), (40, 66), (30, 58),
                   (20, 64)], 7),
              strand([(30, 20), (50, 40), (56, 60)], 'deep', 'f', 1.0), strand([(56, 14), (70, 30)], 'deep', 'f', 1.0),
              L(ell(50, 84, 5, 2.2), BLUSH, 'f', False)],
    'side': [L(outline([(60, 66), (62, 52), (82, 48), (96, 34), (94, 10), (72, -8), (44, -10), (18, 0), (4, 22), (0, 48), (6, 74), (-2, 86, 1), (14, 82), (22, 92, 1),
                        (30, 80), (44, 72)])),
             L(outline([(2, 46), (28, 50), (40, 72), (14, 82), (4, 72)]), 'shade', 'b', False),
             fr([(72, 48), (92, 40), (96, 60), (86, 76, 1), (80, 60)])],
    'back': [L(outline([(14, 88), (6, 76), (-8, 80, 1), (4, 66), (2, 40), (8, 20), (24, 2), (50, -10), (76, 2), (92, 20), (98, 40), (96, 66), (108, 80, 1), (94, 76),
                        (86, 88), (70, 94, 1), (60, 86), (50, 96, 1), (40, 86), (30, 94, 1)])),
             L(outline([(4, 54), (40, 64), (60, 60), (98, 54), (96, 66), (86, 88), (60, 86), (40, 86), (14, 88), (4, 66)]), 'shade', 'b', False),
             L(outline([(56, -8), (84, 6), (98, 40), (76, 50), (70, 20)]), 'shade', 'b', False)],
}

# Reamond Lockhard: pelo verde oscuro en un afro grande y esponjoso, más ancho abajo, con un flequillo de rizos sobre la
# frente; cejas gruesas y una sonrisa enorme enseñando los dientes
CHARS[f'{V}:reamond-lockhard'] = {
    'body': 'normal', 'pal': pal('#3a4a2a', '#fde2cc', iris='#2a2a1e', shade='#2a381e', deep='#1e2814'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'grin', 'mouth_y': 96,
             'hairline': [(14, 68), (20, 60), (28, 62), (36, 56), (44, 60), (52, 56), (60, 60), (68, 56), (76, 62), (82, 58), (86, 68)]},
    'front': [L(bumpy(50, 20, 50, 40, n=14, amp=0.08)), L(bumpy(50, 50, 56, 18, n=12, amp=0.1)),
              L(outline([(56, -14), (94, 8), (106, 50), (90, 64), (80, 30)]), 'shade', 'b', False)],
    'side': [L(bumpy(44, 22, 52, 40, n=14, amp=0.08)), L(bumpy(36, 52, 46, 20, n=12, amp=0.1)),
             L(outline([(-6, 40), (40, 52), (60, 60), (30, 72), (0, 64)]), 'shade', 'b', False)],
    'back': [L(bumpy(50, 20, 52, 40, n=14, amp=0.08)), L(bumpy(50, 54, 58, 22, n=12, amp=0.1)),
             L(outline([(-6, 50), (50, 60), (106, 50), (100, 70), (50, 80), (0, 70)]), 'shade', 'b', False)],
}

# Beryl Granger: pelo castaño oscuro recogido en un moño de pinchos arriba, con mechones en punta a los lados; horquilla
# rosa, gafas rectangulares granates y sonrisa pícara
CHARS[f'{V}:beryl-granger'] = {
    'body': 'normal', 'pal': pal('#4a3028', '#fde2cc', iris='#3a2a2a', shade='#38241e', deep='#281812', clip='#e070b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 80), (12, 56), (12, 34), (24, 12), (40, 2), (60, 2), (76, 10), (88, 26), (100, 24, 1), (90, 40), (88, 56), (84, 80), (80, 60), (20, 60)])),
              L(outline([(26, 8), (14, -10, 1), (30, -2), (34, -16, 1), (44, -2), (50, 8)])),
              L(outline([(60, 4), (82, 16), (90, 40), (86, 76), (78, 46)]), 'shade', 'b', False),
              fr([(14, 66), (14, 42), (26, 22), (46, 14), (70, 18), (86, 30), (102, 32, 1), (88, 40), (84, 52), (74, 46), (60, 44), (48, 50), (36, 56), (26, 62), (20, 72)]),
              L([(62, 28), (72, 18)], 'clip', 'f', False, False, 2.0), rect_glasses('front', 76, (150, 30, 50, 255))],
    'side': [L(outline([(58, 62), (60, 50), (80, 44), (92, 30), (84, 10), (60, 0), (34, 4), (14, 18), (6, 42), (8, 66), (22, 76), (40, 70), (50, 62)])),
             L(outline([(30, 6), (16, -14, 1), (34, -6), (40, -22, 1), (50, -4), (56, 4)])),
             L(outline([(6, 42), (30, 46), (42, 68), (22, 74)]), 'shade', 'b', False),
             rect_glasses('side', 76, (150, 30, 50, 255))],
    'back': [L(outline([(16, 80), (12, 56), (12, 34), (24, 12), (40, 2), (60, 2), (76, 12), (88, 34), (88, 56), (84, 80), (50, 86)])),
             L(outline([(36, 10), (24, -10, 1), (40, -4), (50, -20, 1), (58, -4), (74, -8, 1), (66, 10)])),
             L(outline([(8, 50), (-4, 46, 1), (10, 40)])),
             L(outline([(56, 4), (82, 16), (88, 50), (84, 78), (62, 84), (68, 40)]), 'shade', 'b', False)],
}

# Quip Netley: pelo malva con flequillo recto de mechones cortos y una coleta baja atada con una goma verde en la nuca;
# ojos cerrados de felicidad, rubor y una sonrisa grande con la boca abierta
CHARS[f'{V}:quip-netley'] = {
    'body': 'normal', 'pal': pal('#9a5a6c', '#fde2cc', iris='#2a1e1e', shade='#7a4252', deep='#5e2e3c', tie='#3a7a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 72), (12, 50), (14, 30), (28, 10), (50, 4), (72, 10), (86, 30), (88, 50), (84, 72), (78, 56), (22, 56)])),
              L(outline([(60, 6), (82, 18), (88, 46), (84, 68), (76, 40)]), 'shade', 'b', False),
              fre([(14, 56), (16, 36), (30, 22), (50, 18), (70, 22), (84, 36), (86, 56), (78, 50), (68, 52), (66, 60, 1), (60, 52), (56, 62, 1), (50, 54), (44, 62, 1),
                   (40, 52), (34, 60, 1), (32, 52), (22, 50)], 7),
              L(quad((30, 64), (36, 60), (42, 64)), OUTC, 'f', False, False, 1.8), L(quad((58, 64), (64, 60), (70, 64)), OUTC, 'f', False, False, 1.8)]
             + arcs(78) + dots([(26, 86), (74, 86)], BLUSH, 3.0),
    'side': [L(outline([(60, 60), (62, 48), (80, 42), (90, 30), (80, 10), (56, 2), (30, 6), (12, 20), (6, 44), (10, 68), (24, 78), (40, 72), (50, 62)])),
             L(rope((22, 74), (16, 90), (20, 106), 6)), L(ell(20, 84, 4, 2.4), 'tie', 'f'),
             L(outline([(6, 44), (30, 48), (40, 70), (20, 76)]), 'shade', 'b', False),
             fr([(74, 42), (92, 40), (92, 52), (80, 52)])],
    'back': [L(outline([(16, 74), (12, 50), (14, 30), (28, 10), (50, 4), (72, 10), (86, 30), (88, 50), (84, 74), (60, 86), (40, 86)])),
             L(rope((50, 80), (54, 96), (50, 110), 7)), L(ell(51, 90, 4.4, 2.6), 'tie', 'f'),
             L(outline([(56, 6), (82, 18), (88, 50), (84, 72), (60, 84), (66, 40)]), 'shade', 'b', False),
             strand([(50, 6), (40, 30), (48, 80)], 'deep', 'b', 1.0)],
}

# Kata Caballo (portera): morena de pelo azul marino con mechones largos que se curvan hacia la cara desde los lados y un
# flequillo grande en curva sobre un ojo; ojos azules con raya marcada, rubor y sonrisa de dientes
CHARS[f'{V}:kata-caballo'] = {
    'body': 'chica', 'pal': pal('#1e3a7a', '#b07a54', iris='#4a6ab0', shade='#162c5e', deep='#0e1e44'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 86), (8, 60), (8, 32), (22, 8), (50, -2), (78, 8), (94, 28), (104, 50), (98, 52), (90, 40), (90, 64), (86, 86), (80, 64), (20, 64)])),
              L(outline([(62, 0), (86, 12), (96, 40), (88, 80), (80, 50)]), 'shade', 'b', False),
              fr([(12, 72), (12, 44), (26, 20), (50, 12), (74, 20), (88, 42), (88, 70), (82, 56), (72, 50), (60, 50), (50, 58), (42, 72), (34, 76, 1), (36, 62), (28, 58),
                  (20, 68)]),
              L(rope((16, 60), (4, 84), (12, 104), 4), 'mid', 'f'), L(rope((84, 60), (96, 84), (88, 104), 4), 'mid', 'f')] + dots([(28, 88), (72, 88)], BLUSH, 2.4),
    'side': [L(outline([(60, 62), (62, 50), (82, 46), (94, 32), (90, 10), (68, -4), (40, -4), (16, 6), (4, 30), (4, 60), (16, 82), (34, 84), (44, 72), (50, 62)])),
             L(outline([(4, 40), (28, 46), (40, 74), (16, 80)]), 'shade', 'b', False),
             L(rope((70, 46), (90, 56), (82, 92), 4), 'mid', 'f')],
    'back': [L(outline([(12, 86), (6, 60), (8, 30), (22, 8), (50, -2), (78, 8), (92, 30), (94, 60), (88, 86), (68, 92), (50, 88), (32, 92)])),
             L(rope((10, 40), (-6, 70), (8, 96), 3.4)), L(rope((90, 40), (106, 70), (92, 96), 3.4)),
             L(outline([(56, 0), (84, 14), (94, 50), (88, 86), (64, 90), (70, 40)]), 'shade', 'b', False)],
}

# Asuna Sugami: chica de pelo rubio pálido muy abultado y ondulado, con rizos grandes a los lados y un rizo en espiral que le
# sale arriba como una antena; ojos verdes grandes, rubor y sonrisa
CHARS[f'{V}:asuna-sugami'] = {
    'body': 'chica', 'pal': pal('#f0e2aa', '#fde6d8', iris='#4a8a6a', shade='#d4c286', deep='#a8946a', ahoge='#a8866a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 96), (0, 82), (4, 68), (-6, 50), (0, 28), (16, 8), (40, -4), (60, -4), (84, 8), (100, 28), (106, 50), (96, 68), (100, 82), (88, 96),
                         (80, 74), (20, 74)])),
              L(rope((44, -2), (30, -20), (52, -22), 2.4), 'ahoge', 'b'), L(rope((52, -22), (66, -18), (58, -8), 2.0), 'ahoge', 'b'),
              L(outline([(60, -2), (86, 10), (104, 46), (94, 90), (82, 60)]), 'shade', 'b', False),
              fre([(12, 74), (12, 44), (26, 22), (50, 14), (74, 22), (88, 44), (88, 74), (82, 60), (72, 54), (64, 60, 1), (58, 50), (48, 56), (40, 64, 1), (36, 54), (26, 58),
                   (18, 72)], 7),
              strand([(30, 30), (40, 44)], 'deep', 'f', 1.0), strand([(66, 26), (72, 40)], 'deep', 'f', 1.0)] + dots([(28, 88), (72, 88)], BLUSH, 2.6),
    'side': [L(outline([(60, 70), (62, 54), (82, 48), (96, 34), (94, 12), (74, -4), (46, -6), (20, 2), (2, 22), (-6, 48), (0, 74), (6, 90), (24, 96), (40, 88), (48, 70)])),
             L(rope((50, -4), (40, -24), (64, -24), 2.4), 'ahoge', 'b'),
             L(outline([(-4, 48), (26, 52), (40, 88), (10, 90)]), 'shade', 'b', False),
             fr([(72, 50), (90, 44), (92, 66), (82, 80, 1), (78, 64)])],
    'back': [L(outline([(10, 94), (0, 76), (-6, 50), (0, 26), (18, 6), (50, -4), (82, 6), (100, 26), (106, 50), (100, 76), (90, 94), (70, 100), (50, 92), (30, 100)])),
             L(rope((44, -2), (30, -20), (52, -22), 2.4), 'ahoge', 'b'),
             L(outline([(0, 50), (40, 56), (60, 48), (104, 50), (100, 76), (90, 94), (70, 100), (50, 92), (30, 100), (10, 94), (0, 76)]), 'shade', 'b', False)],
}
