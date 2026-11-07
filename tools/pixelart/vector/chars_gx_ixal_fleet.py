"""Flota Ixar (gx-ixal-fleet): sus modelos 3D de Inazuma Eleven GO Galaxy como referencia (busto de frente, perfil y espalda).

Los ixarianos: piel blanquísima, orejas puntiagudas y pelo azul o gris en formas raras (aletas, cuernos, trenzas de
eslabones). Varios llevan pintura negra en la cara (Deimos, Dione) y el capitán, Ozrock, un tocado turquesa con antenas.
"""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from chars_gx_faram_dite import elf_ears
from heads import quad

WHITE_SKIN = '#f4f2f4'


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def clown(view):
    """Pintura negra en la cara (Deimos, Dione): cejas en ángulo marcadas y rayas bajo los ojos hasta la mandíbula."""
    if view == 'front':
        return [L([(22, 66), (40, 74)], OUTC, 'f', False, False, 3.0), L([(78, 66), (60, 74)], OUTC, 'f', False, False, 3.0),
                L([(34, 82), (30, 100)], OUTC, 'f', False, False, 2.2), L([(66, 82), (70, 100)], OUTC, 'f', False, False, 2.2),
                L(quad((44, 76), (50, 70), (56, 76)), OUTC, 'f', False, False, 1.6)]
    return [L([(70, 68), (86, 74)], OUTC, 'f', False, False, 3.0), L([(80, 82), (78, 98)], OUTC, 'f', False, False, 2.2)]


# Phobos Quasar (portero): melena blanca con reflejos lila, enorme y revuelta, de mechones que se abren hacia los lados y
# por detrás; dos puntos en la frente y ojos rojos
CHARS['phobos'] = {
    'body': 'normal', 'pal': pal('#eceef4', WHITE_SKIN, iris='#c81e1e', shade='#b8a8b8', deep='#8a7a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(12, 100), (-24, 102, 1), (-4, 84), (-26, 70, 1), (-2, 62), (-14, 40, 1), (6, 34), (2, 10, 1), (20, 14), (24, -10, 1), (36, 4), (44, -28, 1),
                         (54, -2), (66, -18, 1), (70, 4), (88, -6, 1), (86, 14), (108, 20, 1), (96, 36), (114, 48, 1), (98, 60), (126, 72, 1), (104, 84), (124, 102, 1),
                         (88, 100), (84, 66), (16, 66)])),
              L(outline([(58, 0), (88, 10), (100, 44), (112, 96), (88, 92), (80, 50)]), 'shade', 'b', False),
              strand([(20, 40), (4, 80)], 'shade', 'b', 1.2), strand([(80, 40), (98, 80)], 'shade', 'b', 1.2)]
             + elf_ears('front', (-8, 58))
             + [fringe([(12, 70), (14, 42), (28, 22), (50, 16), (72, 22), (86, 42), (88, 70), (80, 58), (74, 68, 1), (66, 48), (58, 60, 1), (54, 42), (50, 56, 1), (46, 42),
                        (40, 60, 1), (32, 48), (24, 66, 1), (18, 58)]),
                L(outline([(28, 22), (46, 16), (40, 30)]), 'light', 'f', False),
                L(ell(44, 58, 1.6, 1.6), OUTC, 'f', False), L(ell(56, 58, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(54, 64), (60, 50), (80, 48), (94, 34), (92, 12), (100, -6, 1), (76, 0), (66, -24, 1), (52, -4), (30, -20, 1), (24, 4), (-6, 0, 1), (8, 20), (-20, 30, 1),
                        (2, 42), (-22, 60, 1), (2, 66), (-14, 92, 1), (10, 86), (8, 108, 1), (24, 94), (34, 106, 1), (40, 88), (48, 76)])),
             L(outline([(0, 40), (24, 46), (28, 90), (4, 88)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (96, 42), (94, 68, 1), (86, 52), (80, 62, 1), (76, 42), (66, 30)])] + elf_ears('side', stip=(26, 52)),
    'back': elf_ears('back', (-8, 58))
            + [L(outline([(10, 104), (-24, 104, 1), (-6, 86), (-28, 70, 1), (-4, 60), (-16, 40, 1), (4, 32), (0, 8, 1), (20, 12), (24, -12, 1), (36, 2), (44, -30, 1), (54, -4),
                          (66, -20, 1), (72, 2), (90, -8, 1), (88, 12), (110, 18, 1), (98, 34), (116, 46, 1), (100, 60), (128, 70, 1), (106, 86), (126, 104, 1), (90, 104),
                          (70, 116, 1), (56, 100), (40, 116, 1), (26, 100)]), 'shade'),
               L(outline([(20, 12), (24, -12, 1), (36, 2), (44, -30, 1), (54, -4), (66, -20, 1), (72, 2), (90, -8, 1), (88, 20), (60, 40), (40, 40), (10, 24)]), 'mid', 'b', False)],
}

# Aegir Cepheid: pelo azul en casco con una aleta en lo alto, dos mechones finos que salen disparados a los lados como bigotes
# a la altura de los ojos y los lados que bajan en punta hasta la mandíbula; dos puntos en la frente y ojos amarillos
CHARS['aegir-cepheid'] = {
    'body': 'normal', 'pal': pal('#6a96d0', WHITE_SKIN, iris='#a89a20', shade='#4a5a7e', deep='#3a4462'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 106), (8, 80), (8, 54), (-28, 72, 1), (6, 40), (12, 18), (32, 4), (50, 0), (68, 4), (88, 18), (94, 40), (128, 72, 1), (92, 54), (92, 80),
                         (84, 106), (80, 66), (20, 66)])),
              L(outline([(60, 4), (86, 16), (94, 40), (88, 100), (80, 60)]), 'shade', 'b', False)]
             + elf_ears('front', (-10, 62))
             + [fringe([(12, 66), (12, 42), (26, 22), (50, 14), (74, 22), (88, 42), (88, 66), (78, 52), (66, 46), (56, 52), (50, 64, 1), (44, 52), (34, 46), (22, 52)]),
                L([(50, 4), (50, 18)], 'deep', 'f', False, False, 1.4),
                L(ell(44, 64, 1.6, 1.6), OUTC, 'f', False), L(ell(56, 64, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(52, 68), (58, 52), (78, 50), (92, 38), (90, 14), (74, 0), (46, -6), (20, 0), (4, 16), (-6, 40), (2, 64), (16, 80), (32, 82), (44, 76)])),
             L(outline([(-6, 40), (20, 44), (26, 76), (4, 70)]), 'shade', 'b', False),
             L(outline([(70, 30), (90, 40), (96, 90, 1), (84, 64), (76, 44)]), 'mid', 'f', ln=True),
             fringe([(64, 4), (90, 18), (94, 40), (90, 52, 1), (82, 40), (72, 30)])] + elf_ears('side', stip=(24, 54)),
    'back': elf_ears('back', (-10, 62))
            + [L(outline([(16, 96), (8, 70), (8, 54), (-28, 72, 1), (6, 40), (12, 18), (32, 4), (50, 0), (68, 4), (88, 18), (94, 40), (128, 72, 1), (92, 54), (92, 70), (84, 96),
                          (66, 104), (50, 96), (34, 104)])),
               L(outline([(10, 46), (90, 46), (90, 60), (10, 60)]), 'shade', 'b', False),
               L(outline([(56, 60), (90, 60), (88, 94), (62, 102)]), 'deep', 'b', False)],
}

# Ishigashi Gorham: melena azul larga y lisa, con el flequillo largo que le cae entre los ojos tapando el izquierdo y dos
# mechones gruesos que se curvan hacia fuera a los lados; ojos verdes de sueño
CHARS['meteo-garnet'] = {
    'body': 'delgado', 'pal': pal('#3a7ab8', WHITE_SKIN, iris='#2a9a5a', shade='#2a4a72', deep='#1e3452'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 104), (4, 70), (-8, 66), (-14, 84, 1), (-12, 54), (4, 30), (16, 4), (34, -10), (60, -10), (82, 2), (96, 30), (112, 54), (114, 84, 1), (104, 66),
                         (96, 70), (90, 104), (82, 70), (18, 70)])),
              L(outline([(60, -6), (84, 4), (96, 40), (92, 96), (82, 60)]), 'shade', 'b', False),
              L(ell(10, 74, 3, 5), 'skin', 'b', ln=True)]
             + [fringe([(12, 84), (12, 46), (24, 22), (46, 10), (72, 16), (88, 38), (90, 84), (82, 66), (76, 50), (66, 58), (60, 92, 1), (54, 64), (48, 92, 1), (42, 62), (30, 52),
                        (22, 66)]),
                strand([(54, 18), (56, 60)], 'shade', 'f', 1.2), strand([(36, 22), (30, 60)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 70), (58, 54), (80, 52), (94, 38), (92, 12), (74, -6), (44, -10), (18, -2), (2, 16), (-6, 44), (-30, 30, 1), (-14, 60), (-4, 80), (2, 104), (14, 110, 1),
                        (24, 96), (40, 92), (48, 82)])),
             L(outline([(-6, 44), (22, 50), (30, 92), (2, 92)]), 'shade', 'b', False),
             fringe([(62, 2), (90, 16), (96, 42), (96, 78, 1), (88, 60), (82, 70, 1), (76, 46), (66, 30)])],
    'back': [L(outline([(10, 104), (4, 70), (-8, 66), (-14, 84, 1), (-12, 54), (4, 30), (16, 4), (34, -10), (60, -10), (82, 2), (96, 30), (112, 54), (114, 84, 1), (104, 66),
                        (96, 70), (90, 104), (70, 114, 1), (50, 104), (30, 114, 1)]), 'shade'),
             L(outline([(16, 4), (34, -10), (60, -10), (82, 2), (90, 20), (60, 30), (30, 30), (10, 20)]), 'mid', 'b', False),
             L(outline([(-12, 54), (4, 30), (14, 40), (2, 70)]), 'mid', 'b', False), L(outline([(112, 54), (96, 30), (86, 40), (98, 70)]), 'mid', 'b', False)],
}

# Deimos Lepton: pelo gris azulado en casco hasta la mandíbula, con una coleta baja en la nuca y dos cuernos de pelo que se
# curvan hacia arriba y hacia dentro en lo alto; cara pintada de payaso (cejas negras en ángulo y rayas bajo los ojos)
CHARS['deimos-lepton'] = {
    'body': 'normal', 'pal': pal('#7a8ab8', WHITE_SKIN, iris='#1e1414', shade='#5e6a8e', deep='#46506e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'ears': False},
    'front': [L(outline([(22, 12), (6, -4), (2, -20), (12, -26), (8, -14), (16, -6), (30, 4)])), L(outline([(78, 12), (94, -4), (98, -20), (88, -26), (92, -14), (84, -6), (70, 4)])),
              L(outline([(14, 106), (8, 70), (8, 34), (18, 12), (50, 2), (82, 12), (92, 34), (92, 70), (86, 106), (80, 66), (20, 66)])),
              L(outline([(60, 4), (84, 14), (92, 40), (88, 100), (80, 60)]), 'shade', 'b', False)]
             + elf_ears('front', (-8, 54))
             + [fringe([(12, 70), (12, 42), (24, 22), (50, 14), (76, 22), (88, 42), (88, 70), (80, 56), (66, 52), (56, 60), (50, 72, 1), (44, 60), (34, 52), (20, 56)]),
                L(outline([(38, 22), (50, 16), (62, 22), (50, 30)]), 'deep', 'f', False)] + clown('front'),
    'side': [L(outline([(54, 64), (58, 50), (78, 48), (92, 36), (92, 14), (90, -16), (100, -24), (98, -12), (98, 10), (80, 0), (50, -4), (24, 2), (6, 20), (0, 50), (-10, 66),
                        (-16, 104, 1), (2, 88), (10, 76), (26, 82), (42, 80)])),
             L(outline([(2, 40), (26, 46), (28, 78), (8, 72)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (94, 40), (90, 54, 1), (82, 42), (72, 30)])] + elf_ears('side', stip=(26, 50)) + clown('side'),
    'back': elf_ears('back', (-8, 54))
            + [L(outline([(22, 12), (6, -4), (2, -20), (12, -26), (8, -14), (16, -6), (30, 4)])), L(outline([(78, 12), (94, -4), (98, -20), (88, -26), (92, -14), (84, -6), (70, 4)])),
               L(outline([(14, 88), (8, 60), (8, 34), (18, 12), (50, 2), (82, 12), (92, 34), (92, 60), (86, 88), (50, 96)])),
               L(outline([(56, 4), (84, 14), (92, 44), (86, 84), (62, 92)]), 'shade', 'b', False),
               L(outline([(44, 88), (56, 88), (60, 106), (50, 120, 1), (40, 106)]), 'mid', 'f', ln=True)],
}

# Ymir Catena: pelo celeste muy claro en pinchos de punta hacia arriba, y por detrás y a los lados unas trenzas grises
# largas hechas de eslabones; ojos azules redondos con ojeras y una sonrisa enorme de dientes en sierra
_links = lambda x0, y0, x1, y1: [L(ell(x0 + (x1 - x0) * k / 4, y0 + (y1 - y0) * k / 4, 4.2, 4.6), 'link', 'b', ln=True) for k in range(5)]
CHARS['ymir-catena'] = {
    'body': 'bajito', 'pal': pal('#a8d8f0', WHITE_SKIN, iris='#2a6a8a', shade='#8aa8c0', link='#a0a4b0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': _links(18, 76, -4, 116) + _links(82, 76, 104, 116)
             + [L(outline([(16, 64), (6, 52), (-4, 28, 1), (12, 30), (10, 4, 1), (24, 14), (30, -12, 1), (40, 6), (50, -18, 1), (60, 6), (70, -12, 1), (76, 14), (90, 4, 1), (88, 30),
                           (104, 28, 1), (94, 52), (84, 64), (78, 50), (22, 50)])),
                L(outline([(58, 0), (82, 10), (92, 40), (86, 58), (76, 36)]), 'shade', 'b', False)]
             + elf_ears('front', (-6, 60))
             + [fringe([(14, 56), (16, 40), (30, 30), (50, 26), (70, 30), (84, 40), (86, 56), (78, 48), (70, 54, 1), (62, 44), (54, 52, 1), (50, 42), (46, 52, 1), (38, 44),
                        (30, 54, 1), (22, 48)]),
                L(outline([(30, 92), (50, 98), (70, 92), (64, 104), (50, 108), (36, 104)]), OUTC, 'f', False),
                L([(32, 93), (36, 99), (40, 94), (44, 100), (48, 95), (52, 100), (56, 95), (60, 100), (64, 94), (68, 98)], (250, 250, 250, 255), 'f', False, False, 1.8)],
    'side': _links(30, 74, 0, 112)
            + [L(outline([(56, 54), (62, 42), (80, 40), (90, 26), (98, 4, 1), (76, 8), (72, -18, 1), (58, 0), (40, -24, 1), (34, 4), (10, -8, 1), (14, 18), (-6, 26, 1), (6, 40),
                          (4, 60), (16, 72), (32, 72), (46, 62)])),
               L(outline([(4, 32), (24, 38), (24, 64), (8, 58)]), 'shade', 'b', False)] + elf_ears('side', stip=(26, 56))
            + [L(outline([(80, 92), (94, 90), (92, 102), (80, 102)]), OUTC, 'f', False)],
    'back': elf_ears('back', (-6, 60))
            + [L(outline([(16, 76), (6, 52), (-4, 28, 1), (12, 30), (10, 4, 1), (24, 14), (30, -12, 1), (40, 6), (50, -18, 1), (60, 6), (70, -12, 1), (76, 14), (90, 4, 1),
                          (88, 30), (104, 28, 1), (94, 52), (84, 76), (50, 84)]), 'shade'),
               L(outline([(24, 14), (30, -12, 1), (40, 6), (50, -18, 1), (60, 6), (70, -12, 1), (76, 14), (70, 30), (50, 34), (30, 30)]), 'mid', 'b', False)]
            + [l for k in _links(28, 78, 8, 116) + _links(50, 80, 50, 120) + _links(72, 78, 92, 116) for l in [dict(k, z='f')]],
}

# Sinope Rinoa: pelo azul en casco redondo con dos cuernos finos en lo alto, flequillo que le tapa la frente hasta las cejas y
# los lados bajando en mechones hasta la mandíbula; ojos negros grandes
CHARS['sinope-linea'] = {
    'body': 'normal', 'pal': pal('#5a8ac8', WHITE_SKIN, iris='#1e1414', shade='#3e5a82', deep='#2e4462'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 20), (2, -22, 1), (26, 8)])), L(outline([(84, 20), (98, -22, 1), (74, 8)])),
              L(outline([(10, 100), (6, 60), (8, 24), (26, 6), (50, 0), (74, 6), (92, 24), (94, 60), (90, 100), (82, 70), (18, 70)])),
              L(outline([(60, 4), (86, 16), (94, 44), (90, 96), (80, 60)]), 'shade', 'b', False)]
             + elf_ears('front', (-12, 58))
             + [fringe([(12, 70), (12, 40), (26, 18), (50, 12), (74, 18), (88, 40), (88, 70), (80, 58), (70, 54), (60, 60), (50, 66, 1), (40, 60), (30, 54), (20, 58)])],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (90, 14), (72, 0), (64, -24, 1), (58, -2), (34, -4), (12, 8), (0, 34), (-10, 50), (-2, 74), (-10, 90, 1), (8, 86),
                        (20, 98, 1), (30, 86), (46, 76)])),
             L(outline([(0, 40), (24, 46), (28, 82), (4, 82)]), 'shade', 'b', False),
             fringe([(62, 2), (90, 16), (96, 42), (96, 70, 1), (86, 54), (80, 66, 1), (76, 44), (66, 30)])] + elf_ears('side', stip=(22, 52)),
    'back': elf_ears('back', (-12, 58))
            + [L(outline([(16, 20), (2, -22, 1), (26, 8)])), L(outline([(84, 20), (98, -22, 1), (74, 8)])),
               L(outline([(8, 96), (6, 60), (8, 24), (26, 6), (50, 0), (74, 6), (92, 24), (94, 60), (92, 96), (74, 104, 1), (62, 94), (50, 104, 1), (38, 94), (26, 104, 1)])),
               L(outline([(56, 4), (86, 16), (94, 46), (90, 92), (66, 98)]), 'shade', 'b', False)],
}

# Tarvos Boson: pelo gris azulado en un pico altísimo como una mitra, con dos cuernos finos que salen a los lados, que le cae
# como una capa hasta los hombros; nariz enorme, ojos rojos y sonrisa de dientes
CHARS['tarvos-boson'] = {
    'body': 'corpulento', 'pal': pal('#a8c8d8', WHITE_SKIN, iris='#c81e1e', shade='#8a8494', deep='#6a6474'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 104, 'hairline': False, 'ears': False},
    'front': [L(outline([(26, 40), (2, 20, 1), (24, 30)]), 'mid', 'b', ln=True), L(outline([(74, 40), (98, 20, 1), (76, 30)]), 'mid', 'b', ln=True),
              L(outline([(0, 120), (6, 80), (14, 50), (30, 24), (46, -24, 1), (54, -20), (70, 24), (86, 50), (94, 80), (100, 120), (84, 108), (84, 62), (16, 62), (16, 108)])),
              L(outline([(54, -18), (70, 24), (88, 54), (98, 116), (84, 104), (80, 54)]), 'shade', 'b', False)]
             + elf_ears('front', (-10, 76))
             + [fringe([(14, 66), (24, 42), (40, 30), (50, 50, 1), (60, 30), (76, 42), (86, 66), (70, 56), (50, 62), (30, 56)]),
                L(outline([(42, 76), (58, 76), (62, 92), (50, 98), (38, 92)]), 'skin', 'f', ln=True)],
    'side': [L(outline([(52, 120), (54, 88), (60, 62), (76, 50), (90, 36), (80, 14), (60, -24, 1), (50, -18), (34, 0), (14, 20), (0, 50), (-6, 90), (-10, 120)])),
             L(outline([(0, 50), (30, 30), (40, 110), (-6, 116)]), 'shade', 'b', False),
             L(outline([(48, 30), (34, 6, 1), (56, 22)]), 'mid', 'f', ln=True),
             L(outline([(86, 72), (104, 92), (88, 96)]), 'skin', 'f', ln=True)] + elf_ears('side', stip=(30, 74)),
    'back': elf_ears('back', (-10, 76))
            + [L(outline([(26, 40), (2, 20, 1), (24, 30)]), 'mid', 'b', ln=True), L(outline([(74, 40), (98, 20, 1), (76, 30)]), 'mid', 'b', ln=True),
               L(outline([(0, 120), (6, 80), (14, 50), (30, 24), (46, -24, 1), (54, -20), (70, 24), (86, 50), (94, 80), (100, 120), (50, 126)]), 'shade'),
               L(outline([(46, -24), (54, -20), (64, 20), (60, 80), (50, 110), (40, 80), (36, 20)]), 'mid', 'b', False)],
}

# Dione Bulge: pelo gris azulado peinado hacia atrás en un moño alto con dos mechones que salen ondulados a los lados como
# serpentinas; cara alargada pintada (cejas negras en ángulo y rayas), orejas puntiagudas y gesto serio
CHARS['dione'] = {
    'body': 'delgado', 'pal': pal('#a8c4e0', WHITE_SKIN, iris='#1e1414', shade='#8a8aa0', deep='#6a6a80'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'ears': False,
             'face_front': outline([(20, 52), (24, 30), (50, 22), (76, 30), (80, 52), (78, 84), (62, 104), (50, 110), (38, 104), (22, 84)])},
    'front': [L(outline([(34, 6), (30, -12), (46, -24), (66, -20), (70, -8), (60, 2)])),
              L(quad((20, 30), (-4, 20), (-14, 28)), 'mid', 'b', False, False, 3.4),
              L(quad((80, 30), (100, 22), (104, 36)) + quad((104, 36), (110, 50), (100, 62))[1:], 'mid', 'b', False, False, 3.4),
              L(outline([(18, 58), (16, 30), (28, 10), (50, 4), (72, 10), (84, 30), (82, 58), (72, 40), (62, 32), (50, 30), (38, 32), (28, 40)]))]
             + elf_ears('front', (-6, 66))
             + [L(outline([(40, 8), (50, 4), (60, 8), (54, 24), (46, 24)]), 'light', 'f', False),
                L(outline([(46, 66), (54, 66), (58, 90), (50, 94), (42, 90)]), 'skin', 'f', ln=True)] + clown('front'),
    'side': [L(outline([(40, 10), (24, -4), (2, 4), (-12, 26), (-6, 44), (6, 36), (4, 18), (20, 16)])),
             L(outline([(56, 54), (64, 42), (78, 40), (90, 26), (82, 10), (60, 0), (36, 2), (16, 12), (6, 32), (10, 56), (20, 62), (34, 60), (46, 56)])),
             L(outline([(6, 32), (28, 34), (30, 56), (12, 54)]), 'shade', 'b', False)] + elf_ears('side', stip=(28, 58)) + clown('side'),
    'back': elf_ears('back', (-6, 66))
            + [L(quad((20, 30), (-4, 20), (-14, 28)), 'mid', 'b', False, False, 3.4),
               L(quad((80, 30), (100, 22), (104, 36)) + quad((104, 36), (110, 50), (100, 62))[1:], 'mid', 'b', False, False, 3.4),
               L(outline([(18, 70), (16, 30), (28, 10), (50, 4), (72, 10), (84, 30), (82, 70), (50, 76)])),
               L(outline([(56, 6), (80, 14), (84, 40), (80, 66), (62, 72)]), 'shade', 'b', False),
               L(outline([(34, 6), (30, -14), (50, -26), (68, -18), (66, -2)]), 'mid', 'f', ln=True)],
}

# Despina Lax: melena larga gris azulada que le cae lisa hasta la espalda, con un flequillo largo que le tapa el ojo derecho
# y dos mechones finos que salen curvados hacia los lados; un ojo ámbar visible y una sonrisa
CHARS['despina'] = {
    'body': 'chica', 'pal': pal('#8a90b8', WHITE_SKIN, iris='#c8861e', shade='#6a6488', deep='#504a6e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(quad((18, 38), (-14, 30), (-18, 56)), 'mid', 'b', False, False, 3.0), L(quad((82, 38), (114, 30), (118, 56)), 'mid', 'b', False, False, 3.0),
              L(outline([(6, 116), (2, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (98, 70), (94, 116), (82, 112), (82, 70), (18, 70), (18, 112)])),
              L(outline([(60, 2), (86, 14), (98, 50), (96, 112), (84, 70)]), 'shade', 'b', False)]
             + [fringe([(12, 90), (10, 46), (24, 18), (50, 10), (76, 18), (88, 40), (88, 64), (80, 52), (66, 50), (58, 64), (54, 80), (44, 92, 1), (36, 76), (24, 92, 1)]),
                strand([(30, 22), (22, 70)], 'shade', 'f', 1.0), strand([(44, 16), (38, 80)], 'shade', 'f', 1.0)],
    'side': [L(outline([(52, 74), (56, 58), (78, 54), (92, 40), (88, 14), (66, -2), (36, -4), (14, 10), (2, 40), (-4, 80), (-10, 118, 1), (14, 110), (30, 104), (44, 92)])),
             L(outline([(2, 40), (28, 46), (34, 100), (6, 104)]), 'shade', 'b', False),
             fringe([(62, 2), (90, 16), (96, 44), (96, 86, 1), (86, 66), (78, 46), (66, 30)])],
    'back': [L(quad((18, 38), (-14, 30), (-18, 56)), 'mid', 'b', False, False, 3.0), L(quad((82, 38), (114, 30), (118, 56)), 'mid', 'b', False, False, 3.0),
             L(outline([(4, 118), (2, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (98, 70), (96, 118), (50, 124)]), 'shade'),
             L(outline([(22, 6), (50, -2), (78, 6), (90, 24), (50, 30), (10, 24)]), 'mid', 'b', False)],
}

# Bitway Ozrock (capitán): un tocado turquesa abultado como un cerebro, con una cresta en el centro de la frente y dos antenas
# finísimas que salen a los lados, que le baja por las mejillas como un casco; cara blanca, ojos amarillos y sonrisa
CHARS['ozrock-boldar'] = {
    'body': 'normal', 'pal': pal('#1e8a90', WHITE_SKIN, iris='#a8b020', shade='#14686e', deep='#0e4a4e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L([(14, 48), (-22, 60)], 'deep', 'b', False, False, 2.0), L([(86, 48), (122, 60)], 'deep', 'b', False, False, 2.0),
              L(outline([(16, 104), (6, 84), (12, 70), (2, 50), (8, 24), (22, 6), (50, -2), (78, 6), (92, 24), (98, 50), (88, 70), (94, 84), (84, 104), (78, 88), (78, 66), (22, 66),
                         (22, 88)])),
              L(outline([(60, 2), (86, 14), (96, 48), (88, 98), (80, 64)]), 'shade', 'b', False),
              L(outline([(16, 64), (22, 58), (34, 70), (40, 64), (50, 74, 1), (60, 64), (66, 70), (78, 58), (84, 64), (78, 74), (64, 76), (50, 84), (36, 76), (22, 74)]), 'mid', 'f',
                ln=True),
              L(outline([(44, 10), (50, 2), (56, 10), (54, 60), (50, 68, 1), (46, 60)]), 'deep', 'f', ln=True),
              strand([(22, 24), (30, 50)], 'deep', 'f', 1.0), strand([(78, 24), (70, 50)], 'deep', 'f', 1.0),
              strand([(10, 50), (18, 62)], 'deep', 'f', 1.0), strand([(90, 50), (82, 62)], 'deep', 'f', 1.0)],
    'side': [L([(40, 50), (0, 62)], 'deep', 'b', False, False, 2.0),
             L(outline([(54, 98), (58, 80), (66, 66), (84, 62), (94, 46), (90, 20), (72, 2), (44, -4), (18, 6), (4, 30), (0, 60), (6, 84), (20, 98), (36, 104)])),
             L(outline([(4, 30), (30, 36), (34, 90), (8, 88)]), 'shade', 'b', False),
             strand([(20, 30), (40, 60)], 'deep', 'b', 1.0), strand([(50, 10), (60, 50)], 'deep', 'b', 1.0)],
    'back': [L([(14, 48), (-22, 60)], 'deep', 'b', False, False, 2.0), L([(86, 48), (122, 60)], 'deep', 'b', False, False, 2.0),
             L(outline([(14, 96), (4, 70), (2, 44), (10, 20), (28, 4), (50, -2), (72, 4), (90, 20), (98, 44), (96, 70), (86, 96), (64, 104), (50, 96), (36, 104)])),
             L(outline([(56, 2), (88, 18), (98, 50), (88, 92), (62, 100)]), 'shade', 'b', False),
             L(outline([(36, 10), (50, 6), (64, 10), (60, 60), (50, 90), (40, 60)]), 'deep', 'b', False)],
}

# Loge Kolith: pelo azul en casco redondo con flequillo recto cortado sobre las cejas y dos mechones largos que bajan en arco
# hasta la mandíbula; cara blanca con grietas grises pintadas, ojos morados enormes y una sonrisa torcida
CHARS['loge-colles'] = {
    'body': 'normal', 'pal': pal('#5a88c8', WHITE_SKIN, iris='#8a2a6a', shade='#3e4e72', deep='#2e3a56', crack='#8a8a98'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 54), (2, 72), (-4, 100, 1), (8, 82), (18, 66)])), L(outline([(84, 54), (98, 72), (104, 100, 1), (92, 82), (82, 66)])),
              L(outline([(6, 62), (4, 34), (18, 12), (50, 4), (82, 12), (96, 34), (94, 62), (80, 56), (20, 56)])),
              L(outline([(60, 8), (84, 16), (94, 40), (90, 58), (80, 40)]), 'shade', 'b', False)]
             + elf_ears('front', (-8, 70))
             + [L(outline([(10, 66), (10, 40), (24, 22), (50, 16), (76, 22), (90, 40), (90, 66)]), 'mid', 'f', ln=True),
                L(outline([(56, 22), (78, 28), (88, 46), (88, 64), (78, 64), (74, 40)]), 'shade', 'f', False),
                L([(30, 70), (24, 82), (28, 94)], 'crack', 'f', False, False, 1.4), L([(70, 70), (78, 80), (72, 94)], 'crack', 'f', False, False, 1.4),
                strand([(22, 64), (24, 52)], 'shade', 'f', 1.0), strand([(40, 66), (40, 54)], 'shade', 'f', 1.0), strand([(60, 66), (60, 54)], 'shade', 'f', 1.0),
                strand([(78, 64), (76, 52)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 50), (66, 44), (82, 42), (96, 32), (92, 14), (72, 2), (44, -2), (18, 8), (2, 28), (-6, 52), (8, 64), (28, 62), (44, 54)])),
             L(outline([(70, 44), (84, 52), (82, 96, 1), (72, 66)]), 'mid', 'f', ln=True),
             L(outline([(-6, 40), (30, 44), (36, 60), (-2, 58)]), 'shade', 'b', False),
             L([(84, 70), (88, 84)], 'crack', 'f', False, False, 1.4)] + elf_ears('side', stip=(26, 64)),
    'back': elf_ears('back', (-8, 70))
            + [L(outline([(16, 54), (2, 72), (-4, 100, 1), (8, 82), (18, 66)])), L(outline([(84, 54), (98, 72), (104, 100, 1), (92, 82), (82, 66)])),
               L(outline([(6, 70), (4, 34), (18, 12), (50, 4), (82, 12), (96, 34), (94, 70), (50, 76)])),
               L(outline([(56, 8), (82, 14), (96, 40), (94, 66), (66, 72)]), 'shade', 'b', False),
               L(outline([(30, 70), (70, 70), (66, 90), (34, 90)]), 'shade', 'b')],
}
