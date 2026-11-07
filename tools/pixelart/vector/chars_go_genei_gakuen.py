"""Instituto Espejismo (go-genei-gakuen): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Magos e ilusionistas: melenas como capuchas, sombreros de paja, cuernos de demonio, monóculo y caras pintadas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import SIDE_SKULL, WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)
RED_EYE = (220, 30, 30, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Abram Cadabra (portero): grandullón de piel morena oscura; melena negra lisa como una capucha que le cae por los lados
# hasta los hombros, una cinta blanca en la frente, ojos rojos con rayas negras pintadas debajo y gesto serio
CHARS['abram-cadabra'] = {
    'body': 'corpulento', 'pal': pal('#24222a', '#9a6440', iris='#e02020', band='#f2f0ea'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (46, 40), 'face_front': WIDE_FACE},
    'front': [L(outline([(-14, 120, 1), (2, 92), (10, 52), (14, 24), (30, 4), (50, -2), (70, 4), (86, 24), (90, 52), (98, 92), (114, 120, 1), (86, 108),
                         (82, 62), (18, 62), (14, 108)])),
              L(outline([(60, 2), (84, 18), (92, 56), (102, 100), (88, 104), (80, 50)]), 'shade', 'b', False),
              strand([(30, 8), (22, 50), (8, 100)], 'light', 'b', 1.2), strand([(70, 8), (78, 50), (92, 100)], 'light', 'b', 1.2),
              L(outline([(22, 44), (24, 36), (50, 34), (76, 36), (78, 44), (50, 42)]), 'band', 'f', ln=True),
              L(outline([(28, 80), (32, 80), (30, 96)]), OUTC, 'f', False), L(outline([(68, 80), (72, 80), (70, 96)]), OUTC, 'f', False),
              L(outline([(38, 82), (41, 82), (38, 92)]), OUTC, 'f', False), L(outline([(59, 82), (62, 82), (62, 92)]), OUTC, 'f', False)],
    'side': [L(outline([(68, 44), (80, 30), (74, 8), (50, -4), (24, 2), (8, 22), (2, 60), (-16, 110, 1), (10, 98), (24, 108, 1), (34, 86), (46, 66), (56, 52)])),
             L(outline([(4, 40), (24, 46), (24, 90), (0, 96)]), 'shade', 'b', False),
             L(outline([(70, 42), (74, 34), (90, 36), (92, 44)]), 'band', 'f', ln=True),
             L(outline([(80, 80), (84, 80), (82, 96)]), OUTC, 'f', False)],
    'back': [L(outline([(-14, 124, 1), (-2, 104), (8, 52), (14, 22), (30, 2), (50, -4), (70, 2), (86, 22), (92, 52), (102, 104), (114, 124, 1), (80, 116),
                        (50, 120), (20, 116)])),
             L(outline([(56, 0), (84, 18), (96, 60), (104, 112), (70, 116), (70, 50)]), 'shade', 'b', False)],
}

# Jaymes Randie: pelo negro liso peinado hacia atrás con raya en medio y un mechón largo delante de cada oreja hasta la
# mandíbula, recogido detrás en una coletita baja; piel muy pálida, ojos violetas afilados y sonrisa pícara
CHARS['jaymes-randie'] = {
    'body': 'delgado', 'pal': pal('#1e1c22', '#fcecc4', iris='#8a6ac8', tie='#e8e0e0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': [(14, 64), (22, 46), (40, 36), (50, 40), (60, 36), (78, 46), (86, 64)]},
    'front': [L(outline([(16, 70), (12, 36), (24, 10), (50, 0), (76, 10), (88, 36), (84, 70), (80, 56), (20, 56)])),
              L(outline([(60, 4), (82, 16), (90, 44), (84, 64), (76, 40)]), 'shade', 'b', False),
              strand([(50, 2), (40, 24), (26, 44)], 'light', 'b', 1.0), strand([(50, 2), (60, 24), (74, 44)], 'light', 'b', 1.0),
              L(outline([(16, 58), (20, 62), (18, 100, 1), (14, 80)]), 'mid', 'f', ln=True), L(outline([(84, 58), (80, 62), (82, 100, 1), (86, 80)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 56), (62, 44), (80, 40), (90, 26), (82, 8), (60, -2), (34, 0), (14, 12), (6, 36), (8, 60), (18, 76), (34, 76), (46, 66)])),
             L(outline([(20, 72), (10, 88), (2, 112, 1), (14, 98), (26, 78)]), 'mid', 'b'),
             L(ell(20, 74, 3.4, 3), 'tie', 'f', ln=True),
             strand([(70, 6), (40, 16), (14, 40)], 'light', 'b', 1.0),
             L(outline([(64, 56), (68, 62), (66, 96, 1), (62, 74)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 76), (12, 36), (24, 10), (50, 0), (76, 10), (88, 36), (84, 76), (50, 86)])),
             L(outline([(56, 4), (82, 16), (90, 48), (84, 72), (60, 82)]), 'shade', 'b', False),
             L(outline([(46, 80), (44, 100), (50, 114, 1), (56, 100), (54, 80)]), 'mid', 'f'),
             L(ell(50, 82, 4, 3), 'tie', 'f', ln=True),
             L(outline([(14, 60), (18, 64), (16, 98, 1), (12, 78)]), 'mid', 'f', ln=True), L(outline([(86, 60), (82, 64), (84, 98, 1), (88, 78)]), 'mid', 'f', ln=True)],
}

# Daffyd Blayne: la cabeza rapada castaña y encima un tupé morado que nace en lo alto y baja en curva por la frente hasta
# taparle un ojo; ojos ámbar y media sonrisa
CHARS['daffyd-blayne'] = {
    'body': 'normal', 'pal': pal('#6a2a54', '#fcd8b0', iris='#a87a2a', buzz='#7a5444', buzz_d='#644034'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (60, 44)},
    'front': [L(outline([(16, 66), (14, 36), (26, 12), (50, 4), (74, 12), (86, 36), (84, 66), (80, 56), (20, 56)]), 'buzz'),
              L(outline([(28, 8), (36, -8), (56, -12), (72, -2), (72, 12), (60, 24), (46, 40), (38, 66, 1), (32, 46), (26, 26)]), 'mid', 'f'),
              L(outline([(56, -8), (70, 0), (70, 10), (58, 18), (60, 4)]), 'shade', 'f', False),
              strand([(38, -4), (36, 16), (36, 44)], 'deep', 'f', 1.0)],
    'side': [L(blob(SIDE_SKULL), 'buzz'), L(outline([(14, 40), (30, 60), (28, 86), (16, 76)]), 'buzz_d', 'b', False),
             L(outline([(16, 16), (36, -6), (66, -8), (88, 6), (98, 30), (94, 50), (86, 44), (78, 24), (54, 14), (28, 22)]), 'mid', 'f'),
             L(outline([(18, 14), (40, -2), (30, 14)]), 'shade', 'f', False)],
    'back': [L(outline([(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 88), (34, 88)]), 'buzz'),
             L(outline([(56, 14), (84, 36), (84, 68), (64, 86)]), 'buzz_d', 'b', False),
             L(outline([(22, 24), (30, 6), (50, -4), (70, 6), (78, 24), (50, 18)]), 'mid', 'f')],
}

# Al Kazam: gordo de piel muy pálida; casco de pelo negro con las puntas de los lados vueltas hacia fuera sobre las orejas y
# un pico en la frente, antifaz negro alrededor de los ojos, nariz gris y mofletes
CHARS['al-kazam'] = {
    'body': 'corpulento', 'pal': pal('#24222e', '#fcead4', iris='#d8d8e8', nose='#6a7a7a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': WIDE_FACE, 'nose': (50, 86, 5)},
    'front': [L(outline([(12, 66), (0, 60, 1), (8, 44), (12, 18), (34, 4), (66, 4), (88, 18), (92, 44), (100, 60, 1), (88, 66), (84, 50), (16, 50)])),
              L(outline([(60, 6), (84, 18), (90, 50), (84, 60), (76, 40)]), 'shade', 'b', False),
              fringe([(12, 56), (16, 36), (32, 26), (44, 24), (50, 50, 1), (56, 24), (70, 26), (84, 36), (88, 56), (76, 46), (60, 38), (40, 38), (24, 46)]),
              L(outline([(20, 72), (34, 66), (46, 72), (54, 72), (66, 66), (80, 72), (78, 84), (66, 82), (54, 80), (46, 80), (34, 82), (22, 84)]), OUTC, 'f', False),
              L(ell(34, 76, 6, 3.6), WHITE, 'f', False), L(ell(66, 76, 6, 3.6), WHITE, 'f', False),
              L(ell(35, 76, 2, 2.4), OUTC, 'f', False), L(ell(65, 76, 2, 2.4), OUTC, 'f', False)],
    'side': [L(outline([(56, 48), (64, 30), (56, 10), (32, 2), (12, 14), (6, 44), (-4, 62, 1), (12, 60), (26, 58), (40, 52)])),
             L(outline([(8, 30), (24, 40), (22, 58), (8, 52)]), 'shade', 'b', False),
             L(outline([(72, 70), (90, 72), (90, 82), (72, 82)]), OUTC, 'f', False), L(ell(84, 76, 3, 3), WHITE, 'f', False)],
    'back': [L(outline([(12, 66), (-2, 62, 1), (8, 44), (12, 18), (34, 4), (66, 4), (88, 18), (92, 44), (102, 62, 1), (88, 66), (70, 62), (30, 62)])),
             L(outline([(56, 6), (84, 18), (92, 50), (84, 64), (66, 60)]), 'shade', 'b', False)],
}

# Sigfryd Roi: pelo rubio peinado hacia atrás, con el nacimiento en M y una cresta alta que se levanta en lo alto y baja en
# dientes por la nuca; piel tostada, ojos azules de enfado
CHARS['sigfryd-roi'] = {
    'body': 'normal', 'pal': pal('#ecd078', '#dca46a', iris='#4a8aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98,
             'hairline': [(14, 66), (20, 50), (30, 40), (40, 52), (46, 36), (50, 40), (54, 36), (60, 52), (70, 40), (80, 50), (86, 66)]},
    'front': [L(outline([(16, 70), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (84, 70), (80, 56), (20, 56)])),
              L(outline([(40, 8), (42, -16), (52, -34, 1), (62, -16), (62, 8)])),
              L(outline([(60, 8), (82, 18), (90, 46), (84, 64), (76, 40)]), 'shade', 'b', False),
              strand([(34, 14), (38, 36)], 'shade', 'b', 1.0), strand([(66, 14), (62, 36)], 'shade', 'b', 1.0)],
    'side': [L(outline([(56, 54), (62, 44), (80, 40), (90, 28), (84, 10), (70, 0), (60, -14), (52, -30, 1), (40, -10), (26, 0, 1), (22, 14), (8, 14, 1), (12, 30),
                        (2, 38, 1), (8, 52), (4, 66, 1), (14, 72), (30, 76), (46, 66)])),
             L(outline([(10, 34), (28, 40), (30, 66), (14, 62)]), 'shade', 'b', False),
             strand([(86, 30), (60, 18), (30, 24)], 'shade', 'b', 1.0),
             L(outline([(20, 30), (6, 50), (2, 72), (4, 96), (0, 116, 1), (12, 104), (14, 78), (18, 54), (30, 36)]), 'mid', 'b', ln=True),
             strand([(4, 60), (14, 64)], 'shade', 'b', 1.2), strand([(4, 76), (14, 80)], 'shade', 'b', 1.2), strand([(4, 92), (12, 96)], 'shade', 'b', 1.2)],
    'back': [L(outline([(16, 76), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (84, 76), (50, 84)])),
             L(outline([(40, 8), (42, -16), (52, -34, 1), (62, -16), (62, 8), (58, 30), (66, 40, 1), (58, 50), (64, 62, 1), (56, 70), (60, 84, 1), (50, 80),
                        (42, 60)]), 'mid', 'f', ln=True),
             L(outline([(46, 76), (58, 76), (60, 100), (56, 124), (50, 132, 1), (44, 124), (42, 100)]), 'mid', 'f', ln=True),
             strand([(44, 92), (58, 96)], 'shade', 'f', 1.2), strand([(44, 108), (58, 112)], 'shade', 'f', 1.2),
             L(outline([(56, 10), (82, 18), (90, 50), (84, 72), (66, 80)]), 'shade', 'b', False)],
}

# Dave Coppfielder: tupé azul oscuro enorme y esponjoso, con un mechón que baja en curva por la frente; piel morena, nariz
# larga, ojos blancos de iris granate y gesto serio
CHARS['dave-coppfielder'] = {
    'body': 'normal', 'pal': pal('#2e4468', '#c48e5a', iris='#7a2030'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 66), (4, 40), (6, 14), (26, -6), (54, -10), (80, -2), (96, 18), (96, 42), (88, 66), (84, 52), (18, 52)])),
              L(outline([(60, -6), (86, 6), (96, 40), (88, 60), (78, 36)]), 'shade', 'b', False),
              fringe([(12, 56), (14, 36), (30, 22), (54, 18), (74, 26), (86, 42), (86, 56), (76, 44), (62, 38), (48, 40), (36, 52), (30, 70, 1), (26, 50), (20, 48)]),
              L(outline([(24, 0), (46, -6), (40, 6)]), 'light', 'b', False),
              L([(50, 80), (48, 92)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(56, 52), (66, 40), (82, 34), (92, 16), (78, -6), (48, -12), (20, -6), (4, 14), (4, 40), (10, 64), (14, 88), (36, 90), (46, 70)])),
             L(outline([(6, 30), (26, 40), (30, 86), (12, 84)]), 'shade', 'b', False),
             fringe([(70, -2), (92, 14), (94, 32), (86, 48), (82, 36), (72, 28)])],
    'back': [L(outline([(4, 40), (4, 14), (22, -6), (50, -10), (78, -6), (96, 14), (96, 40), (82, 48), (80, 88), (20, 88), (18, 48)])),
             L(outline([(56, -6), (86, 8), (96, 40), (80, 46), (80, 86), (62, 88)]), 'shade', 'b', False),
             strand([(18, 48), (50, 54), (82, 48)], 'deep', 'b', 1.2)],
}

# Launce Berton: un sombrero de paja cónico verde oscuro, muy ancho, que le tapa hasta las cejas; por debajo, pelo negro de
# puntas sobre la frente y la nuca; perilla verde en punta y dientes apretados
CHARS['launce-berton'] = {
    'body': 'delgado', 'pal': pal('#1e1e22', '#f8dcb4', iris='#2a2a2a', hat='#2c4a3c', hat_d='#1e362c', beard='#2a5a42'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 64), (16, 44), (84, 44), (82, 64), (74, 56), (68, 66, 1), (60, 56), (54, 70, 1), (46, 56), (40, 68, 1), (30, 56), (24, 66, 1)]), 'mid', 'f'),
              L(outline([(-30, 46, 1), (16, 26), (50, -8, 1), (84, 28), (130, 46, 1), (84, 50), (52, 64, 1), (18, 50)]), 'hat', 'f', ln=True),
              L(outline([(50, -16), (84, 26), (128, 46), (84, 48), (54, 60)]), 'hat_d', 'f', False),
              strand([(50, -14), (40, 30), (52, 60)], 'hat_d', 'f', 1.0),
              L(outline([(38, 104), (62, 104), (58, 118), (50, 126, 1), (42, 118)]), 'beard', 'f', ln=True)],
    'side': [L(outline([(52, 60), (54, 44), (20, 40), (8, 60), (14, 84), (30, 90), (40, 76)])),
             L(outline([(-24, 42, 1), (26, 22), (56, -6, 1), (80, 24), (124, 66, 1), (74, 50), (30, 48)]), 'hat', 'f', ln=True),
             L(outline([(56, -12), (80, 22), (120, 62), (74, 46)]), 'hat_d', 'f', False),
             L(outline([(70, 104), (86, 102), (80, 118, 1), (72, 114)]), 'beard', 'f', ln=True)],
    'back': [L(outline([(16, 48), (84, 48), (86, 88), (16, 88)])),
             L(outline([(-30, 44, 1), (16, 24), (50, -8, 1), (84, 26), (130, 44, 1), (84, 50), (16, 50)]), 'hat', 'f', ln=True),
             L(outline([(50, -16), (84, 24), (128, 44), (84, 48), (54, 40)]), 'hat_d', 'f', False)],
}

# Ledger Demain: casco de pelo blanco que se vuelve rosado en las puntas, abiertas en pico a los lados, y un monóculo rojo
# de cristal grueso con montura blanca sobre el ojo izquierdo; ojos pequeños
CHARS['ledger-demain'] = {
    'body': 'bajito', 'pal': pal('#f4eeee', '#fcdcbc', iris='#3a2a1e', shade='#c8a0a6', deep='#a87c84', mono='#d01e3a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 74), (-10, 62, 1), (6, 54), (6, 26), (22, 4), (50, -4), (78, 4), (94, 26), (94, 54), (110, 62, 1), (88, 74), (84, 60), (16, 60)]), 'shade'),
              L(outline([(8, 46), (8, 26), (22, 4), (50, -4), (78, 4), (92, 26), (92, 46), (70, 36), (50, 40), (30, 36)]), 'mid', 'b', False),
              fringe([(10, 66), (12, 44), (26, 26), (50, 20), (74, 26), (88, 44), (90, 66), (82, 56), (76, 64, 1), (70, 50), (60, 58, 1), (54, 46), (46, 58, 1),
                      (40, 46), (30, 58, 1), (24, 50), (18, 62, 1)], 'shade'),
              L(outline([(14, 50), (26, 30), (50, 24), (74, 30), (86, 50), (66, 42), (50, 46), (34, 42)]), 'mid', 'f', False),
              L(ell(64, 78, 10, 10), WHITE, 'f', ln=True), L(ell(64, 78, 7, 7), 'mono', 'f', ln=True), L(ell(64, 78, 2, 2), WHITE, 'f', False)],
    'side': [L(outline([(54, 60), (58, 48), (82, 46), (94, 32), (88, 10), (66, -4), (38, -4), (16, 8), (4, 32), (-8, 48, 1), (4, 56), (0, 72, 1), (12, 78), (16, 92, 1),
                        (28, 80), (44, 74)]), 'shade'),
             L(outline([(10, 26), (20, 6), (44, -4), (70, -2), (90, 12), (94, 30), (70, 22), (40, 26), (20, 40)]), 'mid', 'b', False),
             fringe([(64, 0), (90, 14), (96, 40), (92, 60, 1), (84, 46), (76, 34)], 'shade'),
             L(ell(86, 78, 4, 8), WHITE, 'f', ln=True), L(ell(87, 78, 2.6, 6), 'mono', 'f', False)],
    'back': [L(outline([(12, 80), (-10, 64, 1), (6, 56), (6, 26), (22, 4), (50, -4), (78, 4), (94, 26), (94, 56), (110, 64, 1), (88, 80), (70, 92, 1), (60, 84),
                        (50, 94, 1), (40, 84), (30, 92, 1)]), 'shade'),
             L(outline([(8, 46), (8, 26), (22, 4), (50, -4), (78, 4), (92, 26), (92, 46), (76, 34), (62, 42), (50, 34), (38, 42), (24, 34)]), 'mid', 'b', False)],
}

# Hocus Sesame: pelo rosa fucsia a mechones, con un rizo largo que se levanta de lo alto hacia un lado como una antena y
# flequillo de lado; ojos rosados entornados y sonrisa tranquila
CHARS['hocus-sesame'] = {
    'body': 'normal', 'pal': pal('#c8487a', '#fcd8b0', iris='#b04a6a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 96), (4, 60), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (96, 60), (90, 96), (84, 70), (16, 70)])),
              L(outline([(46, 4), (30, -10), (-8, -18, 1), (30, -20), (58, -4)])),
              L(outline([(60, 4), (84, 16), (94, 44), (90, 88), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 74), (10, 42), (24, 16), (50, 8), (76, 16), (90, 42), (92, 76), (84, 56), (78, 70, 1), (72, 44), (62, 56, 1), (58, 36), (46, 50, 1),
                      (40, 32), (30, 48, 1), (22, 40), (18, 66)]),
              L(outline([(52, 10), (78, 20), (88, 42), (74, 36)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (92, 34), (88, 12), (66, -2), (40, -2), (16, 10), (4, 34), (2, 66), (10, 90), (26, 92), (40, 82)])),
             L(outline([(40, 0), (50, -12), (74, -16, 1), (56, -6), (52, 2)])),
             L(outline([(4, 34), (26, 42), (28, 84), (10, 84)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 66, 1), (84, 48), (76, 34)])],
    'back': [L(outline([(10, 88), (4, 60), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (96, 60), (90, 88), (76, 96, 1), (66, 86), (50, 94), (34, 86), (24, 96, 1)])),
             L(outline([(46, 4), (60, -14), (86, -18, 1), (64, -6), (56, 4)])),
             L(outline([(56, 4), (84, 16), (96, 46), (90, 86), (66, 90)]), 'shade', 'b', False)],
}

# Pocus Sesame: pelo verde azulado de puntas, con dos cuernos grandes que se abren hacia arriba a los lados y pinchos sobre
# las sienes; pico de pelo en medio de la frente, ojos turquesa entornados y sonrisa
CHARS['pocus-sesame'] = {
    'body': 'normal', 'pal': pal('#4a9a92', '#fcd8b0', iris='#3a8a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 60), (-6, 54, 1), (10, 42), (-4, 32, 1), (14, 24), (10, -10, 1), (30, 10), (50, 2), (70, 10), (90, -10, 1), (86, 24), (104, 32, 1),
                         (90, 42), (106, 54, 1), (84, 60), (80, 50), (20, 50)])),
              L(outline([(60, 6), (84, 14), (92, 40), (84, 56), (76, 36)]), 'shade', 'b', False),
              L(outline([(40, 6), (36, -8, 1), (48, 4)]), 'mid', 'b'), L(outline([(60, 6), (64, -8, 1), (52, 4)]), 'mid', 'b'),
              fringe([(16, 56), (18, 36), (32, 22), (50, 18), (68, 22), (82, 36), (84, 56), (72, 46), (60, 50), (50, 64, 1), (40, 50), (28, 46)])],
    'side': [L(outline([(56, 56), (62, 46), (80, 44), (90, 30), (86, 12), (90, -6, 1), (66, 4), (44, -6), (20, 2), (8, -8, 1), (8, 16), (-8, 30, 1), (6, 40),
                        (-4, 58, 1), (12, 62), (12, 78, 1), (26, 72), (36, 80), (46, 66)])),
             L(outline([(6, 30), (24, 40), (26, 66), (10, 60)]), 'shade', 'b', False),
             fringe([(66, 4), (88, 16), (94, 38), (88, 54, 1), (82, 40), (74, 30)])],
    'back': [L(outline([(16, 80), (6, 60), (-6, 54, 1), (8, 44), (0, 30, 1), (14, 24), (6, -12, 1), (30, 10), (50, 2), (70, 10), (94, -12, 1), (86, 24), (100, 30, 1),
                        (92, 44), (106, 54, 1), (94, 60), (84, 80), (50, 86)])),
             L(outline([(56, 6), (84, 18), (92, 50), (84, 76), (62, 84)]), 'shade', 'b', False),
             strand([(50, 4), (50, 40)], 'deep', 'b', 1.0)],
}

# Daren Blakh: media melena lila lisa peinada de lado, que le tapa el ojo derecho y se abre en una punta hacia fuera a ese
# lado; ojo azul claro y gesto frío
CHARS['daren-blakh'] = {
    'body': 'delgado', 'pal': pal('#b4a4c8', '#fcdcc0', iris='#5aa8c8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 70), (-12, 66, 1), (6, 54), (8, 26), (24, 6), (52, -2), (78, 6), (92, 24), (106, 34, 1), (92, 44), (92, 70), (86, 56), (16, 56)])),
              L(outline([(60, 2), (84, 14), (92, 44), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(10, 58), (12, 34), (28, 16), (54, 10), (78, 16), (90, 30), (88, 46), (76, 40), (66, 38), (56, 48), (50, 70), (46, 96, 1), (36, 104),
                      (20, 100), (14, 84)]),
              L(outline([(56, 14), (78, 20), (88, 34), (72, 32)]), 'shade', 'f', False), L(outline([(20, 30), (40, 18), (30, 34)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (66, -2), (40, -4), (16, 6), (2, 26), (-10, 34, 1), (4, 40), (2, 66), (10, 94), (26, 100),
                        (40, 90), (46, 74)])),
             L(outline([(4, 36), (26, 42), (30, 92), (10, 90)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 14), (96, 40), (90, 54, 1), (82, 40), (74, 30)])],
    'back': [L(outline([(10, 92), (6, 56), (-12, 58, 1), (6, 44), (8, 24), (24, 6), (50, -2), (76, 6), (92, 24), (106, 30, 1), (94, 44), (94, 92), (70, 98), (50, 100),
                        (30, 98)])),
             L(outline([(56, 4), (84, 16), (94, 50), (92, 92), (66, 96)]), 'shade', 'b', False)],
}

# Harrold Houdini: pelo rojo en forma de demonio: dos cuernos grandes en lo alto, dos pequeños sobre la frente y mechones
# que le enmarcan la cara hasta la mandíbula; marcas rojas en la frente y ojos de enfado
CHARS['harrold-houdini'] = {
    'body': 'normal', 'pal': pal('#c41e22', '#fcd8b4', iris='#8a6a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 100), (-4, 76, 1), (8, 70), (8, 40), (2, 4), (-6, -16, 1), (22, 8), (50, 2), (78, 8), (106, -16, 1), (98, 4), (92, 40), (92, 70),
                         (104, 76, 1), (86, 100), (82, 66), (18, 66)])),
              L(outline([(60, 6), (84, 12), (92, 40), (90, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 84), (12, 50), (18, 30), (32, 22), (50, 20), (68, 22), (82, 30), (88, 50), (86, 84), (80, 66), (78, 50), (70, 40), (60, 38), (50, 44),
                      (40, 38), (30, 40), (22, 50), (20, 66)]),
              L(outline([(30, 40), (26, 26), (34, 16), (32, 28), (38, 36)]), 'shade', 'f', ln=True),
              L(outline([(70, 40), (74, 26), (66, 16), (68, 28), (62, 36)]), 'shade', 'f', ln=True),
              L(outline([(48, 52), (50, 48), (52, 52), (50, 60)]), 'mid', 'f', False)],
    'side': [L(outline([(54, 66), (60, 54), (82, 52), (92, 38), (88, 14), (70, 0), (60, -18), (52, -34, 1), (44, -6), (24, 0), (6, 18), (2, 50), (-4, 70, 1), (8, 74),
                        (16, 98), (36, 92), (46, 80)])),
             L(outline([(82, 10), (92, -2), (100, 6), (94, 18)]), 'mid', 'f', ln=True),
             L(outline([(4, 34), (26, 40), (30, 86), (12, 80)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (94, 40), (90, 66), (86, 86, 1), (80, 60), (76, 40)])],
    'back': [L(outline([(16, 96), (-4, 76, 1), (8, 66), (8, 40), (2, 4), (-6, -16, 1), (22, 8), (50, 2), (78, 8), (106, -16, 1), (98, 4), (92, 40), (92, 66),
                        (104, 76, 1), (84, 96), (62, 90), (50, 100, 1), (38, 90)])),
             L(outline([(56, 6), (84, 12), (92, 44), (90, 90), (64, 92)]), 'shade', 'b', False)],
}

# Pen Teller (portero suplente): melena azul lavanda lisa hasta los hombros con flequillo recto hasta los ojos y rayas negras
# pintadas bajo los ojos; mirada seria de ojos rojizos
CHARS['pen-teller'] = {
    'body': 'normal', 'pal': pal('#7a80c4', '#fcd8b0', iris='#8a2a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 118), (4, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (96, 70), (94, 118), (82, 108), (84, 66), (16, 66), (18, 108)])),
              L(outline([(60, 4), (84, 16), (94, 50), (94, 112), (84, 104), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (88, 66), (82, 60), (80, 46), (68, 48), (66, 66, 1), (60, 48), (40, 48),
                      (34, 66, 1), (32, 48), (20, 46), (18, 60)]),
              L(outline([(30, 82), (34, 82), (24, 98)]), OUTC, 'f', False), L(outline([(70, 82), (66, 82), (76, 98)]), OUTC, 'f', False)],
    'side': [L(outline([(56, 64), (60, 52), (82, 50), (92, 36), (88, 14), (68, -2), (40, -2), (16, 10), (4, 34), (0, 70), (-6, 112), (24, 116), (40, 94), (46, 76)])),
             L(outline([(2, 40), (26, 46), (30, 108), (0, 108)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 14), (94, 38), (92, 62), (86, 64, 1), (80, 48), (72, 34)]),
             L(outline([(80, 82), (84, 82), (78, 96)]), OUTC, 'f', False)],
    'back': [L(outline([(4, 118), (4, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (96, 70), (96, 118), (50, 122)])),
             L(outline([(56, 4), (84, 16), (96, 50), (96, 116), (66, 118)]), 'shade', 'b', False),
             strand([(30, 70), (30, 116)], 'deep', 'b', 1.0), strand([(70, 70), (70, 116)], 'deep', 'b', 1.0)],
}

# Petey Sorcar: pelo castaño oscuro con dos pinchos enormes que se abren hacia arriba y hacia fuera como alas, y un pico en
# medio de la frente; piel pálida, ojos amarillos y gesto de enfado
CHARS['petey-sorcar'] = {
    'body': 'normal', 'pal': pal('#4a3634', '#fcecc8', iris='#d8a82a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 70), (14, 44), (2, 20), (-28, -10, 1), (20, -2), (42, 6), (60, 4), (80, -6), (126, -12, 1), (96, 20), (86, 44), (82, 70), (78, 54),
                         (22, 54)])),
              L(outline([(60, 6), (84, 0), (120, -10), (94, 18), (84, 44), (76, 30)]), 'shade', 'b', False),
              fringe([(16, 62), (18, 42), (30, 30), (50, 26), (70, 30), (82, 42), (84, 62), (74, 46), (60, 42), (50, 60, 1), (40, 42), (26, 46)]),
              L(outline([(-10, -4), (20, 0), (10, 10)]), 'light', 'b', False)],
    'side': [L(outline([(56, 54), (62, 44), (80, 42), (88, 26), (78, 6), (66, -30, 1), (46, -4), (20, -10), (-10, -10, 1), (10, 10), (6, 40), (14, 66), (30, 74),
                        (46, 64)])),
             L(outline([(8, 30), (26, 40), (28, 66), (12, 60)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 18), (92, 36), (86, 50, 1), (80, 38), (72, 28)])],
    'back': [L(outline([(18, 78), (14, 44), (2, 20), (-30, -16, 1), (20, -4), (50, 4), (80, -6), (128, -14, 1), (96, 20), (86, 44), (82, 78), (50, 86)])),
             L(outline([(56, 4), (82, -2), (122, -12), (94, 20), (84, 50), (82, 76), (62, 82)]), 'shade', 'b', False)],
}

# Trump Loyal: pelo rubio oscuro revuelto con un remolino que sale hacia un lado en lo alto, flequillo largo que le tapa
# medio ojo y puntas abiertas sobre las orejas; ojos blancos de pupila pequeña y sonrisa de pillo
CHARS['trump-loyal'] = {
    'body': 'normal', 'pal': pal('#c8a050', '#fcdcb8', iris='#2a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 72), (-6, 74, 1), (8, 60), (8, 30), (18, 8), (-14, 4, 1), (24, -6), (50, -4), (78, 4), (92, 26), (96, 58), (110, 70, 1), (86, 72),
                         (84, 56), (16, 56)])),
              L(outline([(60, 2), (84, 14), (94, 44), (90, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 36), (30, 20), (52, 14), (76, 20), (88, 38), (90, 60), (82, 50), (76, 60, 1), (68, 42), (62, 58), (58, 84, 1), (52, 58),
                      (44, 42), (34, 56, 1), (28, 44), (20, 58, 1)]),
              L(outline([(26, 22), (48, 16), (38, 28)]), 'light', 'f', False)] + white_eyes(78, 15, 6, 5, 1.6),
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (90, 12), (70, 0), (60, -18, 1), (46, -2), (20, 4), (6, 26), (2, 56), (-8, 72, 1), (10, 72), (16, 86),
                        (30, 78), (44, 72)])),
             L(outline([(4, 32), (26, 40), (28, 70), (8, 64)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 66), (88, 80, 1), (84, 50), (76, 34)])] + side_eye(78),
    'back': [L(outline([(12, 78), (-8, 76, 1), (8, 62), (8, 30), (18, 8), (50, -6), (80, 2), (94, -6, 1), (92, 26), (94, 60), (112, 74, 1), (88, 78), (70, 84),
                        (50, 86), (30, 84)])),
             L(outline([(56, 4), (84, 14), (94, 48), (90, 76), (64, 84)]), 'shade', 'b', False),
             strand([(14, 30), (50, 40), (86, 30)], 'deep', 'b', 1.0), strand([(12, 48), (50, 56), (88, 48)], 'deep', 'b', 1.0)],
}

# Billy Lingsoo: cara ancha y morena de orejas grandes; pelo azul marino como un gorro de punto plano con dos orejitas de
# gato arriba; ojos blancos de pupila pequeña y una bocaza abierta de risa
CHARS['billy-lingsoo'] = {
    'body': 'corpulento', 'pal': pal('#2a2844', '#b87c4c', iris='#2a2a2a', mouth_in='#4a1a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': WIDE_FACE, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(16, 58), (14, 20), (18, -14, 1), (30, 6), (70, 6), (82, -14, 1), (86, 20), (84, 58), (50, 54)])),
              L(outline([(60, 8), (80, 2), (84, 54), (70, 52)]), 'shade', 'b', False),
              L(outline([(22, 4), (24, -6), (30, 4)]), 'light', 'b', False)] + white_eyes(74, 16, 7, 4.6, 2)
             + [L(outline([(24, 88), (50, 92), (76, 88), (70, 104), (50, 110), (30, 104)]), 'mouth_in', 'f', ln=True),
                L(outline([(28, 89), (50, 93), (72, 89), (70, 95), (30, 95)]), WHITE, 'f', False)],
    'side': [L(outline([(70, 40), (76, 22), (62, 0), (58, -18, 1), (44, -2), (20, 4), (8, 30), (10, 56), (40, 50)])),
             L(outline([(10, 30), (30, 34), (30, 54), (12, 54)]), 'shade', 'b', False)] + side_eye(74)
            + [L(outline([(80, 88), (96, 86), (94, 100), (82, 100)]), 'mouth_in', 'f', ln=True)],
    'back': [L(outline([(14, 64), (12, 20), (16, -14, 1), (30, 6), (70, 6), (84, -14, 1), (88, 20), (86, 64), (50, 70)])),
             L(outline([(56, 8), (80, 2), (86, 62), (62, 68)]), 'shade', 'b', False),
             L(quad((14, 62), (50, 70), (86, 62)), OUTC, 'f', False, False, 1.4)],
}
