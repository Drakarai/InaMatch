"""Red Matador / Los Rojos (IE3, España): con sus modelos 3D como referencia (contornos calcados sobre una rejilla de
unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_empire import afro
from chars_orpheus import headband
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)

# Fermín Sánchez (portero): un casco de toro rojo con dos cuernos curvados hacia fuera y un pico en medio de la frente, y
# una mascarilla gris que le tapa la boca; ojos blancos de furia
CHARS['ferm-n-s-nchez'] = {
    'body': 'corpulento', 'pal': pal('#2a1e18', '#c8945a', helm='#a81e14', helm_d='#7a140e', mask='#8a8480'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(20, 30), (6, 12), (-2, -10), (6, -20, 1), (10, 0), (24, 14)]), 'helm', 'b', ln=True),
              L(outline([(80, 30), (94, 12), (102, -10), (94, -20, 1), (90, 0), (76, 14)]), 'helm', 'b', ln=True),
              L(outline([(10, 92), (8, 40), (18, 14), (40, 4), (50, -18, 1), (60, 4), (82, 14), (92, 40), (90, 92), (78, 82), (78, 70), (60, 64), (50, 70), (40, 64), (22, 70), (22, 82)]),
                'helm', 'f', ln=True),
              L(outline([(58, 6), (80, 16), (90, 40), (88, 88), (78, 70), (66, 40)]), 'helm_d', 'f', False),
              L(outline([(26, 72), (42, 72), (40, 78), (28, 78)]), WHITE, 'f', ln=True), L(outline([(74, 72), (58, 72), (60, 78), (72, 78)]), WHITE, 'f', ln=True),
              L(outline([(24, 84), (50, 82), (76, 84), (72, 104), (50, 110), (28, 104)]), 'mask', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(30, 20), (20, 0), (24, -20, 1), (36, -2), (40, 14)]), 'helm', 'f', ln=True),
             L(outline([(14, 92), (8, 40), (20, 14), (50, 2), (70, -10, 1), (74, 10), (90, 26), (94, 56), (80, 66), (60, 66), (52, 80), (40, 92)]), 'helm', 'f', ln=True),
             L(outline([(70, 80), (96, 80), (96, 102), (74, 104)]), 'mask', 'f', ln=True), L(ell(14, 74, 6, 6), 'helm_d', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(20, 30), (6, 12), (-2, -10), (6, -20, 1), (10, 0), (24, 14)]), 'helm', 'b', ln=True),
             L(outline([(80, 30), (94, 12), (102, -10), (94, -20, 1), (90, 0), (76, 14)]), 'helm', 'b', ln=True),
             L(outline([(10, 80), (8, 40), (18, 14), (40, 4), (50, -14, 1), (60, 4), (82, 14), (92, 40), (90, 80), (50, 84)]), 'helm', 'f', ln=True),
             L(outline([(38, 72), (50, 68), (62, 72), (56, 78), (50, 74), (44, 78)]), 'mask', 'f', ln=True)],
}
# José Costa: piel morena; pelo castaño oscuro con tres pinchos de cresta en lo alto y dos matas rizadas a los lados de la
# cara; ojos de pasmo, nariz redonda y una sonrisa enorme de colmillos
CHARS['jos-costa'] = {
    'body': 'normal', 'pal': pal('#3a3024', '#b87a40', shade='#2a2218'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'nose': (50, 84, 4), 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + [L(outline([(18, 48), (20, 20), (30, 2), (36, -12, 1), (44, 2), (50, -16, 1), (56, 2), (64, -12, 1), (70, 2), (80, 20), (82, 48), (64, 34), (50, 30), (36, 34)]), 'mid', 'f')]
             + [L(outline([(16, 60), (0, 66), (-10, 82), (0, 96), (16, 92), (22, 76)]), 'mid', 'b', ln=True),
                L(outline([(84, 60), (100, 66), (110, 82), (100, 96), (84, 92), (78, 76)]), 'mid', 'b', ln=True)]
             + white_eyes(74, 14, 6.4, 6.4, 2.4)
             + [L(outline([(24, 92), (50, 98), (76, 92), (66, 106), (50, 110), (34, 106)]), WHITE, 'f', ln=True), L(quad((26, 94), (50, 102), (74, 94)), OUTC, 'f', False, False, 1.0)],
    'side': bald('side') + buzz('side') + [L(outline([(30, 64), (14, 66), (4, 80), (10, 96), (26, 94), (34, 80)]), 'mid', 'f', ln=True)] + side_eye(74),
    'back': bald('back') + buzz('back', nape=80)
            + [L(outline([(36, 6), (40, -10, 1), (46, 4), (50, -14, 1), (54, 4), (60, -10, 1), (64, 6)]), 'mid', 'f', ln=True),
               L(outline([(14, 66), (-6, 72), (-14, 86), (0, 96), (20, 92)]), 'mid', 'f', ln=True), L(outline([(86, 66), (106, 72), (114, 86), (100, 96), (80, 92)]), 'mid', 'f', ln=True)],
}
# José López: cara larguísima y pálida; melena negra azulada lisa con raya en medio que le cae hasta los hombros abriéndose
# en puntas; ojos negros hundidos con ojeras y la boca en una raya
CHARS['jos-l-pez'] = {
    'body': 'delgado', 'pal': pal('#1e2a3e', '#ecd8b8', shade='#14202e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 104, 'face_front': LONG_FACE, 'nose': (50, 88, 2.6), 'hairline': [(16, 80), (18, 46), (30, 34), (50, 30), (70, 34), (82, 46), (84, 80)]},
    'front': longhair('front', 112, 22, part=True)
             + [L(ell(34, 74, 7, 5.4), (30, 24, 24, 255), 'f', False), L(ell(66, 74, 7, 5.4), (30, 24, 24, 255), 'f', False),
                L(ell(34, 74, 2, 2), (160, 30, 30, 255), 'f', False), L(ell(66, 74, 2, 2), (160, 30, 30, 255), 'f', False)],
    'side': longhair('side', 112, 18),
    'back': longhair('back', 112, 22, part=True, ends=3),
}
# Antonio Gallego: pelo azul marino peinado hacia atrás en pinchos, con una corona de pinchos naranjas en lo alto sujeta por
# una cinta, dos coletas con anillas doradas a los lados; ojos verdes de cansancio
CHARS['antonio-gallego'] = {
    'body': 'normal', 'pal': pal('#1e2e4a', '#c88a50', iris='#4a8a3a', shade='#142038', orange='#e06a1e', band='#c8a050', ring='#d8a020'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': (46, 40)},
    'front': [L(outline([(14, 70), (2, 60, 1), (8, 44), (-4, 30, 1), (12, 22), (14, 4), (24, -16, 1), (34, 2), (50, -22, 1), (66, 2), (76, -16, 1), (86, 4), (88, 22), (104, 30, 1),
                         (92, 44), (98, 60, 1), (86, 70), (82, 40), (18, 40)])),
              L(outline([(34, 2), (40, -14, 1), (46, 2)]), 'orange', 'b', ln=True), L(outline([(54, 2), (60, -14, 1), (66, 2)]), 'orange', 'b', ln=True),
              L(outline([(20, 6), (24, -8, 1), (30, 6)]), 'orange', 'b', ln=True), L(outline([(70, 6), (76, -8, 1), (80, 6)]), 'orange', 'b', ln=True),
              L(quad((14, 40), (50, 30), (86, 40)), 'band', 'f', False, False, 2.4),
              L(rope((12, 74), (6, 90), (10, 106), 6), 'mid', 'f', ln=True), L(rope((88, 74), (94, 90), (90, 106), 6), 'mid', 'f', ln=True),
              L(ell(8, 98, 3, 2), 'ring', 'f', ln=True), L(ell(92, 98, 3, 2), 'ring', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-4, 50, 1), (10, 42), (-6, 26, 1), (14, 20), (16, 0, 1), (32, 8), (44, -14, 1), (54, 6), (70, -6, 1), (78, 12), (90, 26),
                        (88, 40), (74, 42), (60, 46), (52, 62), (50, 80)])),
             L(outline([(50, 6), (56, -14, 1), (62, 6)]), 'orange', 'b', ln=True), L(quad((12, 40), (50, 32), (88, 38)), 'band', 'f', False, False, 2.4),
             L(rope((30, 72), (24, 88), (28, 104), 6), 'mid', 'f', ln=True), L(ell(26, 96, 3, 2), 'ring', 'f', ln=True)],
    'back': [L(outline([(14, 86), (2, 60, 1), (8, 44), (-4, 30, 1), (12, 22), (14, 4), (24, -16, 1), (34, 2), (50, -22, 1), (66, 2), (76, -16, 1), (86, 4), (88, 22), (104, 30, 1),
                        (92, 44), (98, 60, 1), (86, 86), (50, 92)])),
             L(outline([(34, 2), (40, -14, 1), (46, 2)]), 'orange', 'b', ln=True), L(outline([(54, 2), (60, -14, 1), (66, 2)]), 'orange', 'b', ln=True),
             L(quad((10, 42), (50, 36), (90, 42)), 'band', 'f', False, False, 2.4)],
}
# Queraldo Naval: piel morena; melena granate larga y ondulada que le cae por los lados hasta los hombros; rayas de tigre en
# las mejillas, ojos dorados de enfado y un colmillo
CHARS['queraldo-naval'] = {
    'body': 'normal', 'pal': pal('#7a1e14', '#b87a40', iris='#d0a020', shade='#5a140e', stripe='#7a2a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(16, 80), (18, 46), (32, 34), (50, 30), (68, 34), (82, 46), (84, 80)]},
    'front': longhair('front', 108, 20, part=True)
             + [L([(22, 86), (34, 84)], 'stripe', 'f', False, False, 1.8), L([(22, 92), (32, 90)], 'stripe', 'f', False, False, 1.8),
                L([(78, 86), (66, 84)], 'stripe', 'f', False, False, 1.8), L([(78, 92), (68, 90)], 'stripe', 'f', False, False, 1.8),
                L([(56, 98), (58, 102), (60, 98)], WHITE, 'f', False)],
    'side': longhair('side', 108, 16),
    'back': longhair('back', 108, 20, part=True, ends=2),
}
# Juan Nadal: un afro castaño oliva enorme de mechones cuadrados que le cae por la frente; ojos verdes de pillo y una sonrisa
CHARS['juan-nadal'] = dict({
    'body': 'normal', 'pal': pal('#4a3e1a', '#e8a868', iris='#4a8a3a', shade='#342a12', light='#6a5a2e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (66, 54)},
}, **afro(1201, rx=62, ry=56, cy=36, amp=8, n=12, lo=76, nape=98))
# Igor Ferreira: pelo castaño muy abultado y redondo, en forma de casco, que le tapa la frente hasta los ojos y cae por los
# lados; ojos de sueño y una sonrisa
CHARS['igor-ferreira'] = dict({
    'body': 'normal', 'pal': pal('#5a3a20', '#fcd8b0', shade='#42281a', light='#7a5a34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (72, 66)},
}, **afro(1202, rx=62, ry=58, cy=38, amp=3, n=14, lo=96, nape=104))
# Miguel Pereira: pelo azul petróleo oscuro peinado hacia un lado en un tupé abultado, con un mechón que le cae por la
# frente; ojos negros grandes y la boca seria
CHARS['miguel-pereira'] = {
    'body': 'normal', 'pal': pal('#1e3a4a', '#e8a868', shade='#142a36'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 70), (6, 36), (18, 10), (44, -2), (72, 0), (90, 14), (100, 30, 1), (94, 40), (88, 70), (80, 62), (20, 62)])),
              L(outline([(60, 2), (86, 14), (96, 32), (90, 62), (78, 36)]), 'shade', 'b', False),
              L(outline([(12, 66), (14, 40), (30, 22), (52, 16), (74, 20), (88, 36), (90, 56), (78, 46), (60, 44), (46, 50), (36, 62), (30, 74, 1), (26, 58), (18, 62)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 34), (22, 10), (52, 0), (80, 6), (96, 20), (100, 36), (88, 40), (72, 42), (58, 48), (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 84), (6, 36), (18, 10), (50, -2), (82, 10), (96, 36), (90, 84), (50, 90)])),
             L(outline([(56, 2), (86, 16), (96, 44), (90, 82), (64, 88)]), 'shade', 'b', False)],
}
# Pedro Moreno: pelo castaño dorado en una melena abultada con un mechón grande que le tapa la frente hasta la nariz y una
# cinta naranja fina; la boca abierta gritando con colmillos
CHARS['pedro-moreno'] = {
    'body': 'normal', 'pal': pal('#a0661e', '#e8a868', shade='#7a4c14', band='#d0601a', mouth='#9a3a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': longhair('front', 96, 26, top=-4)
             + [L(outline([(16, 64), (14, 40), (24, 14), (40, 0), (50, -4), (60, 0), (76, 14), (86, 40), (84, 64), (70, 56), (60, 70), (50, 80, 1), (40, 70), (30, 56)]), 'mid', 'f', ln=True),
                L(outline([(50, 0), (62, 2), (72, 20), (64, 50), (52, 74)]), 'shade', 'f', False)] + headband('front', 46, 'band')
             + [L(outline([(30, 90), (50, 86), (70, 90), (66, 104), (50, 110), (34, 104)]), 'mouth', 'f', ln=True), L(outline([(30, 90), (70, 90), (66, 94), (34, 94)]), WHITE, 'f', False)],
    'side': longhair('side', 96, 24, top=-4) + headband('side', 44, 'band') + [L(outline([(76, 0), (92, -4), (96, 10), (86, 20)]), 'mid', 'f', ln=True)],
    'back': longhair('back', 96, 26, top=-4, ends=3) + headband('back', 46, 'band'),
}
# Samuel Mayo: pelo negro azulado de pinchos grandes hacia arriba con dos mechones turquesa, y unas patillas en punta que le
# bajan por las mejillas; ojos turquesa de enfado y la boca seria
CHARS['samuel-mayo'] = {
    'body': 'normal', 'pal': pal('#1e2638', '#c88a50', iris='#2aa0a0', shade='#141a28', streak='#2a9aa0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (56, 50)},
    'front': [L(outline([(12, 68), (6, 50), (-10, 46, 1), (6, 36), (12, 14), (24, -10, 1), (34, 6), (50, -22, 1), (62, 2), (80, -10, 1), (86, 14), (92, 36), (110, 46, 1), (94, 50),
                         (88, 68), (82, 60), (18, 60)])),
              L(outline([(56, 4), (78, -6, 1), (84, 16), (92, 40), (86, 62), (76, 32)]), 'shade', 'b', False),
              L(outline([(36, 8), (46, -14, 1), (50, 6), (44, 30)]), 'streak', 'b', False), L(outline([(52, 8), (58, -6, 1), (60, 12), (54, 30)]), 'streak', 'b', False),
              L(outline([(14, 60), (24, 62), (30, 84, 1), (18, 76)]), 'mid', 'f', ln=True), L(outline([(86, 60), (76, 62), (70, 84, 1), (82, 76)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-6, 60, 1), (8, 48), (-10, 34, 1), (12, 26), (8, 4, 1), (28, 12), (40, -14, 1), (52, 6), (74, -6, 1), (78, 14), (90, 28),
                        (82, 42), (64, 46), (54, 62), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False),
             L(outline([(58, 56), (70, 58), (78, 84, 1), (64, 74)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 80), (6, 50), (-10, 46, 1), (6, 36), (12, 14), (24, -10, 1), (34, 6), (50, -22, 1), (62, 2), (80, -10, 1), (86, 14), (92, 36), (110, 46, 1), (94, 50),
                        (88, 80), (50, 88)])),
             L(outline([(56, 4), (80, -6, 1), (86, 16), (92, 44), (88, 78), (64, 86)]), 'shade', 'b', False)],
}
# Davi Peroquê: pelo gris claro peinado hacia atrás en ondas, que se abre en puntas hacia fuera en la nuca y a los lados;
# cejas en punta, ojos azules de enfado y una nariz larga
CHARS['davi-peroqu'] = {
    'body': 'normal', 'pal': pal('#b0aeae', '#e0a050', iris='#3a7a9a', shade='#8a8888'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 86, 3), 'hairline': (56, 46)},
    'front': [L(outline([(-6, 88, 1), (10, 78), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (90, 78), (106, 88, 1), (88, 84), (82, 62), (18, 62), (12, 84)])),
              L(outline([(60, 6), (84, 18), (92, 44), (90, 82), (80, 50)]), 'shade', 'b', False)]
             + [strand([(x, 6 + abs(x - 50) * 0.2), (x + (x - 50) * 0.3, 40)], 'shade', 'b', 1.2) for x in (30, 44, 58, 72)],
    'side': [L(outline([(44, 92), (22, 88), (8, 80), (-8, 88, 1), (6, 70), (8, 36), (22, 10), (52, 2), (78, 8), (92, 26), (90, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(-6, 90, 1), (10, 78), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (90, 78), (106, 90, 1), (80, 88), (70, 98, 1), (60, 88), (50, 96, 1), (40, 88), (30, 98, 1),
                        (20, 88)])),
             L(outline([(56, 6), (84, 18), (92, 48), (90, 84), (64, 90)]), 'shade', 'b', False)],
}
# Juan Espíndola (portero suplente): melena verde muy oscuro rizada y abultada, que le tapa un ojo y cae por los lados en
# mechones; el otro ojo de sueño y la boca seria
CHARS['juan-espindola'] = {
    'body': 'normal', 'pal': pal('#24402e', '#e0a868', shade='#18301e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': longhair('front', 98, 24, top=-4)
             + [L(outline([(12, 66), (14, 40), (28, 20), (50, 12), (72, 20), (86, 40), (88, 64), (76, 54), (64, 56), (58, 70), (52, 90, 1), (46, 70), (36, 66), (22, 74)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 98, 22, top=-4),
    'back': longhair('back', 98, 24, top=-4, ends=3),
}
# Isaac César: pelo verde azulado recogido atrás en un moño, con dos mechones morados en punta que le salen en la frente y
# mechones gruesos que le caen por los lados; ojos morados de enfado
CHARS['isaac-c-sar'] = {
    'body': 'normal', 'pal': pal('#2a7a6a', '#d8a060', iris='#5a3a8a', shade='#1e5a4e', streak='#7a5aaa'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (52, 42)},
    'front': [L(outline([(10, 90), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (90, 90), (80, 80), (80, 62), (20, 62), (20, 80)])),
              L(outline([(60, 6), (84, 18), (92, 44), (88, 86), (80, 50)]), 'shade', 'b', False),
              L(outline([(30, 30), (16, 4, 1), (34, 14), (40, 2, 1), (42, 30)]), 'streak', 'f', ln=True)]
             + [strand([(x, 8 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 40)], 'shade', 'b', 1.2) for x in (52, 64, 76)],
    'side': [L(outline([(44, 92), (22, 88), (10, 80), (2, 90), (10, 70), (8, 36), (22, 10), (52, 2), (78, 8), (92, 26), (90, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(ell(10, 46, 8, 8), 'mid', 'b', ln=True), L(outline([(10, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False),
             L(outline([(64, 14), (74, -6, 1), (80, 14)]), 'streak', 'f', ln=True)],
    'back': [L(outline([(10, 90), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (90, 90), (70, 84), (50, 90), (30, 84)])),
             L(outline([(56, 6), (84, 18), (92, 48), (90, 88), (64, 86)]), 'shade', 'b', False),
             L(ell(52, 56, 9, 9), 'mid', 'f', ln=True), L(outline([(76, 10), (84, -8, 1), (86, 16)]), 'streak', 'f', ln=True)]
            + [strand([(x, 4), (52, 50)], 'shade', 'b', 1.0) for x in (24, 40, 64, 80)],
}
# Laudelino Castor: pelo castaño oliva en pinchos cortos hacia arriba, con un flequillo recto y una barba que le baja por la
# mandíbula; cara alargada de mejillas hundidas, ojos verdes de enfado y una nariz larga en punta
CHARS['laudelino-castor'] = {
    'body': 'normal', 'pal': pal('#6a5a24', '#f0c088', iris='#4a8a3a', shade='#4e421a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': messy('front', 7, 11, seed=1203, rx=46, ry=40, cy=34, lo=56)
             + [L(outline([(14, 50), (16, 34), (30, 26), (50, 24), (70, 26), (84, 34), (86, 50), (74, 46), (50, 48), (26, 46)]), 'mid', 'f'),
                L(outline([(16, 64), (22, 66), (26, 98), (38, 110), (50, 114), (62, 110), (74, 98), (78, 66), (84, 64), (82, 102), (66, 118), (50, 122, 1), (34, 118), (18, 102)]), 'mid', 'f', ln=True),
                L(outline([(46, 70), (54, 70), (58, 96), (50, 100, 1), (42, 96)]), 'skin_d', 'f', ln=True)],
    'side': messy('side', 11, 9, seed=1203, rx=44, ry=40, cy=34, nape=86, sweep=-0.3)
            + [L(outline([(50, 62), (58, 62), (64, 100), (80, 112), (90, 108), (88, 118), (70, 124), (54, 108)]), 'mid', 'f', ln=True),
               L(outline([(86, 76), (104, 96), (88, 98)]), 'skin', 'f', ln=True)],
    'back': messy('back', 7, 11, seed=1203, rx=46, ry=40, cy=34, nape=90),
}
# Carlos Arroyo: pelo granate abultado peinado hacia atrás que se abre a los lados en puntas onduladas como una melena; ojos
# azules claros de enfado y la boca seria
CHARS['carlos-arroyo'] = {
    'body': 'normal', 'pal': pal('#8a1e2a', '#e8a868', iris='#3aa0c8', shade='#68141e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': [L(outline([(10, 76), (-6, 80, 1), (4, 66), (-10, 56, 1), (6, 48), (4, 30), (18, 8), (50, 0), (82, 8), (96, 30), (94, 48), (110, 56, 1), (96, 66), (106, 80, 1),
                         (90, 76), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (96, 40), (92, 72), (80, 50)]), 'shade', 'b', False), strand([(50, 4), (50, 40)], 'deep', 'b', 1.2)],
    'side': [L(outline([(44, 92), (22, 88), (10, 80), (-4, 84, 1), (6, 66), (-8, 56, 1), (6, 48), (6, 30), (20, 8), (52, 0), (78, 8), (92, 26), (90, 40), (74, 42), (60, 48),
                        (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 80), (-10, 84, 1), (2, 70), (-12, 58, 1), (4, 50), (4, 30), (18, 8), (50, 0), (82, 8), (96, 30), (96, 50), (112, 58, 1), (98, 70), (110, 84, 1),
                        (90, 82), (78, 92, 1), (66, 84), (50, 90), (34, 84), (22, 92, 1)])),
             L(outline([(56, 4), (86, 16), (98, 44), (98, 80), (64, 86)]), 'shade', 'b', False)],
}
# Federico Rubiera: pelo castaño corto despeinado de puntas con flequillo hasta las cejas y dos mechones finos largos que
# le cuelgan por detrás de las orejas; ojos negros grandes y la boca seria
CHARS['federico-rubiera'] = {
    'body': 'normal', 'pal': pal('#6a3a1e', '#fcc890', shade='#4e2a14'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 5, 13, seed=1204, rx=48, ry=40, lo=66)
             + [L(outline([(12, 66, 1), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 66, 1), (80, 54), (72, 62, 1), (64, 50), (56, 60, 1), (50, 50), (42, 60, 1),
                           (36, 50), (28, 62, 1), (20, 54)]), 'mid', 'f'),
                L([(14, 70), (12, 92), (14, 108)], 'mid', 'b', False, False, 2.2), L([(86, 70), (88, 92), (86, 108)], 'mid', 'b', False, False, 2.2)],
    'side': messy('side', 6, 11, seed=1204, rx=46, ry=40, nape=92, sweep=-0.2) + [L([(40, 76), (38, 96), (40, 112)], 'mid', 'f', False, False, 2.2)],
    'back': messy('back', 5, 13, seed=1204, rx=48, ry=40, nape=94) + [L([(20, 86), (18, 100), (20, 112)], 'mid', 'f', False, False, 2.2),
                                                                      L([(80, 86), (82, 100), (80, 112)], 'mid', 'f', False, False, 2.2)],
}
