"""Academia Militar Mar de Luna (go-gassan-kunimitsu): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente,
perfil y espalda)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Alessandro Il Grande (portero): pelo azul morado oscuro revuelto con un mechón de antena arriba, puntas abiertas a los
# lados y mechones que le cruzan la cara; ojos rojos y unas marcas finas en las mejillas
CHARS['alessandro-il-grande'] = {
    'body': 'normal', 'pal': pal('#3a3460', '#f0b884', iris='#c81e2a', shade='#2a2648'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 72), (8, 56), (-6, 50, 1), (8, 40), (8, 18), (24, 2), (40, -4), (46, -20, 1), (54, -6), (76, 0), (92, 16), (94, 40), (108, 46, 1), (92, 54),
                         (86, 72), (82, 56), (18, 56)])),
              L(outline([(60, 0), (84, 12), (92, 42), (86, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 66), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (86, 66), (78, 54), (72, 64, 1), (66, 48), (56, 64, 1), (52, 44), (44, 72, 1), (40, 46),
                      (30, 62, 1), (24, 52), (20, 80, 1)]),
              L([(18, 86), (22, 92)], OUTC, 'f', False, False, 1.0), L([(82, 86), (78, 92)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(54, 62), (60, 50), (80, 48), (92, 32), (86, 12), (70, 0), (60, -18, 1), (50, -2), (26, -4), (-6, 2, 1), (14, 14), (2, 30), (-10, 40, 1), (6, 44),
                        (4, 70), (14, 84), (30, 84), (44, 74)])),
             L(outline([(6, 40), (28, 42), (32, 78), (12, 78)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(16, 84), (8, 56), (-8, 46, 1), (8, 40), (8, 18), (24, 2), (40, -4), (46, -20, 1), (54, -6), (76, 0), (92, 16), (94, 40), (110, 46, 1), (92, 56),
                        (86, 84), (66, 92), (34, 92)])),
             L(outline([(56, 2), (86, 14), (92, 50), (84, 82), (62, 88)]), 'shade', 'b', False),
             strand([(30, 20), (40, 40), (34, 70)], 'deep', 'b', 1.0), strand([(70, 20), (60, 40), (66, 70)], 'deep', 'b', 1.0)],
}

# Gene Ghiskhan: grandullón de piel muy pálida y cabeza rapada, con dibujos azul petróleo en lo alto de la cabeza y una
# barba recortada del mismo color en forma de engranaje; cejas pintadas en zigzag y ojos naranjas
CHARS['gene-ghiskhan'] = {
    'body': 'corpulento', 'pal': pal('#2e5a6e', '#fcecd0', iris='#e08a1e', skin_d='#ecd4b4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 3, 'ear_out': 6,
             'face_front': blob([(10, 40), (50, 30), (90, 40), (96, 76), (90, 108), (50, 120), (10, 108), (4, 76)])},
    'front': [L(blob([(12, 66), (10, 36), (24, 14), (50, 6), (76, 14), (90, 36), (88, 66)]), 'skin'),
              L(outline([(22, 34), (20, 20), (32, 14), (34, 28)]), 'mid', 'f', ln=True), L(outline([(43, 12), (57, 12), (56, 26), (44, 26)]), 'mid', 'f', ln=True),
              L(outline([(66, 28), (68, 14), (80, 20), (78, 34)]), 'mid', 'f', ln=True),
              L(outline([(10, 92), (20, 100), (16, 108), (30, 112), (30, 120), (44, 116), (50, 124), (56, 116), (70, 120), (70, 112), (84, 108), (80, 100), (90, 92),
                         (88, 108), (70, 120), (50, 126), (30, 120), (12, 108)]), 'mid', 'f', ln=True),
              L([(18, 72), (28, 64), (34, 74), (42, 66)], OUTC, 'f', False, False, 2.4), L([(82, 72), (72, 64), (66, 74), (58, 66)], OUTC, 'f', False, False, 2.4)],
    'side': [L(outline([(24, 22), (40, 6), (60, 6), (74, 14), (66, 22), (44, 20)]), 'mid', 'f', ln=True),
             L(outline([(54, 92), (66, 96), (80, 112), (70, 122), (56, 118), (48, 104)]), 'mid', 'f', ln=True),
             L([(14, 64), (50, 70)], OUTC, 'f', False, False, 2.6)],
    'back': [L(blob([(12, 66), (10, 36), (24, 14), (50, 6), (76, 14), (90, 36), (88, 66), (76, 92), (24, 92)]), 'skin'),
             L(outline([(22, 34), (20, 20), (32, 14), (34, 28)]), 'mid', 'f', ln=True), L(outline([(43, 12), (57, 12), (56, 26), (44, 26)]), 'mid', 'f', ln=True),
             L(outline([(66, 28), (68, 14), (80, 20), (78, 34)]), 'mid', 'f', ln=True),
             L(quad((10, 56), (50, 62), (90, 56)), OUTC, 'f', False, False, 2.6)],
}

# Attila Hun: pelo rojo tostado en un bloque cuadrado, rapado a los lados, con un pico en la frente; marcas rojas en las
# mejillas, ojos azules hundidos y los dientes apretados
CHARS['attila-hun'] = {
    'body': 'corpulento', 'pal': pal('#b03a22', '#d8945c', iris='#8ab0d0', shade='#8a2a18', mark='#c82a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 104, 'hairline': [(16, 60), (24, 44), (40, 48), (50, 38), (60, 48), (76, 44), (84, 60)]},
    'front': [L(outline([(14, 60), (10, 36), (18, 14), (40, 2), (60, 2), (82, 14), (90, 36), (86, 60), (80, 46), (20, 46)])),
              L(outline([(60, 4), (82, 16), (90, 40), (82, 50)]), 'shade', 'b', False), L(ell(46, 18, 6, 6), 'light', 'b', False),
              L([(18, 82), (24, 86), (18, 90)], 'mark', 'f', False, False, 1.8), L([(82, 82), (76, 86), (82, 90)], 'mark', 'f', False, False, 1.8)],
    'side': [L(outline([(58, 46), (80, 44), (90, 30), (82, 10), (60, 0), (34, 0), (12, 12), (4, 36), (8, 56), (22, 58), (36, 50)])),
             L(outline([(4, 36), (40, 32), (60, 46), (36, 52), (10, 56)]), 'shade', 'b', False),
             L(outline([(78, 84), (88, 80), (82, 92)]), 'mark', 'f', False)],
    'back': [L(outline([(12, 70), (8, 36), (18, 14), (40, 2), (60, 2), (82, 14), (92, 36), (88, 70), (50, 74)])),
             L(outline([(8, 40), (50, 36), (92, 40), (88, 70), (50, 74), (12, 70)]), 'shade', 'b', False),
             L(outline([(26, 80), (74, 80), (74, 86), (26, 86)]), 'shade', 'b', False)],
}

# Sun Tzu: media melena partida en dos colores, negra a un lado y blanca al otro, con un mechón que le tapa el ojo
# derecho; piel morena y ojo rosado entornado
CHARS['sun-tzu'] = {
    'body': 'normal', 'pal': pal('#3a3030', '#b8845a', iris='#c87aa0', white='#f0e8ec', white_d='#c8b0b8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 100), (4, 70), (4, 36), (16, 12), (50, 0), (50, 66), (16, 66)])),
              L(outline([(50, 0), (84, 12), (98, 34), (108, 44, 1), (96, 50), (96, 70), (88, 96), (84, 66), (50, 66)]), 'white'),
              fringe([(10, 74), (10, 44), (22, 22), (50, 12), (52, 44), (46, 70), (40, 94, 1), (30, 78), (20, 86)]),
              fringe([(50, 12), (78, 20), (90, 42), (90, 64), (80, 52), (70, 60, 1), (64, 46), (56, 52), (52, 44)], 'white'),
              L(outline([(30, 18), (50, 12), (40, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 64), (60, 50), (80, 48), (92, 32), (86, 12), (60, -2), (40, -2), (46, 40), (52, 60)]), 'white'),
             L(outline([(40, -2), (16, 8), (2, 34), (-8, 46, 1), (4, 52), (4, 80), (16, 96), (36, 92), (46, 76), (46, 40)])),
             L(outline([(60, -2), (86, 12), (94, 36), (90, 54, 1), (82, 42), (72, 32)]), 'white_d', 'b', False)],
    'back': [L(outline([(12, 92), (4, 70), (4, 36), (16, 12), (50, 0), (84, 12), (98, 34), (110, 44, 1), (96, 50), (94, 76), (80, 90), (50, 94)]), 'white'),
             L(outline([(76, 40), (96, 50), (94, 80), (82, 94), (72, 70)])),
             L(outline([(30, 80), (50, 92), (70, 80), (60, 96, 1), (40, 96, 1)]), 'white_d', 'b', False)],
}

# Arty Xerxes: cara alargada, pelo morado oscuro con un tupé altísimo granate que sube en punta, los lados en punta hacia
# fuera; gafas redondas de cristales verdes, nariz larga y sonrisa de dientes de conejo
CHARS['arty-xerxes'] = {
    'body': 'delgado', 'pal': pal('#3e2e48', '#f6dcb4', shade='#2e2236', top='#7a2a4a', top_d='#5a1e38', lens='#a8e858'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'buck', 'mouth_y': 104, 'hairline': (56, 46), 'face_front': blob([(16, 50), (50, 44), (84, 50), (86, 84), (76, 112), (50, 122), (24, 112), (14, 84)])},
    'front': [L(outline([(16, 62), (10, 46), (-6, 40, 1), (12, 32), (22, 20), (78, 20), (88, 32), (106, 40, 1), (90, 46), (84, 62), (78, 52), (22, 52)])),
              L(outline([(30, 30), (30, 4), (38, -20), (50, -36, 1), (62, -20), (70, 4), (70, 30), (50, 40)]), 'top', 'f', ln=True),
              L(outline([(52, -24), (66, 0), (66, 28), (54, 34)]), 'top_d', 'f', False),
              L(outline([(18, 70), (28, 64), (40, 66), (48, 72), (52, 72), (60, 66), (72, 64), (82, 70), (76, 82), (62, 84), (52, 78), (48, 78), (38, 84), (24, 82)]), OUTC, 'f', False),
              L(ell(34, 74, 8, 6), 'lens', 'f', False), L(ell(66, 74, 8, 6), 'lens', 'f', False),
              L(outline([(46, 76), (54, 76), (56, 98), (50, 102), (44, 98)]), 'skin_d', 'f', False)],
    'side': [L(outline([(62, 46), (80, 40), (84, 24), (60, 18), (36, 16), (4, 18), (-10, 30, 1), (6, 36), (2, 62), (14, 84), (30, 82), (44, 64)])),
             L(outline([(40, 22), (56, 6), (80, -6), (100, -22, 1), (96, 6), (84, 24), (60, 30)]), 'top', 'f', ln=True),
             L(outline([(76, 66), (96, 66), (96, 82), (80, 84)]), 'lens', 'f', ln=True), L([(76, 70), (50, 66)], OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(16, 84), (10, 46), (-8, 34, 1), (12, 30), (24, 18), (50, 12), (76, 18), (88, 30), (108, 34, 1), (90, 46), (84, 84), (50, 96)])),
             L(outline([(56, 16), (86, 30), (88, 60), (82, 82), (60, 92)]), 'shade', 'b', False),
             L(outline([(44, 16), (50, -4, 1), (56, 16)]), 'top', 'f', ln=True)],
}

# Darius Cyrus: pelo gris verdoso liso con un mechón blanco ancho que le cruza la cabeza, flequillo de lado y la nuca a
# mechones en punta; ojos rojos de mirada fija
CHARS['darius-cyrus'] = {
    'body': 'normal', 'pal': pal('#a8b0a8', '#f8c89c', iris='#b02a4a', shade='#8a7e7a', streak='#f4f0e4'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 90), (8, 60), (6, 30), (20, 8), (50, -2), (80, 8), (94, 30), (94, 60), (86, 90), (82, 62), (18, 62)])),
              L(outline([(62, 4), (86, 18), (94, 48), (88, 86), (82, 56)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 42), (26, 20), (52, 10), (78, 18), (90, 40), (90, 64), (82, 52), (72, 50), (62, 58, 1), (56, 44), (44, 50), (34, 64, 1), (26, 56),
                      (18, 66)]),
              L(outline([(24, 20), (40, 12), (46, 30), (40, 56), (34, 64), (32, 40)]), 'streak', 'f', ln=True)],
    'side': [L(outline([(54, 66), (58, 52), (80, 48), (92, 32), (86, 10), (62, -2), (34, -2), (12, 10), (2, 40), (2, 70), (8, 86), (20, 96, 1), (26, 84), (36, 96, 1),
                        (42, 82), (48, 76)])),
             L(outline([(4, 40), (30, 40), (36, 84), (10, 86)]), 'shade', 'b', False),
             L(outline([(70, -2), (86, 8), (94, 32), (90, 52), (84, 30), (76, 12)]), 'streak', 'f', ln=True)],
    'back': [L(outline([(14, 88), (8, 60), (6, 30), (20, 8), (50, -2), (80, 8), (94, 30), (94, 60), (88, 88), (74, 96, 1), (66, 86), (58, 98, 1), (50, 86), (42, 98, 1),
                        (34, 86), (26, 96, 1)])),
             L(outline([(56, 2), (86, 14), (94, 50), (88, 86), (62, 90)]), 'shade', 'b', False)],
}

# Jerry Onimo (sin modelo 3D, del retrato): pelo negro de pinchos largos que salen hacia arriba y hacia los lados, y una
# máscara roja que le tapa la nariz y la boca; ojos fruncidos
CHARS['jerry-onimo'] = {
    'body': 'normal', 'pal': pal('#24242a', '#f8c89c', iris='#2a1a1a', mask='#c81e2a', mask_d='#8a1420'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(16, 86), (-6, 78, 1), (8, 64), (-14, 46, 1), (6, 40), (0, 18, 1), (18, 18), (20, -4, 1), (36, 8), (50, -18, 1), (60, 6), (82, -8, 1), (82, 16),
                         (102, 20, 1), (92, 36), (110, 50, 1), (92, 60), (102, 80, 1), (86, 86), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (94, 50), (88, 76), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 66), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (86, 66), (78, 54), (72, 62, 1), (66, 48), (56, 60, 1), (50, 46), (44, 60, 1), (34, 48),
                      (26, 62, 1), (20, 54)]),
              L(outline([(20, 82), (36, 84), (50, 90), (64, 84), (80, 82), (78, 94), (62, 98), (50, 94), (38, 98), (22, 94)]), 'mask', 'f', ln=True),
              L(outline([(50, 90), (64, 84), (80, 82), (78, 94), (62, 98), (50, 94)]), 'mask_d', 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (80, 48), (92, 32), (86, 12), (96, -6, 1), (70, 0), (62, -20, 1), (48, -2), (22, -12, 1), (20, 8), (-8, 10, 1), (8, 26),
                        (-14, 44, 1), (6, 48), (-6, 72, 1), (12, 72), (14, 92, 1), (30, 80), (46, 72)])),
             L(outline([(6, 40), (28, 42), (30, 76), (12, 74)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 14), (96, 40), (92, 62, 1), (84, 46), (76, 34)]),
             L(outline([(76, 82), (94, 82), (96, 94), (78, 96)]), 'mask', 'f', ln=True), L([(74, 84), (50, 80)], 'mask_d', 'f', False, False, 2.2)],
    'back': [L(outline([(16, 86), (-6, 80, 1), (8, 64), (-14, 46, 1), (6, 40), (0, 18, 1), (18, 18), (20, -4, 1), (36, 8), (50, -18, 1), (60, 6), (82, -8, 1), (82, 16),
                        (102, 20, 1), (92, 36), (110, 50, 1), (92, 60), (104, 82, 1), (86, 88), (66, 96), (50, 104, 1), (34, 96)])),
             L(outline([(56, 6), (86, 16), (94, 50), (88, 84), (62, 92)]), 'shade', 'b', False),
             L(quad((14, 84), (50, 90), (86, 84)), 'mask_d', 'f', False, False, 2.2)],
}

# Leon Ohnepart: piel morena y cabeza rapada, con una tapa plana de pelo negro arriba como un gorro, una cicatriz en estrella
# en la frente y unas gafas de sol naranjas grandes con montura blanca
CHARS['leon-ohnepart'] = {
    'body': 'normal', 'pal': pal('#1e2a26', '#c09060', shade='#141c1a', lens='#f0a040', frame='#f0eee8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(blob([(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]), 'skin'),
              L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(outline([(18, 20), (22, 4), (50, -2), (78, 4), (82, 20), (50, 24)]), 'mid', 'f', ln=True),
              L([(60, 34), (70, 44), (62, 46), (72, 54)], OUTC, 'f', False, False, 1.4),
              L(outline([(12, 68), (50, 64), (88, 68), (86, 74), (50, 70), (14, 74)]), 'frame', 'f', ln=True),
              L(outline([(16, 72), (48, 72), (46, 88), (20, 86)]), 'lens', 'f', ln=True), L(outline([(84, 72), (52, 72), (54, 88), (80, 86)]), 'lens', 'f', ln=True)],
    'side': [L(outline([(16, 30), (24, 6), (50, -2), (76, 2), (84, 16), (60, 22), (36, 22)]), 'mid', 'f', ln=True),
             L(outline([(70, 66), (96, 66), (96, 84), (74, 86)]), 'lens', 'f', ln=True), L(quad((70, 68), (56, 66), (46, 74)), 'frame', 'f', False, False, 3.0)],
    'back': [L(outline([(18, 22), (22, 4), (50, -2), (78, 4), (82, 22), (50, 28)]), 'mid', 'f', ln=True)],
}

# Robert Lee: pelo magenta de pinchos que salen hacia arriba en abanico, con la nuca y los lados más oscuros; ojos blancos
# con pupila pequeña y media sonrisa
CHARS['robert-lee'] = {
    'body': 'normal', 'pal': pal('#a03a6a', '#f8c89c', shade='#5a2a40', deep='#3a1a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(16, 60), (22, 46), (36, 42), (50, 50), (64, 42), (78, 46), (84, 60)]},
    'front': [L(outline([(16, 60), (12, 34), (4, 20, 1), (16, 18), (14, -4, 1), (30, 8), (36, -14, 1), (46, 2), (54, -16, 1), (60, 2), (72, -12, 1), (74, 8), (92, 0, 1),
                         (86, 18), (100, 22, 1), (88, 36), (84, 60), (78, 48), (22, 48)])),
              L(outline([(12, 60), (14, 40), (22, 40), (22, 60)]), 'shade', 'b'), L(outline([(88, 60), (86, 40), (78, 40), (78, 60)]), 'shade', 'b'),
              strand([(30, 10), (40, 30), (50, 46)], 'shade', 'b', 1.0), strand([(70, 10), (60, 30), (50, 46)], 'shade', 'b', 1.0)],
    'side': [L(outline([(60, 46), (80, 44), (90, 30), (82, 10), (90, -10, 1), (70, -2), (62, -24, 1), (50, -4), (34, -14, 1), (34, 4), (14, 12), (6, 40), (8, 70), (22, 82),
                        (36, 76), (48, 60)]), 'shade'),
             L(outline([(34, 4), (34, -14, 1), (50, -4), (62, -24, 1), (70, -2), (90, -10, 1), (82, 10), (90, 28), (70, 26), (50, 20), (34, 18)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 80), (10, 40), (4, 26, 1), (16, 22), (14, 0, 1), (30, 10), (36, -12, 1), (46, 4), (54, -14, 1), (60, 4), (72, -10, 1), (74, 10), (92, 2, 1),
                        (86, 22), (100, 28, 1), (90, 40), (86, 80), (50, 88)]), 'shade'),
             L(outline([(14, 0, 1), (30, 10), (36, -12, 1), (46, 4), (54, -14, 1), (60, 4), (72, -10, 1), (74, 10), (92, 2, 1), (86, 22), (70, 30), (50, 26), (30, 30),
                        (16, 22)]), 'mid', 'b', False)],
}

# Doug McArthur: pelo malva liso en media melena con raya a un lado y un mechón que le cae por la frente hasta el ojo;
# ojos castaños serios
CHARS['doug-mcarthur'] = {
    'body': 'normal', 'pal': pal('#7a3e5e', '#fcdcc0', iris='#7a4a1e', shade='#5a2a44'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (2, 70, 1), (8, 56), (6, 26), (24, 6), (50, -2), (76, 6), (94, 26), (94, 56), (106, 64, 1), (90, 72), (86, 90), (82, 62), (18, 62)])),
              L(outline([(62, 2), (88, 18), (94, 48), (88, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 42), (26, 20), (50, 12), (74, 18), (88, 38), (90, 64), (82, 52), (66, 44), (52, 46), (40, 56), (30, 74, 1), (24, 60), (18, 76)])],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 32), (86, 10), (64, -2), (36, -2), (12, 10), (2, 40), (4, 70), (12, 92, 1), (22, 82), (34, 94, 1), (42, 80),
                        (48, 72)])),
             L(outline([(4, 40), (28, 42), (34, 84), (10, 84)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 60, 1), (86, 48), (76, 36)])],
    'back': [L(outline([(14, 86), (2, 70, 1), (8, 56), (6, 26), (24, 6), (50, -2), (76, 6), (94, 26), (94, 56), (104, 70, 1), (88, 86), (74, 94, 1), (62, 86), (50, 96, 1),
                        (38, 86), (26, 94, 1)])),
             L(outline([(56, 2), (88, 18), (94, 50), (88, 84), (62, 88)]), 'shade', 'b', False),
             strand([(40, 10), (34, 60), (40, 86)], 'deep', 'b', 1.0)],
}

# Nobby Naga: un pañuelo rojo atado en la cabeza del que salen mechones rojos largos curvados como tentáculos hacia
# arriba y hacia los lados, una venda negra que le tapa los ojos con las puntas colgando por detrás
CHARS['nobby-naga'] = {
    'body': 'normal', 'pal': pal('#b0202a', '#c8905c', shade='#801820', band='#2a2a30'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 70), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (86, 70)])),
              L(outline([(60, 4), (84, 16), (90, 44), (82, 64)]), 'shade', 'b', False),
              L(quad((20, 30), (-10, 40), (-10, 80)), 'mid', 'b', False, False, 8.0), L(quad((80, 30), (110, 30), (114, 54)), 'mid', 'b', False, False, 8.0),
              L(quad((36, 14), (20, -20), (34, -30)), 'mid', 'b', False, False, 7.0), L(quad((60, 10), (80, -24), (70, -36)), 'mid', 'b', False, False, 7.0),
              L(quad((14, 60), (-6, 80), (6, 104)), 'mid', 'b', False, False, 7.0),
              L(outline([(10, 66), (12, 56), (50, 54), (88, 56), (90, 66), (88, 80), (50, 82), (12, 80)]), 'band', 'f', ln=True),
              L(ell(34, 74, 6, 4), WHITE, 'f', False), L(ell(66, 74, 6, 4), WHITE, 'f', False),
              L(ell(34, 75, 2.4, 2.4), OUTC, 'f', False), L(ell(66, 75, 2.4, 2.4), OUTC, 'f', False)],
    'side': [L(outline([(60, 50), (80, 44), (90, 28), (80, 8), (56, -2), (30, 0), (12, 14), (4, 40), (8, 60), (30, 62)])),
             L(outline([(4, 40), (30, 36), (44, 56), (10, 60)]), 'shade', 'b', False),
             L(quad((60, 6), (80, -26), (70, -40)), 'mid', 'b', False, False, 7.0), L(quad((20, 10), (-4, -10), (-10, 10)), 'mid', 'b', False, False, 7.0),
             L(outline([(4, 64), (6, 54), (50, 56), (94, 62), (94, 78), (50, 76), (8, 74)]), 'band', 'f', ln=True),
             L(quad((8, 68), (-6, 90), (-2, 116)), 'band', 'f', False, False, 3.0), L(quad((10, 70), (4, 92), (12, 116)), 'band', 'f', False, False, 3.0)],
    'back': [L(outline([(14, 74), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (86, 74), (50, 80)])),
             L(outline([(56, 4), (84, 16), (90, 50), (84, 72), (60, 78)]), 'shade', 'b', False),
             L(quad((20, 30), (-12, 40), (-10, 80)), 'mid', 'b', False, False, 8.0), L(quad((80, 30), (112, 30), (114, 54)), 'mid', 'b', False, False, 8.0),
             L(quad((40, 12), (24, -20), (36, -30)), 'mid', 'b', False, False, 7.0), L(quad((60, 10), (80, -24), (70, -36)), 'mid', 'b', False, False, 7.0),
             L(outline([(10, 72), (12, 62), (50, 60), (88, 62), (90, 72), (88, 84), (50, 86), (12, 84)]), 'band', 'f', ln=True),
             L(quad((48, 82), (42, 100), (46, 120)), 'band', 'f', False, False, 3.0), L(quad((52, 82), (60, 100), (56, 120)), 'band', 'f', False, False, 3.0)],
}

# Salvador Addin (portero): pelo negro azulado recogido en un moño alto de bultos redondos, con dos mechones gruesos en punta
# que salen hacia fuera por debajo de las orejas; ojos grises y una sonrisa de dientes desafiante
CHARS['salvador-addin'] = {
    'body': 'normal', 'pal': pal('#2c3044', '#f0b884', iris='#7a8a9a', shade='#1e2232'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': [(16, 66), (20, 48), (36, 44), (50, 50), (64, 44), (80, 48), (84, 66)]},
    'front': [L(outline([(16, 70), (8, 44), (0, 30), (10, 14), (24, 12), (30, -6), (40, -18), (50, -24), (60, -18), (70, -6), (76, 12), (90, 14), (100, 30), (92, 44),
                         (84, 70)])),
              L(outline([(56, -20), (68, -4), (76, 14), (92, 20), (90, 40), (80, 56)]), 'shade', 'b', False),
              L(outline([(12, 76), (-8, 84), (-22, 98, 1), (-2, 96), (-14, 108, 1), (6, 100), (18, 90)]), 'mid', 'b'),
              L(outline([(88, 76), (108, 84), (122, 98, 1), (102, 96), (114, 108, 1), (94, 100), (82, 90)]), 'mid', 'b'),
              strand([(30, 10), (50, 4), (70, 10)], 'deep', 'b', 1.2), strand([(10, 26), (22, 30)], 'deep', 'b', 1.0), strand([(90, 26), (78, 30)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 48), (80, 44), (88, 28), (78, 10), (70, -10), (54, -22), (34, -18), (20, -4), (6, 10), (-4, 30), (2, 48), (-2, 64), (6, 80), (-16, 96, 1),
                        (8, 92), (2, 110, 1), (22, 92), (34, 74), (46, 62)])),
             L(outline([(0, 40), (24, 42), (30, 76), (8, 80)]), 'shade', 'b', False),
             strand([(20, -2), (40, 10), (66, 6)], 'deep', 'b', 1.2), strand([(4, 30), (24, 36), (50, 30)], 'deep', 'b', 1.2)],
    'back': [L(outline([(16, 84), (8, 44), (0, 30), (10, 14), (24, 12), (30, -6), (40, -18), (50, -24), (60, -18), (70, -6), (76, 12), (90, 14), (100, 30), (92, 44),
                        (84, 84), (60, 92), (50, 104, 1), (40, 92)])),
             L(outline([(12, 80), (-10, 84), (-26, 96, 1), (-4, 96), (-16, 108, 1), (6, 100), (20, 92)]), 'mid', 'b'),
             L(outline([(88, 80), (110, 84), (126, 96, 1), (104, 96), (116, 108, 1), (94, 100), (80, 92)]), 'mid', 'b'),
             L(outline([(56, -20), (68, -4), (76, 14), (92, 20), (90, 50), (84, 80), (60, 90)]), 'shade', 'b', False),
             strand([(30, 10), (50, 2), (70, 10)], 'deep', 'b', 1.2), strand([(14, 40), (50, 34), (86, 40)], 'deep', 'b', 1.2)],
}

# Otto Bismark: piel muy clara, pelo rubio oscuro de pinchos largos peinados hacia arriba y hacia atrás, con la nuca en
# pico; marcas de enfado en la frente y ojos lila
CHARS['otto-bismark'] = {
    'body': 'normal', 'pal': pal('#b89a5a', '#fcf0dc', iris='#6a6ab8', shade='#8a6a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(16, 60), (22, 42), (36, 36), (50, 40), (64, 36), (78, 42), (84, 60)]},
    'front': [L(outline([(16, 60), (8, 40), (-6, 18, 1), (12, 22), (12, 0), (24, -20, 1), (34, 0), (50, -10), (60, -24, 1), (66, 0), (84, -6, 1), (86, 12), (104, 12, 1),
                         (90, 30), (92, 46), (84, 60), (78, 48), (22, 48)])),
              L(outline([(60, -4), (84, 6), (92, 36), (84, 52), (76, 30)]), 'shade', 'b', False),
              L(outline([(34, 6), (50, -2), (50, 30)]), 'light', 'b', False),
              L([(30, 54), (36, 50), (32, 46)], OUTC, 'f', False, False, 1.2), L([(70, 54), (64, 50), (68, 46)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(60, 44), (80, 42), (90, 28), (82, 8), (92, -12, 1), (70, -4), (58, -26, 1), (46, -6), (22, -14, 1), (20, 4), (4, 20), (-10, 30, 1), (4, 40),
                        (6, 66), (16, 82), (30, 80), (44, 64)])),
             L(outline([(6, 40), (26, 40), (30, 74), (12, 74)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (8, 40), (-8, 18, 1), (12, 20), (12, -2), (24, -22, 1), (34, -2), (50, -12), (60, -26, 1), (66, -2), (86, -8, 1), (88, 12), (108, 12, 1),
                        (92, 30), (92, 50), (84, 80), (50, 96, 1)])),
             L(outline([(56, -6), (86, 8), (92, 46), (84, 76), (56, 90)]), 'shade', 'b', False),
             L([(30, 50), (50, 92), (70, 50)], 'deep', 'b', False, False, 1.2)],
}

# Jean Darc: melena castaño rojizo en casco cuadrado hasta la barbilla con flequillo recto, dos moñitos de cuernos arriba;
# ojos amarillos de pupila fina con marcas debajo
CHARS['jean-darc'] = {
    'body': 'chica', 'pal': pal('#b0583a', '#fcdcc0', iris='#d8c81e', shade='#8a3e28'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 106), (2, 60), (6, 26), (14, 4), (22, -4), (34, 4), (50, 0), (66, 4), (78, -4), (86, 4), (94, 26), (98, 60), (94, 106), (82, 100), (84, 68),
                         (16, 68), (18, 100)])),
              L(outline([(62, 4), (86, 10), (96, 50), (92, 100), (84, 94)]), 'shade', 'b', False),
              fringe([(8, 74), (8, 42), (20, 22), (50, 16), (80, 22), (92, 42), (92, 74), (84, 66), (16, 66)]),
              strand([(30, 30), (30, 64)], 'shade', 'f', 1.0), strand([(50, 20), (50, 64)], 'shade', 'f', 1.0), strand([(70, 30), (70, 64)], 'shade', 'f', 1.0),
              L([(28, 86), (32, 90)], OUTC, 'f', False, False, 1.0), L([(72, 86), (68, 90)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(52, 100), (54, 70), (66, 62), (84, 62), (94, 40), (90, 16), (76, 2), (70, -8), (58, -2), (34, -2), (12, 12), (2, 44), (2, 100), (28, 104)])),
             L(outline([(4, 44), (40, 46), (46, 100), (8, 100)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 16), (96, 42), (94, 66), (82, 64), (72, 40)])],
    'back': [L(outline([(4, 100), (2, 60), (6, 26), (14, 4), (22, -4), (34, 4), (50, 0), (66, 4), (78, -4), (86, 4), (94, 26), (98, 60), (96, 100), (76, 104), (50, 98),
                        (24, 104)])),
             L(outline([(56, 2), (86, 10), (96, 56), (94, 100), (66, 102)]), 'shade', 'b', False)],
}

# Bobby Bruce: pelo castaño muy oscuro en una masa de pinchos altísima hacia arriba, que le baja por los lados de la cara en
# patillas anchas; cara de mono con el entrecejo en pico, ojos rojos y sonrisa de dientes
CHARS['bobby-bruce'] = {
    'body': 'corpulento', 'pal': pal('#3a2228', '#f0b884', iris='#a01e1e', shade='#2a1820'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 104, 'hairline': [(14, 100), (16, 60), (30, 54), (50, 40), (70, 54), (84, 60), (86, 100)], 'big_ears': 2},
    'front': [L(outline([(12, 100), (10, 40), (16, 0), (24, -24, 1), (34, -2), (42, -30, 1), (50, -6), (62, -32, 1), (66, -4), (78, -22, 1), (84, 6), (90, 40), (88, 100),
                         (78, 96), (80, 64), (20, 64), (22, 96)])),
              L(outline([(60, -10), (82, 4), (90, 50), (88, 96), (80, 60)]), 'shade', 'b', False),
              strand([(40, 0), (50, 36)], 'deep', 'b', 1.0), strand([(60, 0), (50, 36)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 50), (80, 44), (88, 28), (82, 4), (92, -18, 1), (70, -6), (60, -30, 1), (48, -8), (26, -26, 1), (24, -4), (6, 14), (2, 50), (8, 76), (22, 88),
                        (40, 82), (50, 66)])),
             L(outline([(52, 50), (66, 52), (76, 76), (64, 96), (56, 80)]), 'mid', 'f'),
             L(outline([(6, 40), (28, 40), (32, 80), (12, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 84), (10, 40), (16, 0), (24, -24, 1), (34, -2), (42, -30, 1), (50, -6), (62, -32, 1), (66, -4), (78, -22, 1), (84, 6), (90, 40), (86, 84),
                        (50, 92)])),
             L(outline([(56, -8), (82, 4), (90, 50), (84, 82), (60, 90)]), 'shade', 'b', False),
             strand([(36, 0), (40, 40), (36, 80)], 'deep', 'b', 1.0), strand([(64, 0), (60, 40), (64, 80)], 'deep', 'b', 1.0)],
}

# Hanny Bawl: pelo verde azulado oscuro con un moño alto del que salen tres mechones como hojas, flequillo de picos y la
# nuca recogida; ojos blancos rasgados y orejas puntiagudas
CHARS['hanny-bawl'] = {
    'body': 'bajito', 'pal': pal('#2e5a5a', '#fcdcc0', shade='#1e3e3e', light='#5a8a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(42, 6), (40, -10), (50, -30, 1), (60, -10), (58, 6)])),
              L(outline([(40, 4), (24, -6), (10, -12, 1), (22, 6)])), L(outline([(60, 4), (76, -6), (90, -12, 1), (78, 6)])),
              L(outline([(16, 76), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 76), (80, 60), (20, 60)])),
              L(outline([(60, 8), (84, 18), (90, 46), (82, 66)]), 'shade', 'b', False), L(ell(44, -12, 3, 8), 'light', 'b', False),
              fringe([(14, 66), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (86, 66), (78, 54), (72, 64, 1), (66, 48), (58, 60, 1), (52, 46), (46, 60, 1), (40, 46),
                      (32, 62, 1), (24, 50), (18, 62, 1)])],
    'side': [L(outline([(54, 60), (60, 48), (80, 46), (92, 32), (86, 12), (64, 0), (36, 0), (14, 12), (4, 40), (8, 72), (24, 84), (40, 78)])),
             L(outline([(34, 4), (30, -14), (40, -32, 1), (48, -14), (50, 2)])), L(outline([(30, 4), (10, -6), (-4, -8, 1), (14, 8)])),
             L(outline([(4, 40), (28, 42), (30, 76), (10, 72)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (92, 60, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(42, 6), (38, -10), (50, -30, 1), (62, -10), (58, 6)]), 'shade'),
             L(outline([(40, 4), (24, -6), (8, -12, 1), (22, 6)]), 'shade'), L(outline([(60, 4), (76, -6), (92, -12, 1), (78, 6)]), 'shade'),
             L(outline([(16, 82), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 82), (50, 90)])),
             L(outline([(56, 8), (84, 18), (90, 50), (82, 80), (60, 88)]), 'shade', 'b', False)],
}
