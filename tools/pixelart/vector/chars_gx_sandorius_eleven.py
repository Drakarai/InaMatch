"""Los Sílice (Sandorius Eleven, gx-sandorius-eleven): alienígenas del planeta desértico Sandorius, con sus modelos 3D de
Inazuma Eleven GO Galaxy como referencia (busto de frente, perfil y espalda).

Tienen la cabeza entera de piel (pardo, rojizo o anaranjado), con placas claras en el cráneo, orejas pequeñas en punta y un
hocico pálido en forma de pico; cada uno lleva su mechón, cresta o melena. La cabeza se dibuja con la cara del tamaño de
todo el cráneo (face_front / face_side) y encima las placas y el hocico.
"""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)

# cráneo de frente, de perfil (mirando a la derecha, con el hocico delante) y de espaldas
SKULL_F = [(14, 72), (12, 42), (24, 16), (50, 6), (76, 16), (88, 42), (86, 72), (80, 94), (64, 108), (50, 112), (36, 108), (20, 94)]
SKULL_S = [(40, 108), (18, 98), (8, 70), (10, 38), (26, 14), (54, 6), (78, 16), (90, 40), (92, 64), (96, 80), (98, 96), (86, 106), (64, 110)]
SKULL_B = [(14, 72), (12, 42), (24, 16), (50, 6), (76, 16), (88, 42), (86, 72), (78, 96), (62, 108), (38, 108), (22, 96)]


def muzzle_f(top=82, w=22, bot=108, c='muz'):
    """Hocico pálido de frente: ancho bajo los ojos y en punta redondeada hacia la barbilla."""
    return L(outline([(50 - w, top), (50, top - 3), (50 + w, top), (50 + w * 0.8, top + 12), (50 + w * 0.4, bot - 4), (50, bot), (50 - w * 0.4, bot - 4),
                      (50 - w * 0.8, top + 12)]), c, 'f', ln=True)


def muzzle_s(top=80, bot=106, c='muz'):
    return L(outline([(74, top), (96, top + 2), (100, top + 14), (96, bot - 4), (84, bot), (72, bot - 6), (70, top + 10)]), c, 'f', ln=True)


def plates_f(c='plate', y0=10, y1=44):
    """Placas claras del cráneo: una grande en medio y dos a los lados."""
    m = (y0 + y1) / 2
    return [L(outline([(50, y0), (60, m - 6), (56, y1), (44, y1), (40, m - 6)]), c, 'f', False),
            L(outline([(34, y0 + 8), (40, m), (34, y1 - 4), (28, m)]), c, 'f', False),
            L(outline([(66, y0 + 8), (72, m), (66, y1 - 4), (60, m)]), c, 'f', False)]


def plates_s(c='plate'):
    return [L(outline([(40, 12), (62, 10), (70, 24), (56, 34), (40, 28)]), c, 'f', False), L(outline([(66, 16), (80, 24), (78, 36), (68, 30)]), c, 'f', False)]


def ear_f(dx=0, c='skin_d'):
    """Orejas pequeñas en punta hacia arriba a los lados."""
    return [L(outline([(16 - dx, 50), (2 - dx, 30, 1), (14 - dx, 62)]), c, 'b', ln=True), L(outline([(84 + dx, 50), (98 + dx, 30, 1), (86 + dx, 62)]), c, 'b', ln=True)]


def ear_s(c='skin_d'):
    return L(outline([(40, 46), (30, 26, 1), (34, 50), (46, 62)]), c, 'f', ln=True)


def head(skin, plate='#ecd8b4', muz='#f0e6cc', iris='#1e1e1e', **kw):
    return pal(skin, skin, iris=iris, plate=plate, muz=muz, **kw)


FACE = {'hairline': False, 'ears': False, 'face_front': outline(SKULL_F), 'face_side': outline(SKULL_S), 'eye_sep': 16, 'eye_y': 72}

# ------------------------------------------------------------------ B'adaen (Badai Jaran, portero)
# Cabeza pardo claro alargada con placas crema en lo alto, hocico largo pálido y una correa marrón oscuro que le cruza la
# cara como un parche: en el ojo izquierdo, una lente blanca en espiral; el derecho, azul
CHARS['b-adaen'] = {
    'body': 'normal', 'pal': head('#b08a68', iris='#3a8ac8', strap='#4a3022', lens='#f4f0f0'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 102},
    'front': plates_f(y0=4, y1=40) + [
        muzzle_f(84, 20, 112),
        L(outline([(8, 58), (50, 64), (92, 56), (92, 64), (50, 72), (8, 66)]), 'strap', 'f', False),
        L(ell(36, 72, 9, 9), 'strap', 'f', ln=True), L(ell(36, 72, 6.5, 6.5), 'lens', 'f', ln=True),
        L(ell(36, 72, 3, 3) + [ell(36, 72, 3, 3)[0]], OUTC, 'f', False, False, 1.0)],
    'side': plates_s() + [muzzle_s(82, 108), L(outline([(6, 56), (60, 60), (96, 62), (96, 70), (60, 68), (6, 64)]), 'strap', 'f', False),
                          L(ell(88, 70, 6, 7), 'strap', 'f', ln=True), L(ell(89, 70, 4, 5), 'lens', 'f', ln=True), ear_s()],
    'back': [L(outline([(10, 56), (50, 62), (90, 56), (90, 64), (50, 70), (10, 64)]), 'strap', 'b', False),
             L(outline([(40, 10), (60, 10), (64, 30), (36, 30)]), 'plate', 'b', False)],
}

# ------------------------------------------------------------------ G'ob (Gobila Mongo)
# Cabeza roja anaranjada con manchas crema en el cráneo, un rizo marrón oscuro en lo alto, orejas en punta y un hocico ancho
# pálido; cejas fruncidas
CHARS['g-ob'] = {
    'body': 'normal', 'pal': head('#d06a48', plate='#f4e0c8', muz='#f4ecc8', tuft='#4a3428', tuft_l='#7a5a48'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100},
    'front': ear_f() + [L(outline([(50, 10), (44, -6), (48, -22), (62, -26), (70, -16), (64, -6), (58, -14), (54, -10), (56, 8)]), 'tuft', 'b', ln=True)]
    + plates_f(y0=12, y1=46) + [muzzle_f(80, 24, 108), L([(44, 98), (56, 98)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(40, 10), (30, -6), (36, -22), (52, -24), (56, -12), (46, -8), (50, 8)]), 'tuft', 'b', ln=True)] + plates_s() + [muzzle_s(), ear_s()],
    'back': ear_f() + [L(outline([(50, 10), (44, -6), (48, -22), (62, -26), (70, -16), (64, -6), (58, -14), (54, -10), (56, 8)]), 'tuft', 'b', ln=True)],
}

# ------------------------------------------------------------------ A'ddah (Duff Natter)
# Grandullón de cabeza redonda pardo, con placas crema en el cráneo, ojos redondos de pasmo y un hocico pálido enorme y
# abombado; el cuello, ancho
CHARS['a-ddah'] = {
    'body': 'corpulento', 'pal': head('#a07a58', plate='#ecdcbc', muz='#f0e6d0'),
    'face': {**FACE, 'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 102,
             'face_front': outline([(12, 76), (10, 44), (22, 18), (50, 8), (78, 18), (90, 44), (88, 76), (84, 98), (66, 112), (50, 114), (34, 112), (16, 98)])},
    'front': plates_f(y0=10, y1=42) + [L(outline([(26, 82), (50, 78), (74, 82), (78, 96), (68, 110), (50, 114), (32, 110), (22, 96)]), 'muz', 'f', ln=True),
                                       L(quad((38, 100), (50, 96), (62, 100)), OUTC, 'f', False, False, 1.2)],
    'side': plates_s() + [L(outline([(70, 78), (98, 80), (104, 94), (96, 108), (78, 110), (68, 98)]), 'muz', 'f', ln=True), ear_s()],
    'back': [L(outline([(40, 12), (60, 12), (62, 30), (38, 30)]), 'plate', 'b', False)],
}

# ------------------------------------------------------------------ R'adji (Regi Stanin)
# Cráneo con un ala ancha clara, como un sombrero, que se abre a los lados en dos picos, con dibujo crema; un mechón marrón
# oscuro erizado arriba, hocico pálido y ojos fruncidos
CHARS['r-adji'] = {
    'body': 'normal', 'pal': head('#b88a62', plate='#f0dcb8', muz='#f2e6cc', brim='#d8b48a', brim_d='#b08a64', tuft='#3a2a22'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102},
    'front': [L(outline([(46, 12), (36, -6), (42, -2), (40, -20), (50, -8), (56, -24), (60, -6), (68, -16), (62, 8)]), 'tuft', 'b', ln=True),
              L(outline([(-6, 54, 1), (6, 28), (24, 12), (50, 6), (76, 12), (94, 28), (106, 54, 1), (84, 50), (70, 44), (50, 46), (30, 44), (16, 50)]), 'brim', 'f', ln=True),
              L(outline([(50, 12), (64, 22), (60, 38), (40, 38), (36, 22)]), 'plate', 'f', False),
              L(outline([(56, 10), (76, 14), (94, 30), (100, 48), (84, 46), (72, 30)]), 'brim_d', 'f', False),
              muzzle_f(80, 20, 108)],
    'side': [L(outline([(42, 10), (32, -6), (38, -2), (34, -20), (46, -8), (50, -22), (54, -4), (52, 8)]), 'tuft', 'b', ln=True),
             L(outline([(4, 46), (10, 22), (30, 8), (58, 4), (80, 14), (94, 34, 1), (74, 34), (50, 30), (20, 40)]), 'brim', 'f', ln=True),
             L(outline([(40, 10), (60, 8), (64, 22), (44, 26)]), 'plate', 'f', False), muzzle_s(), ear_s()],
    'back': [L(outline([(46, 12), (36, -6), (42, -2), (40, -20), (50, -8), (56, -24), (60, -6), (68, -16), (62, 8)]), 'tuft', 'b', ln=True),
             L(outline([(-6, 54, 1), (6, 28), (24, 12), (50, 6), (76, 12), (94, 28), (106, 54, 1), (84, 50), (70, 46), (50, 48), (30, 46), (16, 50)]), 'brim', 'f', ln=True)],
}

# ------------------------------------------------------------------ A'kra (Takla Marker)
# Cabeza roja anaranjada muy alargada, como de jirafa, con placas crema arriba, orejas en punta hacia los lados, hocico
# largo rosado y ojos redondos saltones
CHARS['a-kra'] = {
    'body': 'normal', 'pal': head('#d06848', plate='#f4dcc0', muz='#f09a80'),
    'face': {**FACE, 'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 106, 'eye_sep': 18,
             'face_front': outline([(18, 74), (16, 30), (26, 2), (50, -8), (74, 2), (84, 30), (82, 74), (76, 96), (62, 112), (50, 116), (38, 112), (24, 96)]),
             'face_side': outline([(40, 108), (18, 96), (10, 66), (14, 24), (30, -2), (56, -8), (78, 6), (88, 32), (92, 60), (98, 80), (100, 98), (88, 110), (64, 112)])},
    'front': [L(outline([(18, 48), (-2, 36, 1), (16, 58)]), 'skin', 'b', ln=True), L(outline([(82, 48), (102, 36, 1), (84, 58)]), 'skin', 'b', ln=True)]
    + plates_f(y0=-2, y1=36) + [L(outline([(36, 84), (50, 80), (64, 84), (62, 104), (50, 116), (38, 104)]), 'muz', 'f', ln=True)],
    'side': [L(outline([(36, 44), (14, 34, 1), (32, 54)]), 'skin', 'f', ln=True)] + plates_s() + [muzzle_s(82, 110)],
    'back': [L(outline([(18, 48), (-2, 36, 1), (16, 58)]), 'skin', 'b', ln=True), L(outline([(82, 48), (102, 36, 1), (84, 58)]), 'skin', 'b', ln=True)],
}

# ------------------------------------------------------------------ N'ameeb (Namiba Mib)
# Cabeza anaranjada redonda con dos lóbulos a los lados de la cara, placa clara en la frente y un lazo rojo pardo en lo
# alto, sobre un tallito; ojos redondos grandes y dientes de sierra blancos
CHARS['n-ameeb'] = {
    'body': 'normal', 'pal': head('#e8a060', plate='#f6e0c8', muz='#f6ecd8', bow='#9a3a24', bow_d='#6a2414', stem='#8a9a9a'),
    'face': {**FACE, 'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'eye_sep': 18},
    'front': [L(outline([(10, 62), (-6, 50), (-2, 74), (14, 82)]), 'skin', 'b', ln=True), L(outline([(90, 62), (106, 50), (102, 74), (86, 82)]), 'skin', 'b', ln=True),
              L([(50, 8), (50, -6)], 'stem', 'b', False, False, 2.4),
              L(outline([(50, -8), (30, -20), (14, -22, 1), (24, -10), (40, -4)]), 'bow', 'b', ln=True),
              L(outline([(50, -8), (70, -20), (86, -22, 1), (76, -10), (60, -4)]), 'bow', 'b', ln=True),
              L(outline([(36, 12), (64, 12), (60, 40), (40, 40)]), 'plate', 'f', False),
              L(outline([(30, 86), (70, 86), (66, 96), (34, 96)]), WHITE, 'f', ln=True),
              L([(30, 86), (36, 92), (42, 86), (48, 92), (54, 86), (60, 92), (66, 86)], OUTC, 'f', False, False, 1.0)],
    'side': [L([(46, 8), (46, -6)], 'stem', 'b', False, False, 2.4), L(outline([(46, -8), (30, -16), (20, -18, 1), (32, -6)]), 'bow', 'b', ln=True),
             L(outline([(40, 12), (60, 10), (60, 30), (42, 32)]), 'plate', 'f', False),
             L(outline([(78, 86), (98, 86), (96, 96), (80, 96)]), WHITE, 'f', ln=True), ear_s()],
    'back': [L([(50, 8), (50, -6)], 'stem', 'b', False, False, 2.4),
             L(outline([(50, -8), (30, -20), (14, -22, 1), (24, -10), (40, -4)]), 'bow', 'b', ln=True),
             L(outline([(50, -8), (70, -20), (86, -22, 1), (76, -10), (60, -4)]), 'bow', 'b', ln=True)],
}

# ------------------------------------------------------------------ K'aran Uogu (Kazerma Worg)
# Cara roja anaranjada con placas crema y hocico pálido, enmarcada por una melena enorme gris parda, esponjosa, como de león
_mane_f = [(6, 100), (-10, 84), (-14, 60), (-8, 34), (6, 12), (24, -2), (50, -8), (76, -2), (94, 12), (108, 34), (114, 60), (110, 84), (94, 100), (84, 88), (88, 60),
           (80, 30), (50, 18), (20, 30), (12, 60), (16, 88)]
CHARS['k-aran-uogu'] = {
    'body': 'normal', 'pal': head('#c8664a', plate='#f0d8bc', muz='#f2e8d4', mane='#a89888', mane_d='#7e6e64'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102},
    'front': [L(outline(_mane_f), 'mane', 'b'), L(outline([(60, -4), (94, 12), (108, 34), (114, 60), (110, 84), (96, 98), (88, 60), (80, 30)]), 'mane_d', 'b', False)]
    + plates_f(y0=20, y1=48) + [muzzle_f(82, 20, 108)],
    'side': [L(outline([(60, 2), (30, -8), (0, 4), (-20, 30), (-24, 60), (-18, 90), (0, 106), (24, 100), (36, 70), (40, 40), (60, 22)]), 'mane', 'b'),
             L(outline([(-18, 40), (10, 40), (16, 90), (-6, 100)]), 'mane_d', 'b', False)] + plates_s() + [muzzle_s()],
    'back': [L(outline([(4, 100), (-12, 80), (-14, 50), (-4, 22), (20, 2), (50, -6), (80, 2), (104, 22), (114, 50), (112, 80), (96, 100), (70, 112), (30, 112)]), 'mane'),
             L(outline([(54, -4), (80, 2), (104, 22), (114, 50), (112, 80), (96, 100), (64, 110)]), 'mane_d', 'b', False)],
}

# ------------------------------------------------------------------ K'al (Gala Hariza)
# Cabeza parda tostada con placas crema en el cráneo, orejas en punta hacia arriba y una sonrisa enorme de dientes en el
# hocico pálido; ojos fruncidos
CHARS['k-al'] = {
    'body': 'normal', 'pal': head('#c08858', plate='#f0dcbc', muz='#f2e6c8'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none'},
    'front': [L(outline([(16, 48), (-2, 22, 1), (14, 62)]), 'skin', 'b', ln=True), L(outline([(84, 48), (102, 22, 1), (86, 62)]), 'skin', 'b', ln=True)]
    + plates_f(y0=6, y1=44) + [muzzle_f(80, 24, 108),
                               L(outline([(32, 88), (68, 88), (62, 100), (38, 100)]), WHITE, 'f', ln=True),
                               L([(38, 88), (38, 100)], OUTC, 'f', False, False, 0.8), L([(50, 88), (50, 100)], OUTC, 'f', False, False, 0.8),
                               L([(62, 88), (62, 100)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(38, 44), (26, 20, 1), (32, 48), (44, 60)]), 'skin_d', 'f', ln=True)] + plates_s() + [muzzle_s(),
                                                                                                         L(outline([(80, 88), (98, 88), (96, 98), (82, 98)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(16, 48), (-2, 22, 1), (14, 62)]), 'skin', 'b', ln=True), L(outline([(84, 48), (102, 22, 1), (86, 62)]), 'skin', 'b', ln=True)],
}

# ------------------------------------------------------------------ S'haha (Zaba Harler)
# Cabeza roja anaranjada con un ala en el cráneo que acaba en dos cuernos hacia arriba, hocico pálido con los dientes
# apretados y una coleta marrón oscuro larga que le sale de lo alto y ondea hacia atrás
CHARS['s-haha'] = {
    'body': 'normal', 'pal': head('#c86448', plate='#f0c8a8', muz='#f4ece0', tail='#4a3428', tail_l='#6a5040'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none'},
    'front': [L(outline([(54, 8), (64, -14), (84, -22), (104, -16), (92, -10), (74, -6), (62, 10)]), 'tail', 'b', ln=True),
              L(outline([(14, 40), (8, 12, 1), (24, 22), (50, 16), (76, 22), (92, 12, 1), (86, 40), (70, 34), (50, 36), (30, 34)]), 'plate', 'f', ln=True),
              muzzle_f(80, 22, 108), L(outline([(36, 90), (64, 90), (60, 98), (40, 98)]), WHITE, 'f', ln=True),
              L([(36, 94), (64, 94)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(36, 10), (20, -10), (-6, -18), (-30, -10, 1), (-8, -4), (14, 4), (28, 20)]), 'tail', 'b', ln=True),
             L(outline([(20, 30), (28, 8), (52, 4), (78, 12, 1), (66, 26), (40, 28)]), 'plate', 'f', ln=True), muzzle_s(),
             L(outline([(80, 90), (98, 90), (96, 98), (82, 98)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(50, 8), (36, -12), (10, -22), (-12, -16, 1), (8, -8), (30, 2), (44, 14)]), 'tail', 'f', ln=True),
             L(outline([(14, 40), (8, 12, 1), (24, 22), (50, 16), (76, 22), (92, 12, 1), (86, 40), (70, 34), (50, 36), (30, 34)]), 'plate', 'b', ln=True)],
}

# ------------------------------------------------------------------ S'harqiyah (Shar Qiyah)
# Cabeza anaranjada con una corona de placas en capas, como pétalos, y una cresta gris verdosa que sale de lo alto y se curva
# hacia atrás; hocico pálido y ojos tranquilos
CHARS['s-harqiyah'] = {
    'body': 'normal', 'pal': head('#e8a060', plate='#f6c890', muz='#f4ecd8', crest='#5a7a6a', crest_l='#7a9a8a'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 102},
    'front': [L(outline([(48, 14), (56, -10), (70, -22), (78, -18), (68, -4), (60, 16)]), 'crest', 'b', ln=True),
              L(outline([(10, 46), (14, 24), (30, 30), (36, 12), (50, 20), (64, 12), (70, 30), (86, 24), (90, 46), (70, 44), (50, 50), (30, 44)]), 'plate', 'f', ln=True),
              L(outline([(24, 52), (36, 44), (50, 52), (64, 44), (76, 52), (64, 56), (50, 60), (36, 56)]), 'plate', 'f', ln=True),
              muzzle_f(82, 20, 108)],
    'side': [L(outline([(44, 12), (40, -10), (22, -24), (8, -26, 1), (26, -14), (34, 4)]), 'crest', 'b', ln=True),
             L(outline([(16, 40), (22, 18), (40, 12), (60, 10), (80, 22), (88, 40), (68, 38), (44, 44)]), 'plate', 'f', ln=True), muzzle_s(), ear_s()],
    'back': [L(outline([(48, 14), (50, -6), (40, -20), (30, -22, 1), (44, -10), (56, 12)]), 'crest', 'f', ln=True)],
}

# ------------------------------------------------------------------ A'tac (Acker Tamal)
# Cabeza parda con placas puntiagudas y la coronilla crema, ojos rojo anaranjado afilados con dos marcas bajo los ojos, y
# una coleta larga granate atada arriba que le cae ondeando hacia un lado
CHARS['a-tac'] = {
    'body': 'normal', 'pal': head('#b89070', plate='#f0dcb8', muz='#f2e8d4', iris='#c84a1e', tail='#7a1e3a', tail_l='#a0304e'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102},
    'front': [L(outline([(50, 8), (40, -2), (44, -14), (58, -14), (62, -2)]), 'tail', 'b', ln=True),
              L(outline([(80, 70), (100, 74), (112, 84), (104, 96, 1), (106, 84), (96, 80), (82, 80)]), 'tail', 'f', ln=True),
              L(outline([(14, 50), (4, 34, 1), (16, 40), (22, 14), (36, 22), (50, 8), (64, 22), (78, 14), (84, 40), (96, 34, 1), (86, 50), (70, 40), (50, 44), (30, 40)]),
                'plate', 'f', ln=True),
              muzzle_f(82, 20, 108), L([(30, 78), (28, 86)], 'tail', 'f', False, False, 1.6), L([(70, 78), (72, 86)], 'tail', 'f', False, False, 1.6)],
    'side': [L(outline([(44, 6), (30, -10), (8, -14), (-16, 2), (-26, 30), (-22, 60), (-30, 80, 1), (-14, 64), (-8, 36), (8, 12), (30, 10)]), 'tail', 'b', ln=True),
             L(outline([(20, 30), (24, 12), (46, 4), (70, 10), (84, 28), (62, 30), (40, 34)]), 'plate', 'f', ln=True), muzzle_s(), ear_s()],
    'back': [L(outline([(50, 8), (40, -6), (52, -16), (66, -8), (60, 8)]), 'tail', 'f', ln=True),
             L(outline([(54, 2), (30, 10), (10, 30), (-6, 60), (-16, 84, 1), (4, 64), (20, 40), (44, 20)]), 'tail', 'f', ln=True)],
}

# ------------------------------------------------------------------ Zundar Zand (Zundal Zand)
# Cabeza beige muy pálida, alta y calva con arrugas en la frente, orejas en punta, un manojo de rastas grises que le sale de
# lo alto y un chal blanco lila enorme que le envuelve el cuello y los hombros
CHARS['zundar-zand'] = {
    'body': 'normal', 'pal': head('#e0c8a8', plate='#ece0cc', muz='#f2ead8', dread='#8a7a80', shawl='#e8e0ec', shawl_d='#b8a8c0'),
    'face': {**FACE, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102,
             'face_front': outline([(16, 74), (14, 30), (22, 4), (50, -6), (78, 4), (86, 30), (84, 74), (78, 96), (64, 108), (50, 112), (36, 108), (22, 96)]),
             'face_side': outline([(40, 108), (18, 96), (10, 66), (12, 26), (28, 0), (56, -6), (78, 8), (88, 34), (92, 62), (96, 80), (98, 96), (86, 106), (64, 110)])},
    'front': [L(outline([(16, 52), (2, 40, 1), (14, 64)]), 'skin', 'b', ln=True), L(outline([(84, 52), (98, 40, 1), (86, 64)]), 'skin', 'b', ln=True),
              L(quad((46, -4), (30, -14), (14, -12)), 'dread', 'b', False, False, 4.2), L(quad((50, -6), (44, -22), (34, -28)), 'dread', 'b', False, False, 4.2),
              L(quad((54, -4), (66, -18), (80, -16)), 'dread', 'b', False, False, 4.2), L(quad((52, -6), (60, -24), (68, -30)), 'dread', 'b', False, False, 4.2),
              L(quad((30, 16), (50, 12), (70, 16)), 'skin_d', 'f', False, False, 1.4), L(quad((32, 26), (50, 22), (68, 26)), 'skin_d', 'f', False, False, 1.4),
              muzzle_f(82, 20, 108),
              L(outline([(4, 112), (16, 98), (34, 106), (50, 112), (66, 106), (84, 98), (96, 112), (90, 128), (50, 132), (10, 128)]), 'shawl', 'f', ln=True),
              L(outline([(50, 112), (66, 106), (84, 98), (96, 112), (90, 126), (60, 128)]), 'shawl_d', 'f', False)],
    'side': [L(quad((40, -4), (24, -18), (8, -16)), 'dread', 'b', False, False, 4.2), L(quad((44, -6), (36, -24), (20, -30)), 'dread', 'b', False, False, 4.2),
             L(quad((30, 14), (50, 10), (70, 14)), 'skin_d', 'f', False, False, 1.4), muzzle_s(), ear_s(),
             L(outline([(0, 112), (20, 96), (50, 104), (80, 100), (96, 112), (86, 128), (40, 132), (6, 126)]), 'shawl', 'f', ln=True)],
    'back': [L(outline([(16, 52), (2, 40, 1), (14, 64)]), 'skin', 'b', ln=True), L(outline([(84, 52), (98, 40, 1), (86, 64)]), 'skin', 'b', ln=True),
             L(quad((46, -4), (30, -16), (14, -14)), 'dread', 'f', False, False, 4.2), L(quad((54, -4), (70, -16), (86, -14)), 'dread', 'f', False, False, 4.2),
             L(quad((50, -6), (48, -24), (40, -32)), 'dread', 'f', False, False, 4.2),
             L(outline([(4, 112), (16, 96), (50, 102), (84, 96), (96, 112), (90, 128), (50, 132), (10, 128)]), 'shawl', 'f', ln=True)],
}


def _back_skulls():
    """De espaldas, el cráneo entero (la nuca por defecto empieza más abajo y lo de arriba quedaba flotando: el lazo de
    N'ameeb, las rastas de Zundar...). Zundar lleva su cabeza alta."""
    tall = [(16, 74), (14, 30), (22, 4), (50, -6), (78, 4), (86, 30), (84, 74), (78, 96), (62, 108), (38, 108), (22, 96)]
    for pid in ('b-adaen', 'g-ob', 'a-ddah', 'r-adji', 'a-kra', 'n-ameeb', 'k-aran-uogu', 'k-al', 's-haha', 's-harqiyah', 'a-tac', 'zundar-zand'):
        ch = CHARS[pid]
        skull = outline(tall if pid == 'zundar-zand' else SKULL_B)
        ch['back'] = [L(skull, 'skin'), L(outline([(56, 14), (84, 40), (84, 72), (64, 100)]), 'skin_d', 'b', False)] + list(ch['back'])


_back_skulls()
