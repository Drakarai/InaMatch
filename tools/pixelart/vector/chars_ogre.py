"""Ogre / Equipo Ogro (IE3): los del futuro, con sus modelos 3D como referencia (contornos calcados sobre una rejilla de
unidades de cabeza); Lump Trungus no tiene modelo: su retrato (es como su gemelo Bump, con una cruz en la frente)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)
BABY_FACE = blob([(10, 40), (50, 30), (90, 40), (102, 70), (96, 100), (74, 114), (26, 114), (4, 100), (-2, 70)])


def elf_ears(view, c='skin'):
    if view == 'front':
        return [L(outline([(10, 66), (-14, 58, 1), (4, 78)]), c, 'b', ln=True), L(outline([(90, 66), (114, 58, 1), (96, 78)]), c, 'b', ln=True)]
    if view == 'side':
        return [L(outline([(40, 66), (22, 58, 1), (40, 80)]), c, 'f', ln=True)]
    return [L(outline([(10, 66), (-14, 58, 1), (4, 78)]), c, 'f', ln=True), L(outline([(90, 66), (114, 58, 1), (96, 78)]), c, 'f', ln=True)]


def tuft(view, c='mid'):
    if view == 'front':
        return [L(outline([(42, 10), (40, -4), (50, -18), (62, -26, 1), (58, -10), (58, 10)]), c, 'f', ln=True)]
    if view == 'side':
        return [L(outline([(48, 6), (50, -10), (62, -22, 1), (64, -6), (60, 6)]), c, 'f', ln=True)]
    return [L(outline([(44, 8), (50, -10), (60, -18, 1), (58, 8)]), c, 'f', ln=True)]


# Lars Luceafăr (portero): piel morena; pelo rubio en pinchos grandes hacia arriba y a un lado, con una cinta negra y roja
# en diagonal que le sujeta unas gafas dobles de lentes verdes sobre un ojo; dos colmillos blancos enormes en la boca
CHARS['lars-luceaf-r'] = {
    'body': 'corpulento', 'pal': pal('#f0d050', '#9a6438', shade='#c8a830', band='#2a2224', band2='#c83a1e', rim='#8a8a6a', lens='#5a7a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': (52, 40), 'big_ears': 2, 'ear_out': 6},
    'front': [L(outline([(16, 46), (14, 24), (22, 6), (18, -18, 1), (34, -2), (36, -24, 1), (46, -6), (56, -20, 1), (60, 0), (74, 4), (84, 22), (84, 46), (50, 40)])),
              L(outline([(56, -14), (60, 2), (74, 6), (84, 26), (82, 44), (70, 20)]), 'shade', 'b', False),
              L(outline([(10, 74), (80, 14), (88, 22), (14, 84)]), 'band', 'f', ln=True), L([(12, 80), (84, 18)], 'band2', 'f', False, False, 1.2),
              L(ell(30, 68, 9, 8), 'rim', 'f', ln=True), L(ell(30, 68, 6, 5.4), 'lens', 'f', False), L(ell(44, 58, 8, 7), 'rim', 'f', ln=True), L(ell(44, 58, 5, 4.6), 'lens', 'f', False),
              L(outline([(22, 96), (10, 80, 1), (28, 92)]), WHITE, 'f', ln=True), L(outline([(78, 96), (90, 80, 1), (72, 92)]), WHITE, 'f', ln=True),
              L(quad((24, 96), (50, 100), (76, 96)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (2, 10, 1), (24, 16), (28, -12, 1), (42, 4), (58, -20, 1), (64, 0), (80, 4), (92, 24), (88, 40), (74, 42), (60, 46),
                        (52, 62), (50, 80)])),
             L(outline([(12, 48), (90, 36), (92, 44), (14, 56)]), 'band', 'f', ln=True), L(ell(92, 56, 5, 8), 'rim', 'f', ln=True),
             L(outline([(86, 94), (100, 84), (96, 102)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(16, 84), (12, 30), (20, 6), (16, -16, 1), (34, -2), (40, -24, 1), (50, -6), (60, -18, 1), (64, 2), (80, 8), (88, 30), (84, 84), (50, 90)])),
             L(outline([(56, 2), (80, 10), (88, 40), (84, 80), (64, 88)]), 'shade', 'b', False),
             L(outline([(10, 30), (86, 70), (82, 80), (8, 40)]), 'band', 'f', ln=True)],
}
# Bump Trungus: cabeza calva enorme y rosada con orejas de duende, un mechón rubio en punta arriba y una tirita en la frente;
# ojos grandes medio cerrados de sueño y una sonrisa de dientes
CHARS['bump-trungus'] = {
    'body': 'bajito', 'pal': pal('#f0d890', '#f0a090', skin_d='#d08070', plaster='#f0d090'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': BABY_FACE, 'hairline': False, 'ears': False},
    'front': elf_ears('front') + [L(outline([(6, 60), (4, 30), (20, 8), (50, 0), (80, 8), (96, 30), (94, 60)]), 'skin')] + tuft('front')
             + [L(outline([(42, 28), (58, 28), (58, 34), (42, 34)]), 'plaster', 'f', ln=True)]
             + [L(ell(x, 66, 9, 7), WHITE, 'f', ln=True) for x in (32, 68)] + [L(ell(x, 66, 9, 7) + [ell(x, 66, 9, 7)[0]], OUTC, 'f', False, False, 2.4) for x in (32, 68)]
             + [L([(x - 5, 66), (x + 5, 66)], OUTC, 'f', False, False, 2.0) for x in (32, 68)]
             + [L(quad((24, 54), (32, 52), (40, 56)), OUTC, 'f', False, False, 1.6), L(quad((60, 56), (68, 52), (76, 54)), OUTC, 'f', False, False, 1.6),
                L(ell(50, 80, 2.6, 2.4), 'skin_d', 'f', ln=True), L(outline([(34, 90), (50, 94), (66, 88), (60, 98), (40, 98)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(30, 104), (8, 80), (6, 40), (24, 10), (56, 2), (84, 12), (96, 40), (98, 76), (90, 100), (60, 108)]), 'skin')] + elf_ears('side') + tuft('side')
            + [L(ell(88, 66, 4, 6), WHITE, 'f', ln=True), L([(84, 66), (92, 66)], OUTC, 'f', False, False, 1.8), L(ell(100, 80, 3, 3), 'skin', 'f', ln=True)],
    'back': [L(outline([(6, 80), (4, 30), (20, 8), (50, 0), (80, 8), (96, 30), (94, 80), (70, 100), (30, 100)]), 'skin'),
             L(outline([(54, 10), (90, 30), (92, 80), (66, 96)]), 'skin_d', 'b', False)] + elf_ears('back') + tuft('back'),
}
# Lump Trungus (sin modelo 3D; su retrato): el gemelo de Bump, con una cruz amarilla en la frente, ojos verdes de pillo y una
# sonrisa de dientes
CHARS['lump-trungus'] = dict(CHARS['bump-trungus'], face=dict(CHARS['bump-trungus']['face']))
CHARS['lump-trungus']['pal'] = pal('#f0d890', '#f0a090', skin_d='#d08070', plaster='#f0c840', iris='#3a9a6a')
CHARS['lump-trungus']['front'] = elf_ears('front') + [L(outline([(6, 60), (4, 30), (20, 8), (50, 0), (80, 8), (96, 30), (94, 60)]), 'skin')] + tuft('front') + [
    L(outline([(46, 18), (54, 18), (54, 24), (60, 24), (60, 30), (54, 30), (54, 36), (46, 36), (46, 30), (40, 30), (40, 24), (46, 24)]), 'plaster', 'f', ln=True),
    L(ell(32, 66, 8, 6.4), WHITE, 'f', ln=True), L(ell(68, 66, 8, 6.4), WHITE, 'f', ln=True), L(ell(34, 67, 3.6, 3.6), 'iris', 'f', False), L(ell(66, 67, 3.6, 3.6), 'iris', 'f', False),
    L([(22, 56), (40, 62)], OUTC, 'f', False, False, 2.4), L([(78, 56), (60, 62)], OUTC, 'f', False, False, 2.4),
    L(ell(50, 80, 2.6, 2.4), 'skin_d', 'f', ln=True), L(outline([(30, 88), (50, 94), (70, 88), (62, 100), (38, 100)]), WHITE, 'f', ln=True)]
# Radd Ischer: gordo de cabeza calva enorme y pálida, con una cresta verde de hojas que se abre en abanico por arriba y le
# baja por la nuca; ojos de sueño con arrugas, mejillas marcadas y los labios verdes en morro
CHARS['radd-ischer'] = {
    'body': 'corpulento', 'pal': pal('#3a6a1e', '#fcecd8', skin_d='#e0ccb8', shade='#2a501a', lip='#2a8a7a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 7},
    'front': bald('front') + [L(outline([(36, 34), (24, -6), (6, -22, 1), (24, -18), (34, -26, 1), (44, -16), (54, -30, 1), (60, -16), (72, -26, 1), (78, -14), (96, -20, 1), (78, -2), (64, 34),
                                         (58, 20), (50, 36, 1), (42, 20)]), 'mid', 'f', ln=True),
                              L(outline([(56, -14), (72, -22, 1), (78, -10), (88, -14, 1), (76, 2), (64, 24)]), 'shade', 'f', False)]
             + [L(quad((24, 72), (32, 68), (40, 72)), OUTC, 'f', False, False, 1.8), L(quad((60, 72), (68, 68), (76, 72)), OUTC, 'f', False, False, 1.8),
                L(ell(32, 72, 3, 1.6), OUTC, 'f', False), L(ell(68, 72, 3, 1.6), OUTC, 'f', False),
                L(quad((22, 78), (26, 90), (36, 98)), OUTC, 'f', False, False, 1.0), L(quad((78, 78), (74, 90), (64, 98)), OUTC, 'f', False, False, 1.0),
                L(ell(50, 96, 8, 6), 'lip', 'f', ln=True), L([(44, 96), (56, 96)], OUTC, 'f', False, False, 1.0)],
    'side': bald('side') + [L(outline([(10, 60), (6, 30), (-8, 10, 1), (12, 10), (14, -10, 1), (30, 0), (40, -18, 1), (52, -2), (66, -14, 1), (72, 2), (90, 0, 1), (84, 14), (66, 14),
                                        (44, 20), (26, 40)]), 'mid', 'f', ln=True),
                            L(ell(100, 92, 5, 5), 'lip', 'f', ln=True)] + side_eye(72, lid=1.5),
    'back': bald('back') + [L(outline([(30, 20), (14, -6), (0, -16, 1), (20, -12), (34, -24, 1), (44, -10), (56, -24, 1), (62, -10), (76, -20, 1), (82, -6), (98, -12, 1), (86, 6), (68, 22),
                                        (56, 60), (50, 70, 1), (44, 60)]), 'mid', 'f', ln=True)],
}
# Jynx Jenkins: melena larga lisa en dos colores, gris oscuro arriba y blanca en la mitad de abajo, que le cae hasta el pecho
# y le tapa un ojo; un pasador blanco cuadrado a un lado; el otro ojo amarillo
CHARS['jynx-jenkins'] = {
    'body': 'delgado', 'pal': pal('#4a4a4a', '#9a6438', iris='#d8a020', shade='#363636', white='#ece4ec', white_d='#c8bcc8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 124, 4, top=-6)
             + [L(outline([(2, 64), (98, 64), (100, 124), (86, 124), (82, 64), (18, 64), (14, 124), (0, 124)]), 'white', 'b', False),
                L(outline([(14, 70), (14, 40), (30, 18), (52, 12), (74, 18), (88, 40), (90, 64), (78, 62), (66, 70), (60, 92, 1), (52, 70), (44, 62), (36, 76), (30, 98, 1), (22, 72)]), 'mid', 'f', ln=True),
                L(outline([(30, 64), (44, 64), (36, 98, 1)]), 'white', 'f', False),
                L(outline([(56, 70), (66, 70), (66, 78), (56, 78)]) + [(56, 70)], WHITE, 'f', False, False, 1.6)],
    'side': longhair('side', 124, 4, top=-6) + [L(outline([(2, 64), (56, 64), (54, 112), (40, 116), (14, 122), (2, 116)]), 'white', 'b', False)],
    'back': longhair('back', 124, 4, top=-6, ends=0) + [L(outline([(2, 64), (98, 64), (100, 124), (50, 128), (0, 124)]), 'white', 'b', False),
                                                         L(outline([(56, 64), (98, 64), (100, 124), (60, 126)]), 'white_d', 'b', False)],
}
# Oni Triumvir: piel morena; pelo lila peinado hacia atrás en surcos y recogido en una coleta baja, con dos mechones largos que
# le caen por la cara; ojos de enfado y la boca seria
CHARS['oni-triumvir'] = {
    'body': 'normal', 'pal': pal('#8a8ab0', '#a8703e', shade='#6a6a8e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (50, 40)},
    'front': [L(outline([(14, 70), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (86, 70), (82, 60), (18, 60)])),
              L(outline([(60, 4), (82, 14), (90, 36), (86, 64), (76, 36)]), 'shade', 'b', False)]
             + [strand([(x, 6 + abs(x - 50) * 0.2), (x + (x - 50) * 0.3, 40)], 'shade', 'b', 1.2) for x in (28, 40, 52, 64, 76)]
             + [L(rope((40, 30), (30, 60), (26, 92), 3), 'mid', 'f', ln=True), L(rope((60, 30), (70, 60), (76, 90), 3), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 32), (22, 8), (52, 0), (80, 6), (92, 24), (88, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False),
             L(rope((16, 60), (2, 80), (-2, 100), 9), 'mid', 'f', ln=True), L(rope((80, 20), (92, 50), (88, 80), 3), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 84), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (86, 84), (50, 90)])),
             L(outline([(56, 4), (82, 14), (90, 40), (86, 82), (64, 88)]), 'shade', 'b', False),
             L(rope((50, 60), (40, 90), (30, 110), 9), 'mid', 'f', ln=True)] + [strand([(x, 4), (50, 60)], 'shade', 'b', 1.2) for x in (20, 34, 66, 80)],
}
# Drachen Gunther: melena castaño oscuro enorme y despeinada que le cae hasta los hombros, con dos picos arriba y mechones
# curvados en la frente; cara rosada de mandíbula ancha, ojos azules de furia y los dientes apretados
CHARS['drachen-gunther'] = {
    'body': 'corpulento', 'pal': pal('#3a3424', '#f09888', iris='#2a5ac8', shade='#2a2418'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False},
    'front': longhair('front', 110, 22, top=-8)
             + [L(outline([(14, -2), (20, -24, 1), (34, -6)]), 'mid', 'b', ln=True), L(outline([(66, -6), (80, -24, 1), (86, -2)]), 'mid', 'b', ln=True),
                L(outline([(12, 58), (14, 36), (30, 22), (50, 18), (70, 22), (86, 36), (88, 58), (74, 46), (60, 50), (50, 58, 1), (40, 50), (26, 46)]), 'mid', 'f', ln=True)]
             + [L(ell(x, 74, 6, 5), OUTC, 'f', False) for x in (34, 66)] + [L(ell(x, 74, 3, 3), 'iris', 'f', False) for x in (34, 66)]
             + [L([(22, 64), (42, 70)], OUTC, 'f', False, False, 2.6), L([(78, 64), (58, 70)], OUTC, 'f', False, False, 2.6),
                L(outline([(32, 98), (68, 98), (64, 106), (36, 106)]), WHITE, 'f', ln=True)],
    'side': longhair('side', 110, 22, top=-8) + [L(outline([(60, -4), (74, -24, 1), (80, 0)]), 'mid', 'f', ln=True)] + side_eye(74),
    'back': longhair('back', 110, 22, top=-8, ends=4) + [L(outline([(14, -2), (20, -24, 1), (34, -6)]), 'mid', 'b', ln=True), L(outline([(66, -6), (80, -24, 1), (86, -2)]), 'mid', 'b', ln=True)],
}
# Ichabod Stark: cara larga y huesuda con pinturas azules bajo los ojos y la barbilla; pelo rubio ceniza en pinchos largos
# hacia arriba y a los lados, con una cicatriz en aspa en la frente; ojos amarillos y una sonrisa de dientes
CHARS['ichabod-stark'] = {
    'body': 'delgado', 'pal': pal('#b0a070', '#f4d4a8', iris='#c8a020', shade='#8a7c50', paint='#2a3a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': (48, 40)},
    'front': [L(outline([(16, 66), (14, 40), (-14, 26, 1), (12, 22), (22, 4), (24, -22, 1), (36, -2), (42, -30, 1), (50, -6), (58, -24, 1), (66, 2), (80, 4), (88, 22), (114, 26, 1),
                         (86, 40), (84, 66), (80, 50), (20, 50)])),
              L(outline([(58, -18), (66, 4), (80, 6), (88, 24), (106, 28, 1), (84, 38), (78, 20)]), 'shade', 'b', False),
              L([(44, 52), (52, 60)], OUTC, 'f', False, False, 1.2), L([(52, 52), (44, 60)], OUTC, 'f', False, False, 1.2),
              L([(24, 82), (32, 86)], 'paint', 'f', False, False, 3), L([(76, 82), (68, 86)], 'paint', 'f', False, False, 3),
              L(outline([(20, 106), (40, 112), (40, 120), (20, 114)]), 'paint', 'f', ln=True), L(outline([(80, 106), (60, 112), (60, 120), (80, 114)]), 'paint', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 36), (-8, 22, 1), (14, 22), (14, -2, 1), (32, 6), (40, -24, 1), (50, 0), (62, -14, 1), (66, 6), (82, 10), (92, 26), (88, 40),
                        (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False), L(quad((8, 80), (40, 92), (60, 90)), 'paint', 'f', False, False, 3)],
    'back': [L(outline([(16, 84), (14, 40), (-14, 26, 1), (12, 22), (22, 4), (24, -22, 1), (36, -2), (42, -30, 1), (50, -6), (58, -24, 1), (66, 2), (80, 4), (88, 22), (114, 26, 1),
                        (86, 40), (84, 84), (50, 90)])),
             L(outline([(56, 2), (80, 6), (88, 40), (84, 82), (64, 88)]), 'shade', 'b', False), L(quad((10, 84), (50, 90), (90, 84)), 'paint', 'f', False, False, 3)],
}
# Escavan Malice: pelo azul marino muy oscuro de pinchos grandes despeinados en todas direcciones, con mechones que le caen
# sobre la cara; pinturas negras alrededor de los ojos y una sonrisa de pillo
CHARS['escavan-malice'] = {
    'body': 'normal', 'pal': pal('#1e2a40', '#b08048', shade='#141c2c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 20, 11, seed=1701, rx=56, ry=46, cy=38, lo=88)
             + [L(outline([(10, 80, 1), (14, 44), (28, 26), (50, 20), (72, 26), (86, 44), (90, 80, 1), (80, 58), (72, 66, 1), (64, 50), (56, 60, 1), (50, 48), (44, 66, 1), (36, 50), (28, 64, 1),
                           (20, 56)]), 'mid', 'f'),
                L(outline([(20, 70), (40, 72), (36, 84)]), OUTC, 'f', False), L(outline([(80, 70), (60, 72), (64, 84)]), OUTC, 'f', False)],
    'side': messy('side', 22, 9, seed=1701, rx=52, ry=46, cy=38, nape=100, sweep=-0.4),
    'back': messy('back', 20, 11, seed=1701, rx=56, ry=46, cy=38, nape=100),
}
# Bash Lancer: pelo blanco de pinchos enormes que se abren hacia arriba y a los lados, con mechones que le caen por las
# mejillas; un tatuaje negro en la frente, piel morena y ojos rojos de enfado
CHARS['bash-lancer'] = {
    'body': 'normal', 'pal': pal('#e8e4e4', '#a8703e', iris='#c81e2a', shade='#c0b8b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 18, 10, seed=1702, rx=58, ry=46, cy=40, lo=96)
             + [L(outline([(10, 82, 1), (14, 46), (28, 28), (50, 22), (72, 28), (86, 46), (90, 82, 1), (80, 60), (72, 66, 1), (64, 52), (54, 58), (50, 48), (46, 58), (36, 52), (28, 66, 1),
                           (20, 60)]), 'mid', 'f'),
                L(ell(50, 60, 4, 3) + [ell(50, 60, 4, 3)[0]], OUTC, 'f', False, False, 1.4)],
    'side': messy('side', 24, 9, seed=1702, rx=54, ry=46, cy=40, nape=104, sweep=-0.5),
    'back': messy('back', 22, 10, seed=1702, rx=58, ry=46, cy=40, nape=104),
}
# Mystral Callous: pelo verde azulado oscuro con raya en medio, liso y pegado, que se recoge en dos coletas cortas a los
# lados y una trenza que le cae por detrás; mechones por la cara; ojos violetas y una sonrisa
CHARS['mystral-callous'] = {
    'body': 'normal', 'pal': pal('#1e5a5e', '#fcdcc8', iris='#5a3a6a', shade='#144246', tie='#3a3a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 76), (16, 48), (30, 36), (50, 34), (70, 36), (84, 48), (86, 76)]},
    'front': [L(outline([(-12, 44), (8, 36), (12, 50)]), 'mid', 'b', ln=True), L(outline([(112, 44), (92, 36), (88, 50)]), 'mid', 'b', ln=True)]
             + longhair('front', 104, 6, part=True)
             + [L(rope((16, 50), (12, 80), (20, 108), 7), 'mid', 'f', ln=True), L(rope((84, 50), (88, 80), (80, 108), 7), 'mid', 'f', ln=True),
                L(ell(8, 42, 3, 4), 'tie', 'f', ln=True), L(ell(92, 42, 3, 4), 'tie', 'f', ln=True)],
    'side': longhair('side', 96, 4) + [L(rope((20, 60), (14, 90), (22, 116), 8), 'mid', 'f', ln=True), L(ell(26, 32, 6, 5), 'mid', 'f', ln=True)],
    'back': [L(outline([(-12, 44), (8, 36), (12, 50)]), 'mid', 'b', ln=True), L(outline([(112, 44), (92, 36), (88, 50)]), 'mid', 'b', ln=True)]
            + longhair('back', 96, 4, part=True, ends=0) + [L(rope((50, 70), (54, 96), (50, 120), 9), 'mid', 'f', ln=True)],
}
