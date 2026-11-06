"""The Great Horn / Caimanes del Cabo (IE3, Sudáfrica): rastas, moños, gorros de tela y crestas, con sus modelos 3D como
referencia (contornos calcados sobre una rejilla de unidades de cabeza); Moeneeb Booysen no tiene modelo: su retrato."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_desertlion import bandana
from chars_empire import afro
from chars_kingdom import cornrows
from chars_littlegigant import dreads
from chars_orpheus import headband
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)

# Zolani Baloi (portero): cara larga morena con bigote rubio verdoso de puntas caídas; el pelo del mismo color pegado y
# recogido atrás en un moño del que salen cuatro rastas gruesas que se abren a los lados como tentáculos
CHARS['zolani-baloi'] = {
    'body': 'corpulento', 'pal': pal('#b8c030', '#b0703a', shade='#909820', tie='#c81e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': [L(rope((24, 40), (0, 30), (-14, 44), 9), 'mid', 'b', ln=True), L(rope((76, 40), (100, 30), (114, 44), 9), 'mid', 'b', ln=True),
              L(blob(SKULL_F), 'skin'),
              L(outline([(14, 70), (12, 28), (26, 6), (50, 0), (74, 6), (88, 28), (86, 70), (78, 50), (64, 36), (50, 34), (36, 36), (22, 50)]), 'mid', 'f', ln=True),
              L(outline([(26, 92), (40, 86), (50, 90), (60, 86), (74, 92), (78, 106, 1), (66, 96), (50, 96), (34, 96), (22, 106, 1)]), 'mid', 'f', ln=True)],
    'side': [L(rope((20, 40), (-6, 30), (-16, 14), 9), 'mid', 'b', ln=True), L(rope((20, 46), (-8, 48), (-16, 60), 9), 'mid', 'b', ln=True),
             L(blob(SIDE_SKULL), 'skin'),
             L(outline([(12, 64), (12, 30), (26, 8), (54, 2), (80, 10), (90, 26), (70, 26), (44, 36), (26, 56)]), 'mid', 'f', ln=True), L(ell(18, 44, 4, 4), 'tie', 'f', ln=True),
             L(outline([(76, 92), (90, 90), (94, 104, 1), (84, 98)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(14, 84), (12, 28), (26, 6), (50, 0), (74, 6), (88, 28), (86, 84), (50, 90)]), 'mid', 'f', ln=True)]
            + [L(rope((50, 44), (50 + d * 0.6, 30 + abs(d) * 0.2), (50 + d, 46 + abs(d) * 0.1), 9), 'mid', 'f', ln=True) for d in (-62, -48, 48, 62)]
            + [L(ell(50, 44, 6, 5), 'tie', 'f', ln=True)],
}
# Dakarai Furman: pelo castaño grisáceo muy corto con entradas; cejas negras gruesas que le tapan los ojos (rojos), la boca
# en morro de labios gruesos y orejas grandes
CHARS['dakarai-furman'] = {
    'body': 'corpulento', 'pal': pal('#6a5a4a', '#a8806a', shade='#4e4236', lip='#e0c0a8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + buzz('front', front_y=36, peak=(50, 32))
             + [L(outline([(18, 68), (36, 66), (46, 72), (54, 72), (64, 66), (82, 68), (80, 80), (64, 80), (50, 76), (36, 80), (20, 80)]), OUTC, 'f', False),
                L(ell(32, 74, 3, 2.4), (200, 160, 170, 255), 'f', False), L(ell(68, 74, 3, 2.4), (200, 160, 170, 255), 'f', False),
                L(ell(32, 74, 1.4, 1.4), (120, 20, 30, 255), 'f', False), L(ell(68, 74, 1.4, 1.4), (120, 20, 30, 255), 'f', False),
                L([(46, 76), (46, 92), (54, 92)], 'skin_d', 'f', False, False, 1.6),
                L(outline([(30, 98), (50, 96), (70, 98), (66, 106), (34, 106)]), 'lip', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L(outline([(76, 68), (92, 70), (92, 80), (78, 80)]), OUTC, 'f', False),
                                            L(outline([(86, 96), (98, 96), (98, 106), (86, 106)]), 'lip', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=78),
}
# Jake Fana: pelo castaño oscuro con franjas amarillas en lo alto y un moño redondo atado arriba, con un pico en la frente;
# ojos blancos de pillo y una sonrisa enorme de dientes
CHARS['jake-fana'] = {
    'body': 'normal', 'pal': pal('#3a2414', '#b0703a', shade='#2a1a0e', stripe='#e8a828'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': bald('front') + buzz('front', front_y=40, peak=(50, 52))
             + [L(quad((36, 6), (36, 26), (32, 44)), 'stripe', 'f', False, False, 3), L(quad((60, 6), (62, 26), (66, 42)), 'stripe', 'f', False, False, 3),
                L(rope((50, 4), (50, -6), (50, -12), 3), 'stripe', 'f', ln=True), L(ell(50, -20, 12, 9), 'mid', 'f', ln=True),
                L(quad((42, -26), (50, -20), (46, -12)), 'stripe', 'f', False, False, 3),
                L(outline([(22, 70), (40, 74), (38, 80), (24, 78)]), WHITE, 'f', ln=True), L(outline([(78, 70), (60, 74), (62, 80), (76, 78)]), WHITE, 'f', ln=True),
                L(ell(34, 76, 1.6, 1.8), OUTC, 'f', False), L(ell(66, 76, 1.6, 1.8), OUTC, 'f', False),
                L(outline([(24, 92), (50, 96), (76, 92), (68, 108), (50, 112), (32, 108)]), WHITE, 'f', ln=True), L(quad((26, 98), (50, 104), (74, 98)), OUTC, 'f', False, False, 1.0)],
    'side': bald('side') + buzz('side') + [L(rope((44, 6), (40, -4), (38, -10), 3), 'stripe', 'f', ln=True), L(ell(38, -18, 11, 8), 'mid', 'f', ln=True), L(quad((50, 4), (60, 30), (80, 30)), 'stripe', 'f', False, False, 3)] + side_eye(76),
    'back': bald('back') + buzz('back', nape=84) + [L(quad((36, 6), (60, 40), (56, 80)), 'stripe', 'f', False, False, 4), L(rope((50, 4), (50, -6), (50, -12), 3), 'stripe', 'f', ln=True), L(ell(50, -20, 12, 9), 'mid', 'f', ln=True)],
}
# Masego Molelo: un gorro de tela a rayas verticales rojas, amarillas y verde oliva, ancho y calado hasta los ojos, con las
# puntas a los lados como orejas; por debajo, una nariz chata y una sonrisa
CHARS['masego-molelo'] = {
    'body': 'normal', 'pal': pal('#2e2218', '#b0703a', hat='#f0c030', red='#c8401e', olive='#7a6a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(0, 80), (-6, 56), (6, 44), (4, 10), (14, -4, 1), (24, 4), (50, 0), (76, 4), (86, -4, 1), (96, 10), (94, 44), (106, 56), (100, 80), (88, 70), (50, 76), (12, 70)]),
                'hat', 'f', ln=True)]
             + [L(outline([(x - 4, 2), (x + 4, 2), (x + 3, 72), (x - 3, 72)]), c, 'f', False) for x, c in ((20, 'red'), (34, 'olive'), (50, 'red'), (66, 'olive'), (80, 'red'))]
             + [L(quad((4, 62), (50, 72), (96, 62)), 'olive', 'f', False, False, 2), L(ell(50, 84, 3.6, 2.6), 'skin_d', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(-6, 84), (-10, 56), (6, 40), (4, 10), (20, -6), (54, -8), (80, 2), (96, 24), (98, 60), (86, 70), (50, 66), (20, 80)]), 'hat', 'f', ln=True),
             L(ell(52, 6, 12, 8), 'olive', 'f', ln=True)]
            + [L(quad((20 + k * 18, -2), (24 + k * 18, 30), (20 + k * 18, 66)), 'red' if k % 2 == 0 else 'olive', 'f', False, False, 4) for k in range(4)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-4, 82), (-8, 56), (4, 40), (6, 10), (16, -4, 1), (26, 4), (50, 0), (74, 4), (84, -4, 1), (94, 10), (96, 40), (108, 56), (104, 82), (50, 84)]), 'hat', 'f', ln=True)]
            + [L(outline([(x - 4, 2), (x + 4, 2), (x + 3, 80), (x - 3, 80)]), c, 'f', False) for x, c in ((20, 'red'), (34, 'olive'), (50, 'red'), (66, 'olive'), (80, 'red'))]
            + [L(outline([(20, 70), (50, 76), (80, 70), (72, 90), (50, 84), (28, 90)]), 'olive', 'f', ln=True)],
}
# Cassius Tobler: calvo moreno con una cresta azul marino de mechones en punta que se abre hacia atrás y a un lado; ojos
# blancos de pillo y una sonrisa
CHARS['cassius-tobler'] = {
    'body': 'bajito', 'pal': pal('#1e4a7a', '#c88a50', shade='#163860'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': bald('front') + [L(outline([(40, 40), (30, 20), (14, -4, 1), (34, 6), (36, -12, 1), (50, 6), (58, -6, 1), (62, 12), (66, 34), (54, 44)]), 'mid', 'f', ln=True),
                              L(outline([(48, 10), (56, 0, 1), (60, 14), (58, 34)]), 'shade', 'f', False)]
             + white_eyes(74, 15, 6, 5, 2.2) + [L([(24, 66), (40, 72)], OUTC, 'f', False, False, 2.2), L([(76, 66), (60, 72)], OUTC, 'f', False, False, 2.2)],
    'side': bald('side') + [L(outline([(30, 24), (10, 6), (0, -8, 1), (20, -4), (24, -18, 1), (40, -4), (56, -14, 1), (60, 4), (70, 14), (44, 22)]), 'mid', 'f', ln=True)] + side_eye(74),
    'back': bald('back') + [L(outline([(40, 46), (30, 26), (14, 2, 1), (34, 10), (36, -8, 1), (50, 8), (60, -6, 1), (62, 14), (64, 40), (52, 50)]), 'mid', 'f', ln=True)],
}
# Anton Nortje: gordo de cara enorme y redonda; pelo azul marino pegado en un casquete y unas rastas cortas y gruesas que le
# salen a los lados de la cabeza como bigotes; un antifaz negro sobre los ojos blancos y una sonrisa enorme
CHARS['anton-nortje'] = {
    'body': 'corpulento', 'pal': pal('#1e2e4a', '#d8a070', shade='#141e34', mouth='#a8703a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': blob([(10, 30), (50, 20), (90, 30), (100, 70), (96, 110), (74, 126), (26, 126), (4, 110), (0, 70)]),
             'hairline': False, 'big_ears': 2, 'ear_out': 9},
    'front': [L(rope((12, 50 + k * 10), (-4, 52 + k * 10), (-16, 54 + k * 10), 7), 'mid', 'b', ln=True) for k in range(4)]
             + [L(rope((88, 50 + k * 10), (104, 52 + k * 10), (116, 54 + k * 10), 7), 'mid', 'b', ln=True) for k in range(4)]
             + [L(outline([(28, 22), (36, 6), (50, 2), (64, 6), (72, 22), (50, 18)]), 'mid', 'f', ln=True),
                L(outline([(16, 64), (34, 56), (50, 62), (66, 56), (84, 64), (80, 80), (66, 84), (50, 78), (34, 84), (20, 80)]), OUTC, 'f', False),
                L(ell(34, 70, 5, 5), WHITE, 'f', False), L(ell(66, 70, 5, 5), WHITE, 'f', False), L(ell(34, 70, 2.4, 2.4), OUTC, 'f', False), L(ell(66, 70, 2.4, 2.4), OUTC, 'f', False),
                L(outline([(42, 66), (58, 66), (60, 86), (40, 86)]), 'skin_d', 'f', ln=True),
                L(outline([(20, 94), (50, 102), (80, 94), (70, 110), (50, 114), (30, 110)]), 'mouth', 'f', ln=True)],
    'side': [L(rope((18, 50 + k * 10), (2, 46 + k * 10), (-12, 40 + k * 12), 7), 'mid', 'b', ln=True) for k in range(4)]
            + [L(outline([(30, 116), (6, 90), (6, 40), (24, 10), (54, 2), (80, 10), (96, 34), (100, 70), (98, 108), (80, 126), (50, 128)]), 'skin'),
               L(outline([(20, 30), (34, 8), (60, 2), (80, 12), (60, 16), (36, 30)]), 'mid', 'f', ln=True),
               L(outline([(76, 62), (94, 62), (94, 80), (78, 80)]), OUTC, 'f', False), L(ell(88, 70, 3, 4), WHITE, 'f', False),
               L(outline([(84, 96), (100, 94), (98, 108), (86, 108)]), 'mouth', 'f', ln=True)],
    'back': [L(outline([(10, 96), (8, 40), (24, 12), (50, 4), (76, 12), (92, 40), (90, 96), (50, 106)]), 'skin'),
             L(outline([(28, 40), (36, 8), (50, 2), (64, 8), (72, 40), (60, 66), (40, 66)]), 'mid', 'f', ln=True)]
            + [L(rope((50, 60), (50 + d, 54), (50 + d * 1.6, 48 + abs(d) * 0.4), 7), 'mid', 'f', ln=True) for d in (-30, -20, -10, 10, 20, 30)],
}
# Adam Marunga: pelo morado con un moño alto en lo alto y otros cuatro moñitos redondos alrededor atados con anillas
# doradas, y el resto suelto en mechones largos hasta los hombros; pinturas rojas en las mejillas y una sonrisa
CHARS['adam-marunga'] = {
    'body': 'normal', 'pal': pal('#6a2a5a', '#b08068', iris='#6a7a2a', shade='#501e44', ring='#d8a020', paint='#c83a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': longhair('front', 104, 10, top=-2)
             + [L(ell(50, -12, 10, 10), 'mid', 'f', ln=True), L(ell(50, -2, 6, 2.4), 'ring', 'f', ln=True)]
             + [L(ell(x, y, 8, 7), 'mid', 'f', ln=True) for x, y in ((14, 14), (86, 14), (4, 40), (96, 40))]
             + [L(ell(x, y + 6, 4, 1.8), 'ring', 'f', ln=True) for x, y in ((14, 14), (86, 14))]
             + [L(ell(38, 62, 4, 2.6), 'shade', 'f', False), L(ell(62, 62, 4, 2.6), 'shade', 'f', False),
                L(outline([(20, 86), (28, 84), (28, 90), (20, 92)]), 'paint', 'f', False), L(outline([(80, 86), (72, 84), (72, 90), (80, 92)]), 'paint', 'f', False)],
    'side': longhair('side', 104, 8, top=-2) + [L(ell(52, -12, 10, 10), 'mid', 'f', ln=True), L(ell(26, 6, 8, 7), 'mid', 'f', ln=True), L(ell(8, 32, 8, 7), 'mid', 'f', ln=True),
                                                L(outline([(74, 86), (82, 84), (82, 92), (74, 92)]), 'paint', 'f', False)],
    'back': longhair('back', 104, 10, top=-2, ends=4) + [L(ell(50, -12, 10, 10), 'mid', 'f', ln=True)] + [L(ell(x, y, 8, 7), 'mid', 'f', ln=True) for x, y in ((14, 14), (86, 14), (4, 40), (96, 40))],
}
# Siyabonga Mahlangu: pelo castaño rojizo muy oscuro corto y rizado en forma de casquete; cara alargada, ojos medio cerrados,
# nariz larga y labios gruesos
CHARS['siyabonga-mahlangu'] = dict({
    'body': 'normal', 'pal': pal('#5a1e14', '#b0703a', shade='#40140e', lip='#7a3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': LONG_FACE, 'nose': (50, 88, 4), 'hairline': (52, 46), 'big_ears': 2, 'ear_out': 5},
}, **afro(1501, rx=50, ry=44, cy=36, amp=3, n=14, lo=60, nape=86))
CHARS['siyabonga-mahlangu']['front'] += [L(outline([(40, 102), (50, 98), (60, 102), (56, 110), (44, 110)]), 'lip', 'f', ln=True)]
# Nathan Tswane: piel morena; rastas rosa blanquecino largas y lisas que le caen por los lados y la espalda, sujetas con
# dos horquillas negras en aspa; ojos verdes y una sonrisa
CHARS['nathan-tswane'] = {
    'body': 'normal', 'pal': pal('#f4e0dc', '#8a6044', iris='#2a9a7a', shade='#d0b0ac', pin='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (54, 44)},
    'front': longhair('front', 100, 16, top=-4, part=True)
             + [strand([(x, 0), (x + (x - 50) * 0.3, 98)], 'shade', 'b', 1.2) for x in (12, 24, 76, 88)]
             + [L(rope((30, 2), (24, 40), (22, 66), 7), 'mid', 'f', ln=True), L(rope((44, 0), (40, 30), (36, 50), 7), 'mid', 'f', ln=True),
                L(rope((58, 0), (62, 30), (64, 50), 7), 'mid', 'f', ln=True), L(rope((72, 2), (78, 40), (80, 66), 7), 'mid', 'f', ln=True)],
    'side': longhair('side', 100, 12, top=-4) + [strand([(x, 0), (x - 10, 98)], 'shade', 'b', 1.2) for x in (20, 36, 52)]
            + [L([(64, 22), (76, 26)], 'pin', 'f', False, False, 1.6)],
    'back': longhair('back', 100, 16, top=-4, ends=6) + [strand([(x, 0), (x + (x - 50) * 0.2, 100)], 'shade', 'b', 1.2) for x in (14, 28, 42, 58, 72, 86)]
            + [L([(38, 26), (62, 36)], 'pin', 'f', False, False, 1.8), L([(38, 36), (62, 26)], 'pin', 'f', False, False, 1.8)],
}
# Melisizwe Zamani: pelo rojo de rizos enorme y abultado hacia arriba; ojos blancos de furia con ojeras negras y una
# sonrisa de dientes rodeada de perilla
CHARS['melisizwe-zamani'] = dict({
    'body': 'bajito', 'pal': pal('#c02a1a', '#c08048', shade='#901e12', light='#e04a30', beard='#7a4a24'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': (60, 54), 'big_ears': 2, 'ear_out': 6},
}, **afro(1502, rx=58, ry=56, cy=30, amp=7, n=10, lo=66, nape=86))
CHARS['melisizwe-zamani']['front'] += [L(outline([(18, 68), (40, 70), (38, 82), (22, 80)]), OUTC, 'f', False), L(outline([(82, 68), (60, 70), (62, 82), (78, 80)]), OUTC, 'f', False),
                                       L(ell(32, 76, 4, 3), WHITE, 'f', False), L(ell(68, 76, 4, 3), WHITE, 'f', False),
                                       L(outline([(28, 92), (50, 88), (72, 92), (70, 106), (50, 112), (30, 106)]), 'beard', 'f', ln=True),
                                       L(outline([(34, 94), (66, 94), (62, 102), (38, 102)]), WHITE, 'f', ln=True)]
CHARS['melisizwe-zamani']['side'] += [L(outline([(76, 68), (92, 70), (92, 82), (78, 80)]), OUTC, 'f', False), L(outline([(80, 92), (94, 90), (94, 106), (82, 106)]), 'beard', 'f', ln=True)]
# Herschel de Villiers: rastas castaño rojizo gruesas peinadas a un lado que le tapan un ojo y se recogen atrás en una cola
# baja que le cae por el hombro; el otro ojo gris de sueño
CHARS['herschel-de-villiers'] = {
    'body': 'normal', 'pal': pal('#7a2a1a', '#a8703e', shade='#5a1e12'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(12, 76), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (90, 76), (80, 66), (20, 66)])),
              L(outline([(60, 4), (86, 16), (92, 40), (88, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(40, 20), (60, 14), (82, 22), (92, 40), (94, 66), (88, 88, 1), (80, 70), (68, 58), (56, 54), (44, 46)]), 'mid', 'f', ln=True)]
             + [strand([(46 + k * 10, 18 + k), (60 + k * 8, 50), (78 + k * 4, 72)], 'shade', 'f', 1.4) for k in range(3)]
             + [strand([(x, 8), (x - 4, 64)], 'shade', 'b', 1.4) for x in (20, 32)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 8), (54, -2), (80, 6), (94, 24), (92, 46), (76, 46), (60, 50), (52, 64), (50, 80)])),
             L(rope((20, 60), (14, 90), (40, 108), 12), 'mid', 'f', ln=True)]
            + [strand([(20 + k * 12, 70 - k * 12), (50, 4 + k * 6), (88, 20 + k * 6)], 'shade', 'f', 1.4) for k in range(4)],
    'back': [L(outline([(12, 84), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, 84), (50, 90)])),
             L(rope((50, 70), (60, 96), (80, 112), 12), 'mid', 'f', ln=True)]
            + [strand([(x, 4), (50, 70)], 'shade', 'f', 1.4) for x in (14, 28, 42, 58, 72, 86)],
}
# Reggie Ines: rastas negras gruesas y largas que le caen por todos los lados y por la frente, con una venda blanca en la
# frente; piel morena, ojos verdes de enfado y perilla
CHARS['reggie-ines'] = {
    'body': 'normal', 'pal': pal('#24262a', '#a8703e', iris='#2a8a5a', shade='#18191c', band='#f0e8e0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': dreads('front', 8, 50, 8, top=2)
             + [L(outline([(12, 62), (14, 28), (28, 8), (50, 2), (72, 8), (86, 28), (88, 62), (50, 54)]))]
             + [L(outline([(14, 60), (16, 48), (50, 44), (84, 48), (86, 60), (50, 56)]), 'band', 'f', ln=True)]
             + [L(rope((50 + d, 20), (50 + d * 1.2, 46), (50 + d * 1.4, 72), 7), 'mid', 'f', ln=True) for d in (-30, -14, 14, 30)]
             + [L(outline([(44, 108), (56, 108), (50, 116, 1)]), 'mid', 'f', ln=True)],
    'side': dreads('side', 7, 40, 8, top=0) + [L(blob(SIDE_SKULL), 'skin'), L(outline([(12, 60), (14, 26), (30, 6), (56, 0), (80, 8), (90, 26), (70, 30), (40, 44)]))]
            + [L(outline([(16, 54), (16, 44), (90, 40), (92, 52)]), 'band', 'f', ln=True), L(rope((70, 20), (82, 40), (88, 64), 7), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 84), (12, 28), (26, 8), (50, 2), (74, 8), (88, 28), (88, 84), (50, 90)]))] + dreads('back', 9, 52, 8, top=2),
}
# Kennedy McCarthy: gordo de cara redonda; un gorro negro con una cinta de triángulos rojos y verdes en la frente, y rastas
# castañas cortas y gruesas que le salen a los lados; ojos cerrados de risa, nariz ancha y una boca naranja sonriente
CHARS['kennedy-mccarthy'] = {
    'body': 'corpulento', 'pal': pal('#5a3a1a', '#b08060', hat='#2a1a14', red='#d8401e', green='#a8c060', lip='#e8803a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 8},
    'front': [L(rope((14, 60 + k * 10), (-2, 62 + k * 10), (-12, 66 + k * 10), 8), 'mid', 'b', ln=True) for k in range(3)]
             + [L(rope((86, 60 + k * 10), (102, 62 + k * 10), (112, 66 + k * 10), 8), 'mid', 'b', ln=True) for k in range(3)]
             + [L(blob(SKULL_F), 'skin'),
                L(outline([(8, 50), (6, 20), (22, 2), (50, -4), (78, 2), (94, 20), (92, 50), (50, 44)]), 'hat', 'f', ln=True),
                L(outline([(10, 54), (12, 36), (50, 30), (88, 36), (90, 54), (50, 50)]), 'red', 'f', ln=True)]
             + [L([(14 + k * 12, 52), (20 + k * 12, 34), (26 + k * 12, 52)], 'green', 'f', False) for k in range(6)]
             + [L(quad((24, 62), (32, 56), (40, 62)), OUTC, 'f', False, False, 2), L(quad((60, 62), (68, 56), (76, 62)), OUTC, 'f', False, False, 2),
                L(outline([(40, 72), (60, 72), (64, 88), (36, 88)]), 'skin_d', 'f', ln=True),
                L(outline([(26, 94), (50, 98), (74, 94), (66, 108), (50, 112), (34, 108)]), 'lip', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin')] + [L(rope((30, 60 + k * 10), (14, 66 + k * 10), (6, 76 + k * 10), 8), 'mid', 'f', ln=True) for k in range(3)]
            + [L(outline([(4, 56), (4, 20), (22, 0), (52, -6), (80, 2), (96, 24), (96, 44), (60, 42), (30, 52)]), 'hat', 'f', ln=True),
               L(outline([(70, 32), (96, 34), (98, 46), (70, 44)]), 'red', 'f', ln=True), L(outline([(84, 92), (98, 92), (98, 104), (86, 104)]), 'lip', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(4, 60), (4, 20), (22, 0), (50, -6), (78, 0), (96, 20), (96, 60), (50, 64)]), 'hat', 'f', ln=True)]
            + [L(rope((50 + d * 0.3, 62), (50 + d * 0.8, 70), (50 + d * 1.1, 84), 8), 'mid', 'f', ln=True) for d in (-60, -40, -20, 20, 40, 60)],
}
# Moeneeb Booysen (sin modelo 3D; su retrato): pelo castaño oscuro corto y rizado en casquete; ojos negros de enfado, una
# nariz redonda naranja y la boca seria
CHARS['moeneeb-booysen'] = dict({
    'body': 'normal', 'pal': pal('#4a3a1e', '#a8703e', shade='#342812', nose='#c8641e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 86, 4.4), 'hairline': (52, 46), 'big_ears': 3, 'ear_out': 7},
}, **afro(1503, rx=50, ry=42, cy=34, amp=3, n=14, lo=56, nape=84))
# Hugh Makebe (portero suplente): un pañuelo morado y amarillo a rayas en diagonal anudado en la cabeza, con una punta larga
# que le cae por un lado; ojos negros grandes y labios gruesos
CHARS['hugh-makebe'] = {
    'body': 'normal', 'pal': pal('#2e2218', '#8a5a34', cloth='#5a3a6a', cloth_d='#f0b030', lip='#5a3420'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin')] + bandana('front', 'cloth', 'cloth', low=60, tails=False)
             + [L(quad((10, 56), (40, 20), (70, 6)), 'cloth_d', 'f', False, False, 5), L(quad((40, 60), (70, 30), (90, 30)), 'cloth_d', 'f', False, False, 5),
                L(outline([(88, 40), (100, 60), (98, 100, 1), (88, 80), (84, 56)]), 'cloth_d', 'f', ln=True),
                L(outline([(40, 98), (50, 94), (60, 98), (56, 106), (44, 106)]), 'lip', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin')] + bandana('side', 'cloth', 'cloth', low=56, tails=False)
            + [L(quad((10, 50), (40, 20), (80, 6)), 'cloth_d', 'f', False, False, 5),
               L(outline([(16, 40), (2, 70), (6, 104, 1), (16, 74), (22, 50)]), 'cloth_d', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin')] + bandana('back', 'cloth', 'cloth', low=60, tails=False)
            + [L(quad((10, 30), (50, 40), (90, 20)), 'cloth_d', 'f', False, False, 5),
               L(outline([(14, 44), (0, 70), (4, 104, 1), (14, 76), (24, 52)]), 'cloth', 'f', ln=True), L(ell(14, 46, 6, 6), 'cloth', 'f', ln=True)],
}
# Themba Sepeng: trenzas pegadas verde intenso que le cubren la cabeza en surcos curvos; cejas verdes gruesas, ojos de pasmo
# y una sonrisa
CHARS['themba-sepeng'] = {
    'body': 'normal', 'pal': pal('#2e8a1e', '#a8805a', shade='#1e6a14'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': cornrows('front', 5) + white_eyes(76, 15, 5.4, 5.4, 2.4)
             + [L(outline([(22, 64), (38, 60), (42, 66), (26, 68)]), 'mid', 'f', ln=True), L(outline([(78, 64), (62, 60), (58, 66), (74, 68)]), 'mid', 'f', ln=True)],
    'side': cornrows('side') + side_eye(76),
    'back': cornrows('back', 6),
}
