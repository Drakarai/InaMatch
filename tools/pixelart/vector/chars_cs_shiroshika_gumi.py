"""Shiroshika-gumi (cs-shiroshika-gumi): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente,
perfil y espalda; sin modelo, su retrato). La banda de Ciervo Blanco de la era Sengoku: moños de samurái, coletas altas,
melenas revueltas, una máscara de calavera de ciervo y caras pintadas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_bigwaves import bald
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Norimaru Gazen (portero): mayor de piel morena con una melena blanca larga peinada hacia atrás que cae ondulada hasta los
# hombros, arrugas en las mejillas y cejas redondas
CHARS['norimaru-gazen'] = {
    'body': 'normal', 'pal': pal('#d8d4d8', '#b88050', iris='#1e1e1e', shade='#a89098', deep='#7a6a70'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 40), (6, 64), (0, 90), (-6, 112, 1), (8, 104), (12, 118, 1), (20, 100), (20, 72), (16, 50), (18, 16), (40, -2), (60, -2), (82, 16), (84, 50),
                         (80, 72), (80, 100), (88, 118, 1), (92, 104), (106, 112, 1), (100, 90), (94, 64), (84, 40)])),
              L(outline([(60, 0), (84, 16), (90, 50), (104, 90), (90, 98), (82, 70)]), 'shade', 'b', False),
              fr([(14, 56), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (86, 56), (80, 40), (62, 28), (50, 34), (38, 28), (20, 40)]),
              strand([(30, 30), (50, 20), (70, 30)], 'deep', 'f', 1.0),
              L(ell(36, 64, 4, 2.4), 'deep', 'f', False), L(ell(64, 64, 4, 2.4), 'deep', 'f', False),
              L([(30, 84), (34, 100)], OUTC, 'f', False, False, 1.0), L([(70, 84), (66, 100)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(60, 50), (80, 44), (92, 24), (74, 0), (40, -4), (14, 10), (0, 40), (-10, 70), (-18, 104, 1), (-2, 92), (0, 114, 1), (14, 96), (30, 110, 1), (40, 90),
                        (46, 70)])),
             L(outline([(-4, 50), (20, 50), (34, 96), (6, 98)]), 'shade', 'b', False),
             strand([(70, 10), (40, 6), (14, 30)], 'deep', 'b', 1.0), strand([(70, 24), (40, 24), (20, 60)], 'deep', 'b', 1.0),
             L([(78, 84), (82, 98)], OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(10, 100), (-10, 112, 1), (-4, 80), (6, 40), (18, 12), (40, -2), (60, -2), (82, 12), (94, 40), (104, 80), (110, 112, 1), (90, 100), (76, 118, 1),
                        (64, 102), (50, 120, 1), (36, 102), (24, 118, 1)])),
             L(outline([(56, 0), (84, 14), (98, 60), (100, 104), (70, 108)]), 'shade', 'b', False),
             strand([(30, 20), (24, 60), (30, 100)], 'deep', 'b', 1.0), strand([(70, 20), (76, 60), (70, 100)], 'deep', 'b', 1.0)],
}

# Sokichi Kitagami: lleva puesta una calavera de ciervo blanca con cuernos ramificados y la nariz y las cuencas negras, con
# una marca roja en la frente; por detrás le cae una tela blanca con lunares
_SKULL = outline([(14, 70), (10, 34), (24, 12), (50, 6), (76, 12), (90, 34), (86, 70), (68, 96), (50, 110), (32, 96)])
CHARS['sokichi-kitagami'] = {
    'body': 'normal', 'pal': pal('#f4eeea', '#fcdcc0', iris='#1e1e1e', bone='#f6f2ee', bone_d='#d8c4c0', red='#d0603a', blk='#1e1414'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(8, 80), (4, 110), (14, 120), (26, 100), (24, 70)]), 'bone_d'), L(outline([(92, 80), (96, 110), (86, 120), (74, 100), (76, 70)]), 'bone_d'),
              L(outline([(30, 14), (22, -8), (14, -30), (8, -46, 1), (18, -32), (20, -40, 1), (24, -24), (34, -6), (40, -24, 1), (40, -4), (40, 12)]), 'bone', 'f', ln=True),
              L(outline([(70, 14), (78, -8), (86, -30), (92, -46, 1), (82, -32), (80, -40, 1), (76, -24), (66, -6), (60, -24, 1), (60, -4), (60, 12)]), 'bone', 'f', ln=True),
              L(outline([(10, 24), (-6, 18, 1), (8, 38)]), 'bone', 'f', ln=True), L(outline([(90, 24), (106, 18, 1), (92, 38)]), 'bone', 'f', ln=True),
              L(_SKULL, 'bone', 'f', ln=True),
              L(outline([(32, 30), (44, 26), (50, 30), (56, 26), (68, 30), (56, 36), (54, 54), (46, 54), (44, 36)]), 'red', 'f', False),
              L(ell(34, 60, 6, 8), 'blk', 'f', False), L(ell(66, 60, 6, 8), 'blk', 'f', False),
              L(outline([(40, 84), (60, 84), (50, 100)]), 'blk', 'f', False), L(ell(26, 92, 4, 4), 'red', 'f', False), L(ell(74, 92, 4, 4), 'red', 'f', False)],
    'side': [L(outline([(34, 60), (10, 80), (2, 116), (24, 120), (40, 90)]), 'bone_d'),
             L(outline([(20, 70), (16, 30), (36, 8), (64, 6), (84, 20), (96, 50), (108, 74), (96, 92), (74, 96), (54, 104), (36, 92)]), 'bone', 'f', ln=True),
             L(outline([(40, 10), (30, -16), (16, -40), (6, -58, 1), (24, -40), (40, -16), (50, 6)]), 'bone', 'f', ln=True),
             L(outline([(64, 30), (88, 34), (80, 48), (66, 44)]), 'red', 'f', False), L(ell(76, 58, 5, 6), 'blk', 'f', False),
             L(outline([(98, 74), (110, 78), (102, 86)]), 'blk', 'f', False)],
    'back': [L(outline([(10, 110), (12, 40), (24, 12), (50, 6), (76, 12), (88, 40), (90, 110), (50, 116)]), 'bone'),
             L(outline([(56, 10), (84, 20), (90, 110), (60, 112)]), 'bone_d', 'b', False),
             L(outline([(30, 14), (22, -8), (14, -30), (8, -46, 1), (18, -32), (20, -40, 1), (24, -24), (34, -6), (40, -24, 1), (40, -4), (40, 12)]), 'bone', 'f', ln=True),
             L(outline([(70, 14), (78, -8), (86, -30), (92, -46, 1), (82, -32), (80, -40, 1), (76, -24), (66, -6), (60, -24, 1), (60, -4), (60, 12)]), 'bone', 'f', ln=True),
             L(outline([(10, 24), (-6, 18, 1), (8, 38)]), 'bone', 'f', ln=True), L(outline([(90, 24), (106, 18, 1), (92, 38)]), 'bone', 'f', ln=True)],
}

# Hoichiro Ashiguro: calvo de piel morena con tres lunares en fila en la frente y un moño negro largo que sale de la
# coronilla y cae por detrás; un pañuelo negro le tapa la boca
CHARS['hoichiro-ashiguro'] = {
    'body': 'corpulento', 'pal': pal('#2a2224', '#c08048', iris='#8a2a4a', cloth='#1e1e22'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'big_ears': 2},
    'front': bald('front') + [L(outline([(44, 8), (42, -24), (50, -30), (58, -24), (56, 8)]), 'mid', 'b', ln=True),
                              L(ell(50, 24, 3, 3), OUTC, 'f', False), L(ell(50, 38, 3, 3), OUTC, 'f', False), L(ell(50, 52, 3, 3), OUTC, 'f', False),
                              L(outline([(12, 88), (30, 84), (50, 90), (70, 84), (88, 88), (90, 116), (50, 124), (10, 116)]), 'cloth', 'f', ln=True)],
    'side': bald('side') + [L(outline([(36, 8), (26, -20), (8, -30), (-10, -20), (-20, 30), (-26, 120, 1), (-12, 40), (-2, -10), (14, -16), (30, -2)]), 'mid', 'b', ln=True),
                            L(outline([(40, 86), (70, 84), (104, 90), (106, 108), (60, 116), (36, 110)]), 'cloth', 'f', ln=True)],
    'back': bald('back') + [L(outline([(42, 6), (40, -24), (50, -30), (60, -24), (58, 6), (56, 100), (50, 112, 1), (44, 100)]), 'mid', 'f', ln=True),
                            L(outline([(10, 92), (50, 100), (90, 92), (90, 112), (10, 112)]), 'cloth', 'f', ln=True)],
}

# Hanbee Yabe: grandullón moreno con un moño de pelo granate erizado en lo alto atado con una cinta, patillas y barba que
# le enmarcan la cara; ojos saltones y una sonrisa con colmillos
CHARS['hanbee-yabe'] = {
    'body': 'corpulento', 'pal': pal('#4a1a2a', '#c87840', iris='#1e1e1e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(16, 76), (8, 60), (0, 52, 1), (8, 40), (14, 22), (30, 12), (50, 10), (70, 12), (86, 22), (92, 40), (100, 52, 1), (92, 60), (84, 76), (80, 50), (20, 50)])),
              L(outline([(30, 14), (22, -8, 1), (34, -4), (30, -26, 1), (44, -12), (50, -34, 1), (56, -12), (70, -26, 1), (66, -4), (78, -8, 1), (70, 14)]), 'mid', 'b'),
              L(outline([(36, 14), (40, 4), (60, 4), (64, 14)]), 'shade', 'b', ln=True),
              L(outline([(14, 64), (18, 96), (34, 112), (50, 106), (66, 112), (82, 96), (86, 64), (80, 92), (66, 100), (50, 96), (34, 100), (20, 92)]), 'mid', 'f')],
    'side': [L(outline([(56, 50), (60, 38), (80, 36), (90, 24), (70, 12), (40, 10), (18, 20), (8, 44), (12, 72), (26, 80), (44, 70)])),
             L(outline([(30, 12), (24, -12, 1), (36, -6), (34, -28, 1), (46, -12), (58, -26, 1), (58, -6), (70, -10, 1), (62, 12)]), 'mid', 'b'),
             L(outline([(52, 64), (60, 100), (76, 110), (92, 104), (80, 98), (64, 92), (60, 70)]), 'mid', 'f')],
    'back': [L(outline([(16, 84), (8, 60), (0, 52, 1), (8, 40), (14, 22), (30, 12), (50, 10), (70, 12), (86, 22), (92, 40), (100, 52, 1), (92, 60), (84, 84), (50, 92)])),
             L(outline([(30, 14), (22, -8, 1), (34, -4), (30, -26, 1), (44, -12), (50, -34, 1), (56, -12), (70, -26, 1), (66, -4), (78, -8, 1), (70, 14)]), 'mid', 'f'),
             L(outline([(36, 14), (40, 4), (60, 4), (64, 14)]), 'shade', 'f', ln=True)],
}

# Ikkatsu Kano (sin modelo 3D: su retrato): pelo verde oliva revuelto de mechones de punta hacia atrás, una hachimaki blanca
# trenzada en la frente y perilla
CHARS['ikkatsu-kano'] = {
    'body': 'normal', 'pal': pal('#8a9a50', '#f0c890', iris='#1e1e1e', band='#f4f0e8', band_d='#c8c0b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 74), (2, 80, 1), (8, 60), (-6, 50, 1), (6, 40), (4, 18, 1), (22, 18), (24, -4, 1), (40, 6), (50, -12, 1), (60, 6), (78, -4, 1), (78, 18),
                         (98, 16, 1), (92, 40), (108, 54, 1), (94, 60), (102, 84, 1), (84, 74), (82, 50), (18, 50)])),
              L(outline([(60, 6), (84, 18), (98, 54), (90, 74), (80, 44)]), 'shade', 'b', False),
              fr([(14, 60), (16, 46), (30, 42), (40, 52, 1), (44, 42), (56, 42), (60, 54, 1), (66, 42), (84, 46), (86, 60), (80, 52), (20, 52)]),
              L(outline([(10, 46), (10, 30), (50, 24), (90, 30), (90, 46), (50, 40)]), 'band', 'f', ln=True),
              strand([(20, 34), (30, 42)], 'band_d', 'f', 1.2), strand([(40, 30), (50, 40)], 'band_d', 'f', 1.2), strand([(60, 30), (70, 40)], 'band_d', 'f', 1.2),
              L(outline([(46, 104), (54, 104), (50, 114)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(58, 52), (68, 40), (88, 36), (92, 20), (80, 4), (90, -10, 1), (62, -2), (48, -16, 1), (36, 0), (8, -8, 1), (14, 14), (-14, 22, 1), (4, 34), (-14, 50, 1),
                        (6, 56), (-4, 76, 1), (16, 74), (26, 90, 1), (36, 76), (48, 66)])),
             L(outline([(4, 26), (6, 12), (50, 8), (94, 16), (94, 32), (50, 26)]), 'band', 'f', ln=True),
             L(outline([(6, 28), (-8, 40), (-6, 54), (4, 40)]), 'band', 'f', ln=True)],
    'back': [L(outline([(16, 84), (0, 92, 1), (8, 66), (-8, 54, 1), (6, 44), (2, 18, 1), (22, 18), (24, -4, 1), (40, 6), (50, -12, 1), (60, 6), (78, -4, 1), (78, 18),
                        (98, 18, 1), (94, 44), (108, 54, 1), (92, 66), (100, 92, 1), (84, 84), (66, 96, 1), (58, 86), (42, 96, 1), (34, 86)])),
             L(outline([(56, 6), (84, 18), (94, 50), (86, 82), (62, 90)]), 'shade', 'b', False),
             L(outline([(10, 46), (10, 30), (50, 26), (90, 30), (90, 46), (50, 42)]), 'band', 'f', ln=True),
             L(outline([(44, 40), (36, 58), (44, 70), (50, 56), (56, 70), (64, 58), (56, 40)]), 'band', 'f', ln=True)],
}

# Denbee Asama: pelo azul morado liso hasta la mandíbula con el nacimiento en pico en la frente y un moño alto atado con
# cinta clara; dos coletas finas atadas detrás de las orejas; ojos cerrados de sonrisa con maquillaje rosa de kabuki
CHARS['denbee-asama'] = {
    'body': 'delgado', 'pal': pal('#3a2a8a', '#f0d4b0', iris='#1e1e1e', tie='#e8c8c0', paint='#e8607a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(44, 4), (40, -20), (50, -28), (60, -20), (56, 4)]), 'mid', 'b', ln=True),
              L(outline([(42, 0), (58, 0), (58, 6), (42, 6)]), 'tie', 'b', ln=True),
              L(outline([(16, 104), (12, 60), (14, 22), (30, 4), (50, 0), (70, 4), (86, 22), (88, 60), (84, 104), (78, 104), (76, 60), (24, 60), (22, 104)])),
              fr([(14, 60), (16, 30), (30, 12), (50, 8), (70, 12), (84, 30), (86, 60), (76, 42), (62, 36), (50, 52, 1), (38, 36), (24, 42)]),
              L(outline([(26, 72), (40, 66), (42, 74), (30, 78)]), 'paint', 'f', False), L(outline([(74, 72), (60, 66), (58, 74), (70, 78)]), 'paint', 'f', False)],
    'side': [L(outline([(42, 4), (34, -18), (40, -28), (50, -22), (50, 2)]), 'mid', 'b', ln=True),
             L(outline([(54, 50), (60, 38), (80, 36), (90, 20), (72, 2), (44, 0), (20, 10), (8, 36), (10, 70), (24, 80), (40, 70)])),
             L(outline([(70, 10), (90, 24), (94, 50), (90, 104), (84, 104), (84, 50), (74, 30)]), 'mid', 'f'),
             L(outline([(24, 76), (12, 96), (6, 112), (20, 110), (30, 94)]), 'mid', 'b', ln=True), L(outline([(20, 80), (30, 82), (28, 92), (18, 90)]), 'tie', 'b', ln=True),
             L(outline([(76, 72), (90, 70), (88, 78)]), 'paint', 'f', False)],
    'back': [L(outline([(42, 6), (40, -20), (50, -28), (60, -20), (58, 6)]), 'mid', 'f', ln=True), L(outline([(42, 2), (58, 2), (58, 8), (42, 8)]), 'tie', 'f', ln=True),
             L(outline([(14, 80), (10, 40), (22, 12), (50, 4), (78, 12), (90, 40), (86, 80), (70, 92), (50, 84), (30, 92)])),
             L(outline([(56, 6), (84, 18), (90, 50), (84, 80), (66, 90)]), 'shade', 'b', False),
             L(outline([(20, 84), (12, 104), (6, 118), (20, 114), (28, 98)]), 'mid', 'f', ln=True), L(outline([(80, 84), (88, 104), (94, 118), (80, 114), (72, 98)]), 'mid', 'f', ln=True),
             L(outline([(16, 86), (28, 88), (26, 96), (14, 94)]), 'tie', 'f', ln=True), L(outline([(84, 86), (72, 88), (74, 96), (86, 94)]), 'tie', 'f', ln=True)],
}

# Ginji Santetsu: pelo verde oliva oscuro de pinchos enormes en todas direcciones sobre una nuca rapada oscura; ojos
# afilados, sonrisa abierta con colmillos y perilla
CHARS['ginji-santetsu'] = {
    'body': 'delgado', 'pal': pal('#7a6a1a', '#fcdcb8', iris='#1e1e1e', buzz='#3a2a24'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (12, 50), (88, 50), (84, 66), (80, 56), (20, 56)]), 'buzz'),
              L(outline([(14, 54), (-14, 54, 1), (6, 40), (-16, 22, 1), (10, 24), (6, 0, 1), (26, 10), (28, -18, 1), (42, 0), (52, -24, 1), (60, 0), (76, -16, 1), (76, 10),
                         (96, 0, 1), (90, 24), (116, 22, 1), (94, 40), (114, 54, 1), (86, 54), (80, 46), (66, 44), (56, 54, 1), (50, 44), (42, 54, 1), (34, 44), (20, 46)]), 'mid', 'f'),
              L(outline([(56, 4), (74, 10), (90, 28), (76, 30)]), 'shade', 'f', False),
              L(outline([(46, 108), (54, 108), (50, 118)]), 'buzz', 'f', ln=True)],
    'side': [L(outline([(52, 62), (54, 46), (24, 44), (8, 60), (16, 82), (34, 88), (46, 76)]), 'buzz'),
             L(outline([(70, 46), (90, 40), (96, 20), (84, 6), (100, -4, 1), (70, -2), (66, -24, 1), (50, -6), (26, -20, 1), (24, 0), (-6, -4, 1), (8, 16), (-18, 28, 1), (4, 36),
                        (-14, 52, 1), (14, 48), (40, 46)]), 'mid', 'f')],
    'back': [L(outline([(16, 46), (14, 80), (30, 96), (50, 102), (70, 96), (86, 80), (84, 46)]), 'buzz'),
             L(outline([(12, 56), (-14, 56, 1), (6, 40), (-16, 20, 1), (10, 22), (6, -2, 1), (26, 8), (28, -20, 1), (42, -2), (52, -24, 1), (60, -2), (76, -18, 1), (76, 8),
                        (96, -2, 1), (90, 22), (116, 20, 1), (94, 40), (114, 56, 1), (88, 56), (78, 66, 1), (68, 54), (50, 64, 1), (34, 54), (22, 66, 1)]), 'mid', 'f'),
             L(outline([(56, 2), (76, 8), (92, 26), (88, 50), (70, 40)]), 'shade', 'f', False)],
}

# Denrai Ochimura: calvo de piel morena con un pelo granate de llamas que le sale a los lados de la cabeza como dos cuernos
# curvos hacia arriba, cejas pintadas en espiral, un lunar en la frente y un bigote enorme que le baja por la barbilla
CHARS['denrai-ochimura'] = {
    'body': 'corpulento', 'pal': pal('#9a1a1e', '#d89a60', iris='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 2},
    'front': bald('front') + [L(outline([(14, 70), (-10, 64, 1), (6, 50), (-6, 36, 1), (10, 30), (2, -6), (-6, -28, 1), (14, -10), (26, 20), (20, 50)])),
                              L(outline([(86, 70), (110, 64, 1), (94, 50), (106, 36, 1), (90, 30), (98, -6), (106, -28, 1), (86, -10), (74, 20), (80, 50)])),
                              L(outline([(26, 66), (34, 60), (44, 66)]) + [(44, 66)], OUTC, 'f', False, False, 2.4),
                              L(outline([(74, 66), (66, 60), (56, 66)]) + [(56, 66)], OUTC, 'f', False, False, 2.4),
                              L(ell(50, 50, 4, 4), 'skin_d', 'f', ln=True),
                              L(outline([(18, 96), (34, 86), (50, 92), (66, 86), (82, 96), (66, 100), (60, 118, 1), (50, 104), (40, 118, 1), (34, 100)]), 'mid', 'f', ln=True)],
    'side': bald('side') + [L(outline([(48, 70), (24, 74, 1), (30, 56), (10, 50, 1), (28, 40), (24, 12), (34, -12, 1), (40, 16), (52, 50)])),
                            L(outline([(28, 40), (6, 46), (-8, 70, 1), (6, 66), (10, 86, 1), (22, 70), (36, 66)])),
                            L(outline([(78, 96), (96, 90), (94, 104), (84, 116, 1), (80, 102)]), 'mid', 'f', ln=True)],
    'back': bald('back') + [L(outline([(6, 100), (-14, 108, 1), (-2, 86), (-20, 70, 1), (0, 64), (-6, 40, 1), (12, 40), (2, -6), (-6, -28, 1), (14, -10), (30, 30), (50, 40),
                                       (70, 30), (86, -10), (106, -28, 1), (98, -6), (88, 40), (106, 40, 1), (100, 64), (120, 70, 1), (102, 86), (114, 108, 1), (94, 100),
                                       (76, 112, 1), (64, 100), (50, 114, 1), (36, 100), (24, 112, 1)]))],
}

# Senji Kudo: pelo castaño muy oscuro pegado a la cabeza con dos rayas claras afeitadas y dos mechones enormes atados con
# anillas doradas que salen hacia arriba a los lados como orejas
CHARS['senji-kudo'] = {
    'body': 'bajito', 'pal': pal('#2e2020', '#fcdcb4', iris='#1e1e1e', gold='#e0b030', gold_d='#a87a1a', line='#f0c8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (60, 42)},
    'front': [L(outline([(16, 66), (12, 40), (22, 14), (50, 4), (78, 14), (88, 40), (84, 66), (80, 54), (20, 54)])),
              L(outline([(16, 30), (-4, 4), (-2, -24), (14, -12), (28, 20)])), L(outline([(84, 30), (104, 4), (102, -24), (86, -12), (72, 20)])),
              L(outline([(10, 26), (22, 18), (30, 32), (18, 40)]), 'gold', 'f', ln=True), L(outline([(90, 26), (78, 18), (70, 32), (82, 40)]), 'gold', 'f', ln=True),
              strand([(36, 8), (36, 44)], 'line', 'b', 2.0), strand([(64, 8), (64, 44)], 'line', 'b', 2.0)],
    'side': [L(outline([(54, 54), (58, 44), (80, 42), (90, 26), (76, 6), (46, 2), (20, 12), (8, 38), (10, 64), (24, 80), (42, 74)])),
             L(outline([(40, 10), (24, -24), (40, -40), (60, -26), (56, 6)])),
             L(outline([(36, 6), (50, 0), (56, 14), (40, 18)]), 'gold', 'f', ln=True), strand([(70, 6), (80, 20), (82, 40)], 'line', 'f', 2.0)],
    'back': [L(outline([(16, 84), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 84), (50, 92)])),
             L(outline([(20, 30), (-6, 0), (-8, -30), (12, -14), (30, 18)])), L(outline([(80, 30), (106, 0), (108, -30), (88, -14), (70, 18)])),
             L(outline([(14, 22), (28, 14), (34, 30), (20, 36)]), 'gold', 'f', ln=True), L(outline([(86, 22), (72, 14), (66, 30), (80, 36)]), 'gold', 'f', ln=True),
             strand([(36, 10), (34, 86)], 'line', 'b', 2.0), strand([(64, 10), (66, 86)], 'line', 'b', 2.0)],
}

# Taian Inaba: piel morena, melena azul petróleo ondulada y revuelta que le tapa un ojo y le abulta a los lados, con barba
# fina por la mandíbula
CHARS['taian-inaba'] = {
    'body': 'normal', 'pal': pal('#1e4a68', '#b07848', iris='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 90), (-4, 84, 1), (4, 70), (-10, 60, 1), (2, 48), (-6, 30, 1), (10, 20), (24, 4), (50, -4), (76, 4), (90, 20), (106, 30, 1), (98, 48), (110, 60, 1),
                         (96, 70), (104, 84, 1), (84, 90), (82, 60), (18, 60)])),
              L(outline([(60, 0), (86, 14), (100, 44), (94, 80), (80, 50)]), 'shade', 'b', False),
              fr([(12, 76), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (88, 64), (80, 50), (68, 48), (56, 54), (50, 46), (40, 60), (34, 84, 1), (26, 66), (18, 80)]),
              L(outline([(18, 90), (26, 106), (50, 116), (74, 106), (82, 90), (70, 100), (50, 108), (30, 100)]), 'mid', 'f')],
    'side': [L(outline([(56, 60), (62, 48), (84, 48), (94, 30), (84, 8), (60, -4), (30, -2), (8, 14), (-12, 30, 1), (0, 42), (-14, 60, 1), (2, 66), (-8, 84, 1), (12, 82), (14, 100, 1),
                        (30, 86), (46, 80)])),
             L(outline([(70, 6), (92, 24), (96, 50), (92, 70, 1), (84, 52), (76, 40)]), 'mid', 'f'),
             L(outline([(58, 90), (66, 108), (80, 110), (92, 104), (76, 100)]), 'mid', 'f')],
    'back': [L(outline([(18, 96), (0, 92, 1), (6, 74), (-12, 62, 1), (2, 50), (-6, 30, 1), (10, 20), (24, 4), (50, -4), (76, 4), (90, 20), (106, 30, 1), (98, 50), (112, 62, 1),
                        (94, 74), (100, 92, 1), (82, 96), (66, 92, 1), (58, 84), (50, 94, 1), (42, 84), (34, 92, 1)])),
             L(outline([(56, 0), (86, 14), (100, 50), (92, 88), (66, 90)]), 'shade', 'b', False)],
}

# Korin Maebayashi: pelo castaño recogido en una coleta altísima con una goma azul, flequillo de lado, dos mechones cortos
# junto a las orejas y un parche negro en el ojo derecho; ojo azul y media sonrisa
CHARS['korin-maebayashi'] = {
    'body': 'normal', 'pal': pal('#6a3a24', '#fce0c0', iris='#2a8ad0', band='#1e3a6a', patch='#1e1e22'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(36, 6), (32, -26), (50, -40), (68, -26), (64, 6)]), 'mid', 'b', ln=True), L(outline([(38, 0), (62, 0), (62, 8), (38, 8)]), 'band', 'b', ln=True),
              L(outline([(16, 70), (12, 40), (22, 14), (50, 4), (78, 14), (88, 40), (84, 70), (80, 56), (20, 56)])),
              L(outline([(14, 66), (8, 90), (14, 98, 1), (22, 84), (22, 66)]), 'mid', 'f'), L(outline([(86, 66), (92, 90), (86, 98, 1), (78, 84), (78, 66)]), 'mid', 'f'),
              fr([(12, 62), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (88, 56), (76, 40), (58, 36), (44, 46), (30, 58, 1), (24, 48)]),
              L(outline([(22, 66), (44, 64), (44, 82), (32, 86), (22, 78)]), 'patch', 'f', ln=True), L([(14, 60), (86, 50)], 'patch', 'f', False, False, 1.4)],
    'side': [L(outline([(54, 60), (58, 46), (80, 44), (92, 30), (82, 8), (56, -2), (28, 2), (10, 18), (6, 46), (12, 70), (26, 80), (44, 74)])),
             L(outline([(26, 4), (6, -30), (-8, -40), (-26, -20), (-18, 30), (-28, 80, 1), (-6, 40), (-6, -10), (8, -16), (20, 8)]), 'mid', 'b', ln=True),
             L(outline([(16, -8), (26, -16), (32, -4), (22, 2)]), 'band', 'b', ln=True),
             L([(50, 60), (94, 70)], 'patch', 'f', False, False, 1.4)],
    'back': [L(outline([(16, 84), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 84), (50, 92)])),
             L(outline([(56, 6), (84, 18), (92, 50), (84, 80), (62, 88)]), 'shade', 'b', False),
             L(outline([(36, 4), (32, -26), (50, -40), (68, -26), (64, 4), (62, 50), (50, 66, 1), (38, 50)]), 'mid', 'f', ln=True),
             L(outline([(38, 0), (62, 0), (62, 8), (38, 8)]), 'band', 'f', ln=True), L([(10, 60), (90, 60)], 'patch', 'f', False, False, 1.4)],
}

# Mikimaru Ujiki (portero): pelo gris claro corto y de punta encima de una cinta gris oscura ancha atada a la cabeza, la
# nuca negra; orejas grandes, ojos de sueño y boca abierta
CHARS['mikimaru-ujiki'] = {
    'body': 'normal', 'pal': pal('#c8c4c0', '#fcdcb0', iris='#1e1e1e', band='#4a4a52', band_d='#2e2e34', nape='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(14, 40), (10, 26), (-2, 22, 1), (12, 14), (8, -2, 1), (26, 4), (34, -10, 1), (44, 2), (56, -12, 1), (62, 2), (78, -6, 1), (78, 8), (100, 10, 1), (88, 22),
                         (90, 40)])),
              L(outline([(10, 54), (10, 30), (50, 24), (90, 30), (90, 54), (50, 50)]), 'band', 'f', ln=True),
              L(outline([(56, 28), (90, 32), (90, 52), (60, 50)]), 'band_d', 'f', False)],
    'side': [L(outline([(12, 70), (8, 40), (20, 26), (50, 28), (54, 44), (40, 70), (26, 86)]), 'nape'),
             L(outline([(14, 34), (2, 20), (-12, 22, 1), (4, 8), (0, -6, 1), (20, 0), (30, -14, 1), (40, -2), (56, -12, 1), (64, 0), (80, -4, 1), (82, 10), (96, 14, 1), (86, 30)])),
             L(outline([(6, 52), (6, 28), (50, 22), (94, 30), (94, 50), (50, 46)]), 'band', 'f', ln=True)],
    'back': [L(outline([(14, 50), (12, 80), (30, 96), (70, 96), (88, 80), (86, 50)]), 'nape'),
             L(outline([(14, 40), (10, 26), (-2, 22, 1), (12, 14), (8, -2, 1), (26, 4), (34, -10, 1), (44, 2), (56, -12, 1), (62, 2), (78, -6, 1), (78, 8), (100, 10, 1), (88, 22),
                        (90, 40)])),
             L(outline([(10, 56), (10, 32), (50, 26), (90, 32), (90, 56), (50, 52)]), 'band', 'f', ln=True)],
}

# Doshin Yomoyama: piel morena, melena castaño muy oscuro enorme y erizada, de puntas por todos lados, que le tapa la frente
# y le enmarca la cara; cejas pintadas en curva y ojos rojos
CHARS['doshin-yomoyama'] = {
    'body': 'corpulento', 'pal': pal('#2e2422', '#b88050', iris='#c81e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(20, 100), (-6, 104, 1), (6, 84), (-16, 74, 1), (2, 60), (-14, 46, 1), (4, 36), (-4, 14, 1), (14, 10), (16, -14, 1), (32, -6), (40, -28, 1), (52, -10),
                         (64, -28, 1), (70, -6), (88, -14, 1), (86, 10), (104, 14, 1), (96, 36), (114, 46, 1), (98, 60), (116, 74, 1), (94, 84), (106, 104, 1), (80, 100),
                         (80, 60), (20, 60)])),
              L(outline([(60, -4), (86, 10), (104, 46), (96, 90), (80, 54)]), 'shade', 'b', False),
              fr([(18, 96), (16, 70), (20, 44), (34, 30), (50, 26), (66, 30), (80, 44), (84, 70), (82, 96), (76, 80), (74, 58), (62, 56), (56, 62, 1), (50, 54), (44, 62, 1),
                  (38, 56), (26, 58), (24, 80)])],
    'side': [L(outline([(58, 56), (66, 44), (84, 44), (96, 28), (88, 6), (102, -6, 1), (72, -8), (62, -30, 1), (46, -12), (22, -24, 1), (20, 0), (-6, -6, 1), (4, 18), (-18, 30, 1),
                        (-2, 42), (-16, 60, 1), (0, 64), (-10, 84, 1), (12, 80), (12, 100, 1), (28, 84), (40, 94, 1), (44, 74)])),
             L(outline([(74, 4), (94, 24), (96, 48), (92, 70, 1), (84, 52), (76, 40)]), 'mid', 'f')],
    'back': [L(outline([(20, 100), (-6, 104, 1), (6, 84), (-16, 74, 1), (2, 60), (-14, 46, 1), (4, 36), (-4, 14, 1), (14, 10), (16, -14, 1), (32, -6), (40, -28, 1), (52, -10),
                        (64, -28, 1), (70, -6), (88, -14, 1), (86, 10), (104, 14, 1), (96, 36), (114, 46, 1), (98, 60), (116, 74, 1), (94, 84), (106, 104, 1), (80, 100), (64, 92),
                        (58, 104, 1), (50, 92), (42, 104, 1), (36, 92)])),
             L(outline([(56, -4), (86, 10), (104, 46), (98, 96), (70, 96)]), 'shade', 'b', False)],
}

# Tenkei Yazu (sin modelo 3D: su retrato): melena gris azulada lisa y larga con la raya a un lado, que le tapa un ojo y le
# cae en mechones largos hasta los hombros
CHARS['tenkei-yazu'] = {
    'body': 'delgado', 'pal': pal('#5a6a72', '#fce0c0', iris='#c8a01e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 104), (6, 70), (4, 30), (20, 6), (50, -4), (80, 6), (96, 30), (96, 70), (90, 110, 1), (82, 90), (80, 60), (20, 60), (24, 96)])),
              L(outline([(60, 0), (86, 14), (96, 46), (90, 100), (80, 56)]), 'shade', 'b', False),
              fr([(12, 80), (12, 36), (26, 14), (50, 6), (74, 14), (88, 36), (88, 60), (78, 44), (60, 34), (46, 50), (40, 92, 1), (30, 66), (20, 96, 1)])],
    'side': [L(outline([(56, 60), (62, 46), (82, 44), (94, 28), (82, 6), (54, -4), (26, 0), (8, 18), (0, 50), (2, 90), (-4, 110, 1), (14, 96), (26, 108, 1), (36, 86), (46, 74)])),
             L(outline([(66, 4), (90, 20), (96, 48), (94, 96, 1), (86, 70), (82, 46), (72, 30)]), 'mid', 'f')],
    'back': [L(outline([(10, 104), (4, 60), (6, 26), (22, 6), (50, -4), (78, 6), (94, 26), (96, 60), (90, 104), (76, 114, 1), (66, 100), (50, 112, 1), (36, 100), (24, 114, 1)])),
             L(outline([(56, 0), (84, 14), (96, 50), (90, 104), (66, 104)]), 'shade', 'b', False)],
}

# Hokuro Ayabe: melena gris oscura revuelta y enorme de mechones que se curvan hacia fuera como garras a los lados, un
# mechón entre los ojos, ojeras y una sonrisa de dientes de tiburón
CHARS['hokuro-ayabe'] = {
    'body': 'delgado', 'pal': pal('#4a4a56', '#f6dcc0', iris='#1e1e1e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 86), (2, 98), (-10, 112, 1), (-4, 92), (-20, 84), (-30, 64, 1), (-12, 70), (-6, 54), (-20, 40, 1), (-4, 42), (2, 22), (20, 4), (50, -6), (80, 4), (98, 22),
                         (104, 42), (120, 40, 1), (106, 54), (112, 70), (130, 64, 1), (120, 84), (104, 92), (110, 112, 1), (98, 98), (84, 86), (80, 60), (20, 60)])),
              L(outline([(60, -2), (86, 12), (104, 48), (100, 84), (82, 50)]), 'shade', 'b', False),
              fr([(14, 72), (12, 36), (26, 14), (50, 6), (74, 14), (88, 36), (88, 72), (80, 54), (70, 52), (58, 60), (52, 48), (46, 84, 1), (40, 52), (30, 50), (22, 60)])],
    'side': [L(outline([(58, 60), (64, 46), (84, 44), (96, 28), (84, 6), (56, -4), (26, 0), (6, 18), (-16, 22), (-30, 10, 1), (-18, 34), (-34, 48), (-46, 40, 1), (-32, 62), (-12, 74),
                        (-20, 90, 1), (4, 82), (20, 92), (40, 80)])),
             L(outline([(68, 4), (92, 22), (96, 50), (90, 68, 1), (84, 50), (74, 38)]), 'mid', 'f')],
    'back': [L(outline([(16, 90), (2, 98), (-10, 112, 1), (-4, 92), (-20, 84), (-30, 64, 1), (-12, 70), (-6, 54), (-20, 40, 1), (-4, 42), (2, 22), (20, 4), (50, -6), (80, 4), (98, 22),
                        (104, 42), (120, 40, 1), (106, 54), (112, 70), (130, 64, 1), (120, 84), (104, 92), (110, 112, 1), (98, 98), (84, 90), (66, 98, 1), (50, 88), (34, 98, 1)])),
             L(outline([(56, -2), (86, 12), (104, 48), (100, 92), (70, 92)]), 'shade', 'b', False)],
}

# Kaburo Hayama (sin modelo 3D: su retrato): pelo castaño muy oscuro recogido en una coleta altísima que sale de la coronilla
# y cae hacia un lado, con mechones largos que le enmarcan la cara; ceño fruncido
CHARS['kaburo-hayama'] = {
    'body': 'normal', 'pal': pal('#3a2a2e', '#fce0c0', iris='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(44, 4), (46, -24), (62, -36), (82, -24), (100, 20), (106, 80), (96, 104, 1), (92, 60), (84, 20), (64, 2)])),
              L(outline([(16, 76), (12, 40), (22, 14), (50, 4), (78, 14), (88, 40), (84, 76), (80, 56), (20, 56)])),
              L(outline([(14, 60), (8, 92), (14, 104, 1), (22, 84), (22, 62)]), 'mid', 'f'), L(outline([(86, 60), (92, 92), (86, 104, 1), (78, 84), (78, 62)]), 'mid', 'f'),
              fr([(12, 62), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (88, 60), (78, 44), (66, 38), (56, 50, 1), (50, 38), (42, 48, 1), (34, 38), (22, 46)])],
    'side': [L(outline([(54, 60), (58, 46), (80, 44), (92, 30), (82, 8), (56, -2), (28, 2), (10, 18), (6, 46), (12, 70), (26, 80), (44, 74)])),
             L(outline([(40, 2), (34, -26), (16, -40), (-6, -30), (-20, 10), (-28, 100, 1), (-10, 30), (2, -16), (20, -20), (30, 4)]), 'mid', 'b', ln=True),
             L(outline([(64, 10), (88, 22), (94, 46), (92, 84, 1), (84, 56), (76, 36)]), 'mid', 'f')],
    'back': [L(outline([(16, 84), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 84), (50, 92)])),
             L(outline([(56, 6), (84, 18), (92, 50), (84, 80), (62, 88)]), 'shade', 'b', False),
             L(outline([(42, 4), (42, -26), (56, -38), (76, -30), (92, 10), (100, 90), (90, 108, 1), (84, 50), (74, 0), (60, 4)]), 'mid', 'f', ln=True)],
}
