"""Osaka Gals CCC / Triple C de Osaka (IE2): las chicas del Osaka; moños, coletas, flores, trenzas y gorros, con sus
modelos 3D como referencia (la entrenadora, la señora Hartland, con su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, spiky, spiky_face
from chars_otaku import back_hair
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

BLUSH = '#f0a080'


def blush(side=False):
    return [L(ell(80, 86, 3.6, 2.4), 'blush', 'f', False)] if side else [L(ell(26, 86, 4, 2.6), 'blush', 'f', False), L(ell(74, 86, 4, 2.6), 'blush', 'f', False)]


def cap_hair(view):
    """Pelo recogido pegado a la cabeza (para poner moños y coletas encima)."""
    if view == 'front':
        return [L(blob([(12, 66), (10, 38), (22, 14), (50, 6), (78, 14), (90, 38), (88, 66)])), L(blob([(62, 12), (88, 36), (86, 64), (74, 60)], 6), 'shade', 'b', False), sheen(24, 48, 14, 3)]
    if view == 'side':
        return [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
    return [L(blob(SKULL_B))] + back_hair()


# Daisy Fields (portera): corpulenta, pelo castaño recogido en un moño de rizos alto, coloretes y sonrisa
CHARS['daisy-fields'] = {
    'body': 'corpulento', 'pal': pal('#6a4024', '#fcc890', blush=BLUSH),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': (56, 46)},
    'front': [L(bumpy(50, -4, 22, 14, 9, 0.12))] + cap_hair('front') + blush(),
    'side': [L(bumpy(38, -4, 22, 14, 9, 0.12))] + cap_hair('side') + blush(True),
    'back': [L(bumpy(50, -2, 22, 14, 9, 0.12))] + cap_hair('back'),
}
# Alexia Sand: piel morena, pelo verde oliva oscuro en muchos moñitos redondos alrededor de la cabeza y una diadema crema
BUNS = [(10, 40), (20, 16), (40, 2), (60, 2), (80, 16), (90, 40), (6, 64), (94, 64)]
CHARS['alexia-sand'] = {
    'body': 'chica', 'pal': pal('#3a3a1e', '#a8703a', band='#f0e4b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (56, 46)},
    'front': [L(bumpy(x, y, 10, 10, 7, 0.1)) for x, y in BUNS] + cap_hair('front') + [L(quad((14, 40), (50, 26), (86, 40)), 'band', 'f', False, False, 3)],
    'side': [L(bumpy(x, y, 10, 10, 7, 0.1)) for x, y in ((10, 40), (24, 14), (48, 2), (10, 66), (26, 80))] + cap_hair('side') + [L(quad((20, 40), (50, 24), (84, 30)), 'band', 'f', False, False, 3)],
    'back': [L(bumpy(x, y, 10, 10, 7, 0.1)) for x, y in BUNS + [(30, 60), (50, 66), (70, 60)]] + cap_hair('back'),
}
# Hellen Hearth: pelo rosa empolvado con dos moños grandes a los lados y dos tirabuzones que bajan de ellos; flequillo
CHARS['hellen-hearth'] = {
    'body': 'chica', 'pal': pal('#c87a80', '#fce0c8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [L(bumpy(6, 40, 16, 16, 8, 0.08)), L(bumpy(94, 40, 16, 16, 8, 0.08)), L(bumpy(4, 72, 8, 12, 6, 0.1)), L(bumpy(96, 72, 8, 12, 6, 0.1)),
              L(bumpy(6, 92, 6, 8, 6, 0.1)), L(bumpy(94, 92, 6, 8, 6, 0.1))] + cap_hair('front') + fringe(5, 34, 58),
    'side': [L(bumpy(22, 36, 18, 18, 8, 0.08)), L(bumpy(18, 70, 8, 12, 6, 0.1)), L(bumpy(18, 92, 6, 8, 6, 0.1))] + cap_hair('side')
            + [spk((56, 30), (88, 40), (92, 64), 5, z='f', light_left=False)],
    'back': [L(bumpy(6, 40, 16, 16, 8, 0.08)), L(bumpy(94, 40, 16, 16, 8, 0.08)), L(bumpy(4, 72, 8, 12, 6, 0.1)), L(bumpy(96, 72, 8, 12, 6, 0.1))] + cap_hair('back'),
}
# Rose Pinkpetal: pelo naranja rojizo de pinchos cortos, pecas, pendientes y mirada desafiante
CHARS['rose-pinkpetal'] = {
    'body': 'chica', 'pal': pal('#b85a20', '#fcd8b4', freckle='#d08a5a', earring='#c8c8d0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': spiky('front', 0.6) + spiky_face('front')
             + [L(ell(x, y, 1, 1), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (74, 86), (70, 88))]
             + [L(ell(16, 84, 2, 3), 'earring', 'f', ln=True), L(ell(84, 84, 2, 3), 'earring', 'f', ln=True)],
    'side': spiky('side', 0.6) + spiky_face('side'), 'back': spiky('back', 0.6),
}
# Esther Greenland: melena castaña rojiza ondulada hasta los hombros con raya al lado, labios marcados y cejas finas
CHARS['esther-greenland'] = {
    'body': 'chica', 'pal': pal('#5a2a24', '#fcd0b0', lip='#c05a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(10, 66), (24, 52), (44, 42), (60, 48), (76, 56), (90, 66)]},
    'front': [L(blob(BOB_F))] + bob_shade('front') + wavy((2, 66), (12, 70), (-6, 100), -5) + wavy((88, 70), (98, 66), (106, 100), 5, light_left=False)
             + [strand([(44, 8), (30, 48)], 'deep', 'b', 1.1), L(quad((44, 94), (50, 96), (56, 94)), 'lip', 'f', False, False, 1.8)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + wavy((6, 70), (16, 80), (-6, 100), -5) + [spk((56, 30), (90, 40), (92, 70), 5, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + wavy((8, 84), (28, 90), (8, 104), 5) + wavy((72, 90), (92, 84), (92, 104), -5, light_left=False),
}
# Bela Bluebells: gorro verde con una hoja crema estampada, melena castaña clara ondulada y gafas redondas rojas
CHARS['bela-bluebells'] = {
    'body': 'chica', 'pal': pal('#c08a50', '#fcd8b8', hat='#3a7a30', hat_d='#2a5a22', leaf='#c8e0a0', rim='#d02a2a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(bumpy(50, 76, 46, 18, 12, 0.08)), L(blob([(10, 60), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 60), (50, 56)]), 'hat', 'f', ln=True),
              L(blob([(60, 4), (90, 28), (90, 58), (72, 56)], 6), 'hat_d', 'f', False),
              L([(50, 14), (40, 26), (24, 24), (36, 34), (30, 46), (50, 38), (70, 46), (64, 34), (76, 24), (60, 26)], 'leaf', 'f', ln=True),
              L(ell(36, 74, 9, 8), 'rim', 'f', False, False, 1), ] + [L(ell(cx, 74, 9, 8) + [ell(cx, 74, 9, 8)[0]], 'rim', 'f', False, False, 2.2) for cx in (36, 64)]
             + [L([(45, 73), (55, 73)], 'rim', 'f', False, False, 1.8)],
    'side': [L(bumpy(40, 76, 40, 18, 12, 0.08)), L(blob(SIDE_SKULL)),
             L(blob([(10, 62), (8, 28), (26, 6), (56, 0), (82, 10), (94, 30), (94, 58), (50, 58)]), 'hat', 'f', ln=True),
             L([(40, 20), (30, 32), (40, 40), (54, 30)], 'leaf', 'f', ln=True), L(ell(86, 74, 5, 8) + [ell(86, 74, 5, 8)[0]], 'rim', 'f', False, False, 2.2)],
    'back': [L(bumpy(50, 78, 46, 20, 12, 0.08)), L(blob(SKULL_B), 'mid'),
             L(blob([(10, 64), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 64), (50, 66)]), 'hat', 'f', ln=True),
             L(blob([(58, 4), (90, 28), (90, 62), (66, 66)], 6), 'hat_d', 'f', False)],
}
CHARS['bela-bluebells']['front'] = [x for x in CHARS['bela-bluebells']['front'] if not (x['c'] == 'rim' and x['w'] == 1)]
# Natalie Sunrise: piel morena, pelo rubio platino trenzado pegado al cráneo con una cresta en zigzag y dos coletas finas; labios gruesos
CHARS['natalie-sunrise'] = {
    'body': 'chica', 'pal': pal('#ece0b8', '#9a6a40', shade='#c8b890', lip='#6a3020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 8, 'hairline': (54, 44)},
    'front': cap_hair('front') + [L([(50, 8), (46, 16), (54, 24), (46, 32), (54, 40), (50, 46)], 'shade', 'b', False, False, 1.6),
                                  L(quad((16, 60), (12, 80), (14, 100)), 'mid', 'f', False, False, 2.6), L(quad((84, 60), (88, 80), (86, 100)), 'mid', 'f', False, False, 2.6)],
    'side': cap_hair('side') + [L(quad((40, 64), (38, 84), (40, 100)), 'mid', 'f', False, False, 2.6)],
    'back': cap_hair('back') + [L([(50, 8), (46, 20), (54, 32), (46, 44), (54, 56), (50, 68)], 'shade', 'b', False, False, 1.6),
                                L(blob([(40, 70), (60, 70), (56, 84), (44, 84)]), 'mid', 'f', ln=True)],
}
# Hillary Bush: piel morena, pelo lila recogido en una coleta lateral larga con una flor naranja grande en la cabeza; ojos verdes
FLOWER = lambda x, y: [L(ell(x + dx * 6, y + dy * 6, 6, 6), (240, 140, 20, 255), 'f', ln=True) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (0.7, 0.7), (-0.7, -0.7), (0.7, -0.7), (-0.7, 0.7))] \
    + [L(ell(x, y, 4, 4), (240, 200, 40, 255), 'f', ln=True)]
CHARS['hillary-bush'] = {
    'body': 'chica', 'pal': pal('#7a7aa8', '#b88050', iris='#3a8a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(10, 66), (26, 50), (46, 40), (64, 46), (78, 54), (90, 66)]},
    'front': cap_hair('front') + wavy((84, 40), (96, 50), (104, 108), 6, z='f', light_left=False) + [L(blob([(10, 60), (20, 60), (22, 90), (12, 92)]), 'mid', 'f')] + FLOWER(60, 12),
    'side': wavy((10, 40), (24, 40), (-4, 108), 8) + cap_hair('side') + FLOWER(52, 10),
    'back': cap_hair('back') + wavy((14, 40), (28, 46), (2, 110), -6, z='f') + FLOWER(40, 12),
}
# Mary Moor: pelo verde azulado muy oscuro rapado a los lados con una cresta peinada hacia atrás; mirada seria
CHARS['mary-moor'] = {
    'body': 'chica', 'pal': pal('#1e3a44', '#fcd8b4', shave='#6a7a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (56, 48)},
    'front': [L(blob(SKULL_F), 'shave'), L(blob([(28, 50), (30, 14), (50, 0), (70, 14), (72, 50), (50, 44)])), L(blob([(54, 4), (70, 16), (70, 48), (58, 46)], 5), 'shade', 'b', False)],
    'side': [L(blob(SIDE_SKULL), 'shave'), L(blob([(16, 60), (14, 26), (36, 4), (66, 2), (86, 14), (92, 30), (66, 26), (40, 34)]))],
    'back': [L(blob(SKULL_B), 'shave'), L(blob([(28, 80), (30, 14), (50, 0), (70, 14), (72, 80), (50, 86)]))],
}
# Lily Willow: pelo castaño rojizo con una coleta alta de rastas gruesas que caen alrededor y una diadema azul; ojos verdes
CHARS['lily-willow'] = {
    'body': 'chica', 'pal': pal('#a8402a', '#fcd8b4', iris='#3a8a3a', band='#2a6ab0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 48)},
    'front': [L(blob([(x, 14), (x + 8, 14), (x + 6 + (x - 50) * 0.5, 74), (x - 2 + (x - 50) * 0.5, 74)]), 'mid', 'b', ln=True) for x in (6, 22, 70, 86)]
             + cap_hair('front') + [L(quad((16, 30), (50, 16), (84, 30)), 'band', 'f', False, False, 3)] + fringe(4, 36, 58),
    'side': [L(blob([(30, 14), (40, 10), (6, 90), (-6, 86)]), 'mid', 'b', ln=True), L(blob([(36, 10), (44, 10), (24, 96), (12, 94)]), 'mid', 'b', ln=True)]
            + cap_hair('side') + [L(quad((20, 34), (50, 18), (84, 24)), 'band', 'f', False, False, 3)],
    'back': cap_hair('back') + [L(blob([(x, 14), (x + 10, 14), (x + 8 + (x - 45) * 0.4, 100), (x - 2 + (x - 45) * 0.4, 100)]), 'mid', 'f', ln=True) for x in (14, 30, 46, 62, 78)],
}
# Gayle Revel: pelo castaño rojizo corto de mechones en punta hacia atrás, ojos dorados y pendientes
CHARS['gayle-revel'] = {
    'body': 'chica', 'pal': pal('#a04a2a', '#fcdcc0', iris='#c8a020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': cap_hair('front') + spk((40, 8), (60, 8), (54, -12), 5) + fringe(4, 36, 62),
    'side': [spk((20, 30), (40, 12), (-6, 8), 7), spk((40, 12), (60, 8), (40, -14), 6)] + cap_hair('side'),
    'back': cap_hair('back') + spk((28, 70), (50, 76), (40, 96), 5) + spk((50, 76), (72, 70), (60, 96), 5, light_left=False),
}
# Dell Closeout (portera): gorro verde menta pálido muy calado, pelo azul marino que asoma por la nuca y cara de enfado
CHARS['dell-closeout'] = {
    'body': 'chica', 'pal': pal('#1e2a4a', '#f6c08e', hat='#c8e8d0', hat_d='#98b8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob([(10, 76), (12, 56), (88, 56), (90, 76), (78, 72), (22, 72)])),
              L(blob([(8, 62), (6, 30), (22, 6), (50, 0), (78, 6), (94, 30), (92, 62), (50, 58)]), 'hat', 'f', ln=True),
              L(blob([(60, 4), (92, 28), (92, 60), (72, 58)], 6), 'hat_d', 'f', False)],
    'side': [L(blob([(30, 60), (6, 60), (2, 84), (30, 84)])), L(blob(SIDE_SKULL)),
             L(blob([(10, 64), (8, 28), (26, 4), (56, -2), (82, 8), (96, 30), (96, 60), (50, 60)]), 'hat', 'f', ln=True)],
    'back': [L(blob(SKULL_B)), L(blob([(10, 86), (8, 56), (92, 56), (90, 86), (50, 92)])),
             L(blob([(8, 66), (6, 30), (22, 6), (50, 0), (78, 6), (94, 30), (92, 66), (50, 70)]), 'hat', 'f', ln=True),
             L(blob([(58, 4), (92, 28), (92, 64), (66, 68)], 6), 'hat_d', 'f', False)],
}
# Amy Spires: pelo rubio recogido en dos moños con tirabuzones cortos a los lados y flequillo; ojos verdes grandes
CHARS['amy-spires'] = {
    'body': 'chica', 'pal': pal('#d8b060', '#fcdcc0', iris='#3a9a3a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': [L(bumpy(14, 40, 12, 10, 7, 0.1)), L(bumpy(86, 40, 12, 10, 7, 0.1)), L(bumpy(2, 48, 8, 6, 6, 0.1)), L(bumpy(98, 48, 8, 6, 6, 0.1))]
             + cap_hair('front') + fringe(4, 34, 56),
    'side': [L(bumpy(24, 36, 12, 10, 7, 0.1)), L(bumpy(12, 44, 8, 6, 6, 0.1))] + cap_hair('side'),
    'back': [L(bumpy(14, 40, 12, 10, 7, 0.1)), L(bumpy(86, 40, 12, 10, 7, 0.1)), L(bumpy(2, 48, 8, 6, 6, 0.1)), L(bumpy(98, 48, 8, 6, 6, 0.1))] + cap_hair('back'),
}
# Peony Cash: melena rubia lisa hasta los hombros con un mechón sobre un ojo, mirada seria
CHARS['peony-cash'] = {
    'body': 'chica', 'pal': pal('#e0b040', '#fcdcc0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [L(blob([(6, 100), (2, 54), (12, 16), (50, 4), (88, 16), (98, 54), (94, 100), (82, 96), (82, 64), (18, 64), (18, 96)]))]
             + [L(blob([(62, 14), (96, 50), (92, 96), (84, 94)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3)]
             + [L(blob([(14, 40), (40, 28), (62, 32), (58, 60), (50, 82), (42, 84), (38, 64), (22, 54)]), 'mid', 'f'), strand([(60, 34), (56, 60), (46, 84)], OUTC, 'f', 1.0)],
    'side': [L(blob([(54, 100), (14, 102), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (58, 74), (58, 94)]))] + bob_shade('side'),
    'back': [L(blob([(6, 100), (2, 54), (12, 16), (50, 4), (88, 16), (98, 54), (94, 100), (50, 106)])), L(blob([(58, 14), (96, 50), (92, 98), (66, 104)], 6), 'shade', 'b', False)],
}
# Janine Brook: corpulenta, pelo naranja recogido en dos moños altos grandes, una diadema crema y coloretes
CHARS['janine-brook'] = {
    'body': 'corpulento', 'pal': pal('#c8701a', '#fcc890', band='#f0e4c8', blush=BLUSH),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': (54, 44)},
    'front': [L(bumpy(24, 4, 18, 14, 8, 0.1)), L(bumpy(76, 4, 18, 14, 8, 0.1))] + cap_hair('front') + [L(quad((20, 22), (50, 10), (80, 22)), 'band', 'f', False, False, 4)] + blush(),
    'side': [L(bumpy(34, 2, 20, 14, 8, 0.1))] + cap_hair('side') + blush(True),
    'back': [L(bumpy(24, 6, 18, 14, 8, 0.1)), L(bumpy(76, 6, 18, 14, 8, 0.1))] + cap_hair('back'),
}
# Señora Hartland (sin modelo 3D; su retrato): melena azul petróleo muy abultada y ondulada, una gorra roja, pendientes y labios
CHARS['se-ora-hartland'] = {
    'body': 'chica', 'pal': pal('#3a8a9a', '#fcd8b8', cap='#b81a1a', cap_d='#801010', lip='#e08a3a', earring='#f0f0f0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 7, 'hairline': False},
    'front': [L(bumpy(50, 60, 54, 44, 14, 0.08)), L(bumpy(70, 64, 24, 34, 8, 0.08), 'shade', 'b', False),
              L(blob([(8, 50), (8, 26), (22, 8), (50, 2), (78, 8), (92, 26), (92, 50), (50, 46)]), 'cap', 'f', ln=True),
              L(blob([(60, 6), (92, 26), (92, 48), (72, 46)], 6), 'cap_d', 'f', False),
              L(ell(16, 84, 2.4, 2.4), 'earring', 'f', ln=True), L(ell(84, 84, 2.4, 2.4), 'earring', 'f', ln=True)],
    'side': [L(bumpy(40, 60, 50, 44, 14, 0.08)), L(blob(SIDE_SKULL)),
             L(blob([(10, 52), (8, 26), (26, 6), (56, 0), (82, 10), (94, 30), (94, 48), (50, 48)]), 'cap', 'f', ln=True)],
    'back': [L(bumpy(50, 62, 54, 46, 14, 0.08)), L(bumpy(68, 66, 24, 36, 8, 0.08), 'shade', 'b', False),
             L(blob([(8, 52), (8, 26), (22, 8), (50, 2), (78, 8), (92, 26), (92, 52), (50, 50)]), 'cap', 'f', ln=True)],
}
