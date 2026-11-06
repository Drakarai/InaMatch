"""Oumihara / Instituto Mary Times (IE2): el equipo de Okinawa; gafas de buceo, peinados de playa y caras curtidas,
con sus modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, spiky, spiky_face
from chars_ccc import cap_hair
from chars_otaku import back_hair, glasses
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

DARK = (24, 20, 24, 255)

# Rocky Black (portero): corpulento, morro de jabalí: nariz grande roja, colmillos y pelo castaño corto con dos mechones curvos
CHARS['rocky-black'] = {
    'body': 'corpulento', 'pal': pal('#5a3424', '#a8683a', nose='#c84a2a', tusk='#f4ece0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'face_front': WIDE_FACE, 'big_ears': 1, 'nose': (50, 84, 6.4), 'nose_side': (94, 82, 6), 'hairline': (54, 46)},
    'front': cap_hair('front') + [L(quad((26, 16), (16, 0), (4, 6)), 'shade', 'b', False, False, 3), L(quad((74, 16), (84, 0), (96, 6)), 'shade', 'b', False, False, 3),
                                  L([(30, 96), (34, 104), (36, 96)], 'tusk', 'f', ln=True), L([(70, 96), (66, 104), (64, 96)], 'tusk', 'f', ln=True)],
    'side': cap_hair('side'), 'back': cap_hair('back') + [L(quad((26, 16), (16, 0), (4, 6)), 'shade', 'b', False, False, 3), L(quad((74, 16), (84, 0), (96, 6)), 'shade', 'b', False, False, 3)],
}
# Chad Taylor: pelo castaño oscuro despeinado con una cinta rosa y unas gafas de buceo amarillas con tubo puestas
CHARS['chad-taylor'] = {
    'body': 'normal', 'pal': pal('#2e221e', '#a86a3a', rim='#e8c030', lens='#8ab8d8', band='#f0b0c0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': (56, 48)},
    'front': spiky('front', 0.7) + spiky_face('front', False)
             + [L(blob([(12, 60), (50, 54), (88, 60), (86, 86), (50, 90), (14, 86)]), 'rim', 'f', ln=True), L(blob([(18, 64), (50, 60), (82, 64), (80, 82), (50, 84), (20, 82)]), 'lens', 'f', False),
                L(blob([(42, 92), (58, 92), (56, 104), (44, 104)]), 'rim', 'f', ln=True), L(quad((86, 70), (104, 40), (96, 10)), 'rim', 'f', False, False, 3)],
    'side': spiky('side', 0.7) + spiky_face('side', False) + [L(blob([(66, 58), (98, 58), (98, 88), (68, 88)]), 'rim', 'f', ln=True), L(blob([(72, 62), (96, 62), (94, 84), (72, 84)]), 'lens', 'f', False)],
    'back': spiky('back', 0.7) + [L(quad((8, 60), (50, 54), (92, 60)), 'band', 'f', False, False, 3)],
}
# Victor Hills: calvo y rechoncho, con un mechoncito verde en lo alto, nariz roja y barbilla prominente
CHARS['victor-hills'] = {
    'body': 'corpulento', 'pal': pal('#2a5a2a', '#c87a3a', nose='#c84a2a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': WIDE_FACE, 'nose': (50, 84, 4.6), 'nose_side': (94, 82, 4.4), 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)] + spk((42, 8), (52, 6), (40, -12), 3) + spk((50, 6), (58, 8), (62, -10), 3, light_left=False),
    'side': [L(blob(SIDE_SKULL), 'skin')] + spk((40, 8), (52, 6), (44, -12), 3),
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)] + spk((42, 8), (52, 6), (40, -12), 3),
}
# Hector Redding: pelo castaño muy rizado y abultado, rayas rojas en las mejillas, nariz y ceño
CHARS['hector-redding'] = {
    'body': 'normal', 'pal': pal('#6a3e1e', '#d0905a', paint='#d02a2a', nose='#c86a3a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 84, 3.4), 'hairline': (56, 48)},
    'front': [L(bumpy(50, 26, 48, 26, 14, 0.1)), L(bumpy(70, 30, 22, 18, 8, 0.1), 'shade', 'b', False), L(blob([(10, 64), (8, 36), (92, 36), (90, 64), (80, 56), (20, 56)]))]
             + [L([(20, 82), (30, 86)], 'paint', 'f', False, False, 2), L([(80, 82), (70, 86)], 'paint', 'f', False, False, 2)],
    'side': [L(bumpy(44, 28, 44, 26, 14, 0.1)), L(blob(SIDE_SKULL)), L(bumpy(24, 40, 18, 20, 8, 0.1), 'shade', 'b', False), L([(78, 82), (86, 86)], 'paint', 'f', False, False, 2)],
    'back': [L(bumpy(50, 30, 48, 30, 14, 0.1)), L(blob([(10, 70), (8, 36), (92, 36), (90, 70), (70, 84), (30, 84)])), L(bumpy(68, 40, 22, 22, 8, 0.1), 'shade', 'b', False)],
}
# Mackenzie Fordline: pelo rojo en mechones gruesos enrollados y gafas de sol pequeñas; sonrisa
CHARS['mackenzie-fordline'] = {
    'body': 'normal', 'pal': pal('#b8401e', '#a86a3a', lens='#1e1a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (56, 48)},
    'front': [L(bumpy(50, 26, 46, 26, 10, 0.12)), L(bumpy(70, 30, 22, 18, 7, 0.12), 'shade', 'b', False)]
             + [strand([(x, 10 + abs(x - 50) * 0.3), (x + 4, 40)], 'deep', 'b', 1.4) for x in (24, 36, 48, 60, 72)]
             + [L(blob([(10, 62), (8, 36), (92, 36), (90, 62), (80, 54), (20, 54)])),
                L(blob([(22, 70), (44, 70), (42, 78), (24, 78)], 4), 'lens', 'f', ln=True), L(blob([(78, 70), (56, 70), (58, 78), (76, 78)], 4), 'lens', 'f', ln=True),
                L([(44, 72), (56, 72)], (200, 170, 60, 255), 'f', False, False, 1.4)],
    'side': [L(bumpy(44, 28, 44, 26, 10, 0.12)), L(blob(SIDE_SKULL)), L(bumpy(24, 40, 18, 20, 7, 0.12), 'shade', 'b', False),
             L(blob([(76, 70), (94, 70), (92, 78), (78, 78)], 4), 'lens', 'f', ln=True)],
    'back': [L(bumpy(50, 30, 46, 30, 10, 0.12)), L(blob([(10, 66), (8, 36), (92, 36), (90, 66), (70, 80), (30, 80)])), L(bumpy(68, 40, 22, 22, 7, 0.12), 'shade', 'b', False)]
            + [strand([(x, 14), (x + 4, 70)], 'deep', 'b', 1.4) for x in (24, 38, 52, 66)],
}
# Cadence Soundtown: pelo verde azulado despeinado, cascos rosas en las orejas y gafas finas
CHARS['cadence-soundtown'] = {
    'body': 'normal', 'pal': pal('#4aa0a8', '#fcdcc0', muff='#e8a0a8', band='#4a4a50'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'glasses': (90, 60, 50, 255), 'hairline': (58, 50)},
    'front': spiky('front', 0.6) + spiky_face('front') + [L(quad((12, 66), (50, 8), (88, 66)), 'band', 'f', False, False, 2.6),
             L(ell(8, 70, 8, 11), 'muff', 'f', ln=True), L(ell(92, 70, 8, 11), 'muff', 'f', ln=True)],
    'side': spiky('side', 0.6) + spiky_face('side') + [L(ell(42, 68, 11, 13), 'muff', 'f', ln=True), L(quad((42, 56), (40, 20), (54, 4)), 'band', 'f', False, False, 2.6)],
    'back': spiky('back', 0.6) + [L(ell(8, 70, 8, 11), 'muff', 'f', ln=True), L(ell(92, 70, 8, 11), 'muff', 'f', ln=True)],
}
# Dora Delight: un gorro de concha en espiral azul celeste con pinchos, pelo naranja asomando y ojos grandes
CHARS['dora-delight'] = {
    'body': 'chica', 'pal': pal('#e8801e', '#fcdcc0', shell='#b8dcec', shell_d='#8ab0c4', spike='#a8a8b0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 80), (12, 54), (88, 54), (90, 80), (80, 76), (20, 76)]))] + fringe(4, 54, 66)
             + [L(blob([(8, 60), (12, 34), (28, 10), (50, -14), (72, 10), (88, 34), (92, 60), (50, 56)]), 'shell', 'f', ln=True),
                L(blob([(56, -8), (88, 34), (90, 58), (68, 56)], 6), 'shell_d', 'f', False)]
             + [L(quad((10 + k * 4, 52 - k * 14), (50, 40 - k * 16), (90 - k * 4, 52 - k * 14)), 'shell_d', 'f', False, False, 1.6) for k in range(4)]
             + [L([(x - 3, y), (x, y - 7), (x + 3, y)], 'spike', 'f', ln=True) for x, y in ((14, 40), (86, 40), (26, 22), (74, 22), (40, 6), (60, 6))],
    'side': [L(blob(BOB_S))] + [L(blob([(8, 62), (12, 32), (30, 8), (50, -14), (76, 10), (94, 34), (96, 58), (50, 58)]), 'shell', 'f', ln=True)]
            + [L(quad((10 + k * 4, 52 - k * 14), (50, 40 - k * 16), (94 - k * 4, 52 - k * 14)), 'shell_d', 'f', False, False, 1.6) for k in range(4)],
    'back': [L(blob(BOB_B)), L(blob([(8, 64), (12, 34), (28, 10), (50, -14), (72, 10), (88, 34), (92, 64), (50, 62)]), 'shell', 'f', ln=True)]
            + [L(quad((10 + k * 4, 56 - k * 14), (50, 44 - k * 16), (90 - k * 4, 56 - k * 14)), 'shell_d', 'f', False, False, 1.6) for k in range(4)],
}
# Tom Contented: afro rojo oscuro enorme y ancho, piel morena, ojos redondos y rayas verdes en la cara
CHARS['tom-contented'] = {
    'body': 'normal', 'pal': pal('#5a1a14', '#a87a5a', paint='#3a6a4a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94, 'hairline': (56, 46)},
    'front': [L(bumpy(50, 36, 60, 34, 16, 0.1)), L(bumpy(72, 40, 26, 24, 8, 0.1), 'shade', 'b', False), L(blob([(10, 64), (8, 40), (92, 40), (90, 64), (80, 56), (20, 56)])),
              L(quad((20, 60), (18, 80), (26, 100)), 'paint', 'f', False, False, 2), L(quad((80, 60), (82, 80), (74, 100)), 'paint', 'f', False, False, 2)],
    'side': [L(bumpy(40, 38, 56, 34, 16, 0.1)), L(blob(SIDE_SKULL)), L(bumpy(18, 46, 24, 26, 8, 0.1), 'shade', 'b', False)],
    'back': [L(bumpy(50, 40, 60, 38, 16, 0.1)), L(bumpy(70, 46, 26, 26, 8, 0.1), 'shade', 'b', False)],
}
# Joston Easton: piel morena, pelo azul celeste en grandes rizos enrollados (uno sobre la frente y tres a cada lado)
CHARS['joston-easton'] = {
    'body': 'normal', 'pal': pal('#8ac0e0', '#a8703a', iris='#3a5aa0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (56, 48)},
    'front': [L(bumpy(x, y, 11, 10, 7, 0.08)) for x, y in ((6, 50), (4, 72), (94, 50), (96, 72))] + cap_hair('front')
             + [L(bumpy(40, 34, 14, 12, 7, 0.08), 'mid', 'f', ln=True), L(blob([(32, 32), (40, 26), (48, 32), (40, 38), (36, 34)], 5), 'shade', 'f', False, False, 1.6)],
    'side': [L(bumpy(x, y, 11, 10, 7, 0.08)) for x, y in ((16, 50), (14, 72), (30, 84))] + cap_hair('side'),
    'back': [L(bumpy(x, y, 12, 11, 7, 0.08)) for x, y in ((6, 50), (4, 72), (94, 50), (96, 72), (30, 80), (50, 84), (70, 80))] + cap_hair('back'),
}
# Spring Millpond: pelo azul lavanda en una cresta de punta alta y mechones de punta a los lados; ojos afilados
CHARS['spring-millpond'] = {
    'body': 'normal', 'pal': pal('#5a68b0', '#f0b878'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': (56, 46)},
    'front': spk((38, 12), (62, 12), (50, -30), 7) + spk((4, 60), (12, 46), (-16, 52), 5) + spk((88, 46), (96, 60), (116, 52), 5, light_left=False)
             + spk((8, 74), (14, 62), (-8, 80), 4) + spk((86, 62), (92, 74), (108, 80), 4, light_left=False) + cap_hair('front') + fringe(4, 36, 58),
    'side': spk((30, 14), (60, 8), (34, -30), 8) + spk((12, 56), (16, 40), (-14, 50), 6) + cap_hair('side'),
    'back': spk((38, 12), (62, 12), (50, -30), 7) + spk((4, 60), (12, 46), (-16, 52), 5) + spk((88, 46), (96, 60), (116, 52), 5, light_left=False) + cap_hair('back')
            + spk((30, 74), (50, 80), (40, 96), 5) + spk((50, 80), (70, 74), (60, 96), 5, light_left=False),
}
# Gaston Cooley (portero suplente): pelo naranja en forma de seta acabada en punta arriba y alas a los lados; ceño
CHARS['gaston-cooley'] = {
    'body': 'normal', 'pal': pal('#f0a030', '#c8905a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': (58, 52)},
    'front': [L(blob([(-6, 58), (6, 34), (30, 10), (50, -10), (70, 10), (94, 34), (106, 58), (86, 54), (82, 60), (18, 60), (14, 54)])),
              L(blob([(56, -4), (94, 34), (104, 56), (84, 52)], 6), 'shade', 'b', False), sheen(24, 48, 14, 3)] + fringe(5, 40, 60),
    'side': [L(blob([(-8, 56), (4, 30), (30, 6), (52, -10), (80, 8), (96, 30), (92, 52), (60, 50), (20, 54)])), L(blob(SIDE_SKULL[:3] + [(30, 50)]), 'skin')]
            + [L(blob(SIDE_SKULL), 'skin'), L(blob([(-8, 56), (4, 30), (30, 6), (52, -10), (80, 8), (96, 30), (92, 52), (60, 50), (20, 54)]))],
    'back': [L(blob([(-6, 60), (6, 34), (30, 10), (50, -10), (70, 10), (94, 34), (106, 60), (50, 70)])), L(blob(SKULL_B), 'mid'), L(blob([(56, -4), (94, 34), (104, 58), (66, 66)], 6), 'shade', 'b', False)],
}
# Bevan Breakfast: rapado a un lado y el resto del pelo castaño oscuro en un tupé de pinchos hacia atrás; ceño
CHARS['bevan-breakfast'] = {
    'body': 'normal', 'pal': pal('#3e2e1a', '#fcc890'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    # su derecha (izquierda de la imagen) va rapada; el pelo nace en una cresta de la frente a la coronilla, sube en pinchos
    # hacia atrás y cae en un mechón grande por su izquierda hasta la ceja
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(outline([(40, 20), (34, 4), (22, -16, 1), (40, -6), (44, -24, 1), (54, -6), (66, -22, 1), (64, -2), (80, 2, 1), (74, 12), (86, 26),
                         (90, 46), (86, 62, 1), (80, 46), (70, 38), (60, 40), (50, 44, 1), (52, 32), (44, 26)]), 'mid', 'f'),
              L(outline([(58, 0), (74, 12), (86, 30), (86, 54, 1), (76, 36), (62, 30)]), 'shade', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(40, 14), (24, -2), (6, -14, 1), (28, -10), (34, -26, 1), (46, -10), (60, -22, 1), (62, -6), (78, -6, 1), (76, 6), (88, 20),
                        (92, 40, 1), (80, 30), (64, 22), (50, 20)])),
             L(outline([(44, 16), (36, 2), (54, -4), (70, 6), (60, 18)]), 'shade', 'b', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L(outline([(40, 22), (32, 0), (20, -18, 1), (40, -8), (48, -24, 1), (56, -6), (72, -18, 1), (66, 0), (60, 20)])),
             L(outline([(50, 18), (46, -4), (58, -6), (62, 14)]), 'shade', 'b', False)],
}
# Jack Griddle: piel morena, pelo morado oscuro de pinchos hacia atrás y gafas de sol envolventes azul oscuro; sonrisa
CHARS['jack-griddle'] = {
    'body': 'normal', 'pal': pal('#3a1e3a', '#9a6a40', lens='#1e2a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 93, 'hairline': (56, 48)},
    'front': spiky('front', 0.7) + spiky_face('front') + [L(blob([(14, 70), (50, 66), (86, 70), (82, 80), (54, 80), (50, 76), (46, 80), (18, 80)], 4), 'lens', 'f', ln=True)],
    'side': spiky('side', 0.7) + spiky_face('side') + [L(blob([(66, 68), (96, 68), (94, 80), (68, 80)], 4), 'lens', 'f', ln=True)],
    'back': spiky('back', 0.7),
}
# Stan Andagi: pelo castaño oliva corto de pinchos, cara cuadrada y ceño
CHARS['stan-andagi'] = {
    'body': 'normal', 'pal': pal('#4a4424', '#c8904a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': (54, 46)},
    'front': [spk((30, 12), (48, 6), (34, -10), 4), spk((48, 6), (64, 10), (64, -10), 4, light_left=False)] + cap_hair('front'),
    'side': [spk((30, 12), (50, 6), (30, -12), 5)] + cap_hair('side'),
    'back': [spk((30, 12), (48, 6), (34, -10), 4), spk((48, 6), (64, 10), (64, -10), 4, light_left=False)] + cap_hair('back'),
}
# Coral Talent: melena verde claro lisa hasta los hombros con flequillo recto; piel morena
CHARS['coral-talent'] = {
    'body': 'chica', 'pal': pal('#a8d898', '#b8805a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(6, 104), (2, 56), (12, 16), (50, 4), (88, 16), (98, 56), (94, 104), (82, 98), (82, 66), (18, 66), (18, 98)])),
              L(blob([(62, 14), (96, 50), (92, 100), (84, 98)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3),
              L(blob([(12, 62), (10, 40), (24, 22), (50, 16), (76, 22), (90, 40), (88, 62), (50, 60)]), 'mid', 'f', ln=True)]
             + [strand([(x, 30 + abs(x - 50) * 0.2), (x, 60)], 'shade', 'f', 0.9) for x in (28, 40, 52, 64, 76)],
    'side': [L(blob([(54, 104), (14, 106), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (94, 62), (76, 60), (62, 58), (58, 76), (58, 98)]))] + bob_shade('side'),
    'back': [L(blob([(6, 104), (2, 56), (12, 16), (50, 4), (88, 16), (98, 56), (94, 104), (50, 110)])), L(blob([(58, 14), (96, 50), (92, 102), (66, 108)], 6), 'shade', 'b', False)]
            + [strand([(x, 40), (x, 104)], 'shade', 'b', 1.0) for x in (26, 40, 60, 74)],
}
