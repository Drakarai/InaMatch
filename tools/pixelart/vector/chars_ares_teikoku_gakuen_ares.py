"""Royal Academy (Ares) (ares-teikoku-gakuen-ares): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de frente,
perfil y espalda).

Comparados uno a uno con sus dibujos de IE1: Genda, Oono, Banjou, Gojou, Kazemaru, Narukami, Henmi, Sakiyama, Doumen, Jimon
y Sakuma tienen en Ares el mismo peinado y los mismos accesorios, así que se reutilizan. Fudou sí cambia (sin la marca roja
y con el pelo de otra forma): va como 'ares:caleb-stonewall'. Shimerigawa, Koudera y Kageyama (de adulto, como jugador) son
nuevos.
"""
from chars import CHARS, L, OUTC, ell, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE, SKULL_F
from chars_bigwaves import bald
from heads import blob
from heads import quad  # noqa: F401

WHITE = (246, 246, 246, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Shimerigawa Kageru (portero suplente): pelo castaño anaranjado en forma de seta enorme, una cúpula que le cubre hasta la
# mandíbula, con flequillo de mechones hasta los ojos; ojeras, mirada caída y dos colmillos
CHARS['grotley-bogwash'] = {
    'body': 'normal', 'pal': pal('#b47a48', '#fcdcc0', iris='#8a8aa0', shade='#8e5a32', light='#d8a070'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 94), (2, 62), (4, 30), (16, 4), (36, -12), (60, -14), (82, -2), (98, 24), (104, 52), (98, 82), (90, 96), (84, 72), (84, 60), (16, 60),
                         (16, 74)])),
              L(outline([(60, -10), (84, 2), (100, 30), (100, 80), (90, 92), (86, 50)]), 'shade', 'b', False),
              fringe([(12, 76), (12, 44), (26, 24), (50, 16), (74, 22), (88, 42), (88, 72), (80, 56), (74, 66, 1), (66, 50), (58, 62, 1), (50, 48), (44, 62, 1),
                      (36, 50), (28, 64, 1), (20, 52)]),
              strand([(30, 22), (24, 50)], 'shade', 'f', 1.0), strand([(56, 18), (60, 48)], 'shade', 'f', 1.0),
              L(quad((28, 84), (36, 87), (44, 84)), (150, 140, 170, 255), 'f', False, False, 1.4),
              L(quad((56, 84), (64, 87), (72, 84)), (150, 140, 170, 255), 'f', False, False, 1.4),
              L(outline([(43, 98), (46, 98), (44.5, 103, 1)]), WHITE, 'f', ln=True), L(outline([(54, 98), (57, 98), (55.5, 103, 1)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(56, 64), (62, 54), (84, 54), (96, 40), (96, 18), (80, -2), (56, -14), (30, -10), (10, 6), (0, 36), (0, 72), (6, 98), (20, 108), (34, 102),
                        (44, 86)])),
             L(outline([(2, 40), (28, 46), (34, 98), (10, 98)]), 'shade', 'b', False),
             fringe([(70, 4), (92, 20), (98, 44), (96, 70, 1), (88, 54), (82, 66, 1), (76, 44), (68, 30)])],
    'back': [L(outline([(8, 92), (2, 52), (10, 14), (36, -12), (64, -12), (90, 14), (100, 52), (94, 92), (70, 104), (50, 110, 1), (30, 104)])),
             L(outline([(56, -10), (88, 12), (100, 52), (92, 92), (66, 104), (70, 50)]), 'shade', 'b', False),
             strand([(30, 10), (24, 50), (30, 96)], 'deep', 'b', 1.0), strand([(50, -8), (50, 104)], 'deep', 'b', 1.0),
             strand([(70, 10), (76, 50), (70, 96)], 'deep', 'b', 1.0)],
}

# Kageyama Reiji de adulto (juega de medio en el equipo): pelo castaño oscuro peinado hacia atrás y recogido en una coleta
# baja, cara larga de pómulos marcados, orejas grandes y las gafas de sol negras de siempre
CHARS['ares:ray-dark'] = {
    'body': 'delgado', 'pal': pal('#6a5444', '#e8b07a', iris='#1e1414', shade='#4e3c30', nose='#d09a68'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 104, 'hairline': False, 'big_ears': 2, 'ear_out': 2, 'nose': (50, 90, 2.4),
             'face_front': LONG_FACE},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(18, 62), (14, 30), (26, 6), (50, -2), (74, 6), (86, 30), (82, 62), (76, 44), (66, 30), (50, 36, 1), (34, 30), (24, 44)]), 'mid', 'f'),
              L(outline([(56, 2), (78, 10), (86, 34), (82, 56), (74, 36)]), 'shade', 'f', False),
              strand([(40, 8), (36, 30)], 'shade', 'f', 1.0), strand([(60, 8), (64, 30)], 'shade', 'f', 1.0),
              L(outline([(26, 66), (46, 66), (46, 76), (40, 80), (30, 79), (26, 74)]), OUTC, 'f', False),
              L(outline([(74, 66), (54, 66), (54, 76), (60, 80), (70, 79), (74, 74)]), OUTC, 'f', False),
              L([(46, 68), (54, 68)], OUTC, 'f', False, False, 1.8),
              L(quad((30, 96), (36, 100), (40, 104)), (190, 130, 90, 255), 'f', False, False, 1.2),
              L(quad((70, 96), (64, 100), (60, 104)), (190, 130, 90, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(16, 72), (0, 86), (-8, 108, 1), (6, 100), (20, 86), (28, 74)]), 'mid', 'b'),
             L(outline([(54, 50), (60, 38), (80, 30), (90, 20), (80, 4), (54, -4), (30, 0), (12, 16), (6, 40), (10, 66), (20, 80), (28, 72), (38, 60)])),
             L(outline([(8, 40), (30, 44), (32, 72), (14, 70)]), 'shade', 'b', False),
             L(ell(18, 74, 4, 3), (40, 30, 26, 255), 'f', ln=True),
             L([(70, 66), (96, 64)], OUTC, 'f', False, False, 2.4), L(ell(92, 68, 5, 4.6), OUTC, 'f', False)],
    'back': [L(outline([(16, 82), (12, 40), (22, 10), (50, -2), (78, 10), (88, 40), (84, 82), (64, 92), (36, 92)])),
             L(outline([(56, 2), (80, 12), (88, 44), (82, 80), (62, 88)]), 'shade', 'b', False),
             strand([(30, 10), (40, 70)], 'deep', 'b', 1.0), strand([(70, 10), (60, 70)], 'deep', 'b', 1.0),
             L(outline([(44, 84), (56, 84), (58, 100), (52, 120, 1), (46, 100)]), 'mid', 'f', ln=True),
             L(ell(50, 86, 6, 3), (40, 30, 26, 255), 'f', ln=True)],
}

# Koudera Ginpei: una gorra militar negra enorme con la visera calada hasta los ojos y la insignia verde con la estrella
# roja; por debajo asoma una melena azul marino que se vuelve dorada en las puntas
CHARS['emperio-n-guinn'] = {
    'body': 'normal', 'pal': pal('#2a3a6a', '#fcdcc0', iris='#2a3a6a', tip='#c88a3a', cap='#1e1e22', cap_d='#111114', badge='#2a6a3a', star='#c81e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (10, 60), (90, 60), (90, 96), (80, 90), (20, 90)]), 'mid', 'b'),
              L(outline([(12, 96), (14, 84), (86, 84), (88, 96), (78, 92), (70, 98), (62, 92), (50, 96), (38, 92), (30, 98), (22, 92)]), 'tip', 'b'),
              L(outline([(8, 56), (2, 34), (14, 10), (40, -6), (70, -6), (92, 8), (104, 34), (100, 56), (80, 62), (50, 64), (20, 62)]), 'cap', 'f', ln=True),
              L(outline([(16, 58), (50, 60), (84, 56), (96, 64), (70, 70), (50, 71), (30, 70), (12, 64)]), 'cap_d', 'f', ln=True),
              L(ell(84, 46, 6.4, 6.4), 'badge', 'f', ln=True), L(ell(84, 46, 2.6, 2.6), 'star', 'f', False),
              L(ell(34, 78, 4, 4), (40, 40, 70, 255), 'f', False), L(ell(33, 77, 1.4, 1.4), WHITE, 'f', False)],
    'side': [L(outline([(2, 50), (40, 52), (46, 80), (30, 92), (6, 92), (0, 70)]), 'mid', 'b'),
             L(outline([(4, 80), (40, 78), (40, 90), (30, 94), (6, 94)]), 'tip', 'b'),
             L(outline([(2, 52), (0, 20), (20, 0), (60, -6), (92, 4), (104, 24), (98, 48), (60, 56), (20, 58)]), 'cap', 'f', ln=True),
             L(outline([(80, 50), (104, 50), (112, 60), (86, 62)]), 'cap_d', 'f', ln=True)],
    'back': [L(outline([(10, 96), (10, 58), (90, 58), (92, 96), (50, 100)]), 'mid', 'b'),
             L(outline([(10, 96), (12, 84), (90, 84), (92, 96), (80, 92), (70, 98), (60, 92), (50, 98), (40, 92), (30, 98), (20, 92)]), 'tip', 'b'),
             L(outline([(8, 62), (2, 34), (14, 10), (40, -6), (70, -6), (92, 8), (104, 34), (100, 62), (50, 68)]), 'cap', 'f', ln=True)],
}

# Fudou en Ares: sin la marca roja; el pelo castaño oscuro con reflejos blancos sale de lo alto en un penacho de pinchos y
# le cae hacia delante por el lado izquierdo de la frente en mechones largos, con el resto de la cabeza rapado
_cal_pal = pal('#3e2a1e', '#fcd8b0', iris='#2a7a6a', shade='#2a1c14', light='#cfc6c2')
CHARS['ares:caleb-stonewall'] = {
    'body': 'normal', 'pal': _cal_pal,
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': bald('front') + [
        L(outline([(8, 44), (6, 16), (20, -4), (32, -32, 1), (44, -10), (56, -10), (70, -24, 1), (82, -16), (90, -6, 1), (76, 4), (64, 12), (60, 34), (56, 52),
                   (50, 74, 1), (42, 54), (36, 66, 1), (32, 48), (24, 60, 1), (18, 44), (10, 56, 1), (0, 52, 1)]), 'mid', 'f'),
        L(outline([(14, 22), (26, 4), (38, -4), (28, 10), (18, 30)]), 'light', 'f', False),
        L(outline([(36, 20), (46, 12), (44, 40), (40, 56)]), 'light', 'f', False),
        L(outline([(56, -4), (70, -16), (64, 0)]), 'shade', 'f', False)],
    'side': bald('side') + [
        L(outline([(54, 40), (48, 14), (30, 0), (20, -22, 1), (44, -12), (56, -28, 1), (68, -8), (84, -4), (100, -10, 1), (96, 10), (100, 34), (94, 64, 1), (86, 46),
                   (80, 60, 1), (74, 44), (64, 48)]), 'mid', 'f'),
        L(outline([(84, 4), (96, 0), (92, 18), (90, 36)]), 'light', 'f', False)],
    'back': bald('back') + [
        L(outline([(30, 6), (34, -24, 1), (46, -8), (56, -10), (66, -20, 1), (76, 0), (70, 16), (50, 20)]), 'mid', 'f'),
        L(outline([(64, 6), (84, 10), (90, 40), (86, 62, 1), (78, 40), (68, 20)]), 'mid', 'f')],
}
