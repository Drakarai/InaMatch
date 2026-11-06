"""The Kingdom / Os Reis (IE3, Brasil): rastas, afros, trenzas pegadas, crestas y gorros, con sus modelos 3D como referencia
(contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_empire import afro
from chars_littlegigant import dreads
from chars_orpheus import headband
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def cornrows(view, n=6, c='mid', cd='shade'):
    """Trenzas pegadas a la cabeza: casquete con surcos de delante atrás."""
    out = bald(view) + buzz(view, c)
    if view == 'front':
        out += [strand([(50 + (k - (n - 1) / 2) * 11, 8), (50 + (k - (n - 1) / 2) * 13, 40)], cd, 'f', 1.4) for k in range(n)]
    elif view == 'side':
        out += [strand([(22 + k * 4, 64 - k * 8), (40 + k * 6, 14 + k * 3), (78, 20 + k * 3)], cd, 'f', 1.4) for k in range(4)]
    else:
        out += [strand([(50 + (k - (n - 1) / 2) * 12, 6), (50 + (k - (n - 1) / 2) * 14, 80)], cd, 'f', 1.4) for k in range(n)]
    return out


# Falcão da Silva (portero): piel morena; melena de rastas castaño oscuro lisas hasta los hombros con una cinta verde fina en
# la frente y rastas que le caen por la cara; ojos violetas de enfado
CHARS['falc-o-da-silva'] = {
    'body': 'normal', 'pal': pal('#3a3028', '#a8703e', iris='#5a4a9a', shade='#2a221c', band='#2a8a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (56, 44)},
    'front': longhair('front', 98, 14, top=-4, part=True) + headband('front', 52, 'band')
             + [L(rope((30, 30), (26, 50), (24, 70), 6), 'mid', 'f', ln=True), L(rope((66, 30), (70, 52), (74, 74), 6), 'mid', 'f', ln=True)]
             + [strand([(x, 6), (x + (x - 50) * 0.3, 96)], 'deep', 'b', 1.0) for x in (14, 26, 74, 86)],
    'side': longhair('side', 98, 12, top=-4) + headband('side', 50, 'band') + [strand([(x, 2), (x - 10, 96)], 'deep', 'b', 1.0) for x in (20, 36, 52)],
    'back': longhair('back', 98, 14, top=-4, ends=4) + [strand([(x, 0), (x + (x - 50) * 0.2, 98)], 'deep', 'b', 1.0) for x in (20, 34, 50, 66, 80)],
}
# Carlos Lagarto: trenzas pegadas rosa pálido que le cubren la cabeza y caen sobre un ojo; piel grisácea, el otro ojo de
# sueño y labios gruesos
CHARS['carlos-lagarto'] = {
    'body': 'normal', 'pal': pal('#f0d4cc', '#9a7a68', shade='#c0a49c', lip='#f0c8b0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': cornrows('front', 5)
             + [L(outline([(40, 20), (58, 16), (76, 24), (88, 40), (90, 60), (86, 80), (76, 90, 1), (70, 70), (60, 50), (48, 34)]), 'mid', 'f', ln=True)]
             + [strand([(50 + k * 8, 20), (64 + k * 6, 60), (72 + k * 4, 84)], 'shade', 'f', 1.4) for k in range(3)]
             + [L(outline([(40, 96), (50, 92), (60, 96), (56, 104), (44, 104)]), 'lip', 'f', ln=True)],
    'side': cornrows('side') + [L(outline([(80, 94), (92, 94), (90, 102), (82, 102)]), 'lip', 'f', ln=True)],
    'back': cornrows('back', 6),
}
# Antonio Bagre: un afro verde oliva oscuro enorme y redondo; piel morena con pinturas rojas en las mejillas, ojos blancos de
# enfado, nariz larga y labios marrones en morro
CHARS['antonio-bagre'] = dict({
    'body': 'normal', 'pal': pal('#2e3a1e', '#a8703e', shade='#202a14', light='#4a5a2e', paint='#c82a1e', lip='#7a4a24'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': (60, 58)},
}, **afro(1101, rx=64, ry=56, cy=36, amp=4, n=14, lo=72, nape=96))
CHARS['antonio-bagre']['front'] += [L(outline([(22, 70), (42, 72), (40, 78), (26, 78)]), WHITE, 'f', ln=True), L(outline([(78, 70), (58, 72), (60, 78), (74, 78)]), WHITE, 'f', ln=True),
                                    L([(22, 66), (42, 72)], OUTC, 'f', False, False, 2.6), L([(78, 66), (58, 72)], OUTC, 'f', False, False, 2.6),
                                    L([(20, 86), (34, 88)], 'paint', 'f', False, False, 2), L([(20, 92), (34, 94)], 'paint', 'f', False, False, 2),
                                    L([(80, 86), (66, 88)], 'paint', 'f', False, False, 2), L([(80, 92), (66, 94)], 'paint', 'f', False, False, 2),
                                    L([(50, 70), (50, 94)], 'skin_d', 'f', False, False, 1.6),
                                    L(outline([(36, 100), (50, 96), (64, 100), (62, 110), (38, 110)]), 'lip', 'f', ln=True)]
CHARS['antonio-bagre']['side'] += [L([(70, 86), (84, 88)], 'paint', 'f', False, False, 2), L([(70, 92), (84, 94)], 'paint', 'f', False, False, 2)] + side_eye(74)
# Monstro Ximenes: pelo amarillo mostaza corto con un mechón rubio claro enorme que le cae en diagonal por la frente; ojos
# rojos de loco y una sonrisa de colmillos
CHARS['monstro-ximenes'] = {
    'body': 'corpulento', 'pal': pal('#c8a020', '#a8703e', iris='#a81e2a', light='#f0e0a0', shade='#a07e14'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + buzz('front')
             + [L(outline([(16, 46), (20, 20), (34, 4), (56, 0), (60, 16), (50, 30), (44, 46), (40, 64, 1), (32, 46), (24, 56, 1)]), 'light', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L(outline([(20, 30), (40, 4), (70, 0), (90, 14), (96, 30, 1), (80, 22), (56, 16), (34, 26)]), 'light', 'f', ln=True)],
    'back': bald('back') + buzz('back') + [L(outline([(54, 4), (70, 6), (76, 20), (64, 50), (52, 80, 1), (50, 50), (52, 24)]), 'light', 'f', ln=True)],
}
# Formiga Clemens: calvo de piel morena con una cresta verde ondulada en lo alto y dos mechones amarillos a un lado; cejas
# verdes, ojos de pasmo, coloretes y la boca torcida
CHARS['formiga-clemens'] = {
    'body': 'bajito', 'pal': pal('#5a8a1e', '#b87a40', yellow='#f0c020', blush='#e08060'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + [L(outline([(40, 10), (34, -6), (40, -22), (54, -24), (48, -14), (52, -4), (56, 10)]), 'mid', 'f', ln=True),
                              L(outline([(66, 14), (76, 8), (84, 12), (74, 20)]), 'yellow', 'f', ln=True), L(outline([(74, 26), (84, 22), (90, 28), (80, 32)]), 'yellow', 'f', ln=True),
                              L(outline([(24, 66), (40, 62), (42, 68), (28, 70)]), 'mid', 'f', ln=True), L(outline([(76, 66), (60, 62), (58, 68), (72, 70)]), 'mid', 'f', ln=True),
                              L(ell(50, 84, 4, 3.4), 'skin_d', 'f', ln=True), L(ell(26, 88, 4, 2.4), 'blush', 'f', False), L(ell(74, 88, 4, 2.4), 'blush', 'f', False)]
             + white_eyes(76, 14, 6, 6, 2.6),
    'side': bald('side') + [L(outline([(40, 8), (46, -10), (60, -20), (72, -14), (62, -10), (56, 4)]), 'mid', 'f', ln=True)] + side_eye(76),
    'back': bald('back') + [L(outline([(42, 8), (48, -6), (60, -20), (66, -12), (58, -2), (56, 10)]), 'mid', 'f', ln=True),
                            L(outline([(20, 14), (30, 8), (34, 16), (24, 20)]), 'yellow', 'f', ln=True)],
}
# Presa Passos: calvo de cabeza alta y lisa, con dos pinturas rojas en forma de garra sobre los ojos y las mejillas; ojos
# verdes rasgados y media sonrisa
CHARS['presa-passos'] = {
    'body': 'normal', 'pal': pal('#c8945a', '#c8945a', iris='#2a8a7a', paint='#8a1e2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(16, 64), (14, 20), (26, 0), (50, -6), (74, 0), (86, 20), (84, 64)]), 'skin'), L(outline([(62, 0), (84, 18), (84, 60), (72, 40)]), 'skin_d', 'b', False),
              L(outline([(20, 68), (30, 62), (44, 68), (34, 66), (24, 72)]), 'paint', 'f', False), L(outline([(80, 68), (70, 62), (56, 68), (66, 66), (76, 72)]), 'paint', 'f', False),
              L(outline([(16, 82), (24, 86), (20, 96)]), 'paint', 'f', False), L(outline([(84, 82), (76, 86), (80, 96)]), 'paint', 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (10, 60), (12, 20), (30, 0), (60, -4), (80, 8), (88, 30), (86, 50)]), 'skin'),
             L(outline([(70, 76), (82, 70), (84, 88), (72, 90)]), 'paint', 'f', False)],
    'back': [L(outline([(16, 84), (14, 20), (26, 0), (50, -6), (74, 0), (86, 20), (84, 84), (50, 90)]), 'skin'), L(outline([(58, 0), (84, 18), (84, 82), (62, 86)]), 'skin_d', 'b', False)],
}
# Borboleta Barboza: pelo verde menta muy abultado en mechones despeinados que caen por la frente y se abren a los lados;
# piel morena, perilla verde, ojos dorados de sueño
CHARS['borboleta-barboza'] = {
    'body': 'normal', 'pal': pal('#a8d0b8', '#9a7058', iris='#b8901e', shade='#7a9a88', light='#d8f0e0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 10, seed=1102, rx=58, ry=46, cy=38, lo=88)
             + [L(outline([(10, 80, 1), (14, 44), (28, 28), (50, 22), (72, 28), (86, 44), (90, 80, 1), (80, 60), (72, 70, 1), (66, 52), (56, 62, 1), (50, 52), (44, 66, 1), (36, 52),
                           (28, 66, 1), (20, 58)]), 'mid', 'f'),
                L(outline([(42, 104), (58, 104), (50, 112, 1)]), 'mid', 'f', ln=True)],
    'side': messy('side', 13, 8, seed=1102, rx=54, ry=46, cy=38, nape=100, sweep=-0.4),
    'back': messy('back', 12, 10, seed=1102, rx=58, ry=46, cy=38, nape=104),
}
# Coruja Cerezo: piel morena; pelo azul intenso en surcos peinados hacia atrás, con un rizo en espiral en la frente y otro
# en la nuca; ojos de enfado y labios gruesos
CHARS['coruja-cerezo'] = {
    'body': 'normal', 'pal': pal('#1e4aa8', '#a8703e', shade='#163a84', light='#4a7ad0', lip='#c88a5a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': (54, 40)},
    'front': [L(outline([(12, 68), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (88, 68), (80, 54), (60, 46), (40, 46), (20, 54)])),
              L(outline([(60, 4), (82, 16), (90, 40), (84, 62), (74, 36)]), 'shade', 'b', False)]
             + [strand([(x, 6 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 40)], 'shade', 'b', 1.2) for x in (30, 44, 58, 72)]
             + [L(ell(28, 30, 9, 9), 'mid', 'f', ln=True), L(ell(28, 30, 5, 5) + [ell(28, 30, 5, 5)[0]], 'shade', 'f', False, False, 1.4),
                L(outline([(36, 98), (50, 94), (64, 98), (60, 106), (40, 106)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 8), (52, 0), (78, 6), (94, 20), (98, 36), (86, 40), (70, 42), (58, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False), L(ell(92, 28, 7, 8), 'mid', 'f', ln=True)]
            + [strand([(20 + k * 14, 70 - k * 10), (40 + k * 12, 12), (80, 16 + k * 4)], 'shade', 'b', 1.2) for k in range(3)],
    'back': [L(outline([(12, 84), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (88, 84), (50, 90)])),
             L(outline([(56, 4), (82, 16), (90, 44), (86, 82), (64, 88)]), 'shade', 'b', False)]
            + [strand([(x, 4), (x + (x - 50) * 0.1, 86)], 'shade', 'b', 1.2) for x in (26, 40, 54, 68)],
}
# Mac Robingo: piel morena; rastas gris oscuro gruesas y cortas que salen disparadas en todas direcciones; ojos de pasmo y
# la boca abierta
CHARS['mac-robingo'] = {
    'body': 'normal', 'pal': pal('#3a4448', '#7a4e30', shade='#283236', mouth='#4a2a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': (52, 46)},
    'front': [L(blob(SKULL_F), 'skin')]
             + [L(rope((50 + d * 0.4, 20), (50 + d * 0.8, 6), (50 + d, -14 + abs(d) * 0.5), 7), 'mid', 'b', ln=True) for d in (-60, -40, -20, 0, 20, 40, 60)]
             + [L(rope((14, 40), (0, 46), (-14, 44), 7), 'mid', 'b', ln=True), L(rope((86, 40), (100, 46), (114, 44), 7), 'mid', 'b', ln=True),
                L(rope((14, 60), (2, 74), (-6, 84), 6), 'mid', 'b', ln=True), L(rope((86, 60), (98, 74), (106, 84), 6), 'mid', 'b', ln=True),
                L(outline([(14, 56), (14, 28), (28, 10), (50, 4), (72, 10), (86, 28), (86, 56), (70, 44), (50, 40), (30, 44)]))]
             + white_eyes(74, 14, 6, 6, 2) + [L(outline([(38, 98), (50, 94), (62, 98), (60, 106), (40, 106)]), 'mouth', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin')]
            + [L(rope((x, 20), (x - 14, 4 - k), (x - 30, -6 + k * 6), 7), 'mid', 'b', ln=True) for k, x in enumerate((24, 40, 56, 70))]
            + [L(rope((20, 50), (4, 56), (-12, 60), 7), 'mid', 'b', ln=True), L(rope((20, 70), (6, 82), (-4, 90), 6), 'mid', 'b', ln=True),
               L(outline([(14, 66), (12, 30), (26, 8), (54, 2), (80, 10), (90, 26), (70, 28), (48, 36), (30, 50), (22, 70)]))] + side_eye(74),
    'back': [L(blob(SKULL_B), 'skin')]
            + [L(rope((50 + d * 0.4, 30), (50 + d * 0.8, 10), (50 + d * 1.1, -10 + abs(d) * 0.4), 7), 'mid', 'b', ln=True) for d in (-60, -40, -20, 0, 20, 40, 60)]
            + [L(rope((50 + d * 0.5, 60), (50 + d, 74), (50 + d * 1.3, 88), 7), 'mid', 'b', ln=True) for d in (-50, -20, 20, 50)]
            + [L(outline([(12, 80), (12, 28), (26, 8), (50, 2), (74, 8), (88, 28), (88, 80), (50, 86)]))],
}
# Gato Carvalho: afro amarillo mostaza enorme con una cinta negra ancha en la frente y una llama roja pintada en ella; ojos
# rojizos de pillo y una sonrisa de dientes
CHARS['gato-carvalho'] = dict({
    'body': 'normal', 'pal': pal('#c8a020', '#f8c890', iris='#8a2a1e', shade='#9a7814', light='#e8c040', band='#1e1e1e', flame='#d81e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
}, **afro(1103, rx=62, ry=52, cy=30, amp=4, n=14, lo=60, nape=88))
CHARS['gato-carvalho']['front'] += [L(outline([(10, 66), (8, 50), (50, 42), (92, 50), (90, 66), (50, 60)]), 'band', 'f', ln=True),
                                    L(outline([(60, 60), (62, 50), (66, 46, 1), (68, 52), (74, 44, 1), (74, 56), (80, 50, 1), (78, 60)]), 'flame', 'f', False)]
CHARS['gato-carvalho']['side'] += [L(outline([(8, 60), (8, 46), (94, 46), (94, 60)]), 'band', 'f', ln=True)]
CHARS['gato-carvalho']['back'] += [L(outline([(8, 64), (8, 50), (50, 46), (92, 50), (92, 64), (50, 62)]), 'band', 'f', ln=True)]
# Grillo Santos: un gorrito rojo con una franja naranja sobre la cabeza rapada; un antifaz negro en forma de alas sobre unos
# ojos negros redondos, orejas grandes y una sonrisa
CHARS['grillo-santos'] = {
    'body': 'bajito', 'pal': pal('#2e2218', '#b8946a', cap='#b81e2a', cap_d='#8a141e', band='#e0801e', mask='#1e1e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 4, 'ear_out': 9},
    'front': bald('front') + [L(outline([(18, 34), (20, 14), (34, 2), (50, -2), (66, 2), (80, 14), (82, 34), (50, 28)]), 'cap', 'f', ln=True),
                              L(quad((20, 20), (50, 8), (80, 20)), 'band', 'f', False, False, 3),
                              L(outline([(16, 68), (30, 62), (42, 68), (50, 74), (58, 68), (70, 62), (84, 68), (74, 78), (58, 78), (50, 82), (42, 78), (26, 78)]), 'mask', 'f', ln=True)]
             + white_eyes(76, 13, 5.6, 5.6, 3.2) + [L(ell(50, 86, 3, 2.4), 'skin_d', 'f', ln=True)],
    'side': bald('side') + [L(outline([(16, 32), (20, 12), (40, 0), (66, 0), (84, 12), (86, 26), (50, 24)]), 'cap', 'f', ln=True), L(quad((20, 18), (50, 4), (84, 16)), 'band', 'f', False, False, 3),
                            L(outline([(74, 68), (92, 66), (92, 80), (76, 80)]), 'mask', 'f', ln=True)] + side_eye(76),
    'back': bald('back') + [L(outline([(16, 46), (16, 14), (30, 2), (50, -2), (70, 2), (84, 14), (84, 46), (50, 40)]), 'cap', 'f', ln=True),
                            L(quad((16, 26), (50, 14), (84, 26)), 'band', 'f', False, False, 3)],
}
# Leonardo Almeida: pelo castaño liso abultado que se abre hacia fuera a la altura de las orejas, con flequillo barrido a un
# lado; ojos grises de enfado y media sonrisa
CHARS['leonardo-almeida'] = {
    'body': 'normal', 'pal': pal('#7a4a2a', '#e8a868', iris='#4a5a6a', shade='#5a341a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': longhair('front', 82, 24)
             + [L(outline([(12, 64), (14, 40), (30, 22), (52, 16), (74, 22), (88, 40), (88, 60), (76, 50), (62, 46), (48, 52), (38, 62), (30, 74, 1), (26, 58), (18, 60)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 82, 20),
    'back': longhair('back', 82, 24, ends=3),
}
# Xavier Ribeiro (portero suplente): calvo con una cresta a tres franjas (azul, amarilla y verde) en lo alto; un antifaz negro
# pintado alrededor de los ojos y la boca de enfado
CHARS['xavier-ribeiro'] = {
    'body': 'corpulento', 'pal': pal('#2a1e6a', '#a87a5a', yellow='#f0c020', green='#2a8a3a', mask='#1e1e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + [L(outline([(36, 40), (36, 0), (50, -6), (64, 0), (64, 40), (50, 36)]), 'mid', 'f', ln=True),
                              L(outline([(44, -4), (56, -4), (56, 38), (44, 38)]), 'yellow', 'f', False), L(outline([(56, -3), (64, 0), (64, 40), (56, 38)]), 'green', 'f', False),
                              L([(16, 68), (28, 62), (40, 68), (50, 74), (60, 68), (72, 62), (84, 68)], 'mask', 'f', False, False, 2.4),
                              L([(22, 78), (40, 80)], 'mask', 'f', False, False, 1.8), L([(78, 78), (60, 80)], 'mask', 'f', False, False, 1.8)]
             + white_eyes(74, 14, 6, 4, 2),
    'side': bald('side') + [L(outline([(20, 30), (30, 4), (56, -6), (80, 2), (88, 18), (60, 10), (36, 20)]), 'mid', 'f', ln=True),
                            L(outline([(30, 8), (56, -2), (80, 6), (60, 6), (36, 16)]), 'yellow', 'f', False)] + side_eye(74),
    'back': bald('back') + [L(outline([(36, 40), (36, 0), (50, -6), (64, 0), (64, 40), (50, 36)]), 'green', 'f', ln=True),
                            L(outline([(44, -4), (56, -4), (56, 38), (44, 38)]), 'yellow', 'f', False), L(outline([(56, -3), (64, 0), (64, 40), (56, 38)]), 'mid', 'f', False)],
}
# Ulisses Nogueira: cara alargada y huesuda con orejas grandes; pelo gris oscuro muy corto peinado hacia atrás con entradas;
# ojos caídos de cansancio y la boca en una raya
CHARS['ulisses-nogueira'] = {
    'body': 'delgado', 'pal': pal('#4a4442', '#fcd0a8', iris='#6a5a2a', shade='#363230'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 102, 'face_front': LONG_FACE, 'nose': (50, 88, 3.4), 'hairline': False, 'big_ears': 4, 'ear_out': 9},
    'front': bald('front') + [L(outline([(16, 56), (14, 24), (26, 6), (50, 0), (74, 6), (86, 24), (84, 56), (78, 34), (60, 24), (50, 26), (40, 24), (22, 34)]), 'mid', 'f')],
    'side': bald('side') + buzz('side'),
    'back': bald('back') + buzz('back', nape=88),
}
# Gervasio Oliveira: piel morena con arrugas; pelo granate rapado muy corto; ojos cerrados de calma, perilla fina y la boca seria
CHARS['gervasio-oliveira'] = {
    'body': 'normal', 'pal': pal('#7a1e1e', '#a8703e', shade='#5a1414'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + buzz('front', front_y=40, peak=(50, 46))
             + [L([(30, 58), (40, 60)], 'skin_d', 'f', False, False, 1.2), L([(60, 60), (70, 58)], 'skin_d', 'f', False, False, 1.2),
                L([(50, 104), (50, 112)], 'mid', 'f', False, False, 1.6)],
    'side': bald('side') + buzz('side'),
    'back': bald('back') + buzz('back', nape=90),
}
# Tigre Mendes: piel morena; pelo castaño oscuro corto con una raya rapada en zigzag a los lados y un pico en la frente;
# cejas gruesas en punta, ojos de enfado y la boca seria
CHARS['tigre-mendes'] = {
    'body': 'normal', 'pal': pal('#3a2e1e', '#a8703e', shade='#281e12', zig='#c8945a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + buzz('front', front_y=40, peak=(50, 52))
             + [L([(14, 34), (22, 22), (30, 30), (38, 16)], 'zig', 'f', False, False, 2.0), L([(86, 34), (78, 22), (70, 30), (62, 16)], 'zig', 'f', False, False, 2.0),
                L(outline([(22, 64), (32, 58), (44, 66), (32, 66)]), 'mid', 'f', ln=True), L(outline([(78, 64), (68, 58), (56, 66), (68, 66)]), 'mid', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L([(16, 30), (30, 16), (44, 26), (58, 10), (72, 20), (84, 12)], 'zig', 'f', False, False, 2.0)],
    'back': bald('back') + buzz('back', nape=88) + [L([(60, 10), (70, 20), (80, 14)], 'zig', 'f', False, False, 2.0)],
}
