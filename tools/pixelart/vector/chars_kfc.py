"""Inazuma Kids FC (IE1): el equipo de niños del barrio (todos con el cuerpo bajito); gorras, gorros, pañuelos, gafas de
aviador y moños, con sus modelos 3D como referencia (Michael Riverside no tiene modelo: su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
BLUSH = '#f09070'


def blush(side=False):
    if side:
        return [L(ell(80, 86, 4, 2.6), 'blush', 'f', False)]
    return [L(ell(26, 86, 5, 3), 'blush', 'f', False), L(ell(74, 86, 5, 3), 'blush', 'f', False)]


def cap(view, c='cap', cd='cap_d', y=56, peak=True):
    """Gorra o gorro que cubre la cabeza hasta la frente (con visera opcional)."""
    if view == 'side':
        out = [L(blob([(12, y + 6), (10, 30), (26, 8), (54, 0), (80, 8), (92, 28), (92, y), (50, y - 2)]), c, 'f', ln=True),
               L(blob([(12, y), (16, 28), (30, 14), (34, y - 4)], 6), cd, 'f', False)]
        if peak:
            out.append(L(blob([(80, y - 6), (108, y - 2), (110, y + 4), (84, y + 4)], 5), cd, 'f', ln=True))
        return out
    out = [L(blob([(10, y + 4), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, y + 4), (50, y)]), c, 'f', ln=True),
           L(blob([(60, 4), (90, 28), (90, y + 2), (70, y)], 6), cd, 'f', False)]
    if peak and view == 'front':
        out.append(L(blob([(12, y), (50, y - 6), (88, y), (92, y + 8), (50, y + 4), (8, y + 8)], 6), cd, 'f', ln=True))
    return out


# ------------------------------------------------------------------ Herman Muller (portero): gorra marrón de pirata con una
# calavera y unos cordones a los lados, pelo negro que asoma por la nuca; ojos redondos, cejas enfadadas y boca abierta gritando
CHARS['herman-muller'] = {
    'body': 'bajito', 'pal': pal('#2a2422', '#fcc08a', cap='#5e3a30', cap_d='#40261e', skull='#e8e0c8', nose='#d8945a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 82, 2.4), 'nose_side': (90, 80, 2.4), 'big_ears': 1, 'hairline': False},
    'front': [L(blob([(12, 74), (14, 56), (86, 56), (88, 74)]))] + cap('front', y=54, peak=False)
             + [L(quad((10, 60), (2, 72), (8, 82)), 'cap_d', 'f', False, False, 1.6), L(quad((90, 60), (98, 72), (92, 82)), 'cap_d', 'f', False, False, 1.6),
                L(ell(72, 26, 7, 6.4), 'skull', 'f', ln=True), L(ell(70, 26, 1.6, 1.8), OUTC, 'f', False), L(ell(75, 26, 1.6, 1.8), OUTC, 'f', False),
                L(blob([(42, 88), (58, 88), (60, 98), (50, 102), (40, 98)], 5), (110, 40, 40, 255), 'f', ln=True),
                L(blob([(44, 89), (56, 89), (54, 92), (46, 92)], 3), WHITE, 'f', False)],
    'side': [L(blob(SIDE_SKULL))] + cap('side', y=54, peak=False)
            + [L(quad((26, 56), (20, 70), (26, 80)), 'cap_d', 'f', False, False, 1.6), L(blob([(80, 88), (90, 88), (90, 98), (82, 98)], 4), (110, 40, 40, 255), 'f', ln=True)],
    'back': [L(blob(SKULL_B))] + back_hair() + cap('back', y=54, peak=False)
            + [L(quad((10, 60), (2, 72), (8, 82)), 'cap_d', 'f', False, False, 1.6), L(quad((90, 60), (98, 72), (92, 82)), 'cap_d', 'f', False, False, 1.6)],
}

# ------------------------------------------------------------------ Keth Claus: media melena verde oliva con un flequillo largo
# que le tapa un ojo; mirada seria
CHARS['keth-claus'] = {
    'body': 'bajito', 'pal': pal('#4a4a1e', '#f6c08e', iris='#5a5a5a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + [
              L(blob([(12, 40), (40, 26), (66, 30), (64, 60), (56, 86), (46, 90), (40, 70), (24, 56)]), 'mid', 'f'),
              L(blob([(44, 32), (62, 34), (58, 72), (50, 88), (48, 60)], 5), 'shade', 'f', False),
              strand([(64, 32), (62, 60), (52, 88)], OUTC, 'f', 1.0),
              spk((66, 38), (88, 44), (84, 72), 5, z='f', light_left=False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 84), 6, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [strand([(x, 14), (x + (x - 50) * 0.15, 86)], 'deep', 'b', 1.0) for x in (30, 44, 56, 70)],
}

# ------------------------------------------------------------------ Robert Silver: gorra de béisbol gris azulada con el frontal
# crema, el logo amarillo del KFC y la visera calada hasta los ojos; melena negra morada que se abre en puntas hacia los lados y
# una sonrisa enorme con los dientes
CHARS['robert-silver'] = {
    'body': 'bajito', 'pal': pal('#3a3040', '#fcc08a', cap='#4e5e6a', cap_d='#36424c', front='#dcc8b4', logo='#e8b828'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 90, 'hairline': False},
    'front': [L(blob([(4, 70), (-14, 76), (-4, 84), (20, 82), (80, 82), (104, 84), (114, 76), (96, 70)]))] + cap('front', y=60, peak=False)
             + [L(blob([(24, 46), (22, 20), (36, 6), (50, 2), (64, 6), (78, 20), (76, 46), (50, 50)]), 'front', 'f', ln=True),
                L([(44, 28), (54, 22), (50, 30), (58, 30), (46, 42), (50, 34), (42, 34)], 'logo', 'f', ln=True),
                L(blob([(6, 60), (50, 52), (94, 60), (96, 74), (50, 68), (4, 74)], 6), 'cap_d', 'f', ln=True)],
    'side': [L(blob([(30, 64), (6, 66), (-12, 80), (4, 84), (30, 80), (50, 82)])), L(blob(SIDE_SKULL))] + cap('side', y=60, peak=False)
            + [L(blob([(60, 10), (80, 8), (92, 28), (92, 56), (72, 56), (64, 30)]), 'front', 'f', ln=True),
               L(blob([(82, 54), (114, 58), (116, 66), (84, 64)], 5), 'cap_d', 'f', ln=True)],
    'back': [L(blob([(4, 72), (-14, 80), (-4, 88), (20, 86), (50, 92), (80, 86), (104, 88), (114, 80), (96, 72)]))] + cap('back', y=60, peak=False)
            + [L(ell(50, 58, 7, 3), 'cap_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Izzy Island: pelo azul petróleo abultado con un mechón hacia
# arriba, gafas rectangulares, pecas y ceño
CHARS['izzy-island'] = {
    'body': 'bajito', 'pal': pal('#2e4a5a', '#fcdcc0', freckle='#c88a5a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'glasses': (60, 56, 60, 255), 'glasses_rect': True, 'hairline': (58, 50)},
    'front': [L(blob([(10, 70), (8, 40), (20, 12), (46, 2), (64, 4), (82, 16), (92, 40), (90, 70), (80, 62), (20, 62)])),
              L(blob([(62, 10), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3)] + fringe(4, 38, 62)
             + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((24, 86), (28, 88), (76, 86), (72, 88))],
    'side': [L(blob([(46, 90), (20, 86), (8, 60), (10, 28), (28, 6), (60, 0), (84, 12), (94, 34), (90, 52), (74, 48), (60, 52), (52, 66), (50, 84)])),
             L(blob([(12, 46), (16, 80), (38, 86), (26, 62)], 6), 'shade', 'b', False), sheen(30, 62, 10, 3),
             spk((56, 30), (88, 40), (92, 62), 5, z='f', light_left=False)],
    'back': [L(blob([(10, 76), (8, 40), (20, 12), (46, 2), (64, 4), (82, 16), (92, 40), (90, 76), (66, 86), (34, 86)])),
             L(blob([(58, 10), (90, 38), (88, 74), (66, 84)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3)],
}

# ------------------------------------------------------------------ Sothern Newman: cara grande y ancha, pelo castaño corto con un
# pico sobre la frente; ojos pequeños y sonrisa pícara
SOTH_FACE = blob([(14, 54), (50, 46), (86, 54), (90, 76), (82, 96), (64, 106), (50, 108), (36, 106), (18, 96), (10, 76)])
CHARS['sothern-newman'] = {
    'body': 'bajito', 'pal': pal('#5a3a30', '#f6c08e'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'mouth_w': 12, 'face_front': SOTH_FACE, 'nose': (50, 84, 2.4),
             'hairline': [(10, 60), (30, 50), (44, 48), (50, 56), (56, 48), (70, 50), (90, 60)]},
    'front': [L(blob([(10, 64), (8, 36), (22, 12), (50, 4), (78, 12), (92, 36), (90, 64)])),
              L(blob([(62, 10), (90, 34), (88, 62), (76, 58)], 6), 'shade', 'b', False), sheen(24, 50, 16, 3)],
    'side': [L(blob([(46, 74), (20, 72), (10, 50), (14, 26), (30, 8), (58, 4), (82, 14), (94, 34), (80, 40), (62, 42), (52, 54)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 50)], 6), 'shade', 'b', False), sheen(32, 64, 14, 3)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Bart Grantham: pelo rubio rosado muy despeinado y abultado
# con unas gafas de aviador en la frente sujetas con una cinta rosa; coloretes y sonrisa
BART_TOP = [spk((6, 58), (10, 40), (-14, 46), 6), spk((12, 38), (24, 20), (-6, 6), 6), spk((24, 20), (42, 10), (24, -14), 6),
            spk((42, 10), (60, 10), (56, -16), 6, light_left=False), spk((60, 12), (76, 20), (92, -2), 6, light_left=False),
            spk((78, 26), (90, 42), (112, 32), 6, light_left=False), spk((88, 46), (94, 62), (110, 64), 5, light_left=False)]
CHARS['bart-grantham'] = {
    'body': 'bajito', 'pal': pal('#c89a80', '#fcc08a', light='#f0dcb0', strap='#e07a8a', rim='#c8c0a8', lens='#4a5a3a', blush=BLUSH),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': BART_TOP + [L(blob([(10, 72), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 72), (80, 64), (20, 64)])),
                         L(blob([(62, 12), (90, 38), (88, 68), (78, 64)], 6), 'shade', 'b', False), L(ell(40, 18, 12, 6), 'light', 'b', False),
                         spk((12, 50), (28, 46), (16, 74), 4, z='f'), spk((72, 46), (88, 50), (86, 74), 4, z='f', light_left=False),
                         L(quad((10, 44), (50, 36), (90, 44)) + quad((90, 50), (50, 42), (10, 50)), 'strap', 'f', ln=True),
                         L([(20, 34), (44, 34), (44, 48), (20, 48)], 'rim', 'f', ln=True), L([(56, 34), (80, 34), (80, 48), (56, 48)], 'rim', 'f', ln=True),
                         L([(23, 37), (41, 37), (41, 45), (23, 45)], 'lens', 'f', False), L([(59, 37), (77, 37), (77, 45), (59, 45)], 'lens', 'f', False),
                         L([(44, 40), (56, 40)], 'strap', 'f', False, False, 2.4)] + blush(),
    'side': [spk((16, 40), (24, 22), (-16, 18), 7), spk((24, 24), (42, 12), (10, -14), 7), spk((42, 12), (62, 6), (56, -18), 7),
             spk((14, 58), (16, 40), (-16, 52), 6), spk((18, 74), (22, 58), (-8, 82), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 12), (82, 22), (98, 2), 6, light_left=False),
             L(quad((14, 44), (50, 36), (92, 42)) + quad((92, 50), (50, 44), (14, 52)), 'strap', 'f', ln=True),
             L([(78, 30), (94, 32), (94, 48), (78, 48)], 'rim', 'f', ln=True), L([(82, 34), (92, 35), (92, 45), (82, 45)], 'lens', 'f', False)] + blush(True),
    'back': BART_TOP + [L(blob([(10, 74), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 74), (66, 88), (34, 88)])),
                        spk((12, 72), (30, 86), (8, 98), 5), spk((30, 88), (50, 92), (40, 108), 5), spk((50, 92), (70, 88), (62, 108), 5, light_left=False),
                        spk((70, 86), (88, 72), (92, 98), 5, light_left=False),
                        L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False), L(ell(50, 28, 14, 10), 'light', 'b', False),
                        L(quad((8, 50), (50, 44), (92, 50)) + quad((92, 56), (50, 50), (8, 56)), 'strap', 'f', ln=True)],
}

# ------------------------------------------------------------------ Irwin Hall: corte de tazón verde oliva oscuro con flequillo de
# mechones; ojos grandes y boca seria
CHARS['irwin-hall'] = {
    'body': 'bajito', 'pal': pal('#3e4224', '#fcd8b8'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(5, 36, 64),
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (88, 40), (92, 66), 5, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back'),
}

# ------------------------------------------------------------------ Taylor Higgins: gorro de lana rosa grisáceo con dos orejas
# de gato y un gatito negro bordado delante; asoma un mechón castaño rojizo sobre la frente; coloretes y sonrisa
CHARS['taylor-higgins'] = {
    'body': 'bajito', 'pal': pal('#8a3a1e', '#fcc08a', cap='#c4aca4', cap_d='#9c8078', blush=BLUSH),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(14, 74), (14, 56), (86, 56), (86, 74)])),
              L([(8, 30), (4, 0), (26, 14)], 'cap', 'f', ln=True), L([(92, 30), (96, 0), (74, 14)], 'cap', 'f', ln=True)] + cap('front', y=56, peak=False)
             + [spk((40, 54), (52, 52), (42, 72), 4, z='f'),
                L(ell(50, 40, 7, 5), OUTC, 'f', False), L([(44, 38), (45, 32), (48, 36)], OUTC, 'f', False), L([(56, 38), (55, 32), (52, 36)], OUTC, 'f', False)]
             + blush(),
    'side': [L(blob(SIDE_SKULL)), L([(30, 16), (36, -10), (50, 6)], 'cap', 'f', ln=True)] + cap('side', y=56, peak=False)
            + [spk((70, 54), (84, 54), (84, 70), 3, z='f', light_left=False)] + blush(True),
    'back': [spk((24, 80), (40, 84), (28, 96), 4), spk((40, 84), (60, 84), (50, 98), 4), spk((60, 84), (76, 80), (72, 96), 4, light_left=False),
             L(blob(SKULL_B)), L([(8, 30), (4, 0), (26, 14)], 'cap', 'f', ln=True), L([(92, 30), (96, 0), (74, 14)], 'cap', 'f', ln=True)]
            + cap('back', y=62, peak=False),
}

# ------------------------------------------------------------------ Jamie Cool: pelo morado oscuro despeinado con pinchos y una
# coleta corta en la nuca; ojos rojos afilados
CHARS['jamie-cool'] = {
    'body': 'bajito', 'pal': pal('#3e3048', '#f6b878', iris='#c03a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [spk((10, 52), (16, 38), (-4, 40), 3), spk((30, 16), (42, 12), (32, -2), 3), spk((46, 10), (56, 10), (54, -6), 3, light_left=False),
              spk((66, 16), (78, 22), (86, 8), 3, light_left=False), spk((86, 38), (92, 52), (104, 50), 3, light_left=False),
              L(blob([(8, 76), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 76), (80, 66), (20, 66)])),
              L(blob([(62, 12), (92, 38), (90, 72), (80, 68)], 6), 'shade', 'b', False)] + fringe(5, 36, 66),
    'side': [L(blob([(20, 64), (4, 74), (-6, 96), (4, 98), (16, 82), (26, 72)]), 'shade', 'b', ln=True),
             spk((18, 38), (26, 20), (-6, 16), 6), spk((28, 20), (46, 10), (24, -10), 6), spk((14, 56), (16, 40), (-10, 50), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((52, 10), (72, 14), (78, -6), 5, light_left=False), spk((56, 30), (88, 40), (92, 68), 6, z='f', light_left=False)],
    'back': [spk((10, 52), (16, 38), (-4, 40), 3), spk((30, 16), (42, 12), (32, -2), 3), spk((46, 10), (56, 10), (54, -6), 3, light_left=False),
             spk((66, 16), (78, 22), (86, 8), 3, light_left=False), spk((86, 38), (92, 52), (104, 50), 3, light_left=False),
             L(blob([(8, 76), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 76), (66, 88), (34, 88)])),
             L(blob([(58, 12), (92, 38), (90, 74), (66, 86)], 6), 'shade', 'b', False),
             L(blob([(44, 78), (58, 78), (60, 96), (52, 112), (44, 96)]), 'shade', 'f', ln=True)],
}

# ------------------------------------------------------------------ Hans Randall: piel tostada, pelo rubio que asoma bajo un pañuelo
# azul atado a la cabeza con una franja blanca en medio y las puntas del nudo en la nuca; ojos grandes, pecas y sonrisa
CHARS['hans-randall'] = {
    'body': 'bajito', 'pal': pal('#e0b040', '#c88a4a', cap='#3a7aa0', cap_d='#285a7a', freckle='#8a5a2a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 70), (12, 54), (88, 54), (90, 70)])),
              spk((12, 56), (24, 56), (16, 70), 3, z='f'), spk((24, 56), (36, 56), (30, 66), 3, z='f'),
              spk((64, 56), (76, 56), (70, 66), 3, z='f', light_left=False), spk((76, 56), (88, 56), (86, 70), 3, z='f', light_left=False)]
             + cap('front', y=56, peak=False) + [L([(46, 0), (54, 0), (54, 56), (46, 56)], (236, 232, 224, 255), 'f', ln=True)]
             + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((24, 86), (28, 88), (76, 86), (72, 88))],
    'side': [L(blob(SIDE_SKULL))] + cap('side', y=56, peak=False)
            + [L(blob([(14, 50), (-6, 52), (-14, 62), (0, 62), (16, 58)], 4), 'cap', 'f', ln=True), spk((72, 54), (86, 54), (86, 68), 3, z='f', light_left=False)],
    'back': [spk((14, 72), (30, 80), (16, 88), 4), spk((70, 80), (86, 72), (84, 88), 4, light_left=False),
             L(blob(SKULL_B))] + cap('back', y=72, peak=False)
            + [L([(46, 0), (54, 0), (54, 72), (46, 72)], (236, 232, 224, 255), 'f', ln=True),
               L(blob([(50, 72), (30, 78), (22, 92), (40, 86)], 4), 'cap', 'f', ln=True), L(blob([(50, 72), (70, 78), (78, 92), (60, 86)], 4), 'cap', 'f', ln=True),
               L(ell(50, 74, 5, 4), 'cap_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Millie Moonlight: pelo rosa parduzco con flequillo y dos
# coletas abiertas a los lados; ojos grandes y sonrisa
CHARS['millie-moonlight'] = {
    'body': 'bajito', 'pal': pal('#9a6a6a', '#fcdcc4'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [L(blob([(14, 30), (2, 26), (-14, 50), (-10, 70), (6, 52), (14, 44)])), L(blob([(86, 30), (98, 26), (114, 50), (110, 70), (94, 52), (86, 44)])),
              L(blob([(-6, 48), (-10, 66), (2, 54)], 4), 'shade', 'b', False), L(blob([(106, 48), (110, 66), (98, 54)], 4), 'shade', 'b', False),
              L(blob([(10, 76), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (90, 76), (80, 70), (80, 60), (20, 60), (20, 70)])),
              L(blob([(62, 12), (92, 38), (88, 74), (82, 72)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3)] + fringe(5, 36, 62),
    'side': [L(blob([(24, 24), (10, 18), (-10, 28), (-14, 52), (2, 46), (20, 36)])),
             L(blob(BOB_S)), L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 66), 5, z='f', light_left=False)],
    'back': [L(blob([(14, 30), (2, 26), (-14, 50), (-10, 70), (6, 52), (14, 44)])), L(blob([(86, 30), (98, 26), (114, 50), (110, 70), (94, 52), (86, 44)])),
             L(blob([(10, 80), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (90, 80), (50, 86)]))] + bob_shade('back')
            + [L([(40, 70), (50, 82), (60, 70)], 'shade', 'b', False, False, 1.2)],
}

# ------------------------------------------------------------------ Michael Riverside (sin modelo 3D; su retrato): piel morena,
# afro castaño rojizo muy abultado, ceño fruncido, marcas en las mejillas y boca apretada
CHARS['michael-riverside'] = {
    'body': 'bajito', 'pal': pal('#6a2a1a', '#a8683a', mark='#5a2a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'nose': (50, 83, 2.6), 'hairline': (56, 48)},
    'front': [L(bumpy(50, 30, 50, 34, 16, 0.08)), L(bumpy(70, 34, 24, 24, 8, 0.08), 'shade', 'b', False), L(ell(30, 12, 12, 5), 'light', 'b', False),
              L(blob([(6, 70), (4, 42), (96, 42), (94, 70), (82, 60), (18, 60)])),
              L(ell(50, 60, 1.4, 1.4), OUTC, 'f', False),
              L([(22, 80), (28, 86)], 'mark', 'f', False, False, 1.2), L([(78, 80), (72, 86)], 'mark', 'f', False, False, 1.2)],
    'side': [L(bumpy(42, 32, 50, 34, 16, 0.08)), L(blob(SIDE_SKULL)), L(bumpy(22, 46, 20, 24, 8, 0.08), 'shade', 'b', False),
             L([(78, 80), (84, 86)], 'mark', 'f', False, False, 1.2)],
    'back': [L(bumpy(50, 34, 50, 38, 16, 0.08)), L(bumpy(68, 44, 24, 26, 8, 0.08), 'shade', 'b', False), L(ell(30, 14, 12, 5), 'light', 'b', False),
             L(bumpy(50, 74, 36, 14, 10, 0.1))],
}

# ------------------------------------------------------------------ Karl Blue: pelo castaño corto con un pequeño tupé, orejas
# grandes y mirada de párpados caídos con sonrisa
CHARS['karl-blue'] = {
    'body': 'bajito', 'pal': pal('#7a4220', '#f6c08e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'big_ears': 1.5, 'ear_out': 2, 'hairline': (54, 46)},
    'front': [L(blob([(14, 62), (12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (86, 62)])),
              L(blob([(62, 10), (88, 34), (86, 60), (74, 56)], 6), 'shade', 'b', False), sheen(26, 50, 12, 3),
              L(quad((30, 18), (50, 8), (70, 18)), 'shade', 'b', False, False, 1.2),
              L([(28, 73), (42, 74)], OUTC, 'f', False, False, 2.2), L([(72, 73), (58, 74)], OUTC, 'f', False, False, 2.2)],
    'side': [L(blob([(44, 74), (20, 72), (10, 50), (14, 24), (32, 6), (60, 2), (84, 12), (92, 30), (80, 38), (62, 40), (52, 54)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 50)], 6), 'shade', 'b', False), sheen(32, 64, 12, 3)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Theakston Plank: pelo rubio oscuro de pinchos grandes hacia
# arriba y a los lados con una diadema gris; ojos verdes y cara redonda
THEA_TOP = [spk((6, 62), (10, 40), (-22, 50), 6), spk((14, 32), (32, 14), (-6, -6), 7), spk((34, 12), (56, 8), (46, -28), 7),
            spk((58, 10), (78, 22), (96, -12), 7, light_left=False), spk((82, 30), (92, 52), (120, 40), 6, light_left=False)]
CHARS['theakston-plank'] = {
    'body': 'bajito', 'pal': pal('#c09a50', '#fcc89a', iris='#6a8a3a', band='#8a8a90'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': THEA_TOP + [L(blob([(10, 72), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 72), (80, 64), (20, 64)])),
                         L(blob([(62, 12), (90, 38), (88, 68), (78, 64)], 6), 'shade', 'b', False),
                         L(quad((12, 46), (50, 34), (88, 46)), 'band', 'f', False, False, 2.6)] + fringe(4, 44, 66),
    'side': [spk((16, 40), (24, 22), (-20, 14), 8), spk((24, 24), (42, 12), (8, -18), 8), spk((42, 12), (62, 6), (52, -24), 8),
             spk((14, 58), (16, 40), (-18, 52), 7), spk((18, 76), (22, 58), (-10, 84), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 12), (82, 22), (98, -6), 6, light_left=False),
             L(quad((16, 44), (50, 34), (90, 42)), 'band', 'f', False, False, 2.6), spk((56, 34), (88, 42), (92, 66), 5, z='f', light_left=False)],
    'back': THEA_TOP + [L(blob([(10, 74), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 74), (66, 88), (34, 88)])),
                        spk((12, 72), (30, 86), (6, 100), 6), spk((30, 88), (50, 92), (40, 110), 6), spk((50, 92), (70, 88), (64, 110), 6, light_left=False),
                        spk((70, 86), (88, 72), (94, 100), 6, light_left=False),
                        L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Ken Cake: cara muy redonda y grande, pelo castaño oscuro
# pegado al cráneo con dos moños a los lados de la cabeza; ojos cerrados de felicidad y nariz pequeña
KEN_FACE = blob([(10, 56), (50, 48), (90, 56), (96, 78), (88, 98), (68, 108), (50, 110), (32, 108), (12, 98), (4, 78)])
CHARS['ken-cake'] = {
    'body': 'bajito', 'pal': pal('#3a3020', '#f6b878'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'face_front': KEN_FACE, 'nose': (50, 84, 2.4), 'ear_out': 4,
             'hairline': (54, 46)},
    'front': [L(bumpy(10, 16, 13, 13, 8, 0.1)), L(bumpy(90, 16, 13, 13, 8, 0.1)),
              L(bumpy(14, 14, 6, 6, 6, 0.1), 'light', 'b', False), L(bumpy(86, 14, 6, 6, 6, 0.1), 'light', 'b', False),
              L(blob([(8, 62), (8, 36), (22, 14), (50, 8), (78, 14), (92, 36), (92, 62)])),
              L(blob([(62, 12), (90, 36), (90, 60), (76, 56)], 6), 'shade', 'b', False)],
    'side': [L(bumpy(34, 10, 13, 13, 8, 0.1)),
             L(blob([(44, 96), (16, 90), (6, 62), (10, 32), (28, 12), (56, 8), (80, 16), (92, 36), (78, 42), (60, 46), (52, 62), (50, 80)])),
             L(blob([(12, 46), (16, 80), (38, 88), (26, 62)], 6), 'shade', 'b', False)],
    'back': [L(bumpy(10, 18, 13, 13, 8, 0.1)), L(bumpy(90, 18, 13, 13, 8, 0.1)),
             L(blob([(8, 72), (8, 36), (22, 14), (50, 8), (78, 14), (92, 36), (92, 72), (70, 88), (30, 88)]))] + back_hair()
            + [strand([(50, 10), (50, 84)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Mitch Grumble: gorra de lana verde oliva tipo bombín con
# visera calada sobre los ojos; asoma pelo castaño claro despeinado por los lados y la nuca
CHARS['mitch-grumble'] = {
    'body': 'bajito', 'pal': pal('#9a8070', '#fcdcc0', cap='#4e4a24', cap_d='#36321a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob(BOB_F)), spk((10, 66), (20, 66), (12, 86), 3, z='f'), spk((80, 66), (90, 66), (88, 86), 3, z='f', light_left=False),
              spk((22, 64), (34, 64), (28, 80), 3, z='f'), spk((66, 64), (78, 64), (72, 80), 3, z='f', light_left=False)]
             + [L(blob([(2, 62), (0, 30), (18, 6), (50, 0), (82, 6), (100, 30), (98, 62), (50, 60)]), 'cap', 'f', ln=True),
                L(blob([(62, 4), (98, 30), (98, 60), (74, 60)], 6), 'cap_d', 'f', False),
                L(blob([(10, 58), (50, 52), (90, 58), (92, 70), (50, 66), (8, 70)], 6), 'cap_d', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side')
            + [L(blob([(6, 62), (4, 30), (24, 6), (56, 0), (84, 8), (98, 30), (98, 56), (50, 58)]), 'cap', 'f', ln=True),
               L(blob([(8, 56), (12, 30), (28, 14), (32, 56)], 6), 'cap_d', 'f', False),
               L(blob([(84, 52), (112, 56), (112, 64), (86, 64)], 5), 'cap_d', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back')
            + [spk((10, 80), (28, 88), (12, 100), 5), spk((28, 88), (48, 92), (36, 104), 5), spk((52, 92), (72, 88), (64, 104), 5, light_left=False),
               spk((72, 88), (90, 80), (88, 100), 5, light_left=False),
               L(blob([(2, 64), (0, 30), (18, 6), (50, 0), (82, 6), (100, 30), (98, 64), (50, 68)]), 'cap', 'f', ln=True),
               L(blob([(58, 4), (98, 30), (98, 62), (66, 66)], 6), 'cap_d', 'f', False)],
}

