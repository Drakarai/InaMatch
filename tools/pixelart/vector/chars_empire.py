"""The Empire / Los Emperadores (IE3, Argentina): melenas, afros y rizos, con sus modelos 3D como referencia (contornos
calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_orpheus import headband
from heads import quad

WHITE = (250, 250, 250, 255)


def afro(seed, rx=62, ry=54, cy=36, amp=4, n=16, lo=74, nape=96):
    return {v: messy(v, amp if v != 'side' else amp + 0.5, n if v != 'side' else n - 2, seed=seed, rx=rx if v != 'side' else rx - 4, ry=ry, cy=cy, lo=lo, nape=nape)
            for v in ('front', 'side', 'back')}


# Jorge Ortega (portero): cara ancha morena; melena verde azulado ondulada que se abre a los lados hasta la mandíbula, con
# una cinta marrón en la frente; ojos rojizos de enfado, nariz ancha y la boca torcida
CHARS['jorge-ortega'] = {
    'body': 'corpulento', 'pal': pal('#1e6a7a', '#c8963e', iris='#a83a2a', shade='#164e5a', band='#5a3a24'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'nose': (50, 86, 3.4), 'hairline': (46, 40)},
    'front': longhair('front', 96, 16, top=-2) + headband('front', 36),
    'side': longhair('side', 96, 14, top=-2) + headband('side', 34),
    'back': longhair('back', 96, 16, top=-2, ends=5) + headband('back', 36),
}
# Thiago Torres: piel morena; melena verde muy oscuro con raya en medio, lisa arriba y rizada en las puntas, hasta los
# hombros; ojos rojos de enfado, perilla y la boca seria
CHARS['thiago-torres'] = {
    'body': 'normal', 'pal': pal('#1e3a2a', '#b07a40', iris='#a81e2a', shade='#14281e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'hairline': [(14, 68), (16, 46), (32, 36), (50, 34), (68, 36), (84, 46), (86, 68)]},
    'front': longhair('front', 112, 18, part=True) + [L(outline([(46, 104), (54, 104), (50, 110, 1)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 112, 16),
    'back': longhair('back', 112, 18, part=True, ends=5),
}
# Julio Acosta: gordo; una mata de pelo naranja enorme y abultada en rizos gruesos que se abre a los lados; cejas en
# punta, ojos de pasmo, nariz larga marrón y la boca torcida
CHARS['julio-acosta'] = dict({
    'body': 'corpulento', 'pal': pal('#e0762a', '#f0c890', shade='#b0561a', light='#f8a050', nose='#a86a30'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': (56, 46), 'big_ears': 2, 'ear_out': 8},
}, **{k: v for k, v in afro(1001, rx=66, ry=50, cy=34, amp=6, n=10, lo=70).items()})
CHARS['julio-acosta']['front'] += white_eyes(76, 15, 5, 5, 1.8) + [L([(22, 62), (42, 70)], 'mid', 'f', False, False, 3), L([(78, 62), (58, 70)], 'mid', 'f', False, False, 3),
                                                                    L(outline([(46, 70), (54, 70), (60, 92), (40, 92)]), 'nose', 'f', ln=True)]
CHARS['julio-acosta']['side'] += side_eye(76) + [L(outline([(86, 70), (102, 90), (88, 92)]), 'nose', 'f', ln=True)]
# Grande Díaz: cara alargada de mentón enorme; melena castaña lisa con raya en medio hasta los hombros, recogida en dos
# mechones gruesos; ojos cerrados con dos arrugas en el entrecejo, nariz larga y una sonrisa
CHARS['grande-d-az'] = {
    'body': 'normal', 'pal': pal('#5a2a1a', '#f8c8a0', shade='#401e12', nose='#c08a50'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': [(16, 80), (18, 50), (32, 36), (50, 30), (68, 36), (82, 50), (84, 80)]},
    'front': longhair('front', 108, 8, part=True)
             + [L(rope((16, 90), (8, 104), (14, 116), 9), 'mid', 'f', ln=True), L(rope((84, 90), (92, 104), (86, 116), 9), 'mid', 'f', ln=True),
                L([(26, 74), (42, 74)], OUTC, 'f', False, False, 2.2), L([(58, 74), (74, 74)], OUTC, 'f', False, False, 2.2),
                L([(46, 66), (46, 80)], OUTC, 'f', False, False, 1.4), L([(54, 66), (54, 80)], OUTC, 'f', False, False, 1.4),
                L(outline([(46, 76), (54, 76), (58, 96), (42, 96)]), 'nose', 'f', ln=True), L(quad((30, 100), (50, 110), (70, 100)), OUTC, 'f', False, False, 1.6)],
    'side': longhair('side', 108, 6) + [L(rope((40, 96), (36, 110), (44, 118), 9), 'mid', 'f', ln=True), L(outline([(86, 74), (104, 94), (88, 96)]), 'nose', 'f', ln=True)],
    'back': longhair('back', 108, 8, part=True, ends=2) + [L(rope((20, 96), (14, 108), (22, 118), 10), 'mid', 'f', ln=True), L(rope((80, 96), (86, 108), (78, 118), 10), 'mid', 'f', ln=True)],
}
# Ramón Martínez: pelo gris verdoso liso en casco con flequillo de mechones y las puntas abiertas en las patillas y la nuca;
# cara alargada, perilla, ojos de sueño y media sonrisa
CHARS['ram-n-mart-nez'] = {
    'body': 'normal', 'pal': pal('#6a6a5a', '#fcd8b8', shade='#4e4e40'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': longhair('front', 90, 22, fringe=64) + [L(outline([(46, 108), (54, 108), (50, 116, 1)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 90, 22),
    'back': longhair('back', 90, 22, ends=4),
}
# Esteban Carlos: melena castaña ondulada hasta los hombros, con un flequillo largo que le cae tapándole un ojo; un ojo azul
# de sueño y la boca seria
CHARS['esteban-carlos'] = {
    'body': 'normal', 'pal': pal('#8a4a26', '#fcdcc0', iris='#3a6a9a', shade='#6a3418'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 104, 16)
             + [L(outline([(12, 66), (14, 40), (30, 22), (52, 16), (74, 22), (88, 40), (88, 60), (76, 50), (64, 50), (58, 64), (52, 80), (44, 94, 1), (40, 70), (28, 66), (18, 74)]), 'mid', 'f', ln=True),
                L(rope((16, 76), (8, 92), (16, 106), 10), 'mid', 'f', ln=True), L(rope((84, 76), (92, 92), (84, 106), 10), 'mid', 'f', ln=True)],
    'side': longhair('side', 100, 12) + [spk((60, 30), (90, 40), (92, 72), 5, z='f', light_left=False)],
    'back': longhair('back', 100, 12, ends=3),
}
# Sergio Pérez: pelo castaño corto despeinado de puntas; ojos castaños grandes y una sonrisa
CHARS['sergio-p-rez'] = {
    'body': 'normal', 'pal': pal('#6a3a2a', '#fcdcc0', iris='#a87020', shade='#4e2a1e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 10, 11, seed=1002, rx=48, ry=40, lo=66)
             + [L(outline([(12, 66, 1), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 66, 1), (80, 54), (72, 60, 1), (64, 50), (56, 58, 1), (50, 50), (42, 58, 1),
                           (36, 50), (28, 60, 1), (20, 54)]), 'mid', 'f')],
    'side': messy('side', 11, 9, seed=1002, rx=46, ry=40, nape=92, sweep=-0.2),
    'back': messy('back', 10, 11, seed=1002, rx=48, ry=40, nape=94),
}
# Roberto Torres: cara alargada; melena azul marino lisa con raya en medio que cae recta y se abre en campana a la altura
# de los hombros; cejas gruesas, ojos de pasmo y una sonrisa
CHARS['roberto-torres'] = {
    'body': 'normal', 'pal': pal('#1e3a6a', '#e89a68', shade='#142a50'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': [(16, 80), (18, 50), (30, 34), (50, 28), (70, 34), (82, 50), (84, 80)]},
    'front': longhair('front', 108, 24, part=True) + white_eyes(76, 14, 5.4, 5.4, 2.2)
             + [L(outline([(22, 66), (32, 60), (42, 66), (32, 68)]), 'mid', 'f', ln=True), L(outline([(78, 66), (68, 60), (58, 66), (68, 68)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 104, 22) + side_eye(76),
    'back': longhair('back', 108, 24, part=True, ends=5),
}
# Pablo Castillo: melena verde agua lisa y larga con raya en medio que le cae por los lados hasta el pecho y una cinta negra
# en la frente; cejas verdes, ojos de pasmo y la boca seria
CHARS['pablo-castillo'] = {
    'body': 'normal', 'pal': pal('#7ab0a0', '#c8964e', shade='#5a8a7a', band='#1e1e1e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(16, 72), (18, 46), (32, 36), (50, 30), (68, 36), (82, 46), (84, 72)]},
    'front': longhair('front', 120, 6, part=True) + headband('front', 30, 'band'),
    'side': longhair('side', 116, 8) + headband('side', 28, 'band'),
    'back': longhair('back', 120, 6, part=True, ends=3) + headband('back', 30, 'band'),
}
# Leone Badigo: pelo rubio claro muy abultado de mechones en punta que se abren a los lados como una melena de león; ojos
# azules y una sonrisa de dientes
CHARS['leone-badigo'] = {
    'body': 'normal', 'pal': pal('#f4dc90', '#f8c890', iris='#2a5aa8', shade='#d0b060', light=WHITE),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 12, 10, seed=1003, rx=56, ry=44, cy=42, lo=84)
             + [L(outline([(10, 74, 1), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (90, 74, 1), (80, 56), (70, 48), (54, 44), (50, 56, 1), (46, 44), (30, 48), (20, 56)]), 'mid', 'f'),
                L(outline([(30, 28), (50, 22), (44, 34)]), 'light', 'f', False)],
    'side': messy('side', 14, 8, seed=1003, rx=52, ry=44, cy=42, nape=96, sweep=-0.6),
    'back': messy('back', 12, 10, seed=1003, rx=56, ry=44, cy=42, nape=100),
}
# Diego Oro: afro verde muy oscuro, enorme y redondo, que le cae hasta las cejas; cejas gruesas, ojos cerrados y la boca seria
CHARS['diego-oro'] = dict({
    'body': 'normal', 'pal': pal('#1e3a2a', '#c8945a', shade='#142a1e', light='#2e5a40'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': (60, 58)},
}, **afro(1004, rx=64, ry=58, cy=36, amp=5, n=14, lo=72, nape=100))
CHARS['diego-oro']['front'] += [L(outline([(24, 64), (40, 60), (44, 66), (28, 68)]), 'mid', 'f', ln=True), L(outline([(76, 64), (60, 60), (56, 66), (72, 68)]), 'mid', 'f', ln=True)]
# Lionel Cruz (portero suplente): afro azul marino enorme y redondo con una cresta verde de rizos en medio de la frente;
# cara alargada, ojos medio cerrados de enfado y la boca torcida
CHARS['lionel-cruz'] = dict({
    'body': 'normal', 'pal': pal('#24447a', '#c88a4a', shade='#1a325e', light='#3a5a96', crest='#2e9a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': (66, 64)},
}, **afro(1005, rx=62, ry=56, cy=36, amp=5, n=14, lo=70, nape=100))
CHARS['lionel-cruz']['front'] += [L(outline([(34, 64), (30, 40), (36, 26), (50, 20), (64, 26), (70, 40), (66, 64), (50, 56)]), 'crest', 'f', ln=True),
                                  L(outline([(36, 76), (50, 60), (64, 76), (50, 70)]), 'mid', 'f', False)]
CHARS['lionel-cruz']['side'] += [L(outline([(84, 30), (96, 40), (94, 60), (84, 56)]), 'crest', 'f', ln=True)]
# Mario Saviola: cara alargada; pelo naranja de rizos abultados que le enmarca la cara hasta la mandíbula, con mechones que
# caen en la frente; ojos pequeños y una sonrisa
CHARS['mario-saviola'] = dict({
    'body': 'normal', 'pal': pal('#f08a1e', '#fcd0a0', shade='#c06a14', light='#ffb050'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': (64, 48)},
}, **afro(1006, rx=64, ry=56, cy=46, amp=5, n=14, lo=96, nape=102))
# Hernán Tévez: pelo castaño rojizo con una cinta marrón gruesa en la frente, mechones finos que le cruzan la cara y dos
# coletas bajas atadas a los lados; ojos verdes de enfado y la boca torcida
CHARS['hern-n-t-vez'] = {
    'body': 'normal', 'pal': pal('#b04a1e', '#fcdcc0', iris='#7a8a2a', shade='#8a3614', band='#5a3018'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (88, 70), (80, 62), (20, 62)])),
              L(outline([(60, 6), (84, 18), (92, 44), (86, 66), (78, 40)]), 'shade', 'b', False), strand([(50, 4), (50, 36)], 'deep', 'b', 1.2),
              L(outline([(10, 42), (50, 36), (90, 42), (90, 56), (50, 50), (10, 56)]), 'band', 'f', ln=True),
              L(rope((14, 80), (0, 92), (6, 108), 10), 'mid', 'f', ln=True), L(rope((86, 80), (100, 92), (94, 108), 10), 'mid', 'f', ln=True),
              L([(28, 56), (30, 74), (26, 90)], 'mid', 'f', False, False, 1.6), L([(70, 56), (68, 74), (72, 88)], 'mid', 'f', False, False, 1.6)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 34), (24, 10), (52, 2), (78, 8), (92, 26), (90, 42), (76, 44), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False),
             L(outline([(8, 40), (90, 36), (92, 50), (10, 54)]), 'band', 'f', ln=True), L(rope((20, 74), (10, 90), (16, 106), 10), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 84), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (88, 84), (50, 90)])),
             L(outline([(56, 6), (84, 18), (92, 48), (88, 82), (64, 88)]), 'shade', 'b', False),
             L(outline([(8, 44), (50, 38), (92, 44), (92, 58), (50, 52), (8, 58)]), 'band', 'f', ln=True),
             L(rope((26, 78), (10, 92), (14, 110), 10), 'mid', 'f', ln=True), L(rope((74, 78), (90, 92), (86, 110), 10), 'mid', 'f', ln=True)],
}
# Herman Samuel: pelo verde musgo en dos matas abultadas a los lados y una franja dorada en medio, sujetos con una cinta a
# cuadros; patillas rizadas hasta las mejillas; ojos grandes y la boca seria
CHARS['herman-samuel'] = {
    'body': 'normal', 'pal': pal('#4a6a24', '#b07a48', shade='#36501a', gold='#d8a020', band='#a88a8a', band_d='#6a4a4a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin')]
             + [L(outline([(10, 70), (-4, 54), (-6, 30), (8, 12), (30, 8), (36, 40), (30, 62)]), 'mid', 'f', ln=True),
                L(outline([(90, 70), (104, 54), (106, 30), (92, 12), (70, 8), (64, 40), (70, 62)]), 'mid', 'f', ln=True),
                L(outline([(32, 50), (30, 10), (40, -6), (60, -6), (70, 10), (68, 50)]), 'gold', 'f', ln=True),
                L(outline([(14, 54), (50, 50), (86, 54), (86, 62), (50, 58), (14, 62)]), 'band', 'f', ln=True)]
             + [L([(x, 52), (x, 61)], 'band_d', 'f', False, False, 1.4) for x in (24, 36, 50, 64, 76)]
             + [L(outline([(14, 64), (24, 66), (26, 90), (16, 96, 1)]), 'mid', 'f', ln=True), L(outline([(86, 64), (76, 66), (74, 90), (84, 96, 1)]), 'mid', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(10, 70), (4, 30), (20, 6), (54, -4), (84, 4), (96, 22), (92, 46), (60, 50), (30, 60)]), 'mid', 'f', ln=True),
             L(outline([(20, 10), (54, -6), (86, 4), (96, 20), (60, 14), (30, 20)]), 'gold', 'f', ln=True),
             L(outline([(16, 52), (90, 46), (92, 54), (18, 60)]), 'band', 'f', ln=True),
             L(outline([(62, 60), (72, 62), (76, 90), (66, 94, 1)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(10, 80), (-4, 54), (-6, 30), (8, 12), (30, 8), (36, 60)]), 'mid', 'f', ln=True),
             L(outline([(90, 80), (104, 54), (106, 30), (92, 12), (70, 8), (64, 60)]), 'mid', 'f', ln=True),
             L(outline([(32, 60), (30, 10), (40, -6), (60, -6), (70, 10), (68, 60)]), 'gold', 'f', ln=True),
             L(outline([(14, 54), (50, 50), (86, 54), (86, 62), (50, 58), (14, 62)]), 'band', 'f', ln=True),
             L(outline([(20, 64), (80, 64), (76, 86), (50, 90), (24, 86)]), 'mid', 'f', ln=True)],
}
# Ricardo Agüero: pelo granate liso y abultado, peinado a un lado con mechones que le caen por la frente y patillas largas;
# cara alargada, ojos de sueño y la boca torcida
CHARS['ricardo-ag-ero'] = {
    'body': 'normal', 'pal': pal('#7a1e2a', '#d8a060', shade='#5a141e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': longhair('front', 92, 6)
             + [L(outline([(12, 66), (14, 40), (28, 22), (52, 16), (74, 22), (88, 40), (88, 62), (76, 50), (62, 46), (50, 54), (40, 70), (34, 80, 1), (30, 62), (20, 60)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 92, 4),
    'back': longhair('back', 92, 4, ends=3),
}
