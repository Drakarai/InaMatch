"""Secundaria South Cirrus (vr-nagumohara, Nagumohara): el equipo protagonista de Inazuma Eleven: Victory Road, con sus
modelos 3D de la enciclopedia (英雄たちのヴィクトリーロード) como referencia. Cada uno tiene un solo modelo (en la enciclopedia
salen con el uniforme del colegio; la equipación es la de la wiki: camiseta blanca con la ola azul, pantalón azul y medias
azules; el portero de morado). Ningún id coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_keizen_arashiyama import WHITE, cloud, fr, lash_side, lashes
from chars_vr_meiran_gakuin import back_cap, back_shade, bangs, cap, cap_shade, long_back, long_front, long_side, side_cap
from heads import quad  # noqa: F401

BLUSH = (244, 168, 150, 255)


def blush(y=86, x=27, w=4.4):
    return [L(ell(x, y, w, 2.4), BLUSH, 'f', False), L(ell(100 - x, y, w, 2.4), BLUSH, 'f', False)]


# Alix La Fontaine (Shisendou Garyuu, portero): pelo celeste muy claro, largo y liso hasta el pecho, peinado hacia atrás y
# a un lado con un gran mechón que le cruza la frente; mechones finos le caen delante de las orejas; ojos violeta y sonrisa
CHARS['alix-la-fontaine'] = {
    'body': 'delgado', 'pal': pal('#bfe2ec', '#fce8dc', iris='#5a4aa8', shade='#9ac0cc', deep='#7a9aa8'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (24, 46), (36, 40), (52, 38), (68, 40), (80, 46), (86, 58), (88, 76)]},
    'front': long_front(124, 4) + [
              cap(2, 44, 62, 4), cap_shade(2),
              L(outline([(14, 50), (20, 26), (40, 14), (62, 12), (80, 20), (60, 26), (40, 34), (24, 48)]), 'light', 'b', False),
              L(quad((20, 64), (18, 92), (14, 118)), 'mid', 'f', False, False, 2.0), L(quad((80, 64), (82, 92), (86, 118)), 'mid', 'f', False, False, 2.0)],
    'side': [side_cap(0, 62, (2, 70)), long_side(126, -8),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(40, 4), (70, 10), (88, 26), (70, 22), (46, 18)]), 'light', 'b', False),
             L(quad((58, 62), (58, 92), (56, 118)), 'mid', 'f', False, False, 2.0)],
    'back': [long_back(126, 4, 4), back_shade(2, 118),
             L(outline([(20, 20), (40, 8), (60, 8), (40, 20), (26, 34)]), 'light', 'b', False)],
}

# Cade Shelby (Kodoukai Kameo): grandote de cara enorme y redonda, mofletes rosados; casco de pelo castaño con el flequillo
# recto, y unos cascos de música negros en las orejas con la diadema por detrás; ojos verdes y la boca con los dos dientes
_cade_face = outline([(10, 52), (50, 46), (90, 52), (102, 80), (94, 104), (70, 116), (50, 118), (30, 116), (6, 104), (-2, 80)])
CHARS['cade-shelby'] = {
    'body': 'corpulento', 'pal': pal('#8e623e', '#fcd2b0', iris='#2a8a7a', shade='#704c2e', deep='#523620', phone='#2e2e32', phone_l='#6a6a70'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'buck', 'mouth_y': 98, 'eye_y': 78, 'nose': (50, 86, 2.4), 'face_front': _cade_face, 'ears': False,
             'hairline': False},
    'front': [L(outline([(-4, 66), (-6, 36), (12, 14), (50, 6), (88, 14), (106, 36), (104, 66), (88, 64), (70, 60), (50, 64), (30, 60), (12, 64)]), 'mid', 'f'),
              L(outline([(60, 10), (90, 18), (104, 40), (100, 62), (86, 42)]), 'shade', 'f', False),
              strand([(30, 50), (30, 60)], 'deep', 'f', 1.0), strand([(50, 52), (50, 62)], 'deep', 'f', 1.0), strand([(70, 50), (70, 60)], 'deep', 'f', 1.0),
              L(outline([(-12, 62), (-4, 58), (2, 64), (2, 92), (-4, 96), (-12, 92)]), 'phone', 'f', ln=True),
              L(outline([(112, 62), (104, 58), (98, 64), (98, 92), (104, 96), (112, 92)]), 'phone', 'f', ln=True),
              L(outline([(-10, 70), (-6, 68), (-6, 86), (-10, 86)]), 'phone_l', 'f', False), L(outline([(110, 70), (106, 68), (106, 86), (110, 86)]), 'phone_l', 'f', False)]
             + blush(90, 18, 5),
    'side': [L(outline([(48, 76), (54, 64), (94, 64), (96, 44), (82, 18), (50, 6), (20, 12), (2, 34), (0, 62), (12, 80), (28, 84)])),
             L(outline([(4, 50), (30, 54), (30, 80), (12, 76)]), 'shade', 'b', False),
             L(ell(42, 74, 12, 13), 'phone', 'f', ln=True), L(ell(42, 74, 6, 7), 'phone_l', 'f', False),
             L(quad((32, 66), (16, 58), (4, 70)), 'phone', 'f', False, False, 2.6),
             L(ell(86, 90, 4, 2.6), BLUSH, 'f', False)],
    'back': [L(outline([(2, 80), (-4, 44), (12, 16), (50, 6), (88, 16), (104, 44), (98, 80), (50, 86)])),
             L(outline([(0, 56), (50, 62), (100, 56), (98, 80), (50, 86), (2, 80)]), 'shade', 'b', False),
             L(quad((0, 76), (50, 84), (100, 76)), 'phone', 'f', False, False, 2.8),
             L(outline([(-8, 60), (2, 58), (4, 92), (-6, 94)]), 'phone', 'f', ln=True), L(outline([(108, 60), (98, 58), (96, 92), (106, 94)]), 'phone', 'f', ln=True)],
}

# Winsor Compete (Makushita Teru): grandote; pelo negro corto en casco con la nuca rapada y un moño de sumo en abanico de
# mechones gruesos arriba, una diadema gris fina; cejas negras gruesas y fruncidas, mofletes rosados y una sonrisa ancha
CHARS['winsor-compete'] = {
    'body': 'corpulento', 'pal': pal('#24222c', '#fcd6b6', iris='#2a2a3a', shade='#1a1820', deep='#121016', band='#8a9a9e', nose='#e89a8a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_w': 14, 'mouth_y': 96, 'big_ears': 2, 'ear_out': 4, 'nose': (50, 85, 2.6),
             'face_front': outline([(14, 52), (50, 46), (86, 52), (92, 78), (86, 100), (68, 112), (50, 114), (32, 112), (14, 100), (8, 78)]),
             'hairline': [(12, 66), (16, 54), (30, 50), (44, 50), (50, 58), (56, 50), (70, 50), (84, 54), (88, 66)]},
    'front': [L(outline([(14, 70), (12, 44), (22, 26), (50, 20), (78, 26), (88, 44), (86, 70), (80, 58), (20, 58)])),
              L(outline([(30, 24), (6, 22, 1), (16, 12), (2, 0, 1), (22, 2), (20, -12, 1), (36, -4), (44, -16, 1), (56, -4), (66, -14, 1), (72, 0), (90, -6, 1), (86, 8),
                         (98, 14, 1), (84, 20), (92, 30, 1), (70, 24)])),
              L(quad((14, 56), (50, 48), (86, 56)), 'band', 'f', False, False, 2.2),
              L(outline([(24, 62), (30, 58), (44, 64), (42, 68), (28, 68)]), 'mid', 'f', ln=True), L(outline([(76, 62), (70, 58), (56, 64), (58, 68), (72, 68)]), 'mid', 'f', ln=True)]
             + blush(86, 24, 4.6),
    'side': [L(outline([(54, 62), (60, 50), (82, 44), (88, 30), (70, 18), (40, 16), (18, 24), (6, 44), (8, 66), (20, 80), (36, 80), (46, 72)])),
             L(outline([(40, 18), (30, 0, 1), (20, -2), (16, -16, 1), (34, -12), (40, -20, 1), (50, -8), (54, 6)])),
             L(quad((10, 50), (40, 50), (70, 42)), 'band', 'f', False, False, 2.2),
             L(outline([(72, 62), (82, 58), (88, 64), (76, 68)]), 'mid', 'f', ln=True),
             L(ell(84, 86, 4, 2.4), BLUSH, 'f', False)],
    'back': [L(outline([(14, 82), (10, 44), (20, 22), (50, 16), (80, 22), (90, 44), (86, 82), (50, 88)])),
             L(outline([(32, 22), (6, 22, 1), (16, 12), (2, 0, 1), (22, 2), (20, -12, 1), (36, -4), (44, -16, 1), (56, -4), (66, -14, 1), (72, 0), (90, -6, 1), (86, 8),
                        (98, 14, 1), (84, 20), (94, 30, 1), (68, 24)])),
             L(outline([(58, 20), (82, 26), (90, 46), (86, 80), (64, 86)]), 'shade', 'b', False),
             L(quad((12, 52), (50, 62), (88, 52)), 'band', 'f', False, False, 2.2)],
}

# Charis Benzaie (Benten Kuroumaru): casco de pelo morado lila liso y redondo, con el flequillo largo de lado que le tapa
# el ojo derecho y los lados hasta la mandíbula; ojo azul con pestañas y una sonrisa
CHARS['charis-benzaie'] = {
    'body': 'normal', 'pal': pal('#9a62a8', '#fce4d4', iris='#3a7ac8', shade='#7c4a8a', deep='#5e346a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 80), (16, 58), (26, 50), (40, 48), (60, 46), (76, 50), (84, 58), (88, 80)]},
    'front': [L(outline([(12, 92), (4, 56), (10, 26), (28, 8), (50, 2), (72, 8), (90, 26), (96, 56), (88, 92), (82, 80), (82, 64), (18, 64), (18, 80)])),
              L(outline([(60, 4), (84, 16), (96, 46), (90, 80), (80, 44)]), 'shade', 'b', False),
              strand([(36, 6), (30, 30)], 'deep', 'b', 1.0), strand([(60, 4), (64, 30)], 'deep', 'b', 1.0),
              fr([(12, 66), (12, 42), (28, 28), (50, 24), (68, 30), (80, 50), (84, 70), (78, 90, 1), (70, 76), (62, 64), (52, 54), (40, 50), (26, 54), (18, 70, 1)])] + lashes(),
    'side': [L(outline([(54, 66), (58, 54), (72, 52), (80, 62), (86, 72), (92, 52), (92, 26), (78, 6), (50, -2), (22, 6), (4, 30), (2, 62), (8, 88), (26, 96), (40, 90),
                        (48, 80)])),
             L(outline([(2, 56), (30, 60), (40, 90), (26, 96), (8, 88)]), 'shade', 'b', False),
             L(outline([(56, 56), (64, 66), (64, 92, 1), (58, 76)]), 'mid', 'f')],
    'back': [L(outline([(8, 92), (4, 56), (10, 26), (28, 8), (50, 2), (72, 8), (90, 26), (96, 56), (92, 92), (50, 96)])),
             L(outline([(4, 60), (50, 66), (96, 60), (92, 92), (50, 96), (8, 92)]), 'shade', 'b', False)],
}

# Amelia Rainwalker (Udou Mirika): pelo azul marino oscuro largo y liso con raya a un lado, recogido por detrás con una
# pinza plateada y suelto hasta el pecho; una franja rosa le cruza el pelo a un lado de la cara; ojos verdes con una
# pinza de estrellitas, pecas y sonrisa
CHARS['amelia-rainwalker'] = {
    'body': 'chica', 'pal': pal('#2c4a64', '#fce4d4', iris='#4a9a5a', shade='#223a50', deep='#18283a', pink='#f0a0a0', clip='#c0c4c8'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (24, 46), (34, 38), (44, 34), (58, 38), (74, 46), (84, 58), (88, 76)]},
    'front': long_front(120, 4) + [
              cap(2, 44, 62, 4), cap_shade(2), strand([(42, 4), (44, 34)], 'deep', 'b', 1.2),
              fr([(56, 36), (74, 44), (86, 58), (90, 84), (86, 104, 1), (80, 76), (70, 56)]),
              L(quad((74, 76), (84, 70), (92, 80)), 'pink', 'f', False, False, 2.6),
              L(ell(26, 68, 1.4, 1.4), 'clip', 'f', ln=True), L(ell(30, 66, 1.4, 1.4), 'clip', 'f', ln=True),
              L(ell(32, 86, 0.8, 0.8), (190, 120, 90, 255), 'f', False), L(ell(36, 88, 0.8, 0.8), (190, 120, 90, 255), 'f', False),
              L(ell(68, 86, 0.8, 0.8), (190, 120, 90, 255), 'f', False)] + lashes(dx=7.6),
    'side': [side_cap(0, 62, (2, 70)), long_side(120, -6),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(outline([(24, 6), (30, 0), (36, 10), (30, 14)]), 'clip', 'b', ln=True),
             L(quad((70, 76), (80, 70), (88, 78)), 'pink', 'f', False, False, 2.4)] + lash_side(),
    'back': [long_back(120, 4, 4), back_shade(2, 112),
             strand([(20, 30), (40, 50), (46, 56)], 'deep', 'b', 1.2), strand([(80, 30), (60, 50), (54, 56)], 'deep', 'b', 1.2),
             L(outline([(44, 52), (56, 52), (54, 62), (46, 62)]), 'clip', 'f', ln=True)],
}

# Cedric Freud (Kisoji Heita): pelo castaño muy oscuro corto, ahuecado y en puntas hacia los lados, con una bola de pelo
# (moñito) arriba y un mechón más claro a un lado de la frente; ojos marrones y una sonrisa
CHARS['cedric-freud'] = {
    'body': 'normal', 'pal': pal('#40261e', '#fcdcc4', iris='#8a5a2a', shade='#301c16', deep='#20120e', lite='#7a5a4a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 60), (24, 50), (40, 44), (50, 50), (60, 44), (76, 48), (84, 58), (88, 76)]},
    'front': [L(ell(54, -4, 10, 9)), L(quad((50, 4), (52, 10), (50, 16)), 'mid', 'b', True, False, 3),
              L(outline([(14, 78), (2, 84, 1), (8, 70), (-8, 62, 1), (8, 54), (4, 36), (16, 16), (38, 6), (62, 6), (84, 16), (96, 36), (92, 54), (108, 62, 1), (92, 70),
                         (98, 84, 1), (86, 78), (82, 62), (18, 62)])),
              L(outline([(58, 8), (84, 18), (96, 40), (92, 70), (80, 44)]), 'shade', 'b', False),
              fr([(60, 44), (72, 42), (82, 50), (86, 70), (80, 60), (72, 52)], 'lite'),
              strand([(48, 10), (46, 26)], 'deep', 'b', 1.0)],
    'side': [L(ell(48, -8, 9, 9)),
             L(outline([(54, 62), (58, 50), (80, 44), (92, 32), (90, 12), (70, 0), (40, 0), (18, 10), (4, 30), (-10, 40, 1), (4, 50), (-8, 62, 1), (6, 66), (0, 82, 1),
                        (16, 80), (20, 92, 1), (30, 82), (44, 78), (48, 70)])),
             L(outline([(4, 40), (24, 46), (28, 78), (10, 76)]), 'shade', 'b', False)],
    'back': [L(ell(50, -6, 10, 9)),
             L(outline([(14, 82), (2, 88, 1), (8, 72), (-8, 62, 1), (8, 54), (4, 36), (16, 16), (38, 6), (62, 6), (84, 16), (96, 36), (92, 54), (108, 62, 1), (92, 72),
                        (98, 88, 1), (86, 82), (74, 90, 1), (62, 82), (50, 92, 1), (38, 82), (26, 90, 1)])),
             L(outline([(58, 8), (84, 18), (96, 40), (92, 80), (64, 86)]), 'shade', 'b', False)],
}

# Destin Billows (Sasanami Unmei): media melena verde azulado con raya a un lado, lisa y que se abre en las puntas, que
# acaban en turquesa claro a la altura de la barbilla; cejas gruesas, ojos azul oscuro y una sonrisa
CHARS['destin-billows'] = {
    'body': 'normal', 'pal': pal('#2e8070', '#fcdcc4', iris='#22306a', shade='#22665a', deep='#184c42', tip='#4ae0c8'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 56), (24, 44), (36, 36), (44, 32), (56, 36), (74, 44), (84, 56), (88, 76)]},
    'front': [L(outline([(16, 58), (4, 84), (0, 104, 1), (10, 98), (14, 108, 1), (22, 94), (24, 80)])), L(outline([(84, 58), (96, 84), (100, 104, 1), (90, 98), (86, 108, 1), (78, 94), (76, 80)])),
              L(outline([(4, 86), (0, 104, 1), (10, 98), (14, 108, 1), (22, 94), (20, 86)]), 'tip', 'b', False),
              L(outline([(96, 86), (100, 104, 1), (90, 98), (86, 108, 1), (78, 94), (80, 86)]), 'tip', 'b', False),
              cap(2, 44, 62, 4), cap_shade(2), strand([(44, 4), (44, 32)], 'deep', 'b', 1.2)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (2, 36), (0, 66), (-6, 90), (2, 100, 1), (12, 92), (22, 102, 1),
                        (30, 92), (40, 102, 1), (44, 84), (50, 72)])),
             L(outline([(-4, 84), (2, 100, 1), (12, 92), (22, 102, 1), (30, 92), (40, 102, 1), (42, 86)]), 'tip', 'b', False),
             L(outline([(4, 40), (26, 46), (30, 82), (8, 82)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 82), (6, 42), (16, 16), (40, 2), (60, 2), (84, 16), (94, 42), (92, 82), (104, 100, 1), (90, 96), (80, 106, 1), (66, 98), (50, 106, 1),
                        (34, 98), (20, 106, 1), (10, 96), (-4, 100, 1)])),
             L(outline([(4, 80), (50, 86), (96, 80), (104, 100, 1), (90, 96), (80, 106, 1), (66, 98), (50, 106, 1), (34, 98), (20, 106, 1), (10, 96), (-4, 100, 1)]),
               'tip', 'b', False),
             back_shade(2, 84)],
}

# Thierry Reyes (Yagyuu Suruga): piel tostada; pelo rubio dorado muy largo y liso peinado hacia atrás, con mechones finos
# trenzados que le caen delante de las orejas y un tocado de plumas (negra, blanca y roja) a un lado; ojos azul oscuro y
# media sonrisa
CHARS['thierry-reyes'] = {
    'body': 'normal', 'pal': pal('#f0c46a', '#d29a72', iris='#2a3a6a', shade='#d4a44e', deep='#b08436', fw='#f2ece4', fb='#2a2222', fr='#c8401e'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 56), (24, 42), (40, 34), (52, 36), (66, 40), (78, 46), (86, 58), (88, 76)]},
    'front': long_front(128, 2) + [
              cap(2, 44, 62, 2), cap_shade(2),
              L(rope((50, 22), (78, 4), (106, 12), 7), 'fw', 'f'), L(rope((52, 18), (66, 2), (84, -6), 5), 'fb', 'f'),
              L(rope((62, 30), (76, 50), (84, 80), 6), 'fr', 'f'),
              strand([(44, 36), (40, 60), (46, 84)], 'deep', 'f', 1.0),
              L(rope((20, 64), (18, 96), (20, 122), 3.2)), L(rope((80, 64), (82, 96), (80, 122), 3.2))],
    'side': [side_cap(0, 62, (2, 70)), long_side(130, -8),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 84)]), 'shade', 'b', False),
             L(rope((56, 14), (66, -4), (82, -12), 5), 'fb', 'f'), L(rope((50, 18), (30, 6), (8, 8), 6), 'fw', 'f'),
             L(rope((58, 62), (58, 96), (60, 124), 3.2))],
    'back': [long_back(130, 2, 4), back_shade(2, 122),
             L(rope((62, 20), (90, 10), (116, 18), 7), 'fw', 'f'), L(rope((60, 16), (74, 0), (88, -8), 5), 'fb', 'f'),
             L(rope((70, 26), (84, 50), (92, 84), 6), 'fr', 'b')],
}

# Raika Shinohara (Shinohara Raika): pelo rojo coral recogido en una coleta altísima con una goma oscura que cae larga por
# detrás; flequillo de mechones y dos mechones largos que le enmarcan la cara y se curvan hacia dentro bajo la barbilla, con
# las puntas amarillas; ojos granate con pestañas y una sonrisa
CHARS['raika-shinohara'] = {
    'body': 'chica', 'pal': pal('#ee6a62', '#fce4d4', iris='#9a2a2a', shade='#cc504a', deep='#a03a36', tip='#f0c44a', tie='#2a2230'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 50), (36, 56), (44, 46), (52, 54), (60, 46), (70, 54), (78, 50), (86, 60), (88, 76)]},
    'front': [L(outline([(16, 62), (8, 80), (2, 96), (8, 106), (20, 104, 1), (12, 98), (16, 86), (24, 76)])),
              L(outline([(84, 62), (92, 80), (98, 96), (92, 106), (80, 104, 1), (88, 98), (84, 86), (76, 76)])),
              L(outline([(4, 86), (2, 96), (8, 106), (12, 98), (10, 88)]), 'tip', 'b', False), L(outline([(96, 86), (98, 96), (92, 106), (88, 98), (90, 88)]), 'tip', 'b', False),
              L(outline([(40, 10), (34, -8), (44, -18), (56, -18), (66, -8), (60, 10)])),
              L(ell(50, 10, 8, 3), 'tie', 'b', False),
              cap(4, 44, 62, 2), cap_shade(4),
              fr([(14, 62), (16, 42), (30, 32), (50, 28), (70, 32), (84, 42), (86, 62), (78, 52), (70, 60, 1), (64, 48), (54, 58, 1), (50, 46), (42, 58, 1), (36, 48),
                  (26, 58, 1)])] + lashes(dx=7.6),
    'side': [L(outline([(42, 0), (30, -18), (10, -14), (-14, 10), (-30, 60), (-40, 110, 1), (-22, 70), (-4, 30), (14, 8), (34, 6)])),
             L(ell(36, 0, 3, 6), 'tie', 'b', False),
             side_cap(2, 62, (4, 66)),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(64, 46), (72, 58), (76, 90), (66, 104, 1), (70, 88), (64, 70)]), 'mid', 'f'),
             L(outline([(72, 82), (76, 90), (66, 104, 1), (70, 90)]), 'tip', 'f', False)] + lash_side(),
    'back': [back_cap(4, 84), back_shade(4, 84),
             L(outline([(16, 62), (8, 80), (2, 96), (8, 106), (20, 104, 1), (16, 86), (24, 76)])), L(outline([(84, 62), (92, 80), (98, 96), (92, 106), (80, 104, 1), (84, 86), (76, 76)])),
             L(outline([(42, 10), (36, -10), (46, -20), (58, -16), (64, 0), (62, 30), (66, 80), (60, 120, 1), (52, 80), (50, 30)])),
             L(ell(52, 6, 8, 3), 'tie', 'f', False)],
}

# Briar Bloomhurst (Sakurazaki Jouji): piel morena; pelo malva rosado muy revuelto en mechones gruesos que se enroscan
# hacia fuera, con la nuca y los lados oscuros rapados y un mechón que le cae entre los ojos; ojos azul hielo entornados con
# la raya negra y una media sonrisa
CHARS['briar-bloomhurst'] = {
    'body': 'normal', 'pal': pal('#b07aa8', '#9a5e3e', iris='#5aa0b0', shade='#8e5e88', deep='#6e4468', dark='#2a2028'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 66), (18, 54), (32, 50), (50, 52), (68, 50), (82, 54), (88, 66)]},
    'front': [L(outline([(14, 70), (12, 44), (22, 26), (78, 26), (88, 44), (86, 70), (80, 56), (20, 56)]), 'dark'),
              L(outline([(16, 54), (2, 50, 1), (8, 40), (-10, 30, 1), (8, 24), (0, 4, 1), (20, 10), (24, -10, 1), (38, 2), (46, -16, 1), (56, 0), (68, -10, 1), (74, 6),
                         (96, 2, 1), (88, 18), (108, 26, 1), (92, 36), (100, 50, 1), (84, 54), (74, 46), (60, 50), (50, 44), (40, 50), (26, 46)])),
              L(outline([(58, 2), (68, -8), (74, 6), (92, 6), (88, 22), (98, 36), (84, 50), (76, 36)]), 'shade', 'b', False),
              strand([(30, 14), (36, 30)], 'deep', 'b', 1.2), strand([(64, 12), (60, 30)], 'deep', 'b', 1.2),
              fr([(44, 42), (56, 42), (54, 58), (48, 74, 1), (46, 56)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 44), (88, 30), (70, 20), (40, 20), (18, 28), (6, 48), (8, 70), (22, 84), (38, 82), (46, 72)]), 'dark'),
             L(outline([(14, 38), (-4, 32, 1), (8, 22), (0, 6, 1), (20, 8), (22, -12, 1), (40, 0), (52, -16, 1), (60, 0), (80, -10, 1), (80, 8), (100, 10, 1), (90, 22),
                        (104, 36, 1), (88, 40), (72, 34), (52, 38), (30, 36)])),
             L(outline([(70, 34), (84, 40), (88, 56, 1), (78, 46)]), 'mid', 'f')],
    'back': [L(outline([(14, 82), (10, 44), (22, 24), (78, 24), (90, 44), (86, 82), (50, 88)]), 'dark'),
             L(outline([(16, 58), (2, 54, 1), (8, 42), (-10, 32, 1), (8, 24), (0, 4, 1), (20, 10), (24, -10, 1), (38, 2), (48, -16, 1), (56, 0), (68, -10, 1), (74, 6),
                        (98, 2, 1), (88, 18), (108, 28, 1), (92, 38), (102, 54, 1), (84, 58), (70, 52, 1), (60, 60), (50, 50, 1), (40, 60), (30, 52, 1)])),
             L(outline([(58, 2), (90, 6), (96, 40), (84, 56), (70, 48)]), 'shade', 'b', False)],
}

# Marisol Cavallo (Imasato Himana): melena gris oscura lisa en corte bob hasta la mandíbula, con flequillo recto; ojos
# ámbar con pestañas, pecas de puntitos bajo los ojos y la boca seria
CHARS['marisol-cavallo'] = {
    'body': 'chica', 'pal': pal('#5e5c62', '#fcece4', iris='#b08a2a', shade='#4a484e', deep='#36343a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(8, 98), (4, 56), (10, 24), (28, 6), (50, 0), (72, 6), (90, 24), (96, 56), (92, 98), (80, 100), (80, 64), (20, 64), (20, 100)])),
              L(outline([(60, 2), (84, 14), (96, 46), (92, 96), (82, 64)]), 'shade', 'b', False),
              bangs(64, 16, 84, 6, 30, 'mid', 0),
              L(ell(30, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(34, 88, 0.9, 0.9), OUTC, 'f', False),
              L(ell(70, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(66, 88, 0.9, 0.9), OUTC, 'f', False)] + lashes(),
    'side': [L(outline([(54, 66), (58, 54), (72, 52), (80, 62), (86, 68), (94, 52), (92, 24), (76, 4), (50, -4), (22, 4), (2, 30), (0, 70), (4, 100), (40, 104), (46, 86)])),
             L(outline([(2, 60), (30, 64), (44, 100), (4, 100)]), 'shade', 'b', False)] + lash_side(),
    'back': [L(outline([(6, 100), (2, 56), (10, 24), (28, 6), (50, 0), (72, 6), (90, 24), (98, 56), (94, 100), (50, 104)])),
             L(outline([(58, 2), (84, 14), (98, 50), (94, 100), (64, 104)]), 'shade', 'b', False)],
}

# Maine Alsop (Iseya Kaname): pelo negro ondulado en media melena con raya en medio, que se abre en mechones a la altura
# de la mandíbula; gafas cuadradas moradas oscuras, ojos turquesa y la boca seria
CHARS['maine-alsop'] = {
    'body': 'normal', 'pal': pal('#1e1c22', '#fce4d4', iris='#3a9aa0', shade='#16141a', deep='#0e0c10'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'frown', 'mouth_y': 95, 'glasses': (60, 40, 80, 255), 'glasses_rect': True,
             'hairline': [(12, 76), (16, 56), (26, 44), (40, 38), (50, 30), (60, 38), (74, 44), (84, 56), (88, 76)]},
    'front': [L(outline([(16, 58), (4, 82), (8, 96), (0, 108, 1), (14, 102), (22, 108, 1), (24, 86)])), L(outline([(84, 58), (96, 82), (92, 96), (100, 108, 1), (86, 102), (78, 108, 1), (76, 86)])),
              cap(2, 44, 62, 4), cap_shade(2), strand([(50, 4), (50, 30)], 'light', 'b', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (2, 36), (0, 70), (-6, 90), (4, 104, 1), (14, 94), (24, 104, 1),
                        (32, 92), (44, 82), (50, 72)])),
             L(outline([(4, 40), (26, 46), (30, 82), (8, 82)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 84), (6, 42), (16, 16), (40, 2), (60, 2), (84, 16), (94, 42), (92, 84), (100, 102, 1), (84, 96), (72, 106, 1), (60, 96), (50, 104, 1), (40, 96),
                        (28, 106, 1), (16, 96), (0, 102, 1)])),
             back_shade(2, 90)],
}

# Dario Highton (Itadaki Idomu): pelo verde hierba peinado en un tupé alto que se riza hacia arriba en la punta, con los
# lados cortos rubios verdosos; un mechón le cae a un lado de la frente; cejas verdes, ojos marrones, mofletes sonrosados
# y una sonrisa de dientes
CHARS['dario-highton'] = {
    'body': 'bajito', 'pal': pal('#6ab048', '#fcdcc4', iris='#5a3a2a', shade='#4e8c34', deep='#386a24', side='#c8c062', side_d='#a49a48'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'big_ears': 2, 'ear_out': 3,
             'hairline': [(12, 66), (16, 54), (28, 48), (44, 46), (56, 46), (72, 48), (84, 54), (88, 66)]},
    'front': [L(outline([(14, 70), (12, 44), (22, 28), (78, 28), (88, 44), (86, 70), (80, 56), (20, 56)]), 'side'),
              L(outline([(20, 50), (18, 30), (30, 12), (44, 0), (52, -16), (62, -26, 1), (60, -10), (74, 0), (84, 16), (84, 34), (80, 50), (70, 40), (54, 48), (36, 44)])),
              L(outline([(56, -8), (74, 2), (84, 18), (84, 36), (74, 24)]), 'shade', 'b', False),
              strand([(40, 14), (54, 2), (60, -12)], 'deep', 'b', 1.2), strand([(30, 26), (46, 16)], 'deep', 'b', 1.2),
              fr([(56, 44), (66, 46), (70, 60), (64, 76, 1), (62, 58)]),
              L(outline([(24, 64), (30, 60), (42, 64), (40, 68), (28, 68)]), 'mid', 'f', ln=True), L(outline([(76, 64), (70, 60), (58, 64), (60, 68), (72, 68)]), 'mid', 'f', ln=True)]
             + blush(86, 26, 4.4),
    'side': [L(outline([(54, 62), (60, 50), (82, 44), (88, 30), (70, 18), (40, 18), (18, 26), (6, 46), (8, 70), (22, 84), (38, 82), (46, 72)]), 'side'),
             L(outline([(6, 50), (30, 56), (46, 72), (38, 82), (22, 84), (8, 70)]), 'side_d', 'b', False),
             L(outline([(30, 30), (40, 10), (56, 0), (64, -20), (76, -30, 1), (70, -12), (86, 0), (94, 20), (90, 40), (74, 34), (52, 30)])),
             L(outline([(76, 34), (86, 44), (84, 64, 1), (78, 48)]), 'mid', 'f'),
             L(ell(84, 86, 4, 2.4), BLUSH, 'f', False)],
    'back': [L(outline([(14, 82), (10, 44), (20, 24), (80, 24), (90, 44), (86, 82), (50, 90)]), 'side'),
             L(outline([(12, 56), (50, 62), (88, 56), (86, 82), (50, 90), (14, 82)]), 'side_d', 'b', False),
             L(outline([(24, 40), (26, 20), (40, 6), (52, -12), (62, -24, 1), (60, -8), (72, 4), (80, 22), (78, 40), (62, 30, 1), (50, 40)])),
             L(outline([(52, 36), (40, 24), (58, 20), (62, 30)]), 'shade', 'b', False)],
}

# Meridia Althoff (Koteuchi Nanami): pelo azul eléctrico corto y revuelto en mechones de punta que salen hacia los lados,
# con un mechón largo que le cae en medio de la cara entre los ojos; ojos turquesa grandes con pestañas y una sonrisa
CHARS['meridia-althoff'] = {
    'body': 'chica', 'pal': pal('#2a2ec0', '#fce4d4', iris='#3ac8d0', shade='#1e2296', deep='#141870'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 50), (40, 46), (60, 46), (74, 50), (84, 58), (88, 76)]},
    'front': [L(outline([(14, 86), (2, 92, 1), (8, 76), (-10, 66, 1), (6, 56), (-10, 40, 1), (8, 32), (16, 12), (40, 2), (64, 2), (86, 14), (94, 32), (110, 40, 1), (94, 56),
                         (110, 66, 1), (92, 76), (98, 92, 1), (86, 86), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (98, 44), (92, 80), (80, 44)]), 'shade', 'b', False),
              fr([(12, 66), (14, 44), (28, 32), (50, 28), (72, 32), (86, 44), (88, 66), (80, 58), (72, 66, 1), (66, 54), (56, 50), (54, 70), (48, 92, 1), (46, 64), (40, 52),
                  (30, 58), (22, 70, 1)])] + lashes(dx=7.6),
    'side': [L(outline([(54, 62), (58, 50), (80, 44), (92, 30), (90, 12), (70, 0), (40, 0), (18, 10), (4, 30), (-12, 40, 1), (4, 52), (-10, 64, 1), (6, 70), (2, 88, 1),
                        (18, 82), (24, 96, 1), (34, 84), (44, 78), (48, 70)])),
             L(outline([(4, 40), (24, 46), (28, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(66, 40), (88, 44), (94, 60), (88, 74, 1), (80, 56)]), 'mid', 'f')] + lash_side(),
    'back': [L(outline([(14, 86), (0, 92, 1), (8, 76), (-10, 66, 1), (6, 56), (-10, 40, 1), (8, 32), (16, 12), (40, 2), (64, 2), (86, 14), (94, 32), (110, 40, 1), (94, 56),
                        (110, 66, 1), (92, 76), (100, 92, 1), (86, 86), (74, 96, 1), (62, 86), (50, 98, 1), (38, 86), (26, 96, 1)])),
             back_shade(2, 90)],
}

# Tai Richter (Banme Saito): pelo azul petróleo casi negro, muy rizado y abultado en una nube de rizos, con mechones que le
# caen sobre la frente; ojos verdes grandes y una sonrisa
CHARS['tai-richter'] = {
    'body': 'normal', 'pal': pal('#20303e', '#fcdcc4', iris='#2a9a6a', shade='#18242e', deep='#101820'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(cloud(50, 40, 54, 50, 10, 0.1)),
              L(cloud(24, 74, 16, 20, 5, 0.3), 'shade', 'b', False), L(cloud(76, 74, 16, 20, 5, 0.6), 'shade', 'b', False),
              fr([(12, 66), (14, 42), (28, 30), (50, 26), (72, 30), (86, 42), (88, 66), (80, 56), (72, 66, 1), (64, 54), (56, 64, 1), (50, 52), (42, 68, 1), (36, 54),
                  (26, 64, 1), (20, 56)])],
    'side': [L(outline([(54, 62), (58, 52), (80, 46), (90, 32), (96, 14), (80, -6), (50, -12), (20, -6), (2, 14), (-8, 44), (-4, 76), (10, 94), (30, 98), (44, 86), (50, 74)])),
             L(cloud(38, 30, 52, 44, 10, 0.2)),
             L(outline([(72, 40), (90, 46), (94, 62, 1), (82, 54)]), 'mid', 'f')],
    'back': [L(cloud(50, 44, 56, 52, 10, 0.1)), L(cloud(50, 80, 34, 16, 6, 0.3), 'shade', 'b', False)],
}

# Davin Bullock (Ushijima Totsugorou): grandullón de cara ancha y cuadrada; pelo rojo oscuro muy rizado y abultado en
# bucles que le forman una corona alrededor de la cabeza; cejas rojas gruesas, nariz triangular y sonrisa ancha
CHARS['davin-bullock'] = {
    'body': 'corpulento', 'pal': pal('#a8282a', '#fcd0a8', iris='#3a2a22', shade='#86181c', deep='#641014', nose='#d89a7a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_w': 14, 'mouth_y': 98,
             'face_front': outline([(12, 52), (50, 46), (88, 52), (92, 80), (86, 104), (66, 112), (50, 114), (34, 112), (14, 104), (8, 80)]),
             'hairline': [(10, 70), (14, 58), (26, 52), (40, 56), (50, 50), (60, 56), (74, 52), (86, 58), (90, 70)]},
    'front': [L(cloud(50, 32, 50, 34, 9, 0.2)), L(cloud(14, 60, 12, 14, 4, 0.3)), L(cloud(86, 60, 12, 14, 4, 0.6)),
              L(cloud(64, 26, 22, 16, 5, 0.4), 'shade', 'b', False),
              L(outline([(50, 82), (45, 90), (55, 90)]), 'nose', 'f', ln=True)],
    'side': [L(cloud(40, 34, 48, 36, 9, 0.2)), L(cloud(14, 70, 14, 16, 4, 0.3)),
             L(cloud(20, 56, 18, 18, 5, 0.6), 'shade', 'b', False)],
    'back': [L(cloud(50, 40, 52, 44, 10, 0.2)), L(cloud(50, 74, 30, 14, 6, 0.3), 'shade', 'b', False)],
}
