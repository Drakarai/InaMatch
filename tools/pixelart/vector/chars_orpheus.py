"""Orpheus / Orfeo (IE3, Italia): con sus modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de
cabeza); Hidetoshi Nakata no tiene modelo: su retrato."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_desertlion import bandana
from chars_firedragon import bowl
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def headband(view, y=40, c='band'):
    if view == 'front':
        return [L(quad((8, y + 2), (50, y - 8), (92, y + 2)), c, 'f', False, False, 2.8)]
    if view == 'side':
        return [L(quad((4, y + 2), (50, y - 8), (94, y - 2)), c, 'f', False, False, 2.8)]
    return [L(quad((4, y + 2), (50, y - 4), (96, y + 2)), c, 'f', False, False, 2.8)]


# Gigi Blasi (portero): grandullón de cara cuadrada morena; un pañuelo morado anudado en la cabeza hasta las cejas, y por
# debajo una melena negra rizada que se abre en mechones a los lados; ojos de enfado, nariz larga y la boca en una raya
CHARS['gigi-blasi'] = {
    'body': 'corpulento', 'pal': pal('#2e2a26', '#a87648', cloth='#4a3ab0', cloth_d='#36288a', shade='#1e1a18'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'eye_y': 72, 'face_front': WIDE_FACE, 'nose': (50, 84, 3.6), 'hairline': False,
             'ears': False},
    'front': [L(outline([(14, 50), (-6, 52), (-16, 66, 1), (-4, 70), (-14, 84, 1), (4, 86), (0, 100, 1), (16, 92), (20, 66)])),
              L(outline([(86, 50), (106, 52), (116, 66, 1), (104, 70), (114, 84, 1), (96, 86), (100, 100, 1), (84, 92), (80, 66)])),
              L(blob(SKULL_F), 'skin')] + bandana('front', 'cloth', 'cloth_d', low=60, tails=False),
    'side': [L(outline([(44, 60), (24, 54), (-2, 60), (-14, 74, 1), (0, 80), (-10, 96, 1), (8, 94), (6, 108, 1), (24, 98), (40, 90)])), L(blob(SIDE_SKULL), 'skin')]
            + bandana('side', 'cloth', 'cloth_d', low=56, tails=False),
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-6, 54), (106, 54), (116, 70, 1), (104, 78), (110, 94, 1), (94, 94), (86, 106, 1), (70, 96), (58, 108, 1), (50, 96), (42, 108, 1), (30, 96), (14, 106, 1),
                        (6, 94), (-10, 94, 1), (-4, 78), (-16, 70, 1)])),
             L(outline([(56, 56), (104, 56), (106, 80), (90, 96), (66, 94)]), 'shade', 'b', False)] + bandana('back', 'cloth', 'cloth_d', low=60, tails=False),
}
# Vento Galliano: pelo azul celeste en un tupé enorme de pinchos echados hacia arriba y a un lado, con un mechón que le
# cae tapándole media cara; un ojo de enfado y la boca seria
CHARS['vento-galliano'] = {
    'body': 'delgado', 'pal': pal('#8ac8e8', '#e8a868', shade='#6a8aaa', light='#c0e4f4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(16, 60), (8, 30), (2, 10), (26, 2), (54, -6), (70, -30, 1), (74, -4), (90, -20, 1), (90, 6), (98, 22), (88, 60), (80, 50), (20, 50)])),
              L(outline([(60, -2), (68, -24, 1), (74, 8), (92, 4, 1), (88, 24), (86, 56), (76, 30)]), 'shade', 'b', False),
              L(outline([(2, 34, 1), (16, 22), (40, 12), (66, 16), (84, 30), (88, 48), (74, 40), (60, 40), (50, 54), (44, 76), (34, 98, 1), (30, 72), (24, 50), (12, 40)]), 'mid', 'f', ln=True),
              L(outline([(20, 26), (44, 16), (36, 26)]), 'light', 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (4, 10, 1), (26, 14), (34, -14, 1), (50, 6), (66, -22, 1), (74, 4), (92, -8, 1), (90, 18), (94, 34), (78, 42),
                        (62, 46), (52, 62), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 86), (12, 30), (2, 6, 1), (26, 10), (36, -22, 1), (50, 2), (68, -28, 1), (74, 6), (98, -2, 1), (90, 24), (88, 86), (50, 94)])),
             L(outline([(14, 40), (50, 30), (88, 40), (86, 84), (50, 92), (16, 84)]), 'shade', 'b', False)],
}
# Otto Nobili: gordo de cara enorme y pálida con papada; pelo castaño rojizo con raya en medio, liso y pegado, que se abre
# en puntas a la altura de la nuca; ojos pequeños de sueño, nariz grande y la boca en una raya
OTTO_FACE = blob([(10, 40), (50, 34), (90, 40), (100, 78), (96, 112), (76, 128), (24, 128), (4, 112), (0, 78)])
CHARS['otto-nobili'] = {
    'body': 'corpulento', 'pal': pal('#7a3424', '#fce0b0', shade='#5a2418', nose='#e8a080'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': OTTO_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 10},
    'front': [L(outline([(-12, 98, 1), (0, 86), (2, 40), (16, 10), (50, 2), (84, 10), (98, 40), (100, 86), (112, 98, 1), (92, 92), (88, 50), (50, 40), (12, 50), (8, 92)])),
              L(outline([(60, 6), (86, 18), (98, 50), (100, 90), (90, 88), (86, 50)]), 'shade', 'b', False), strand([(50, 4), (50, 40)], 'deep', 'b', 1.2),
              L(outline([(24, 70), (40, 70), (38, 76), (26, 76)]), WHITE, 'f', ln=True), L(outline([(76, 70), (60, 70), (62, 76), (74, 76)]), WHITE, 'f', ln=True),
              L([(24, 70), (40, 70)], OUTC, 'f', False, False, 2.0), L([(76, 70), (60, 70)], OUTC, 'f', False, False, 2.0),
              L(ell(32, 73, 1.4, 1.6), OUTC, 'f', False), L(ell(68, 73, 1.4, 1.6), OUTC, 'f', False),
              L(outline([(42, 72), (58, 72), (60, 86), (40, 86)]), 'nose', 'f', ln=True),
              L(quad((32, 100), (50, 94), (68, 100)), OUTC, 'f', False, False, 1.6), L(quad((34, 118), (50, 122), (66, 118)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(28, 120), (6, 90), (6, 30), (24, 8), (54, -2), (80, 8), (96, 30), (100, 70), (98, 110), (80, 128), (50, 130)]), 'skin'),
             L(outline([(4, 80), (-14, 92, 1), (-2, 70), (2, 30), (22, 6), (54, -2), (80, 8), (92, 24), (70, 22), (46, 40), (40, 70), (24, 90), (10, 96)])),
             L(outline([(94, 72), (106, 80), (96, 88)]), 'nose', 'f', ln=True)] + side_eye(72, lid=1.5),
    'back': [L(outline([(-12, 100, 1), (0, 86), (2, 40), (16, 10), (50, 2), (84, 10), (98, 40), (100, 86), (112, 100, 1), (80, 96), (70, 106), (30, 106), (20, 96)])),
             L(outline([(30, 92), (70, 92), (70, 106), (30, 106)]), 'shade', 'b', False),
             L(outline([(56, 6), (86, 18), (98, 50), (100, 90), (74, 96)]), 'shade', 'b', False)],
}
# Anton Graziuso: la cabeza rapada en castaño muy corto y un tupé rubio enroscado hacia un lado en lo alto de la frente;
# perilla fina, pestañas marcadas y la boca seria
CHARS['anton-graziuso'] = {
    'body': 'normal', 'pal': pal('#6a5440', '#fcdcc0', iris='#2a7ab8', curl='#e0b850', curl_d='#b8902a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 7},
    'front': bald('front') + [L(outline([(12, 56), (12, 22), (22, 6), (50, 0), (78, 6), (88, 22), (88, 56), (80, 40), (20, 40)]), 'mid', 'f'),
                              L(outline([(36, 26), (34, 4), (50, -6), (70, 0), (74, 14), (62, 20), (56, 12), (50, 22)]), 'curl', 'f', ln=True),
                              L(outline([(56, 2), (70, 4), (68, 14), (60, 10)]), 'curl_d', 'f', False),
                              L(outline([(44, 108), (56, 108), (50, 116, 1)]), 'mid', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L(outline([(68, 8), (76, -8), (90, -6), (92, 6), (82, 10)]), 'curl', 'f', ln=True)] + side_eye(76),
    'back': bald('back') + buzz('back', nape=90),
}
# Marco Maserati: pelo burdeos ondulado y corto, abultado, con un mechón que le cae en la frente; ojos verdes y una sonrisa
# pícara de dientes
CHARS['marco-maserati'] = {
    'body': 'normal', 'pal': pal('#8a2a30', '#fce0c0', iris='#7a8a2a', shade='#6a1e24', light='#b04a50'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 3, 16, seed=801, rx=52, ry=44, cy=40, lo=70)
             + [L(outline([(12, 64), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 64), (78, 52), (62, 46), (44, 48), (36, 60, 1), (30, 48), (20, 56)]), 'mid', 'f'),
                L(outline([(30, 30), (48, 24), (40, 34)]), 'light', 'f', False)],
    'side': messy('side', 3.5, 14, seed=801, rx=50, ry=44, cy=40, nape=92),
    'back': messy('back', 3, 16, seed=801, rx=52, ry=44, cy=40, nape=94),
}
# Giuseppe Cannavaro: pelo verde azulado en ondas gruesas como olas, peinado a un lado tapándole un ojo; unas gafas
# redondas de montura marrón sobre el otro, pecas y una sonrisa
CHARS['giuseppe-cannavaro'] = {
    'body': 'delgado', 'pal': pal('#3aa0a8', '#fce4cc', shade='#2a7078', rim='#6a4a2a', freckle='#d09a70'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 34), (20, 10), (50, 0), (80, 8), (94, 26), (92, 50), (86, 66), (80, 50), (20, 50)])),
              L(outline([(60, 4), (86, 16), (94, 36), (88, 60), (78, 38)]), 'shade', 'b', False),
              L(outline([(-2, 74), (2, 46), (16, 24), (40, 14), (66, 16), (82, 30), (72, 34), (60, 34), (54, 48), (46, 62), (36, 80), (24, 90, 1), (14, 82)]), 'mid', 'f', ln=True)]
             + [strand([(x, y), (x + 14, y - 4)], 'shade', 'f', 1.6) for x, y in ((10, 50), (16, 36), (28, 26), (8, 66), (22, 56))]
             + [L(ell(68, 76, 8, 8) + [ell(68, 76, 8, 8)[0]], 'rim', 'f', False, False, 2.0), L(ell(68, 76, 1.8, 2), OUTC, 'f', False),
                L([(76, 74), (88, 70)], 'rim', 'f', False, False, 1.6)]
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((60, 88), (64, 90), (72, 88))],
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (-2, 66), (6, 50), (8, 30), (22, 8), (50, 0), (76, 8), (92, 24), (94, 40), (80, 44), (66, 46), (56, 58), (52, 72), (50, 84)])),
             L(outline([(4, 50), (34, 44), (42, 80), (22, 88), (8, 66)]), 'shade', 'b', False),
             L(ell(86, 76, 4, 7) + [ell(86, 76, 4, 7)[0]], 'rim', 'f', False, False, 2.0), L([(50, 72), (82, 74)], 'rim', 'f', False, False, 1.6)],
    'back': [L(outline([(12, 84), (-4, 76), (4, 40), (20, 10), (50, 0), (80, 10), (96, 36), (90, 84), (50, 90)])),
             L(outline([(4, 50), (50, 44), (94, 50), (90, 82), (50, 88), (12, 84)]), 'shade', 'b', False)],
}
# Angelo Gabrini: un aro de ángel blanco flotando sobre una melena rubia anaranjada de rizos que se abre a los lados en
# mechones gruesos; ojos azules grandes, coloretes y una sonrisa
CHARS['angelo-gabrini'] = {
    'body': 'bajito', 'pal': pal('#f0b030', '#fce4cc', iris='#2a9aa8', shade='#c88820', blush='#f0a080', halo=WHITE),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(ell(50, -8, 24, 5) + [ell(50, -8, 24, 5)[0]], 'halo', 'b', False, False, 2.6),
              L(outline([(-12, 96, 1), (-2, 84), (-10, 74, 1), (2, 66), (4, 36), (18, 10), (50, 2), (82, 10), (96, 36), (98, 66), (110, 74, 1), (102, 84), (112, 96, 1), (88, 92),
                         (82, 64), (18, 64), (12, 92)])),
              L(outline([(60, 6), (86, 18), (98, 46), (100, 88), (88, 88), (82, 50)]), 'shade', 'b', False),
              L(outline([(12, 66, 1), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (88, 66, 1), (78, 52), (66, 58, 1), (60, 46), (50, 56, 1), (40, 46), (34, 58, 1), (22, 52)]), 'mid', 'f'),
              L(ell(26, 86, 5, 3), 'blush', 'f', False), L(ell(74, 86, 5, 3), 'blush', 'f', False)],
    'side': [L(outline([(36, -6), (52, -12), (72, -10), (74, -6), (54, -6)]), 'halo', 'b', ln=True),
             L(outline([(44, 92), (40, 102, 1), (26, 96), (10, 104, 1), (6, 86), (-6, 78, 1), (4, 66), (4, 36), (18, 10), (50, 2), (78, 8), (92, 26), (92, 46), (80, 46), (66, 48),
                        (56, 60), (52, 74), (50, 84)])),
             L(outline([(6, 46), (34, 46), (44, 84), (24, 96), (8, 80)]), 'shade', 'b', False), L(ell(74, 86, 5, 3), 'blush', 'f', False)],
    'back': [L(outline([(-12, 96, 1), (-2, 84), (-10, 74, 1), (2, 66), (4, 36), (18, 10), (50, 2), (82, 10), (96, 36), (98, 66), (110, 74, 1), (102, 84), (112, 96, 1), (84, 96),
                        (70, 106, 1), (60, 94), (50, 104, 1), (40, 94), (30, 106, 1), (16, 96)])),
             L(outline([(56, 6), (86, 18), (98, 50), (100, 92), (70, 100), (64, 50)]), 'shade', 'b', False),
             L(ell(50, -8, 24, 5) + [ell(50, -8, 24, 5)[0]], 'halo', 'f', False, False, 2.6)],
}
# Hidetoshi Nakata (sin modelo 3D; su retrato): piel morena; la cabeza rapada con una cresta castaña de pinchos en lo alto y
# barba de pocos días; ojos de enfado y orejas grandes
CHARS['hidetoshi-nakata'] = {
    'body': 'normal', 'pal': pal('#5a3a1e', '#c8915a', skin_d='#a8743e', stubble='#a08060'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': bald('front') + [L(outline([(16, 52), (16, 30), (28, 12), (36, -6, 1), (44, 4), (50, -14, 1), (56, 4), (64, -6, 1), (72, 12), (84, 30), (84, 52), (72, 36), (50, 30),
                                         (28, 36)]), 'mid', 'f'),
                              L(outline([(56, 4), (64, -4, 1), (72, 14), (84, 34), (74, 34)]), 'shade', 'f', False),
                              L(outline([(26, 92), (36, 104), (50, 108), (64, 104), (74, 92), (64, 100), (50, 102), (36, 100)]), 'stubble', 'f', False)],
    'side': bald('side') + [L(outline([(16, 40), (22, 16), (36, 0), (42, -14, 1), (52, 0), (62, -10, 1), (68, 6), (82, 14), (88, 30), (64, 30), (40, 40), (24, 56)]), 'mid', 'f')],
    'back': bald('back') + [L(outline([(16, 60), (16, 28), (30, 8), (40, -6, 1), (50, 2), (60, -6, 1), (70, 8), (84, 28), (84, 60), (50, 54)]), 'mid', 'f')],
}
# Giorgio Giannini: pelo morado azulado liso y abultado, con raya a un lado, mechones que caen por la frente y las puntas
# abiertas por encima de las orejas; ojos castaños de enfado y la boca seria
CHARS['giorgio-giannini'] = {
    'body': 'normal', 'pal': pal('#5a5a9a', '#f0b880', iris='#8a5a2a', shade='#40407a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 60), (-10, 64, 1), (6, 52), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 52), (110, 64, 1), (92, 60), (88, 70), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (94, 40), (90, 62), (78, 36)]), 'shade', 'b', False),
              L(outline([(12, 66), (14, 40), (26, 22), (40, 14), (60, 16), (78, 26), (88, 42), (88, 62), (78, 48), (62, 38), (46, 40), (38, 54), (32, 70, 1), (26, 54), (18, 58)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 70), (-8, 70, 1), (6, 58), (-6, 48, 1), (8, 40), (8, 30), (22, 8), (50, 0), (78, 8), (94, 26), (94, 46), (80, 44), (66, 46),
                        (54, 60), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 84), (22, 88), (12, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 80), (-10, 76, 1), (6, 64), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 64), (110, 76, 1), (88, 80), (70, 86), (60, 96, 1), (50, 86), (40, 96, 1),
                        (30, 86)])),
             L(outline([(56, 4), (86, 16), (94, 44), (90, 78), (64, 86)]), 'shade', 'b', False)],
}
# Paolo Bianchi: pelo castaño oscuro liso con un flequillo despeinado de mechones en punta que le cae hasta los ojos y la
# nuca abierta en puntas; ojos azules grandes y una sonrisa
CHARS['paolo-bianchi'] = {
    'body': 'normal', 'pal': pal('#3a2e1a', '#fcdcc0', iris='#2a4a8a', shade='#2a2010'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 84, 1), (10, 64), (4, 34), (18, 10), (50, 0), (82, 10), (96, 34), (90, 64), (92, 84, 1), (82, 74), (82, 62), (18, 62), (18, 74)])),
              L(outline([(60, 4), (86, 16), (96, 44), (90, 78), (80, 44)]), 'shade', 'b', False),
              L(outline([(10, 70, 1), (14, 42), (28, 24), (50, 18), (72, 24), (86, 42), (90, 70, 1), (80, 54), (72, 64, 1), (66, 50), (56, 62, 1), (50, 50), (42, 68, 1), (36, 52),
                         (26, 64, 1), (20, 54)]), 'mid', 'f')],
    'side': [L(outline([(44, 92), (34, 100, 1), (24, 88), (8, 96, 1), (8, 70), (4, 36), (18, 10), (50, 0), (78, 8), (94, 26), (96, 46), (100, 56, 1), (86, 52), (68, 50), (56, 60),
                        (52, 74), (50, 84)])),
             L(outline([(8, 40), (34, 40), (44, 84), (24, 92), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 84, 1), (10, 64), (4, 34), (18, 10), (50, 0), (82, 10), (96, 34), (90, 64), (92, 84, 1), (76, 86), (66, 98, 1), (56, 86), (46, 98, 1), (36, 86), (22, 92, 1)])),
             L(outline([(56, 4), (86, 16), (96, 44), (90, 80), (64, 88)]), 'shade', 'b', False)],
}
# Raffaele Generani: melena castaña rizada hasta la barbilla con una cinta negra en la frente; ojos rojos rasgados de
# villano y una sonrisa de dientes
CHARS['raffaele-generani'] = {
    'body': 'normal', 'pal': pal('#7a4a26', '#fcecc8', iris='#a81e3a', shade='#5a3418', band='#2a3036'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': [(14, 66), (16, 46), (30, 44), (50, 44), (70, 44), (84, 46), (86, 66)]},
    'front': [L(outline([(-4, 106, 1), (2, 90), (-6, 80, 1), (4, 66), (4, 32), (18, 8), (50, 0), (82, 8), (96, 32), (96, 66), (106, 80, 1), (98, 90), (104, 106, 1), (86, 98), (84, 64),
                         (16, 64), (14, 98)])),
              L(outline([(60, 4), (86, 16), (96, 44), (98, 96), (86, 96), (80, 50)]), 'shade', 'b', False),
              L(outline([(30, 44), (36, 56), (32, 64), (40, 74, 1)]), 'mid', 'f', False, False, 1.6)] + headband('front', 42),
    'side': [L(outline([(54, 70), (52, 96), (40, 104), (26, 112, 1), (16, 98), (2, 104, 1), (2, 70), (2, 34), (18, 8), (50, 0), (78, 8), (92, 26), (92, 44), (78, 44), (64, 50)])),
             L(outline([(4, 40), (34, 40), (46, 84), (36, 104), (14, 100), (4, 80)]), 'shade', 'b', False)] + headband('side', 40),
    'back': [L(outline([(-4, 106, 1), (2, 90), (-6, 80, 1), (4, 66), (4, 32), (18, 8), (50, 0), (82, 8), (96, 32), (96, 66), (106, 80, 1), (98, 90), (104, 106, 1), (80, 102),
                        (66, 112, 1), (56, 102), (44, 112, 1), (34, 102), (20, 106)])),
             L(outline([(56, 4), (86, 16), (96, 48), (98, 100), (70, 106), (64, 50)]), 'shade', 'b', False)] + headband('back', 42),
}
# Dante Diavolo: cara roja y alargada; pelo azul marino peinado hacia atrás con dos cuernos de pelo a los lados y un nudo
# en lo alto; una cicatriz en zigzag bajo el ojo, ojos amarillos de diablo con ojeras negras y colmillos
CHARS['dante-diavolo'] = {
    'body': 'normal', 'pal': pal('#1e2a4a', '#e07a6a', skin_d='#c06050', iris='#e8b020', shade='#141e36'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': [L(outline([(16, 56), (4, 46), (-6, 28, 1), (10, 30), (20, 10), (50, 2), (80, 10), (90, 30), (106, 28, 1), (96, 46), (84, 56), (70, 40), (58, 34), (52, 50, 1), (44, 34),
                         (30, 40)])),
              L(outline([(60, 4), (82, 14), (92, 32), (86, 50), (74, 34)]), 'shade', 'b', False),
              L(ell(50, 8, 10, 7), 'mid', 'f', ln=True),
              L(outline([(22, 66), (42, 66), (40, 80), (24, 80)]), OUTC, 'f', False), L(outline([(78, 66), (58, 66), (60, 80), (76, 80)]), OUTC, 'f', False),
              L(ell(32, 73, 4.6, 4.2), 'iris', 'f', False), L(ell(68, 73, 4.6, 4.2), 'iris', 'f', False),
              L(ell(32, 73, 1.6, 2), OUTC, 'f', False), L(ell(68, 73, 1.6, 2), OUTC, 'f', False),
              L([(58, 84), (66, 88), (58, 94), (66, 100), (60, 104)], OUTC, 'f', False, False, 1.6),
              L([(46, 64), (46, 96)], 'skin_d', 'f', False, False, 1.4),
              L(outline([(34, 104), (66, 104), (62, 112), (38, 112)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (24, 8), (54, 0), (80, 8), (92, 24), (90, 38), (76, 40), (62, 44), (52, 62), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 84), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(64, 6), (78, -10), (92, -4), (84, 8)]), 'mid', 'f', ln=True),
             L(outline([(76, 66), (92, 66), (92, 80), (78, 80)]), OUTC, 'f', False), L(ell(86, 73, 3.4, 4), 'iris', 'f', False)],
    'back': [L(outline([(16, 84), (14, 30), (0, 28, 1), (8, 16), (20, 10), (50, 2), (80, 10), (92, 16), (100, 28, 1), (86, 30), (84, 84), (50, 90)])),
             L(outline([(56, 4), (82, 14), (86, 46), (84, 82), (62, 88)]), 'shade', 'b', False)],
}
# Daniele Sanctis (portero suplente): gordo de cara redonda con una nariz enorme de bola; pelo castaño oscuro corto que se
# abomba en dos bollos rizados a los lados; ojos pequeños de pestañas y una sonrisa ancha
CHARS['daniele-sanctis'] = {
    'body': 'corpulento', 'pal': pal('#3a2a1e', '#f0a070', nose='#c8784a', shade='#261a12'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(12, 52), (14, 26), (28, 8), (50, 2), (72, 8), (86, 26), (88, 52), (70, 34), (50, 30), (30, 34)]), 'mid', 'f'),
              L(outline([(16, 40), (-2, 40), (-10, 56), (-2, 70), (12, 72), (18, 60)]), 'mid', 'f', ln=True),
              L(outline([(84, 40), (102, 40), (110, 56), (102, 70), (88, 72), (82, 60)]), 'mid', 'f', ln=True),
              L(ell(30, 70, 4, 4), WHITE, 'f', ln=True), L(ell(70, 70, 4, 4), WHITE, 'f', ln=True), L(ell(30, 70, 2, 2.2), (40, 60, 140, 255), 'f', False),
              L(ell(70, 70, 2, 2.2), (40, 60, 140, 255), 'f', False),
              L(ell(50, 84, 14, 11), 'nose', 'f', ln=True), L(quad((24, 98), (50, 110), (76, 98)), OUTC, 'f', False, False, 1.6)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(14, 66), (12, 30), (26, 8), (54, 2), (80, 10), (88, 24), (70, 28), (50, 32), (36, 50), (24, 70)]), 'mid', 'f'),
             L(outline([(12, 44), (32, 40), (42, 60), (30, 76), (14, 72)]), 'mid', 'f', ln=True),
             L(ell(96, 84, 10, 10), 'nose', 'f', ln=True)] + side_eye(70),
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-12, 60), (-6, 36), (14, 22), (30, 8), (50, 2), (70, 8), (86, 22), (106, 36), (112, 60), (100, 76), (84, 74), (50, 80), (16, 74), (0, 76)])),
             L(outline([(56, 6), (86, 22), (106, 40), (110, 62), (90, 74), (64, 76)]), 'shade', 'b', False)],
}
# Enrico Oliviero: cara alargada y pálida; melena negra lisa hasta los hombros con raya en medio y una cinta azul en la
# frente, que se recoge atrás en una coleta; ojos de villano con ojeras y la boca seria
CHARS['enrico-oliviero'] = {
    'body': 'delgado', 'pal': pal('#2e2824', '#fce8d0', iris='#8a6a1e', shade='#1e1a18', band='#3a6a9a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE,
             'hairline': [(16, 66), (18, 46), (32, 40), (50, 42), (68, 40), (82, 46), (84, 66)]},
    'front': [L(outline([(2, 110, 1), (6, 86), (4, 34), (18, 8), (50, 0), (82, 8), (96, 34), (94, 86), (98, 110, 1), (84, 98), (82, 62), (18, 62), (16, 98)])),
              L(outline([(60, 4), (86, 16), (96, 44), (96, 102), (84, 96), (80, 50)]), 'shade', 'b', False), strand([(50, 2), (50, 40)], 'deep', 'b', 1.0)]
             + headband('front', 38) + [L([(22, 82), (40, 82)], (180, 160, 150, 255), 'f', False, False, 1.0), L([(60, 82), (78, 82)], (180, 160, 150, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(54, 70), (52, 104), (36, 112), (14, 118, 1), (6, 96), (2, 34), (18, 8), (50, 0), (78, 8), (92, 26), (92, 44), (78, 44), (62, 50)])),
             L(outline([(4, 40), (34, 40), (46, 90), (34, 110), (10, 106)]), 'shade', 'b', False),
             L(outline([(14, 60), (6, 90), (12, 110, 1), (20, 84)]), 'deep', 'b', ln=True)] + headband('side', 36),
    'back': [L(outline([(2, 110, 1), (6, 86), (4, 34), (18, 8), (50, 0), (82, 8), (96, 34), (94, 86), (98, 110, 1), (70, 108), (50, 114), (30, 108)])),
             L(outline([(56, 4), (86, 16), (96, 44), (96, 104), (66, 108)]), 'shade', 'b', False)] + headband('back', 38),
}
# Alessandro Rossa: pelo rubio cobrizo de rizos muy abultados y redondos que le caen por la frente; cejas gruesas, ojos
# verdes y la boca seria
CHARS['alessandro-rossa'] = {
    'body': 'normal', 'pal': pal('#e8963a', '#f0d0b0', iris='#2a8a7a', shade='#c0742a', light='#f8b860'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 4, 16, seed=802, rx=56, ry=46, cy=40, lo=70)
             + [L(outline([(10, 62), (14, 42), (30, 30), (50, 26), (70, 30), (86, 42), (90, 62), (80, 54), (72, 60), (62, 50), (52, 58), (42, 50), (32, 58), (22, 52)]), 'mid', 'f'),
                L(outline([(28, 34), (44, 30), (40, 38)]), 'light', 'f', False), L(outline([(56, 32), (72, 34), (66, 40)]), 'light', 'f', False)],
    'side': messy('side', 4, 14, seed=802, rx=54, ry=46, cy=40, nape=92) + [spk((60, 30), (88, 40), (90, 60), 4, z='f', light_left=False)],
    'back': messy('back', 4, 16, seed=802, rx=56, ry=46, cy=40, nape=94),
}
# Gianluca Zanardi: pelo castaño oscuro liso con raya a un lado, peinado hacia atrás hasta la nuca y abierto en dos puntas
# hacia fuera a la altura de la barbilla; ojos azules grandes de enfado y la boca seria
CHARS['gianluca-zanardi'] = {
    'body': 'normal', 'pal': pal('#3a2a1e', '#fcdcc0', iris='#3a8ab8', shade='#261a12'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(14, 66), (16, 46), (26, 38), (46, 36), (70, 40), (84, 46), (86, 66)]},
    'front': [L(outline([(-6, 96, 1), (8, 86), (6, 36), (20, 10), (50, 0), (80, 10), (94, 36), (92, 86), (106, 96, 1), (84, 92), (82, 62), (18, 62), (16, 92)])),
              L(outline([(60, 4), (86, 16), (94, 44), (92, 90), (84, 88), (80, 50)]), 'shade', 'b', False), strand([(38, 2), (32, 36)], 'deep', 'b', 1.0)],
    'side': [L(outline([(54, 70), (52, 96), (36, 102), (10, 108, 1), (8, 86), (4, 36), (18, 10), (50, 0), (78, 8), (92, 26), (92, 44), (78, 44), (62, 50)])),
             L(outline([(6, 40), (34, 40), (46, 86), (30, 102), (10, 100)]), 'shade', 'b', False)],
    'back': [L(outline([(-6, 96, 1), (8, 86), (6, 36), (20, 10), (50, 0), (80, 10), (94, 36), (92, 86), (106, 96, 1), (74, 96), (50, 102), (26, 96)])),
             L(outline([(56, 4), (86, 16), (94, 44), (94, 92), (64, 98)]), 'shade', 'b', False)],
}
