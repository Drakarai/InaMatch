"""Tenkuu no Shito / Sky Team (IE3): los ángeles, con sus modelos 3D como referencia (contornos calcados sobre una rejilla
de unidades de cabeza). Las alas van en la equipación (body.py)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_empire import afro
from heads import quad

WHITE = (250, 250, 250, 255)

# Anorel (portero): una nube de pelo verde azulado enorme y plana en lo alto de la cabeza, ancha como un sombrero, con el
# resto corto; los ojos cerrados con unos párpados marrones y la cara alargada
CHARS['anorel'] = {
    'body': 'corpulento', 'pal': pal('#2a9a7a', '#f8d8b0', shade='#1e7a60', light='#5ac0a0', lid='#8a5a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + [L(outline([(16, 46), (14, 20), (26, 6), (50, 2), (74, 6), (86, 20), (84, 46), (50, 40)]), 'shade', 'f'),
                              L(outline([(-16, 20), (-4, 8), (10, 10), (14, -4), (30, -6), (36, -18), (50, -14), (62, -24), (70, -10), (88, -8), (92, 6), (110, 10), (118, 20), (100, 26),
                                         (80, 24), (50, 28), (20, 24), (0, 28)]), 'mid', 'f', ln=True),
                              L(outline([(10, 8), (30, 0), (40, 6), (24, 12)]), 'light', 'f', False), L(outline([(60, -6), (80, -2), (70, 6)]), 'light', 'f', False),
                              L(outline([(24, 70), (42, 70), (40, 80), (26, 80)]), 'lid', 'f', ln=True), L(outline([(76, 70), (58, 70), (60, 80), (74, 80)]), 'lid', 'f', ln=True)],
    'side': bald('side') + [L(outline([(12, 62), (12, 30), (28, 8), (56, 2), (80, 10), (88, 26), (60, 30), (34, 40)]), 'shade', 'f'),
                            L(outline([(-12, 18), (0, 6), (20, -4), (40, -16), (60, -14), (80, -6), (100, 4), (110, 16), (90, 22), (50, 24), (10, 26)]), 'mid', 'f', ln=True),
                            L(outline([(76, 70), (92, 70), (92, 80), (78, 80)]), 'lid', 'f', ln=True)],
    'back': bald('back') + [L(outline([(14, 84), (12, 20), (26, 6), (50, 2), (74, 6), (88, 20), (86, 84), (50, 90)]), 'shade', 'f'),
                            L(outline([(-16, 20), (-4, 8), (14, -4), (36, -16), (64, -18), (86, -6), (106, 8), (118, 20), (100, 28), (50, 32), (0, 28)]), 'mid', 'f', ln=True)],
}
# Nenel: pelo castaño ondulado y abultado en mechones que se curvan hacia fuera a los lados; ojos cerrados de calma, pecas y
# una sonrisa
CHARS['nenel'] = {
    'body': 'normal', 'pal': pal('#6a4a2a', '#fce0b8', shade='#4e341c', freckle='#c8906a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 74), (-8, 66, 1), (4, 56), (2, 30), (16, 8), (40, -6), (60, -6), (84, 8), (98, 30), (96, 56), (108, 66, 1), (92, 74), (84, 62), (16, 62)])),
              L(outline([(60, -2), (84, 10), (96, 34), (92, 62), (80, 40)]), 'shade', 'b', False),
              L(outline([(12, 64), (14, 40), (28, 20), (44, 12), (52, 20), (60, 12), (74, 20), (86, 40), (88, 62), (76, 50), (62, 52), (52, 44), (40, 52), (24, 50)]), 'mid', 'f', ln=True)]
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (28, 84), (74, 86), (70, 88), (72, 84))],
    'side': [L(outline([(44, 92), (22, 88), (8, 76), (-8, 70, 1), (6, 60), (4, 30), (18, 6), (48, -6), (76, 2), (94, 22), (98, 46), (86, 50), (70, 48), (58, 54), (52, 66), (50, 80)])),
             L(outline([(6, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 84), (-8, 76, 1), (4, 60), (2, 30), (16, 8), (40, -6), (60, -6), (84, 8), (98, 30), (96, 60), (108, 76, 1), (92, 84), (70, 90), (50, 84), (30, 90)])),
             L(outline([(56, -2), (84, 10), (98, 40), (94, 80), (64, 88)]), 'shade', 'b', False)],
}
# Genel: cara alargada morena con un mentón larguísimo; una melena rubia rosada enorme y abultada en ondas que se abre a los
# lados; ojos verdes pequeños de pasmo, pestañas y una sonrisa
CHARS['genel'] = {
    'body': 'corpulento', 'pal': pal('#f8d0b0', '#8a5a3a', iris='#4a8a3a', shade='#e0a888', light='#fff0e0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': blob([(22, 30), (50, 24), (78, 30), (80, 70), (74, 110), (60, 128), (40, 128), (26, 110), (20, 70)]),
             'hairline': False, 'ears': False},
    'front': [L(outline([(-14, 86), (-24, 60), (-14, 40), (-20, 20), (0, 4), (20, -8), (50, -12), (80, -8), (100, 4), (120, 20), (114, 40), (124, 60), (114, 86), (90, 72), (80, 48),
                         (60, 30), (40, 30), (20, 48), (10, 72)])),
              L(outline([(60, -8), (98, 6), (116, 36), (114, 80), (92, 70), (80, 40)]), 'shade', 'b', False),
              L(outline([(20, 6), (44, -4), (36, 8)]), 'light', 'b', False),
              L(outline([(22, 40), (36, 26), (50, 30), (64, 26), (78, 40), (66, 42), (50, 38), (34, 42)]), 'mid', 'f', ln=True),
              L(ell(38, 66, 3, 3) + [ell(38, 66, 3, 3)[0]], OUTC, 'f', False, False, 1.2), L(ell(62, 66, 3, 3) + [ell(62, 66, 3, 3)[0]], OUTC, 'f', False, False, 1.2),
              L(ell(38, 66, 1.6, 1.6), 'iris', 'f', False), L(ell(62, 66, 1.6, 1.6), 'iris', 'f', False),
              L([(48, 70), (46, 96), (52, 98)], 'skin_d', 'f', False, False, 1.4),
              L(outline([(38, 104), (50, 106), (62, 104), (56, 114), (44, 114)]), (200, 60, 60, 255), 'f', ln=True)],
    'side': [L(outline([(60, 80), (48, 100), (30, 112, 1), (20, 96), (-4, 104, 1), (-4, 80), (-20, 70, 1), (-8, 54), (-18, 30, 1), (0, 22), (6, 0), (40, -12), (76, -6), (96, 10), (102, 30),
                        (90, 40), (74, 40), (64, 54)])),
             L(outline([(0, 40), (36, 40), (52, 84), (24, 104), (0, 90)]), 'shade', 'b', False)],
    'back': [L(outline([(-14, 86), (-24, 60), (-14, 40), (-20, 20), (0, 4), (20, -8), (50, -12), (80, -8), (100, 4), (120, 20), (114, 40), (124, 60), (114, 86), (94, 100, 1), (76, 90),
                        (60, 106, 1), (50, 92), (40, 106, 1), (24, 90), (6, 100, 1)])),
             L(outline([(56, -8), (98, 6), (118, 40), (110, 84), (70, 96), (66, 40)]), 'shade', 'b', False)],
}
# Ekadel: melena azul marino lisa con raya a un lado que le cae recta hasta los hombros; cara alargada, ojos azules de sueño y
# la boca seria
CHARS['ekadel'] = {
    'body': 'delgado', 'pal': pal('#2a4a9a', '#fce0c0', iris='#2a4a8a', shade='#1e3878'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': [(16, 80), (18, 50), (30, 36), (44, 32), (60, 38), (76, 40), (82, 50), (84, 80)]},
    'front': longhair('front', 118, 0, top=-4) + [strand([(42, 0), (36, 36)], 'shade', 'b', 1.2)]
             + [L(rope((18, 50), (16, 80), (20, 116), 6), 'mid', 'f', ln=True), L(rope((82, 50), (84, 80), (80, 116), 6), 'mid', 'f', ln=True)],
    'side': longhair('side', 118, 0, top=-4),
    'back': longhair('back', 110, 0, top=-4, ends=0) + [strand([(x, 0), (x, 108)], 'shade', 'b', 1.0) for x in (30, 50, 70)],
}
# Lephiel: un gorro blanco redondo y ajustado sobre una melena verde oliva que le cae a los lados y le tapa un ojo; el otro
# ojo verde de sueño y una media sonrisa
CHARS['lephiel'] = {
    'body': 'normal', 'pal': pal('#5a6a24', '#fcd8b0', iris='#6a8a3a', shade='#42501a', cap='#f4ecec', cap_d='#d0c4c4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 108, 10, top=4)
             + [L(outline([(14, 66), (16, 44), (34, 34), (54, 32), (72, 36), (84, 46), (86, 66), (76, 56), (64, 54), (52, 64), (44, 84, 1), (38, 66), (26, 70)]), 'mid', 'f', ln=True),
                L(outline([(12, 44), (8, 18), (24, -2), (50, -8), (76, -2), (92, 18), (88, 44), (50, 40)]), 'cap', 'f', ln=True),
                L(outline([(56, -4), (80, 4), (92, 24), (88, 42), (70, 38)]), 'cap_d', 'f', False)],
    'side': longhair('side', 106, 8, top=4) + [L(rope((20, 50), (4, 70), (-2, 96), 10), 'mid', 'f', ln=True),
                                                L(outline([(10, 44), (8, 18), (26, -4), (54, -8), (80, 2), (94, 22), (90, 44), (50, 40)]), 'cap', 'f', ln=True)],
    'back': longhair('back', 100, 10, top=4, ends=3) + [L(outline([(8, 46), (6, 18), (24, -4), (50, -10), (76, -4), (94, 18), (92, 46), (50, 44)]), 'cap', 'f', ln=True),
                                                         L(outline([(56, -6), (80, 2), (94, 24), (92, 44), (66, 42)]), 'cap_d', 'f', False)],
}
# Sachinel: calvo de cabeza redonda con un moño morado enorme en forma de gota que se curva hacia un lado, atado con una
# anilla dorada; ojos negros redondos de loco con pupila de diana y una sonrisa de dientes
CHARS['sachinel'] = {
    'body': 'bajito', 'pal': pal('#9a7ab8', '#fcd0a8', shade='#7a5a9a', ring='#e8b020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + [L(outline([(44, 8), (34, -2), (32, -20), (44, -32), (58, -32), (66, -26), (58, -24), (64, -14), (60, -2), (56, 8)]), 'mid', 'f', ln=True),
                              L(outline([(52, -28), (60, -26), (60, -10), (54, 0)]), 'shade', 'f', False), L(ell(50, 8, 7, 3), 'ring', 'f', ln=True),
                              L(ell(32, 74, 9, 9), (60, 30, 50, 255), 'f', ln=True), L(ell(68, 74, 9, 9), (60, 30, 50, 255), 'f', ln=True),
                              L(ell(32, 74, 6, 6), WHITE, 'f', False), L(ell(68, 74, 6, 6), WHITE, 'f', False),
                              L(ell(32, 74, 3, 3), OUTC, 'f', False), L(ell(68, 74, 3, 3), OUTC, 'f', False),
                              L(outline([(32, 94), (50, 98), (68, 94), (62, 106), (38, 106)]), WHITE, 'f', ln=True)],
    'side': bald('side') + [L(outline([(42, 6), (34, -8), (40, -26), (58, -32), (70, -22), (62, -12), (58, 6)]), 'mid', 'f', ln=True), L(ell(50, 6, 7, 3), 'ring', 'f', ln=True),
                            L(ell(86, 74, 5, 8), (60, 30, 50, 255), 'f', ln=True), L(ell(88, 74, 2.4, 3), OUTC, 'f', False)],
    'back': bald('back') + [L(outline([(44, 8), (34, -2), (30, -20), (44, -32), (62, -32), (70, -20), (62, -2), (56, 8)]), 'mid', 'f', ln=True), L(ell(50, 8, 7, 3), 'ring', 'f', ln=True)],
}
# Wenel: pelo rubio dorado muy abultado en mechones como llamas que se abren hacia arriba y a los lados; ojos violetas de
# enfado y la boca seria
CHARS['wenel'] = {
    'body': 'normal', 'pal': pal('#f0cc60', '#fcdcc0', iris='#6a3a8a', shade='#c8a040', light='#fff0b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 9, seed=1901, rx=58, ry=48, cy=38, lo=80)
             + [L(outline([(10, 74, 1), (14, 42), (30, 26), (50, 20), (70, 26), (86, 42), (90, 74, 1), (80, 58), (72, 64, 1), (64, 50), (56, 58, 1), (50, 48), (44, 58, 1), (36, 50), (28, 64, 1),
                           (20, 56)]), 'mid', 'f'),
                L(outline([(30, 30), (48, 24), (40, 34)]), 'light', 'f', False)],
    'side': messy('side', 14, 8, seed=1901, rx=54, ry=48, cy=38, nape=96, sweep=-0.3),
    'back': messy('back', 12, 9, seed=1901, rx=58, ry=48, cy=38, nape=98),
}
# Nuel: una capucha blanca ajustada y puntiaguda que le cubre toda la cabeza, con un mechón naranja que asoma en la frente;
# cara redonda, ojos grandes, coloretes y una sonrisa
CHARS['nuel'] = {
    'body': 'bajito', 'pal': pal('#e8862a', '#fce4c0', iris='#4a3a2a', hood='#f4ecec', hood_d='#d0c4c4', blush='#f0a080'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(2, 104), (-2, 60), (10, 20), (36, -2), (50, -24, 1), (64, -2), (90, 20), (102, 60), (98, 104), (84, 100), (84, 60), (70, 46), (50, 42), (30, 46), (16, 60), (16, 100)]),
                'hood', 'f', ln=True),
              L(outline([(58, -6), (88, 22), (100, 62), (96, 102), (86, 98), (84, 56)]), 'hood_d', 'f', False),
              L(outline([(44, 50), (50, 34), (60, 40), (56, 54), (50, 46)]), 'mid', 'f', ln=True),
              L(ell(24, 88, 5, 3), 'blush', 'f', False), L(ell(76, 88, 5, 3), 'blush', 'f', False)],
    'side': [L(outline([(60, 104), (8, 104), (0, 60), (10, 20), (34, -4), (40, -26, 1), (60, 0), (82, 16), (94, 40), (90, 58), (76, 48), (64, 56), (60, 80)]), 'hood', 'f', ln=True),
             L(outline([(4, 50), (36, 50), (52, 100), (10, 100)]), 'hood_d', 'f', False), L(ell(78, 88, 4, 3), 'blush', 'f', False)],
    'back': [L(outline([(2, 104), (-2, 60), (10, 20), (36, -2), (50, -24, 1), (64, -2), (90, 20), (102, 60), (98, 104), (50, 108)]), 'hood', 'f', ln=True),
             L(outline([(56, -10), (88, 20), (100, 62), (96, 102), (60, 106)]), 'hood_d', 'f', False)],
}
# Ientel: pelo dorado oscuro en una forma de cuerno enorme y retorcido que sale de un lado de la cabeza y se curva hacia el
# otro como un cruasán; ojos turquesa de pasmo y una sonrisa
CHARS['ientel'] = {
    'body': 'normal', 'pal': pal('#d0a020', '#fcd8b0', iris='#2a9aa0', shade='#a07a14'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(-24, 60, 1), (-8, 44), (4, 24), (20, 6), (46, -10), (74, -8), (94, 6), (106, 24), (126, 34, 1), (100, 44), (90, 60), (80, 50), (60, 44), (40, 50), (20, 56)])),
              L(outline([(60, -6), (92, 8), (104, 28), (118, 36, 1), (96, 42), (84, 30)]), 'shade', 'b', False)]
             + [strand([(x, -6 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 46)], 'shade', 'b', 1.2) for x in (20, 40, 60, 80)]
             + white_eyes(76, 14, 6.4, 6.4, 2.6),
    'side': [L(outline([(44, 92), (22, 88), (10, 70), (2, 40), (14, 8), (46, -8), (76, 0), (94, 16), (98, 40), (86, 54), (70, 50), (58, 56), (52, 70), (50, 80)])),
             L(outline([(4, 40), (34, 40), (42, 80), (20, 86)]), 'shade', 'b', False)] + side_eye(76),
    'back': [L(outline([(-24, 60, 1), (-8, 44), (4, 24), (20, 6), (46, -10), (74, -8), (94, 6), (106, 24), (126, 34, 1), (100, 44), (88, 80), (50, 86), (12, 80)])),
             L(outline([(56, -6), (92, 8), (104, 28), (118, 36, 1), (94, 46), (84, 78), (64, 84)]), 'shade', 'b', False)],
}
# Gaiel: pelo rubio crema recogido con dos trenzas que le rodean la cabeza como una corona y el resto suelto por detrás en una
# melena lisa; cara pálida, ojos grises y una sonrisa
CHARS['gaiel'] = {
    'body': 'normal', 'pal': pal('#e8e0b8', '#fce8d8', iris='#5a5a6a', shade='#c0b890', braid='#d8cca0'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': (50, 40)},
    'front': longhair('front', 100, 4)
             + [L(quad((14, 44), (50, 20), (86, 44)), 'braid', 'f', False, False, 6), L(quad((14, 44), (50, 20), (86, 44)), OUTC, 'f', False, False, 0.6)]
             + [L(ell(14 + k * 8.8, 44 - 22 * (1 - ((14 + k * 8.8 - 50) / 36) ** 2) * 0.95, 3, 2.4), 'shade', 'f', False) for k in range(9)],
    'side': longhair('side', 100, 4) + [L(quad((10, 50), (40, 16), (86, 30)), 'braid', 'f', False, False, 6)],
    'back': longhair('back', 100, 4, ends=0) + [L(quad((8, 44), (50, 30), (92, 44)), 'braid', 'f', False, False, 6)]
            + [strand([(x, 0), (x, 96)], 'shade', 'b', 1.0) for x in (24, 40, 60, 76)],
}
# Sanctus: pelo rojo peinado hacia atrás en surcos con un pico muy marcado en la frente, recogido en una trenza larga que le
# cae por la espalda; ojos azules de enfado y una media sonrisa
CHARS['sanctus'] = {
    'body': 'normal', 'pal': pal('#c02a1e', '#fcd8b0', iris='#2a8ab0', shade='#901e14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(14, 66), (16, 40), (30, 36), (40, 44), (50, 56), (60, 44), (70, 36), (84, 40), (86, 66)]},
    'front': [L(outline([(12, 70), (8, 30), (20, 6), (50, -2), (80, 6), (92, 30), (88, 70), (82, 60), (18, 60)])),
              L(outline([(60, 2), (84, 14), (92, 40), (86, 66), (76, 36)]), 'shade', 'b', False)]
             + [strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 40)], 'shade', 'b', 1.2) for x in (30, 50, 70)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 30), (22, 6), (52, -2), (80, 6), (92, 24), (90, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)]
            + [L(ell(10 - k * 4, 40 + k * 12, 6, 7), 'mid', 'b', ln=True) for k in range(6)],
    'back': [L(outline([(12, 84), (8, 30), (20, 6), (50, -2), (80, 6), (92, 30), (88, 84), (50, 90)])),
             L(outline([(56, 2), (84, 14), (92, 44), (88, 82), (64, 88)]), 'shade', 'b', False), strand([(50, 0), (50, 60)], 'shade', 'b', 1.2)]
            + [L(ell(50, 60 + k * 11, 7, 7), 'mid', 'f', ln=True) for k in range(6)],
}
