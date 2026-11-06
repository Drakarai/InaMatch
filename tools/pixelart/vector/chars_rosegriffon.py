"""Rose Griffon / Grifos de la Rosa (IE3, Francia): melenas onduladas, tazones, rapados y crestas, con sus modelos 3D como
referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_empire import afro
from chars_firedragon import bowl
from chars_orpheus import headband
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def side_fringe(left=True, y=70, c='mid'):
    """Flequillo largo barrido que tapa un ojo (left: el de la izquierda de la imagen)."""
    if left:
        return L(outline([(12, 66), (14, 40), (30, 22), (54, 16), (74, 22), (88, 40), (88, 60), (78, 48), (64, 44), (56, 52), (46, 66), (38, y + 10, 1), (30, y), (20, y - 4)]), c, 'f', ln=True)
    return L(outline([(88, 66), (86, 40), (70, 22), (46, 16), (26, 22), (12, 40), (12, 60), (22, 48), (36, 44), (44, 52), (54, 66), (62, y + 10, 1), (70, y), (80, y - 4)]), c, 'f', ln=True)


# Roger Pialat (portero): pelo gris oliva liso en tazón, con un flequillo largo que le tapa el ojo derecho; el otro ojo
# rojizo, cara alargada y la boca seria
CHARS['roger-pialat'] = {
    'body': 'delgado', 'pal': pal('#6a6a50', '#f0b880', iris='#a83a2a', shade='#4e4a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': bowl('front', fringe_y=60) + [side_fringe(True, 82)],
    'side': bowl('side') + [spk((58, 28), (90, 40), (92, 76), 6, z='f', light_left=False)],
    'back': bowl('back', nape=84),
}
# Pierre Godin: melena verde agua larga y ondulada que le cae hasta el pecho, con raya a un lado y un mechón que le tapa un
# ojo; el otro ojo de pestañas y una sonrisa tranquila
CHARS['pierre-godin'] = {
    'body': 'delgado', 'pal': pal('#7ac0a8', '#fce4cc', iris='#a8641e', shade='#5a9a88'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': longhair('front', 126, 18) + [side_fringe(False, 84)]
             + [L(rope((86, 70), (100, 96), (94, 122), 10), 'mid', 'f', ln=True), L(rope((14, 70), (2, 96), (8, 122), 10), 'mid', 'f', ln=True)],
    'side': longhair('side', 126, 14),
    'back': longhair('back', 126, 18, ends=4),
}
# Michaël Aron: gordo de piel morena y cara enorme; pelo verde azulado muy corto con entradas en punta; ojos blancos de
# enfado y los dientes apretados
CHARS['micha-l-aron'] = {
    'body': 'corpulento', 'pal': pal('#2a6a6a', '#a8703e', shade='#1e5050'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 4, 'ear_out': 10},
    'front': bald('front') + buzz('front', front_y=36, peak=(50, 42)) + white_eyes(74, 15, 5.4, 4.6, 2)
             + [L([(24, 64), (42, 70)], OUTC, 'f', False, False, 2.4), L([(76, 64), (58, 70)], OUTC, 'f', False, False, 2.4),
                L(outline([(28, 96), (50, 92), (72, 96), (68, 104), (32, 104)]), WHITE, 'f', ln=True), L([(30, 100), (70, 100)], OUTC, 'f', False, False, 1.0)],
    'side': bald('side') + buzz('side') + side_eye(74),
    'back': bald('back') + buzz('back', nape=78),
}
# Francis Poujol: cabeza cuadrada con mandíbula enorme; pelo castaño oscuro en un cepillo plano arriba; cejas gruesas, ojos
# de sueño y la boca en una raya de enfado
FRANCIS_FACE = blob([(12, 36), (50, 30), (88, 36), (92, 76), (90, 108), (70, 122), (30, 122), (10, 108), (8, 76)])
CHARS['francis-poujol'] = {
    'body': 'corpulento', 'pal': pal('#3a2a1e', '#e0a868', shade='#2a1e14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 104, 'face_front': FRANCIS_FACE, 'nose': (50, 86, 4), 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(14, 50), (14, 6), (50, -2), (86, 6), (86, 50), (78, 34), (22, 34)]))],
    'side': [L(outline([(36, 112), (14, 104), (10, 60), (12, 6), (50, -2), (80, 4), (92, 30), (94, 70), (92, 106), (80, 120), (56, 122)]), 'skin'),
             L(outline([(12, 70), (12, 6), (50, -2), (80, 4), (82, 16), (60, 18), (40, 34), (30, 70)]))],
    'back': [L(outline([(14, 90), (14, 6), (50, -2), (86, 6), (86, 90), (50, 96)])), L(outline([(56, 2), (86, 8), (86, 88), (60, 94)]), 'shade', 'b', False)],
}
# Kevin Pinot: piel morena; pelo granate muy corto con un pico de entradas en la frente; ojos verdes de enfado y media sonrisa
CHARS['kevin-pinot'] = {
    'body': 'normal', 'pal': pal('#5a1e24', '#a8703e', iris='#7a9a3a', shade='#401418'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': bald('front') + buzz('front', front_y=34, peak=(50, 26)),
    'side': bald('side') + buzz('side'),
    'back': bald('back') + buzz('back', nape=88),
}
# Roland Pérec: media melena rubia ceniza lisa con raya a un lado, que le tapa media frente y cae por un lado en una coleta
# fina atada con una cinta morada; ojos azules y la boca entreabierta
CHARS['roland-p-rec'] = {
    'body': 'normal', 'pal': pal('#c8c098', '#fcdcc0', iris='#3a7ab8', shade='#a09a74', ribbon='#6a3a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 96, 6) + [side_fringe(False, 78)]
             + [L(rope((84, 70), (92, 94), (88, 110), 7), 'mid', 'f', ln=True), L(ell(88, 96, 4, 3), 'ribbon', 'f', ln=True)],
    'side': longhair('side', 96, 6),
    'back': longhair('back', 96, 6, ends=2) + [L(rope((80, 80), (90, 96), (86, 110), 7), 'mid', 'f', ln=True)],
}
# Romuald Huysmans: pelo granate ondulado y abultado que le enmarca la cara en ondas hasta la mandíbula; ojos verdes de
# enfado y la boca seria
CHARS['romuald-huysmans'] = {
    'body': 'normal', 'pal': pal('#6a3040', '#fce0c4', iris='#3a8a6a', shade='#50222e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (60, 48)},
    'front': longhair('front', 96, 18, top=-2) + [L(outline([(16, 46), (30, 28), (50, 22), (70, 28), (84, 46), (70, 40), (52, 40), (36, 48), (24, 54)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 96, 14, top=-2),
    'back': longhair('back', 96, 18, top=-2, ends=4),
}
# Stéphane Hinault: pelo castaño muy oscuro despeinado y abultado que le cae por la frente tapándole un ojo y por los lados;
# un ojo verde y la boca seria
CHARS['st-phane-hinault'] = {
    'body': 'normal', 'pal': pal('#2e2420', '#fcdcc0', iris='#4a8a3a', shade='#201814'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 4, 14, seed=1301, rx=56, ry=48, cy=40, lo=96) + [side_fringe(True, 80)],
    'side': messy('side', 5, 12, seed=1301, rx=52, ry=48, cy=40, nape=100, sweep=-0.2),
    'back': messy('back', 4, 14, seed=1301, rx=56, ry=48, cy=40, nape=104),
}
# Julien Rousseau: melena rubia dorada larga y ondulada; ojos azules de pestañas largas y una rosa roja sujeta entre los dientes
CHARS['julien-rousseau'] = {
    'body': 'normal', 'pal': pal('#e8c050', '#fce4cc', iris='#3a7ab8', shade='#c09a30', rose='#d8404a', leaf='#2a7a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': longhair('front', 116, 22, top=-4)
             + [L(outline([(12, 66), (14, 40), (30, 22), (50, 16), (70, 22), (86, 40), (88, 66), (78, 54), (64, 48), (50, 56), (40, 50), (28, 56), (20, 64)]), 'mid', 'f', ln=True),
                L(rope((38, 96), (60, 96), (76, 94), 2.4), 'leaf', 'f'), L(ell(74, 98, 7, 6.4), 'rose', 'f', ln=True), L(ell(74, 98, 3, 2.6), (160, 30, 40, 255), 'f', False)],
    'side': longhair('side', 116, 18, top=-4) + [L(ell(96, 98, 6, 6), 'rose', 'f', ln=True)],
    'back': longhair('back', 116, 22, top=-4, ends=4),
}
# Jérôme Hervaud: calvo de cabeza lisa y redondeada; cejas finas en punta, ojos verdes de enfado y la boca seria
CHARS['j-r-me-hervaud'] = {
    'body': 'normal', 'pal': pal('#2a1e14', '#c8945a', iris='#2a8a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front'),
    'side': bald('side'),
    'back': bald('back'),
}
# Alain Favreau: piel morena; media melena rubia lisa que le cae por los lados y la nuca abierta en puntas, con una cinta
# azul marino ancha en la frente; ojos verdes y la boca seria
CHARS['alain-favreau'] = {
    'body': 'normal', 'pal': pal('#e8c858', '#a8703e', iris='#6a9a3a', shade='#c0a038', band='#1e2a5a', band_d='#141e44'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 90, 22, top=-2) + [L(outline([(8, 50), (8, 34), (50, 28), (92, 34), (92, 50), (50, 46)]), 'band', 'f', ln=True)],
    'side': longhair('side', 90, 18, top=-2) + [L(outline([(4, 48), (4, 32), (92, 30), (92, 46)]), 'band', 'f', ln=True)],
    'back': longhair('back', 90, 22, top=-2, ends=4) + [L(outline([(6, 52), (6, 36), (50, 30), (94, 36), (94, 52), (50, 46)]), 'band', 'f', ln=True)],
}
# Émile Lazare (portero suplente): pelo crema blanquecino de pinchos que caen por los lados, con un mechón azul en la frente;
# piel morena, ojos turquesa y una sonrisa
CHARS['mile-lazare'] = {
    'body': 'normal', 'pal': pal('#f4ecd0', '#a8703e', iris='#2a9aa0', shade='#d0c4a0', streak='#2a6ad0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 5, 13, seed=1302, rx=56, ry=46, cy=40, lo=90)
             + [L(outline([(10, 80, 1), (14, 44), (28, 26), (50, 20), (72, 26), (86, 44), (90, 80, 1), (80, 60), (72, 70, 1), (66, 52), (58, 62, 1), (52, 52), (44, 64, 1), (36, 52),
                           (28, 66, 1), (20, 58)]), 'mid', 'f'),
                L(outline([(48, 22), (66, 24), (62, 46), (54, 62, 1), (50, 40)]), 'streak', 'f', False)],
    'side': messy('side', 6, 11, seed=1302, rx=52, ry=46, cy=40, nape=100, sweep=-0.3),
    'back': messy('back', 5, 13, seed=1302, rx=56, ry=46, cy=40, nape=104),
}
# André Pinson: calvo moreno con una cresta corta crema en lo alto; cejas negras en punta muy marcadas, ojos de enfado, una
# perilla clara en la barbilla y la boca torcida
CHARS['andr-pinson'] = {
    'body': 'normal', 'pal': pal('#f0e4c8', '#a87a50', nose='#8a5a34'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': WIDE_FACE, 'nose': (50, 84, 4), 'hairline': False, 'big_ears': 3, 'ear_out': 7},
    'front': bald('front') + [L(outline([(44, 34), (42, 0), (50, -6), (58, 0), (56, 34)]), 'mid', 'f', ln=True),
                              L([(18, 66), (32, 62), (46, 70), (50, 74), (54, 70), (68, 62), (82, 66)], OUTC, 'f', False, False, 3.0),
                              L(outline([(40, 106), (60, 106), (50, 114, 1)]), 'mid', 'f', ln=True)] + white_eyes(76, 15, 5.4, 4.4, 2),
    'side': bald('side') + [L(outline([(36, 8), (52, -4), (76, 0), (84, 10), (60, 10)]), 'mid', 'f', ln=True)] + side_eye(76),
    'back': bald('back') + [L(outline([(44, 12), (44, -2), (50, -6), (56, -2), (56, 12)]), 'mid', 'f', ln=True)],
}
# Jean Gutain: pelo morado liso cortado en tazón con el flequillo recto en mechones y las puntas a la altura de la barbilla;
# ojos de pillo y una sonrisa de dientes
CHARS['jean-gutain'] = {
    'body': 'normal', 'pal': pal('#9a5ab0', '#fce4cc', iris='#1e1e1e', shade='#7a4290'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(4, 104), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (96, 104), (84, 104), (84, 62), (16, 62), (16, 104)])),
              L(outline([(60, 2), (86, 16), (98, 44), (96, 102), (86, 102), (80, 50)]), 'shade', 'b', False),
              L(outline([(10, 62), (12, 38), (28, 22), (50, 18), (72, 22), (88, 38), (90, 62), (50, 58)]), 'mid', 'f', ln=True)]
             + [strand([(x, 24 + abs(x - 50) * 0.1), (x, 60)], 'shade', 'f', 1.0) for x in (24, 36, 50, 64, 76)]
             + [strand([(x, 60), (x, 102)], 'shade', 'b', 1.0) for x in (8, 92)],
    'side': [L(outline([(60, 104), (8, 104), (4, 40), (18, 10), (50, -2), (78, 6), (94, 26), (96, 50), (86, 56), (70, 56), (62, 64)])),
             L(outline([(6, 50), (40, 50), (56, 100), (8, 102)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x - 4, 102)], 'deep', 'b', 1.0) for x in (20, 34, 48)],
    'back': [L(outline([(4, 104), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (96, 104), (50, 102)])),
             L(outline([(56, 4), (86, 16), (98, 44), (96, 102), (64, 102)]), 'shade', 'b', False)]
            + [strand([(x, 6 + abs(x - 50) * 0.2), (x, 102)], 'deep', 'b', 1.0) for x in (16, 30, 44, 58, 72, 86)],
}
# Claude Moreau: piel morena y cara redonda con pecas; pelo verde oliva muy corto con una flor amarilla de pétalos en
# punta en lo alto; ojos turquesa pequeños y una sonrisa
CHARS['claude-moreau'] = {
    'body': 'bajito', 'pal': pal('#6a6a2a', '#c88a50', iris='#2a9a9a', shade='#4e4e1e', flower='#f0c830', freckle='#a86a3a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + buzz('front', front_y=30)
             + [L(outline([(40, 22), (30, 6, 1), (44, 10), (50, -6, 1), (56, 10), (68, 2, 1), (62, 18), (72, 26, 1), (54, 24)]), 'flower', 'f', ln=True)]
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((28, 86), (32, 88), (68, 88), (72, 86))],
    'side': bald('side') + buzz('side') + [L(outline([(64, 14), (60, -4, 1), (70, 6), (82, 0, 1), (76, 14)]), 'flower', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=86) + [L(outline([(46, 6), (50, -6, 1), (54, 6)]), 'flower', 'f', ln=True)],
}
# Michel Morland: cabeza grande y redonda pálida; pelo granate corto con un tupé rosa enorme que se curva hacia arriba y a
# un lado; cejas gruesas rojizas, nariz redonda y la boca en una raya de enfado
CHARS['michel-morland'] = {
    'body': 'corpulento', 'pal': pal('#8a2a24', '#fcdcc4', shade='#681e1a', pink='#f0a0a8', pink_d='#c87880'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'nose': (50, 86, 3.4), 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': bald('front') + buzz('front', front_y=34)
             + [L(outline([(20, 30), (26, 10), (44, 0), (66, -2), (84, 4), (100, -6, 1), (92, 14), (80, 26), (60, 30), (40, 34)]), 'pink', 'f', ln=True),
                L(outline([(60, 2), (84, 6), (92, 12), (78, 22), (60, 24)]), 'pink_d', 'f', False),
                L(outline([(22, 66), (38, 62), (42, 68), (26, 70)]), 'mid', 'f', ln=True), L(outline([(78, 66), (62, 62), (58, 68), (74, 70)]), 'mid', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L(outline([(56, 6), (76, -4), (92, 4), (96, 16), (84, 20), (66, 18)]), 'pink', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=90) + [L(outline([(16, 20), (8, 2, 1), (26, 10)]), 'pink', 'f', ln=True)],
}
