"""Raimon II (IE2): los fichajes de la caravana (Shawn, Hurley, Scott, Darren, Suzette, Victoria) y Eugene, con sus
modelos 3D como referencia (Eugene Conwell no tiene modelo: su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]


# ------------------------------------------------------------------ Shawn Froste: pelo gris lavanda despeinado con las puntas
# hacia fuera (más oscuras, malva) a la altura de las orejas, un remolino de pelillos en lo alto y una bufanda crema al cuello
CHARS['shawn-froste'] = {
    'body': 'normal', 'pal': pal('#b8b4c8', '#f8dcc0', iris='#5a7a7a', tips='#8a6a7a', scarf='#f0e4d8', scarf_d='#c8b0a4'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'eye_y': 77, 'hairline': (60, 52)},
    'front': [spk((44, 8), (50, 8), (40, -6), 2), spk((50, 8), (56, 8), (60, -6), 2, light_left=False),
              L(blob([(6, 76), (2, 44), (14, 14), (50, 6), (86, 14), (98, 44), (94, 76), (82, 70), (82, 60), (18, 60), (18, 70)])),
              spk((2, 58), (10, 74), (-14, 76), 4), spk((90, 74), (98, 58), (114, 76), 4, light_left=False),
              spk((8, 72), (18, 80), (-2, 90), 4), spk((82, 80), (92, 72), (102, 90), 4, light_left=False),
              L(blob([(-10, 74), (-4, 80), (8, 82), (2, 76)], 4), 'tips', 'b', False), L(blob([(110, 74), (104, 80), (92, 82), (98, 76)], 4), 'tips', 'b', False),
              L(blob([(62, 12), (96, 44), (92, 74), (84, 72)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3),
              spk((12, 44), (30, 38), (18, 70), 5, z='f'), spk((28, 38), (48, 34), (38, 64), 5, z='f'),
              spk((52, 34), (70, 38), (60, 64), 5, z='f', light_left=False), spk((70, 40), (88, 44), (84, 70), 5, z='f', light_left=False),
              L(blob([(18, 100), (50, 106), (82, 100), (86, 114), (50, 120), (14, 114)]), 'scarf', 'f', ln=True),
              L(blob([(56, 104), (84, 100), (86, 114), (58, 118)], 5), 'scarf_d', 'f', False)],
    'side': [spk((44, 6), (52, 6), (44, -8), 2),
             L(blob([(48, 92), (14, 90), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 88)])),
             spk((4, 54), (8, 70), (-16, 66), 5), spk((8, 70), (16, 82), (-12, 92), 5), spk((18, 84), (32, 90), (8, 102), 4),
             L(blob([(-14, 66), (-6, 70), (-2, 66)], 3), 'tips', 'b', False), L(blob([(-10, 90), (-2, 88), (4, 84)], 3), 'tips', 'b', False),
             L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 12, 3),
             spk((56, 30), (88, 40), (92, 72), 6, z='f', light_left=False), spk((50, 54), (62, 54), (56, 82), 3, z='f'),
             L(blob([(30, 98), (70, 100), (90, 108), (84, 118), (40, 116), (24, 108)]), 'scarf', 'f', ln=True),
             L(blob([(30, 104), (18, 108), (10, 128), (22, 130), (32, 112)]), 'scarf_d', 'f', ln=True)],
    'back': [spk((44, 8), (50, 8), (40, -6), 2), spk((50, 8), (56, 8), (60, -6), 2, light_left=False),
             L(blob([(6, 78), (2, 44), (14, 14), (50, 6), (86, 14), (98, 44), (94, 78), (50, 86)])),
             spk((2, 58), (10, 74), (-14, 76), 4), spk((90, 74), (98, 58), (114, 76), 4, light_left=False),
             spk((10, 76), (28, 84), (6, 96), 5), spk((28, 84), (50, 88), (36, 102), 5), spk((50, 88), (72, 84), (66, 102), 5, light_left=False),
             spk((72, 84), (90, 76), (94, 96), 5, light_left=False),
             L(blob([(58, 12), (96, 44), (92, 76), (66, 84)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3),
             L(blob([(16, 98), (50, 102), (84, 98), (86, 112), (50, 116), (14, 112)]), 'scarf', 'f', ln=True)],
}

# ------------------------------------------------------------------ Hurley Kane: piel morena, melena rosa salmón de pinchos largos
# hacia arriba y a los lados, con dos mechones largos que le caen junto a la cara, y unas gafas de buceo en la frente
HURLEY_TOP = [spk((6, 58), (10, 40), (-18, 42), 6), spk((12, 38), (24, 20), (-8, 2), 7), spk((24, 20), (42, 10), (20, -20), 7),
              spk((42, 10), (60, 10), (52, -26), 7), spk((58, 12), (76, 18), (86, -16), 7, light_left=False),
              spk((76, 22), (90, 38), (118, 24), 7, light_left=False), spk((88, 44), (94, 60), (116, 62), 6, light_left=False)]
CHARS['hurley-kane'] = {
    'body': 'normal', 'pal': pal('#e8907e', '#b0703e', rim='#e8e8ec', lens='#2a8a9a', strap='#3a3a40'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': HURLEY_TOP + [L(blob([(10, 72), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 72), (80, 64), (20, 64)])),
                           L(blob([(62, 12), (90, 38), (88, 68), (78, 64)], 6), 'shade', 'b', False),
                           spk((12, 48), (26, 46), (20, 102), 4, z='f'), spk((74, 46), (88, 48), (80, 102), 4, z='f', light_left=False),
                           spk((26, 44), (44, 40), (34, 64), 4, z='f'), spk((56, 40), (74, 44), (66, 64), 4, z='f', light_left=False),
                           L(quad((10, 40), (50, 32), (90, 40)), 'strap', 'f', False, False, 2.4),
                           L(ell(36, 36, 8, 6), 'rim', 'f', ln=True), L(ell(64, 36, 8, 6), 'rim', 'f', ln=True),
                           L(ell(36, 36, 5, 3.6), 'lens', 'f', False), L(ell(64, 36, 5, 3.6), 'lens', 'f', False)],
    'side': [spk((16, 40), (24, 22), (-20, 14), 8), spk((24, 24), (42, 12), (8, -20), 8), spk((42, 12), (62, 6), (54, -26), 8),
             spk((14, 58), (16, 40), (-20, 50), 7), spk((18, 76), (22, 58), (-12, 84), 6), spk((28, 88), (32, 74), (10, 104), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 12), (82, 22), (102, -2), 7, light_left=False),
             spk((54, 30), (86, 40), (90, 72), 6, z='f', light_left=False), spk((50, 52), (62, 52), (58, 100), 3, z='f'),
             L(quad((16, 40), (50, 30), (90, 34)), 'strap', 'f', False, False, 2.4),
             L(ell(84, 32, 6, 6), 'rim', 'f', ln=True), L(ell(85, 32, 3.4, 4), 'lens', 'f', False)],
    'back': HURLEY_TOP + [L(blob([(10, 74), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 74), (66, 88), (34, 88)])),
                          spk((12, 72), (30, 86), (6, 100), 6), spk((30, 88), (50, 92), (38, 110), 6), spk((50, 92), (70, 88), (64, 110), 6, light_left=False),
                          spk((70, 86), (88, 72), (94, 100), 6, light_left=False),
                          L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False),
                          L(quad((8, 44), (50, 36), (92, 44)), 'strap', 'f', False, False, 2.4)],
}

# ------------------------------------------------------------------ Scott Banyan: bajito, pelo azul marino con dos pinchos grandes
# a los lados como cuernos y uno arriba; ojos naranjas grandes y sonrisa pícara
CHARS['scott-banyan'] = {
    'body': 'bajito', 'pal': pal('#2e3a6a', '#f8cca0', iris='#e07a10'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'big_ears': 1, 'hairline': (58, 50)},
    'front': [spk((4, 40), (16, 24), (-18, 4), 6), spk((84, 24), (96, 40), (118, 4), 6, light_left=False),
              spk((40, 10), (58, 8), (46, -10), 5),
              L(blob([(12, 66), (10, 38), (22, 14), (50, 6), (78, 14), (90, 38), (88, 66)])),
              L(blob([(62, 12), (88, 36), (86, 62), (76, 58)], 6), 'shade', 'b', False), sheen(24, 48, 14, 3),
              spk((14, 44), (34, 38), (20, 64), 5, z='f'), spk((34, 38), (54, 36), (44, 58), 5, z='f'),
              spk((54, 36), (72, 40), (64, 58), 5, z='f', light_left=False), spk((70, 42), (88, 46), (84, 64), 4, z='f', light_left=False)],
    'side': [spk((20, 26), (40, 12), (-4, -4), 7), spk((42, 10), (62, 8), (58, -12), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 14, 3),
             spk((56, 30), (86, 40), (90, 60), 5, z='f', light_left=False)],
    'back': [spk((4, 40), (16, 24), (-18, 4), 6), spk((84, 24), (96, 40), (118, 4), 6, light_left=False), spk((40, 10), (58, 8), (46, -10), 5),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Victoria Vanguard: melena roja hasta la mandíbula con las
# puntas muy abiertas hacia fuera y un gorro de lana azul petróleo con franjas crema; coloretes y ojos grandes
CHARS['victoria-vanguard'] = {
    'body': 'chica', 'pal': pal('#c84040', '#fcd8b8', hat='#2e5a6a', hat_d='#1e3e4a', band='#f0e8d0', band_d='#c8a060', blush='#f09080'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(12, 50), (88, 50), (92, 72), (110, 92), (96, 98), (84, 86), (82, 64), (18, 64), (16, 86), (4, 98), (-10, 92), (8, 72)])),
              L(blob([(84, 66), (92, 74), (106, 90), (96, 94), (86, 84)], 5), 'shade', 'b', False),
              spk((16, 54), (34, 52), (22, 70), 4, z='f'), spk((32, 52), (50, 52), (40, 66), 4, z='f'),
              spk((50, 52), (68, 52), (60, 66), 4, z='f', light_left=False), spk((66, 52), (84, 54), (78, 70), 4, z='f', light_left=False),
              L(blob([(12, 54), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (88, 54), (50, 50)]), 'hat', 'f', ln=True),
              L(quad((12, 36), (50, 28), (88, 36)) + quad((88, 48), (50, 40), (12, 48)), 'band', 'f', ln=True),
              L(quad((12, 42), (50, 34), (88, 42)), 'band_d', 'f', False, False, 1.4),
              L(blob([(62, 8), (88, 28), (88, 36), (70, 32)], 5), 'hat_d', 'f', False),
              L(ell(24, 86, 4, 2.6), 'blush', 'f', False), L(ell(76, 86, 4, 2.6), 'blush', 'f', False)],
    'side': [L(blob([(56, 64), (22, 60), (8, 70), (2, 92), (-14, 102), (10, 104), (30, 92), (48, 92), (54, 78)])),
             L(blob([(6, 72), (10, 92), (-6, 100), (2, 88)], 4), 'shade', 'b', False),
             L(blob(SIDE_SKULL)),
             L(blob([(12, 54), (10, 28), (26, 8), (54, 2), (80, 10), (92, 30), (92, 54), (50, 52)]), 'hat', 'f', ln=True),
             L(quad((12, 34), (50, 26), (92, 32)) + quad((92, 46), (50, 40), (12, 46)), 'band', 'f', ln=True),
             spk((60, 52), (84, 52), (88, 72), 5, z='f', light_left=False),
             L(ell(80, 86, 3.6, 2.4), 'blush', 'f', False)],
    'back': [L(blob([(12, 50), (88, 50), (92, 72), (110, 92), (96, 100), (70, 94), (50, 98), (30, 94), (4, 100), (-10, 92), (8, 72)])),
             L(blob([(58, 54), (92, 72), (104, 92), (70, 92)], 6), 'shade', 'b', False),
             L(blob([(12, 58), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (88, 58), (50, 60)]), 'hat', 'f', ln=True),
             L(quad((12, 38), (50, 30), (88, 38)) + quad((88, 50), (50, 42), (12, 50)), 'band', 'f', ln=True),
             L(quad((12, 44), (50, 36), (88, 44)), 'band_d', 'f', False, False, 1.4)],
}

# ------------------------------------------------------------------ Suzette Hartland: piel morena, melena lisa verde azulado larga
# con raya al lado y mechones junto a la cara; ojos grandes con pestañas y labios marcados
CHARS['suzette-hartland'] = {
    'body': 'chica', 'pal': pal('#5aa8ac', '#c88a54', iris='#4a4a7a', lip='#a04a3a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(10, 66), (24, 52), (42, 44), (60, 50), (76, 54), (90, 66)]},
    'front': [L(blob([(6, 104), (2, 56), (12, 18), (50, 6), (88, 18), (98, 56), (94, 104), (82, 100), (82, 64), (18, 64), (18, 100)])),
              L(blob([(62, 14), (96, 48), (92, 100), (84, 98)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              strand([(40, 8), (28, 48)], 'deep', 'b', 1.1),
              L(blob([(10, 54), (22, 56), (24, 96), (16, 104), (8, 84)]), 'mid', 'f'), L(blob([(90, 54), (78, 56), (76, 96), (84, 104), (92, 84)]), 'mid', 'f'),
              strand([(22, 58), (24, 96), (18, 102)], OUTC, 'f', 1.0), strand([(78, 58), (76, 96), (82, 102)], OUTC, 'f', 1.0),
              L(quad((44, 93), (50, 95), (56, 93)), 'lip', 'f', False, False, 1.6)],
    'side': [L(blob([(54, 104), (14, 106), (0, 64), (4, 28), (24, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 76), (58, 100)])),
             L(blob([(4, 50), (8, 98), (44, 102), (24, 72)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(22, 32), (14, 100)], 'shade', 'b', 1.0), strand([(40, 28), (36, 102)], 'shade', 'b', 1.0),
             spk((56, 30), (90, 40), (92, 70), 5, z='f', light_left=False),
             L([(84, 93), (88, 93)], 'lip', 'f', False, False, 1.6)],
    'back': [L(blob([(6, 104), (2, 56), (12, 18), (50, 6), (88, 18), (98, 56), (94, 104), (50, 110)])),
             L(blob([(58, 14), (96, 48), (92, 102), (66, 108)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
             strand([(50, 10), (50, 104)], 'deep', 'b', 1.2)],
}

# ------------------------------------------------------------------ Darren LaChance (portero): pelo castaño oliva muy rizado y
# despeinado, abultado; ojos grandes y sonrisa tímida
CHARS['darren-lachance'] = {
    'body': 'normal', 'pal': pal('#6a5a1e', '#f8c890', iris='#3a4a6a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [L(bumpy(50, 32, 48, 30, 16, 0.09)), L(bumpy(12, 58, 10, 12, 6, 0.12)), L(bumpy(88, 58, 10, 12, 6, 0.12)),
              L(bumpy(68, 36, 24, 20, 8, 0.09), 'shade', 'b', False), L(ell(32, 12, 10, 4), 'light', 'b', False),
              spk((12, 42), (30, 38), (16, 64), 5, z='f'), spk((30, 38), (48, 36), (38, 60), 5, z='f'),
              spk((52, 36), (70, 38), (62, 60), 5, z='f', light_left=False), spk((70, 40), (88, 44), (84, 64), 5, z='f', light_left=False)],
    'side': [L(bumpy(44, 34, 46, 30, 16, 0.09)), L(bumpy(18, 62, 12, 14, 6, 0.12)),
             L(blob(SIDE_SKULL)), L(bumpy(26, 46, 18, 22, 8, 0.09), 'shade', 'b', False),
             spk((56, 30), (86, 38), (90, 62), 5, z='f', light_left=False)],
    'back': [L(bumpy(50, 36, 48, 34, 16, 0.09)), L(bumpy(50, 72, 34, 16, 10, 0.12)),
             L(bumpy(66, 46, 24, 26, 8, 0.09), 'shade', 'b', False), L(ell(32, 14, 10, 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Eugene Conwell (sin modelo 3D; su retrato): pelo verde grisáceo
# en casco con flequillo de mechones, ojos afilados, un colmillo y marcas en las mejillas
CHARS['eugene-conwell'] = {
    'body': 'bajito', 'pal': pal('#7a8a6a', '#f6c08e', mark='#d07a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 94, 'big_ears': 1, 'ear_out': 2, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 36, 68) + [
              L([(24, 86), (30, 88)], 'mark', 'f', False, False, 1.2), L([(76, 86), (70, 88)], 'mark', 'f', False, False, 1.2)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False),
             L([(78, 86), (84, 88)], 'mark', 'f', False, False, 1.2)],
    'back': [L(blob(BOB_B))] + bob_shade('back'),
}
