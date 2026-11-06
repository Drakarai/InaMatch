"""Big Waves (IE3, Australia): pelos de surfista, tupés, crestas, gafas y viseras, con sus modelos 3D como referencia
(contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from heads import quad

WHITE = (250, 250, 250, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


def white_eyes(y=76, sep=15, rx=6.4, ry=6, pupil=1.8, lid=None):
    """Ojos blancos redondos con la pupila pequeña (los de cara de pasmo); lid: párpado caído de sueño."""
    out = []
    for cx in (50 - sep, 50 + sep):
        out += [L(ell(cx, y, rx, ry), WHITE, 'f', ln=True), L(ell(cx, y + 0.5, pupil, pupil * 1.1), OUTC, 'f', False)]
        if lid:
            out.append(L(outline([(cx - rx - 0.6, y - lid), (cx + rx + 0.6, y - lid), (cx + rx, y - ry - 1), (cx - rx, y - ry - 1)]), 'skin', 'f', False))
            out.append(L([(cx - rx, y - lid), (cx + rx, y - lid)], OUTC, 'f', False, False, 1.8))
    return out


def side_eye(y=76, lid=None):
    out = [L(ell(84, y, 3.6, 5.4), WHITE, 'f', ln=True), L(ell(85.4, y + 0.5, 1.4, 1.8), OUTC, 'f', False)]
    if lid:
        out.append(L([(80, y - lid), (88, y - lid)], OUTC, 'f', False, False, 1.8))
    return out


def rect_glasses(view, y=76, c=(30, 30, 30, 255)):
    if view == 'front':
        return [L(outline([(22, y - 6), (46, y - 6), (46, y + 5), (23, y + 5)]) + [(22, y - 6)], c, 'f', False, False, 1.4),
                L(outline([(78, y - 6), (54, y - 6), (54, y + 5), (77, y + 5)]) + [(78, y - 6)], c, 'f', False, False, 1.4),
                L([(46, y - 3), (54, y - 3)], c, 'f', False, False, 1.2)]
    if view == 'side':
        return [L([(78, y - 6), (90, y - 6), (90, y + 5), (79, y + 5), (78, y - 6)], c, 'f', False, False, 1.4), L([(50, y - 3), (78, y - 3)], c, 'f', False, False, 1.2)]
    return []


# Gene Whalon (portero): piel morena; pelo rosa blanquecino liso en forma de casco, con un flequillo largo de mechones en
# punta que le tapa la frente y el ojo derecho, y la nuca en puntas; una cicatriz blanca en la mejilla y sonrisa de dientes
CHARS['gene-whalon'] = {
    'body': 'normal', 'pal': pal('#e8cad0', '#9a6236', iris='#2a9aa0', shade='#c4a0aa', scar='#ecd8d8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(12, 72), (8, 38), (20, 12), (50, 2), (80, 12), (92, 38), (90, 72), (82, 66), (18, 66)])),
              L(outline([(60, 6), (84, 18), (92, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(12, 74, 1), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 72, 1), (80, 58), (74, 70, 1), (66, 56), (58, 66, 1), (52, 54),
                         (44, 84, 1), (38, 62), (30, 76, 1), (24, 60), (18, 70)]), 'mid', 'f'),
              L(outline([(56, 22), (78, 30), (86, 50), (78, 56), (70, 40)]), 'shade', 'f', False),
              L(outline([(26, 26), (50, 20), (40, 30)]), WHITE, 'f', False),
              L([(70, 84), (78, 92)], 'scar', 'f', False, False, 1.8), L([(74, 82), (80, 88)], 'scar', 'f', False, False, 1.4)],
    'side': [L(outline([(44, 92), (34, 98, 1), (26, 88), (12, 92, 1), (10, 70), (8, 38), (22, 12), (50, 2), (74, 8), (90, 26), (94, 46), (92, 62, 1), (84, 48),
                        (70, 46), (58, 52), (52, 66), (50, 80)])),
             L(outline([(10, 44), (34, 44), (44, 82), (26, 90), (12, 72)]), 'shade', 'b', False),
             L([(60, 82), (70, 92)], 'scar', 'f', False, False, 1.8)],
    'back': [L(outline([(12, 82), (8, 38), (20, 12), (50, 2), (80, 12), (92, 38), (88, 82), (76, 92, 1), (66, 84), (56, 96, 1), (48, 84), (38, 96, 1), (30, 84),
                        (20, 92, 1)])),
             L(outline([(20, 50), (50, 40), (80, 50), (86, 80), (60, 92), (30, 92), (14, 78)]), 'shade', 'b', False)],
}
# David Waterman: pelo morado de rizos en punta, abultadísimo y abierto en todas direcciones; piel clara con pecas, ojos
# blancos redondos de pasmo y la boca en una raya
CHARS['david-waterman'] = {
    'body': 'normal', 'pal': pal('#7a3a6e', '#f4c08a', shade='#5e2a54', freckle='#c88050'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 14, 9, seed=301, rx=58, ry=44, cy=40, lo=74)
             + [L(outline([(10, 70, 1), (14, 46), (28, 32), (50, 28), (72, 32), (86, 46), (90, 70, 1), (82, 58), (74, 62, 1), (66, 52), (58, 58, 1), (50, 50),
                           (42, 58, 1), (34, 52), (26, 62, 1), (18, 58)]), 'mid', 'f'),
                L(outline([(56, 30), (78, 38), (88, 54), (78, 56), (70, 44)]), 'shade', 'f', False)]
             + white_eyes(77, 15, 6.6, 6.4, 1.8)
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((24, 86), (28, 88), (26, 84), (76, 86), (72, 88), (74, 84))],
    'side': messy('side', 15, 8, seed=301, rx=54, ry=44, cy=40, nape=92, sweep=-0.3) + side_eye(77)
            + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((72, 86), (76, 88))],
    'back': messy('back', 14, 9, seed=301, rx=58, ry=44, cy=40, nape=92),
}
# Sonny Shore: piel muy clara; pelo castaño claro cortado en tazón, liso y con rayas de mechones, que le cae hasta las cejas
# y tapa las orejas; ojos rojizos y la boca seria
CHARS['sonny-shore'] = {
    'body': 'normal', 'pal': pal('#a87a40', '#fce8d8', iris='#b04a4a', shade='#86602e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 80), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (96, 80), (86, 80), (84, 66), (16, 66), (14, 80)])),
              L(outline([(62, 2), (86, 14), (98, 44), (94, 78), (86, 74), (80, 40)]), 'shade', 'b', False),
              L(outline([(6, 74), (8, 44), (24, 24), (50, 18), (76, 24), (92, 44), (94, 74), (84, 72), (82, 62), (66, 66), (50, 64), (34, 66), (18, 62), (16, 72)]), 'mid', 'f', ln=True),
              L(outline([(56, 22), (80, 30), (92, 50), (90, 70), (82, 60), (70, 40)]), 'shade', 'f', False)]
             + [strand([(x, 26 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 64)], 'deep', 'f', 1.0) for x in (20, 32, 44, 56, 68, 80)],
    'side': [L(outline([(52, 74), (40, 86), (18, 88), (6, 70), (6, 36), (22, 10), (52, 0), (78, 8), (94, 28), (96, 52), (92, 62), (78, 60), (64, 62), (56, 66)])),
             L(outline([(8, 40), (36, 40), (46, 74), (24, 86), (8, 70)]), 'shade', 'b', False)]
            + [strand([(x, 6 + abs(x - 50) * 0.2), (x - 4, 60 + (50 - x) * 0.3)], 'deep', 'b', 1.0) for x in (24, 40, 56, 72, 86)],
    'back': [L(outline([(4, 80), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (96, 80), (80, 88), (50, 90), (20, 88)])),
             L(outline([(58, 4), (86, 16), (98, 44), (94, 80), (70, 88), (66, 50)]), 'shade', 'b', False)]
            + [strand([(x, 2 + abs(x - 50) * 0.2), (x + (x - 50) * 0.1, 86)], 'deep', 'b', 1.0) for x in (16, 30, 44, 58, 72, 86)],
}
# Kjell Snapper: grandullón moreno de cara enorme y larga; la cabeza afeitada con el pelo rojo a los lados y una cresta
# verde de pinchos en lo alto; una nariz larga y gorda que le cuelga, los ojos cerrados y la boca en una raya
KJELL_FACE = blob([(14, 30), (50, 20), (86, 30), (92, 70), (88, 104), (70, 116), (30, 116), (12, 104), (8, 70)])
CHARS['kjell-snapper'] = {
    'body': 'corpulento', 'pal': pal('#c41a14', '#b07040', crest='#2a8060', crest_d='#1e5e46', nose='#8a5a5a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'none', 'face_front': KJELL_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(16, 40), (16, 10), (34, -4), (50, -8), (66, -4), (84, 10), (84, 40)]), 'skin'),
              L(outline([(18, 20), (24, 4), (34, -2), (28, 12), (22, 26)]), 'mid', 'f', ln=True),
              L(outline([(82, 20), (76, 4), (66, -2), (72, 12), (78, 26)]), 'mid', 'f', ln=True),
              L(outline([(40, 0), (36, -18, 1), (44, -10), (48, -26, 1), (54, -10), (62, -20, 1), (60, 0)]), 'crest', 'f', ln=True),
              L(outline([(50, -6), (54, -16), (58, -4)]), 'crest_d', 'f', False),
              L(outline([(44, 66), (56, 66), (60, 92), (54, 98), (46, 98), (40, 92)]), 'nose', 'f', ln=True),
              L([(30, 104), (70, 104)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(24, 104), (10, 70), (10, 10), (40, -6), (70, -4), (90, 20), (94, 60), (96, 96), (82, 116), (50, 120), (30, 114)]), 'skin'),
             L(outline([(10, 70), (8, 20), (30, 0), (60, -2), (70, 10), (50, 20), (30, 50), (24, 76)]), 'mid', 'b'),
             L(outline([(40, -2), (44, -20, 1), (52, -8), (60, -24, 1), (64, -6), (74, -14, 1), (72, 6), (56, 4)]), 'crest', 'f', ln=True),
             L(outline([(88, 66), (104, 86), (100, 96), (88, 90)]), 'nose', 'f', ln=True),
             L(quad((76, 74), (82, 78), (88, 74)), OUTC, 'f', False, False, 2.0), L([(80, 106), (92, 106)], OUTC, 'f', False, False, 1.6)],
    'back': [L(outline([(10, 96), (8, 20), (30, -2), (50, -6), (70, -2), (92, 20), (90, 96), (50, 104)]), 'mid'),
             L(outline([(56, 0), (84, 16), (92, 50), (88, 94), (60, 100)]), (150, 14, 10, 255), 'b', False),
             L(outline([(40, 0), (36, -18, 1), (44, -10), (48, -26, 1), (54, -10), (62, -20, 1), (60, 0)]), 'crest', 'f', ln=True)],
}
# Ken Crackham: pelo castaño oliva ondulado en un tupé abultado que se echa hacia delante y atrás; pecas, ojos rasgados y
# media sonrisa de listillo
CHARS['ken-crackham'] = {
    'body': 'normal', 'pal': pal('#6a5a24', '#f4b880', iris='#1e1e1e', shade='#4e421a', light='#9a8a4a', freckle='#c88050'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 66), (6, 38), (14, 12), (36, -6), (60, -8), (80, 2), (94, 22), (94, 46), (88, 66), (80, 56), (60, 50), (40, 48), (22, 56)])),
              L(outline([(60, -4), (82, 6), (94, 30), (88, 56), (76, 40)]), 'shade', 'b', False),
              L(outline([(22, 6), (40, -4), (56, 2), (44, 12), (30, 16)]), 'light', 'b', False), L(outline([(56, 18), (72, 14), (78, 26), (62, 28)]), 'light', 'b', False)]
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (74, 86), (70, 88))],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 36), (20, 6), (50, -10), (82, -6), (102, 6), (110, 22), (100, 36), (84, 40), (70, 44), (58, 50), (52, 64),
                        (50, 80)])),
             L(outline([(10, 40), (34, 40), (44, 80), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(40, -4), (70, -6), (96, 4), (78, 10), (50, 6)]), 'light', 'b', False)],
    'back': [L(outline([(12, 82), (6, 38), (14, 12), (36, -6), (64, -6), (86, 12), (94, 38), (88, 82), (50, 90)])),
             L(outline([(56, -2), (86, 14), (94, 44), (88, 80), (64, 88)]), 'shade', 'b', False),
             L(outline([(30, 6), (50, 0), (60, 14), (40, 18)]), 'light', 'b', False)],
}
# Shawn Princeton: cara alargada y pálida con orejas grandes; pelo verde muy oscuro peinado hacia arriba en un rulo alto y
# estrecho, con las sienes cortas; gafas de media luna negras sobre unos ojos de sueño y una sonrisa ladeada
CHARS['shawn-princeton'] = {
    'body': 'delgado', 'pal': pal('#1e4a3a', '#fce4cc', shade='#163a2c', light='#3a6a54'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(outline([(18, 64), (16, 30), (30, 10), (34, 0), (38, -14), (50, -20), (62, -14), (66, 0), (70, 10), (84, 30), (82, 64), (70, 40), (60, 30),
                         (50, 40), (40, 30), (30, 40)])),
              L(outline([(54, -18), (62, -12), (66, 0), (76, 20), (82, 50), (70, 34), (58, 10)]), 'shade', 'b', False),
              L(outline([(44, -14), (50, -18), (48, -2), (44, 10)]), 'light', 'b', False),
              strand([(36, 0), (42, 30)], 'deep', 'b', 1.0), strand([(64, 0), (58, 30)], 'deep', 'b', 1.0),
              L([(24, 78), (44, 78)], OUTC, 'f', False, False, 2.0), L([(56, 78), (76, 78)], OUTC, 'f', False, False, 2.0),
              L(ell(34, 80, 2, 1.6), OUTC, 'f', False), L(ell(66, 80, 2, 1.6), OUTC, 'f', False),
              L(quad((22, 78), (34, 88), (46, 78)), OUTC, 'f', False, False, 1.4), L(quad((54, 78), (66, 88), (78, 78)), OUTC, 'f', False, False, 1.4),
              L([(46, 78), (54, 78)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (24, 6), (40, -18), (62, -30), (86, -24), (98, -10), (94, 6), (84, 20), (72, 36), (60, 44), (52, 62),
                        (50, 80)])),
             L(outline([(14, 34), (40, 30), (46, 80), (24, 88), (12, 60)]), 'shade', 'b', False),
             L([(78, 78), (90, 78)], OUTC, 'f', False, False, 2.0), L(quad((78, 78), (84, 86), (92, 78)), OUTC, 'f', False, False, 1.4),
             L([(50, 78), (78, 78)], OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(18, 84), (14, 34), (28, 10), (36, -10), (44, -28), (56, -28), (64, -10), (72, 10), (86, 34), (82, 84), (50, 92)])),
             L(outline([(54, -24), (64, -8), (82, 30), (82, 80), (60, 88)]), 'shade', 'b', False)],
}
# Matt Fischer: cabeza alta y rectangular; las sienes y la nuca de castaño rapado y arriba una corona de pinchos rubios;
# orejas en punta, gafas rectangulares de alambre, ojos de sueño y la boca seria
MATT_FACE = blob([(18, 20), (50, 16), (82, 20), (84, 70), (82, 108), (66, 116), (34, 116), (18, 108), (16, 70)])
CHARS['matt-fischer'] = {
    'body': 'delgado', 'pal': pal('#5a3a26', '#b88a5a', skin_d='#9a6e44', crown='#e8c860', crown_d='#b89030'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 104, 'face_front': MATT_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': [L(outline([(18, 30), (18, 0), (82, 0), (82, 30)]), 'mid', 'b'),
              L(outline([(20, 8), (16, -16, 1), (28, -6), (32, -24, 1), (42, -8), (50, -28, 1), (58, -8), (68, -24, 1), (72, -6), (84, -16, 1), (80, 8)]), 'crown', 'f', ln=True),
              L(outline([(60, -6), (70, -22, 1), (74, -4), (82, -14, 1), (80, 6)]), 'crown_d', 'f', False),
              L([(50, 64), (50, 92)], 'skin_d', 'f', False, False, 1.8), L([(42, 94), (58, 94)], 'skin_d', 'f', False, False, 1.4)]
             + white_eyes(74, 14, 5.4, 4.4, 1.4) + rect_glasses('front', 74),
    'side': [L(outline([(40, 112), (16, 104), (10, 60), (12, 0), (60, -2), (84, 10), (90, 50), (92, 100), (80, 116), (60, 118)]), 'skin'),
             L(outline([(12, 60), (12, 4), (44, 0), (36, 30), (24, 70)]), 'mid', 'b'),
             L(outline([(14, 6), (14, -14, 1), (26, -4), (34, -22, 1), (44, -6), (56, -24, 1), (62, -6), (74, -18, 1), (78, 6)]), 'crown', 'f', ln=True)]
            + side_eye(74) + rect_glasses('side', 74),
    'back': [L(outline([(18, 100), (16, 0), (84, 0), (82, 100), (50, 106)]), 'mid'),
             L(outline([(56, 4), (84, 4), (82, 98), (60, 104)]), 'deep', 'b', False),
             L(outline([(20, 8), (16, -16, 1), (28, -6), (32, -24, 1), (42, -8), (50, -28, 1), (58, -8), (68, -24, 1), (72, -6), (84, -16, 1), (80, 8)]), 'crown', 'f', ln=True)],
}
# Hank Tennyson: pelo azul acero de pinchos grandes hacia arriba y atrás; unas gafas redondas de aviador amarillas con los
# cristales verde oscuro sobre los ojos, nariz larga y una sonrisa enorme de dientes
CHARS['hank-tennyson'] = {
    'body': 'normal', 'pal': pal('#5a7ab8', '#f8c088', shade='#3e5a8e', frame='#e0a020', lens='#2a4a40'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': (56, 50)},
    'front': [L(outline([(14, 64), (8, 46), (-6, 40, 1), (8, 32), (2, 14, 1), (18, 14), (16, -6, 1), (30, 4), (36, -16, 1), (46, 0), (58, -14, 1), (62, 4), (78, -6, 1),
                         (78, 12), (96, 10, 1), (88, 26), (102, 36, 1), (90, 42), (86, 64), (78, 58), (22, 58)])),
              L(outline([(58, 0), (76, -4, 1), (78, 14), (94, 12, 1), (88, 28), (98, 36, 1), (88, 44), (84, 60), (72, 30)]), 'shade', 'b', False),
              L(outline([(14, 68), (50, 64), (86, 68), (86, 84), (60, 84), (50, 78), (40, 84), (14, 84)]), 'frame', 'f', ln=True),
              L(ell(33, 75, 8.4, 7.6), 'frame', 'f', ln=True), L(ell(67, 75, 8.4, 7.6), 'frame', 'f', ln=True),
              L(ell(33, 75, 6, 5.4), 'lens', 'f', False), L(ell(67, 75, 6, 5.4), 'lens', 'f', False),
              L(ell(31, 73, 2, 1.4), (120, 160, 150, 255), 'f', False), L(ell(65, 73, 2, 1.4), (120, 160, 150, 255), 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-4, 60, 1), (10, 48), (-6, 30, 1), (14, 24), (8, 2, 1), (28, 10), (32, -12, 1), (46, 4), (56, -16, 1), (64, 6),
                        (82, 0, 1), (84, 18), (92, 32), (78, 42), (62, 46), (52, 62), (50, 80)])),
             L(outline([(12, 40), (34, 44), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(48, 68), (82, 68), (82, 82), (50, 80)]), 'frame', 'f', ln=True), L(ell(88, 75, 4.6, 7.4), 'frame', 'f', ln=True),
             L(ell(89, 75, 3, 5.4), 'lens', 'f', False)],
    'back': [L(outline([(14, 80), (8, 46), (-6, 40, 1), (8, 32), (2, 14, 1), (18, 14), (16, -6, 1), (30, 4), (36, -16, 1), (46, 0), (58, -14, 1), (62, 4), (78, -6, 1),
                        (78, 12), (96, 10, 1), (88, 26), (102, 36, 1), (90, 42), (86, 80), (66, 88), (50, 98, 1), (34, 88)])),
             L(outline([(56, 2), (84, 16), (90, 46), (84, 78), (62, 88)]), 'shade', 'b', False),
             L(quad((10, 70), (50, 66), (90, 70)), 'frame', 'f', False, False, 3.4)],
}
# Dolph Hensen: piel morena; melena rubia clara despeinada que le tapa la frente en mechones en punta y le cae por los lados
# hasta la mandíbula, abierta en puntas en la nuca; ojos verdes y la boca seria
CHARS['dolph-hensen'] = {
    'body': 'normal', 'pal': pal('#f4dc9a', '#a87048', iris='#2a8a6a', shade='#d8b070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 98, 1), (6, 70), (2, 40), (16, 12), (50, 0), (84, 12), (98, 40), (96, 70), (98, 98, 1), (86, 86), (84, 64), (16, 64), (14, 86)])),
              L(outline([(60, 4), (86, 16), (98, 44), (94, 90), (86, 82), (80, 44)]), 'shade', 'b', False),
              L(outline([(8, 80, 1), (10, 46), (24, 26), (50, 18), (76, 26), (90, 46), (92, 80, 1), (84, 62), (76, 74, 1), (70, 56), (62, 70, 1), (56, 54), (48, 76, 1),
                         (42, 54), (34, 68, 1), (28, 54), (18, 70, 1)]), 'mid', 'f'),
              L(outline([(56, 22), (78, 30), (90, 50), (82, 62), (70, 44)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 70), (52, 92), (40, 98), (28, 108, 1), (22, 94), (8, 100, 1), (6, 72), (6, 36), (20, 10), (50, 0), (78, 8), (94, 28), (96, 52),
                        (92, 66, 1), (84, 50), (70, 48), (60, 52)])),
             L(outline([(8, 40), (32, 40), (46, 76), (40, 96), (22, 94), (8, 74)]), 'shade', 'b', False)],
    'back': [L(outline([(4, 98, 1), (6, 70), (2, 40), (16, 12), (50, 0), (84, 12), (98, 40), (96, 70), (98, 98, 1), (80, 92), (70, 104, 1), (60, 92), (50, 106, 1),
                        (40, 92), (30, 104, 1), (20, 92)])),
             L(outline([(56, 4), (86, 18), (98, 50), (94, 90), (70, 96), (64, 50)]), 'shade', 'b', False)],
}
# Hamilton Reith: melena verde hierba lisa y larga hasta los hombros, despeinada en mechones en punta, con un flequillo
# largo que le cae en pico entre los ojos; piel clara y ojos turquesa rasgados
CHARS['hamilton-reith'] = {
    'body': 'delgado', 'pal': pal('#8aa83a', '#fce4d0', iris='#2a9aa0', shade='#6a8428'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(-6, 112, 1), (0, 80), (-10, 70, 1), (0, 56), (0, 30), (16, 6), (50, -4), (84, 6), (100, 30), (100, 56), (110, 70, 1), (100, 80), (106, 112, 1),
                         (88, 100), (84, 66), (16, 66), (12, 100)])),
              L(outline([(60, 2), (86, 14), (100, 40), (100, 90), (88, 98), (80, 50)]), 'shade', 'b', False),
              L(outline([(8, 70, 1), (12, 40), (26, 22), (50, 16), (74, 22), (88, 40), (92, 70, 1), (84, 56), (74, 62), (62, 56), (52, 80, 1), (46, 58), (34, 54), (24, 62),
                         (16, 58)]), 'mid', 'f'),
              L(outline([(56, 22), (78, 30), (88, 50), (78, 56), (68, 42)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 70), (54, 100), (44, 112, 1), (36, 100), (24, 116, 1), (16, 100), (2, 108, 1), (2, 80), (-8, 64, 1), (2, 54), (4, 30), (18, 8), (48, -2), (76, 6),
                        (94, 26), (96, 50), (90, 64, 1), (82, 50), (70, 48), (62, 52)])),
             L(outline([(6, 40), (32, 40), (46, 80), (40, 104), (16, 104), (6, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(-6, 112, 1), (0, 80), (-10, 70, 1), (0, 56), (0, 30), (16, 6), (50, -4), (84, 6), (100, 30), (100, 56), (110, 70, 1), (100, 80), (106, 112, 1),
                        (80, 108), (66, 120, 1), (56, 106), (44, 120, 1), (34, 106), (20, 108)])),
             L(outline([(58, 2), (86, 14), (100, 40), (100, 100), (70, 110), (66, 50)]), 'shade', 'b', False)],
}
# Joe Dawes: cara ancha y cuadrada con orejas grandes; pelo azul petróleo en un tupé ondulado arriba, las sienes rapadas y
# unas patillas que le bajan por la mandíbula; ojos negros pequeños de enfado y la boca en una raya
CHARS['joe-dawes'] = {
    'body': 'corpulento', 'pal': pal('#1e5a6e', '#e0946a', shade='#164454', light='#3a7a8e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(18, 48), (16, 20), (10, 6), (24, -4), (40, 2), (50, -6), (64, 0), (78, -6), (92, 6), (84, 20), (82, 48), (70, 30), (50, 34), (30, 30)])),
              L(outline([(60, 0), (78, -4), (90, 8), (82, 30), (70, 24)]), 'shade', 'b', False),
              L(outline([(16, 8), (30, 0), (40, 8), (28, 12)]), 'light', 'b', False), L(outline([(56, 4), (70, 0), (74, 10), (60, 12)]), 'light', 'b', False),
              L(outline([(10, 70), (16, 66), (20, 92), (14, 96)]), 'mid', 'f'), L(outline([(90, 70), (84, 66), (80, 92), (86, 96)]), 'mid', 'f'),
              L(outline([(24, 74), (36, 72), (42, 76), (34, 80)]), OUTC, 'f', False), L(outline([(76, 74), (64, 72), (58, 76), (66, 80)]), OUTC, 'f', False),
              L([(24, 66), (40, 70)], OUTC, 'f', False, False, 2.2), L([(76, 66), (60, 70)], OUTC, 'f', False, False, 2.2)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (20, 6), (44, -6), (70, -6), (92, 6), (100, 22), (90, 30), (76, 40), (62, 46), (52, 62), (50, 80)])),
             L(outline([(12, 36), (36, 40), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(54, 62), (62, 66), (74, 96), (80, 106), (70, 106), (56, 80)]), 'mid', 'f', ln=True),
             L(outline([(80, 74), (88, 72), (90, 78), (82, 80)]), OUTC, 'f', False)],
    'back': [L(outline([(16, 90), (12, 30), (20, 6), (50, -6), (80, 6), (88, 30), (84, 90), (50, 96)])),
             L(outline([(56, 0), (82, 12), (88, 50), (84, 88), (62, 94)]), 'shade', 'b', False)],
}
# Quincy Horace (portero suplente): media melena rubia lisa en forma de casco hasta la mandíbula, con una visera verde
# oscuro en la frente; ojos azules y sonrisa
CHARS['quincy-horace'] = {
    'body': 'normal', 'pal': pal('#e0d050', '#e8a870', iris='#3a7ab0', shade='#b8a830', visor='#2a3a2a', visor_d='#1a261a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 98), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (94, 98), (84, 96), (84, 66), (16, 66), (16, 96)])),
              L(outline([(60, 4), (86, 16), (98, 44), (94, 96), (86, 94), (80, 50)]), 'shade', 'b', False),
              L(outline([(14, 58), (14, 44), (50, 40), (86, 44), (86, 58), (96, 66), (50, 70), (4, 66)]), 'visor', 'f', ln=True),
              L(outline([(50, 42), (86, 46), (86, 58), (96, 66), (60, 68)]), 'visor_d', 'f', False),
              L(outline([(16, 72), (24, 70), (22, 96), (16, 100, 1)]), 'mid', 'f'), L(outline([(84, 72), (76, 70), (78, 96), (84, 100, 1)]), 'mid', 'f')],
    'side': [L(outline([(56, 70), (54, 100), (36, 104), (8, 100), (4, 40), (18, 10), (50, -2), (78, 8), (94, 28), (94, 50), (80, 48), (66, 52)])),
             L(outline([(6, 60), (40, 60), (50, 96), (8, 98)]), 'shade', 'b', False),
             L(outline([(14, 50), (60, 44), (90, 48), (110, 58), (90, 62), (40, 60)]), 'visor', 'f', ln=True)],
    'back': [L(outline([(6, 98), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (94, 98), (50, 100)])),
             L(outline([(4, 62), (50, 54), (96, 62), (94, 98), (50, 100), (6, 98)]), 'shade', 'b', False),
             L(quad((4, 50), (50, 44), (96, 50)), 'visor', 'f', False, False, 3)],
}
# Holly Summers: pelo castaño ceniza liso con un flequillo largo que le tapa el ojo izquierdo y dos mechones largos que le
# caen por delante de las orejas hasta los hombros; piel clara, un ojo verde y la boca seria
CHARS['holly-summers'] = {
    'body': 'normal', 'pal': pal('#8a7a60', '#fce8d4', iris='#3a8a7a', shade='#6a5c48'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 36), (20, 10), (50, 0), (80, 10), (92, 36), (88, 70), (80, 64), (20, 64)])),
              L(outline([(60, 4), (84, 16), (92, 42), (86, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(14, 60), (16, 38), (30, 22), (52, 16), (74, 22), (88, 40), (90, 66), (86, 86, 1), (76, 74), (66, 60), (56, 50), (40, 46), (24, 52)]), 'mid', 'f', ln=True),
              L(outline([(58, 22), (82, 34), (88, 60), (84, 80), (74, 62)]), 'shade', 'f', False),
              L(outline([(14, 60), (22, 62), (22, 90), (18, 112, 1), (12, 90)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 34), (24, 12), (52, 2), (76, 8), (92, 26), (92, 50), (86, 70, 1), (78, 50), (64, 48), (54, 62), (50, 80)])),
             L(outline([(14, 40), (34, 44), (42, 80), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(48, 60), (56, 62), (58, 96), (52, 114, 1), (46, 92)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 84), (8, 36), (20, 10), (50, 0), (80, 10), (92, 36), (88, 84), (76, 96, 1), (66, 86), (50, 92), (34, 86), (24, 96, 1)])),
             L(outline([(56, 4), (84, 16), (92, 50), (86, 82), (64, 88)]), 'shade', 'b', False)],
}
# Derek Rabson: pelo castaño arena revuelto y peinado a un lado en mechones gruesos que le caen por la frente; perilla,
# ojos de sueño con ojeras y los dientes apretados
CHARS['derek-rabson'] = {
    'body': 'normal', 'pal': pal('#a08a4a', '#f4c090', shade='#7a6834', light='#c0aa6a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'eye_y': 76, 'hairline': False},
    'front': messy('front', 9, 9, seed=302, rx=50, ry=40, lo=68)
             + [L(outline([(10, 70, 1), (14, 44), (28, 28), (52, 22), (74, 26), (88, 40), (94, 52, 1), (82, 52), (70, 46), (54, 46), (36, 54), (24, 66, 1), (20, 56)]), 'mid', 'f'),
                L(outline([(30, 34), (54, 28), (72, 34), (50, 38)]), 'light', 'f', False),
                L(outline([(44, 104), (50, 100), (56, 104), (50, 110, 1)]), 'mid', 'f', ln=True)]
             + white_eyes(76, 14, 5.4, 4.6, 1.6, lid=1.5),
    'side': messy('side', 10, 8, seed=302, rx=46, ry=40, nape=92, sweep=-0.3)
            + [spk((56, 30), (88, 40), (94, 60), 4, z='f', light_left=False), L(outline([(84, 100), (92, 100), (88, 108, 1)]), 'mid', 'f', ln=True)]
            + side_eye(76, lid=1.5),
    'back': messy('back', 9, 9, seed=302, rx=50, ry=40, nape=92),
}
# Barack Daniels: grandullón de cabeza alta y cuadrada; pelo azul marino muy corto con entradas, y una barba fina del mismo
# color que le recorre la mandíbula; ojos blancos medio cerrados, nariz recta larga y labios gruesos
BARACK_FACE = blob([(14, 30), (50, 26), (86, 30), (88, 70), (86, 108), (68, 118), (32, 118), (14, 108), (12, 70)])
CHARS['barack-daniels'] = {
    'body': 'corpulento', 'pal': pal('#2a2e5a', '#c88a50', skin_d='#a86e38', lip='#a8642a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': BARACK_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': [L(outline([(14, 60), (12, 10), (24, -4), (50, -8), (76, -4), (88, 10), (86, 60), (80, 40), (64, 36), (56, 44, 1), (50, 34), (44, 44, 1), (36, 36), (20, 40)])),
              L(outline([(60, -4), (80, 2), (88, 30), (82, 46), (74, 20)]), 'shade', 'b', False),
              L(outline([(12, 70), (16, 98), (30, 116), (50, 120), (70, 116), (84, 98), (88, 70), (84, 100), (70, 112), (50, 116), (30, 112), (16, 100)]), 'mid', 'f'),
              L([(50, 64), (50, 92)], 'skin_d', 'f', False, False, 2.0), L([(44, 92), (56, 92)], 'skin_d', 'f', False, False, 1.4),
              L(outline([(34, 100), (66, 100), (64, 108), (36, 108)]), 'lip', 'f', ln=True), L([(36, 104), (64, 104)], OUTC, 'f', False, False, 1.0)]
             + white_eyes(72, 15, 5.4, 4, 1.4, lid=1),
    'side': [L(outline([(38, 112), (14, 106), (8, 60), (10, 6), (40, -8), (72, -6), (88, 10), (92, 50), (94, 100), (82, 116), (60, 120)]), 'skin'),
             L(outline([(10, 70), (8, 10), (40, -8), (70, -6), (84, 6), (60, 10), (36, 30), (28, 60), (30, 96), (40, 112), (20, 108)]), 'mid', 'b'),
             L(outline([(40, 106), (60, 118), (80, 116), (90, 104), (82, 108), (60, 112)]), 'mid', 'f'),
             L(outline([(86, 98), (96, 98), (96, 108), (86, 108)]), 'lip', 'f', ln=True)] + side_eye(72, lid=1),
    'back': [L(outline([(14, 100), (12, 10), (24, -4), (50, -8), (76, -4), (88, 10), (86, 100), (50, 106)])),
             L(outline([(56, -4), (80, 4), (88, 40), (86, 96), (62, 102)]), 'shade', 'b', False)],
}
# Bruce Marlin: pelo rubio dorado liso hasta el cuello, con unas gafas de aviador de cristales azules y montura crema
# subidas sobre la frente y mechones que le caen por la cara; ojos negros de enfado y media sonrisa
CHARS['bruce-marlin'] = {
    'body': 'normal', 'pal': pal('#e8b828', '#f8c890', iris='#1e1e1e', shade='#c09018', frame='#c8b098', lens='#3a5a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(6, 92), (4, 40), (16, 10), (50, -2), (84, 10), (96, 40), (94, 92), (84, 88), (84, 64), (16, 64), (16, 88)])),
              L(outline([(60, 4), (86, 16), (96, 44), (92, 88), (84, 84), (80, 44)]), 'shade', 'b', False),
              L(outline([(12, 66, 1), (14, 40), (28, 26), (50, 22), (72, 26), (86, 40), (88, 66, 1), (82, 54), (72, 62, 1), (64, 52), (54, 74, 1), (50, 54), (40, 64, 1),
                         (34, 54), (24, 62, 1), (18, 54)]), 'mid', 'f'),
              L(outline([(12, 44), (50, 40), (88, 44), (88, 56), (60, 58), (50, 52), (40, 58), (12, 56)]), 'frame', 'f', ln=True),
              L(ell(32, 49, 10, 6.6), 'frame', 'f', ln=True), L(ell(68, 49, 10, 6.6), 'frame', 'f', ln=True),
              L(ell(32, 49, 7.6, 4.8), 'lens', 'f', False), L(ell(68, 49, 7.6, 4.8), 'lens', 'f', False),
              L(outline([(16, 64), (24, 66), (22, 92), (16, 98, 1)]), 'mid', 'f'), L(outline([(84, 64), (76, 66), (78, 92), (84, 98, 1)]), 'mid', 'f')],
    'side': [L(outline([(56, 70), (54, 96), (40, 100), (22, 104, 1), (16, 96), (6, 98, 1), (4, 40), (18, 10), (50, -2), (78, 8), (94, 28), (94, 50), (80, 48), (66, 52)])),
             L(outline([(6, 50), (34, 50), (48, 90), (20, 100), (6, 90)]), 'shade', 'b', False),
             L(outline([(40, 44), (84, 42), (92, 48), (86, 56), (42, 56)]), 'frame', 'f', ln=True), L(ell(88, 49, 4.4, 6), 'lens', 'f', ln=True)],
    'back': [L(outline([(6, 92), (4, 40), (16, 10), (50, -2), (84, 10), (96, 40), (94, 92), (82, 98, 1), (72, 90), (62, 100, 1), (50, 90), (38, 100, 1), (28, 90),
                        (18, 98, 1)])),
             L(outline([(6, 60), (50, 54), (94, 60), (94, 92), (50, 96), (6, 92)]), 'shade', 'b', False),
             L(quad((4, 48), (50, 42), (96, 48)), 'frame', 'f', False, False, 3)],
}
