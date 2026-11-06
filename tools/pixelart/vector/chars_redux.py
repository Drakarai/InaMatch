"""Shin Teikoku Gakuen / Royal Academy Redux (IE2): el equipo de Ray Dark; máscaras, gafas, gorros y caras pintadas, con
sus modelos 3D como referencia (Rowan Beltzer, con su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, LONG_FACE, spiky, spiky_face
from chars_ccc import cap_hair
from chars_otaku import back_hair
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

DARK = (24, 20, 24, 255)
WHITE = (250, 250, 250, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


# Rowan Beltzer: piel tostada, pelo gris azulado en surcos gruesos pegados al cráneo, ojos pequeños de enfado y labios enormes
CHARS['rowan-beltzer'] = {
    'body': 'corpulento', 'pal': pal('#4a5464', '#c89a50', lip='#a05a3a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'big_ears': 2, 'ear_out': 4, 'hairline': (52, 44)},
    'front': cap_hair('front') + [strand([(x, 10 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 46)], 'deep', 'b', 2) for x in (26, 38, 50, 62, 74)]
             + [L(blob([(30, 88), (50, 84), (70, 88), (66, 98), (50, 100), (34, 98)]), 'lip', 'f', ln=True)],
    'side': cap_hair('side') + [L(blob([(80, 86), (96, 86), (96, 98), (82, 98)]), 'lip', 'f', ln=True)],
    'back': cap_hair('back') + [strand([(x, 10), (x, 80)], 'deep', 'b', 2) for x in (30, 42, 54, 66)],
}
# Blade Healen: pelo gris oliva despeinado recogido en un moño alto, una cinta morada sobre los ojos y colmillos
CHARS['blade-healen'] = {
    'body': 'normal', 'pal': pal('#5a5a48', '#f8c890', band='#6a3a7a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': [L(bumpy(54, 0, 10, 10, 6, 0.1))] + spiky('front', 0.6) + spiky_face('front', False)
             + [L(quad((14, 64), (50, 58), (86, 64)) + quad((86, 72), (50, 66), (14, 72)), 'band', 'f', ln=True)] + fringe(4, 34, 62),
    'side': [L(bumpy(44, -4, 10, 10, 6, 0.1))] + spiky('side', 0.6) + spiky_face('side'),
    'back': [L(bumpy(54, 0, 10, 10, 6, 0.1))] + spiky('back', 0.6),
}
# Argie Bargie: corpulento, cabeza pequeña con un mechón morado oscuro de pinchos, nariz y ojos blancos furiosos
CHARS['argie-bargie'] = {
    'body': 'corpulento', 'pal': pal('#4a2a4a', '#d0a080', nose='#b07a5a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'nose': (50, 82, 4.4), 'hairline': False},
    'front': bald('front') + spk((32, 14), (50, 8), (26, -16), 6) + spk((50, 8), (68, 14), (74, -16), 6, light_left=False) + spk((42, 10), (58, 10), (50, -22), 5),
    'side': bald('side') + spk((26, 22), (44, 8), (2, -6), 8) + spk((44, 8), (62, 8), (40, -18), 6),
    'back': bald('back') + spk((32, 14), (50, 8), (26, -16), 6) + spk((50, 8), (68, 14), (74, -16), 6, light_left=False),
}
# Lee Bamboo: piel amarilla, pelo morado en forma de casco con dos picos y orejas puntiagudas; sonrisa malvada
CHARS['lee-bamboo'] = {
    'body': 'normal', 'pal': pal('#4a3a6a', '#d8a850'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'face_front': LONG_FACE, 'big_ears': 2, 'ear_out': 5, 'hairline': (50, 40)},
    'front': [L(blob([(0, 22), (14, 4), (50, 0), (86, 4), (100, 22), (84, 30), (88, 50), (12, 50), (16, 30)])), L(blob([(62, 4), (98, 22), (86, 48), (72, 44)], 6), 'shade', 'b', False)],
    'side': cap_hair('side'),
    'back': [L(blob([(0, 22), (14, 4), (50, 0), (86, 4), (100, 22), (84, 30), (86, 70), (50, 80), (14, 70), (16, 30)]))] + back_hair(),
}
from heads import fat
fat_streak = fat((40, 30), (60, 30), (50, -18), 5)
# Dawson Little: pelo blanco de pinchos con una franja azul en medio y una banda negra sobre los ojos; piel morena
CHARS['dawson-little'] = {
    'body': 'normal', 'pal': pal('#e8e4e0', '#a8703a', shade='#b8b0b0', streak='#3a6aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 50)},
    'front': spiky('front', 0.8) + spiky_face('front') + [L(fat_streak, 'streak', 'f', ln=True)]
             + [L(quad((12, 68), (50, 62), (88, 68)) + quad((88, 80), (50, 74), (12, 80)), DARK, 'f', ln=True)],
    'side': spiky('side', 0.8) + spiky_face('side') + [L(quad((12, 66), (50, 62), (96, 66)) + quad((96, 80), (50, 76), (12, 80)), DARK, 'f', ln=True)],
    'back': spiky('back', 0.8) + [L(quad((10, 70), (50, 66), (90, 70)) + quad((90, 82), (50, 78), (10, 82)), DARK, 'f', ln=True)],
}
# Eton Messer: pelo rubio de pinchos cortos arriba, un monóculo verde con lente azul en un ojo y una bufanda crema hasta la nariz
CHARS['eton-messer'] = {
    'body': 'normal', 'pal': pal('#e0b020', '#f0c080', scarf='#e8dcc8', scarf_d='#b8a890', rim='#3a5a3a', lens='#2a8ac0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': (40, 34)},
    'front': [spk((12 + k * 13, 24), (24 + k * 13, 24), (18 + k * 13, -6), 3) for k in range(6)] + cap_hair('front')
             + [L(quad((10, 66), (50, 58), (90, 66)) + quad((90, 72), (50, 64), (10, 72)), 'rim', 'f', ln=True),
                L(ell(50, 70, 10, 9), 'rim', 'f', ln=True), L(ell(50, 70, 6, 5.4), 'lens', 'f', False),
                L(blob([(8, 80), (50, 76), (92, 80), (96, 110), (50, 118), (4, 110)]), 'scarf', 'f', ln=True), L(blob([(56, 78), (92, 82), (94, 108), (58, 114)], 5), 'scarf_d', 'f', False)],
    'side': [spk((20 + k * 14, 20), (32 + k * 14, 18), (26 + k * 14, -6), 3) for k in range(4)] + cap_hair('side')
            + [L(ell(88, 68, 6, 9), 'rim', 'f', ln=True), L(blob([(30, 80), (96, 80), (96, 110), (30, 112)]), 'scarf', 'f', ln=True)],
    'back': [spk((12 + k * 13, 24), (24 + k * 13, 24), (18 + k * 13, -6), 3) for k in range(6)] + cap_hair('back')
            + [L(quad((10, 66), (50, 60), (90, 66)) + quad((90, 72), (50, 66), (10, 72)), 'rim', 'f', ln=True),
               L(blob([(8, 86), (50, 84), (92, 86), (94, 110), (50, 116), (6, 110)]), 'scarf', 'f', ln=True)],
}
# Jonah Spark: melena rubia ceniza con dos coletas bajas atadas y media cara cubierta por una máscara negra con un ojo blanco
CHARS['jonah-spark'] = {
    'body': 'normal', 'pal': pal('#e0d4b8', '#f8d8b8', shade='#c0b098', mask='#2a3a4a', tie='#c87a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front')
             + [L(blob([(16, 60), (50, 56), (52, 106), (24, 100), (14, 80)]), 'mask', 'f', ln=True), L(ell(32, 74, 6, 5), WHITE, 'f', ln=True),
                L(blob([(8, 84), (20, 84), (18, 100), (6, 100)]), 'mid', 'f', ln=True), L(blob([(92, 84), (80, 84), (82, 100), (94, 100)]), 'mid', 'f', ln=True),
                L(ell(13, 84, 4, 2.4), 'tie', 'f', ln=True), L(ell(87, 84, 4, 2.4), 'tie', 'f', ln=True)] + fringe(4, 34, 60),
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 74), 6, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [L(ell(16, 86, 5, 3), 'tie', 'f', ln=True), L(ell(84, 86, 5, 3), 'tie', 'f', ln=True)],
}
# Sue Sparrow: pelo coral rizado y suelto a los lados, con un mechón sobre un ojo y una mascarilla roja
CHARS['sue-sparrow'] = {
    'body': 'chica', 'pal': pal('#e0786a', '#fcd8b8', mask='#c03a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + wavy((2, 60), (12, 66), (-6, 100), -6) + wavy((88, 66), (98, 60), (106, 100), 6, light_left=False)
             + [L(blob([(14, 40), (40, 28), (62, 32), (58, 60), (50, 82), (42, 84), (38, 64), (22, 54)]), 'mid', 'f'), strand([(60, 34), (56, 60), (46, 84)], OUTC, 'f', 1.0),
                L(blob([(26, 82), (50, 78), (74, 82), (72, 98), (50, 104), (28, 98)]), 'mask', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + wavy((4, 64), (14, 74), (-8, 100), -6) + [L(blob([(70, 80), (96, 82), (96, 98), (74, 102)]), 'mask', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + wavy((6, 80), (24, 88), (2, 106), 6) + wavy((76, 88), (94, 80), (98, 106), -6, light_left=False),
}
# Riley Jamm: cara pintada de payaso blanca con una sonrisa enorme, y un pelo verde azulado en dos grandes cuernos curvados
CHARS['riley-jamm'] = {
    'body': 'normal', 'pal': pal('#1e7a6a', '#f4f0e8', smile='#2a2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': (52, 44)},
    'front': wavy((22, 20), (36, 12), (-16, 40), 10) + wavy((64, 12), (78, 20), (116, 40), -10, light_left=False) + cap_hair('front')
             + [L(quad((22, 84), (50, 104), (78, 84)) + quad((78, 84), (50, 94), (22, 84))[1:], WHITE, 'f', ln=True),
                L([(28, 86), (72, 86)], OUTC, 'f', False, False, 1.0)],
    'side': wavy((30, 16), (50, 8), (-8, 30), 10) + cap_hair('side') + [L(quad((66, 84), (84, 100), (98, 84)), OUTC, 'f', False, False, 1.6)],
    'back': wavy((22, 20), (36, 12), (-16, 40), 10) + wavy((64, 12), (78, 20), (116, 40), -10, light_left=False) + cap_hair('back'),
}
# Caleb Stonewall: rapado por detrás con un mechón castaño oscuro de pinchos arriba y un rayo rojo pintado en la frente
CHARS['caleb-stonewall'] = {
    'body': 'normal', 'pal': pal('#3a2a1e', '#fcd8b8', paint='#c03a2a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (50, 40)},
    'front': spk((20, 30), (44, 10), (10, -12), 6) + spk((44, 10), (64, 12), (60, -18), 6, light_left=False) + cap_hair('front')
             + [L([(62, 44), (70, 52), (64, 56), (74, 64)], 'paint', 'f', False, False, 2.2)],
    'side': bald('side') + spk((30, 20), (52, 6), (12, -10), 7) + spk((50, 6), (68, 8), (64, -18), 6, light_left=False),
    'back': bald('back') + spk((36, 12), (52, 8), (28, -16), 6) + spk((52, 8), (66, 12), (70, -14), 5, light_left=False),
}
# Jimbo Cellar (portero suplente): melena castaña lisa y larga con raya en medio, cara alargada pálida y ojos rasgados
CHARS['jimbo-cellar'] = {
    'body': 'delgado', 'pal': pal('#6a4830', '#fce4c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(14, 70), (26, 52), (42, 42), (50, 48), (58, 42), (74, 52), (86, 70)]},
    'front': [L(blob([(6, 120), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 120), (82, 116), (82, 66), (18, 66), (18, 116)])),
              L(blob([(62, 14), (96, 50), (92, 116), (84, 114)], 6), 'shade', 'b', False), strand([(50, 6), (50, 46)], 'deep', 'b', 1.2)],
    'side': [L(blob([(56, 118), (14, 120), (2, 66), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 78), (60, 106)]))] + bob_shade('side'),
    'back': [L(blob([(6, 120), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 120), (50, 126)])), L(blob([(58, 14), (96, 50), (92, 118), (66, 124)], 6), 'shade', 'b', False)],
}
# Zenn Wildhorse: gorro de lana verde con franjas amarillas y un mechón rojo que asoma por un lado; ojos cerrados y sonrisa
CHARS['zenn-wildhorse'] = {
    'body': 'normal', 'pal': pal('#c02a1a', '#fcc890', hat='#2a6a3a', hat_d='#1e4a2a', stripe='#e8b020'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': bald('front') + [L(blob([(8, 60), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (92, 60), (50, 56)]), 'hat', 'f', ln=True),
                              L(quad((8, 34), (50, 24), (92, 34)) + quad((92, 40), (50, 30), (8, 40)), 'stripe', 'f', False),
                              L(quad((8, 50), (50, 42), (92, 50)) + quad((92, 56), (50, 48), (8, 56)), 'stripe', 'f', False)]
             + wavy((70, 10), (84, 18), (88, 64), 8, z='f', light_left=False),
    'side': bald('side') + [L(blob([(10, 62), (8, 26), (26, 4), (56, -4), (84, 6), (96, 30), (96, 58), (50, 58)]), 'hat', 'f', ln=True),
                            L(quad((8, 34), (50, 24), (96, 34)) + quad((96, 40), (50, 30), (8, 40)), 'stripe', 'f', False)],
    'back': bald('back') + [L(blob([(8, 64), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (92, 64), (50, 68)]), 'hat', 'f', ln=True),
                            L(quad((8, 36), (50, 28), (92, 36)) + quad((92, 42), (50, 34), (8, 42)), 'stripe', 'f', False)]
            + wavy((16, 10), (30, 6), (8, 60), -8, z='f'),
}
# Maston Color: un sombrero de bruja morado pequeño y caído sobre una cara ancha sin pelo a la vista; ojos y boca de fastidio
CHARS['maston-color'] = {
    'body': 'normal', 'pal': pal('#3a2a4a', '#f8dcc0', hat='#5a4a7a', hat_d='#3e325a'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': False},
    'front': bald('front') + [L(blob([(0, 58), (20, 46), (34, 10), (50, -16), (60, -6), (66, 10), (80, 46), (100, 58), (50, 62)]), 'hat', 'f', ln=True),
                              L(blob([(54, -6), (66, 12), (80, 46), (98, 56), (60, 56)], 5), 'hat_d', 'f', False)],
    'side': bald('side') + [L(blob([(-8, 56), (20, 44), (40, 8), (60, -12), (70, -2), (72, 10), (84, 44), (104, 58), (50, 60)]), 'hat', 'f', ln=True)],
    'back': bald('back') + [L(blob([(0, 60), (20, 48), (34, 10), (50, -16), (60, -6), (66, 10), (80, 48), (100, 60), (50, 66)]), 'hat', 'f', ln=True)],
}
# Cosimo Beck (sin modelo 3D; su retrato): melena granate con flequillo sobre un ojo y puntas abiertas a la altura de la
# barbilla, gafas de sol rectangulares oscuras
CHARS['cosimo-beck'] = {
    'body': 'normal', 'pal': pal('#8a1a2a', '#e8b880', lens='#24302a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + wavy((4, 74), (14, 84), (-8, 96), -5) + wavy((86, 84), (96, 74), (108, 96), 5, light_left=False)
             + [L(blob([(14, 40), (40, 26), (62, 30), (58, 56), (48, 70), (40, 70), (36, 56), (22, 52)]), 'mid', 'f'), strand([(60, 32), (56, 56), (46, 70)], OUTC, 'f', 1.0),
                L(blob([(18, 70), (46, 70), (46, 80), (20, 80)], 4), 'lens', 'f', ln=True), L(blob([(82, 70), (54, 70), (54, 80), (80, 80)], 4), 'lens', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L(blob([(68, 70), (96, 70), (94, 80), (70, 80)], 4), 'lens', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + wavy((6, 80), (24, 88), (2, 102), 5) + wavy((76, 88), (94, 80), (98, 102), -5, light_left=False),
}
