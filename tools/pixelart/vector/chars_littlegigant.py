"""Little Gigant / Los Pequeños Gigantes (IE3, Cotarl): rastas, pañuelos, afros y pinchos, con sus modelos 3D como
referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_desertlion import bandana
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def dreads(view, n=7, length=40, w=8, c='mid', top=8, spread=1.0, back_len=None):
    """Rastas gruesas que salen de la coronilla y caen alrededor de la cabeza."""
    out = []
    if view == 'front':
        for k in range(n):
            t = k / (n - 1)
            x0 = 14 + 72 * t
            side = (t - 0.5) * 2
            out.append(L(rope((x0, top + abs(side) * 20), (x0 + side * 22 * spread, top + 30 + abs(side) * 14), (x0 + side * 30 * spread, top + 30 + length * (0.4 + 0.6 * abs(side))), w), c, 'b', ln=True))
    elif view == 'side':
        for k in range(n - 1):
            t = k / (n - 2)
            x0 = 20 + 56 * t
            out.append(L(rope((x0, top + 4), (x0 - 16, top + 30), (x0 - 24 + t * 6, top + 30 + length), w), c, 'b', ln=True))
    else:
        bl = back_len or length
        for k in range(n):
            t = k / (n - 1)
            x0 = 12 + 76 * t
            side = (t - 0.5) * 2
            out.append(L(rope((x0, top + 4), (x0 + side * 14 * spread, top + 34), (x0 + side * 20 * spread, top + 34 + bl), w), c, 'b', ln=True))
    return out


# Hector Helio (portero): pelo azul petróleo liso en casco con dos picos arriba y mechones que le bajan por las mejillas;
# ojos negros grandes y una sonrisa
CHARS['hector-helio'] = {
    'body': 'normal', 'pal': pal('#1e5a74', '#a8703e', shade='#164458'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 92), (8, 40), (14, 14), (12, -8, 1), (30, 6), (50, 2), (70, 6), (88, -8, 1), (86, 14), (92, 40), (88, 92), (80, 86), (80, 62), (20, 62), (20, 86)])),
              L(outline([(60, 6), (82, -2, 1), (84, 16), (92, 44), (86, 86), (80, 50)]), 'shade', 'b', False),
              L(outline([(12, 64, 1), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (88, 64, 1), (78, 50), (64, 46), (50, 60, 1), (36, 46), (22, 50)]), 'mid', 'f')],
    'side': [L(outline([(52, 96), (44, 98), (40, 76), (22, 88), (12, 64), (10, 36), (-16, 22, 1), (12, 14), (30, 2), (60, 0), (80, 8), (94, 26), (90, 44), (74, 44), (60, 52), (54, 70)])),
             L(outline([(12, 40), (34, 40), (40, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 86), (8, 40), (14, 14), (12, -8, 1), (30, 6), (50, 2), (70, 6), (88, -8, 1), (86, 14), (92, 40), (88, 86), (50, 92)])),
             L(outline([(56, 6), (84, 14), (92, 44), (88, 84), (64, 90)]), 'shade', 'b', False)],
}
# Zephyr Vitesse: un pañuelo verde azulado anudado en la cabeza y una melena gris lila lisa que le cae a los lados y tapa
# un ojo; piel naranja y una sonrisa pícara
CHARS['zephyr-vitesse'] = {
    'body': 'normal', 'pal': pal('#c0b8d8', '#d8803a', iris='#5a5aa8', shade='#9a92b8', cloth='#2e6a6a', cloth_d='#1e4e50'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(4, 106, 1), (8, 70), (6, 40), (94, 40), (92, 70), (100, 106, 1), (86, 94), (82, 64), (18, 64), (16, 94)])),
              L(outline([(60, 44), (92, 44), (96, 100), (84, 92), (80, 60)]), 'shade', 'b', False)]
             + bandana('front', 'cloth', 'cloth_d', low=50, tails=False)
             + [L(outline([(14, 52), (30, 50), (40, 58), (36, 76), (28, 94, 1), (22, 70)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(48, 60), (40, 96), (18, 112, 1), (8, 88), (8, 50)]))] + [L(blob(SIDE_SKULL), 'skin')] + bandana('side', 'cloth', 'cloth_d', low=48),
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(4, 106), (6, 48), (94, 48), (96, 106), (50, 112)])),
             L(outline([(56, 50), (94, 50), (96, 104), (64, 108)]), 'shade', 'b', False)] + bandana('back', 'cloth', 'cloth_d', low=50),
}
# Walter Mountain: gordo de cara redonda; la cabeza cubierta de cuernos de pelo granate como un erizo, con dos franjas
# doradas; cejas gruesas, ojos de pasmo, nariz gorda y la boca abierta con labios gruesos
CHARS['walter-mountain'] = {
    'body': 'corpulento', 'pal': pal('#7a2a1a', '#b8784a', shade='#5a1e12', gold='#d8a050', lip='#e8a0a0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 8},
    'front': [L(outline([(x - 4, 26 if abs(x - 50) > 20 else 16), (x + (x - 50) * 0.7, -10 + abs(x - 50) * 0.5 if abs(x - 50) < 40 else 30, 1), (x + 4, 26 if abs(x - 50) > 20 else 16)]),
                'mid', 'b', ln=True) for x in (8, 22, 36, 50, 64, 78, 92)]
             + [L(outline([(12, 50), (14, 26), (28, 10), (50, 4), (72, 10), (86, 26), (88, 50), (70, 40), (50, 38), (30, 40)]), 'mid', 'f', ln=True),
                L(quad((28, 12), (34, 30), (32, 46)), 'gold', 'f', False, False, 1.4), L(quad((72, 12), (66, 30), (68, 46)), 'gold', 'f', False, False, 1.4),
                L(outline([(22, 62), (36, 56), (44, 62), (32, 64)]), 'mid', 'f', ln=True), L(outline([(78, 62), (64, 56), (56, 62), (68, 64)]), 'mid', 'f', ln=True)]
             + white_eyes(72, 15, 5.4, 5.4, 2)
             + [L(ell(50, 84, 9, 5), 'skin_d', 'f', ln=True),
                L(outline([(30, 96), (50, 92), (70, 96), (66, 106), (50, 110), (34, 106)]), 'lip', 'f', ln=True), L([(34, 100), (66, 100)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(x, 20), (x - 14, -14 + k * 2, 1), (x + 8, 16)]), 'mid', 'b', ln=True) for k, x in enumerate((20, 34, 48, 62))]
            + [L(blob(SIDE_SKULL), 'skin'), L(outline([(12, 44), (14, 22), (30, 8), (56, 2), (80, 10), (88, 24), (60, 26), (34, 40)]), 'mid', 'f', ln=True)] + side_eye(72),
    'back': [L(outline([(x - 4, 26), (x + (x - 50) * 0.8, -6 + abs(x - 50) * 0.4, 1), (x + 4, 26)]), 'mid', 'b', ln=True) for x in (10, 24, 38, 50, 62, 76, 90)]
            + [L(outline([(10, 86), (8, 30), (22, 8), (50, 2), (78, 8), (92, 30), (90, 86), (50, 92)]), 'mid', 'f', ln=True),
               L(quad((36, 8), (34, 50), (40, 88)), 'gold', 'f', False, False, 1.4), L(quad((64, 8), (66, 50), (60, 88)), 'gold', 'f', False, False, 1.4)],
}
# Jimi Gaines: piel morena; melena azul petróleo lisa muy larga, peinada hacia atrás, con un mechón que le cruza la cara
# de arriba abajo y una trenza con cuentas de colores a un lado; gafas de sol redondas negras
CHARS['jimi-gaines'] = {
    'body': 'normal', 'pal': pal('#1e4a6a', '#a8703e', shade='#163650', lens='#141414', bead1='#e8c020', bead2='#3a9a5a', bead3='#c82a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': [(16, 70), (18, 44), (34, 34), (50, 32), (66, 34), (82, 44), (84, 70)]},
    'front': [L(outline([(4, 118), (6, 70), (4, 30), (18, 6), (50, -2), (82, 6), (96, 30), (94, 70), (96, 118), (86, 112), (82, 62), (18, 62), (14, 112)])),
              L(outline([(60, 2), (86, 14), (96, 40), (94, 112), (84, 108), (80, 50)]), 'shade', 'b', False),
              L(ell(34, 76, 9, 7), 'lens', 'f', ln=True), L(ell(66, 76, 9, 7), 'lens', 'f', ln=True), L([(43, 76), (57, 76)], 'lens', 'f', False, False, 1.8),
              L(rope((60, 2), (64, 60), (58, 112), 6), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 70), (52, 104), (30, 118), (2, 120, 1), (4, 80), (4, 30), (18, 6), (50, -2), (78, 6), (92, 24), (92, 44), (78, 44), (64, 50)])),
             L(outline([(4, 40), (34, 40), (46, 90), (30, 112), (6, 112)]), 'shade', 'b', False),
             L([(64, 50), (70, 80), (72, 104)], 'mid', 'f', False, False, 2.2)]
            + [L(ell(72, y, 2.4, 2.4), c, 'f', ln=True) for y, c in ((84, 'bead1'), (90, 'bead2'), (96, 'bead1'), (102, 'bead3'))]
            + [L(outline([(76, 70), (94, 70), (94, 82), (78, 82)]), 'lens', 'f', ln=True)],
    'back': [L(outline([(4, 118), (6, 70), (4, 30), (18, 6), (50, -2), (82, 6), (96, 30), (94, 70), (96, 118), (70, 126), (50, 130, 1), (30, 126)])),
             L(outline([(56, 2), (86, 14), (96, 40), (96, 116), (64, 124)]), 'shade', 'b', False)],
}
# Ian Ferrum: piel morena; pelo verde lima en casco con flequillo de mechones en punta y un brote de dos hojas en lo alto;
# ojos negros grandes y una sonrisa con dos dientes de conejo
CHARS['ian-ferrum'] = {
    'body': 'bajito', 'pal': pal('#a8c058', '#a8703e', shade='#7a8a3e', leaf='#a8c058'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(48, 6), (48, -8), (34, -12), (28, -18), (42, -18), (50, -12), (58, -18), (72, -18), (66, -12), (52, -8), (52, 6)]), 'leaf', 'b', ln=True),
              L(outline([(10, 74, 1), (12, 40), (24, 12), (50, 2), (76, 12), (88, 40), (90, 74, 1), (82, 60), (72, 50), (62, 58, 1), (54, 48), (46, 56, 1), (38, 48), (28, 58, 1), (18, 54)])),
              L(outline([(60, 6), (82, 18), (88, 46), (84, 64), (74, 40)]), 'shade', 'b', False)],
    'side': [L(outline([(54, 6), (52, -10), (44, -18), (56, -16), (58, 6)]), 'leaf', 'b', ln=True),
             L(outline([(44, 92), (22, 88), (12, 64), (12, 36), (24, 12), (52, 2), (76, 8), (92, 26), (96, 50), (90, 62, 1), (84, 46), (68, 44), (56, 52), (52, 66), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(48, 6), (48, -8), (34, -12), (28, -18), (42, -18), (50, -12), (58, -18), (72, -18), (66, -12), (52, -8), (52, 6)]), 'leaf', 'b', ln=True),
             L(outline([(4, 64, 1), (12, 60), (10, 36), (24, 12), (50, 2), (76, 12), (90, 36), (88, 60), (96, 64, 1), (86, 76), (50, 86), (14, 76)])),
             L(outline([(40, 6), (76, 14), (90, 40), (86, 74), (50, 84), (40, 40)]), 'shade', 'b', False)],
}
# Quint Hampton: piel morena; afro castaño muy oscuro enorme y redondo, abultado en mechones; ojos dorados y una sonrisa
CHARS['quint-hampton'] = {
    'body': 'normal', 'pal': pal('#2e2218', '#a8703e', iris='#b89020', shade='#1e1610', light='#4a3a2e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(10, 80), (14, 56), (24, 46), (40, 50), (52, 44), (66, 50), (80, 46), (88, 56), (90, 80)]},
    'front': messy('front', 4, 16, seed=901, rx=62, ry=56, cy=40, lo=84),
    'side': messy('side', 4, 14, seed=901, rx=58, ry=56, cy=40, nape=100),
    'back': messy('back', 4, 16, seed=901, rx=62, ry=56, cy=40, nape=104),
}
# Yasir Haddad: la cabeza rapada en verde oliva y dos coletas de rastas gruesas atadas a los lados que caen hacia fuera;
# cejas verdes, ojos blancos pequeños y una sonrisa
CHARS['yasir-haddad'] = {
    'body': 'normal', 'pal': pal('#4a5a24', '#a8703e', shade='#36421a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(rope((14, 76), (2, 80), (-6, 96), 9), 'mid', 'b', ln=True), L(rope((16, 80), (8, 92), (4, 104), 9), 'mid', 'b', ln=True),
              L(rope((86, 76), (98, 80), (106, 96), 9), 'mid', 'b', ln=True), L(rope((84, 80), (92, 92), (96, 104), 9), 'mid', 'b', ln=True),
              L(blob(SKULL_F), 'skin'),
              L(outline([(14, 60), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (86, 60), (76, 44), (50, 36), (24, 44)]), 'mid', 'f'),
              L(outline([(24, 64), (36, 60), (42, 66), (30, 66)]), 'mid', 'f', ln=True), L(outline([(76, 64), (64, 60), (58, 66), (70, 66)]), 'mid', 'f', ln=True)]
             + white_eyes(76, 14, 4.4, 4.4, 1.6),
    'side': [L(rope((30, 70), (14, 80), (6, 98), 9), 'mid', 'b', ln=True), L(rope((34, 74), (24, 88), (20, 104), 9), 'mid', 'b', ln=True), L(rope((40, 74), (36, 90), (36, 104), 9), 'mid', 'b', ln=True)]
            + bald('side') + buzz('side') + side_eye(76),
    'back': bald('back') + buzz('back', nape=86)
            + [L(rope((22, 70), (6, 80), (-6, 96), 9), 'mid', 'f', ln=True), L(rope((26, 74), (14, 90), (8, 104), 9), 'mid', 'f', ln=True),
               L(rope((78, 70), (94, 80), (106, 96), 9), 'mid', 'f', ln=True), L(rope((74, 74), (86, 90), (92, 104), 9), 'mid', 'f', ln=True)],
}
# Keith Ryan: un afro rojo coral enorme y redondo que le cae hasta los ojos; gafas de sol azul oscuro envolventes y la boca
# en una O pequeña
CHARS['keith-ryan'] = {
    'body': 'normal', 'pal': pal('#f06a50', '#a8703e', shade='#c84a36', light='#ff9a80', lens='#1e3a5a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(-12, 74), (-14, 36), (0, 6), (30, -12), (70, -12), (100, 6), (114, 36), (112, 74), (96, 82), (80, 66), (20, 66), (4, 82)])),
              L(outline([(60, -8), (98, 8), (112, 40), (108, 72), (94, 78), (82, 40)]), 'shade', 'b', False),
              L(outline([(20, 6), (36, 0), (30, 10)]), 'light', 'b', False), L(outline([(60, 2), (76, 4), (68, 10)]), 'light', 'b', False),
              L(outline([(14, 66), (48, 66), (50, 72), (52, 66), (86, 66), (84, 80), (60, 84), (50, 76), (40, 84), (16, 80)]), 'lens', 'f', ln=True),
              L(ell(50, 98, 4, 3.4), (120, 40, 40, 255), 'f', ln=True)],
    'side': [L(outline([(52, 74), (40, 92), (10, 90), (-12, 70), (-12, 30), (6, 2), (40, -12), (76, -8), (100, 10), (108, 40), (100, 62), (80, 64), (64, 66)])),
             L(outline([(-8, 40), (30, 40), (44, 80), (12, 88)]), 'shade', 'b', False),
             L(outline([(76, 66), (96, 66), (96, 80), (80, 80)]), 'lens', 'f', ln=True)],
    'back': [L(outline([(-12, 74), (-14, 36), (0, 6), (30, -12), (70, -12), (100, 6), (114, 36), (112, 74), (96, 90), (50, 96), (4, 90)])),
             L(outline([(56, -8), (98, 8), (112, 40), (108, 80), (66, 92)]), 'shade', 'b', False)],
}
# Maximino Cruz: piel morena; rastas castañas gruesas y largas que le caen alrededor de la cara, y una cinta ancha verde y
# amarilla en la frente; ojos negros grandes y una sonrisa de labios gruesos
CHARS['maximino-cruz'] = {
    'body': 'normal', 'pal': pal('#6a3a1e', '#8a5a2e', shade='#4e2a14', band='#2a6a2a', band2='#e8c020', lip='#a8603a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': dreads('front', 8, 50, 9) + [L(outline([(12, 60), (14, 26), (28, 8), (50, 2), (72, 8), (86, 26), (88, 60), (82, 52), (18, 52)]))]
             + [L(outline([(16, 52), (16, 34), (50, 30), (84, 34), (84, 52), (50, 48)]), 'band', 'f', ln=True), L(outline([(36, 31), (64, 31), (64, 50), (36, 50)]), 'band2', 'f', False)]
             + [L(rope((22, 52), (16, 76), (14, 104), 8), 'mid', 'f', ln=True), L(rope((78, 52), (84, 76), (86, 104), 8), 'mid', 'f', ln=True),
                L(outline([(32, 94), (50, 90), (68, 94), (62, 104), (38, 104)]), 'lip', 'f', ln=True)],
    'side': dreads('side', 7, 56, 9) + [L(outline([(44, 92), (22, 88), (12, 60), (14, 30), (28, 8), (54, 2), (80, 10), (90, 26), (88, 40), (60, 40), (40, 52)]))]
            + [L(outline([(10, 44), (14, 30), (92, 30), (92, 44)]), 'band', 'f', ln=True)],
    'back': [L(outline([(12, 80), (12, 26), (28, 8), (50, 2), (72, 8), (88, 26), (88, 80), (50, 86)]))] + dreads('back', 8, 50, 9),
}
# Gareth Flare: piel morena; pelo rubio claro en pinchos largos que suben como llamas y dos mechones que le bajan por las
# mejillas; ojos morados y media sonrisa
CHARS['gareth-flare'] = {
    'body': 'normal', 'pal': pal('#f0dc90', '#a8703e', iris='#5a4aa8', shade='#c8b060', light=WHITE),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 66), (8, 50), (-12, 48, 1), (6, 38), (6, 24), (14, -4, 1), (28, 10), (34, -16, 1), (44, 4), (50, -24, 1), (56, 4), (66, -16, 1), (72, 10), (86, -4, 1),
                         (94, 24), (94, 38), (112, 48, 1), (92, 50), (88, 66)])),
              L(outline([(56, 4), (66, -12, 1), (72, 12), (84, 2, 1), (92, 26), (90, 50), (78, 30)]), 'shade', 'b', False),
              L(outline([(12, 66, 1), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (88, 66, 1), (76, 50), (50, 42), (24, 50)]), 'mid', 'f'),
              L(outline([(14, 60), (24, 62), (28, 90), (20, 96, 1)]), 'mid', 'f', ln=True), L(outline([(86, 60), (76, 62), (72, 90), (80, 96, 1)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-6, 54, 1), (10, 46), (8, 26), (-10, 16, 1), (18, 10), (26, -14, 1), (40, 2), (58, -20, 1), (64, 2), (82, -4, 1), (82, 16), (94, 30),
                        (82, 44), (64, 48), (54, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(58, 58), (70, 60), (80, 92), (70, 96, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 80), (8, 50), (-12, 48, 1), (6, 38), (6, 24), (14, -4, 1), (28, 10), (34, -16, 1), (44, 4), (50, -24, 1), (56, 4), (66, -16, 1), (72, 10), (86, -4, 1),
                        (94, 24), (94, 38), (112, 48, 1), (92, 50), (88, 80), (50, 86)])),
             L(outline([(56, 4), (86, 4), (92, 50), (86, 78), (64, 84)]), 'shade', 'b', False)],
}
# Drago Hill: piel morena; rastas verde jade gruesas y largas que le caen desde la coronilla por todos los lados; ojeras
# moradas, ojos blancos de enfado y labios gruesos
CHARS['drago-hill'] = {
    'body': 'normal', 'pal': pal('#3aa078', '#8a5a2e', shade='#2a7858', lip='#e8b080', bag='#7a5a9a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False},
    'front': dreads('front', 8, 56, 8) + [L(outline([(18, 50), (18, 26), (30, 8), (50, 2), (70, 8), (82, 26), (82, 50), (50, 40)]))]
             + [L(rope((20, 30), (12, 70), (10, 108), 8), 'mid', 'f', ln=True), L(rope((80, 30), (88, 70), (90, 108), 8), 'mid', 'f', ln=True),
                L(outline([(22, 72), (42, 70), (42, 84), (24, 84)]), 'bag', 'f', False), L(outline([(78, 72), (58, 70), (58, 84), (76, 84)]), 'bag', 'f', False)]
             + white_eyes(76, 16, 6, 4.4, 1.8)
             + [L([(24, 70), (42, 74)], OUTC, 'f', False, False, 2.4), L([(76, 70), (58, 74)], OUTC, 'f', False, False, 2.4),
                L(outline([(34, 100), (50, 96), (66, 100), (60, 108), (40, 108)]), 'lip', 'f', ln=True)],
    'side': dreads('side', 7, 60, 8) + [L(blob(SIDE_SKULL), 'skin'), L(outline([(12, 50), (14, 22), (30, 6), (56, 2), (80, 10), (88, 24), (60, 24), (36, 34)]), 'shade', 'f')] + side_eye(76),
    'back': [L(blob(SKULL_B), 'skin')] + dreads('back', 9, 60, 8),
}
# Keenan DiFortune (portero suplente): piel morena; pelo verde oscuro recogido arriba en un moño de pinchos con una goma roja
# y las sienes en verde más claro rapado; ojos rojos y una sonrisa
CHARS['keenan-difortune'] = {
    'body': 'normal', 'pal': pal('#3a6a1e', '#a8703e', iris='#c82a1e', shave='#7aa04a', shade='#2a5014', tie='#c82a1e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(14, 60), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (86, 60), (76, 46), (24, 46)]), 'shave', 'f'),
              L(outline([(26, 50), (24, 30), (10, 14, 1), (30, 12), (34, -4, 1), (44, 6), (50, -16, 1), (56, 6), (66, -4, 1), (70, 12), (90, 14, 1), (76, 30), (74, 50), (50, 58, 1)]), 'mid', 'f', ln=True),
              L(outline([(56, 6), (66, 0, 1), (70, 14), (84, 16, 1), (74, 30), (72, 48), (62, 30)]), 'shade', 'f', False), L(ell(50, 4, 4, 2.6), 'tie', 'f', ln=True)],
    'side': bald('side') + [L(outline([(44, 90), (22, 86), (12, 64), (12, 30), (26, 10), (52, 2), (78, 8), (90, 24), (88, 34), (70, 34), (58, 42), (50, 62), (48, 80)]), 'shave', 'f'),
                            L(outline([(30, 40), (20, 16), (-4, 10, 1), (24, 4), (30, -12, 1), (44, 2), (60, -8, 1), (66, 8), (88, 4, 1), (80, 22), (60, 30)]), 'mid', 'f', ln=True),
                            L(ell(40, 2, 3, 4), 'tie', 'f', ln=True)],
    'back': bald('back') + [L(outline([(14, 84), (12, 30), (24, 10), (50, 4), (76, 10), (88, 30), (86, 84), (50, 90)]), 'shave', 'f'),
                            L(outline([(20, 44), (10, 20, 1), (30, 18), (34, 0, 1), (44, 10), (50, -10, 1), (56, 10), (66, 0, 1), (70, 18), (90, 20, 1), (80, 44), (50, 54)]), 'mid', 'f', ln=True)],
}
# Jarell Mangrove: piel morena; pelo castaño oscuro corto con cuatro moñitos en punta atados con gomas naranjas; ojos
# negros grandes y los labios gruesos naranjas
CHARS['jarell-mangrove'] = {
    'body': 'bajito', 'pal': pal('#2e2218', '#8a5a2e', tie='#e0601a', lip='#e8a060'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'none', 'hairline': (52, 46)},
    'front': [L(outline([(x, y), (x + dx, y + dy, 1), (x + 6, y + 2)]), 'mid', 'b', ln=True) for x, y, dx, dy in ((10, 30, -16, -14), (20, 10, -8, -20), (74, 10, 14, -20), (84, 30, 22, -14))]
             + [L(ell(x, y, 3.6, 2.4), 'tie', 'b', ln=True) for x, y in ((6, 26), (20, 4), (80, 4), (94, 26))]
             + [L(outline([(12, 66), (10, 34), (22, 12), (50, 4), (78, 12), (90, 34), (88, 66), (80, 58), (20, 58)]))],
    'side': [L(outline([(x, y), (x + dx, y + dy, 1), (x + 6, y + 2)]), 'mid', 'b', ln=True) for x, y, dx, dy in ((22, 14, -14, -18), (14, 44, -20, -6), (56, 4, 4, -20))]
            + [L(blob(SIDE_SKULL)), L(outline([(16, 46), (18, 76), (38, 88), (28, 60)]), 'shade', 'b', False)]
            + [L(outline([(80, 94), (92, 92), (92, 100), (82, 100)]), 'lip', 'f', ln=True)],
    'back': [L(outline([(12, 80), (10, 34), (22, 12), (50, 4), (78, 12), (90, 34), (88, 80), (50, 88)]))]
            + [L(outline([(x, y), (x + dx, y + dy, 1), (x + 6, y + 2)]), 'mid', 'f', ln=True) for x, y, dx, dy in ((10, 30, -16, -14), (20, 10, -8, -20), (74, 10, 14, -20), (84, 30, 22, -14))]
            + [L(ell(x, y, 3.6, 2.4), 'tie', 'f', ln=True) for x, y in ((6, 26), (20, 4), (80, 4), (94, 26))],
}
# Vic Vitrum: un pañuelo amarillo con franjas verde y roja anudado en la cabeza, con dos orejitas de nudo arriba; gafas
# redondas de montura negra y una sonrisa
CHARS['vic-vitrum'] = {
    'body': 'normal', 'pal': pal('#2e2218', '#a8703e', cloth='#f0c030', cloth_d='#c89a20', green='#2a8a3a', red='#c82a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin')]
             + [L(outline([(14, 16), (2, 0, 1), (22, 6)]), 'cloth', 'b', ln=True), L(outline([(86, 16), (98, 0, 1), (78, 6)]), 'cloth', 'b', ln=True)]
             + bandana('front', 'cloth', 'cloth_d', low=62, tails=False)
             + [L(outline([(36, 0), (50, -2), (50, 56), (36, 56)]), 'green', 'f', False), L(outline([(50, -2), (64, 0), (64, 56), (50, 56)]), 'red', 'f', False),
                L(ell(34, 76, 9, 8) + [ell(34, 76, 9, 8)[0]], OUTC, 'f', False, False, 2.2), L(ell(66, 76, 9, 8) + [ell(66, 76, 9, 8)[0]], OUTC, 'f', False, False, 2.2),
                L([(43, 76), (57, 76)], OUTC, 'f', False, False, 1.6)],
    'side': [L(blob(SIDE_SKULL), 'skin')] + bandana('side', 'cloth', 'cloth_d', low=58, tails=False)
            + [L(outline([(50, 2), (56, -16, 1), (62, 4)]), 'cloth', 'f', ln=True), L(ell(86, 76, 4, 7) + [ell(86, 76, 4, 7)[0]], OUTC, 'f', False, False, 2.2),
               L([(50, 74), (82, 74)], OUTC, 'f', False, False, 1.6)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 84), (16, 60), (84, 60), (84, 84), (50, 90)]), 'mid', 'b')]
            + [L(outline([(14, 16), (2, 0, 1), (22, 6)]), 'cloth', 'b', ln=True), L(outline([(86, 16), (98, 0, 1), (78, 6)]), 'cloth', 'b', ln=True)]
            + bandana('back', 'cloth', 'cloth_d', low=62, tails=False)
            + [L(outline([(36, 0), (50, -2), (50, 56), (36, 56)]), 'red', 'f', False), L(outline([(50, -2), (64, 0), (64, 56), (50, 56)]), 'green', 'f', False),
               L(outline([(30, 52), (50, 58), (70, 52), (60, 70), (50, 62), (40, 70)]), 'cloth', 'f', ln=True)],
}
# Li Leung: un pañuelo rojo anudado en la cabeza con dos tiras largas que le caen por la espalda; por debajo asoma el pelo
# rubio blanquecino en puntas a los lados y un mechón en la frente; ojos de sueño y una sonrisa
CHARS['li-leung'] = {
    'body': 'normal', 'pal': pal('#f4ecd0', '#a8703e', shade='#d0c4a0', cloth='#c81e1e', cloth_d='#981414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 60), (-6, 70, 1), (8, 76), (-2, 88, 1), (16, 84)]), 'mid', 'b', ln=True),
              L(outline([(84, 60), (106, 70, 1), (92, 76), (102, 88, 1), (84, 84)]), 'mid', 'b', ln=True),
              L(blob(SKULL_F), 'skin')] + bandana('front', 'cloth', 'cloth_d', low=58, tails=False)
             + [L(outline([(60, 40), (68, 30), (72, 46), (66, 62, 1), (62, 50)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(36, 60), (14, 70, 1), (28, 76), (18, 88, 1), (36, 84)]), 'mid', 'b', ln=True), L(blob(SIDE_SKULL), 'skin')]
            + bandana('side', 'cloth', 'cloth_d', low=54, tails=False)
            + [L(rope((14, 44), (-6, 70), (-14, 106), 7), 'cloth', 'f', ln=True), L(rope((16, 48), (2, 80), (0, 112), 7), 'cloth_d', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(10, 84), (8, 56), (92, 56), (90, 84), (50, 90)]), 'mid', 'b')]
            + bandana('back', 'cloth', 'cloth_d', low=56, tails=False)
            + [L(rope((44, 54), (34, 90), (30, 124), 9), 'cloth', 'f', ln=True), L(rope((56, 54), (66, 90), (70, 124), 9), 'cloth_d', 'f', ln=True),
               L(ell(50, 54, 9, 7), 'cloth', 'f', ln=True)],
}
# Jazzy Hedgeer: piel morena; rastas naranjas gruesas y cortas que salen en todas direcciones desde la coronilla, y una
# visera morada en la frente; ojos negros de enfado
CHARS['jazzy-hedgeer'] = {
    'body': 'normal', 'pal': pal('#e8862a', '#a8703e', shade='#b8661a', visor='#4a3a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin')] + dreads('front', 9, 30, 8, top=2, spread=1.4)
             + [L(outline([(16, 56), (16, 30), (30, 10), (50, 4), (70, 10), (84, 30), (84, 56)]), 'mid', 'f')]
             + [L(rope((50 + d, 12), (50 + d * 1.4, 30), (50 + d * 1.6, 56), 8), 'mid', 'f', ln=True) for d in (-24, -8, 8, 24)]
             + [L(outline([(8, 64), (14, 56), (50, 52), (86, 56), (92, 64), (50, 60)]), 'visor', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin')] + dreads('side', 7, 30, 8, top=0)
            + [L(outline([(10, 50), (14, 24), (30, 6), (56, 0), (80, 8), (90, 26), (70, 30), (40, 40)]), 'mid', 'f')]
            + [L(rope((60, 6), (78, 14), (96, 30), 8), 'mid', 'f', ln=True), L(outline([(44, 56), (94, 54), (110, 62), (92, 64), (46, 62)]), 'visor', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin')] + dreads('back', 9, 34, 8, top=0, spread=1.2)
            + [L(rope((50 + d, 6), (50 + d * 1.2, 40), (50 + d * 1.3, 74), 8), 'mid', 'f', ln=True) for d in (-28, -14, 0, 14, 28)],
}
