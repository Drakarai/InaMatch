"""Royal Academy de Victory Road (vr-senjutsu-no-teikoku, 戦術の帝国): sus modelos 3D de Inazuma Eleven: Victory Road
(英雄たちのヴィクトリーロード) en la enciclopedia. Son personajes nuevos de Victory Road con un solo modelo cada uno; muchos
llevan pintura negra de guerra alrededor de los ojos. Ningún id coge por prefijo el dibujo de otro."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_ouja_raimon import puff
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (24, 22, 26, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


def tears(y=82, c=BLACK):
    """Rayas negras que caen de los ojos (pintura de guerra de la Royal)."""
    return [L([(33, y), (32, y + 8)], c, 'f', False, False, 1.4), L([(67, y), (68, y + 8)], c, 'f', False, False, 1.4)]


# Jinno Ashley (Ashlan Panoptos, portero): pelo castaño en pinchos cortos revueltos por todos lados; un antifaz negro que
# le tapa los ojos con dibujos blancos en forma de rayo a los lados; ojos amarillo verdoso y cara seria
CHARS['ashlan-panoptos'] = {
    'body': 'normal', 'pal': pal('#6a3a2a', '#fbe0cc', iris='#a8b85a', shade='#4e2a1e', deep='#3a1e14'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 74), (6, 64, 1), (8, 52), (-6, 42, 1), (6, 32), (0, 16, 1), (16, 14), (16, -2, 1), (32, 4), (40, -12, 1), (50, 0), (60, -12, 1), (68, 4),
                         (84, -2, 1), (84, 14), (100, 16, 1), (94, 32), (106, 42, 1), (92, 52), (94, 64, 1), (84, 74), (82, 60), (18, 60)])),
              L(outline([(60, -12), (68, 4), (84, -2), (84, 14), (100, 16), (94, 32), (106, 42), (92, 52), (86, 40), (72, 18)]), 'shade', 'b', False),
              fr([(14, 66, 1), (12, 44), (24, 28), (36, 32), (44, 20, 1), (50, 30), (58, 20, 1), (64, 32), (76, 28), (88, 44), (86, 66, 1), (78, 54), (22, 54)]),
              L(outline([(16, 72), (24, 64), (40, 66), (50, 70), (60, 66), (76, 64), (84, 72), (80, 84), (64, 86), (50, 80), (36, 86), (20, 84)]), BLACK, 'f', False),
              L(ell(36, 76, 5, 4.6), WHITE, 'f', False), L(ell(64, 76, 5, 4.6), WHITE, 'f', False),
              L(ell(36, 76, 3.4, 3.6), 'iris', 'f', False), L(ell(64, 76, 3.4, 3.6), 'iris', 'f', False),
              L(ell(36, 76, 1.5, 1.6), BLACK, 'f', False), L(ell(64, 76, 1.5, 1.6), BLACK, 'f', False),
              L([(20, 66), (24, 74), (20, 82)], WHITE, 'f', False, False, 1.4), L([(26, 64), (28, 72)], WHITE, 'f', False, False, 1.2),
              L([(80, 66), (76, 74), (80, 82)], WHITE, 'f', False, False, 1.4), L([(74, 64), (72, 72)], WHITE, 'f', False, False, 1.2)],
    'side': [L(outline([(64, 56), (70, 46), (86, 44), (98, 38, 1), (90, 28), (100, 14, 1), (82, 12), (84, -6, 1), (66, 2), (58, -14, 1), (46, 0), (30, -10, 1), (26, 6),
                        (8, 4, 1), (12, 20), (-6, 28, 1), (6, 40), (-6, 54, 1), (6, 60), (2, 74, 1), (16, 72), (20, 86, 1), (30, 74), (44, 64)])),
             L(outline([(4, 40), (26, 44), (32, 72), (12, 72)]), 'shade', 'b', False),
             L(outline([(60, 68), (76, 64), (88, 66), (88, 82), (74, 84), (60, 76)]), BLACK, 'f', False),
             L([(70, 66), (76, 74), (72, 82)], WHITE, 'f', False, False, 1.3),
             L(ell(82, 75, 3.4, 4), WHITE, 'f', False), L(ell(83, 75, 2.2, 2.8), 'iris', 'f', False)],
    'back': [L(outline([(16, 88), (6, 76, 1), (8, 62), (-6, 50, 1), (6, 36), (0, 18, 1), (16, 14), (16, -2, 1), (32, 4), (40, -12, 1), (50, 0), (60, -12, 1), (68, 4),
                        (84, -2, 1), (84, 14), (100, 18, 1), (94, 36), (106, 50, 1), (92, 62), (94, 76, 1), (84, 88), (50, 94)])),
             L(outline([(56, 0), (84, 8), (100, 40), (90, 84), (64, 90), (70, 40)]), 'shade', 'b', False),
             L(quad((6, 64), (50, 70), (94, 64)), BLACK, 'b', False, False, 3.0),
             strand([(30, 20), (36, 50)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50)], 'deep', 'b', 1.0)],
}

# Erusaki Eichi (Hudson Headland): melena lisa gris oscuro con raya en medio que le cae a los lados como una capucha hasta
# el pecho; dos adornos metálicos en triángulo a los lados de la cabeza; ojos negros afilados con rayas negras debajo
CHARS['hudson-headland'] = {
    'body': 'delgado', 'pal': pal('#5a5468', '#fbdcc4', iris='#2a2430', shade='#423c4e', deep='#2e2a38', metal='#d8d8e0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 120), (2, 80), (4, 40), (14, 14), (36, -2), (64, -2), (86, 14), (96, 40), (98, 80), (92, 120), (82, 118), (80, 60), (20, 60),
                         (18, 118)])),
              L(outline([(60, 0), (86, 14), (96, 44), (96, 116), (84, 70)]), 'shade', 'b', False),
              fr([(12, 116), (10, 60), (14, 34), (30, 16), (50, 10), (70, 16), (86, 34), (90, 60), (88, 116), (80, 116), (80, 68), (72, 46), (56, 36), (50, 30), (44, 36),
                  (28, 46), (20, 68), (20, 116)]),
              strand([(50, 12), (50, 30)], 'deep', 'f', 1.2),
              L([(4, 46), (-6, 46), (4, 58), (4, 46)], 'metal', 'f', False, False, 1.6), L([(96, 46), (106, 46), (96, 58), (96, 46)], 'metal', 'f', False, False, 1.6)]
             + tears(),
    'side': [L(outline([(60, 66), (66, 50), (84, 46), (94, 30), (86, 8), (60, -4), (32, -2), (10, 12), (0, 40), (0, 80), (4, 110), (24, 120), (40, 104), (50, 80)])),
             L(outline([(0, 50), (30, 56), (40, 104), (24, 120), (4, 110)]), 'shade', 'b', False),
             L(quad((24, 50), (56, 46), (78, 34)), 'metal', 'f', False, False, 1.8),
             fr([(66, 6), (90, 18), (96, 44), (94, 70, 1), (86, 56), (78, 42)])],
    'back': [L(outline([(10, 100), (2, 70), (4, 36), (14, 12), (36, -2), (64, -2), (86, 12), (96, 36), (98, 70), (90, 100), (70, 104), (50, 100), (30, 104)])),
             L(outline([(56, 0), (86, 14), (98, 44), (94, 96), (64, 96), (70, 50)]), 'shade', 'b', False),
             L(quad((4, 74), (50, 80), (96, 74)), 'deep', 'b', False, False, 3.0),
             L([(4, 46), (-6, 46), (4, 58), (4, 46)], 'metal', 'f', False, False, 1.6), L([(96, 46), (106, 46), (96, 58), (96, 46)], 'metal', 'f', False, False, 1.6)],
}

# Anza Naoichi (Vex Frieden): pelo morado corto y ahuecado, con las puntas hacia fuera a los lados y un mechón turquesa en
# forma de llama sobre la frente; ojos rojos muy abiertos con sombra negra alrededor y una sonrisa de dientes de loco
CHARS['vex-frieden'] = {
    'body': 'bajito', 'pal': pal('#8a3a96', '#fbe0cc', iris='#c82a2a', shade='#6a2a74', deep='#4e1e58', teal='#62e6d0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 74), (-6, 60, 1), (4, 48), (6, 22), (22, 4), (46, -4), (70, 0), (90, 14), (98, 36), (110, 52, 1), (94, 56), (86, 74), (82, 60), (18, 60)])),
              L(outline([(60, 0), (88, 14), (98, 40), (108, 52), (92, 54), (84, 36)]), 'shade', 'b', False),
              fr([(12, 66, 1), (6, 50), (14, 30), (34, 16), (60, 14), (84, 24), (96, 44), (104, 54, 1), (88, 52), (86, 66, 1), (76, 52), (60, 50), (46, 56), (34, 52),
                  (24, 58)]),
              L(outline([(30, 30), (44, 20), (62, 18), (76, 10, 1), (66, 22), (56, 26), (70, 28, 1), (54, 32), (40, 36), (32, 40, 1)]), 'teal', 'f', ln=True),
              L(ell(36, 76, 7, 6), BLACK, 'f', False), L(ell(64, 76, 7, 6), BLACK, 'f', False),
              L(ell(36, 75, 4.6, 4.8), WHITE, 'f', False), L(ell(64, 75, 4.6, 4.8), WHITE, 'f', False),
              L(ell(36, 75, 2.2, 2.4), 'iris', 'f', False), L(ell(64, 75, 2.2, 2.4), 'iris', 'f', False)],
    'side': [L(outline([(60, 60), (66, 48), (84, 46), (94, 36), (90, 14), (66, -2), (36, -2), (14, 10), (2, 34), (4, 58), (-8, 70, 1), (14, 70), (34, 70), (46, 62)])),
             L(outline([(4, 34), (28, 38), (34, 68), (10, 66)]), 'shade', 'b', False),
             L(outline([(64, 14), (84, 10, 1), (78, 22), (88, 26, 1), (72, 30), (62, 26)]), 'teal', 'f', ln=True),
             fr([(66, 8), (90, 22), (96, 44), (92, 58, 1), (84, 50), (76, 40)])],
    'back': [L(outline([(14, 82), (-6, 66, 1), (4, 52), (6, 22), (22, 4), (46, -4), (70, 0), (90, 14), (98, 36), (110, 56, 1), (94, 62), (86, 82), (50, 90)])),
             L(outline([(56, 0), (88, 14), (98, 44), (90, 80), (64, 86), (70, 40)]), 'shade', 'b', False)],
}

# Meteo Kirameki (Asten Royds): grandullón de cara ancha y redonda morena con papada; una cresta de pinchos azul pizarra
# sobre el pelo rapado, y unas gafas redondas de espiral sobre un antifaz negro
_royds_face = blob([(10, 50), (50, 36), (90, 50), (100, 80), (92, 104), (70, 116), (50, 118), (30, 116), (8, 104), (0, 80)])
CHARS['asten-royds'] = {
    'body': 'corpulento', 'pal': pal('#3e4e6e', '#b47a5a', iris='#2a2a2a', shade='#2c3a54', deep='#1e283e', glass='#e0e0e4', glass_d='#8a8a92'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': _royds_face, 'big_ears': 2, 'ear_out': 6},
    'front': [L(outline([(14, 56), (16, 36), (30, 24), (50, 20), (70, 24), (84, 36), (86, 56), (50, 50)])),
              L(outline([(26, 30), (16, -4, 1), (36, 22), (42, -14, 1), (50, 20), (58, -14, 1), (64, 22), (84, -4, 1), (74, 30)]), 'mid', 'f', ln=True),
              L(outline([(58, -14), (64, 22), (84, -4), (74, 30), (64, 30)]), 'shade', 'f', False),
              L(outline([(8, 70), (30, 62), (50, 70), (70, 62), (92, 70), (88, 88), (70, 90), (50, 84), (30, 90), (12, 88)]), BLACK, 'f', False),
              L(ell(32, 76, 10, 8), 'glass', 'f', ln=True), L(ell(68, 76, 10, 8), 'glass', 'f', ln=True),
              L(ell(32, 76, 6, 4.6), 'glass_d', 'f', False), L(ell(68, 76, 6, 4.6), 'glass_d', 'f', False),
              L(ell(32, 76, 3, 2.2), 'glass', 'f', False), L(ell(68, 76, 3, 2.2), 'glass', 'f', False),
              L(quad((40, 106), (50, 110), (60, 106)), 'skin_d', 'f', False, False, 1.4)],
    'side': [L(outline([(10, 60), (14, 36), (34, 22), (60, 20), (80, 30), (88, 46), (60, 46)])),
             L(outline([(26, 26), (10, 4, 1), (36, 22), (44, -14, 1), (54, 20), (72, -8, 1), (70, 26)]), 'mid', 'f', ln=True),
             L(quad((10, 68), (50, 62), (90, 70)), BLACK, 'f', False, False, 7.0),
             L(ell(82, 74, 7, 8), 'glass', 'f', ln=True), L(ell(83, 74, 3.6, 4.4), 'glass_d', 'f', False)],
    'back': [L(outline([(14, 60), (14, 36), (30, 22), (50, 18), (70, 22), (86, 36), (86, 60), (50, 66)])),
             L(outline([(26, 30), (16, -4, 1), (36, 22), (42, -14, 1), (50, 20), (58, -14, 1), (64, 22), (84, -4, 1), (74, 30)]), 'mid', 'f', ln=True),
             L(quad((10, 64), (50, 70), (90, 64)), BLACK, 'f', False, False, 7.0)],
}

# Inobe Kiko (Ruelle Neurivieu): niña bajita; flequillo recto azul vivo sobre la frente y el resto del pelo gris oscuro,
# recogido en lazos y aros que salen de la cabeza como antenas (dos arriba, dos a cada lado y dos que bajan en curva);
# ojos grises afilados con sombra negra y colorete
CHARS['ruelle-neurivieu'] = {
    'body': 'chica', 'pal': pal('#4a4646', '#fcdcc8', iris='#5a6a7a', shade='#363232', deep='#262222', blue='#2a6ad8', blush='#f0a0a0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(24, -26), (34, -26), (36, 6), (24, 6)]), 'mid', 'b'), L(outline([(76, -26), (66, -26), (64, 6), (76, 6)]), 'mid', 'b'),
              L(ell(29, -14, 2.4, 7), 'skin', 'b', False), L(ell(71, -14, 2.4, 7), 'skin', 'b', False),
              L(outline([(10, 26), (-14, 14, 1), (-12, 34), (8, 38)]), 'mid', 'b'), L(outline([(90, 26), (114, 14, 1), (112, 34), (92, 38)]), 'mid', 'b'),
              L(outline([(8, 44), (-16, 44, 1), (-10, 60), (10, 56)]), 'mid', 'b'), L(outline([(92, 44), (116, 44, 1), (110, 60), (90, 56)]), 'mid', 'b'),
              L(rope((14, 70), (-6, 84), (2, 108), 5), 'mid', 'b'), L(rope((86, 70), (106, 84), (98, 108), 5), 'mid', 'b'),
              L(outline([(12, 80), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (88, 80), (80, 62), (20, 62)])),
              L(outline([(60, 4), (82, 14), (92, 44), (88, 76), (80, 50)]), 'shade', 'b', False),
              fr([(18, 64), (16, 40), (28, 24), (50, 18), (72, 24), (84, 40), (82, 64), (74, 62), (72, 66, 1), (66, 60), (56, 62), (52, 66, 1), (46, 60), (36, 62),
                  (32, 66, 1), (26, 62)], 'blue'),
              L(ell(32, 88, 5, 2.4), 'blush', 'f', False), L(ell(68, 88, 5, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(34, -26), (46, -26), (44, 8), (32, 8)]), 'mid', 'b'),
             L(outline([(20, 30), (-6, 20, 1), (-4, 40), (18, 42)]), 'mid', 'b'), L(rope((24, 70), (2, 86), (8, 108), 5), 'mid', 'b'),
             L(outline([(60, 58), (66, 46), (84, 44), (92, 30), (84, 8), (58, -2), (32, 2), (12, 18), (6, 44), (12, 70), (30, 74), (46, 62)])),
             L(outline([(8, 30), (30, 36), (36, 66), (14, 68)]), 'shade', 'b', False),
             fr([(66, 8), (88, 18), (96, 40), (92, 62, 1), (84, 58), (78, 42)], 'blue'),
             L(ell(78, 88, 4, 2.2), 'blush', 'f', False)],
    'back': [L(outline([(24, -26), (34, -26), (36, 6), (24, 6)]), 'mid', 'b'), L(outline([(76, -26), (66, -26), (64, 6), (76, 6)]), 'mid', 'b'),
             L(outline([(10, 26), (-14, 14, 1), (-12, 34), (8, 38)]), 'mid', 'b'), L(outline([(90, 26), (114, 14, 1), (112, 34), (92, 38)]), 'mid', 'b'),
             L(outline([(8, 44), (-16, 44, 1), (-10, 60), (10, 56)]), 'mid', 'b'), L(outline([(92, 44), (116, 44, 1), (110, 60), (90, 56)]), 'mid', 'b'),
             L(rope((14, 70), (-6, 84), (2, 108), 5), 'mid', 'b'), L(rope((86, 70), (106, 84), (98, 108), 5), 'mid', 'b'),
             L(outline([(12, 76), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (88, 76), (50, 84)])),
             L(outline([(56, 4), (82, 14), (92, 44), (86, 72), (60, 60)]), 'shade', 'b', False)],
}

# Tonosaki Theo (Theon Stillcliffe): piel muy oscura; pelo castaño oscuro recogido en un moño alto y recto como una torre,
# con una cinta blanca fina que le rodea la cabeza en curva; ojos verdes caídos con rayas negras debajo
CHARS['theon-stillcliffe'] = {
    'body': 'delgado', 'pal': pal('#3a2420', '#5a3a30', iris='#a8d84a', shade='#281816', deep='#1c100e', band='#e8e0d8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 70), (10, 40), (22, 16), (50, 8), (78, 16), (90, 40), (84, 70), (78, 50), (22, 50)])),
              L(outline([(36, 10), (30, -28, 1), (70, -28, 1), (64, 10)])),
              L(outline([(52, -28), (70, -28, 1), (64, 10), (54, 10)]), 'shade', 'b', False),
              L(outline([(16, 52), (22, 40), (36, 32), (46, 46), (50, 56), (54, 46), (64, 32), (78, 40), (84, 52), (78, 46), (66, 42), (56, 54), (50, 64), (44, 54),
                         (34, 42), (22, 46)]), 'mid', 'f'),
              L(quad((14, 54), (24, 14), (50, 14)) + quad((50, 14), (76, 14), (86, 54))[1:], 'band', 'f', False, False, 1.6)] + tears(84),
    'side': [L(outline([(64, 50), (72, 40), (86, 40), (90, 24), (74, 8), (46, 4), (22, 12), (8, 34), (8, 60), (20, 72), (36, 68), (48, 56)])),
             L(outline([(26, 10), (18, -28), (38, -30), (48, 8)])),
             L(outline([(2, 40), (14, 30), (4, 110), (-8, 104)]), 'mid', 'b'),
             L(outline([(8, 36), (30, 40), (36, 66), (18, 70)]), 'shade', 'b', False),
             L(quad((84, 40), (60, 10), (14, 30)), 'band', 'f', False, False, 1.6),
             L([(80, 84), (81, 92)], BLACK, 'f', False, False, 1.4)],
    'back': [L(outline([(16, 78), (10, 40), (22, 16), (50, 8), (78, 16), (90, 40), (84, 78), (50, 86)])),
             L(outline([(36, 10), (30, -28, 1), (70, -28, 1), (64, 10)])),
             L(outline([(40, 60), (60, 60), (58, 112), (42, 112)])),
             L(outline([(56, 10), (80, 18), (90, 44), (84, 74), (60, 60)]), 'shade', 'b', False),
             L(quad((12, 42), (50, 120), (88, 42)), 'band', 'f', False, False, 1.6)],
}

# Honnouji Nemi (Ciel Natcherall): pelo negro en forma de casco de seta (corte tazón) con las puntas de los lados hacia
# fuera y un flequillo recto partido sobre las cejas; ojos grises afilados con raya lila y boca de gato
CHARS['ciel-natcherall'] = {
    'body': 'normal', 'pal': pal('#1c1e24', '#fce4d4', iris='#9aa0a8', shade='#121418', deep='#2c3038', light='#3a3e48'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 76), (12, 56), (-4, 50, 1), (6, 36), (8, 14), (28, -2), (50, -6), (72, -2), (92, 14), (94, 36), (104, 50, 1), (88, 56), (84, 76), (82, 60),
                         (18, 60)])),
              L(outline([(60, -4), (90, 12), (94, 40), (102, 50), (86, 50)]), 'shade', 'b', False),
              fr([(14, 66), (10, 48), (16, 28), (34, 16), (66, 16), (84, 28), (90, 48), (86, 66), (80, 60), (74, 64, 1), (64, 60), (54, 64, 1), (48, 60), (36, 62),
                  (28, 66, 1), (22, 60)]),
              strand([(26, 10), (50, 4), (74, 10)], 'light', 'f', 1.2),
              L(quad((42, 94), (46, 97), (50, 94)) + quad((50, 94), (54, 97), (58, 94))[1:], OUTC, 'f', False, False, 1.2),
              L(outline([(49, 84), (51, 84), (50, 86)]), 'skin_d', 'f', False)],
    'side': [L(outline([(60, 62), (66, 52), (84, 50), (94, 36), (90, 12), (66, -4), (36, -4), (12, 10), (2, 36), (6, 62), (-4, 74, 1), (18, 82), (36, 72), (46, 66)])),
             L(outline([(4, 34), (30, 40), (34, 72), (12, 72)]), 'shade', 'b', False),
             fr([(66, 10), (90, 22), (96, 44), (92, 62, 1), (84, 58), (76, 42)])],
    'back': [L(outline([(16, 80), (12, 60), (-4, 54, 1), (6, 38), (8, 14), (28, -2), (50, -6), (72, -2), (92, 14), (94, 38), (104, 54, 1), (88, 60), (84, 80),
                        (66, 88), (50, 84), (34, 88)])),
             L(outline([(56, -2), (90, 12), (96, 44), (86, 80), (64, 86), (70, 40)]), 'shade', 'b', False),
             strand([(10, 50), (50, 58), (90, 50)], 'deep', 'b', 1.0)],
}

# Homura Eisuke (Syd Faircrest): piel morena; pelo fucsia enorme y revuelto peinado hacia arriba y hacia su izquierda en
# mechones ondulados, con el lado derecho rapado gris oscuro; mascarilla negra que le tapa la boca y ojos grises afilados
CHARS['syd-faircrest'] = {
    'body': 'delgado', 'pal': pal('#d8285a', '#a8704e', iris='#9aa4b0', shade='#a81c44', deep='#7c1432', shaved='#3a3a3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 66), (12, 46), (16, 30), (40, 24), (70, 26), (88, 40), (90, 66), (82, 56), (20, 56)]), 'shaved', 'b'),
              L(outline([(70, 30), (80, 6), (100, -10, 1), (78, -14), (64, -28, 1), (50, -18), (32, -30, 1), (26, -14), (4, -12, 1), (10, 4), (-10, 14, 1), (4, 26),
                         (-8, 50, 1), (6, 56), (-6, 80, 1), (8, 84), (4, 104, 1), (16, 96), (18, 60), (30, 40), (46, 36), (60, 42)])),
              L(outline([(32, -30), (26, -14), (4, -12), (10, 4), (-10, 14), (4, 26), (-8, 50), (6, 56), (12, 40), (24, 20)]), 'shade', 'b', False),
              fr([(72, 36), (66, 20), (48, 10), (26, 14), (12, 30), (6, 52), (10, 72, 1), (18, 56), (28, 46), (36, 60, 1), (40, 44), (52, 40), (64, 50, 1)]),
              strand([(60, 4), (40, 10), (20, 30)], 'deep', 'b', 1.0),
              L(outline([(24, 84), (40, 82), (50, 86), (60, 82), (76, 84), (80, 96), (70, 108), (50, 112), (30, 108), (20, 96)]), BLACK, 'f', False)],
    'side': [L(outline([(60, 56), (64, 46), (82, 44), (90, 30), (80, 14), (54, 8), (26, 12), (10, 30), (8, 56), (20, 70), (36, 66), (48, 58)]), 'shaved', 'b'),
             L(outline([(70, 30), (90, 22), (96, 4, 1), (78, 2), (70, -24, 1), (50, -16), (30, -30, 1), (24, -10), (2, -8, 1), (10, 8), (-10, 20, 1), (4, 34), (-4, 52, 1),
                        (10, 50), (14, 30), (40, 14), (60, 20)])),
             L(outline([(4, 30), (-4, 52), (10, 50), (14, 30)]), 'shade', 'b', False),
             L(outline([(70, 86), (88, 84), (90, 98), (80, 110), (62, 106)]), BLACK, 'f', False)],
    'back': [L(outline([(16, 80), (10, 46), (16, 26), (50, 18), (84, 26), (90, 46), (84, 80), (50, 86)]), 'shaved', 'b'),
             L(outline([(30, 30), (20, 6), (0, -10, 1), (22, -14), (36, -28, 1), (50, -18), (68, -30, 1), (74, -14), (96, -12, 1), (90, 4), (110, 14, 1), (96, 26),
                        (108, 50, 1), (94, 56), (106, 80, 1), (92, 84), (96, 104, 1), (80, 96), (76, 60), (64, 50), (50, 52), (40, 40)])),
             L(outline([(68, -30), (74, -14), (96, -12), (90, 4), (110, 14), (96, 26), (108, 50), (94, 56), (88, 40), (76, 20)]), 'shade', 'b', False)],
}

# Reidou Kaiya (Kaien Spiradawn): media melena rubia lisa hasta la mandíbula, abierta hacia fuera en las puntas, con un
# flequillo largo de mechones en punta que le llega a los ojos; ojos lila con ojeras oscuras y cara enfadada
CHARS['kaien-spiradawn'] = {
    'body': 'bajito', 'pal': pal('#f4cc78', '#fce0cc', iris='#a07ab8', shade='#d8a85a', deep='#b88a44', bag='#6a5a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 96), (-6, 98, 1), (2, 80), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (98, 80), (106, 98, 1), (88, 96), (82, 64),
                         (18, 64)])),
              L(outline([(60, 0), (84, 14), (96, 44), (98, 80), (104, 96), (88, 94), (82, 56)]), 'shade', 'b', False),
              fr([(10, 86), (8, 50), (18, 24), (40, 12), (60, 12), (82, 24), (92, 50), (90, 86, 1), (82, 66), (76, 72, 1), (72, 56), (62, 62, 1), (58, 50), (52, 76, 1),
                  (46, 50), (40, 64, 1), (32, 54), (26, 72, 1), (20, 62)]),
              strand([(50, 4), (50, 14)], 'deep', 'f', 1.2),
              L(quad((28, 82), (36, 85), (44, 82)), 'bag', 'f', False, False, 1.2), L(quad((56, 82), (64, 85), (72, 82)), 'bag', 'f', False, False, 1.2)],
    'side': [L(outline([(60, 64), (66, 52), (84, 48), (94, 32), (88, 8), (62, -4), (34, -4), (10, 10), (0, 40), (0, 80), (-8, 98, 1), (14, 96), (36, 100, 1), (42, 84),
                        (50, 74)])),
             L(outline([(0, 40), (28, 44), (40, 84), (36, 100), (14, 96), (-8, 98), (0, 80)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (96, 44), (94, 76, 1), (86, 58), (80, 66, 1), (76, 42)])],
    'back': [L(outline([(12, 96), (-8, 100, 1), (2, 80), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (98, 80), (108, 100, 1), (88, 96), (70, 100),
                        (50, 96), (30, 100)])),
             L(ell(66, 34, 22, 18), 'shade', 'b', False)],
}

# Hoshimizawa Kyou (Kyo Seestar): piel morena; pelo blanco menta abundante y ondulado hasta los hombros, en mechones
# revueltos que se ensombrecen a rosado por detrás; ojos turquesa redondos muy abiertos con ojeras, nariz roja y sonrisa
CHARS['kyo-seestar'] = {
    'body': 'normal', 'pal': pal('#eef6ee', '#9a6444', iris='#4ac8c8', shade='#c8b4ae', deep='#a8948e', nose='#c84a3a', bag='#5a3a2a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'nose': (50, 86, 2.4)},
    'front': [L(outline([(12, 100), (-4, 96, 1), (4, 80), (-6, 66, 1), (4, 56), (0, 34), (12, 12), (26, 0), (36, -10, 1), (48, -2), (64, -6), (80, 4), (94, 22),
                         (100, 40), (96, 58), (106, 70, 1), (96, 80), (104, 96, 1), (88, 100), (82, 66), (18, 66)])),
              L(outline([(4, 70), (12, 100), (-4, 96), (4, 80)]), 'shade', 'f', False), L(outline([(96, 70), (88, 100), (104, 96), (96, 80)]), 'shade', 'f', False),
              fr([(10, 84), (8, 50), (18, 26), (40, 16), (62, 16), (82, 26), (92, 50), (90, 84, 1), (82, 66), (78, 54), (70, 58, 1), (66, 46), (54, 52), (48, 64, 1),
                  (44, 50), (34, 56, 1), (28, 52), (20, 66)]),
              strand([(26, 30), (36, 42)], 'shade', 'f', 1.2), strand([(70, 28), (64, 42)], 'shade', 'f', 1.2),
              L(quad((28, 83), (36, 86), (44, 83)), 'bag', 'f', False, False, 1.2), L(quad((56, 83), (64, 86), (72, 83)), 'bag', 'f', False, False, 1.2)],
    'side': [L(outline([(60, 66), (66, 52), (84, 48), (96, 34), (90, 10), (64, -6), (34, -6), (10, 8), (-2, 36), (-8, 52, 1), (2, 60), (-6, 80, 1), (6, 84), (2, 102, 1),
                        (20, 94), (30, 106, 1), (40, 90), (50, 76)])),
             L(outline([(-2, 44), (30, 50), (40, 90), (30, 106), (20, 94), (2, 102), (6, 84), (-6, 80), (2, 60)]), 'shade', 'b', False),
             fr([(66, 6), (90, 20), (98, 44), (94, 66, 1), (86, 56), (78, 42)])],
    'back': [L(outline([(12, 102), (-6, 98, 1), (4, 80), (-6, 66, 1), (4, 56), (0, 34), (12, 12), (26, 0), (36, -10, 1), (48, -2), (64, -6), (80, 4), (94, 22),
                        (100, 40), (96, 58), (106, 70, 1), (96, 80), (106, 98, 1), (88, 102), (74, 108, 1), (62, 100), (50, 110, 1), (38, 100), (26, 108, 1)])),
             L(outline([(0, 50), (30, 40), (60, 50), (100, 44), (96, 80), (88, 102), (62, 100), (38, 100), (12, 102), (4, 80)]), 'shade', 'b', False)],
}

# Motoyashiki Kuuki (Solan Brightmoor): grandullón pálido; pelo blanco con mechones azul marino, una melena enorme que le
# cae como una capa por la espalda y los hombros; un mechón azul le tapa el ojo izquierdo; ojo lila y sonrisa torcida
CHARS['solan-brightmoor'] = {
    'body': 'corpulento', 'pal': pal('#e8e6e6', '#fbe4d6', iris='#8a6aa8', shade='#c4aeaa', deep='#a8908c', navy='#1e2a4e', navy_d='#141c34'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(puff(-4, 96, 22, 14, 5, 0.3)), L(puff(104, 96, 22, 14, 5, 0.6)),
              L(outline([(10, 100), (4, 60), (8, 30), (24, 6), (50, -4), (76, 6), (92, 30), (96, 60), (90, 100), (82, 66), (18, 66)])),
              L(outline([(60, -2), (86, 12), (96, 44), (92, 96), (82, 56)]), 'shade', 'b', False),
              fr([(12, 80), (10, 46), (20, 22), (44, 10), (50, 20), (40, 34), (28, 50), (20, 70)]),
              L(outline([(50, 10), (70, 14), (88, 30), (94, 56), (90, 80), (84, 66), (76, 58), (66, 64), (58, 92, 1), (54, 62), (48, 40), (44, 24)]), 'navy', 'f'),
              L(outline([(22, 30), (34, 16), (40, 26), (30, 40)]), 'navy', 'f', False),
              L(ell(18, 82, 1.2, 1.2), OUTC, 'f', False)],
    'side': [L(outline([(60, 62), (66, 50), (84, 46), (94, 30), (86, 6), (60, -6), (30, -4), (6, 14), (-6, 50), (-14, 96), (-24, 120, 1), (0, 112), (20, 118, 1),
                        (30, 100), (44, 80)])),
             L(outline([(-6, 50), (24, 56), (40, 84), (20, 118), (0, 112), (-24, 120), (-14, 96)]), 'shade', 'b', False),
             L(outline([(70, 4), (90, 18), (96, 44), (92, 70, 1), (84, 52), (76, 40)]), 'navy', 'f')],
    'back': [L(puff(-8, 90, 24, 18, 5, 0.3)), L(puff(108, 90, 24, 18, 5, 0.6)),
             L(outline([(4, 110), (0, 60), (8, 26), (24, 4), (50, -4), (76, 4), (92, 26), (100, 60), (96, 110), (74, 118), (50, 112), (26, 118)])),
             L(outline([(0, 70), (30, 60), (50, 70), (70, 60), (100, 70), (96, 110), (74, 118), (50, 112), (26, 118), (4, 110)]), 'shade', 'b', False),
             L(outline([(64, 0), (80, 8), (70, 30)]), 'navy', 'b', False),
             L(outline([(-20, 100), (-30, 120, 1), (-10, 110)]), 'navy', 'f', False), L(outline([(120, 100), (130, 120, 1), (110, 110)]), 'navy', 'f', False)],
}

# Yozakura Shishio (Lenox Grinder): piel morena; pelo gris azulado peinado hacia atrás en mechones de punta que le caen
# hasta la nuca y salen a los lados; unos auriculares rojos con la diadema por encima de la cabeza; ojos naranja afilados
# con pestañas gruesas y cejas pobladas
CHARS['lenox-grinder'] = {
    'body': 'normal', 'pal': pal('#5e6e74', '#a06a4a', iris='#e0701e', shade='#46545a', deep='#343e44', red='#c82a3a', red_d='#9a1e2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 100), (-6, 92, 1), (4, 78), (-8, 64, 1), (4, 54), (2, 30), (16, 8), (30, -4, 1), (40, 2), (50, -6), (60, 2), (70, -4, 1), (84, 8), (98, 30),
                         (96, 54), (108, 64, 1), (96, 78), (106, 92, 1), (88, 100), (82, 64), (18, 64)])),
              L(outline([(60, 2), (84, 10), (98, 34), (96, 54), (106, 64), (96, 78), (88, 60)]), 'shade', 'b', False),
              fr([(14, 72), (12, 46), (20, 30), (36, 24), (50, 32), (64, 24), (80, 30), (88, 46), (86, 72), (78, 60), (72, 50), (60, 44), (50, 52), (40, 44), (28, 50),
                  (22, 60)]),
              strand([(36, 24), (44, 4)], 'deep', 'f', 1.0), strand([(64, 24), (56, 4)], 'deep', 'f', 1.0),
              L(quad((10, 52), (50, -16), (90, 52)), 'red', 'f', False, False, 4.4),
              L(outline([(4, 60), (14, 56), (18, 86), (8, 88), (0, 74)]), 'red', 'f', ln=True), L(outline([(96, 60), (86, 56), (82, 86), (92, 88), (100, 74)]), 'red', 'f', ln=True)],
    'side': [L(outline([(60, 60), (66, 48), (84, 46), (94, 30), (86, 6), (60, -6), (32, -4), (14, 8, 1), (12, 22), (-8, 30, 1), (4, 42), (-12, 56, 1), (2, 62),
                        (-8, 80, 1), (8, 82), (2, 100, 1), (22, 92), (30, 104, 1), (38, 88), (48, 74)])),
             L(outline([(2, 42), (26, 48), (38, 88), (22, 92), (6, 92)]), 'shade', 'b', False),
             fr([(68, 10), (90, 22), (96, 44), (92, 62, 1), (84, 52), (76, 40)]),
             L(quad((34, 70), (40, 20), (60, -4)), 'red', 'f', False, False, 4.4),
             L(ell(44, 72, 11, 12), 'red', 'f', ln=True), L(ell(44, 72, 6, 7), 'red_d', 'f', False)],
    'back': [L(outline([(12, 104), (-6, 96, 1), (4, 80), (-8, 66, 1), (4, 56), (2, 30), (16, 8), (30, -4, 1), (40, 2), (50, -6), (60, 2), (70, -4, 1), (84, 8), (98, 30),
                        (96, 56), (108, 66, 1), (96, 80), (106, 96, 1), (88, 104), (74, 110, 1), (62, 100), (50, 112, 1), (38, 100), (26, 110, 1)])),
             L(outline([(56, 2), (84, 10), (98, 40), (96, 96), (62, 100), (70, 50)]), 'shade', 'b', False),
             L(quad((10, 52), (50, -16), (90, 52)), 'red', 'f', False, False, 4.4),
             L(outline([(4, 60), (14, 56), (18, 86), (8, 88), (0, 74)]), 'red', 'f', ln=True), L(outline([(96, 60), (86, 56), (82, 86), (92, 88), (100, 74)]), 'red', 'f', ln=True)],
}

# Horiuchi Honoka (Ophelia Ennercourt): niña de melena gris ondulada y abundante que se abre en rizos hasta los hombros,
# con las puntas azul marino casi negro en pico; ojos morados grandes con pestañas y sonrisa
CHARS['ophelia-ennercourt'] = {
    'body': 'chica', 'pal': pal('#7c7c7c', '#fce0d0', iris='#8a3a8a', shade='#5e5c5c', deep='#4a4848', tip='#1e2232'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 106), (-14, 112, 1), (-6, 96), (-10, 76), (0, 60), (0, 34), (12, 10), (36, -4), (64, -4), (88, 10), (100, 34), (100, 60), (110, 76),
                         (106, 96), (114, 112, 1), (90, 106), (82, 66), (18, 66)])),
              L(outline([(-14, 112), (-6, 96), (4, 98), (10, 106)]), 'tip', 'f', False), L(outline([(114, 112), (106, 96), (96, 98), (90, 106)]), 'tip', 'f', False),
              L(outline([(-10, 76), (-20, 70, 1), (-4, 66)]), 'tip', 'b'), L(outline([(110, 76), (120, 70, 1), (104, 66)]), 'tip', 'b'),
              L(outline([(60, -2), (88, 12), (100, 44), (100, 90), (84, 60)]), 'shade', 'b', False),
              fr([(10, 84), (6, 50), (16, 26), (40, 14), (62, 14), (84, 26), (94, 50), (90, 84), (82, 66), (76, 54), (64, 58), (58, 48), (50, 56), (42, 48), (34, 58),
                  (22, 56), (18, 70)]),
              L(puff(10, 80, 10, 12, 4, 0.2), 'mid', 'f'), L(puff(90, 80, 10, 12, 4, 0.6), 'mid', 'f')],
    'side': [L(outline([(60, 64), (66, 50), (84, 46), (94, 30), (86, 6), (60, -6), (30, -4), (8, 14), (-2, 44), (-14, 70), (-24, 96, 1), (-4, 92), (-16, 112, 1), (10, 102),
                        (20, 116, 1), (30, 96), (46, 78)])),
             L(outline([(-24, 96), (-4, 92), (-16, 112), (10, 102), (20, 116), (14, 98)]), 'tip', 'b', False),
             L(outline([(0, 44), (30, 50), (40, 84), (20, 100), (-10, 90)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (96, 42), (92, 62, 1), (84, 56), (76, 40)])],
    'back': [L(outline([(8, 108), (-14, 114, 1), (-6, 96), (-10, 76), (0, 60), (0, 34), (12, 10), (36, -4), (64, -4), (88, 10), (100, 34), (100, 60), (110, 76),
                        (106, 96), (114, 114, 1), (92, 108), (70, 114, 1), (58, 100), (50, 110), (42, 100), (30, 114, 1)])),
             L(outline([(-14, 114), (-6, 96), (8, 100), (8, 108)]), 'tip', 'b', False), L(outline([(114, 114), (106, 96), (92, 100), (92, 108)]), 'tip', 'b', False),
             L(outline([(50, 0), (70, 10), (80, 60), (60, 100), (50, 110), (40, 60)]), 'shade', 'b', False)],
}

# Tetsubashira Dousuke (Riggs Fornstrut): grandullón moreno de cara ancha y mandíbula cuadrada; pelo azul marino peinado
# hacia atrás, con dos franjas naranja a los lados, que acaba en una cola ancha que le cae por la nuca; cejas negras
# enormes, ojos rojos pequeños con manchas blancas debajo y boca apretada
_riggs_face = blob([(10, 50), (50, 40), (90, 50), (98, 80), (94, 104), (74, 116), (50, 118), (26, 116), (6, 104), (2, 80)])
CHARS['riggs-fornstrut'] = {
    'body': 'corpulento', 'pal': pal('#3a3e60', '#9a5e3a', iris='#c82a2a', shade='#2a2e48', deep='#1e2034', orange='#e8742a', pale='#e8e0d8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': _riggs_face, 'ear_out': 6},
    'front': [L(outline([(10, 70), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (90, 70), (82, 56), (18, 56)])),
              L(outline([(8, 50), (14, 26), (30, 10), (36, 18), (24, 34), (18, 54)]), 'orange', 'f', False),
              L(outline([(92, 50), (86, 26), (70, 10), (64, 18), (76, 34), (82, 54)]), 'orange', 'f', False),
              L(outline([(10, 54), (20, 40), (50, 30), (80, 40), (90, 54), (80, 50), (50, 46), (20, 50)]), 'mid', 'f'),
              strand([(46, 12), (46, 22)], 'deep', 'f', 1.0), strand([(50, 12), (50, 22)], 'deep', 'f', 1.0), strand([(54, 12), (54, 22)], 'deep', 'f', 1.0),
              L(outline([(22, 66), (34, 58), (46, 62), (44, 68), (32, 66), (24, 70)]), BLACK, 'f', False),
              L(outline([(78, 66), (66, 58), (54, 62), (56, 68), (68, 66), (76, 70)]), BLACK, 'f', False),
              L(outline([(26, 82), (36, 80), (44, 82), (40, 86), (30, 86)]), 'pale', 'f', False),
              L(outline([(74, 82), (64, 80), (56, 82), (60, 86), (70, 86)]), 'pale', 'f', False),
              L([(44, 88), (56, 88)], 'skin_d', 'f', False, False, 1.4)],
    'side': [L(outline([(70, 54), (84, 46), (90, 30), (70, 10), (40, 4), (14, 16), (4, 40), (-10, 70), (-20, 96), (0, 98), (14, 80), (30, 64), (50, 56)])),
             L(outline([(84, 40), (70, 18), (40, 12), (14, 26), (0, 56), (-14, 90), (-6, 94), (8, 64), (20, 40), (44, 26), (70, 30)]), 'orange', 'f', False),
             L(outline([(70, 64), (82, 58), (90, 62), (84, 68)]), BLACK, 'f', False)],
    'back': [L(outline([(10, 70), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (90, 70), (96, 110), (70, 116), (50, 112), (30, 116), (4, 110)])),
             L(outline([(14, 30), (24, 20), (30, 60), (20, 100), (10, 108), (12, 70)]), 'orange', 'f', False),
             L(outline([(86, 30), (76, 20), (70, 60), (80, 100), (90, 108), (88, 70)]), 'orange', 'f', False)],
}

# Sendou Marin (Leticia Legatus, portera): pelo índigo en mechones de punta con un remolino alto arriba, un mechón largo
# que le cruza la cara por en medio y puntas a los lados; dos mechones finos y largos por detrás hasta la espalda; ojos
# gris azulado afilados con la raya marcada
CHARS['leticia-legatus'] = {
    'body': 'chica', 'pal': pal('#2c2c8a', '#fce4d6', iris='#7a8aa0', shade='#20206a', deep='#16164c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 80), (-4, 74, 1), (6, 62), (-2, 46, 1), (8, 40), (6, 18), (22, 2), (36, -2), (40, -22, 1), (52, -8), (70, -18, 1), (66, 0), (84, 10), (94, 30),
                         (106, 44, 1), (94, 50), (104, 66, 1), (90, 72), (86, 80), (82, 62), (18, 62)])),
              L(outline([(66, 0), (84, 10), (94, 30), (106, 44), (94, 50), (104, 66), (90, 66), (84, 40)]), 'shade', 'b', False),
              fr([(14, 72, 1), (10, 46), (20, 26), (42, 14), (62, 16), (80, 26), (90, 46), (86, 72, 1), (78, 56), (68, 50), (58, 54), (52, 92, 1), (48, 56), (40, 48),
                  (28, 54), (22, 66)]),
              strand([(40, 0), (52, 18)], 'deep', 'f', 1.0), strand([(66, 2), (56, 20)], 'deep', 'f', 1.0)],
    'side': [L(rope((14, 40), (-6, 80), (-4, 120), 4), 'mid', 'b'),
             L(outline([(60, 60), (66, 48), (84, 46), (94, 32), (90, 12), (70, -4), (64, -20, 1), (52, -6), (32, -4), (12, 10), (2, 34), (-10, 44, 1), (4, 52), (-6, 70, 1),
                        (10, 72), (24, 84, 1), (34, 70), (46, 62)])),
             L(outline([(4, 40), (28, 44), (32, 70), (12, 72)]), 'shade', 'b', False),
             fr([(66, 8), (90, 20), (96, 46), (94, 70, 1), (86, 56), (78, 42)])],
    'back': [L(rope((36, 60), (30, 96), (34, 126), 4), 'mid', 'b'), L(rope((64, 60), (70, 96), (66, 126), 4), 'mid', 'b'),
             L(outline([(14, 84), (-4, 78, 1), (6, 64), (-2, 48, 1), (8, 40), (6, 18), (22, 2), (36, -2), (40, -22, 1), (52, -8), (70, -18, 1), (66, 0), (84, 10), (94, 30),
                        (106, 46, 1), (94, 52), (104, 70, 1), (90, 76), (86, 86), (70, 92, 1), (60, 82), (50, 94, 1), (40, 82), (30, 92, 1)])),
             L(outline([(56, 0), (84, 10), (98, 44), (90, 80), (64, 84), (70, 40)]), 'shade', 'b', False)],
}

# Kanae Shana (Arran Realis): pelo granate oscuro con un moño redondo arriba del que salen dos mechones curvados como
# cuernos, un flequillo largo partido que le cae sobre los ojos y mechones a los lados que se curvan hacia fuera a la
# altura de la barbilla; ojos grises caídos con ojeras marcadas
CHARS['arran-realis'] = {
    'body': 'normal', 'pal': pal('#7a1424', '#fce4d6', iris='#8a8a9a', shade='#5a0e1a', deep='#420a12', bag='#7a5a5a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(rope((44, -10), (28, -34), (8, -20), 2.6), 'mid', 'b'), L(rope((56, -10), (72, -34), (92, -20), 2.6), 'mid', 'b'),
              L(puff(50, -8, 14, 12, 4, 0.3)),
              L(outline([(14, 74), (8, 40), (18, 12), (40, 0), (60, 0), (82, 12), (92, 40), (86, 74), (82, 60), (18, 60)])),
              L(outline([(60, 2), (82, 14), (92, 44), (86, 70), (80, 44)]), 'shade', 'b', False),
              fr([(14, 80), (10, 46), (20, 24), (42, 12), (60, 12), (80, 24), (90, 46), (86, 80, 1), (80, 66), (74, 76, 1), (70, 58), (60, 54), (56, 80, 1), (52, 54),
                  (48, 54), (44, 80, 1), (40, 54), (30, 58), (26, 76, 1), (20, 66)]),
              L(rope((14, 76), (6, 96), (-6, 98), 2.6), 'mid', 'f'), L(rope((86, 76), (94, 96), (106, 98), 2.6), 'mid', 'f'),
              L(quad((28, 82), (36, 85), (44, 82)), 'bag', 'f', False, False, 1.2), L(quad((56, 82), (64, 85), (72, 82)), 'bag', 'f', False, False, 1.2)],
    'side': [L(rope((32, -12), (20, -36), (2, -26), 2.6), 'mid', 'b'),
             L(puff(38, -6, 14, 12, 4, 0.3)),
             L(outline([(60, 60), (66, 48), (84, 46), (94, 32), (88, 8), (62, -2), (32, 2), (12, 18), (6, 44), (10, 72), (28, 78), (46, 64)])),
             L(outline([(8, 30), (30, 36), (36, 66), (14, 70)]), 'shade', 'b', False),
             fr([(66, 8), (90, 20), (98, 46), (94, 76, 1), (86, 56), (78, 42)]),
             L(rope((62, 70), (60, 92), (48, 100), 2.6), 'mid', 'f')],
    'back': [L(rope((44, -10), (28, -34), (8, -20), 2.6), 'mid', 'b'), L(rope((56, -10), (72, -34), (92, -20), 2.6), 'mid', 'b'),
             L(puff(50, -8, 14, 12, 4, 0.3)),
             L(outline([(14, 80), (8, 40), (18, 12), (40, 0), (60, 0), (82, 12), (92, 40), (86, 80), (50, 86)])),
             L(outline([(56, 2), (82, 14), (92, 44), (86, 76), (60, 60)]), 'shade', 'b', False),
             L(rope((14, 76), (6, 96), (-6, 98), 2.6), 'mid', 'b'), L(rope((86, 76), (94, 96), (106, 98), 2.6), 'mid', 'b')],
}
