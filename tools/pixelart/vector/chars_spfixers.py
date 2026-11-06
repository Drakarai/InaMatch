"""SP Fixers / Servicio Secreto (IE2): escoltas de traje negro con auricular y micro, cascos con gafas, sombreros y gafas
de sol, con sus modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from heads import quad

DARK = (24, 22, 28, 255)
WHITE = (250, 250, 250, 255)
SHADE_LENS = (40, 40, 48, 255)


def headset(view, mouth_y=92):
    """Auricular negro en la oreja izquierda (derecha de la imagen) con el micro que baja hasta la boca."""
    if view == 'front':
        return [L(outline([(80, 64), (88, 62), (90, 76), (82, 78)]), DARK, 'f', ln=True),
                L(quad((84, 78), (80, mouth_y + 2), (66, mouth_y + 2)), DARK, 'f', False, False, 1.4), L(ell(64, mouth_y + 2, 2.6, 2.2), DARK, 'f', False)]
    if view == 'side':
        return [L(ell(46, 70, 5, 6), DARK, 'f', ln=True), L(quad((48, 76), (62, mouth_y + 4), (80, mouth_y)), DARK, 'f', False, False, 1.4),
                L(ell(81, mouth_y, 2.4, 2), DARK, 'f', False)]
    return [L(outline([(80, 64), (88, 62), (90, 76), (82, 78)]), DARK, 'f', ln=True)]


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


def helmet(view, low=60):
    """Casco azul grisáceo de agujeros con la correa negra alrededor."""
    if view == 'front':
        return [L(outline([(8, low + 8), (6, 36), (18, 10), (50, -2), (82, 10), (94, 36), (92, low + 8), (82, low), (18, low)]), 'helm', 'f', ln=True),
                L(outline([(58, 2), (82, 12), (92, 40), (90, low + 4), (80, low - 2), (74, 24)]), 'helm_d', 'f', False),
                L(ell(30, 18, 2.4, 2.2), DARK, 'f', False), L(ell(50, 10, 2.4, 2.2), DARK, 'f', False), L(ell(70, 18, 2.4, 2.2), DARK, 'f', False),
                L(ell(16, 38, 2, 2.4), DARK, 'f', False), L(ell(84, 38, 2, 2.4), DARK, 'f', False)]
    if view == 'side':
        return [L(outline([(4, 60), (6, 30), (24, 6), (54, -2), (80, 6), (94, 26), (98, 44), (104, 52, 1), (86, 54), (60, 56), (30, 62)]), 'helm', 'f', ln=True),
                L(quad((8, 46), (50, 40), (96, 46)), DARK, 'f', False, False, 3.0),
                L(ell(52, 14, 2.4, 2.2), DARK, 'f', False), L(ell(66, 20, 2, 2), DARK, 'f', False)]
    return [L(outline([(6, 66), (6, 32), (20, 8), (50, -2), (80, 8), (94, 32), (94, 66), (50, 60)]), 'helm', 'f', ln=True),
            L(outline([(58, 2), (82, 10), (94, 36), (94, 62), (72, 60)]), 'helm_d', 'f', False),
            L(quad((6, 46), (50, 40), (94, 46)), DARK, 'f', False, False, 3.0)]


def goggles_up(view, y=46):
    """Gafas de esquí blancas subidas sobre el casco, de montura verde oliva."""
    if view == 'front':
        return [L(outline([(16, y - 8), (50, y - 12), (84, y - 8), (86, y + 8), (60, y + 10), (50, y + 4), (40, y + 10), (14, y + 8)]), 'frame', 'f', ln=True),
                L(outline([(20, y - 5), (48, y - 8), (48, y + 3), (40, y + 7), (20, y + 5)]), 'lens', 'f', False),
                L(outline([(80, y - 5), (52, y - 8), (52, y + 3), (60, y + 7), (80, y + 5)]), 'lens', 'f', False),
                L(outline([(24, y - 3), (40, y - 5), (26, y + 1)]), WHITE, 'f', False)]
    if view == 'side':
        return [L(outline([(80, y - 10), (96, y - 10), (100, y + 6), (84, y + 8)]), 'frame', 'f', ln=True), L(outline([(88, y - 7), (97, y - 7), (98, y + 4), (89, y + 5)]), 'lens', 'f', False)]
    return []


def sunglasses(view, y=74, kind='wrap'):
    if view == 'front':
        if kind == 'round':
            return [L(ell(34, y, 8.5, 7.5), SHADE_LENS, 'f', ln=True), L(ell(66, y, 8.5, 7.5), SHADE_LENS, 'f', ln=True),
                    L([(42, y - 2), (58, y - 2)], SHADE_LENS, 'f', False, False, 1.4)]
        if kind == 'band':  # una banda negra de lado a lado
            return [L(outline([(10, y - 7), (50, y - 4), (90, y - 7), (90, y + 5), (60, y + 7), (50, y + 3), (40, y + 7), (10, y + 5)]), SHADE_LENS, 'f', ln=True)]
        return [L(outline([(14, y - 6), (50, y - 6), (86, y - 6), (84, y + 4), (62, y + 7), (50, y + 2), (38, y + 7), (16, y + 4)]), SHADE_LENS, 'f', ln=True),
                L(outline([(22, y - 4), (36, y - 4), (24, y)]), (110, 110, 124, 255), 'f', False)]
    if view == 'side':
        return [L(outline([(76, y - 6), (94, y - 5), (94, y + 5), (78, y + 5)]), SHADE_LENS, 'f', ln=True), L([(50, y - 2), (76, y - 2)], SHADE_LENS, 'f', False, False, 1.4)]
    return [L(quad((8, y - 2), (50, y - 6), (92, y - 2)), SHADE_LENS, 'f', False, False, 1.6)]


HELM = dict(helm='#5a6290', helm_d='#454c74', frame='#4a5236', lens='#e8eef0', mask='#2a3040', mask_d='#1e2430')

# Ken Ironwall (portero): casco azul grisáceo con las gafas de esquí blancas subidas y un pasamontañas azul marino que le
# tapa la cara hasta los ojos; ojos entornados de aburrimiento
CHARS['ken-ironwall'] = {
    'body': 'corpulento', 'pal': pal('#2a3040', '#f0a050', **HELM),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'eye_y': 74, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 72), (6, 40), (94, 40), (94, 72), (96, 100), (84, 114), (50, 120), (16, 114), (4, 100)]), 'mask', 'b'),
              L(outline([(60, 44), (94, 44), (96, 100), (84, 112), (66, 112)]), 'mask_d', 'b', False),
              L(outline([(16, 84), (34, 82), (50, 85), (66, 82), (84, 84), (88, 100), (72, 112), (50, 116), (28, 112), (12, 100)]), 'mask', 'f'),
              L(quad((16, 84), (50, 80), (84, 84)), OUTC, 'f', False, False, 1.2),
              L(outline([(56, 84), (80, 82), (86, 100), (72, 112), (58, 112)]), 'mask_d', 'f', False)]
             + helmet('front', 58) + goggles_up('front', 46),
    'side': [L(outline([(14, 50), (40, 50), (60, 56), (88, 76), (92, 96), (84, 114), (56, 118), (26, 112), (10, 90)]), 'mask', 'b'),
             L(outline([(14, 50), (40, 52), (40, 104), (24, 110), (10, 90)]), 'mask_d', 'b', False),
             L(outline([(70, 80), (92, 82), (94, 100), (84, 112), (64, 110)]), 'mask', 'f', ln=True)]
            + helmet('side') + goggles_up('side', 48),
    'back': [L(outline([(4, 64), (96, 64), (98, 96), (84, 114), (50, 118), (16, 114), (2, 96)]), 'mask', 'b'),
             L(outline([(56, 64), (98, 64), (98, 96), (84, 112), (62, 110)]), 'mask_d', 'b', False)] + helmet('back'),
}
# Timothy Western: el mismo casco bajado hasta las cejas, con las gafas de montura verde puestas sobre los ojos y el
# pasamontañas negro que le asoma por los lados de la cara; ojos caídos y sonrisa torcida
CHARS['timothy-western'] = {
    'body': 'normal', 'pal': pal('#2a3040', '#e8a060', iris='#6a2a2a', nose='#e8a0a0', **HELM),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'eye_y': 75, 'nose': (50, 84, 2.6), 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 60), (94, 60), (96, 100), (82, 112), (50, 116), (18, 112), (4, 100)]), 'mask', 'b'),
              L(outline([(10, 62), (90, 62), (88, 70), (12, 70)]), DARK, 'f', False),
              # gafas puestas: solo la montura verde oliva alrededor de cada ojo (los cristales dejan ver los ojos)
              L(outline([(18, 67), (46, 65), (47, 81), (38, 84), (18, 81)]) + [outline([(18, 67), (46, 65), (47, 81), (38, 84), (18, 81)])[0]], 'frame', 'f', False, False, 3.2),
              L(outline([(82, 67), (54, 65), (53, 81), (62, 84), (82, 81)]) + [outline([(82, 67), (54, 65), (53, 81), (62, 84), (82, 81)])[0]], 'frame', 'f', False, False, 3.2),
              L([(46, 70), (54, 70)], 'frame', 'f', False, False, 2.4)]
             + helmet('front', 60),
    'side': [L(outline([(14, 54), (40, 54), (50, 70), (44, 96), (24, 104), (10, 86)]), 'mask', 'b')]
            + helmet('side') + [L(outline([(78, 64), (94, 64), (98, 82), (82, 84)]), 'frame', 'f', ln=True), L([(48, 70), (78, 70)], DARK, 'f', False, False, 2.4)],
    'back': [L(outline([(4, 60), (96, 60), (96, 92), (80, 104), (50, 108), (20, 104), (4, 92)]), 'mask', 'b')] + helmet('back')
            + [L(quad((6, 72), (50, 68), (94, 72)), DARK, 'f', False, False, 2.4)],
}
# Wallace Hammond: casco con las gafas blancas subidas, rayas de tigre marrones en las mejillas y la nariz, ojos grandes
# azules y la barbilla tapada por el pasamontañas negro
CHARS['wallace-hammond'] = {
    'body': 'normal', 'pal': pal('#2a3040', '#f0a050', iris='#2a7a8a', stripe='#a0501e', **HELM),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'eye_y': 76, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 60), (94, 60), (96, 100), (82, 112), (50, 116), (18, 112), (4, 100)]), 'mask', 'b'),
              L(outline([(30, 104), (50, 100), (70, 104), (62, 114), (50, 116), (38, 114)]), 'mask', 'f', ln=True),
              L([(18, 84), (30, 86)], 'stripe', 'f', False, False, 2.2), L([(18, 90), (32, 92)], 'stripe', 'f', False, False, 2.2),
              L([(82, 84), (70, 86)], 'stripe', 'f', False, False, 2.2), L([(82, 90), (68, 92)], 'stripe', 'f', False, False, 2.2),
              L([(44, 66), (50, 70), (56, 66)], 'stripe', 'f', False, False, 1.6)]
             + helmet('front', 60) + goggles_up('front', 50),
    'side': [L(outline([(14, 54), (40, 54), (50, 70), (44, 96), (24, 104), (10, 86)]), 'mask', 'b')]
            + helmet('side') + goggles_up('side', 50) + [L([(70, 88), (80, 90)], 'stripe', 'f', False, False, 2.2)],
    'back': [L(outline([(4, 60), (96, 60), (96, 92), (80, 104), (50, 108), (20, 104), (4, 92)]), 'mask', 'b')] + helmet('back'),
}
# Shirley Stevens: pelo negro peinado hacia atrás que acaba en pinchos de punta en lo alto, sienes cortas; cara alargada
# morena con una nariz larga, cejas gruesas de enfado, ojos verdes y la boca en un arco de disgusto
CHARS['shirley-stevens'] = {
    'body': 'normal', 'pal': pal('#24201e', '#d09060', iris='#3a7a3a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'eye_y': 76, 'face_front': LONG_FACE, 'nose': (50, 86, 3),
             'hairline': [(14, 64), (18, 46), (30, 40), (44, 46), (50, 56), (56, 46), (70, 40), (82, 46), (86, 64)]},
    'front': [L(outline([(12, 70), (10, 40), (18, 18), (24, 2, 1), (34, 12), (40, -10, 1), (48, 6), (50, -24, 1), (56, 4), (64, -8, 1), (68, 10),
                         (78, 2, 1), (84, 20), (90, 40), (88, 70), (82, 66), (18, 66)])),
              L(outline([(56, 4), (64, -8, 1), (68, 10), (78, 2, 1), (84, 20), (88, 44), (86, 64), (76, 40)]), 'shade', 'b', False)] + headset('front', 98),
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (12, 40), (4, 22, 1), (20, 22), (18, 2, 1), (34, 10), (40, -14, 1), (52, 4), (60, -12, 1), (66, 8),
                        (84, 10, 1), (82, 24), (88, 36), (76, 42), (60, 46), (52, 62), (50, 80)])),
             L(outline([(16, 46), (20, 76), (38, 88), (28, 60)]), 'shade', 'b', False)] + headset('side', 96),
    'back': [L(outline([(14, 82), (10, 40), (18, 18), (24, 0, 1), (34, 12), (40, -12, 1), (48, 4), (52, -22, 1), (58, 4), (64, -10, 1), (68, 10),
                        (78, 0, 1), (84, 20), (90, 40), (86, 82), (50, 88)])),
             L(outline([(58, 6), (84, 22), (88, 50), (84, 80), (66, 84)]), 'shade', 'b', False)] + headset('back'),
}
# Ian Smith: cabeza alta y cuadrada morena, rapada, con un pelo rojo corto y plano arriba como un cepillo; ojos blancos
# medio cerrados de aburrimiento, ojeras y unos labios enormes en morro
IAN_FACE = blob([(14, 40), (50, 34), (86, 40), (90, 76), (86, 104), (64, 114), (36, 114), (14, 104), (10, 76)])
CHARS['ian-smith'] = {
    'body': 'corpulento', 'pal': pal('#a82a1a', '#a87a5a', lip='#f0d8c8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': IAN_FACE, 'hairline': False, 'big_ears': 1, 'ear_out': 2},
    'front': [L(outline([(18, 42), (16, 8), (50, 0), (84, 8), (82, 42)]), 'skin'),
              L(outline([(16, 12), (50, 2), (84, 12), (84, 0), (78, -10), (50, -14), (22, -10), (16, 0)]), 'mid', 'f', ln=True),
              L(outline([(58, -12), (80, -8), (84, 6), (62, 4)]), 'shade', 'f', False),
              L(outline([(24, 72), (42, 70), (40, 76), (26, 76)]), WHITE, 'f', ln=True), L(outline([(76, 72), (58, 70), (60, 76), (74, 76)]), WHITE, 'f', ln=True),
              L(ell(33, 74, 1.2, 1.4), OUTC, 'f', False), L(ell(67, 74, 1.2, 1.4), OUTC, 'f', False),
              L([(24, 70), (42, 68)], OUTC, 'f', False, False, 1.6), L([(76, 70), (58, 68)], OUTC, 'f', False, False, 1.6),
              L([(50, 70), (50, 88)], 'skin_d', 'f', False, False, 1.2),
              L(outline([(36, 98), (50, 92), (64, 98), (60, 106), (50, 108), (40, 106)]), 'lip', 'f', ln=True),
              L(quad((40, 100), (50, 104), (60, 100)), OUTC, 'f', False, False, 1.0)] + headset('front', 100),
    'side': [L(outline([(20, 96), (12, 60), (14, 6), (50, 0), (80, 6), (90, 40), (94, 80), (90, 108), (70, 116), (40, 112)]), 'skin'),
             L(outline([(12, 40), (40, 50), (50, 90), (40, 110), (20, 96)]), 'skin_d', 'b', False),
             L(outline([(14, 10), (50, 2), (80, 8), (80, -4), (50, -14), (16, -8)]), 'mid', 'f', ln=True),
             L(outline([(84, 96), (96, 94), (98, 104), (86, 106)]), 'lip', 'f', ln=True), L([(78, 72), (88, 72)], OUTC, 'f', False, False, 1.6)]
            + headset('side', 100),
    'back': [L(outline([(18, 96), (16, 8), (50, 0), (84, 8), (82, 96), (50, 104)]), 'skin'),
             L(outline([(52, 10), (82, 10), (82, 94), (52, 100)]), 'skin_d', 'b', False),
             L(outline([(16, 12), (50, 2), (84, 12), (84, 0), (78, -10), (50, -14), (22, -10), (16, 0)]), 'mid', 'f', ln=True)] + headset('back'),
}
# Greene Beray: un casco de cubo azul marino con una insignia amarilla que le tapa hasta los ojos; en el derecho (izquierda
# de la imagen) lleva una mira roja en un aro negro; el otro ojo, de enfado
CHARS['greene-beray'] = {
    'body': 'normal', 'pal': pal('#2a3456', '#f0a858', hat='#2a3456', hat_d='#1e263e', badge='#e8c820', scope='#d81a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(4, 74), (8, 12), (14, -2), (86, -2), (92, 12), (96, 74), (84, 66), (16, 66)]), 'hat', 'f', ln=True),
              L(outline([(58, 0), (86, 0), (94, 70), (82, 64), (70, 40)]), 'hat_d', 'f', False),
              L(outline([(50, 22, 1), (58, 30), (54, 40), (46, 40), (42, 30)]), 'badge', 'f', ln=True),
              L(ell(30, 78, 10, 10), DARK, 'f', ln=True), L(ell(30, 78, 6.8, 6.8), 'scope', 'f', False), L(ell(28, 76, 2, 2), (255, 160, 160, 255), 'f', False),
              L(quad((22, 86), (18, 96), (24, 104)), DARK, 'f', False, False, 1.4),
              L(outline([(58, 76), (76, 72), (74, 80), (62, 82)]), WHITE, 'f', ln=True), L(ell(68, 77, 2.4, 2.8), OUTC, 'f', False),
              L([(56, 72), (78, 68)], OUTC, 'f', False, False, 2.4)] + headset('front', 96),
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(0, 70), (4, 10), (14, -2), (80, -2), (90, 10), (96, 66), (60, 60), (30, 66)]), 'hat', 'f', ln=True),
             L(outline([(4, 30), (40, 34), (30, 66), (0, 70)]), 'hat_d', 'f', False),
             L(ell(90, 76, 4, 7), 'scope', 'f', ln=True)] + headset('side', 96),
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(2, 74), (6, 12), (14, -2), (86, -2), (94, 12), (98, 74), (50, 76)]), 'hat', 'f', ln=True),
             L(outline([(58, 0), (86, 0), (96, 74), (64, 76)]), 'hat_d', 'f', False)] + headset('back'),
}
# Taylor Firepool: sombrero de ala ancha verde oscuro con una cinta crema; debajo, pelo lila corto y un antifaz negro sobre
# los ojos; media sonrisa
CHARS['taylor-firepool'] = {
    'body': 'normal', 'pal': pal('#a898c8', '#fcd8b8', hat='#2e3a2a', hat_d='#1e2a1c', band='#ece4cc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(14, 70), (14, 40), (86, 40), (86, 70), (80, 66), (20, 66)])),
              L(outline([(20, 64), (50, 60), (80, 64), (82, 80), (62, 82), (50, 76), (38, 82), (18, 80)]), DARK, 'f', ln=True),
              L(ell(34, 72, 4, 2.6), WHITE, 'f', False), L(ell(66, 72, 4, 2.6), WHITE, 'f', False),
              L(outline([(-24, 52), (-10, 40), (20, 34), (50, 32), (80, 34), (110, 40), (124, 52), (104, 58), (50, 52), (-4, 58)]), 'hat', 'f', ln=True),
              L(outline([(20, 36), (24, 0), (40, -12), (50, -6), (60, -12), (76, 0), (80, 36), (50, 34)]), 'hat', 'f', ln=True),
              L(outline([(22, 22), (50, 20), (78, 22), (80, 34), (50, 34), (20, 34)]), 'band', 'f', ln=True),
              L(outline([(60, -8), (76, 2), (80, 22), (66, 20)]), 'hat_d', 'f', False)] + headset('front', 94),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (14, 40), (60, 40), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(outline([(70, 64), (92, 64), (92, 78), (72, 78)]), DARK, 'f', ln=True),
             L(outline([(-14, 66), (0, 52), (40, 40), (80, 32), (112, 26), (118, 32), (84, 44), (40, 54), (4, 66)]), 'hat', 'f', ln=True),
             L(outline([(16, 46), (18, 10), (36, -6), (64, -6), (78, 8), (80, 36), (50, 40)]), 'hat', 'f', ln=True),
             L(outline([(16, 30), (80, 22), (80, 36), (16, 44)]), 'band', 'f', ln=True)] + headset('side', 94),
    'back': [L(outline([(14, 80), (12, 40), (88, 40), (86, 80), (70, 88), (64, 80, 1), (58, 90), (50, 82, 1), (42, 90), (36, 80, 1), (30, 88)])),
             L(outline([(56, 42), (86, 42), (86, 78), (64, 84)]), 'shade', 'b', False),
             L(outline([(-20, 50), (-8, 38), (20, 32), (50, 30), (80, 32), (108, 38), (120, 50), (100, 56), (50, 52), (0, 56)]), 'hat', 'f', ln=True),
             L(outline([(20, 36), (22, 6), (40, -8), (60, -8), (78, 6), (80, 36), (50, 34)]), 'hat', 'f', ln=True),
             L(outline([(20, 22), (50, 20), (80, 22), (80, 34), (20, 34)]), 'band', 'f', ln=True)] + headset('back'),
}
# Marge Fielding: pelo rubio recogido; un flequillo barrido hacia su izquierda con una horquilla marrón, y por detrás un
# moño en punta que sube curvándose; ojos grandes azules y sonrisa
CHARS['marge-fielding'] = {
    'body': 'chica', 'pal': pal('#f0d890', '#fcd8b8', iris='#2a8ab0', clip='#8a5a2a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(44, 10), (46, -14), (54, -30, 1), (58, -10), (66, -18, 1), (64, 6)])),
              L(outline([(14, 66), (12, 38), (24, 14), (50, 6), (76, 14), (88, 38), (86, 66), (80, 56), (70, 48), (50, 44), (30, 48), (20, 56)])),
              L(outline([(60, 10), (82, 22), (88, 44), (80, 54), (72, 32)]), 'shade', 'b', False),
              L(outline([(14, 66), (16, 40), (30, 24), (56, 20), (76, 26), (60, 36), (40, 48), (26, 60)]), 'mid', 'f', ln=True),
              L(outline([(30, 30), (36, 28), (34, 40), (28, 42)]), 'clip', 'f', ln=True)] + headset('front', 94),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (14, 36), (26, 14), (40, 4), (36, -22), (50, -34, 1), (54, -14), (62, -24, 1), (64, 4), (80, 14),
                        (90, 34), (78, 44), (62, 46), (52, 62), (50, 80)])),
             L(outline([(16, 46), (20, 76), (38, 88), (28, 60)]), 'shade', 'b', False)] + headset('side', 94),
    'back': [L(outline([(14, 76), (12, 38), (24, 14), (40, 6), (40, -16), (50, -32, 1), (56, -12), (64, -22, 1), (62, 6), (76, 14), (88, 38), (86, 76),
                        (50, 84)])),
             L(outline([(56, 8), (82, 26), (88, 50), (84, 74), (64, 80)]), 'shade', 'b', False),
             strand([(50, 10), (50, 70)], 'shade', 'b', 1.0)] + headset('back'),
}
# Marshall Firsthand: una melena gris clara enorme y lisa que le cae como una campana hasta los hombros, con mechones que
# le cruzan la frente; visor oscuro de lado a lado y sonrisa de suficiencia
CHARS['marshall-firsthand'] = {
    'body': 'normal', 'pal': pal('#bcb4bc', '#f0a858', light='#d8eaee', shade='#9a8e98'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(-18, 92, 1), (-4, 60), (8, 26), (26, 4), (50, -2), (74, 4), (92, 26), (104, 60), (118, 92, 1), (90, 88), (84, 60), (16, 60),
                         (10, 88)])),
              L(outline([(62, 4), (90, 28), (104, 64), (114, 90, 1), (92, 84), (84, 56)]), 'shade', 'b', False),
              L(outline([(16, 60), (22, 40), (36, 30), (48, 40), (58, 30), (70, 34), (62, 46), (56, 58), (64, 70, 1), (48, 56), (40, 46), (28, 56)]), 'mid', 'f', ln=True),
              L(outline([(30, 34), (44, 30), (50, 38), (40, 40)]), 'light', 'f', False)]
             + sunglasses('front', 74, 'band') + headset('front', 94),
    'side': [L(outline([(60, 80), (44, 92), (24, 98), (-4, 98, 1), (0, 70), (8, 36), (24, 10), (52, 0), (76, 8), (90, 26), (88, 40), (76, 44), (66, 54)])),
             L(outline([(0, 70), (20, 50), (44, 60), (40, 90), (20, 96), (0, 96)]), 'shade', 'b', False)] + sunglasses('side', 74) + headset('side', 94),
    'back': [L(outline([(-18, 96, 1), (-4, 60), (8, 26), (26, 4), (50, -2), (74, 4), (92, 26), (104, 60), (118, 96, 1), (80, 92), (50, 90), (20, 92)])),
             L(outline([(58, 4), (92, 30), (106, 66), (114, 92), (70, 88)]), 'shade', 'b', False),
             L(outline([(30, 50), (50, 44), (66, 52), (50, 58)]), 'light', 'b', False)] + headset('back'),
}
# Holly Mirror: piel morena; pelo verde oliva oscuro peinado hacia atrás con raya en medio, pegado a la cabeza y abierto en
# puntas a la altura de la barbilla; ojos turquesa rasgados, un lunar y labios pequeños
CHARS['holly-mirror'] = {
    'body': 'chica', 'pal': pal('#3e4a24', '#8a6448', iris='#3ac0c8', lip='#c09080'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'eye_y': 76, 'hairline': [(14, 70), (16, 46), (30, 34), (50, 32), (70, 34), (84, 46), (86, 70)]},
    'front': [L(outline([(-4, 106, 1), (10, 90), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (90, 90), (104, 106, 1), (82, 98), (80, 66), (20, 66),
                         (18, 98)])),
              L(outline([(60, 8), (86, 26), (92, 60), (92, 96), (82, 96), (80, 50)]), 'shade', 'b', False),
              strand([(50, 6), (50, 32)], 'deep', 'b', 1.2), strand([(40, 10), (32, 34)], 'deep', 'b', 1.0), strand([(60, 10), (68, 34)], 'deep', 'b', 1.0),
              L(ell(28, 86, 1.2, 1.2), OUTC, 'f', False), L(ell(50, 94, 3.4, 1.8), 'lip', 'f', ln=True)] + headset('front', 94),
    'side': [L(outline([(54, 70), (52, 96), (40, 104), (22, 112, 1), (16, 100), (8, 106, 1), (6, 80), (6, 40), (20, 14), (50, 2), (76, 8), (90, 26), (86, 40),
                        (74, 44), (62, 50)])),
             L(outline([(10, 50), (30, 50), (44, 76), (40, 100), (20, 104), (8, 86)]), 'shade', 'b', False)] + headset('side', 94),
    'back': [L(outline([(-4, 110, 1), (8, 90), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (92, 90), (104, 110, 1), (74, 104), (50, 118, 1), (26, 104)])),
             L(outline([(58, 8), (88, 30), (94, 80), (90, 104), (70, 100), (66, 60)]), 'shade', 'b', False),
             strand([(50, 10), (50, 110)], 'deep', 'b', 1.0)] + headset('back'),
}
# Joe Kenneddy: pelo castaño anaranjado en un tupé de dos pinchos hacia arriba y atrás, con las sienes cortas; un visor
# negro de lado a lado sobre los ojos, orejas grandes y sonrisa
CHARS['joe-kenneddy'] = {
    'body': 'normal', 'pal': pal('#9a5a1a', '#f4b060'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'big_ears': 2, 'ear_out': 3,
             'hairline': [(14, 62), (18, 48), (34, 52), (50, 50), (66, 52), (82, 48), (86, 62)]},
    'front': [L(outline([(14, 64), (12, 40), (22, 20), (34, 6), (36, -14, 1), (46, 0), (54, -10), (62, -22, 1), (64, 0), (78, 16), (88, 40), (86, 64)])),
              L(outline([(58, 0), (64, -18, 1), (66, 2), (80, 18), (88, 44), (84, 60), (72, 30)]), 'shade', 'b', False),
              strand([(40, 10), (36, 40)], 'deep', 'b', 1.0), strand([(56, 6), (58, 40)], 'deep', 'b', 1.0)]
             + sunglasses('front', 76, 'band') + headset('front', 94),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 36), (24, 12), (40, 2), (52, -20, 1), (58, 0), (70, -10), (80, -26, 1), (80, 4), (90, 28), (84, 40),
                        (70, 44), (58, 48), (52, 62), (50, 80)])),
             L(outline([(14, 46), (18, 76), (38, 88), (28, 60)]), 'shade', 'b', False)] + sunglasses('side', 76) + headset('side', 94),
    'back': [L(outline([(14, 80), (10, 40), (22, 16), (36, 4), (40, -14, 1), (50, 0), (58, -10), (64, -20, 1), (66, 2), (80, 16), (90, 40), (86, 80), (50, 88)])),
             L(outline([(56, 4), (82, 22), (90, 50), (84, 78), (64, 84)]), 'shade', 'b', False)] + headset('back'),
}
# Ian Sights (portero suplente): gorra de visera gris verdosa, por debajo un pelo verde oliva recogido con dos manojos de
# billetes (o lazos) verdes abiertos a cada lado; gafas de sol redondas negras y una sonrisa de dientes apretados
CHARS['ian-sights'] = {
    'body': 'normal', 'pal': pal('#5a5a24', '#f4a050', cap='#4a5a5a', cap_d='#36424a', bill='#5a7a2a', bill_d='#3e5a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': [L(outline([(16, 66), (14, 40), (86, 40), (84, 66), (70, 60), (30, 60)])),
              L(outline([(16, 66), (-10, 56, 1), (2, 66), (-14, 72, 1), (4, 74), (-8, 86, 1), (16, 78)]), 'bill', 'b', ln=True),
              L(outline([(84, 66), (110, 56, 1), (98, 66), (114, 72, 1), (96, 74), (108, 86, 1), (84, 78)]), 'bill', 'b', ln=True),
              L(outline([(12, 48), (12, 22), (26, 4), (50, -2), (74, 4), (88, 22), (88, 48), (50, 44)]), 'cap', 'f', ln=True),
              L(outline([(60, 0), (80, 10), (88, 30), (88, 46), (70, 42)]), 'cap_d', 'f', False),
              L(quad((12, 48), (50, 54), (88, 48)), OUTC, 'f', False, False, 1.2)]
             + sunglasses('front', 74, 'round') + headset('front', 94),
    'side': [L(outline([(44, 94), (22, 90), (10, 66), (12, 44), (60, 44), (58, 54), (52, 64), (50, 82)])),
             L(outline([(14, 66), (-14, 54, 1), (0, 66), (-16, 76, 1), (4, 76), (-6, 90, 1), (20, 80)]), 'bill', 'b', ln=True),
             L(outline([(8, 48), (8, 22), (24, 2), (52, -4), (74, 4), (84, 22), (86, 42), (106, 50, 1), (86, 52), (50, 50)]), 'cap', 'f', ln=True)]
            + sunglasses('side', 74) + headset('side', 94),
    'back': [L(outline([(14, 84), (12, 40), (88, 40), (86, 84), (50, 90)])),
             L(outline([(14, 66), (-12, 56, 1), (0, 66), (-14, 74, 1), (4, 76), (-6, 88, 1), (16, 80)]), 'bill', 'b', ln=True),
             L(outline([(86, 66), (112, 56, 1), (100, 66), (114, 74, 1), (96, 76), (106, 88, 1), (84, 80)]), 'bill', 'b', ln=True),
             strand([(36, 50), (34, 84)], 'deep', 'b', 1.0), strand([(64, 50), (66, 84)], 'deep', 'b', 1.0),
             L(outline([(10, 50), (10, 22), (26, 4), (50, -2), (74, 4), (90, 22), (90, 50), (50, 54)]), 'cap', 'f', ln=True),
             L(outline([(58, 0), (80, 10), (90, 30), (90, 50), (70, 52)]), 'cap_d', 'f', False)] + headset('back'),
}
# Ryan Tappin: cara pálida y redonda; pelo castaño corto con un pico en medio de la frente y las sienes peladas, la nuca en
# dos puntas; gafas de sol redondas negras, sonrisa amplia y orejas grandes
CHARS['ryan-tappin'] = {
    'body': 'normal', 'pal': pal('#5a361a', '#fce8c8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 2, 'ear_out': 5, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(18, 42), (16, 24), (28, 8), (50, 2), (72, 8), (84, 24), (82, 42), (70, 30), (58, 30), (50, 56, 1), (42, 30), (30, 30)]), 'mid', 'f', ln=True),
              L(outline([(56, 8), (74, 12), (82, 30), (70, 26), (56, 26)]), 'shade', 'f', False),
              L(quad((30, 92), (50, 104), (70, 92)), OUTC, 'f', False, False, 1.6)]
             + sunglasses('front', 76, 'round') + headset('front', 96),
    'side': [L(outline([(44, 94), (40, 108, 1), (30, 96), (22, 90), (12, 66), (14, 36), (28, 12), (54, 4), (78, 12), (88, 30), (74, 36), (62, 34), (54, 54),
                        (52, 76)])),
             L(outline([(16, 46), (22, 76), (40, 92), (30, 60)]), 'shade', 'b', False),
             L(quad((82, 92), (86, 96), (90, 92)), OUTC, 'f', False, False, 1.4)] + sunglasses('side', 76) + headset('side', 96),
    'back': [L(outline([(16, 80), (14, 38), (26, 12), (50, 4), (74, 12), (86, 38), (84, 80), (66, 86), (60, 98, 1), (54, 86), (46, 86), (40, 98, 1), (34, 86)])),
             L(outline([(58, 8), (84, 30), (86, 76), (66, 84)]), 'shade', 'b', False)] + headset('back'),
}
# Linda Shadey: pelo morado oscuro con raya en medio, liso y pegado, que se recoge por detrás y se abre en dos ondas a los
# lados del cuello; ojos verdes rasgados y la boca en una raya seria
CHARS['linda-shadey'] = {
    'body': 'chica', 'pal': pal('#3a2a48', '#fcd4b0', iris='#2a8a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94, 'hairline': [(14, 72), (16, 48), (30, 36), (50, 34), (70, 36), (84, 48), (86, 72)]},
    'front': [L(outline([(10, 72), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (90, 72), (82, 66), (18, 66)])),
              L(outline([(60, 8), (86, 26), (92, 60), (84, 66), (80, 40)]), 'shade', 'b', False),
              strand([(50, 6), (50, 34)], 'deep', 'b', 1.2),
              L(outline([(14, 82), (2, 90), (-4, 104), (8, 112), (20, 104), (16, 96)]), 'mid', 'f', ln=True),
              L(outline([(86, 82), (98, 90), (104, 104), (92, 112), (80, 104), (84, 96)]), 'mid', 'f', ln=True)] + headset('front', 94),
    'side': [L(outline([(48, 76), (46, 96), (52, 110), (40, 116), (22, 108), (10, 90), (6, 60), (10, 32), (24, 10), (52, 2), (76, 8), (90, 26), (86, 40),
                        (74, 44), (60, 48)])),
             L(outline([(10, 50), (30, 50), (44, 80), (48, 104), (28, 110), (12, 90)]), 'shade', 'b', False)] + headset('side', 94),
    'back': [L(outline([(6, 90), (6, 40), (20, 14), (50, 4), (80, 14), (94, 40), (94, 90), (80, 108), (50, 112), (20, 108)])),
             L(outline([(58, 8), (88, 30), (94, 80), (80, 104), (62, 104)]), 'shade', 'b', False),
             strand([(50, 8), (50, 108)], 'deep', 'b', 1.0)] + headset('back'),
}
# Sid Safehouse: grandullón moreno de cara ancha y rapado, con el pelo en franjas gris claro sobre la coronilla; gafas de
# sol oscuras envolventes y la boca en una raya de enfado
CHARS['sid-safehouse'] = {
    'body': 'corpulento', 'pal': pal('#c8ccd8', '#b87840', skin_d='#9a6230'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'face_front': WIDE_FACE, 'nose': (50, 86, 2.6), 'hairline': False,
             'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + [L(quad((26, 30), (50, 10), (74, 30)), 'mid', 'f', False, False, 3.2), L(quad((22, 44), (50, 24), (78, 44)), 'mid', 'f', False, False, 3.2),
                              L(quad((36, 18), (50, 4), (64, 18)), 'mid', 'f', False, False, 3.0)]
             + sunglasses('front', 72) + headset('front', 96),
    'side': bald('side') + [L(quad((20, 40), (40, 10), (72, 14)), 'mid', 'f', False, False, 3.2), L(quad((30, 52), (50, 24), (82, 30)), 'mid', 'f', False, False, 3.2),
                            L(quad((14, 30), (30, 6), (58, 4)), 'mid', 'f', False, False, 3.0)]
            + sunglasses('side', 72) + headset('side', 96),
    'back': bald('back') + [L(quad((22, 34), (50, 14), (78, 34)), 'mid', 'f', False, False, 3.2), L(quad((20, 50), (50, 30), (80, 50)), 'mid', 'f', False, False, 3.2),
                            L(quad((34, 20), (50, 6), (66, 20)), 'mid', 'f', False, False, 3.0)] + headset('back'),
}
