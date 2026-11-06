"""Teikoku Gakuen (IE1): pelo, rasgos y accesorios de cada jugador, con sus modelos 3D como referencia."""
from chars import (BACK_SKULL, CHARS, DOME, L, OUTC, blob, bumpy, caps, clumps, dread, ell, fat, mirror, outline, pal, sheen,
                   spk, strand)
from heads import quad

DARK = (36, 24, 22, 255)
WHITE = (255, 255, 255, 255)


def mustache(y=86, w=11, c='mid'):
    return L(blob([(50 - w, y + 2), (44, y - 1.5), (50, y), (56, y - 1.5), (50 + w, y + 2), (52, y + 3), (48, y + 3)], 5), c, 'f')


def round_glasses(y=75, r=7.5, c=(70, 70, 80, 255)):
    out = []
    for cx in (36, 64):
        pts = [(cx + r * __import__('math').cos(i / 18 * 6.283), y + r * __import__('math').sin(i / 18 * 6.283)) for i in range(19)]
        out.append(L(pts, c, 'f', False, False, 1.4))
    out.append(L([(43.5, y - 1), (56.5, y - 1)], c, 'f', False, False, 1.2))
    return out


# ------------------------------------------------------------------ Joseph King (portero): pelo rojizo de pinchos grandes y
# desordenados, un mechón que le cae entre los ojos y dos marcas en las mejillas
CHARS['joseph-king'] = {
    'body': 'normal', 'pal': pal('#8e3c16', '#f2b886', iris='#3a5a6a', mark='#d0702a', light='#b85a26'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    # el pelo barrido hacia su derecha (izquierda de la imagen) en pinchos largos, con mechones del flequillo que le cruzan
    # la cara en diagonal hasta la nariz, y dos rayas naranjas en cada mejilla
    'front': [L(outline([(12, 72), (-8, 80, 1), (6, 60), (-20, 56, 1), (2, 40), (-26, 30, 1), (4, 22), (-16, 6, 1), (14, 6), (8, -14, 1), (30, -4),
                         (26, -24, 1), (50, -6), (64, -12, 1), (72, 4), (88, 10), (96, 28), (98, 50), (92, 72, 1), (86, 62), (84, 72)])),
              L(outline([(60, 0), (86, 12), (94, 30), (96, 50), (88, 60), (76, 30)]), 'shade', 'b', False),
              L(outline([(-12, 32, 1), (10, 22), (30, 10), (10, 30)]), 'light', 'b', False),
              L([(26, 80), (32, 92)], 'mark', 'f', False, False, 1.8), L([(31, 79), (37, 91)], 'mark', 'f', False, False, 1.8),
              L([(74, 80), (68, 92)], 'mark', 'f', False, False, 1.8), L([(69, 79), (63, 91)], 'mark', 'f', False, False, 1.8),
              L(outline([(14, 64), (16, 40), (34, 24), (60, 18), (80, 26), (88, 44), (90, 64, 1), (80, 54), (66, 74, 1), (60, 52), (47, 92, 1), (44, 60),
                         (32, 72, 1), (30, 54), (20, 66, 1)]), 'mid', 'f'),
              L(outline([(56, 22), (80, 28), (88, 46), (82, 56), (66, 40)]), 'shade', 'f', False),
              strand([(62, 24), (52, 50), (47, 88)], 'deep', 'f', 1.0), strand([(70, 30), (64, 52), (66, 70)], 'deep', 'f', 1.0)],
    'side': [L(blob([(44, 92), (22, 88), (10, 66), (10, 40), (24, 18), (52, 10), (76, 16), (90, 34), (84, 48), (66, 50), (56, 56), (52, 72)])),
             spk((14, 44), (26, 26), (-12, 20), 7), spk((24, 26), (44, 16), (6, -6), 7), spk((44, 16), (62, 14), (46, -10), 6),
             spk((12, 64), (20, 48), (-10, 60), 5), spk((14, 80), (28, 88), (0, 96), 4),
             L(blob([(16, 50), (18, 74), (38, 88), (28, 62)], 6), 'shade', 'b', False),
             spk((56, 26), (84, 36), (92, 70), 6, z='f', light_left=False), spk((52, 54), (60, 54), (56, 74), 2, z='f'),
             L([(80, 82), (86, 85)], 'mark', 'f', False, False, 1.6)],
    'back': [L(outline([(88, 72), (108, 80, 1), (94, 60), (120, 56, 1), (98, 40), (126, 30, 1), (96, 22), (116, 6, 1), (86, 6), (92, -14, 1), (70, -4),
                        (74, -24, 1), (50, -6), (36, -12, 1), (28, 4), (12, 10), (4, 28), (2, 50), (6, 80), (30, 92), (60, 94), (80, 88)])),
             L(outline([(4, 30), (14, 12), (30, 6), (28, 50), (14, 86), (4, 70)]), 'shade', 'b', False),
             L(outline([(112, 32, 1), (90, 22), (70, 10), (90, 30)]), 'light', 'b', False),
             strand([(40, 4), (70, 30), (100, 54)], 'deep', 'b', 1.2), strand([(30, 30), (60, 60), (90, 76)], 'deep', 'b', 1.2)],
}

# ------------------------------------------------------------------ Peter Drent: afro oscuro, gorro gris con gafas de aviador en
# la frente; corpulento y piel morena, sonrisa
PETER_CAP = blob([(14, 56), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (86, 56), (50, 52)])
CHARS['peter-drent'] = {
    'body': 'corpulento', 'pal': pal('#2c2640', '#8e5c3c', cap='#c4c4cc', cap_d='#9a9aa6', rim='#7ab8b8', lens='#1e3050', lens_l='#5a7aa0', mark='#c83030'),
    # casco gris pegado a la cabeza hasta las cejas, con unas gafas redondas de cristal azul oscuro opaco unidas al casco
    # que le tapan los ojos; afro a los lados, sonrisa enorme con dientes
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 90, 'hairline': False},
    'front': [L(bumpy(10, 72, 16, 22, 8, 0.1)), L(bumpy(90, 72, 16, 22, 8, 0.1)),
              L(blob([(16, 70), (14, 40), (26, 16), (50, 8), (74, 16), (86, 40), (84, 70), (70, 66), (50, 64), (30, 66)]), 'cap', 'f'),
              L(blob([(62, 14), (84, 36), (84, 66), (72, 62)], 6), 'cap_d', 'f', False),
              L([(66, 22), (72, 30)], 'mark', 'f', False, False, 1.6), L([(70, 20), (76, 28)], 'mark', 'f', False, False, 1.6),
              L([(26, 74), (18, 70)], 'cap_d', 'f', False, False, 2.4), L([(74, 74), (82, 70)], 'cap_d', 'f', False, False, 2.4),
              L(ell(36, 75, 10, 9), 'rim', 'f', ln=True), L(ell(64, 75, 10, 9), 'rim', 'f', ln=True),
              L(ell(36, 75, 7, 6.4), 'lens', 'f', False), L(ell(64, 75, 7, 6.4), 'lens', 'f', False),
              L(ell(33, 72, 2.4, 1.8), 'lens_l', 'f', False), L(ell(61, 72, 2.4, 1.8), 'lens_l', 'f', False),
              L([(46, 75), (54, 75)], 'rim', 'f', False, False, 1.6)],
    'side': [L(bumpy(22, 66, 26, 30, 10, 0.1)), L(bumpy(16, 72, 14, 16, 6), 'shade', 'b', False),
             L(blob([(16, 66), (14, 34), (30, 12), (54, 6), (76, 14), (88, 34), (90, 66), (70, 64), (50, 62)]), 'cap', 'f'),
             L(blob([(16, 34), (30, 14), (34, 44), (20, 60)], 6), 'cap_d', 'f', False),
             L([(84, 72), (62, 68)], 'cap_d', 'f', False, False, 2.4),
             L(ell(85, 75, 6, 8), 'rim', 'f', ln=True), L(ell(86, 75, 3.6, 5.6), 'lens', 'f', False)],
    'back': [L(bumpy(50, 70, 46, 30, 14, 0.08)), L(bumpy(66, 78, 22, 16, 8), 'shade', 'b', False),
             L(blob([(16, 70), (14, 40), (26, 16), (50, 8), (74, 16), (86, 40), (84, 70), (50, 74)]), 'cap', 'f'),
             L(blob([(58, 14), (84, 34), (84, 68), (68, 70)], 6), 'cap_d', 'f', False)],
}

# ------------------------------------------------------------------ Ben Simmons: melena lisa granate hasta la mandíbula con
# flequillo recto hasta las cejas, mirada de enfado y bigote
CHARS['ben-simmons'] = {
    'body': 'normal', 'pal': pal('#5e2212', '#e8b080'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob([(10, 98), (8, 46), (18, 18), (50, 8), (82, 18), (92, 46), (90, 98), (80, 96), (80, 66), (20, 66), (20, 96)])),
              L(blob([(76, 30), (90, 50), (88, 96), (80, 94)], 6), 'shade', 'b', False), sheen(26, 56, 20, 3),
              L(blob([(16, 66), (16, 46), (24, 26), (50, 18), (76, 26), (84, 46), (84, 66)]), 'mid', 'f'),
              L(blob([(60, 22), (80, 34), (84, 64), (70, 64)], 6), 'shade', 'f', False),
              strand([(30, 40), (30, 64)], 'shade', 'f', 1.0), strand([(46, 40), (46, 64)], 'shade', 'f', 1.0), strand([(62, 40), (62, 64)], 'shade', 'f', 1.0),
              mustache(86, 12)],
    'side': [L(blob([(46, 98), (16, 98), (8, 62), (12, 30), (34, 12), (64, 12), (84, 28), (90, 66), (74, 66), (60, 60), (54, 74), (52, 96)])),
             L(blob([(12, 50), (14, 92), (40, 96), (26, 70)], 6), 'shade', 'b', False), sheen(30, 62, 18, 3),
             L(blob([(84, 86), (91, 84), (92, 89), (84, 90)], 3), 'mid', 'f')],
    'back': [L(blob([(10, 98), (8, 46), (18, 18), (50, 8), (82, 18), (92, 46), (90, 98), (50, 102)])),
             L(blob([(56, 14), (86, 34), (90, 96), (66, 100)], 6), 'shade', 'b', False), sheen(26, 56, 20, 3),
             strand([(36, 40), (34, 96)], 'shade', 'b', 1.0), strand([(64, 40), (66, 96)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Gus Martin: pelo castaño peinado hacia atrás con un rizo en
# espiral sobre la frente, gafas redondas, sonrisa enorme de oreja a oreja y orejas puntiagudas
GUS_CURL = blob([(42, 62), (32, 50), (34, 36), (48, 28), (60, 34), (62, 46), (54, 54), (46, 48), (50, 42)], 6)
CHARS['gus-martin'] = {
    'body': 'delgado', 'pal': pal('#4a2e14', '#f6d6b4', lens=(248, 248, 248, 255), lens_d=(214, 218, 226, 255)),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 1, 'ear_out': 3, 'hairline': (56, 46)},
    # gafas redondas blancas y opacas (no se le ven los ojos)
    'front': [L(blob([(16, 60), (14, 36), (26, 16), (50, 10), (74, 16), (86, 36), (84, 60), (50, 50)])),
              L(blob([(58, 14), (84, 32), (84, 58), (70, 52)], 6), 'shade', 'b', False), sheen(28, 54, 18, 3),
              L(GUS_CURL, 'mid', 'f', ln=True), L(blob([(44, 36), (54, 34), (56, 44), (48, 44)], 3), 'shade', 'f', False),
              L(outline([(22, 84, 1), (50, 90), (78, 84, 1), (68, 98), (50, 103), (32, 98)]), WHITE, 'f', ln=True),
              L(quad((26, 88), (50, 96), (74, 88)), OUTC, 'f', False, False, 0.8),
              L(ell(36, 75, 9, 8.4), 'lens', 'f', ln=True), L(ell(64, 75, 9, 8.4), 'lens', 'f', ln=True),
              L([(31, 71), (36, 69)], 'lens_d', 'f', False, False, 1.4), L([(59, 71), (64, 69)], 'lens_d', 'f', False, False, 1.4),
              L([(45, 74), (55, 74)], OUTC, 'f', False, False, 1.3), L([(27, 73), (18, 70)], OUTC, 'f', False, False, 1.3),
              L([(73, 73), (82, 70)], OUTC, 'f', False, False, 1.3)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(blob([(16, 48), (20, 74), (38, 86), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 16, 3),
             L(blob([(74, 44), (82, 36), (90, 40), (88, 47), (82, 48)], 6), 'mid', 'f', ln=True),
             L(ell(84, 75, 5.6, 8), 'lens', 'f', ln=True), L([(78, 74), (50, 72)], OUTC, 'f', False, False, 1.3)],
    'back': [L(blob([(16, 66), (14, 38), (26, 16), (50, 10), (74, 16), (86, 38), (84, 66), (70, 86), (50, 92), (30, 86)])),
             L(blob([(58, 16), (86, 38), (84, 66), (66, 86)], 6), 'shade', 'b', False), sheen(28, 56, 20, 3),
             strand([(40, 30), (38, 80)], 'shade', 'b', 1.0), strand([(60, 30), (62, 80)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Bob Carlton: muy corpulento, pelo castaño corto de pinchos
# cortos hacia arriba, piel morena y cara de enfado
CHARS['bob-carlton'] = {
    'body': 'corpulento', 'pal': pal('#8a5a20', '#c8905a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(blob([(16, 62), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 62)])),
              spk((16, 38), (30, 24), (6, 8), 5), spk((28, 24), (46, 18), (26, 0), 5), spk((44, 18), (60, 18), (54, -4), 5),
              spk((58, 20), (74, 26), (78, 2), 5, light_left=False), spk((70, 28), (86, 40), (96, 12), 5, light_left=False),
              L(blob([(60, 18), (86, 36), (84, 60), (70, 56)], 6), 'shade', 'b', False),
              spk((30, 46), (46, 44), (36, 58), 2, z='f'), spk((52, 44), (68, 46), (62, 58), 2, z='f', light_left=False)],
    'side': [L(blob([(44, 90), (24, 86), (14, 64), (16, 40), (30, 22), (56, 16), (78, 24), (86, 40), (70, 46), (58, 50), (52, 64), (50, 80)])),
             spk((18, 42), (30, 26), (0, 18), 5), spk((28, 26), (46, 18), (18, 0), 5), spk((46, 18), (64, 18), (48, -4), 5),
             spk((62, 20), (78, 28), (80, 4), 5, light_left=False), spk((14, 62), (20, 48), (-2, 52), 4),
             L(blob([(18, 52), (20, 76), (38, 86), (28, 62)], 6), 'shade', 'b', False)],
    'back': [L(blob([(16, 68), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 68), (68, 84), (32, 84)])),
             spk((16, 38), (30, 24), (6, 8), 5), spk((28, 24), (46, 18), (26, 0), 5), spk((44, 18), (60, 18), (54, -4), 5),
             spk((58, 20), (74, 26), (78, 2), 5, light_left=False), spk((70, 28), (86, 40), (96, 12), 5, light_left=False),
             spk((22, 74), (40, 82), (24, 94), 3), spk((40, 84), (60, 84), (50, 96), 3), spk((60, 82), (78, 74), (78, 94), 3, light_left=False),
             L(blob([(58, 20), (86, 40), (84, 66), (66, 82)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Alan Master: pelo morado de pinchos largos que salen en
# todas direcciones (dos grandes como cuernos), auriculares grises, un lunar en la frente y ojos azules
ALAN_SPIKES = [spk((12, 52), (22, 40), (-14, 34), 6), spk((18, 36), (32, 24), (0, 6), 6), spk((30, 24), (46, 16), (24, -14), 6),
               spk((46, 16), (60, 18), (54, -10), 5, light_left=False), spk((60, 20), (74, 28), (84, -12), 6, light_left=False),
               spk((74, 32), (86, 42), (110, 22), 6, light_left=False), spk((80, 50), (90, 60), (108, 60), 4, light_left=False),
               spk((10, 62), (18, 70), (-6, 76), 4)]
CHARS['alan-master'] = {
    'body': 'normal', 'pal': pal('#6a5a7c', '#f6caa0', iris='#3a8ac8', phone='#8a8a8a', phone_d='#5a5a5a', mole='#3a2a2a'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'hairline': (60, 52)},
    'front': [L(blob([(12, 64), (10, 40), (22, 18), (50, 12), (78, 18), (90, 40), (88, 64)]))] + ALAN_SPIKES + [
              L(blob([(60, 16), (88, 36), (88, 62), (74, 58)], 6), 'shade', 'b', False),
              spk((18, 48), (36, 44), (24, 70), 4, z='f'), spk((34, 44), (52, 42), (42, 66), 4, z='f'),
              spk((50, 42), (68, 44), (62, 66), 4, z='f', light_left=False), spk((66, 46), (84, 50), (82, 72), 4, z='f', light_left=False),
              L(quad((16, 66), (50, -4), (84, 66)), 'phone_d', 'b', False, False, 2.4),
              L(ell(15, 72, 6, 9), 'phone', 'f', ln=True), L(ell(85, 72, 6, 9), 'phone', 'f', ln=True),
              L(ell(15, 72, 3, 5), 'phone_d', 'f', False), L(ell(85, 72, 3, 5), 'phone_d', 'f', False),
              L(ell(40, 62, 1.6, 1.6), 'mole', 'f', False)],
    'side': [L(blob([(44, 92), (22, 88), (12, 66), (12, 40), (26, 18), (54, 10), (78, 18), (88, 36), (74, 44), (60, 48), (52, 62), (50, 80)])),
             spk((14, 44), (26, 26), (-16, 20), 6), spk((24, 26), (44, 16), (4, -10), 6), spk((44, 16), (62, 14), (52, -14), 5),
             spk((60, 18), (76, 26), (88, -8), 5, light_left=False), spk((12, 64), (20, 50), (-14, 58), 5), spk((14, 80), (28, 88), (-2, 98), 4),
             L(blob([(16, 50), (18, 76), (38, 88), (28, 62)], 6), 'shade', 'b', False),
             spk((56, 26), (84, 38), (92, 72), 6, z='f', light_left=False),
             L(blob([(46, 30), (56, 30), (54, 64), (46, 66)], 4), 'phone_d', 'f'), L(ell(48, 72, 9, 9), 'phone', 'f'), L(ell(48, 72, 5, 5), 'phone_d', 'f', False)],
    'back': [L(blob([(12, 66), (10, 40), (22, 18), (50, 12), (78, 18), (90, 40), (88, 66), (74, 88), (50, 94), (26, 88)]))] + ALAN_SPIKES + [
             spk((16, 76), (32, 86), (6, 100), 5), spk((32, 88), (50, 92), (36, 110), 5), spk((50, 92), (68, 88), (66, 110), 5, light_left=False),
             spk((68, 86), (84, 76), (96, 100), 5, light_left=False),
             L(blob([(58, 18), (88, 40), (86, 70), (68, 88)], 6), 'shade', 'b', False),
             L(ell(15, 72, 6, 9), 'phone', 'f', ln=True), L(ell(85, 72, 6, 9), 'phone', 'f', ln=True)],
}

# ------------------------------------------------------------------ Herman Waldon: pelo largo peinado hacia atrás (frente
# despejada) que cae liso hasta los hombros, ojos naranjas y mirada dura
CHARS['herman-waldon'] = {
    'body': 'normal', 'pal': pal('#a07a6a', '#f6c49a', iris='#c86020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 40)},
    'front': [L(blob([(10, 118), (8, 50), (18, 20), (50, 10), (82, 20), (92, 50), (90, 118), (80, 116), (82, 62), (18, 62), (20, 116)])),
              L(blob([(70, 20), (90, 50), (88, 114), (80, 112)], 6), 'shade', 'b', False),
              strand([(36, 14), (34, 44)], 'shade', 'b', 1.0), strand([(50, 12), (50, 42)], 'shade', 'b', 1.0), strand([(64, 14), (66, 44)], 'shade', 'b', 1.0),
              sheen(28, 50, 18, 3)],
    'side': [L(blob([(54, 46), (40, 50), (30, 70), (26, 110), (8, 114), (6, 70), (12, 30), (34, 12), (62, 12), (80, 26), (82, 40)])),
             L(blob([(12, 50), (10, 100), (24, 108), (22, 70)], 6), 'shade', 'b', False), sheen(30, 62, 18, 3),
             strand([(70, 22), (40, 26), (20, 50)], 'shade', 'b', 1.0), strand([(74, 34), (44, 38), (26, 70)], 'shade', 'b', 1.0)],
    'back': [L(blob([(10, 118), (8, 50), (18, 20), (50, 10), (82, 20), (92, 50), (90, 118), (50, 122)])),
             L(blob([(56, 16), (86, 34), (90, 116), (66, 120)], 6), 'shade', 'b', False), sheen(28, 52, 20, 3),
             strand([(36, 20), (32, 116)], 'shade', 'b', 1.0), strand([(50, 14), (50, 118)], 'deep', 'b', 1.0), strand([(66, 20), (70, 116)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ John Bloom: media melena verde oliva con un flequillo largo
# que le tapa el ojo derecho y cae en punta hasta la barbilla
CHARS['john-bloom'] = {
    'body': 'normal', 'pal': pal('#6c8442', '#f8d0a8', mask='#f0e6c0'),
    'face': {'eyes': 'sharp', 'mouth': 'none', 'hairline': (62, 52)},
    'front': [L(blob([(12, 92), (8, 46), (18, 18), (50, 8), (82, 18), (92, 46), (90, 92), (80, 88), (80, 62), (20, 62), (20, 88)])),
              L(blob([(70, 20), (90, 48), (88, 90), (80, 86)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              L(outline([(16, 82), (36, 80), (56, 84), (62, 104), (50, 106), (30, 100), (18, 92)]), 'mask', 'f', ln=True),
              spk((16, 46), (34, 42), (22, 70), 4, z='f'),
              L(blob([(32, 40), (58, 34), (80, 42), (88, 66), (84, 96), (74, 100), (66, 80), (56, 62), (42, 52)]), 'mid', 'f', ln=True),
              L(blob([(64, 44), (82, 54), (82, 92), (74, 96), (70, 70)], 6), 'shade', 'f', False)],
    'side': [L(blob([(48, 98), (20, 94), (8, 66), (10, 38), (26, 16), (54, 8), (78, 16), (90, 34), (78, 44), (62, 48), (54, 62), (52, 84)])),
             L(blob([(12, 50), (14, 88), (40, 96), (26, 66)], 6), 'shade', 'b', False), sheen(30, 60, 14, 3),
             L(outline([(68, 84), (88, 80), (92, 96), (80, 104), (66, 100)]), 'mask', 'f', ln=True),
             spk((56, 24), (86, 36), (90, 88), 6, z='f', light_left=False)],
    'back': [L(blob([(12, 92), (8, 46), (18, 18), (50, 8), (82, 18), (92, 46), (90, 92), (70, 100), (30, 100)])),
             L(blob([(56, 14), (86, 34), (88, 90), (66, 98)], 6), 'shade', 'b', False), sheen(26, 54, 20, 3),
             strand([(40, 30), (36, 96)], 'shade', 'b', 1.0), strand([(62, 30), (66, 96)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Daniel Hatch: rastas largas peinadas hacia atrás que caen
# hasta los hombros, piel morena y sonrisa confiada
CHARS['daniel-hatch'] = {
    'body': 'normal', 'pal': pal('#3e2a1e', '#9e6c48'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': (60, 44)},
    'front': [L(blob([(14, 66), (12, 40), (24, 16), (50, 10), (76, 16), (88, 40), (86, 66)])),
              L(blob([(58, 14), (86, 34), (86, 62), (72, 58)], 6), 'shade', 'b', False)]
             + [x for k in range(5) for x in dread((14 + k * 4, 50 + k * 3), (8 + k * 4, 112), 4.4)]
             + [x for k in range(5) for x in dread((86 - k * 4, 50 + k * 3), (92 - k * 4, 112), 4.4)]
             + [strand([(30, 18), (34, 42)], 'deep', 'b', 1.0), strand([(50, 14), (50, 40)], 'deep', 'b', 1.0), strand([(70, 18), (66, 42)], 'deep', 'b', 1.0)],
    'side': [L(blob([(54, 48), (36, 54), (24, 70), (12, 64), (12, 34), (32, 14), (60, 12), (80, 24), (82, 40)]))]
            + [x for k in range(5) for x in dread((16 + k * 6, 44 + k * 4), (4 + k * 6, 114), 4.4)]
            + [strand([(70, 22), (40, 22), (20, 40)], 'deep', 'b', 1.0), strand([(74, 34), (46, 34), (26, 56)], 'deep', 'b', 1.0)],
    'back': [L(blob([(14, 66), (12, 40), (24, 16), (50, 10), (76, 16), (88, 40), (86, 66), (50, 72)]))]
            + [x for k in range(8) for x in dread((18 + k * 9, 40), (16 + k * 9.5, 114 - abs(k - 3.5) * 2), 4.6)],
}

# ------------------------------------------------------------------ David Samford: melena larga blanca verdosa hasta los
# hombros, cinta oscura en la frente, parche en el ojo y ojo rojo
CHARS['david-samford'] = {
    'body': 'normal', 'pal': pal('#d6eee6', '#d8a070', iris='#a02a2a', band='#4a3a30', patch='#3a3a42'),
    'face': {'eyes': 'sharp', 'mouth': 'line', 'hairline': (64, 56)},
    'front': [L(blob([(10, 112), (6, 50), (16, 20), (50, 10), (84, 20), (94, 50), (90, 112), (80, 110), (82, 64), (18, 64), (20, 110)])),
              L(blob([(70, 20), (92, 50), (90, 108), (80, 106)], 6), 'shade', 'b', False), sheen(24, 50, 22, 3),
              spk((14, 48), (34, 44), (20, 82), 4, z='f'), spk((32, 44), (52, 42), (42, 66), 4, z='f'),
              spk((50, 42), (68, 44), (60, 64), 4, z='f', light_left=False), spk((66, 46), (88, 50), (84, 88), 4, z='f', light_left=False),
              L(ell(36, 76, 10, 8.5), 'patch', 'f'), L(ell(33, 73, 3.6, 2.2), (110, 110, 120, 255), 'f', False),
              # correa del parche: del parche sube en diagonal por la frente hasta el lado derecho de la cabeza
              L([(44, 70), (60, 56), (78, 44), (90, 40)], 'band', 'f', False, False, 1.8), L([(27, 72), (14, 70)], 'band', 'f', False, False, 1.8)],
    'side': [L(blob([(54, 46), (36, 52), (28, 76), (24, 112), (6, 110), (6, 66), (12, 32), (34, 12), (62, 10), (82, 22), (88, 40)])),
             L(blob([(10, 50), (8, 104), (22, 108), (22, 70)], 6), 'shade', 'b', False), sheen(32, 62, 16, 3),
             spk((56, 26), (86, 38), (90, 70), 5, z='f', light_left=False),
             L([(10, 40), (40, 40), (66, 46), (82, 66), (84, 74)], 'band', 'f', False, False, 1.8), L(ell(86, 76, 4, 6.5), 'patch', 'f')],
    'back': [L(blob([(10, 112), (6, 50), (16, 20), (50, 10), (84, 20), (94, 50), (90, 112), (50, 118)])),
             L(blob([(56, 16), (88, 36), (90, 110), (66, 116)], 6), 'shade', 'b', False), sheen(26, 54, 22, 3),
             strand([(34, 50), (30, 110)], 'shade', 'b', 1.0), strand([(50, 50), (50, 114)], 'shade', 'b', 1.0), strand([(66, 50), (70, 110)], 'deep', 'b', 1.0),
             L([(8, 44), (50, 40), (92, 44)], 'band', 'f', False, False, 1.8)],
}

# ------------------------------------------------------------------ Derek Swing: pelo castaño en forma de alas abiertas con un
# mechón en punta arriba, ojos blancos redondos, pinturas naranja y azul en la cara y bufanda naranja
DEREK_WINGS = blob([(12, 66), (-10, 40), (-18, 20), (6, 22), (24, 16), (44, 10), (50, -2), (56, 10), (76, 16), (94, 22), (118, 20), (110, 40), (88, 66), (50, 56)])
CHARS['derek-swing'] = {
    'body': 'bajito', 'pal': pal('#6c5a30', '#f6c690', paint='#e88a40', paint2='#4aa0a8', scarf='#e07020', scarf_d='#b45414'),
    # ojos: dos óvalos blancos grandes sin pupila; pintura naranja que baja por el ojo izquierdo hasta la mejilla y
    # pintura azul por el lado derecho; nariz pequeña y sonrisa; pelo en alas con un pincho arriba y bufanda naranja
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 54)},
    'front': [L(DEREK_WINGS), L(blob([(60, 16), (110, 26), (100, 42), (82, 56)], 6), 'shade', 'b', False),
              L(blob([(-10, 28), (20, 22), (30, 30), (6, 36)], 6), 'light', 'b', False),
              strand([(-6, 30), (20, 40)], 'deep', 'b', 1.2), strand([(106, 30), (80, 40)], 'deep', 'b', 1.2),
              L(blob([(30, 54), (38, 54), (36, 74), (34, 96), (28, 96), (30, 74)], 4), 'paint', 'f', False),
              L(blob([(64, 54), (72, 54), (72, 76), (68, 96), (62, 94), (66, 76)], 4), 'paint2', 'f', False),
              L(ell(36, 76, 8.4, 7.4), WHITE, 'f', ln=True), L(ell(64, 76, 8.4, 7.4), WHITE, 'f', ln=True),
              L([(48, 86), (50, 84), (52, 86)], OUTC, 'f', False, False, 1.0),
              L(blob([(18, 100), (50, 106), (82, 100), (84, 112), (50, 118), (16, 112)], 5), 'scarf', 'f', ln=True),
              L(blob([(50, 108), (82, 102), (82, 110), (50, 116)], 4), 'scarf_d', 'f', False)],
    'side': [L(blob([(44, 90), (22, 86), (14, 60), (-12, 36), (-18, 14), (10, 20), (30, 12), (48, 0), (56, 12), (78, 18), (88, 36), (70, 46), (56, 54), (50, 76)])),
             L(blob([(-10, 22), (20, 22), (30, 34), (4, 34)], 6), 'light', 'b', False), L(blob([(14, 52), (18, 76), (38, 86), (26, 62)], 6), 'shade', 'b', False),
             L(blob([(76, 54), (84, 56), (84, 76), (82, 96), (76, 94), (78, 74)], 4), 'paint', 'f', False),
             L(ell(83, 76, 5, 7.4), WHITE, 'f', ln=True),
             L(blob([(46, 98), (84, 100), (84, 110), (46, 112)], 5), 'scarf', 'f', ln=True),
             L(blob([(46, 104), (30, 112), (20, 128), (30, 128), (44, 114)], 4), 'scarf_d', 'f', ln=True)],
    'back': [L(DEREK_WINGS), L(blob([(56, 20), (110, 26), (100, 42), (80, 60)], 6), 'shade', 'b', False),
             L(blob([(18, 58), (82, 58), (76, 84), (50, 92), (24, 84)])), L(blob([(54, 60), (80, 60), (74, 82), (56, 90)], 6), 'shade', 'b', False),
             L(blob([(16, 100), (84, 100), (84, 112), (16, 112)], 5), 'scarf', 'f', ln=True),
             L(blob([(44, 106), (56, 106), (60, 130), (40, 130)], 4), 'scarf_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Cliff Tomlinson: pelo verde azulado de puntas barridas hacia
# un lado, con un mechón largo hacia fuera a cada lado
CHARS['cliff-tomlinson'] = {
    'body': 'normal', 'pal': pal('#4a8a82', '#f6caa0', iris='#2a2a3a'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'hairline': (62, 54)},
    'front': [L(blob([(12, 66), (10, 40), (22, 16), (50, 8), (78, 14), (92, 36), (90, 64)])),
              spk((10, 56), (22, 48), (-12, 52), 5), spk((80, 60), (90, 52), (108, 74), 5, light_left=False),
              spk((54, 12), (72, 14), (78, -8), 5, light_left=False), spk((38, 12), (54, 10), (40, -8), 5),
              L(blob([(60, 16), (90, 36), (90, 60), (76, 58)], 6), 'shade', 'b', False), sheen(22, 46, 22, 3),
              spk((60, 34), (80, 42), (20, 70), 7, z='f'), spk((52, 40), (70, 42), (40, 70), 4, z='f'),
              spk((70, 44), (88, 50), (82, 70), 3, z='f', light_left=False)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (12, 38), (26, 16), (54, 6), (78, 14), (90, 34), (76, 44), (60, 48), (52, 62), (50, 80)])),
             spk((14, 60), (22, 44), (-12, 46), 6), spk((20, 40), (38, 22), (2, 10), 6), spk((40, 18), (58, 10), (36, -8), 5),
             spk((14, 78), (26, 88), (0, 96), 4), L(blob([(16, 50), (18, 76), (38, 88), (28, 62)], 6), 'shade', 'b', False),
             spk((56, 22), (86, 34), (94, 70), 6, z='f', light_left=False)],
    'back': [L(blob([(12, 66), (10, 40), (22, 16), (50, 8), (78, 14), (92, 36), (90, 66), (76, 88), (50, 94), (24, 88)])),
             spk((10, 56), (22, 48), (-12, 52), 5), spk((80, 60), (90, 52), (108, 74), 5, light_left=False),
             spk((54, 12), (72, 14), (78, -8), 5, light_left=False), spk((38, 12), (54, 10), (40, -8), 5),
             spk((20, 80), (40, 90), (24, 104), 4), spk((40, 92), (60, 92), (54, 106), 4), spk((60, 90), (80, 80), (82, 102), 4, light_left=False),
             L(blob([(58, 16), (90, 38), (88, 68), (70, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Jim Lawrenson: bajito y regordete, pelo verde amarillento
# despeinado, ojos pequeños medio cerrados, nariz naranja y un lunar en la frente
CHARS['jim-lawrenson'] = {
    'body': 'bajito', 'pal': pal('#94a038', '#f6c48c', nose='#e88a50', mole='#3a2a2a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'nose': (50, 82, 3.6), 'nose_side': (89, 80, 3.4), 'hairline': (62, 52)},
    'front': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66)])),
              spk((8, 50), (16, 64), (-8, 68), 4), spk((84, 64), (92, 50), (108, 68), 4, light_left=False),
              L(blob([(60, 14), (88, 34), (88, 62), (74, 58)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((16, 44), (34, 40), (20, 66), 4, z='f'), spk((30, 40), (50, 38), (40, 60), 4, z='f'),
              spk((48, 38), (66, 40), (62, 58), 4, z='f', light_left=False), spk((62, 42), (84, 48), (84, 68), 4, z='f', light_left=False),
              L(ell(50, 66, 1.6, 1.6), 'mole', 'f', False)],
    'side': [L(blob([(44, 92), (22, 88), (10, 64), (12, 36), (28, 14), (56, 8), (80, 16), (90, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             spk((12, 62), (22, 46), (-10, 52), 5), spk((14, 80), (28, 88), (0, 96), 4),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 14, 3),
             spk((54, 26), (84, 38), (92, 66), 6, z='f', light_left=False)],
    'back': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66), (76, 88), (50, 94), (24, 88)])),
             spk((8, 50), (16, 64), (-8, 68), 4), spk((84, 64), (92, 50), (108, 68), 4, light_left=False),
             spk((18, 78), (36, 88), (14, 100), 4), spk((36, 90), (54, 92), (40, 106), 4), spk((54, 92), (72, 88), (70, 106), 4, light_left=False),
             spk((70, 86), (86, 76), (94, 98), 4, light_left=False),
             L(blob([(58, 16), (88, 38), (86, 68), (70, 86)], 6), 'shade', 'b', False), sheen(24, 50, 20, 3)],
}

# ------------------------------------------------------------------ Barry Potts: corpulento, pelo rizado azul marino alto,
# gafas de sol oscuras y bigote; piel morena
CHARS['barry-potts'] = {
    'body': 'corpulento', 'pal': pal('#2c3654', '#a87052', glass=(26, 26, 34, 255), glass_l=(90, 90, 110, 255)),
    'face': {'eyes': 'none', 'mouth': 'frown', 'mouth_y': 94, 'hairline': (62, 56)},
    'front': [L(bumpy(50, 30, 42, 34, 12, 0.09)), L(bumpy(66, 38, 20, 20, 8), 'shade', 'b', False), L(ell(34, 14, 9, 3), 'light', 'b', False)]
             + clumps([(18, 52), (82, 52)], 12) + [
              L(blob([(18, 70), (46, 68), (50, 72), (54, 68), (82, 70), (80, 80), (58, 82), (50, 76), (42, 82), (20, 80)], 4), 'glass', 'f'),
              L(blob([(24, 72), (36, 71), (30, 75)], 3), 'glass_l', 'f', False), L(blob([(64, 71), (76, 72), (70, 75)], 3), 'glass_l', 'f', False),
              mustache(88, 12)],
    'side': [L(bumpy(44, 34, 42, 34, 12, 0.09)), L(bumpy(26, 46, 20, 22, 8), 'shade', 'b', False), L(ell(44, 10, 8, 3), 'light', 'b', False),
             L(blob([(66, 70), (88, 70), (87, 79), (68, 78)], 4), 'glass', 'f'), L([(66, 72), (50, 70)], 'glass', 'f', False, False, 1.4),
             L(blob([(82, 86), (91, 84), (92, 90), (84, 91)], 3), 'mid', 'f')],
    'back': [L(bumpy(50, 40, 46, 42, 14, 0.08)), L(bumpy(68, 50, 22, 26, 8), 'shade', 'b', False), L(ell(34, 16, 9, 3), 'light', 'b', False),
             L(blob([(22, 64), (78, 64), (74, 86), (50, 92), (26, 86)]))],
}

# ------------------------------------------------------------------ Steve Ingham: pelo castaño con dos mechones curvos a los
# lados de la cara (como cuernos), ojos cerrados de felicidad y rubor en las mejillas
CHARS['steve-ingham'] = {
    'body': 'normal', 'pal': pal('#8a6a3e', '#f8d8b4', horn='#9aa0a8', blush='#f0a090'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'hairline': (62, 54)},
    'front': [L(blob([(10, 70), (6, 42), (18, 16), (50, 8), (82, 16), (94, 42), (90, 70)])),
              spk((6, 52), (16, 66), (-8, 72), 4), spk((84, 66), (94, 52), (108, 72), 4, light_left=False),
              L(blob([(60, 14), (90, 36), (90, 64), (76, 60)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              spk((16, 46), (34, 42), (20, 68), 4, z='f'), spk((32, 42), (50, 40), (42, 62), 4, z='f'),
              spk((50, 40), (68, 42), (60, 62), 4, z='f', light_left=False), spk((66, 44), (84, 48), (80, 68), 4, z='f', light_left=False),
              L(blob([(30, 46), (24, 60), (26, 76), (32, 80), (30, 62), (36, 50)], 6), 'horn', 'f', ln=True),
              L(blob([(70, 46), (76, 60), (74, 76), (68, 80), (70, 62), (64, 50)], 6), 'horn', 'f', ln=True),
              L(ell(30, 84, 5, 2.4), 'blush', 'f', False), L(ell(70, 84, 5, 2.4), 'blush', 'f', False)],
    'side': [L(blob([(44, 92), (22, 88), (10, 64), (12, 36), (28, 14), (56, 8), (80, 16), (90, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             spk((12, 62), (22, 46), (-10, 52), 5), spk((14, 80), (28, 88), (0, 96), 4),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 14, 3),
             spk((54, 26), (84, 38), (90, 66), 6, z='f', light_left=False),
             L(blob([(70, 46), (76, 60), (74, 76), (68, 80), (70, 62), (64, 50)], 6), 'horn', 'f', ln=True),
             L(ell(78, 86, 4, 2.2), 'blush', 'f', False)],
    'back': [L(blob([(10, 70), (6, 42), (18, 16), (50, 8), (82, 16), (94, 42), (90, 70), (76, 90), (50, 96), (24, 90)])),
             spk((6, 52), (16, 66), (-8, 72), 4), spk((84, 66), (94, 52), (108, 72), 4, light_left=False),
             spk((18, 80), (36, 90), (14, 102), 4), spk((36, 92), (54, 94), (40, 108), 4), spk((54, 94), (72, 90), (70, 108), 4, light_left=False),
             spk((70, 88), (86, 78), (94, 100), 4, light_left=False),
             L(blob([(58, 16), (90, 38), (88, 68), (70, 88)], 6), 'shade', 'b', False), sheen(24, 50, 20, 3)],
}
