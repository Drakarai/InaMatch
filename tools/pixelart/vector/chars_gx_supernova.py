"""Supernova (gx-supernova): equipo de alienígenas de Galaxy (la ruta de la versión Supernova). Referencias: sus modelos 3D de
Inazuma Eleven GO Galaxy en la enciclopedia (uno por jugador)."""
from chars import CHARS, L, OUTC, ell, mirror, outline, pal, rope, strand  # noqa: F401
from chars_gx_big_bang import NOEARS, ball, elf
from heads import quad

WHITE = (248, 248, 248, 255)


def both(pts, c='mid', z='f', ln=True, sil=True):
    """La misma forma a la izquierda y, reflejada, a la derecha."""
    o = outline(pts)
    return [L(o, c, z, sil, ln), L(mirror(o), c, z, sil, ln)]


# Ashvina Bharani (portera): piel morena rojiza, melena lisa larguísima blanca plateada (lila por detrás) con flequillo de
# mechones; dos cuernos anaranjados que salen de los lados de la cabeza y se curvan hacia arriba; ojos granates
_ash_horns = both([(16, 60), (4, 40), (2, 14), (8, -8), (14, -18, 1), (14, 0), (14, 24), (22, 46)], 'horn') \
    + both([(10, 30), (8, 6), (13, -10), (12, 12)], 'horn_d', 'f', False, False)
CHARS['ashvina-bharani'] = {
    'body': 'chica', 'pal': pal('#dcf0f4', '#b4603e', iris='#a03050', shade='#b4aec4', deep='#9a92ac', horn='#c8642c', horn_d='#9a4a20'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(14, 130), (4, 100), (2, 44), (14, 14), (50, 2), (86, 14), (98, 44), (96, 100), (86, 130), (82, 70), (18, 70)])),
              L(outline([(58, 6), (84, 16), (98, 48), (94, 120), (84, 126), (82, 66)]), 'shade', 'b', False),
              L(outline([(12, 86), (10, 46), (22, 22), (46, 12), (72, 18), (88, 40), (90, 86), (84, 64), (76, 72, 1), (70, 50), (60, 60, 1), (56, 42), (48, 64, 1),
                         (42, 44), (32, 58, 1), (26, 46), (18, 70, 1)]), 'mid', 'f'),
              L(outline([(60, 20), (80, 30), (86, 50), (74, 44)]), 'shade', 'f', False)] + _ash_horns,
    'side': [L(outline([(54, 66), (58, 52), (80, 48), (92, 34), (86, 12), (62, -2), (34, 0), (12, 14), (2, 40), (-2, 90), (-6, 130), (20, 132), (32, 100), (46, 80)])),
             L(outline([(2, 40), (28, 46), (30, 120), (0, 126)]), 'shade', 'b', False),
             L(outline([(64, 4), (90, 18), (96, 42), (94, 72, 1), (86, 54), (80, 66, 1), (76, 44), (64, 30)]), 'mid', 'f'),
             L(outline([(52, 62), (42, 40), (40, 12), (46, -8), (52, -18, 1), (52, 2), (52, 26), (58, 48)]), 'horn', 'f', ln=True)],
    'back': [L(outline([(10, 130), (2, 90), (2, 44), (14, 14), (50, 2), (86, 14), (98, 44), (98, 90), (90, 130), (50, 136)])),
             L(outline([(54, 4), (84, 16), (98, 50), (98, 124), (64, 132), (66, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 70), (26, 126)], 'deep', 'b', 1.0), strand([(70, 20), (76, 70), (74, 126)], 'deep', 'b', 1.0)] + _ash_horns,
}

# Hastah Savitar: piel verde agua de reptil, sin pelo; la cabeza acaba en pico arriba, con dos cuernecillos, puntos blancos en
# la frente y unas orejas grandes de animal (rosas por dentro) hacia arriba y a los lados; ojos negros y boca ancha
_hs_ears = both([(18, 58), (-10, 34, 1), (-4, 52), (16, 70)], 'skin', 'b') + both([(14, 58), (-4, 40, 1), (0, 52), (14, 64)], 'inner', 'b', False, False)
CHARS['hastar-savitar'] = {
    'body': 'normal', 'pal': pal('#7ab8a2', '#7ab8a2', iris='#1a1a1e', skin_d='#5e9a86', inner='#e8a8b0', horn='#c8c0b8'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': _hs_ears + both([(28, 24), (20, 2), (24, -10, 1), (32, 16)], 'horn', 'b')
             + [L(outline([(16, 72), (14, 44), (24, 20), (40, 6), (50, -10, 1), (60, 6), (76, 20), (86, 44), (84, 72)]), 'skin'),
                L(outline([(58, 8), (76, 22), (86, 46), (82, 64)]), 'skin_d', 'b', False),
                L(ell(50, 30, 2.4, 4), WHITE, 'f', ln=True), L(ell(42, 40, 2, 3), WHITE, 'f', ln=True), L(ell(58, 40, 2, 3), WHITE, 'f', ln=True),
                L(ell(36, 50, 1.6, 2.6), WHITE, 'f', ln=True), L(ell(64, 50, 1.6, 2.6), WHITE, 'f', ln=True)],
    'side': [L(outline([(56, 62), (62, 48), (82, 44), (92, 30), (84, 10), (60, -8, 1), (34, 0), (14, 14), (6, 40), (8, 66), (22, 84), (40, 84), (48, 72)]), 'skin'),
             L(outline([(10, 40), (30, 46), (32, 78), (14, 72)]), 'skin_d', 'b', False),
             L(outline([(40, 54), (14, 24, 1), (22, 48), (38, 68)]), 'skin', 'f', ln=True), L(outline([(36, 54), (20, 32, 1), (26, 50), (36, 62)]), 'inner', 'f', False),
             L(outline([(60, 14), (54, -6), (58, -16, 1), (66, 10)]), 'horn', 'f', ln=True),
             L(ell(84, 40, 1.8, 3), WHITE, 'f', ln=True), L(ell(78, 30, 1.8, 3), WHITE, 'f', ln=True)],
    'back': _hs_ears + both([(28, 24), (20, 2), (24, -10, 1), (32, 16)], 'horn', 'b')
            + [L(outline([(16, 76), (14, 44), (24, 20), (40, 6), (50, -10, 1), (60, 6), (76, 20), (86, 44), (84, 76), (62, 88), (38, 88)]), 'skin'),
               L(outline([(56, 8), (76, 22), (86, 50), (82, 74), (60, 86)]), 'skin_d', 'b', False)],
}

# Apas Muulan: tupé verde oscuro altísimo y redondeado, con la melena que baja por los lados hasta la mandíbula y por detrás
# hasta la nuca; cara pálida, nariz redonda naranja, ojos rasgados y una sonrisa enorme de dientes
CHARS['apas-mulan'] = {
    'body': 'delgado', 'pal': pal('#40503a', '#f8e4b4', iris='#1a1a1e', shade='#2e3a2a', light='#6a8a5e', nose='#e8783a'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False, 'nose': (50, 84, 3.4)},
    'front': elf('front', 22, 4)
             + [L(outline([(14, 104), (8, 70), (10, 40), (18, 20), (14, -2), (20, -24), (40, -34), (60, -34), (80, -24), (86, -2), (82, 20), (90, 40), (92, 70), (86, 104),
                           (80, 66), (20, 66)])),
                L(outline([(58, -30), (80, -20), (84, 0), (80, 22), (90, 48), (88, 96), (80, 60), (66, 16)]), 'shade', 'b', False),
                L(outline([(30, -24), (44, -30), (38, -12)]), 'light', 'b', False),
                L(outline([(16, 58), (24, 34), (40, 22), (50, 30), (60, 22), (76, 34), (84, 58), (74, 48), (62, 44), (56, 64, 1), (50, 46), (44, 64, 1), (38, 44), (26, 48)]), 'mid', 'f'),
                L(outline([(14, 66), (22, 68), (24, 100), (18, 108, 1), (14, 96)]), 'mid', 'f', ln=True), L(outline([(86, 66), (78, 68), (76, 100), (82, 108, 1), (86, 96)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 62), (60, 48), (80, 46), (92, 32), (90, 14), (96, -8), (86, -26), (62, -34), (36, -30), (18, -14), (14, 10), (6, 40), (4, 74), (12, 96), (28, 98),
                        (42, 86), (48, 74)])),
             L(outline([(6, 40), (30, 40), (34, 90), (12, 92)]), 'shade', 'b', False), L(outline([(40, -26), (60, -30), (50, -16)]), 'light', 'b', False),
             L(outline([(66, 2), (92, 16), (96, 40), (94, 60, 1), (86, 46), (76, 36)]), 'mid', 'f')]
            + elf('side', 20, 4),
    'back': elf('front', 22, 4)
            + [L(outline([(14, 100), (8, 70), (10, 40), (18, 20), (14, -2), (20, -24), (40, -34), (60, -34), (80, -24), (86, -2), (82, 20), (90, 40), (92, 70), (86, 100),
                          (70, 108, 1), (50, 102), (30, 108, 1)])),
               L(outline([(56, -30), (80, -20), (84, 0), (82, 24), (92, 56), (88, 98), (64, 104)]), 'shade', 'b', False)],
}

# Soma Rohby: pelo azul grisáceo ondulado y corto por detrás, con flequillo de mechones y una trenza que le cae por un lado
# hasta el pecho; orejas enormes de murciélago, rosas por dentro, hacia arriba y a los lados; ojos amarillos
_soma_ears = both([(20, 64), (-12, 30, 1), (-2, 60), (16, 80)], 'skin', 'b') + both([(16, 64), (-4, 38, 1), (2, 60), (14, 74)], 'inner', 'b', False, False)
CHARS['soma-lobi'] = {
    'body': 'normal', 'pal': pal('#3e4c5c', '#fce6cc', iris='#d8a020', shade='#2c3846', inner='#e8a8a0', light='#6a7c8e'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': _soma_ears
             + [L(outline([(16, 82), (10, 50), (14, 24), (30, 6), (50, 0), (70, 6), (86, 24), (90, 50), (84, 82), (80, 64), (20, 64)])),
                L(outline([(58, 4), (82, 16), (90, 44), (86, 72), (78, 46)]), 'shade', 'b', False),
                L(outline([(12, 74), (12, 44), (24, 20), (48, 12), (72, 18), (86, 38), (88, 74), (82, 60), (76, 68, 1), (70, 50), (60, 60, 1), (56, 44), (50, 66, 1),
                           (44, 46), (36, 60, 1), (28, 48), (20, 66, 1)]), 'mid', 'f'),
                L(outline([(30, 20), (46, 14), (38, 26)]), 'light', 'f', False),
                L(rope((80, 70), (90, 90), (84, 116), 9)), strand([(78, 80), (90, 84)], 'shade', 'f', 1.2), strand([(82, 94), (92, 98)], 'shade', 'f', 1.2),
                strand([(80, 106), (90, 110)], 'shade', 'f', 1.2)],
    'side': [L(outline([(54, 62), (58, 48), (80, 46), (92, 32), (86, 12), (62, -2), (34, 0), (12, 14), (2, 40), (2, 66), (12, 84), (30, 88), (44, 80)])),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(48, 66), (30, 22, 1), (36, 56), (46, 80)]), 'skin', 'f', ln=True), L(outline([(46, 64), (34, 34, 1), (38, 58), (44, 74)]), 'inner', 'f', False),
             L(outline([(64, 2), (90, 16), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (64, 30)]), 'mid', 'f'),
             L(rope((66, 76), (76, 96), (72, 118), 8))],
    'back': _soma_ears
            + [L(outline([(14, 84), (8, 50), (14, 24), (30, 6), (50, 0), (70, 6), (86, 24), (92, 50), (86, 84), (70, 94, 1), (60, 86), (50, 96, 1), (40, 86), (30, 94, 1)])),
               L(outline([(56, 4), (82, 16), (92, 48), (86, 80), (62, 88)]), 'shade', 'b', False),
               L(rope((20, 78), (12, 96), (16, 116), 8))],
}

# Rudra Ard: casco blanco que le cubre la cabeza y se alarga hacia atrás como una cola, con dos orejas grises puntiagudas y
# una máscara gris de dibujos en forma de alas sobre la cara; solo se le ven los ojos rojos
_ru_ears = both([(22, 40), (8, 2, 1), (32, 26)], 'grey', 'f')
CHARS['rudra-ardo'] = {
    'body': 'normal', 'pal': pal('#eeeeee', '#9a9aa2', iris='#c01e2a', shade='#c8c8cc', grey='#8a8a92', grey_d='#6a6a72', pinkb='#d8aaa4'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(-2, 70), (0, 40), (16, 14), (50, 2), (84, 14), (100, 40), (102, 70), (84, 60), (50, 54), (16, 60)])),
              L(outline([(58, 6), (84, 16), (98, 44), (100, 66), (86, 58)]), 'shade', 'b', False)] + _ru_ears
             + [L(outline([(18, 56), (30, 34), (40, 42), (46, 30), (50, 60), (54, 30), (60, 42), (70, 34), (82, 56), (70, 70), (50, 66), (30, 70)]), 'grey', 'f', ln=True),
                L(outline([(30, 82), (50, 90), (70, 82), (66, 100), (50, 104), (34, 100)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(54, 58), (62, 46), (82, 42), (92, 28), (84, 8), (60, -2), (30, 0), (6, 20), (-30, 50), (-48, 60, 1), (-20, 62), (4, 70), (24, 80), (44, 70)])),
             L(outline([(-30, 50), (4, 34), (24, 50), (4, 66), (-20, 62)]), 'pinkb', 'b', False),
             L(outline([(60, 22), (54, -10, 1), (72, 18)]), 'grey', 'f', ln=True),
             L(outline([(62, 50), (78, 40), (92, 44), (94, 70), (80, 66)]), 'grey', 'f', ln=True)],
    'back': [L(outline([(-4, 70), (-2, 40), (16, 14), (50, 2), (84, 14), (102, 40), (104, 70), (80, 84), (50, 90), (20, 84)])),
             L(outline([(14, 50), (50, 40), (86, 50), (80, 80), (50, 88), (20, 80)]), 'pinkb', 'b', False)] + _ru_ears,
}

# Bhaga Gouny: corpulento, con una melena-pelaje morado oscuro muy espesa y erizada que le rodea la cara como a un gorila,
# la cara celeste pálido con el pelo bajando por la frente, orejas pequeñas puntiagudas y ojos amarillos
CHARS['bhaga-guni'] = {
    'body': 'corpulento', 'pal': pal('#2e2a3c', '#ace0d8', iris='#d8b020', shade='#1e1c2a', light='#4a4660'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': elf('front', 18, 2)
             + [L(outline([(8, 110), (-6, 96, 1), (2, 84), (-10, 70, 1), (4, 60), (-6, 42, 1), (8, 34), (4, 12, 1), (22, 16), (26, -4, 1), (40, 8), (50, -10, 1), (60, 8),
                           (74, -4, 1), (78, 16), (96, 12, 1), (92, 34), (106, 42, 1), (96, 60), (110, 70, 1), (98, 84), (106, 96, 1), (92, 110), (82, 100), (82, 70), (18, 70),
                           (18, 100)])),
                L(outline([(58, 6), (80, 14), (96, 44), (94, 100), (82, 92), (84, 60)]), 'shade', 'b', False),
                L(outline([(14, 66), (20, 44), (34, 36), (50, 42), (66, 36), (80, 44), (86, 66), (74, 62), (64, 66, 1), (58, 58), (50, 64, 1), (42, 58), (36, 66, 1), (26, 62)]), 'mid', 'f'),
                L(outline([(18, 86), (28, 100), (50, 106), (72, 100), (82, 86), (84, 108), (50, 118), (16, 108)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 64), (60, 48), (78, 44), (88, 30), (96, 14, 1), (78, 10), (76, -8, 1), (60, 2), (46, -12, 1), (36, 4), (14, -4, 1), (16, 16), (-6, 20, 1), (6, 34),
                        (-10, 50, 1), (6, 56), (-6, 74, 1), (10, 78), (4, 98, 1), (20, 92), (30, 108, 1), (40, 96), (54, 104, 1), (52, 86)])),
             L(outline([(4, 40), (26, 46), (30, 86), (8, 82)]), 'shade', 'b', False),
             L(outline([(66, 92), (90, 98), (84, 110), (64, 106)]), 'mid', 'f', ln=True)]
            + elf('side', 16, 2),
    'back': elf('front', 18, 2)
            + [L(outline([(8, 108), (-8, 96, 1), (0, 82), (-12, 68, 1), (2, 58), (-8, 40, 1), (8, 32), (4, 12, 1), (22, 16), (26, -4, 1), (40, 8), (50, -10, 1), (60, 8),
                          (74, -4, 1), (78, 16), (96, 12, 1), (92, 32), (108, 40, 1), (98, 58), (112, 68, 1), (100, 82), (108, 96, 1), (92, 108), (72, 118, 1), (60, 108),
                          (50, 120, 1), (40, 108), (28, 118, 1)])),
               L(outline([(56, 6), (80, 14), (98, 46), (96, 104), (66, 112), (70, 50)]), 'shade', 'b', False)],
}

# Mitra Jeshuu: pelo verde azulado en forma de seta que le cubre la frente hasta los ojos, con dos mechones finos que acaban
# en bolitas junto a la barbilla; unas lentes amarillas con rayas negras le tapan los ojos; sonrisa
_mi_lens = both([(20, 66), (34, 64), (44, 70), (42, 82), (30, 84), (20, 78)], 'lens', 'f') \
    + [L([(24, 70), (40, 74)], OUTC, 'f', False, False, 1.4), L([(22, 76), (40, 79)], OUTC, 'f', False, False, 1.4),
       L([(76, 70), (60, 74)], OUTC, 'f', False, False, 1.4), L([(78, 76), (60, 79)], OUTC, 'f', False, False, 1.4)]
CHARS['mitra-jeshu'] = {
    'body': 'normal', 'pal': pal('#2aa8aa', '#fce8d4', shade='#1e8486', light='#6ad4d4', lens='#f0b830'),
    'face': {**NOEARS, 'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 74), (6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (90, 74), (80, 66), (60, 62), (50, 66), (40, 62), (20, 66)])),
              L(outline([(58, 4), (82, 14), (94, 42), (88, 70), (76, 54)]), 'shade', 'b', False),
              L(outline([(26, 14), (42, 8), (34, 22)]), 'light', 'b', False),
              strand([(36, 14), (30, 60)], 'shade', 'f', 1.0), strand([(64, 14), (70, 60)], 'shade', 'f', 1.0), strand([(50, 4), (50, 62)], 'shade', 'f', 1.0)]
             + _mi_lens
             + [L(rope((30, 80), (28, 92), (30, 102), 3)), ball(30, 106, 3.6), L(rope((70, 80), (72, 92), (70, 102), 3)), ball(70, 106, 3.6)],
    'side': [L(outline([(56, 64), (62, 50), (80, 48), (92, 34), (88, 12), (62, -2), (32, 0), (10, 16), (2, 42), (6, 70), (20, 82), (38, 80), (48, 70)])),
             L(outline([(4, 40), (28, 46), (30, 78), (10, 74)]), 'shade', 'b', False),
             L(outline([(64, 2), (90, 16), (98, 40), (96, 64), (84, 66), (78, 44)]), 'mid', 'f'),
             L(outline([(82, 66), (94, 66), (94, 82), (84, 82)]), 'lens', 'f', ln=True), L(rope((76, 82), (76, 94), (78, 102), 3)), ball(78, 106, 3.6)],
    'back': [L(outline([(10, 78), (6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (90, 78), (66, 90), (34, 90)])),
             L(outline([(56, 4), (82, 14), (94, 44), (88, 76), (62, 88)]), 'shade', 'b', False),
             ball(30, 96, 3.6), ball(70, 96, 3.6)],
}

# Indra Vayu: cabeza de cobra dorada: una capucha marrón ancha detrás de la cabeza que le baja hasta los hombros (y una
# trenza por detrás), la cabeza amarilla con una cresta, dos cuernos y puntos rojos; ojos rojos y dientes apretados
CHARS['indra-vayu'] = {
    'body': 'corpulento', 'pal': pal('#b8822c', '#e8c440', iris='#b01e1e', shade='#94661e', skin_d='#c8a028', dot='#c0301e', braid='#d8aa88'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(-6, 104), (-14, 70), (-8, 34), (10, 10), (50, -2), (90, 10), (108, 34), (114, 70), (106, 104), (86, 94), (84, 60), (16, 60), (14, 94)])),
              L(outline([(60, 2), (90, 12), (108, 40), (110, 96), (90, 90)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 34), (30, 16), (50, 10), (70, 16), (84, 34), (84, 62)]), 'skin'),
              L(outline([(58, 12), (72, 18), (84, 38), (84, 60)]), 'skin_d', 'b', False),
              L(outline([(24, 26), (16, 2), (20, -18, 1), (30, 18)]), 'skin', 'f', ln=True), L(outline([(76, 26), (84, 2), (80, -18, 1), (70, 18)]), 'skin', 'f', ln=True),
              L(outline([(44, 14), (50, 6), (56, 14), (54, 50), (50, 56), (46, 50)]), 'skin_d', 'f', False),
              L(ell(38, 36, 2.6, 2.6), 'dot', 'f', False), L(ell(62, 36, 2.6, 2.6), 'dot', 'f', False), L(ell(34, 50, 2.2, 2.2), 'dot', 'f', False),
              L(ell(66, 50, 2.2, 2.2), 'dot', 'f', False)],
    'side': [L(outline([(54, 60), (62, 48), (82, 44), (92, 30), (86, 10), (62, -2), (30, 0), (6, 16), (-12, 50), (-20, 96), (-4, 104), (14, 92), (30, 82), (46, 70)])),
             L(outline([(-12, 50), (10, 40), (16, 86), (-10, 96)]), 'shade', 'b', False),
             L(outline([(54, 56), (60, 40), (66, 16), (84, 12), (92, 30), (82, 44), (66, 50)]), 'skin', 'f'),
             L(outline([(70, 16), (68, -10), (74, -20, 1), (78, 12)]), 'skin', 'f', ln=True),
             L(rope((-8, 98), (-12, 116), (-6, 132), 5), 'braid')],
    'back': [L(outline([(-8, 106), (-14, 70), (-8, 34), (10, 10), (50, -2), (90, 10), (108, 34), (114, 70), (108, 106), (80, 112), (50, 116), (20, 112)])),
             L(outline([(56, 2), (90, 12), (108, 40), (110, 100), (70, 110), (72, 50)]), 'shade', 'b', False),
             L(outline([(24, 26), (16, 2), (20, -18, 1), (30, 18)]), 'skin', 'f', ln=True), L(outline([(76, 26), (84, 2), (80, -18, 1), (70, 18)]), 'skin', 'f', ln=True),
             L(outline([(18, 30), (50, 20), (82, 30), (70, 60), (50, 66), (30, 60)]), 'skin_d', 'f', False),
             L(rope((50, 100), (48, 116), (50, 134), 5), 'braid')],
}

# Vassu Dhanissh: piel tostada, pelo crema muy corto en casco con un pico en medio de la frente y orejas grandes y redondas
# de mono, marrones; ojos rasgados y media sonrisa
CHARS['bass-danish'] = {
    'body': 'normal', 'pal': pal('#f2e6ba', '#c48c62', iris='#1e1e24', shade='#d8c494', ear='#a86e4a', ear_d='#8a5636'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': both([(20, 60), (6, 50), (-6, 56), (-8, 76), (2, 90), (18, 84)], 'ear', 'b') + both([(14, 62), (2, 60), (0, 76), (14, 80)], 'ear_d', 'b', False, False)
             + [L(outline([(16, 62), (14, 34), (26, 12), (50, 4), (74, 12), (86, 34), (84, 62), (76, 48), (60, 40), (54, 50), (50, 62, 1), (46, 50), (40, 40), (24, 48)])),
                L(outline([(58, 8), (80, 18), (86, 42), (82, 58), (74, 42)]), 'shade', 'b', False)],
    'side': [L(outline([(56, 56), (62, 44), (80, 40), (90, 26), (82, 8), (58, -2), (30, 2), (12, 18), (6, 44), (10, 66), (24, 76), (40, 74), (48, 66)])),
             L(outline([(10, 40), (30, 44), (32, 70), (14, 66)]), 'shade', 'b', False),
             L(outline([(52, 56), (36, 50), (28, 64), (32, 82), (48, 86)]), 'ear', 'f', ln=True), L(outline([(48, 60), (38, 58), (36, 72), (46, 78)]), 'ear_d', 'f', False)],
    'back': both([(20, 60), (6, 50), (-6, 56), (-8, 76), (2, 90), (18, 84)], 'ear', 'b')
            + [L(outline([(16, 70), (14, 34), (26, 12), (50, 4), (74, 12), (86, 34), (84, 70), (64, 78), (36, 78)])),
               L(outline([(56, 8), (80, 18), (86, 46), (82, 68), (62, 76)]), 'shade', 'b', False)],
}

# Ashley Sarpara: piel blanca lila, melena lisa lavanda hasta los hombros (rosada por detrás) con raya en medio; dos aletas
# plateadas a los lados de la cabeza y ojos enormes amarillos de alienígena; sonrisa pequeña
_as_fins = both([(16, 56), (4, 48, 1), (8, 60), (18, 64)], 'fin', 'f')
CHARS['ashley-sarpala'] = {
    'body': 'chica', 'pal': pal('#dcd0e4', '#f4e6f2', iris='#c8a020', shade='#b8909a', deep='#9a7880', fin='#b8bcc4'),
    'face': {**NOEARS, 'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 104), (6, 80), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (94, 80), (86, 104), (82, 66), (18, 66)])),
              L(outline([(58, 6), (84, 16), (94, 46), (92, 96), (82, 60)]), 'shade', 'b', False),
              L(outline([(14, 70), (14, 40), (26, 18), (50, 10), (74, 18), (86, 40), (86, 70), (76, 54), (60, 44), (50, 30), (40, 44), (24, 54)]), 'mid', 'f'),
              strand([(50, 12), (50, 30)], 'shade', 'f', 1.0)] + _as_fins
             + both([(26, 70), (40, 66), (46, 74), (42, 84), (30, 84), (24, 78)], 'iris', 'f') + both([(30, 72), (38, 70), (40, 76), (34, 80)], 'deep', 'f', False, False),
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (92, 34), (86, 12), (62, -2), (34, 0), (12, 14), (2, 40), (0, 80), (-6, 104), (12, 106), (30, 96), (46, 80)])),
             L(outline([(2, 40), (26, 46), (30, 92), (4, 100)]), 'shade', 'b', False),
             L(outline([(64, 4), (90, 18), (96, 42), (94, 60), (86, 58), (80, 40), (68, 30)]), 'mid', 'f'),
             L(outline([(80, 68), (92, 66), (94, 82), (82, 82)]), 'iris', 'f', ln=True), L(outline([(56, 56), (40, 46, 1), (46, 60), (56, 64)]), 'fin', 'f', ln=True)],
    'back': [L(outline([(12, 104), (4, 76), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (96, 76), (88, 104), (50, 110)]), 'shade'),
             L(outline([(16, 14), (50, 2), (84, 14), (94, 40), (50, 50), (6, 40)]), 'mid', 'b', False)] + _as_fins,
}

# Acrous Obies: melena morado oscuro larga, espesa y revuelta, con mechones que se enroscan como tentáculos a los lados y
# por detrás, un flequillo que le tapa un ojo y orejas largas de elfo; ojos granates y boca seria
CHARS['arculus-orbes'] = {
    'body': 'normal', 'pal': pal('#4c2c5e', '#fce4cc', iris='#8a1e3a', shade='#341c44', light='#6e4a86'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': elf('front', 30, 10)
             + [L(outline([(16, 108), (2, 100), (-4, 70), (0, 40), (10, 14), (24, -2), (36, -12, 1), (44, 2), (56, -10, 1), (62, 4), (80, 6), (94, 24), (100, 50), (104, 80),
                           (98, 104), (84, 108), (82, 68), (18, 68)])),
                L(outline([(58, 2), (84, 14), (98, 48), (98, 100), (84, 100), (82, 62)]), 'shade', 'b', False),
                L(rope((10, 96), (-16, 104), (-10, 120), 8)), L(rope((90, 96), (116, 104), (110, 120), 8)),
                L(outline([(12, 80), (10, 46), (22, 22), (46, 12), (72, 18), (88, 38), (90, 80), (84, 62), (78, 70, 1), (72, 50), (62, 56), (58, 86, 1), (50, 72),
                           (44, 92, 1), (36, 74), (28, 84, 1), (20, 66)]), 'mid', 'f'),
                L(outline([(28, 22), (44, 16), (36, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (90, 12), (98, -6, 1), (74, -2), (64, -16, 1), (52, -4), (30, -6), (10, 10), (-2, 40), (-12, 80), (-20, 112),
                        (-4, 118), (12, 104), (30, 98), (46, 82)])),
             L(outline([(-2, 40), (24, 48), (30, 96), (-4, 108)]), 'shade', 'b', False),
             L(rope((-6, 100), (-30, 104), (-26, 122), 8)),
             L(outline([(64, 4), (90, 18), (96, 42), (96, 74, 1), (86, 56), (80, 70, 1), (76, 44), (64, 30)]), 'mid', 'f')]
            + elf('side', 28, 10),
    'back': elf('front', 30, 10)
            + [L(outline([(12, 112), (-2, 92), (-6, 60), (0, 30), (16, 8), (36, -8, 1), (44, 4), (56, -8, 1), (62, 4), (84, 8), (100, 30), (106, 60), (102, 92), (88, 112),
                          (70, 120, 1), (50, 112), (30, 120, 1)])),
               L(outline([(56, 2), (86, 12), (102, 46), (100, 106), (66, 114), (70, 50)]), 'shade', 'b', False),
               L(rope((14, 100), (-14, 104), (-10, 122), 8)), L(rope((86, 100), (114, 104), (110, 122), 8)),
               strand([(30, 20), (24, 70), (30, 110)], 'shade', 'b', 1.2), strand([(70, 20), (76, 70), (70, 110)], 'shade', 'b', 1.2)],
}
