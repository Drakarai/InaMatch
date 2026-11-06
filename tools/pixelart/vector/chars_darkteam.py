"""Makai Gundan Z / Dark Team (IE3): los demonios, con sus modelos 3D como referencia (contornos calcados sobre una rejilla
de unidades de cabeza). Las alas de murciélago van en la equipación (body.py)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def horns(view, c='horn', y=24, h=-14, spread=20, curl=0):
    """Dos cuernos que salen de lo alto de la cabeza hacia arriba y hacia fuera."""
    if view == 'front':
        return [L(outline([(50 - spread, y + 4), (50 - spread - 10 - curl, y - 6), (50 - spread - 4 - curl, h, 1), (50 - spread + 6, y - 4)]), c, 'f', ln=True),
                L(outline([(50 + spread, y + 4), (50 + spread + 10 + curl, y - 6), (50 + spread + 4 + curl, h, 1), (50 + spread - 6, y - 4)]), c, 'f', ln=True)]
    if view == 'side':
        return [L(outline([(54, y + 4), (60, y - 8), (62 + curl, h, 1), (68, y - 4)]), c, 'f', ln=True)]
    return [L(outline([(50 - spread, y + 4), (50 - spread - 10 - curl, y - 6), (50 - spread - 4 - curl, h, 1), (50 - spread + 6, y - 4)]), c, 'f', ln=True),
            L(outline([(50 + spread, y + 4), (50 + spread + 10 + curl, y - 6), (50 + spread + 4 + curl, h, 1), (50 + spread - 6, y - 4)]), c, 'f', ln=True)]


# Astaroth (portero): una capucha negra ajustada con un cráneo blanco en lo alto y dos cuernos de carnero blancos curvados a
# los lados; la cara pálida con pinturas negras alrededor de los ojos rojos y labios negros
CHARS['astaroth'] = {
    'body': 'normal', 'pal': pal('#24222a', '#fce4d4', iris='#a83a4a', hood='#24222a', horn='#ece4e0', horn_d='#b8aca8', paint='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(22, 30), (6, 16), (-12, 26), (-18, 44), (-12, 56), (0, 46), (14, 40)]), 'horn', 'f', ln=True),
              L(outline([(78, 30), (94, 16), (112, 26), (118, 44), (112, 56), (100, 46), (86, 40)]), 'horn', 'f', ln=True),
              L(outline([(10, 92), (8, 40), (18, 10), (50, -4), (82, 10), (92, 40), (90, 92), (78, 80), (76, 64), (50, 54, 1), (24, 64), (22, 80)]), 'hood', 'f', ln=True),
              L(outline([(40, 8), (50, 2), (60, 8), (58, 18), (42, 18)]), WHITE, 'f', ln=True), L(ell(46, 10, 1.6, 2), OUTC, 'f', False), L(ell(54, 10, 1.6, 2), OUTC, 'f', False),
              L(quad((22, 70), (30, 84), (28, 96)), 'paint', 'f', False, False, 1.6), L(quad((78, 70), (70, 84), (72, 96)), 'paint', 'f', False, False, 1.6)],
    'side': [L(outline([(14, 96), (8, 40), (20, 10), (50, -4), (78, 4), (94, 26), (92, 60), (80, 56), (66, 60), (56, 80), (50, 96)]), 'hood', 'f', ln=True),
             L(outline([(40, 30), (54, 22), (64, 36), (62, 60), (50, 72), (42, 60)]), 'horn', 'f', ln=True), L(outline([(46, 34), (56, 30), (58, 56), (50, 64)]), 'horn_d', 'f', False)],
    'back': [L(outline([(10, 92), (8, 40), (18, 10), (50, -4), (82, 10), (92, 40), (90, 92), (50, 100)]), 'hood', 'f', ln=True),
             L(outline([(14, 30), (-4, 16), (-18, 28), (-20, 46), (-12, 54), (0, 44), (12, 42)]), 'horn', 'f', ln=True),
             L(outline([(86, 30), (104, 16), (118, 28), (120, 46), (112, 54), (100, 44), (88, 42)]), 'horn', 'f', ln=True)],
}
# Bael: pelo gris azulado enorme de pinchos largos en todas direcciones, con mechones que le caen por la cara; ojos violetas
# y la boca seria
CHARS['bael'] = {
    'body': 'normal', 'pal': pal('#5a6078', '#fce0c8', iris='#5a3a8a', shade='#40465a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 18, 11, seed=2001, rx=60, ry=48, cy=40, lo=96)
             + [L(outline([(10, 80, 1), (14, 44), (28, 26), (50, 20), (72, 26), (86, 44), (90, 80, 1), (80, 58), (72, 68, 1), (64, 50), (56, 60, 1), (50, 48), (44, 64, 1), (36, 50), (28, 66, 1),
                           (20, 58)]), 'mid', 'f')],
    'side': messy('side', 26, 10, seed=2001, rx=56, ry=48, cy=40, nape=100, sweep=-0.4),
    'back': messy('back', 18, 11, seed=2001, rx=60, ry=48, cy=40, nape=100),
}
# Abigor: cabeza calva alargada y amarilla con un mechón marrón curvado en lo alto, orejas puntiagudas, un monóculo blanco
# grande sujeto con una cinta roja en diagonal y el otro ojo cerrado en un guiño; colmillos que asoman
CHARS['abigor'] = {
    'body': 'corpulento', 'pal': pal('#8a6a3a', '#f8c070', band='#d02a2a', rim='#ece4e0', lens='#8a6a6a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(12, 70), (-12, 66, 1), (8, 82)]), 'skin', 'b', ln=True), L(outline([(88, 70), (112, 66, 1), (92, 82)]), 'skin', 'b', ln=True),
              L(outline([(16, 64), (14, 20), (26, -2), (50, -10), (74, -2), (86, 20), (84, 64)]), 'skin'),
              L(outline([(42, 2), (36, -12), (46, -24), (58, -22), (50, -16), (52, 2)]), 'mid', 'f', ln=True),
              L(outline([(8, 80), (92, 20), (94, 28), (10, 88)]), 'band', 'f', ln=True),
              L(ell(30, 74, 11, 10), 'rim', 'f', ln=True), L(ell(30, 74, 6, 5.4), 'lens', 'f', ln=True),
              L([(62, 72), (68, 76), (62, 80)], OUTC, 'f', False, False, 1.8), L([(70, 74), (76, 74)], OUTC, 'f', False, False, 1.4),
              L(outline([(36, 104), (40, 98), (42, 108)]), WHITE, 'f', ln=True), L(outline([(64, 104), (60, 98), (58, 108)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(40, 100), (16, 90), (10, 40), (22, 6), (52, -8), (78, 2), (90, 30), (92, 70), (86, 100), (60, 108)]), 'skin'),
             L(outline([(46, 70), (30, 62, 1), (46, 82)]), 'skin', 'f', ln=True),
             L(outline([(50, -6), (48, -20), (58, -26), (62, -18), (56, -14), (58, -4)]), 'mid', 'f', ln=True),
             L(outline([(10, 54), (92, 60), (92, 68), (10, 62)]), 'band', 'f', ln=True), L(ell(94, 66, 4, 9), 'rim', 'f', ln=True)],
    'back': [L(outline([(16, 90), (14, 20), (26, -2), (50, -10), (74, -2), (86, 20), (84, 90), (50, 96)]), 'skin'),
             L(outline([(12, 70), (-12, 66, 1), (8, 82)]), 'skin', 'f', ln=True), L(outline([(88, 70), (112, 66, 1), (92, 82)]), 'skin', 'f', ln=True),
             L(outline([(8, 36), (92, 76), (90, 84), (8, 44)]), 'band', 'f', ln=True)],
}
# Behemoth: grandullón con un casco de toro gris azulado que le tapa la cara hasta la nariz, con dos cuernos blancos y un
# hocico azul; un manto de piel por los hombros y los dientes apretados
CHARS['behemoth'] = {
    'body': 'corpulento', 'pal': pal('#5a5e70', '#c8743e', helm='#6a6e84', helm_d='#4e5266', horn='#d8d0c8', snout='#2a5a6a', fur='#a8987a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(-8, 110), (-10, 80), (14, 70), (50, 76), (86, 70), (110, 80), (108, 110)]), 'fur', 'b', ln=True),
              L(outline([(14, 30), (-10, 26), (-16, 12, 1), (0, 18), (18, 18)]), 'horn', 'f', ln=True), L(outline([(86, 30), (110, 26), (116, 12, 1), (100, 18), (82, 18)]), 'horn', 'f', ln=True),
              L(outline([(6, 70), (4, 30), (18, 8), (50, 2), (82, 8), (96, 30), (94, 70), (70, 66), (64, 86), (36, 86), (30, 66)]), 'helm', 'f', ln=True),
              L(outline([(60, 6), (82, 12), (94, 36), (92, 68), (72, 62)]), 'helm_d', 'f', False),
              L(outline([(34, 72), (66, 72), (68, 90), (32, 90)]), 'snout', 'f', ln=True),
              L(ell(30, 48, 6, 5), WHITE, 'f', ln=True), L(ell(70, 48, 6, 5), WHITE, 'f', ln=True),
              L(outline([(28, 100), (72, 100), (68, 110), (32, 110)]), WHITE, 'f', ln=True), L([(30, 105), (70, 105)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(-20, 110), (-16, 80), (20, 70), (60, 80), (60, 110)]), 'fur', 'b', ln=True),
             L(outline([(4, 76), (4, 30), (22, 6), (54, 0), (80, 10), (100, 40), (116, 70), (110, 84), (92, 80), (70, 72), (40, 76)]), 'helm', 'f', ln=True),
             L(outline([(46, 8), (52, -14, 1), (60, 6)]), 'horn', 'f', ln=True), L(outline([(102, 66), (118, 70), (114, 86), (100, 82)]), 'snout', 'f', ln=True),
             L(ell(80, 44, 4, 5), WHITE, 'f', ln=True)],
    'back': [L(outline([(-12, 112), (-12, 72), (50, 66), (112, 72), (112, 112)]), 'fur', 'b', ln=True),
             L(outline([(14, 30), (-10, 26), (-16, 12, 1), (0, 18), (18, 18)]), 'horn', 'f', ln=True), L(outline([(86, 30), (110, 26), (116, 12, 1), (100, 18), (82, 18)]), 'horn', 'f', ln=True),
             L(outline([(4, 74), (4, 30), (18, 8), (50, 2), (82, 8), (96, 30), (96, 74), (50, 78)]), 'helm', 'f', ln=True)],
}
# Belial: melena verde oscuro lisa y larga con raya en medio hasta el pecho, con dos cuernos de pelo que se curvan hacia
# arriba a los lados; ojos negros grandes y la boca seria
CHARS['belial'] = {
    'body': 'delgado', 'pal': pal('#1e5a4a', '#fce4cc', iris='#1e1e2a', shade='#144236', horn='#1e5a4a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(16, 80), (18, 50), (34, 36), (50, 40), (66, 36), (82, 50), (84, 80)]},
    'front': longhair('front', 124, 0, part=True) + horns('front', 'horn', y=26, h=-16, spread=34, curl=4),
    'side': longhair('side', 124, 0) + horns('side', 'horn', y=20, h=-18),
    'back': longhair('back', 124, 0, part=True, ends=0) + horns('back', 'horn', y=26, h=-16, spread=34, curl=4),
}
# Jezebeth: media melena castaña lisa cortada en tazón hasta la barbilla con dos cuernos de pelo curvados hacia arriba; ojos
# cerrados con pestañas largas y la boca seria
CHARS['jezebeth'] = {
    'body': 'normal', 'pal': pal('#8a4a1a', '#fcdcc0', shade='#6a3410', horn='#8a4a1a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 94), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (90, 94), (80, 92), (80, 64), (64, 54), (50, 72, 1), (36, 54), (20, 64), (20, 92)])),
              L(outline([(60, 6), (84, 18), (94, 44), (90, 90), (80, 88), (80, 50)]), 'shade', 'b', False)]
             + [strand([(x, 8 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 54)], 'shade', 'b', 1.0) for x in (28, 40, 60, 72)]
             + horns('front', 'horn', y=22, h=-10, spread=28, curl=8),
    'side': [L(outline([(60, 90), (8, 92), (4, 40), (18, 10), (50, 0), (78, 8), (94, 28), (94, 52), (82, 50), (66, 54), (60, 66)])),
             L(outline([(6, 50), (36, 50), (52, 88), (10, 88)]), 'shade', 'b', False)] + horns('side', 'horn', y=18, h=-12),
    'back': [L(outline([(8, 94), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (92, 94), (50, 96)])),
             L(outline([(56, 6), (84, 18), (94, 44), (92, 92), (62, 94)]), 'shade', 'b', False)] + horns('back', 'horn', y=22, h=-10, spread=28, curl=8),
}
# Malphas: piel morena; melena blanca rosada lisa peinada a un lado que le tapa un ojo y le cae hasta los hombros, recogida
# atrás en una coleta; el otro ojo violeta y los labios azules
CHARS['malphas'] = {
    'body': 'normal', 'pal': pal('#ece0e4', '#8a5a3a', iris='#6a3a8a', shade='#c8b8c0', lip='#3a6ab0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': longhair('front', 108, 6)
             + [L(outline([(12, 66), (14, 40), (30, 22), (52, 16), (74, 22), (88, 40), (88, 64), (76, 56), (64, 56), (56, 70), (48, 92, 1), (42, 70), (32, 64), (20, 72)]), 'mid', 'f', ln=True),
                L(outline([(58, 94), (68, 92), (74, 96), (66, 100)]), 'lip', 'f', ln=True)],
    'side': longhair('side', 106, 6),
    'back': longhair('back', 100, 6, ends=0) + [L(rope((50, 80), (50, 100), (50, 118), 9), 'mid', 'f', ln=True)],
}
# Glasya: pelo rosa salmón en forma de seta enorme y plana que le cae por los lados hasta las mejillas; cara pálida de muñeca
# con coloretes, ojos rasgados y labios rojos
CHARS['glasya'] = {
    'body': 'normal', 'pal': pal('#d87070', '#fce8d8', iris='#3a6a6a', shade='#b05050', blush='#f09090', lip='#a83a4a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(-16, 74), (-18, 44), (0, 16), (30, 2), (70, 2), (100, 16), (118, 44), (116, 74), (90, 66), (80, 56), (50, 52), (20, 56), (10, 66)])),
              L(outline([(60, 4), (100, 18), (116, 46), (112, 72), (90, 64), (80, 40)]), 'shade', 'b', False),
              L(ell(24, 86, 6, 4), 'blush', 'f', False), L(ell(76, 86, 6, 4), 'blush', 'f', False),
              L(outline([(42, 96), (50, 94), (58, 96), (54, 102), (46, 102)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(60, 70), (40, 80), (0, 80), (-16, 60), (-8, 30), (16, 6), (56, -2), (90, 8), (106, 30), (100, 48), (84, 50), (70, 54)])),
             L(outline([(-12, 50), (40, 50), (52, 76), (2, 78)]), 'shade', 'b', False), L(ell(80, 86, 5, 3.4), 'blush', 'f', False)],
    'back': [L(outline([(-16, 76), (-18, 44), (0, 16), (30, 2), (70, 2), (100, 16), (118, 44), (116, 76), (90, 84), (50, 86), (10, 84)])),
             L(outline([(56, 4), (100, 18), (116, 46), (114, 76), (64, 84)]), 'shade', 'b', False)],
}
# Arachne: pelo verde oscuro abultado y redondo que le cae hasta la barbilla, con dos mechones que se curvan hacia arriba en
# espiral como cuernos a los lados; piel morena, ojos violetas y los labios negros
CHARS['arachne'] = {
    'body': 'normal', 'pal': pal('#1e6a2a', '#b07848', iris='#7a4ab0', shade='#144e1e', lip='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': (50, 40)},
    'front': [L(outline([(4, 88), (-2, 50), (6, 20), (30, 2), (70, 2), (94, 20), (102, 50), (96, 88), (82, 82), (80, 60), (20, 60), (18, 82)])),
              L(outline([(60, 4), (90, 20), (100, 50), (94, 86), (82, 80), (80, 40)]), 'shade', 'b', False),
              L(rope((6, 40), (-14, 20), (-4, 0), 10), 'mid', 'f', ln=True), L(rope((94, 40), (114, 20), (104, 0), 10), 'mid', 'f', ln=True),
              L(outline([(40, 96), (50, 94), (60, 96), (56, 102), (44, 102)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(56, 80), (40, 90), (8, 88), (-4, 60), (2, 24), (26, 4), (58, 0), (84, 10), (96, 30), (92, 48), (78, 48), (64, 54)])),
             L(outline([(0, 46), (36, 46), (48, 84), (10, 84)]), 'shade', 'b', False), L(rope((20, 30), (6, 4), (24, -10), 10), 'mid', 'f', ln=True)],
    'back': [L(outline([(4, 88), (-2, 50), (6, 20), (30, 2), (70, 2), (94, 20), (102, 50), (96, 88), (50, 94)])),
             L(outline([(56, 4), (90, 20), (100, 50), (94, 86), (62, 92)]), 'shade', 'b', False),
             L(rope((6, 40), (-14, 20), (-4, 0), 10), 'mid', 'f', ln=True), L(rope((94, 40), (114, 20), (104, 0), 10), 'mid', 'f', ln=True)],
}
# Thanatos: un casco morado con una franja blanca y dos cuernos grandes que se curvan hacia arriba; unas gafas de dos lentes
# azules redondas, orejas puntiagudas, la cara arrugada y una sonrisa enorme
CHARS['thanatos'] = {
    'body': 'normal', 'pal': pal('#5a2aa0', '#f4dcb8', helm='#5a2aa0', helm_d='#401e7a', rim='#a8a8b0', lens='#2a8ac8', mouth='#f0e4e0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(12, 70), (-14, 62, 1), (6, 84)]), 'skin', 'b', ln=True), L(outline([(88, 70), (114, 62, 1), (94, 84)]), 'skin', 'b', ln=True),
              L(blob(SKULL_F), 'skin'),
              L(outline([(6, 52), (8, 22), (22, 6), (50, 2), (78, 6), (92, 22), (94, 52), (50, 48)]), 'helm', 'f', ln=True),
              L(outline([(18, 20), (14, -8), (22, -30, 1), (28, -6), (32, 10)]), 'helm', 'f', ln=True), L(outline([(82, 20), (86, -8), (78, -30, 1), (72, -6), (68, 10)]), 'helm', 'f', ln=True),
              L(outline([(44, 4), (56, 4), (56, 48), (44, 48)]), WHITE, 'f', False),
              L(outline([(14, 66), (86, 66), (86, 80), (14, 80)]), 'rim', 'f', ln=True), L(ell(30, 73, 8, 8), 'rim', 'f', ln=True), L(ell(70, 73, 8, 8), 'rim', 'f', ln=True),
              L(ell(30, 73, 4, 4), 'lens', 'f', False), L(ell(70, 73, 4, 4), 'lens', 'f', False),
              L(outline([(16, 90), (50, 96), (84, 90), (76, 104), (50, 110), (24, 104)]), 'mouth', 'f', ln=True), L(quad((18, 94), (50, 102), (82, 94)), OUTC, 'f', False, False, 1.0)],
    'side': [L(blob(SIDE_SKULL), 'skin'), L(outline([(46, 70), (28, 60, 1), (46, 82)]), 'skin', 'f', ln=True),
             L(outline([(6, 56), (8, 22), (26, 4), (54, 0), (80, 8), (94, 26), (96, 50), (60, 50), (30, 60)]), 'helm', 'f', ln=True),
             L(outline([(40, 8), (36, -20), (50, -36, 1), (52, -14), (58, 4)]), 'helm', 'f', ln=True),
             L(outline([(46, 68), (96, 68), (96, 80), (48, 80)]), 'rim', 'f', ln=True), L(ell(94, 74, 4, 7), 'lens', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(6, 62), (8, 22), (22, 6), (50, 2), (78, 6), (92, 22), (94, 62), (50, 58)]), 'helm', 'f', ln=True),
             L(outline([(18, 20), (14, -8), (22, -30, 1), (28, -6), (32, 10)]), 'helm', 'f', ln=True), L(outline([(82, 20), (86, -8), (78, -30, 1), (72, -6), (68, 10)]), 'helm', 'f', ln=True),
             L(outline([(44, 4), (56, 4), (56, 58), (44, 58)]), (220, 210, 220, 255), 'f', False)],
}
# Destra: melena castaño rojiza enorme de pinchos largos que se abren en todas direcciones y le caen hasta los hombros; piel
# morena, ojos verdes y una media sonrisa
CHARS['destra'] = {
    'body': 'normal', 'pal': pal('#8a3a1e', '#b07848', iris='#7a8a3a', shade='#6a2a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 11, seed=2002, rx=64, ry=56, cy=46, lo=110)
             + [L(outline([(10, 74, 1), (14, 44), (30, 26), (50, 20), (70, 26), (86, 44), (90, 74, 1), (80, 58), (72, 64, 1), (62, 48), (50, 60, 1), (38, 48), (28, 64, 1), (20, 58)]), 'mid', 'f')],
    'side': messy('side', 20, 10, seed=2002, rx=60, ry=56, cy=46, nape=110, sweep=-0.4),
    'back': messy('back', 12, 11, seed=2002, rx=64, ry=56, cy=46, nape=114),
}
