"""Olé de Samba (orion-ol-de-samba): sus modelos 3D de Inazuma Eleven: Orion no Kokuin (オリオンの刻印) en la enciclopedia, de
frente, perfil y espalda. Todos tienen una sola forma y ninguno coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_orion_arab_no_hi_no_tori_gundan import clipx, clipy, curls  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)

# Gonçalo (Macero, portero): flaco y de cara alargada; pelo morado oscuro abultado arriba con una nube enorme de pelo
# lila claro que le sale disparada hacia un lado; ojos redondos, cejas finas de enfado, nariz larga con la punta roja
LILA = (214, 172, 204, 255)
LILA_D = (180, 136, 172, 255)
CHARS['gon-alo'] = {
    'body': 'delgado', 'pal': pal('#6c2c6c', '#fcd2b2', shade='#521e52', deep='#3c143c', nose='#e88070'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(18, 62), (28, 50), (44, 52), (56, 46), (70, 48), (82, 62)],
             'nose': (50, 86, 2.2)},
    'front': [L(outline([(18, 64), (14, 46), (18, 24), (30, 4), (50, -6), (72, -4), (88, 10), (92, 32), (86, 50), (82, 64), (74, 54), (26, 54)])),
              L(outline([(60, -4), (78, 0), (90, 14), (92, 32), (86, 50), (78, 30)]), 'shade', 'b', False),
              L(curls(6, 16, (32, 24), 7, 0.4, 0.84), LILA, 'f'), L(curls(-16, 8, (16, 13), 5, 0.1, 0.84), LILA, 'f'),
              L(curls(0, 26, (18, 10), 5, 0.2, 0.84), LILA_D, 'f', False)],
    'side': [L(outline([(76, 56), (82, 44), (86, 28), (78, 10), (60, -2), (34, -4), (14, 6), (4, 26), (4, 52), (10, 72), (26, 78), (40, 70), (44, 58), (56, 56), (66, 56)])),
             L(outline([(4, 26), (4, 52), (10, 72), (26, 78), (40, 70), (44, 58), (24, 44)]), 'shade', 'b', False),
             L(curls(86, 18, (28, 22), 7, 0.4, 0.84), LILA, 'f'), L(curls(94, 28, (16, 12), 5, 0.2, 0.84), LILA_D, 'f', False)],
    'back': [L(outline([(20, 82), (16, 50), (18, 24), (30, 4), (50, -6), (70, -4), (84, 10), (86, 34), (80, 60), (76, 84), (50, 90)])),
             L(outline([(56, -4), (76, 2), (86, 34), (80, 60), (76, 84), (60, 88), (62, 30)]), 'shade', 'b', False),
             L(curls(92, 22, (24, 22), 7, 0.3, 0.84), LILA, 'b'), L(curls(96, 30, (14, 12), 5, 0.2, 0.84), LILA_D, 'b', False)],
}

# Bernardo (Ricardo): grandullón de piel oscura con pecas; una nube de rizos blanco lila que le tapa un ojo y le cae en
# bucles a los lados de la cara; el otro ojo turquesa y una sonrisa con un diente
CLOUD_D = (196, 186, 204, 255)
CHARS['bernardo'] = {
    'body': 'corpulento', 'pal': pal('#e6e2ea', '#8a5a3c', iris='#2a9aa0', shade='#c4bccc', deep='#9e94a8', freckle='#6a4028'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(curls(50, 30, (48, 34), 9, 0.2, 0.86)),
              L(curls(10, 80, (16, 14), 5, 0.3, 0.84)), L(curls(90, 80, (16, 14), 5, 0.6, 0.84)), L(curls(14, 100, (12, 10), 4, 0.1, 0.84)), L(curls(86, 100, (12, 10), 4, 0.5, 0.84)),
              L(curls(40, 52, (30, 20), 7, 0.4, 0.86), 'mid', 'f', ln=True), L(curls(42, 58, (18, 10), 5, 0.4, 0.86), CLOUD_D, 'f', False),
              L(curls(78, 50, (14, 10), 5, 0.3, 0.86), 'mid', 'f', ln=True),
              L([(57, 76), (71, 74), (71, 80), (58, 81)], WHITE, 'f', False), L(ell(65, 77.5, 2.8, 3.2), 'iris', 'f', False), L(ell(65, 77.5, 1.2, 1.6), OUTC, 'f', False),
              L([(56, 74), (72, 72)], OUTC, 'f', False, False, 2.4),
              L([(48, 93), (52, 93), (52, 97), (48, 97)], WHITE, 'f', False),
              L(ell(34, 82, 0.9, 0.9), 'freckle', 'f', False), L(ell(38, 84, 0.9, 0.9), 'freckle', 'f', False), L(ell(62, 84, 0.9, 0.9), 'freckle', 'f', False),
              L(ell(66, 82, 0.9, 0.9), 'freckle', 'f', False)],
    'side': [L(curls(40, 40, (48, 40), 10, 0.2, 0.86)), L(curls(20, 82, (20, 16), 6, 0.3, 0.84)),
             L(clipy(curls(40, 40, (48, 40), 10, 0.2, 0.86), 50, 100), 'shade', 'b', False),
             L(curls(74, 54, (16, 12), 5, 0.3, 0.86), 'mid', 'f', ln=True)],
    'back': [L(curls(50, 44, (50, 42), 10, 0.2, 0.86)), L(curls(6, 80, (16, 12), 5, 0.3, 0.84)), L(curls(94, 80, (16, 12), 5, 0.6, 0.84)),
             L(curls(50, 86, (34, 12), 7, 0.3, 0.84)),
             L(clipy(curls(50, 44, (50, 42), 10, 0.2, 0.86), 54, 100), 'shade', 'b', False)],
}

# Maceió (Matheus): flaco, un afro magenta enorme y redondo; cara alargada y pálida, ojos pequeños afilados y una
# sonrisa ancha de pillo
CHARS['macei'] = {
    'body': 'delgado', 'pal': pal('#c02262', '#fcdcc4', iris='#3a3a3a', shade='#961a4c', deep='#6e1238'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 70), (24, 62), (40, 58), (50, 64), (60, 58), (76, 62), (84, 70)]},
    'front': [L(curls(50, 28, (56, 46), 11, 0.1, 0.88)), L(clipx(curls(50, 28, (56, 46), 11, 0.1, 0.88), 60, 120), 'shade', 'b', False),
              L(quad((40, 96), (50, 99), (60, 95)), OUTC, 'f', False, False, 1.0)],
    'side': [L(curls(42, 30, (54, 46), 11, 0.1, 0.88)), L(clipx(curls(42, 30, (54, 46), 11, 0.1, 0.88), -20, 24), 'shade', 'b', False),
             ],
    'back': [L(curls(50, 30, (56, 48), 11, 0.1, 0.88)), L(clipx(curls(50, 30, (56, 48), 11, 0.1, 0.88), 60, 120), 'shade', 'b', False),
             ],
}

# João (Marcelo): pelo azul intenso en pinchos revueltos hacia arriba y a los lados, con mechones sobre la frente y
# patillas en punta; ojos grandes gris lavanda
CHARS['jo-o'] = {
    'body': 'normal', 'pal': pal('#3a72d2', '#fdddc4', iris='#6c6aa8', shade='#2a56a4', deep='#1c3c7a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'line', 'hairline': [(14, 64), (24, 52), (40, 50), (50, 56), (60, 50), (76, 52), (86, 64)]},
    'front': [L(outline([(16, 74), (8, 56), (-6, 42, 1), (8, 36), (2, 18, 1), (16, 14), (20, -4, 1), (32, 6), (44, -6, 1), (52, 4), (64, -12, 1), (68, 4), (82, 2, 1),
                         (82, 16), (98, 26, 1), (90, 34), (100, 48, 1), (88, 52), (84, 74), (76, 56), (24, 56)])),
              L(outline([(52, 4), (64, -12), (68, 4), (82, 2), (82, 16), (98, 26), (90, 34), (100, 48), (88, 54), (74, 30)]), 'shade', 'b', False),
              strand([(30, 12), (36, 28), (32, 40)], 'deep', 'b', 1.0), strand([(58, 8), (64, 24), (72, 34)], 'deep', 'b', 1.0),
              L(outline([(26, 48), (38, 40), (54, 38), (70, 42), (80, 50), (70, 50), (62, 62, 1), (56, 48), (46, 62, 1), (42, 48), (32, 56, 1)]), 'mid', 'f', ln=True),
              L(outline([(16, 58), (24, 56), (22, 80, 1)]), 'deep', 'f'), L(outline([(84, 58), (76, 56), (78, 80, 1)]), 'deep', 'f')],
    'side': [L(outline([(74, 58), (80, 46), (90, 42, 1), (82, 34), (96, 22, 1), (80, 18), (84, 2, 1), (66, 8), (62, -8, 1), (50, 4), (30, -6, 1), (30, 8), (8, 8, 1),
                        (16, 20), (-6, 28, 1), (8, 38), (-8, 50, 1), (8, 54), (-2, 68, 1), (12, 68), (14, 84, 1), (26, 74), (36, 76), (44, 62), (56, 56), (64, 60)])),
             L(outline([(-8, 50), (8, 54), (-2, 68), (12, 68), (14, 84), (26, 74), (36, 76), (44, 62), (24, 52), (10, 40)]), 'shade', 'b', False),
             strand([(58, 6), (66, 22), (78, 30)], 'deep', 'b', 1.0),
             L(outline([(72, 50), (84, 52), (82, 70, 1)]), 'mid', 'f', ln=True), L(outline([(54, 62), (58, 60), (58, 80, 1)]), 'deep', 'f')],
    'back': [L(outline([(18, 70), (6, 58, 1), (12, 48), (0, 36, 1), (14, 28), (8, 10, 1), (24, 12), (30, -6, 1), (42, 4), (52, -10, 1), (58, 4), (70, -4, 1), (72, 10),
                        (90, 8, 1), (86, 24), (100, 32, 1), (88, 42), (96, 56, 1), (84, 62), (82, 80), (64, 86), (50, 96, 1), (36, 86), (20, 82)])),
             L(outline([(58, 4), (70, -4), (72, 10), (90, 8), (86, 24), (100, 32), (88, 42), (96, 56), (84, 62), (82, 80), (64, 86), (62, 40)]), 'shade', 'b', False),
             ],
}

# Luís (Lucian): piel morena; un moño afro azul marino casi negro arriba, sobre los lados cortos azul marino más claro;
# cejas gruesas azul oscuro de enfado, ojos verde azulado y morros de enfurruñado
NAVY_L = (74, 78, 140, 255)
CHARS['lu-s'] = {
    'body': 'normal', 'pal': pal('#1e2052', '#aa744c', iris='#1e8a9a', shade='#14163c', deep='#0c0e28', side=NAVY_L),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 1, 'hairline': [(16, 60), (22, 46), (40, 42), (50, 44), (60, 42), (78, 46), (84, 60)]},
    'front': [L(blob([(17, 62), (15, 40), (24, 22), (50, 16), (76, 22), (85, 40), (83, 62)]), 'side'),
              L(curls(50, 2, (40, 22), 9, 0.2, 0.86)), L(curls(58, -14, (16, 12), 5, 0.2, 0.86)),
              L(clipx(curls(50, 2, (40, 22), 9, 0.2, 0.86), 62, 120), 'shade', 'b', False),
              L(outline([(24, 62), (44, 66, 1), (43, 70), (26, 67)]), 'mid', 'f', False), L(outline([(76, 62), (56, 66, 1), (57, 70), (74, 67)]), 'mid', 'f', False)],
    'side': [L(blob([(44, 90), (22, 92), (14, 66), (16, 38), (34, 20), (60, 18), (80, 28), (86, 50), (64, 54)]), 'side'),
             L(curls(52, 0, (44, 22), 9, 0.2, 0.86)), L(curls(68, -14, (18, 12), 5, 0.2, 0.86)),
             L(clipx(curls(52, 0, (44, 22), 9, 0.2, 0.86), -20, 24), 'shade', 'b', False),
             L(outline([(72, 61), (86, 65, 1), (85, 68), (73, 66)]), 'mid', 'f', False)],
    'back': [L(blob([(16, 66), (14, 40), (24, 22), (50, 16), (76, 22), (86, 40), (84, 66), (70, 80), (50, 84), (30, 80)]), 'side'),
             L(curls(50, 4, (42, 22), 9, 0.2, 0.86)), L(curls(40, -12, (16, 12), 5, 0.2, 0.86)),
             L(clipx(curls(50, 4, (42, 22), 9, 0.2, 0.86), 62, 120), 'shade', 'b', False)],
}

# Belo (Renato): piel morena, pelo en casco: rubio por delante, con un flequillo largo que le tapa medio lado de la cara,
# y castaño por detrás y en la nuca, con un remolino oscuro en lo alto; ojos azul violeta y sonrisa
BROWN = (168, 104, 44, 255)
BROWN_D = (130, 78, 30, 255)
CHARS['belo'] = {
    'body': 'normal', 'pal': pal('#f2c42c', '#b07a4c', iris='#5a5aa8', shade='#d29a20', deep='#9a6a14', back=BROWN, back_d=BROWN_D),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'hairline': [(14, 70), (20, 54), (36, 46), (50, 46), (64, 46), (80, 54), (86, 70)]},
    'front': [L(outline([(14, 96), (8, 80), (10, 50), (18, 26), (34, 12), (50, 8), (66, 12), (82, 26), (90, 50), (92, 80), (86, 96), (80, 76), (20, 76)])),
              L(outline([(58, 10), (78, 20), (90, 50), (92, 80), (86, 96), (80, 60), (72, 30)]), 'shade', 'b', False),
              L(outline([(50, 16), (52, 20), (56, 20), (53, 23), (54, 27), (50, 25), (46, 27), (47, 23), (44, 20), (48, 20)]), 'shade', 'b', False),
              L(outline([(70, 40), (52, 36), (34, 42), (20, 54), (14, 76), (16, 96, 1), (24, 76), (30, 64), (40, 56), (56, 50), (66, 50), (80, 56), (84, 66, 1), (82, 48)]),
                'mid', 'f', ln=True)],
    'side': [L(outline([(76, 56), (84, 44), (84, 26), (70, 10), (46, 4), (24, 12), (8, 30), (4, 56), (10, 80), (30, 88), (40, 78), (44, 62), (56, 56), (66, 56)]), 'back'),
             L(outline([(8, 30), (4, 56), (10, 80), (30, 88), (40, 78), (44, 62), (24, 50)]), 'back_d', 'b', False),
             L(outline([(52, 20), (70, 10), (84, 26), (84, 44), (88, 80), (84, 100, 1), (76, 76), (70, 56), (60, 40)])),
             L(outline([(72, 48), (86, 50), (88, 82), (84, 100, 1), (76, 76)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 84), (10, 56), (16, 30), (32, 14), (50, 10), (68, 14), (84, 30), (90, 56), (84, 84), (50, 90)]), 'back'),
             L(outline([(56, 12), (78, 22), (90, 56), (84, 84), (62, 88)]), 'back_d', 'b', False),
             strand([(44, 20), (40, 60)], BROWN_D, 'b', 1.0), strand([(60, 22), (64, 60)], BROWN_D, 'b', 1.0)],
}

# Igaçu (Daninho): una melena granate oscuro en pinchos largos que le cae como una crin hasta los hombros, con pico en la
# frente; cara grande y cuadrada, ojos redondos de enfado, nariz ancha y boca apretada
CHARS['iga-u'] = {
    'body': 'normal', 'pal': pal('#8a0c12', '#fcd6ae', iris='#202020', shade='#6a080c', deep='#4a0408'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(18, 60), (24, 48), (36, 42), (50, 52), (64, 42), (76, 48), (82, 60)],
             'nose': (50, 86, 3.0)},
    'front': [L(outline([(18, 80), (4, 104, 1), (6, 84), (-10, 80, 1), (4, 66), (-12, 56, 1), (4, 46), (-6, 30, 1), (10, 24), (8, 6, 1), (22, 10), (26, -10, 1), (38, 0),
                         (50, -16, 1), (62, 0), (74, -10, 1), (78, 10), (92, 6, 1), (90, 24), (106, 30, 1), (96, 46), (112, 56, 1), (96, 66), (110, 80, 1), (94, 84), (96, 104, 1),
                         (82, 80), (80, 60), (20, 60)])),
              L(outline([(62, 0), (74, -10), (78, 10), (92, 6), (90, 24), (106, 30), (96, 46), (112, 56), (96, 66), (110, 80), (94, 84), (96, 104), (82, 80), (78, 40)]),
                'shade', 'b', False),
              strand([(30, 10), (36, 30)], 'deep', 'b', 1.0), strand([(64, 10), (60, 30)], 'deep', 'b', 1.0)],
    'side': [L(outline([(74, 52), (82, 40), (84, 22), (74, 6), (60, -14, 1), (52, 2), (36, -16, 1), (32, 4), (12, -6, 1), (14, 12), (-10, 14, 1), (2, 28), (-18, 40, 1),
                        (-2, 48), (-20, 64, 1), (-2, 68), (-14, 88, 1), (4, 84), (0, 104, 1), (16, 92), (24, 106, 1), (30, 86), (40, 70), (44, 58), (56, 54), (66, 52)])),
             L(outline([(-18, 40), (-2, 48), (-20, 64), (-2, 68), (-14, 88), (4, 84), (0, 104), (16, 92), (24, 106), (30, 86), (40, 70), (24, 54), (10, 36)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 104, 1), (4, 84), (-10, 80, 1), (4, 66), (-12, 56, 1), (4, 46), (-6, 30, 1), (10, 24), (8, 6, 1), (22, 10), (26, -10, 1), (38, 0), (50, -16, 1),
                        (62, 0), (74, -10, 1), (78, 10), (92, 6, 1), (90, 24), (106, 30, 1), (96, 46), (112, 56, 1), (96, 66), (110, 80, 1), (96, 84), (86, 104, 1), (74, 94),
                        (64, 108, 1), (56, 94), (46, 108, 1), (38, 94), (26, 106, 1), (22, 92)])),
             L(outline([(62, 0), (74, -10), (78, 10), (92, 6), (90, 24), (106, 30), (96, 46), (112, 56), (96, 66), (110, 80), (96, 84), (86, 104), (74, 94), (66, 40)]), 'shade', 'b', False),
             strand([(40, 20), (36, 70)], 'deep', 'b', 1.0), strand([(56, 20), (60, 70)], 'deep', 'b', 1.0)],
}

# Manaus (Rolan): rastas negras con reflejos magenta en la raíz, que salen hacia arriba y se curvan hacia fuera a los
# lados hasta el cuello; piel morena, ojos tranquilos y media sonrisa
MAG = (110, 50, 100, 255)


def locks(pts, w=3.4, c='mid', z='b'):
    """Rasta: cordón grueso con contorno que sigue la línea de puntos (suavizada)."""
    import math
    line = []
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        line += [(a[0] + (b[0] - a[0]) * t / 5, a[1] + (b[1] - a[1]) * t / 5) for t in range(5)]
    line.append(pts[-1])
    left, right = [], []
    for i, p in enumerate(line):
        q0, q1 = line[max(0, i - 1)], line[min(len(line) - 1, i + 1)]
        dx, dy = q1[0] - q0[0], q1[1] - q0[1]
        n = math.hypot(dx, dy) or 1
        k = w * (1 - 0.35 * i / len(line))
        left.append((p[0] - dy / n * k, p[1] + dx / n * k))
        right.append((p[0] + dy / n * k, p[1] - dx / n * k))
    return L(left + right[::-1], c, z)


CHARS['manaus'] = {
    'body': 'normal', 'pal': pal('#1e1c2e', '#c08a5e', iris='#2a2a3a', shade='#14121e', deep='#0a0a12', mag=MAG),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'hairline': [(16, 62), (24, 48), (36, 42), (50, 40), (64, 42), (76, 48), (84, 62)]},
    'front': [L(outline([(18, 62), (12, 40), (20, 16), (36, 2), (50, -6), (64, 2), (80, 16), (88, 40), (82, 62), (76, 52), (24, 52)])),
              L(outline([(24, 50), (34, 40), (50, 38), (66, 40), (76, 50), (66, 32), (50, 28), (34, 32)]), 'mag', 'b', False),
              locks([(18, 26), (4, 30), (-4, 44), (2, 52)]), locks([(16, 40), (6, 50), (4, 66), (10, 74)]), locks([(18, 52), (14, 70), (16, 88), (12, 98)]),
              locks([(82, 26), (96, 30), (104, 44), (98, 52)]), locks([(84, 40), (94, 50), (96, 66), (90, 74)]), locks([(82, 52), (86, 70), (84, 88), (88, 98)]),
              locks([(30, 8), (22, -2), (12, -2)]), locks([(70, 8), (78, -2), (88, -2)])],
    'side': [L(outline([(76, 56), (82, 44), (84, 26), (72, 8), (50, -2), (28, 2), (12, 16), (6, 40), (14, 62), (30, 70), (40, 64), (44, 56), (56, 54), (66, 54)])),
             L(outline([(70, 46), (80, 40), (82, 28), (74, 32)]), 'mag', 'b', False),
             locks([(20, 14), (4, 6), (-10, 12)]), locks([(12, 30), (-4, 34), (-14, 50), (-10, 60)]), locks([(10, 46), (-2, 60), (-4, 76), (2, 84)]),
             locks([(20, 60), (14, 76), (16, 92), (8, 102)]), locks([(34, 66), (32, 84), (36, 96), (30, 104)]), locks([(44, 0), (40, -8), (30, -10)])],
    'back': [L(outline([(18, 76), (12, 46), (20, 18), (36, 4), (50, -4), (64, 4), (80, 18), (88, 46), (82, 76), (50, 82)])),
             locks([(18, 26), (4, 30), (-6, 44), (0, 52)]), locks([(16, 42), (6, 52), (4, 68), (10, 76)]), locks([(20, 60), (16, 78), (18, 94), (12, 104)]),
             locks([(82, 26), (96, 30), (106, 44), (100, 52)]), locks([(84, 42), (94, 52), (96, 68), (90, 76)]), locks([(80, 60), (84, 78), (82, 94), (88, 104)]),
             locks([(36, 74), (34, 90), (30, 100)]), locks([(64, 74), (66, 90), (70, 100)]),
             locks([(30, 10), (22, 0), (12, 0)]), locks([(70, 10), (78, 0), (88, 0)])],
}

# André (Samuel): media melena rubio crema con dos mechas negras, cortada en casco y con las puntas que se abren hacia
# fuera a la altura de las orejas; ojos ámbar y sonrisa
STREAK = (40, 40, 44, 255)
CHARS['andr'] = {
    'body': 'bajito', 'pal': pal('#fcf0c2', '#fde0c6', iris='#c8861e', shade='#e0cc96', deep='#b8a06e'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'hairline': [(14, 66), (20, 56), (50, 54), (80, 56), (86, 66)]},
    'front': [L(outline([(16, 80), (4, 84, 1), (8, 70), (10, 46), (20, 22), (36, 10), (50, 8), (64, 10), (80, 22), (90, 46), (92, 70), (96, 84, 1), (84, 80), (80, 70), (20, 70)])),
              L(outline([(56, 10), (76, 18), (90, 46), (92, 70), (96, 84), (84, 80), (80, 56)]), 'shade', 'b', False),
              L(outline([(16, 64), (18, 44), (30, 30), (50, 26), (70, 30), (82, 44), (84, 64), (76, 56), (70, 66, 1), (64, 54), (56, 66, 1), (50, 54), (42, 66, 1), (36, 54),
                         (28, 66, 1), (22, 58)]), 'mid', 'f', ln=True),
              L(outline([(34, 12), (42, 10), (44, 40), (40, 64, 1), (36, 40)]), STREAK, 'f'), L(outline([(22, 26), (28, 22), (28, 50), (24, 62, 1), (20, 44)]), STREAK, 'f')],
    'side': [L(outline([(76, 56), (84, 44), (84, 26), (70, 10), (46, 6), (24, 14), (10, 34), (8, 60), (14, 80), (4, 88, 1), (24, 86), (36, 80), (42, 68), (44, 58), (56, 56),
                        (66, 56)])),
             L(outline([(24, 14), (46, 6), (70, 10), (84, 26), (84, 36), (60, 26), (34, 30), (10, 40), (12, 28)]), STREAK),
             L(outline([(72, 48), (86, 52), (84, 76, 1), (78, 62)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 82), (4, 86, 1), (8, 70), (10, 46), (20, 22), (36, 10), (50, 8), (64, 10), (80, 22), (90, 46), (92, 70), (96, 86, 1), (84, 82), (66, 88), (50, 92),
                        (34, 88)])),
             L(outline([(52, 8), (66, 10), (80, 22), (86, 38), (70, 34), (56, 40), (50, 26)]), STREAK, 'b', False),
             ],
}

# Alegre (Arthur): piel morena, pelo rojo en pinchos revueltos con la parte de abajo negra junto a las sienes, mechones
# largos que le caen sobre los ojos verde azulado y la nuca larga en punta; sonrisa tranquila
DARK = (42, 38, 40, 255)
CHARS['alegre'] = {
    'body': 'normal', 'pal': pal('#e24c3a', '#b07a4e', iris='#2a8a8a', shade='#b83a2c', deep='#8a2a20', dark=DARK),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': [(14, 64), (24, 50), (38, 48), (50, 54), (62, 48), (76, 50), (86, 64)]},
    'front': [L(outline([(16, 70), (10, 54), (4, 36, 1), (12, 30), (10, 12, 1), (24, 14), (28, -6, 1), (38, 6), (46, -10, 1), (54, 4), (66, -6, 1), (70, 10), (84, 6, 1),
                         (84, 24), (96, 32, 1), (88, 40), (90, 54), (84, 70), (76, 56), (24, 56)])),
              L(outline([(54, 4), (66, -6), (70, 10), (84, 6), (84, 24), (96, 32), (88, 42), (74, 26)]), 'shade', 'b', False),
              L(outline([(15, 58), (21, 54), (21, 70), (17, 72)]), 'dark', 'f'), L(outline([(85, 58), (79, 54), (79, 70), (83, 72)]), 'dark', 'f'),
              L(outline([(20, 50), (32, 40), (50, 36), (68, 40), (80, 50), (72, 50), (66, 70, 1), (60, 50), (52, 66, 1), (48, 50), (40, 66, 1), (34, 50), (28, 60, 1)]),
                'mid', 'f', ln=True),
              strand([(40, 40), (42, 58)], 'deep', 'f', 1.0), strand([(58, 40), (58, 56)], 'deep', 'f', 1.0)],
    'side': [L(outline([(74, 58), (82, 46), (90, 36, 1), (82, 30), (90, 16, 1), (76, 14), (76, -4, 1), (62, 6), (52, -10, 1), (44, 6), (28, -2, 1), (28, 12), (10, 16, 1),
                        (14, 28), (-2, 40, 1), (10, 46), (6, 64), (14, 84), (22, 100, 1), (28, 84), (36, 74), (44, 62), (56, 56), (64, 58)])),
             L(outline([(-2, 40), (10, 46), (6, 64), (14, 84), (22, 100), (28, 84), (36, 74), (44, 62), (26, 52), (12, 36)]), 'shade', 'b', False),
             L(outline([(52, 58), (62, 50), (66, 64), (58, 74)]), 'dark', 'f'),
             L(outline([(72, 48), (84, 50), (84, 70, 1), (78, 60)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 70), (8, 56), (2, 38, 1), (12, 32), (8, 12, 1), (24, 14), (28, -6, 1), (40, 6), (48, -10, 1), (56, 4), (68, -6, 1), (72, 10), (88, 8, 1), (86, 24),
                        (98, 34, 1), (88, 42), (94, 56, 1), (84, 64), (80, 84), (66, 90), (56, 104, 1), (50, 90), (44, 104, 1), (36, 90), (20, 84)])),
             L(outline([(56, 4), (68, -6), (72, 10), (88, 8), (86, 24), (98, 34), (88, 42), (94, 56), (84, 64), (80, 84), (66, 90), (62, 40)]), 'shade', 'b', False),
             strand([(40, 60), (44, 96)], 'deep', 'b', 1.0), strand([(60, 60), (56, 96)], 'deep', 'b', 1.0)],
}

# Rio (Miguel): bajito, pelo rojo anaranjado ondulado y abultado, con puntas que salen hacia fuera a los lados a la
# altura de la boca; ojos azules grandes y la boca abierta de sorpresa
CHARS['rio'] = {
    'body': 'bajito', 'pal': pal('#e04c2a', '#fde0c6', iris='#4a6ab8', shade='#b8381e', deep='#8a2814'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'none', 'hairline': [(14, 66), (22, 54), (34, 50), (40, 58), (48, 48), (60, 52), (72, 48), (80, 56), (86, 66)]},
    'front': [L(outline([(16, 96), (6, 90), (8, 82), (-12, 74, 1), (6, 66), (8, 44), (14, 22), (24, 6), (36, 12), (48, 0), (62, 10), (76, 4), (86, 22), (92, 44), (94, 66),
                         (112, 74, 1), (92, 82), (94, 90), (84, 96), (80, 76), (20, 76)])),
              L(outline([(62, 10), (76, 4), (86, 22), (92, 44), (94, 66), (112, 74), (92, 82), (94, 90), (84, 96), (80, 56), (72, 26)]), 'shade', 'b', False),
              L(outline([(16, 62), (20, 44), (34, 32), (50, 30), (66, 32), (80, 44), (84, 62), (76, 54), (70, 62, 1), (62, 50), (52, 58, 1), (46, 48), (36, 60, 1), (28, 52),
                         (22, 66, 1)]), 'mid', 'f', ln=True),
              L(ell(50, 94, 4, 4.4), (196, 80, 80, 255), 'f'), L([(47.5, 90.5), (52.5, 90.5), (52.5, 93), (47.5, 93)], WHITE, 'f', False)],
    'side': [L(outline([(78, 56), (86, 44), (90, 26), (82, 8), (64, -4), (40, -2), (20, 8), (6, 26), (2, 50), (6, 76), (14, 90), (30, 96), (44, 92), (50, 76), (46, 60),
                        (60, 56), (70, 56)])),
             L(outline([(2, 50), (6, 76), (14, 90), (30, 96), (44, 92), (50, 76), (46, 60), (26, 48)]), 'shade', 'b', False),
             L(outline([(76, 50), (88, 52), (88, 92, 1), (80, 76)]), 'mid', 'f', ln=True),
             L(ell(85, 94, 2.4, 3), (196, 80, 80, 255), 'f')],
    'back': [L(outline([(16, 98), (6, 92), (8, 82), (-12, 74, 1), (6, 66), (8, 44), (14, 22), (22, 4, 1), (36, 12), (46, -2, 1), (52, 10), (66, 2, 1), (74, 14), (86, 20), (92, 44),
                        (94, 66), (112, 74, 1), (92, 82), (94, 92), (84, 98), (66, 94), (50, 100), (34, 94)])),
             L(outline([(52, 10), (66, 2), (74, 14), (86, 20), (92, 44), (94, 66), (112, 74), (92, 82), (94, 92), (84, 98), (66, 94), (60, 50)]), 'shade', 'b', False),
             ],
}

# Belém (Raymond): piel morena, pelo rizado abundante castaño grisáceo con las puntas de arriba color crema que le
# caen sobre la frente; ojos redondos y una media sonrisa de chulo
CREAM = (228, 220, 202, 255)
CHARS['bel-m'] = {
    'body': 'normal', 'pal': pal('#8c6c6a', '#a26e48', iris='#202020', shade='#6e5250', deep='#523c3a', cream=CREAM),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'hairline': [(14, 70), (22, 58), (36, 54), (50, 60), (62, 52), (78, 58), (86, 70)]},
    'front': [L(curls(50, 38, (54, 46), 12, 0.2, 0.86)), L(clipx(curls(50, 38, (54, 46), 12, 0.2, 0.86), 62, 120), 'shade', 'b', False),
              L(outline([(24, 20), (34, 4), (50, -2), (66, 4), (76, 20), (66, 18), (60, 30, 1), (54, 18), (46, 32, 1), (42, 18), (32, 26, 1)]), 'cream'),
              L(outline([(30, 52), (36, 40), (44, 38), (50, 62, 1), (54, 40), (64, 40), (70, 52), (60, 48), (52, 50)]), 'cream', 'f', ln=True)],
    'side': [L(curls(42, 40, (50, 46), 12, 0.2, 0.86)), L(clipx(curls(42, 40, (50, 46), 12, 0.2, 0.86), -20, 24), 'shade', 'b', False),
             L(outline([(50, 4), (66, -2), (84, 8), (92, 30), (86, 46, 1), (80, 30), (70, 22), (56, 22)]), 'cream')],
    'back': [L(curls(50, 42, (54, 46), 12, 0.2, 0.86)), L(clipx(curls(50, 42, (54, 46), 12, 0.2, 0.86), 62, 120), 'shade', 'b', False),
             L(outline([(30, 14), (42, 2), (58, 2), (70, 14), (60, 22), (50, 36, 1), (42, 22)]), 'cream', 'b', False)],
}

# Cristiano Dabola (Leoneira Camion): un señor mayor y fornido; pelo gris corto peinado hacia atrás, cara cuadrada con
# arrugas, cejas gruesas y oscuras, orejas grandes y boca de enfado
CHARS['cristiano-dabola'] = {
    'body': 'corpulento', 'pal': pal('#9a94a6', '#fcd6a8', iris='#3a8a9a', shade='#7a7486', deep='#5e586a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 3, 'ear_out': 3, 'hairline': (40, 34),
             'face_front': blob([(16, 40), (50, 30), (84, 40), (88, 70), (86, 96), (70, 110), (50, 112), (30, 110), (14, 96), (12, 70)]), 'nose': (50, 86, 2.6)},
    'front': [L(outline([(16, 54), (14, 30), (22, 10), (38, 0), (50, -2), (62, 0), (78, 10), (86, 30), (84, 54), (78, 36), (22, 36)])),
              L(outline([(56, 0), (76, 8), (86, 30), (84, 52), (76, 28)]), 'shade', 'b', False),
              strand([(30, 10), (40, 30)], 'deep', 'b', 1.0), strand([(50, 4), (52, 30)], 'deep', 'b', 1.0), strand([(70, 10), (62, 30)], 'deep', 'b', 1.0),
              L(outline([(24, 62), (44, 64), (44, 70), (24, 70)]), (56, 60, 70, 255), 'f', False), L(outline([(76, 62), (56, 64), (56, 70), (76, 70)]), (56, 60, 70, 255), 'f', False),
              L([(44, 58), (48, 66)], OUTC, 'f', False, False, 1.0), L([(56, 58), (52, 66)], OUTC, 'f', False, False, 1.0),
              L([(32, 84), (36, 96)], OUTC, 'f', False, False, 1.0), L([(68, 84), (64, 96)], OUTC, 'f', False, False, 1.0),
              L(quad((38, 104), (50, 106), (62, 104)), OUTC, 'f', False, False, 0.9)],
    'side': [L(outline([(80, 38), (84, 24), (74, 6), (54, -4), (30, -2), (12, 10), (4, 30), (6, 56), (14, 66), (34, 60), (42, 50), (56, 42), (70, 38)])),
             L(outline([(4, 30), (6, 56), (14, 66), (34, 60), (42, 50), (24, 40)]), 'shade', 'b', False),
             L([(70, 62), (86, 64)], (56, 60, 70, 255), 'f', False, False, 3.0)],
    'back': [L(outline([(16, 72), (14, 40), (20, 14), (36, 2), (50, -2), (64, 2), (80, 14), (86, 40), (84, 72), (50, 76)])),
             L(outline([(56, 0), (78, 12), (86, 40), (84, 72), (62, 76), (66, 30)]), 'shade', 'b', False),
             strand([(40, 20), (36, 60)], 'deep', 'b', 1.0), strand([(60, 20), (64, 60)], 'deep', 'b', 1.0)],
}

# Paulo: piel morena, un afro enorme gris azulado arriba que se oscurece a negro por debajo, con mechones negros sobre
# la frente; ojos rojos y sonrisa de dientes
AFRO_D = (40, 30, 30, 255)
CHARS['paulo'] = {
    'body': 'normal', 'pal': pal('#7e9abc', '#a8704a', iris='#b82020', shade='#5e7898', deep='#3e5470', dark=AFRO_D),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'hairline': [(14, 70), (22, 60), (36, 56), (44, 64), (52, 54), (62, 60), (78, 60), (86, 70)]},
    'front': [L(curls(50, 54, (56, 46), 12, 0.2, 0.88), 'dark'), L(curls(50, 32, (56, 40), 12, 0.2, 0.88)),
              L(clipx(curls(50, 32, (56, 40), 12, 0.2, 0.88), 64, 120), 'shade', 'b', False),
              L(outline([(20, 64), (30, 52), (46, 50), (40, 70, 1), (52, 52), (66, 52), (80, 62), (64, 58), (56, 66, 1), (50, 58), (30, 60)]), 'dark', 'f', ln=True)],
    'side': [L(curls(40, 54, (50, 44), 12, 0.2, 0.88), 'dark'), L(curls(40, 32, (52, 40), 12, 0.2, 0.88)),
             L(clipx(curls(40, 32, (52, 40), 12, 0.2, 0.88), -20, 22), 'shade', 'b', False),
             L(outline([(70, 52), (84, 56), (80, 70, 1)]), 'dark', 'f', ln=True)],
    'back': [L(curls(50, 56, (54, 44), 12, 0.2, 0.88), 'dark'), L(curls(50, 34, (56, 42), 12, 0.2, 0.88)),
             L(clipx(curls(50, 34, (56, 42), 12, 0.2, 0.88), 64, 120), 'shade', 'b', False)],
}
