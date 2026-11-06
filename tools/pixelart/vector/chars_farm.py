"""Senbayama / Instituto Farm (IE1): los chicos de la granja; sombrero de paja, orejeras, hojas en el pelo y peinados de
campo, con sus modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]


def messy(top_spikes_f, back_extra=()):
    """Pelo de pinchos: los mismos pinchos de arriba de frente y de espaldas."""
    return top_spikes_f


def whiskers(c=OUTC, side=False):
    if side:
        return [L([(80, 84), (86, 85)], c, 'f', False, False, 1.0), L([(80, 88), (86, 88)], c, 'f', False, False, 1.0)]
    return [L([(22, 84), (30, 85)], c, 'f', False, False, 1.0), L([(22, 88), (30, 88)], c, 'f', False, False, 1.0),
            L([(78, 84), (70, 85)], c, 'f', False, False, 1.0), L([(78, 88), (70, 88)], c, 'f', False, False, 1.0)]


# ------------------------------------------------------------------ Albert Green (portero): pelo gris azulado muy despeinado, de
# pinchos largos en todas direcciones y un flequillo de puntas que le cae hasta los ojos; ojos medio cerrados, bigotes de gato
# en las mejillas y la boca abierta refunfuñando
ALB_TOP = [spk((6, 62), (10, 40), (-22, 46), 5), spk((14, 32), (30, 16), (-6, -2), 6), spk((30, 16), (52, 8), (36, -26), 6),
           spk((52, 8), (70, 14), (78, -12), 5, light_left=False), spk((72, 20), (90, 38), (122, 22), 6, light_left=False),
           spk((90, 46), (94, 64), (114, 70), 4, light_left=False), spk((8, 74), (12, 62), (-6, 82), 3)]
CHARS['albert-green'] = {
    'body': 'normal', 'pal': pal('#4a6a7a', '#f6c08e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'eye_y': 77, 'hairline': (62, 54)},
    'front': ALB_TOP + [L(blob([(8, 74), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 74), (80, 66), (20, 66)])),
                        L(blob([(62, 12), (92, 38), (90, 70), (78, 66)], 6), 'shade', 'b', False),
                        spk((10, 46), (28, 40), (16, 78), 5, z='f'), spk((26, 40), (44, 34), (34, 70), 5, z='f'),
                        spk((42, 36), (58, 36), (52, 74), 5, z='f'), spk((56, 36), (74, 40), (66, 70), 5, z='f', light_left=False),
                        spk((72, 40), (90, 46), (86, 78), 5, z='f', light_left=False)] + whiskers(),
    'side': [spk((14, 50), (18, 30), (-22, 26), 6), spk((22, 26), (40, 10), (0, -14), 6), spk((40, 12), (62, 6), (40, -26), 6),
             spk((14, 72), (16, 52), (-16, 62), 5), spk((22, 86), (24, 70), (0, 92), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 10), (82, 20), (84, -10), 5, light_left=False),
             spk((56, 30), (88, 40), (94, 80), 7, z='f', light_left=False), spk((50, 52), (62, 52), (58, 84), 3, z='f')] + whiskers(side=True),
    'back': ALB_TOP + [L(blob([(8, 76), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 76), (66, 88), (34, 88)])),
                       spk((10, 74), (28, 86), (2, 100), 6), spk((28, 88), (50, 92), (36, 110), 6), spk((50, 92), (72, 88), (66, 110), 6, light_left=False),
                       spk((72, 86), (90, 74), (98, 100), 6, light_left=False),
                       L(blob([(58, 12), (92, 38), (90, 74), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Seward Hayseed: piel morena, pelo castaño muy oscuro de
# pinchos alborotados; cejas gruesas de enfado y dientes apretados
SEW_TOP = [spk((6, 62), (10, 42), (-16, 54), 5), spk((12, 38), (26, 18), (-8, 10), 6), spk((26, 18), (46, 8), (30, -20), 6),
           spk((46, 8), (64, 10), (66, -18), 5, light_left=False), spk((64, 12), (82, 26), (104, 4), 6, light_left=False),
           spk((84, 30), (92, 50), (116, 44), 5, light_left=False), spk((90, 52), (94, 66), (110, 72), 3, light_left=False)]
CHARS['seward-hayseed'] = {
    'body': 'normal', 'pal': pal('#3a2418', '#a8683a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': SEW_TOP + [L(blob([(10, 70), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
                        L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
                        spk((12, 46), (30, 40), (16, 70), 5, z='f'), spk((30, 40), (48, 36), (38, 60), 5, z='f'),
                        spk((52, 36), (70, 40), (62, 60), 5, z='f', light_left=False), spk((70, 40), (88, 46), (86, 70), 5, z='f', light_left=False)],
    'side': [spk((14, 50), (18, 30), (-22, 26), 6), spk((22, 26), (40, 10), (0, -14), 6), spk((40, 12), (62, 6), (40, -26), 6),
             spk((14, 72), (16, 52), (-16, 62), 5), spk((22, 86), (24, 70), (0, 92), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 10), (82, 20), (84, -10), 5, light_left=False), spk((56, 30), (88, 40), (92, 66), 6, z='f', light_left=False)],
    'back': SEW_TOP + [L(blob([(10, 72), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
                       spk((12, 72), (30, 84), (8, 96), 5), spk((30, 86), (50, 88), (38, 104), 5), spk((50, 88), (70, 86), (64, 104), 5, light_left=False),
                       spk((70, 84), (88, 72), (92, 96), 5, light_left=False),
                       L(blob([(58, 12), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Kent Work: bajito, media melena castaña con un mechón naranja
# sobre la frente y un moño pequeño en lo alto atado con una goma roja; ojos redondos y un colmillo al sonreír
CHARS['kent-work'] = {
    'body': 'bajito', 'pal': pal('#5a3420', '#fcd2a6', streak='#d0702a', tie='#c03a2a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [L(blob([(42, 10), (40, -4), (50, -14), (62, -8), (58, 4), (56, 10)]), 'mid', 'b', ln=True),
              L(blob([(52, -10), (62, -8), (58, 2)], 4), 'shade', 'b', False), L(ell(50, 8, 7, 4), 'tie', 'b', ln=True),
              L(blob([(8, 84), (4, 48), (14, 18), (50, 8), (86, 18), (96, 48), (92, 84), (82, 80), (82, 60), (18, 60), (18, 80)])),
              L(blob([(62, 14), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False),
              spk((10, 44), (28, 38), (14, 76), 5, z='f'), spk((26, 38), (44, 32), (34, 64), 5, z='f'),
              spk((40, 32), (58, 30), (46, 66), 6, z='f'), spk((56, 32), (72, 38), (66, 64), 5, z='f', light_left=False),
              spk((70, 40), (90, 46), (86, 76), 5, z='f', light_left=False),
              L(blob([(34, 24), (48, 18), (54, 26), (48, 50), (40, 62), (38, 44)], 5), 'streak', 'f', ln=True)],
    'side': [L(blob([(34, 6), (30, -10), (40, -18), (52, -12), (46, 4)]), 'mid', 'b', ln=True), L(ell(38, 6, 5, 4), 'tie', 'b', ln=True),
             L(blob([(48, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 72), 6, z='f', light_left=False),
             L(blob([(70, 22), (86, 26), (90, 50), (82, 40)], 5), 'streak', 'f', ln=True)],
    'back': [L(blob([(42, 12), (40, -4), (50, -14), (62, -8), (58, 4), (56, 12)]), 'mid', 'b', ln=True), L(ell(50, 10, 7, 4), 'tie', 'b', ln=True),
             L(blob([(8, 84), (4, 48), (14, 18), (50, 8), (86, 18), (96, 48), (92, 84), (50, 90)])),
             spk((12, 80), (30, 88), (12, 98), 4), spk((30, 88), (50, 90), (40, 102), 4), spk((50, 90), (70, 88), (60, 102), 4, light_left=False),
             spk((70, 88), (88, 80), (88, 98), 4, light_left=False),
             L(blob([(58, 14), (94, 46), (92, 82), (66, 88)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)],
}

# ------------------------------------------------------------------ Mark Hillvalley: corpulento, piel morena, pelo rizado rojo
# oscuro abultado, marcas en las mejillas, perilla roja y ojos entornados
CHARS['mark-hillvalley'] = {
    'body': 'corpulento', 'pal': pal('#5a1a14', '#a8603a', mark='#c03a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 92, 'eye_y': 76, 'hairline': (56, 48)},
    'front': [L(bumpy(50, 30, 46, 28, 14, 0.08)),
              L(blob([(8, 66), (6, 38), (94, 38), (92, 66), (80, 58), (20, 58)])),
              L(bumpy(68, 34, 22, 18, 8, 0.08), 'shade', 'b', False), L(ell(30, 14, 10, 4), 'light', 'b', False),
              L([(22, 82), (30, 84)], 'mark', 'f', False, False, 1.6), L([(22, 87), (30, 88)], 'mark', 'f', False, False, 1.6),
              L([(78, 82), (70, 84)], 'mark', 'f', False, False, 1.6), L([(78, 87), (70, 88)], 'mark', 'f', False, False, 1.6),
              L(blob([(42, 96), (58, 96), (54, 104), (46, 104)], 4), 'mark', 'f', ln=True)],
    'side': [L(bumpy(42, 32, 44, 28, 14, 0.08)),
             L(blob(SIDE_SKULL)), L(bumpy(24, 46, 18, 22, 8, 0.08), 'shade', 'b', False),
             L([(76, 82), (84, 84)], 'mark', 'f', False, False, 1.6), L(blob([(82, 94), (92, 94), (90, 102), (84, 102)], 4), 'mark', 'f', ln=True)],
    'back': [L(bumpy(50, 34, 46, 30, 14, 0.08)),
             L(blob([(8, 70), (6, 40), (94, 40), (92, 70), (70, 84), (30, 84)])),
             L(bumpy(66, 50, 22, 24, 8, 0.08), 'shade', 'b', False), L(ell(30, 16, 10, 4), 'light', 'b', False),
             L(bumpy(20, 74, 10, 8, 6, 0.1)), L(bumpy(50, 80, 12, 8, 6, 0.1)), L(bumpy(80, 74, 10, 8, 6, 0.1))],
}

# ------------------------------------------------------------------ Herb Sherman: pelo verde grisáceo rizado y abultado solo
# arriba (como un brócoli) con los lados rapados; ojos redondos, tirita en la mejilla y un pendiente
CHARS['herb-sherman'] = {
    'body': 'normal', 'pal': pal('#6a8a74', '#fcc89a', shave='#6a5a4a', aid='#f0e0c0', ring='#2a2a2e'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 93, 'hairline': (52, 46)},
    'front': [L(blob(SKULL_F), 'shave'),
              L(bumpy(50, 26, 46, 22, 12, 0.08)), L(bumpy(66, 30, 22, 14, 8, 0.08), 'shade', 'b', False), L(ell(34, 14, 12, 4), 'light', 'b', False),
              L([(66, 82), (76, 80), (77, 86), (67, 88)], 'aid', 'f', ln=True), L(ell(14, 82, 1.8, 1.8), 'ring', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'shave'),
             L(bumpy(46, 26, 46, 22, 12, 0.08)), L(bumpy(28, 32, 20, 14, 8, 0.08), 'shade', 'b', False),
             L(ell(44, 82, 1.8, 1.8), 'ring', 'f', False)],
    'back': [L(blob(SKULL_B), 'shave'),
             L(bumpy(50, 28, 46, 24, 12, 0.08)), L(bumpy(66, 32, 22, 16, 8, 0.08), 'shade', 'b', False),
             L(ell(14, 82, 1.8, 1.8), 'ring', 'f', False)],
}

# ------------------------------------------------------------------ Joe Small: sombrero de paja de ala ancha con una cinta verde
# azulada; debajo, media melena gris oscura y la cara en sombra con los ojos tapados por el ala
HAT_BRIM_F = blob([(-18, 54), (0, 44), (50, 40), (100, 44), (118, 54), (100, 62), (50, 64), (0, 62)], 6)
CHARS['joe-small'] = {
    'body': 'normal', 'pal': pal('#5a5450', '#f6c08e', straw='#e8b848', straw_d='#c08a2a', ribbon='#2e6a6a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 92), (6, 56), (94, 56), (90, 92), (80, 88), (80, 64), (20, 64), (20, 88)])),
              L(blob([(80, 60), (92, 60), (90, 90), (82, 88)], 5), 'shade', 'b', False),
              L(blob([(20, 60), (80, 60), (80, 74), (50, 72), (20, 74)]), (60, 40, 30, 90), 'f', False),
              L(blob([(22, 50), (20, 26), (32, 10), (50, 6), (68, 10), (80, 26), (78, 50)]), 'straw', 'f', ln=True),
              L(blob([(60, 10), (78, 24), (78, 48), (66, 48)], 6), 'straw_d', 'f', False),
              L(quad((20, 36), (50, 30), (80, 36)) + quad((80, 46), (50, 40), (20, 46)), 'ribbon', 'f', ln=True),
              L(HAT_BRIM_F, 'straw', 'f', ln=True), L(blob([(50, 56), (100, 50), (114, 54), (100, 60), (50, 62)], 5), 'straw_d', 'f', False)]
             + [L(quad((x, 46), (x + (x - 50) * 0.3, 52), (x + (x - 50) * 0.55, 60)), 'straw_d', 'f', False, False, 1.0) for x in (8, 26, 74, 92)],
    'side': [L(blob([(46, 96), (14, 94), (4, 62), (40, 56), (60, 60), (56, 78), (54, 92)])),
             L(blob([(6, 60), (8, 90), (40, 94), (24, 70)], 6), 'shade', 'b', False),
             L(blob([(60, 56), (90, 58), (90, 70), (66, 68)]), (60, 40, 30, 90), 'f', False),
             L(blob([(20, 50), (22, 24), (40, 8), (64, 8), (80, 22), (82, 50)]), 'straw', 'f', ln=True),
             L(quad((20, 36), (50, 30), (82, 36)) + quad((82, 46), (50, 40), (20, 46)), 'ribbon', 'f', ln=True),
             L(blob([(-16, 60), (20, 48), (60, 46), (100, 50), (118, 58), (90, 60), (50, 56), (10, 60)], 6), 'straw', 'f', ln=True)],
    'back': [L(blob([(8, 94), (6, 56), (94, 56), (92, 94), (50, 98)])),
             L(blob([(58, 58), (92, 60), (90, 92), (66, 96)], 6), 'shade', 'b', False),
             L(blob([(22, 50), (20, 26), (32, 10), (50, 6), (68, 10), (80, 26), (78, 50)]), 'straw', 'f', ln=True),
             L(quad((20, 36), (50, 30), (80, 36)) + quad((80, 46), (50, 40), (20, 46)), 'ribbon', 'f', ln=True),
             L(HAT_BRIM_F, 'straw', 'f', ln=True), L(blob([(50, 56), (100, 50), (114, 54), (100, 60), (50, 62)], 5), 'straw_d', 'f', False)],
}

# ------------------------------------------------------------------ Ike Steiner: corte de tazón castaño con flequillo recto hasta
# las cejas; ojos redondos, ceño y un pañuelo crema al cuello
def bowl(c_f=None):
    return blob([(10, 82), (6, 44), (16, 16), (50, 6), (84, 16), (94, 44), (90, 82), (80, 78), (80, 62), (20, 62), (20, 78)])


CHARS['ike-steiner'] = {
    'body': 'normal', 'pal': pal('#6a5048', '#dca068', scarf='#e0c8a8', scarf_d='#b89a7a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': [L(bowl()), L(blob([(62, 12), (92, 44), (90, 80), (82, 78)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3),
              L(blob([(12, 66), (10, 42), (24, 22), (50, 16), (76, 22), (90, 42), (88, 66), (50, 64)]), 'mid', 'f', ln=True),
              L(blob([(60, 22), (86, 40), (86, 64), (70, 64)], 6), 'shade', 'f', False)]
             + [strand([(x, 30 + abs(x - 50) * 0.2), (x, 64)], 'deep', 'f', 1.0) for x in (26, 38, 50, 62, 74)]
             + [L(blob([(20, 100), (36, 96), (50, 104), (64, 96), (80, 100), (70, 112), (50, 114), (30, 112)]), 'scarf', 'f', ln=True),
                L([(36, 104), (44, 120), (52, 108)], 'scarf_d', 'f', ln=True)],
    'side': [L(blob([(46, 90), (14, 88), (4, 60), (8, 28), (28, 8), (58, 4), (82, 14), (94, 36), (94, 64), (78, 64), (62, 64), (56, 76), (52, 86)])),
             L(blob([(6, 50), (8, 84), (40, 88), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(70, 40), (70, 64)], 'deep', 'b', 1.0), strand([(84, 40), (86, 64)], 'deep', 'b', 1.0),
             L(blob([(36, 98), (64, 96), (86, 104), (80, 114), (50, 114), (34, 108)]), 'scarf', 'f', ln=True)],
    'back': [L(blob([(10, 84), (6, 44), (16, 16), (50, 6), (84, 16), (94, 44), (90, 84), (50, 88)])),
             L(blob([(58, 12), (92, 44), (90, 82), (66, 86)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3)]
            + [strand([(x, 50), (x, 84)], 'deep', 'b', 1.0) for x in (24, 37, 50, 63, 76)]
            + [L(blob([(20, 98), (50, 94), (80, 98), (80, 108), (50, 106), (20, 108)]), 'scarf', 'f', ln=True)],
}

# ------------------------------------------------------------------ Orville Newman: pelo rojo intenso de pinchos muy largos hacia
# arriba y los lados, con un mechón que le tapa un ojo; cicatrices en la cara y ojos rojos
ORV_TOP = [spk((6, 60), (10, 40), (-24, 40), 5), spk((14, 32), (30, 16), (-10, -10), 6), spk((30, 16), (50, 8), (40, -30), 6),
           spk((50, 8), (68, 12), (84, -20), 6, light_left=False), spk((70, 18), (88, 34), (120, 18), 6, light_left=False),
           spk((88, 42), (94, 62), (118, 64), 4, light_left=False)]
CHARS['orville-newman'] = {
    'body': 'normal', 'pal': pal('#b02410', '#f0b878', iris='#c03020', scar='#a05030'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': ORV_TOP + [L(blob([(10, 72), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 72), (80, 64), (20, 64)])),
                        L(blob([(62, 12), (90, 38), (88, 68), (78, 64)], 6), 'shade', 'b', False),
                        spk((12, 46), (30, 40), (16, 72), 5, z='f'), spk((28, 40), (46, 36), (36, 62), 5, z='f'),
                        spk((46, 36), (64, 38), (70, 86), 7, z='f', light_left=False), spk((70, 40), (88, 46), (88, 76), 5, z='f', light_left=False),
                        L([(26, 80), (38, 88)], 'scar', 'f', False, False, 1.2), L([(32, 92), (40, 86)], 'scar', 'f', False, False, 1.0)],
    'side': [spk((14, 50), (18, 30), (-22, 26), 6), spk((22, 26), (40, 10), (0, -14), 6), spk((40, 12), (62, 6), (40, -26), 6),
             spk((14, 72), (16, 52), (-16, 62), 5), spk((22, 86), (24, 70), (0, 92), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 10), (82, 20), (88, -12), 5, light_left=False), spk((56, 30), (90, 40), (96, 80), 7, z='f', light_left=False),
             L([(80, 82), (88, 90)], 'scar', 'f', False, False, 1.2)],
    'back': ORV_TOP + [L(blob([(10, 74), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 74), (66, 88), (34, 88)])),
                       spk((12, 72), (30, 86), (6, 98), 5), spk((30, 88), (50, 90), (38, 108), 6), spk((50, 90), (70, 88), (64, 108), 6, light_left=False),
                       spk((70, 86), (88, 72), (94, 98), 5, light_left=False),
                       L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Tom Walters: pelo gris muy corto, orejas grandes, coloretes
# naranjas y cara de enfado
CHARS['tom-walters'] = {
    'body': 'normal', 'pal': pal('#6a6064', '#fcc89a', blush='#e07a3a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'big_ears': 2, 'ear_out': 3, 'hairline': (52, 44)},
    'front': [L(blob([(14, 60), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 60)])),
              L(blob([(62, 14), (88, 34), (86, 58), (74, 54)], 6), 'shade', 'b', False), sheen(28, 52, 18, 3),
              L(ell(26, 86, 5, 4), 'blush', 'f', False), L(ell(74, 86, 5, 4), 'blush', 'f', False)],
    'side': [L(blob([(44, 70), (20, 70), (12, 50), (16, 30), (30, 14), (56, 8), (78, 16), (88, 32), (76, 38), (60, 40), (50, 52)])),
             L(blob([(16, 40), (20, 64), (38, 68), (28, 50)], 6), 'shade', 'b', False), sheen(32, 62, 16, 3),
             L(ell(82, 86, 4, 3.6), 'blush', 'f', False)],
    'back': [L(blob([(14, 70), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 70), (66, 82), (34, 82)]))] + back_hair(),
}

# ------------------------------------------------------------------ Daniel Dawson: pelo castaño de pinchos con hojas verdes
# enganchadas, una tirita en la frente, ojos redondos y una sonrisa enorme
def leaf(cx, cy, ang_dx, ang_dy, r=6):
    return [L(blob([(cx - ang_dx * r, cy - ang_dy * r), (cx + ang_dy * r * 0.5, cy - ang_dx * r * 0.5), (cx + ang_dx * r, cy + ang_dy * r),
                    (cx - ang_dy * r * 0.5, cy + ang_dx * r * 0.5)], 4), 'leaf', 'f', ln=True),
            L([(cx - ang_dx * r * 0.8, cy - ang_dy * r * 0.8), (cx + ang_dx * r * 0.8, cy + ang_dy * r * 0.8)], 'leaf_d', 'f', False, False, 0.9)]


DAN_TOP = [spk((6, 58), (10, 42), (-14, 46), 7), spk((10, 42), (22, 24), (-10, 12), 7), spk((22, 24), (40, 12), (20, -12), 7),
           spk((40, 12), (58, 10), (52, -16), 7), spk((56, 12), (74, 18), (82, -10), 7, light_left=False),
           spk((74, 22), (88, 38), (112, 26), 7, light_left=False), spk((88, 42), (92, 60), (110, 58), 6, light_left=False)]
CHARS['daniel-dawson'] = {
    'body': 'normal', 'pal': pal('#7a4a2a', '#fcd2a6', leaf='#7aa88a', leaf_d='#4a7a5a', aid='#f0a050'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'grin', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': DAN_TOP + [L(blob([(10, 70), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
                        L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
                        spk((12, 46), (30, 40), (18, 70), 5, z='f'), spk((30, 40), (46, 36), (36, 58), 4, z='f'),
                        spk((54, 36), (72, 40), (64, 58), 4, z='f', light_left=False), spk((70, 40), (88, 46), (84, 70), 5, z='f', light_left=False),
                        L([(28, 50), (40, 46), (42, 52), (30, 56)], 'aid', 'f', ln=True)]
             + leaf(48, 4, 0, 1, 7) + leaf(28, 20, 0.7, 0.7, 6) + leaf(72, 24, -0.8, 0.6, 6) + leaf(18, 40, 0.9, 0.4, 5),
    'side': [spk((16, 40), (24, 22), (-18, 16), 7), spk((24, 24), (42, 12), (10, -14), 7), spk((42, 12), (62, 6), (56, -18), 7),
             spk((14, 58), (16, 40), (-16, 52), 6), spk((18, 74), (22, 58), (-8, 80), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 12), (82, 22), (100, 2), 6, light_left=False), spk((56, 30), (88, 40), (92, 66), 6, z='f', light_left=False)]
            + leaf(46, 4, 0, 1, 7) + leaf(72, 18, -0.6, 0.8, 6),
    'back': DAN_TOP + [L(blob([(10, 72), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
                       spk((12, 72), (30, 84), (8, 96), 5), spk((30, 86), (50, 90), (40, 106), 5), spk((50, 90), (70, 86), (62, 106), 5, light_left=False),
                       spk((70, 84), (88, 72), (92, 96), 5, light_left=False),
                       L(blob([(58, 12), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False)] + leaf(48, 4, 0, 1, 7) + leaf(30, 24, 0.7, 0.7, 5),
}

# ------------------------------------------------------------------ Stuart Racoonfur: media melena rosa grisácea con flequillo,
# una coleta baja y unas orejeras blancas con la diadema azul por encima de la cabeza
CHARS['stuart-racoonfur'] = {
    'body': 'normal', 'pal': pal('#a8706a', '#fcd8b4', muff='#e8e0d4', muff_d='#b8ac9c', band='#3a4a6a', blush='#e8907a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'nose': (50, 84, 1.8), 'hairline': (60, 52)},
    'front': [L(blob([(8, 84), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 84), (80, 80), (80, 62), (20, 62), (20, 80)])),
              L(blob([(62, 12), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((12, 44), (30, 38), (18, 66), 5, z='f'), spk((30, 38), (48, 34), (38, 62), 5, z='f'),
              spk((52, 34), (70, 38), (62, 62), 5, z='f', light_left=False), spk((70, 40), (88, 44), (82, 66), 5, z='f', light_left=False),
              L(quad((6, 70), (4, 10), (50, 4)) + quad((50, 4), (96, 10), (94, 70))[1:], 'band', 'f', False, False, 2.4),
              L(ell(6, 72, 9, 12), 'muff', 'f', ln=True), L(ell(94, 72, 9, 12), 'muff', 'f', ln=True),
              L(ell(98, 74, 5, 9), 'muff_d', 'f', False), L(ell(24, 88, 4, 2.6), 'blush', 'f', False), L(ell(76, 88, 4, 2.6), 'blush', 'f', False)],
    'side': [L(blob([(22, 72), (8, 76), (-8, 90), (0, 96), (18, 86), (28, 80)]), 'mid', 'b', ln=True),
             L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 68), 6, z='f', light_left=False),
             L(quad((36, 64), (34, 12), (60, 2)), 'band', 'f', False, False, 2.4),
             L(ell(42, 70, 11, 13), 'muff', 'f', ln=True), L(ell(42, 70, 6, 8), 'muff_d', 'f', False)],
    'back': [L(blob([(8, 84), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 84), (50, 90)])),
             L(blob([(58, 12), (94, 46), (92, 82), (66, 88)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             L(blob([(44, 80), (56, 80), (60, 100), (50, 110), (40, 100)]), 'mid', 'f', ln=True),
             L(quad((6, 70), (4, 10), (50, 4)) + quad((50, 4), (96, 10), (94, 70))[1:], 'band', 'f', False, False, 2.4),
             L(ell(6, 72, 9, 12), 'muff', 'f', ln=True), L(ell(94, 72, 9, 12), 'muff', 'f', ln=True)],
}

# ------------------------------------------------------------------ Lorne Mower: corpulento, pelo gris morado muy corto con un
# pequeño copete; nariz roja, ojos cerrados de felicidad y sonrisa
CHARS['lorne-mower'] = {
    'body': 'corpulento', 'pal': pal('#6a5a74', '#fcc080', nose='#e0603a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'big_ears': 1, 'ear_out': 3, 'nose': (50, 83, 3.4),
             'nose_side': (92, 81, 3.2), 'hairline': (52, 42)},
    'front': [L(blob([(14, 60), (12, 34), (24, 14), (50, 8), (76, 14), (88, 34), (86, 60)])),
              L(blob([(62, 14), (88, 34), (86, 58), (74, 54)], 6), 'shade', 'b', False),
              spk((40, 12), (54, 10), (48, -2), 4), spk((52, 10), (62, 12), (64, 0), 3, light_left=False)],
    'side': [L(blob([(44, 70), (20, 70), (12, 50), (16, 30), (30, 14), (56, 8), (78, 16), (88, 32), (76, 38), (60, 40), (50, 52)])),
             L(blob([(16, 40), (20, 64), (38, 68), (28, 50)], 6), 'shade', 'b', False), spk((56, 8), (70, 12), (74, -2), 4, light_left=False)],
    'back': [L(blob([(14, 68), (12, 34), (24, 14), (50, 8), (76, 14), (88, 34), (86, 68), (66, 80), (34, 80)]))] + back_hair()
            + spk((40, 12), (54, 10), (48, -2), 4),
}

# ------------------------------------------------------------------ Homer Grower: pelo gris claro barrido hacia un lado con un
# pincho que se levanta arriba y un mechón sobre un ojo; nariz grande y sonrisa con dientes
CHARS['homer-grower'] = {
    'body': 'normal', 'pal': pal('#8a8478', '#fcc89a', nose='#e8a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'big_ears': 1, 'nose': (50, 83, 4.4), 'nose_side': (92, 81, 4),
             'hairline': (56, 46)},
    'front': [spk((52, 8), (68, 14), (84, -18), 5, light_left=False), spk((70, 18), (84, 30), (100, 22), 4, light_left=False),
              L(blob([(14, 64), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (86, 64)])),
              L(blob([(62, 12), (88, 34), (86, 62), (74, 58)], 6), 'shade', 'b', False),
              spk((20, 30), (60, 20), (34, 70), 7, z='f'), spk((56, 26), (80, 34), (86, 56), 5, z='f', light_left=False),
              strand([(24, 32), (40, 50)], 'deep', 'f', 1.0)],
    'side': [spk((40, 10), (58, 8), (56, -20), 5, light_left=False), spk((22, 22), (40, 10), (2, 4), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 26), (88, 36), (92, 62), 6, z='f', light_left=False)],
    'back': [spk((32, 14), (48, 8), (16, -18), 5), spk((16, 30), (30, 18), (0, 22), 4),
             L(blob([(14, 70), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (86, 70), (66, 84), (34, 84)]))] + back_hair(),
}

# ------------------------------------------------------------------ Rolf Howells: bajito, casco de pelo verde oliva oscuro en forma
# de seta que le tapa los ojos; solo asoman unos ojos pequeños bajo el flequillo
CHARS['rolf-howells'] = {
    'body': 'bajito', 'pal': pal('#3a3a22', '#f6b878'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'eye_y': 78, 'hairline': False},
    'front': [L(blob([(2, 80), (0, 46), (12, 14), (50, 4), (88, 14), (100, 46), (98, 80), (82, 74), (82, 70), (18, 70), (18, 74)])),
              L(blob([(62, 12), (98, 46), (96, 78), (84, 74)], 6), 'shade', 'b', False), sheen(20, 46, 18, 3),
              L(blob([(4, 76), (2, 46), (14, 18), (50, 10), (86, 18), (98, 46), (96, 76), (74, 72), (50, 74), (26, 72)]), 'mid', 'f', ln=True),
              L(blob([(62, 18), (94, 44), (94, 74), (74, 72)], 6), 'shade', 'f', False)]
             + [strand([(x, 40 + abs(x - 50) * 0.2), (x, 72)], 'deep', 'f', 1.0) for x in (22, 36, 50, 64, 78)],
    'side': [L(blob([(44, 84), (6, 82), (-2, 52), (6, 24), (28, 6), (60, 2), (88, 14), (100, 40), (100, 72), (84, 72), (70, 70), (56, 74), (50, 82)])),
             L(blob([(4, 46), (8, 78), (40, 82), (22, 60)], 6), 'shade', 'b', False), sheen(30, 64, 12, 3),
             strand([(80, 46), (82, 72)], 'deep', 'b', 1.0), strand([(94, 46), (96, 72)], 'deep', 'b', 1.0)],
    'back': [L(blob([(2, 82), (0, 46), (12, 14), (50, 4), (88, 14), (100, 46), (98, 82), (50, 86)])),
             L(blob([(58, 12), (98, 46), (96, 80), (66, 84)], 6), 'shade', 'b', False), sheen(20, 46, 18, 3)],
}

# ------------------------------------------------------------------ Luke Lively: corpulento, cara redonda, pelo naranja peinado a
# un lado en una media melena que le tapa las orejas; ojos pequeños y sonrisa
CHARS['luke-lively'] = {
    'body': 'corpulento', 'pal': pal('#d0601a', '#fcc89a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'hairline': (62, 50)},
    'front': [L(blob([(8, 84), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 84), (82, 80), (82, 60), (18, 60), (18, 80)])),
              L(blob([(62, 12), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              L(blob([(28, 20), (60, 12), (88, 30), (90, 58), (74, 50), (50, 44), (30, 44)]), 'mid', 'f', ln=True),
              L(blob([(64, 18), (88, 32), (88, 56), (72, 48)], 6), 'shade', 'f', False),
              strand([(36, 24), (66, 22), (86, 44)], 'deep', 'f', 1.0)],
    'side': [L(blob([(48, 96), (14, 94), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 74), (56, 92)])),
             L(blob([(6, 50), (8, 90), (40, 94), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(84, 18), (50, 12), (22, 40)], 'deep', 'b', 1.0),
             spk((56, 30), (88, 40), (92, 66), 6, z='f', light_left=False)],
    'back': [L(blob([(8, 86), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 86), (50, 92)])),
             L(blob([(58, 12), (94, 46), (92, 84), (66, 90)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             strand([(36, 10), (30, 84)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Ben Nevis: pelo rosa rojizo en capas con puntas despeinadas
# hacia fuera hasta el cuello; ojos verdes afilados y ceño
CHARS['ben-nevis'] = {
    'body': 'normal', 'pal': pal('#b05a5a', '#f6c08e', iris='#5a8a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(8, 84), (4, 46), (14, 16), (50, 6), (86, 16), (96, 46), (92, 84), (80, 80), (80, 62), (20, 62), (20, 80)])),
              spk((4, 64), (12, 78), (-10, 82), 5), spk((88, 78), (96, 64), (110, 82), 5, light_left=False),
              spk((10, 78), (20, 82), (6, 98), 4), spk((80, 82), (90, 78), (94, 98), 4, light_left=False),
              L(blob([(62, 12), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((12, 44), (30, 38), (18, 72), 5, z='f'), spk((28, 38), (46, 34), (36, 64), 5, z='f'),
              spk((46, 34), (62, 36), (54, 68), 5, z='f', light_left=False), spk((62, 38), (80, 40), (72, 64), 5, z='f', light_left=False),
              spk((76, 42), (90, 46), (86, 74), 4, z='f', light_left=False)],
    'side': [L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             spk((4, 66), (10, 82), (-12, 84), 5), spk((14, 84), (26, 92), (6, 104), 4),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 74), 6, z='f', light_left=False), spk((50, 54), (62, 54), (58, 84), 3, z='f')],
    'back': [L(blob([(8, 86), (4, 46), (14, 16), (50, 6), (86, 16), (96, 46), (92, 86), (50, 92)])),
             spk((4, 64), (12, 78), (-10, 82), 5), spk((88, 78), (96, 64), (110, 82), 5, light_left=False),
             spk((12, 84), (30, 90), (12, 102), 5), spk((30, 90), (50, 92), (40, 108), 5), spk((50, 92), (70, 90), (62, 108), 5, light_left=False),
             spk((70, 90), (88, 84), (88, 102), 5, light_left=False),
             L(blob([(58, 12), (94, 46), (92, 84), (66, 90)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             L([(40, 60), (50, 68), (60, 60)], 'deep', 'b', False, False, 1.2)],
}
