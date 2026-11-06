"""Sengoku Igajima / Instituto Shuriken (IE1): ninjas y samuráis; capuchas, cintas con placa, bufandas, moños de samurái y
shurikens de adorno, con sus modelos 3D como referencia."""
import math

from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]


def star(cx, cy, r, ri, rot=0.0, n=4):
    """Shuriken: estrella de n puntas."""
    pts = []
    for i in range(n * 2):
        a = rot + math.pi * i / n
        rr = r if i % 2 == 0 else ri
        pts.append((cx + rr * math.sin(a), cy - rr * math.cos(a)))
    return pts


def shuriken(cx, cy, r, rot=0.0, c='shur', cd='shur_d', hole=True, ri=0.32, disk=0):
    out = [L(star(cx, cy, r, r * ri, rot), c, 'f', ln=True),
           L([(cx, cy)] + star(cx, cy, r, r * ri, rot)[1:4], cd, 'f', False)]
    if disk:  # disco central (el shuriken de la frente de Jez)
        out.append(L(ell(cx, cy, r * disk, r * disk), cd, 'f', ln=True))
    elif hole:
        out.append(L(ell(cx, cy, r * 0.22, r * 0.22), OUTC, 'f', False))
    return out


def wavy(a, b, tip, bend=6, z='b', light_left=True, sil=True):
    """Mechón ondulado: como un pincho pero con el eje curvado (bend > 0 lo dobla hacia la izquierda de su dirección)."""
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    dx, dy = tip[0] - m[0], tip[1] - m[1]
    n = math.hypot(dx, dy) or 1
    c = ((m[0] + tip[0]) / 2 + dy / n * bend, (m[1] + tip[1]) / 2 - dx / n * bend)

    def shape(p, q):
        mm = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        ca = (c[0] + (p[0] - mm[0]) * 0.7, c[1] + (p[1] - mm[1]) * 0.7)
        cb = (c[0] + (q[0] - mm[0]) * 0.7, c[1] + (q[1] - mm[1]) * 0.7)
        return quad(p, ca, tip) + quad(tip, cb, q)[1:]
    t = 0.5
    sh = shape((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t), b) if light_left else shape(a, (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return [L(shape(a, b), 'mid', z, sil), L(sh, 'shade', z, False)]


def band(y0, y1, c='band', z='f', bow=8, x0=10, x1=90):
    """Cinta alrededor de la cabeza (de frente o de espaldas): arco de y0 a y1."""
    return L(quad((x0, y0), (50, y0 - bow), (x1, y0)) + quad((x1, y1), (50, y1 - bow), (x0, y1)), c, z, ln=True)


# ------------------------------------------------------------------ Morgan Sanders (portero): capucha ninja morada que le cubre
# toda la cabeza; dentro, una franja oscura con dos ojos blancos, una placa metálica en la frente y una máscara gris de tela
# que acaba en pico sobre el pecho
MORGAN_HOOD = blob([(-6, 118), (0, 70), (8, 32), (28, 6), (50, -6), (72, 6), (92, 32), (100, 70), (106, 118), (88, 108), (84, 66), (78, 50),
                    (50, 42), (22, 50), (16, 66), (12, 108)], 8)
CHARS['morgan-sanders'] = {
    'body': 'normal', 'pal': pal('#3a3040', '#f2c49a', hood='#5a4a7a', hood_d='#3e3258', mask='#9090a8', mask_d='#70708a',
                                 dark='#10261e', plate='#c8c0b0', plate_d='#988e80', gem='#c8502a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(blob([(16, 42), (84, 42), (86, 80), (50, 110), (14, 80)]), 'dark', 'f', False),
              L(ell(37, 69, 3.2, 2.6), WHITE, 'f', False), L(ell(63, 69, 3.2, 2.6), WHITE, 'f', False),
              L([(16, 76), (84, 76), (84, 86), (70, 102), (50, 118), (30, 102), (16, 86)], 'mask', 'f', ln=True),
              L([(50, 76), (84, 76), (84, 86), (70, 102), (50, 118)], 'mask_d', 'f', False),
              L([(24, 46), (76, 46), (77, 60), (23, 60)], 'plate', 'f', ln=True), L([(24, 56), (76, 56), (77, 60), (23, 60)], 'plate_d', 'f', False),
              L([(50, 47), (57, 53), (50, 59), (43, 53)], 'gem', 'f', ln=True),
              L(MORGAN_HOOD, 'hood', 'f', ln=True), L(blob([(60, 2), (96, 50), (102, 112), (90, 106), (86, 60)], 6), 'hood_d', 'f', False),
              strand([(50, -4), (50, 40)], 'hood_d', 'f', 1.0)],
    'side': [L(blob([(64, 44), (94, 44), (96, 80), (84, 104), (64, 100)]), 'dark', 'f', False),
             L(ell(88, 68, 2.2, 2.6), WHITE, 'f', False),
             L([(66, 76), (96, 76), (96, 90), (86, 102), (72, 112), (62, 98)], 'mask', 'f', ln=True),
             L([(80, 44), (93, 46), (93, 60), (80, 60)], 'plate', 'f', ln=True),
             L([(40, 118), (4, 106), (0, 62), (8, 26), (30, 6), (56, 0), (80, 10), (94, 34), (94, 44), (80, 42), (72, 60), (74, 100), (66, 114)],
               'hood', 'f', ln=True),
             L(blob([(6, 62), (12, 28), (28, 14), (32, 60), (26, 104)], 6), 'hood_d', 'f', False),
             strand([(30, 8), (8, 50)], 'hood_d', 'f', 1.0)],
    'back': [L(blob([(-6, 120), (0, 70), (8, 32), (28, 6), (50, -6), (72, 6), (92, 32), (100, 70), (106, 120), (50, 126)]), 'hood', 'f', ln=True),
             L(blob([(58, 0), (96, 50), (102, 118), (66, 124)], 6), 'hood_d', 'f', False),
             strand([(50, -4), (50, 60)], 'hood_d', 'f', 1.2)],
}

# ------------------------------------------------------------------ Newton Flust: casco rubio oscuro con un flequillo recto que
# le tapa los ojos y una coleta alta (atada con una cinta azul) que cae por detrás
NEWTON_FRINGE = [(10, 44), (22, 28), (50, 20), (78, 28), (90, 44), (90, 70), (88, 82), (80, 78), (74, 84), (66, 79), (58, 85), (50, 80),
                 (42, 85), (34, 79), (26, 84), (18, 78), (10, 72)]
CHARS['newton-flust'] = {
    'body': 'normal', 'pal': pal('#b09a54', '#f6c08e', tail='#7a5634', tail_d='#5a3e24', tie='#5a9aa0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob([(46, 14), (48, -6), (60, -16), (76, -12), (84, 6), (86, 36), (82, 62), (76, 36), (68, 16)]), 'tail', 'b'),
              L(blob([(72, -6), (84, 8), (84, 40), (78, 20)], 6), 'tail_d', 'b', False),
              L(blob([(44, 12), (45, 2), (57, 0), (58, 12)], 3), 'tie', 'b'),
              L(blob([(10, 82), (6, 46), (16, 18), (50, 8), (84, 18), (94, 46), (90, 82)])),
              L(NEWTON_FRINGE, 'mid', 'f'), strand(NEWTON_FRINGE[5:] + NEWTON_FRINGE[:1], OUTC, 'f', 1.1),
              L([(64, 28), (78, 30), (90, 44), (90, 70), (88, 82), (80, 78), (74, 84), (70, 60)], 'shade', 'f', False),
              sheen(22, 52, 30, 3, z='f'),
              strand([(36, 36), (34, 78)], 'shade', 'f', 1.0), strand([(50, 32), (50, 78)], 'shade', 'f', 1.0), strand([(64, 36), (66, 78)], 'shade', 'f', 1.0)],
    'side': [L(blob([(36, 16), (30, -6), (14, -16), (-2, -10), (-10, 14), (-10, 50), (-6, 82), (0, 58), (2, 26), (10, 6), (22, 6), (28, 20)]), 'tail', 'b', ln=True),
             L(blob([(-6, 0), (-8, 40), (-4, 70), (0, 30)], 6), 'tail_d', 'b', False),
             L(ell(32, 10, 4.6, 5.6), 'tie', 'b', ln=True),
             L([(46, 92), (22, 88), (10, 62), (12, 34), (28, 14), (56, 8), (80, 16), (92, 36), (95, 62), (92, 82), (86, 78), (80, 84), (74, 78),
                (64, 80), (58, 66), (52, 68), (50, 84)]),
             L(blob([(14, 46), (16, 80), (40, 88), (28, 60)], 6), 'shade', 'b', False), sheen(30, 62, 18, 3),
             strand([(72, 20), (88, 78)], 'shade', 'b', 1.0), strand([(60, 16), (72, 78)], 'shade', 'b', 1.0)],
    'back': [L(blob([(10, 82), (6, 46), (16, 18), (50, 8), (84, 18), (94, 46), (90, 82), (72, 90), (50, 92), (28, 90)])),
             L(blob([(58, 16), (90, 40), (88, 78), (70, 88)], 6), 'shade', 'b', False),
             L(blob([(44, 10), (50, -6), (62, -8), (68, 8), (64, 46), (56, 84), (46, 98), (40, 70), (38, 40)]), 'tail', 'f', ln=True),
             L(blob([(56, 4), (64, 10), (60, 50), (50, 92), (54, 50)], 6), 'tail_d', 'f', False),
             L(ell(53, 4, 7, 4.4), 'tie', 'f', ln=True)],
}

# ------------------------------------------------------------------ Jim Hillfort: pelo castaño oscuro de pinchos en todas
# direcciones (con reflejos verdosos), cinta ninja ocre con una placa metálica, ojos rojos y una bufanda ocre que le tapa la
# boca y ondea a un lado
JIM_SPIKES_F = [spk((8, 60), (12, 42), (-14, 62), 7), spk((10, 44), (20, 24), (-16, 26), 8), spk((20, 26), (40, 12), (12, -16), 8),
                spk((36, 12), (54, 8), (44, -24), 8), spk((52, 8), (70, 14), (74, -12), 8, light_left=False),
                spk((68, 16), (86, 30), (108, 10), 8, light_left=False), spk((86, 34), (92, 56), (116, 50), 7, light_left=False)]
CHARS['jim-hillfort'] = {
    'body': 'normal', 'pal': pal('#3e3024', '#f6c08e', iris='#c02424', light='#6e6a3a', band='#a89024', band_d='#7a6818',
                                 plate='#b0b0b8', plate_d='#7a7a88', scarf='#ab9a24', scarf_d='#7e7018'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'eye_y': 71, 'hairline': (52, 46)},
    'front': JIM_SPIKES_F + [L(blob([(10, 62), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 62)])),
                             L(blob([(60, 12), (90, 36), (88, 60), (74, 56)], 6), 'shade', 'b', False),
                             spk((14, 56), (24, 56), (16, 74), 2.5, z='f'), spk((76, 56), (86, 56), (84, 74), 2.5, z='f', light_left=False),
                             band(48, 60), L([(28, 47), (72, 47), (72, 58), (28, 58)], 'plate', 'f', ln=True),
                             L([(28, 55), (72, 55), (72, 58), (28, 58)], 'plate_d', 'f', False)]
             + [L(star(x, 52, 3.4, 1.1), OUTC, 'f', False) for x in (38, 50, 62)]
             + [L(blob([(30, 98), (70, 98), (60, 122), (40, 122)]), 'scarf_d', 'f', ln=True),
                L(blob([(80, 86), (98, 82), (108, 88), (98, 94), (84, 98)]), 'scarf', 'f', ln=True),
                L(blob([(12, 78), (50, 80), (88, 78), (90, 92), (76, 104), (50, 110), (24, 104), (10, 92)]), 'scarf', 'f', ln=True),
                L(blob([(56, 82), (88, 80), (88, 94), (74, 104), (58, 106)], 6), 'scarf_d', 'f', False),
                strand([(30, 90), (46, 96)], 'scarf_d', 'f', 1.0)],
    'side': [spk((16, 40), (24, 24), (-18, 20), 7), spk((24, 26), (40, 14), (8, -14), 7), spk((40, 14), (58, 8), (46, -16), 6),
             spk((56, 10), (74, 14), (82, -10), 6, light_left=False), spk((14, 56), (16, 40), (-16, 50), 6), spk((16, 70), (20, 58), (-8, 76), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((70, 18), (86, 32), (100, 14), 5, light_left=False),
             L(quad((12, 46), (50, 40), (92, 44)) + quad((92, 56), (50, 52), (12, 58)), 'band', 'f', ln=True),
             L([(80, 43), (93, 44), (93, 56), (80, 56)], 'plate', 'f', ln=True),
             L(blob([(14, 48), (2, 48), (-6, 58), (6, 58)], 4), 'band', 'f', ln=True),
             L(blob([(40, 92), (24, 98), (12, 108), (26, 110), (44, 104)]), 'scarf', 'b', ln=True),
             L(blob([(60, 78), (94, 80), (96, 94), (84, 104), (64, 108), (54, 94)]), 'scarf', 'f', ln=True),
             L(blob([(58, 96), (84, 102), (64, 108)], 4), 'scarf_d', 'f', False)],
    'back': JIM_SPIKES_F + [
             L(blob([(10, 68), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 68), (72, 84), (28, 84)])),
             spk((12, 70), (30, 80), (4, 92), 4), spk((30, 82), (50, 84), (38, 98), 4), spk((50, 84), (70, 82), (62, 98), 4, light_left=False),
             spk((70, 80), (88, 70), (96, 92), 4, light_left=False),
             L(blob([(58, 12), (90, 36), (88, 66), (70, 80)], 6), 'shade', 'b', False),
             band(54, 66), L(blob([(26, 60), (12, 62), (6, 74), (16, 72), (28, 66)], 4), 'band', 'f', ln=True),
             L(blob([(22, 92), (78, 92), (80, 104), (20, 104)]), 'scarf', 'f', ln=True),
             L(blob([(26, 96), (10, 100), (2, 110), (14, 110), (28, 104)]), 'scarf', 'f', ln=True)],
}

# ------------------------------------------------------------------ Galen Thunderbird: corpulento, peinado de samurái: coronilla
# afeitada (gris) en pico sobre la frente, pelo castaño a los lados y un moño en brocha en lo alto; ojos redondos, nariz
# grande y bigote fino
GALEN_KNOT_F = [L(blob([(38, 6), (34, -12), (42, -22), (50, -14), (58, -24), (66, -12), (62, 6)]), 'mid', 'b', ln=True),
                L(blob([(54, -14), (64, -12), (60, 4), (54, 4)], 4), 'shade', 'b', False),
                strand([(44, 2), (42, -14)], 'deep', 'b', 1.0), strand([(52, 2), (52, -12)], 'deep', 'b', 1.0),
                L(blob([(42, 14), (42, 2), (58, 2), (58, 14)], 3), 'shave', 'b', ln=True)]
CHARS['galen-thunderbird'] = {
    'body': 'corpulento', 'pal': pal('#7a4a1e', '#fcd29c', shave='#a4aaa8', shave_d='#868c8c', nose='#e8a070'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93, 'nose': (50, 82, 5.4), 'nose_side': (91, 80, 4.8),
             'big_ears': 1, 'hairline': (60, 46)},
    'front': GALEN_KNOT_F + [L(blob([(12, 70), (10, 42), (22, 20), (50, 12), (78, 20), (90, 42), (88, 70)])),
                             L(blob([(62, 18), (88, 40), (86, 68), (74, 62)], 6), 'shade', 'b', False),
                             L(blob([(28, 20), (50, 12), (72, 20), (62, 38), (50, 50), (38, 38)]), 'shave', 'b', False),
                             L(blob([(54, 16), (72, 20), (62, 38), (52, 46)], 4), 'shave_d', 'b', False),
                             L(blob([(36, 88), (44, 85), (50, 86.5), (56, 85), (64, 88), (56, 89.5), (44, 89.5)], 4), 'deep', 'f')],
    'side': [L(blob([(36, 8), (30, -10), (36, -20), (44, -14), (50, -22), (58, -12), (50, 10)]), 'mid', 'b', ln=True),
             strand([(42, 6), (38, -12)], 'deep', 'b', 1.0), L(blob([(36, 14), (36, 4), (50, 4), (50, 14)], 3), 'shave', 'b', ln=True),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(36, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 42), (46, 30)]), 'shave', 'b', False),
             L(blob([(84, 85), (93, 84), (93, 88), (85, 89)], 3), 'deep', 'f')],
    'back': GALEN_KNOT_F + [L(blob([(14, 72), (12, 42), (24, 20), (50, 12), (76, 20), (88, 42), (86, 72), (70, 90), (30, 90)])),
                            L(blob([(36, 14), (50, 10), (64, 14), (60, 26), (40, 26)]), 'shave', 'b', False)] + back_hair(),
}

# ------------------------------------------------------------------ Finn Stoned: corpulento, piel morena, pelo negro azulado
# pegado al cráneo con un moño en gancho que se curva hacia arriba; cicatriz en X en la frente, ceño y labios gruesos
CHARS['finn-stoned'] = {
    'body': 'corpulento', 'pal': pal('#26343e', '#c8903e', scar='#6a3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 92, 'mouth_w': 8, 'nose': (50, 83, 3.4), 'nose_side': (91, 81, 3.2),
             'hairline': (54, 40)},
    'front': [L(blob([(47, 14), (47, -4), (40, -12), (30, -14), (38, -19), (50, -12), (54, 2), (54, 14)]), 'mid', 'b', ln=True),
              L(blob([(16, 64), (14, 36), (26, 14), (50, 8), (74, 14), (86, 36), (84, 64)])),
              L(blob([(60, 12), (86, 34), (84, 62), (70, 56)], 6), 'shade', 'b', False), sheen(28, 52, 18, 3),
              strand([(40, 12), (34, 44)], 'deep', 'b', 1.0), strand([(60, 12), (66, 44)], 'deep', 'b', 1.0),
              L([(43, 48), (57, 60)], 'scar', 'f', False, False, 1.6), L([(57, 48), (43, 60)], 'scar', 'f', False, False, 1.6)],
    'side': [L(blob([(37, 14), (40, -4), (50, -16), (62, -22), (55, -11), (46, 2), (46, 14)]), 'mid', 'b', ln=True),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             strand([(76, 20), (50, 14), (22, 40)], 'deep', 'b', 1.0), strand([(84, 34), (50, 26), (26, 60)], 'deep', 'b', 1.0),
             L([(80, 50), (88, 56)], 'scar', 'f', False, False, 1.4)],
    'back': [L(blob([(46, 14), (46, -4), (52, -12), (62, -14), (56, -19), (46, -12), (40, 2), (40, 14)]), 'mid', 'b', ln=True),
             L(blob([(16, 70), (14, 36), (26, 14), (50, 8), (74, 14), (86, 36), (84, 70), (66, 84), (34, 84)]))] + back_hair() + [
             strand([(40, 12), (38, 76)], 'deep', 'b', 1.0), strand([(60, 12), (62, 76)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Phil Wingate: melena lisa negra verdosa hasta la barbilla,
# mechones largos a los lados de la cara (le tapan las orejas) y una cinta blanca rosada en la frente; ojos verdes afilados
CHARS['phil-wingate'] = {
    'body': 'normal', 'pal': pal('#2e3424', '#f6c08e', iris='#3a8a7a', band='#ecdcd4', band_d='#c4a09c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'hairline': (58, 50), 'ears': False},
    'front': [L(blob([(8, 104), (4, 60), (12, 22), (50, 8), (88, 22), (96, 60), (92, 104), (80, 102), (80, 70), (20, 70), (20, 102)])),
              L(blob([(62, 14), (94, 46), (92, 100), (82, 98)], 6), 'shade', 'b', False), sheen(24, 50, 22, 3),
              strand([(36, 12), (30, 46)], 'deep', 'b', 1.0), strand([(64, 12), (70, 46)], 'deep', 'b', 1.0),
              band(54, 63, bow=8, x0=12, x1=88), L(quad((12, 60), (50, 52), (88, 60)) + quad((88, 63), (50, 55), (12, 63)), 'band_d', 'f', False),
              spk((40, 44), (50, 42), (46, 64), 2, z='f'), spk((50, 42), (60, 44), (54, 62), 2, z='f', light_left=False),
              L(blob([(10, 44), (26, 46), (30, 74), (24, 104), (12, 106), (8, 74)]), 'mid', 'f'),
              L(blob([(90, 44), (74, 46), (70, 74), (76, 104), (88, 106), (92, 74)]), 'mid', 'f'),
              L(blob([(80, 50), (88, 60), (88, 100), (80, 98)], 5), 'shade', 'f', False),
              strand([(27, 50), (30, 74), (25, 102)], OUTC, 'f', 1.1), strand([(73, 50), (70, 74), (75, 102)], OUTC, 'f', 1.1),
              strand([(18, 52), (18, 100)], 'deep', 'f', 0.9), strand([(82, 52), (82, 100)], 'deep', 'f', 0.9)],
    'side': [L(blob([(46, 100), (10, 102), (2, 62), (8, 28), (28, 10), (56, 6), (80, 14), (92, 34), (92, 56), (76, 54), (62, 54), (58, 70), (58, 98)])),
             L(blob([(6, 50), (8, 96), (40, 100), (24, 70)], 6), 'shade', 'b', False), sheen(30, 62, 16, 3),
             strand([(20, 30), (12, 96)], 'deep', 'b', 1.0), strand([(34, 30), (30, 98)], 'deep', 'b', 1.0), strand([(50, 40), (48, 98)], 'deep', 'b', 1.0),
             L(quad((6, 46), (50, 36), (92, 42)) + quad((92, 52), (50, 46), (6, 56)), 'band', 'f', ln=True),
             spk((76, 52), (90, 52), (88, 70), 2, z='f', light_left=False)],
    'back': [L(blob([(8, 104), (4, 60), (12, 22), (50, 8), (88, 22), (96, 60), (92, 104), (50, 108)])),
             L(blob([(58, 14), (94, 46), (92, 102), (66, 106)], 6), 'shade', 'b', False), sheen(24, 50, 22, 3),
             band(46, 56, bow=10, x0=4, x1=96), L(quad((4, 53), (50, 43), (96, 53)) + quad((96, 56), (50, 46), (4, 56)), 'band_d', 'f', False)]
            + [strand([(x, 58), (x + (x - 50) * 0.1, 104)], 'deep', 'f', 1.0) for x in (26, 40, 50, 60, 74)],
}

# ------------------------------------------------------------------ Jez Shell: media melena verde oliva con las puntas hacia
# fuera, dos pelillos de antena y un shuriken gris enorme en la frente (con un disco en el centro)
CHARS['jez-shell'] = {
    'body': 'normal', 'pal': pal('#5e5a26', '#fbe0b8', iris='#6a3a1a', shur='#8e8e94', shur_d='#66666e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'eye_y': 77, 'hairline': (60, 50)},
    'front': [spk((44, 10), (50, 10), (38, -6), 2), spk((50, 10), (56, 10), (60, -4), 2, light_left=False),
              L(blob([(8, 86), (4, 56), (14, 22), (50, 8), (86, 22), (96, 56), (92, 86), (80, 80), (80, 62), (20, 62), (20, 80)])),
              spk((6, 70), (14, 82), (-6, 94), 3), spk((86, 82), (94, 70), (106, 94), 3, light_left=False),
              L(blob([(62, 14), (94, 48), (92, 84), (82, 80)], 6), 'shade', 'b', False), sheen(22, 48, 22, 3),
              spk((12, 42), (32, 36), (16, 72), 5, z='f'), spk((68, 36), (88, 42), (86, 72), 5, z='f', light_left=False),
              spk((28, 40), (44, 36), (34, 64), 4, z='f'), spk((56, 36), (72, 40), (66, 64), 4, z='f', light_left=False)]
             + shuriken(50, 44, 26, 0.12, ri=0.42, disk=0.26),
    'side': [spk((40, 10), (48, 8), (40, -6), 2),
             L(blob([(48, 94), (14, 92), (2, 62), (6, 30), (26, 10), (56, 6), (80, 14), (92, 34), (90, 56), (74, 54), (60, 56), (54, 72), (52, 90)])),
             spk((4, 76), (16, 88), (-4, 96), 3), spk((22, 90), (40, 94), (26, 104), 3),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 16, 3),
             spk((56, 50), (68, 52), (62, 76), 3, z='f'),
             L([(82, 20), (94, 44), (90, 70), (84, 46)], 'shur', 'f', ln=True)],
    'back': [spk((44, 10), (50, 10), (38, -6), 2), spk((50, 10), (56, 10), (60, -4), 2, light_left=False),
             L(blob([(8, 84), (4, 56), (14, 22), (50, 8), (86, 22), (96, 56), (92, 84), (50, 90)])),
             spk((6, 70), (14, 82), (-6, 94), 3), spk((86, 82), (94, 70), (106, 94), 3, light_left=False),
             spk((14, 82), (32, 88), (14, 100), 4), spk((32, 88), (50, 90), (40, 102), 4), spk((50, 90), (68, 88), (60, 102), 4, light_left=False),
             spk((68, 88), (86, 82), (86, 100), 4, light_left=False),
             L(blob([(58, 14), (94, 48), (92, 82), (66, 88)], 6), 'shade', 'b', False), sheen(24, 50, 22, 3),
             strand([(40, 14), (36, 84)], 'shade', 'b', 1.0), strand([(60, 14), (64, 84)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Jupiter Jumper: pelo rosa rojizo alborotado y abultado, con
# las puntas hacia fuera junto a las orejas y una horquilla en forma de shuriken a un lado; ojos redondos y ceño fruncido
CHARS['jupiter-jumper'] = {
    'body': 'normal', 'pal': pal('#c25a62', '#f6c08e', shur='#a0a0a8', shur_d='#70707a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [spk((40, 8), (48, 6), (36, -6), 2.5), spk((50, 6), (58, 8), (58, -6), 2.5, light_left=False),
              L(bumpy(50, 38, 46, 32, 12, 0.06)),
              L(bumpy(12, 66, 11, 12, 6, 0.1)), L(bumpy(88, 66, 11, 12, 6, 0.1)),
              spk((6, 72), (14, 78), (2, 88), 2.5), spk((86, 78), (94, 72), (98, 88), 2.5, light_left=False),
              L(bumpy(68, 40, 22, 22, 8, 0.06), 'shade', 'b', False), L(ell(30, 18, 12, 4), 'light', 'b', False),
              spk((12, 46), (32, 40), (18, 68), 5, z='f'), spk((30, 40), (50, 38), (40, 62), 5, z='f'),
              spk((50, 38), (70, 40), (60, 62), 5, z='f', light_left=False), spk((68, 40), (88, 46), (84, 68), 5, z='f', light_left=False)]
             + shuriken(84, 48, 12, 0.7, hole=False),
    'side': [spk((44, 4), (52, 4), (48, -8), 2.5),
             L(bumpy(44, 38, 44, 32, 12, 0.06)),
             L(bumpy(14, 66, 12, 14, 6, 0.1)), spk((10, 76), (22, 84), (8, 94), 3),
             L(bumpy(26, 48, 20, 22, 8, 0.06), 'shade', 'b', False),
             L(blob([(46, 92), (24, 88), (16, 64), (40, 60), (54, 64), (50, 80)]), 'mid', 'b', False),
             spk((56, 30), (86, 40), (92, 68), 6, z='f', light_left=False)]
            + shuriken(36, 52, 11, 0.7, hole=False),
    'back': [spk((40, 8), (48, 6), (36, -6), 2.5), spk((50, 6), (58, 8), (58, -6), 2.5, light_left=False),
             L(bumpy(50, 42, 46, 36, 12, 0.06)),
             L(bumpy(12, 68, 11, 12, 6, 0.1)), L(bumpy(88, 68, 11, 12, 6, 0.1)),
             spk((14, 76), (32, 86), (14, 96), 4), spk((68, 86), (86, 76), (86, 96), 4, light_left=False),
             spk((32, 86), (50, 88), (40, 100), 4), spk((50, 88), (68, 86), (60, 100), 4, light_left=False),
             L(bumpy(66, 50, 22, 24, 8, 0.06), 'shade', 'b', False), L(ell(30, 20, 12, 4), 'light', 'b', False)]
            + shuriken(16, 50, 12, 0.7, hole=False),
}

# ------------------------------------------------------------------ Hank Sullivan: pelo verde hierba con mechones grandes
# barridos de derecha a izquierda sobre la frente y las puntas vueltas hacia fuera junto a la mandíbula
CHARS['hank-sullivan'] = {
    'body': 'normal', 'pal': pal('#6a9a34', '#fbd8b0', iris='#4a4a7a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'line', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [L(blob([(10, 82), (6, 46), (18, 16), (50, 6), (84, 16), (96, 46), (92, 82), (82, 78), (82, 60), (18, 60), (18, 78)])),
              spk((4, 72), (16, 82), (-2, 92), 3), spk((84, 82), (96, 72), (102, 92), 3, light_left=False),
              L(blob([(62, 12), (94, 44), (92, 80), (84, 78)], 6), 'shade', 'b', False), sheen(22, 46, 20, 3),
              spk((30, 32), (50, 26), (12, 54), 5, z='f'),
              spk((54, 22), (80, 30), (16, 64), 8, z='f', light_left=False),
              spk((72, 34), (90, 46), (44, 62), 6, z='f', light_left=False),
              spk((82, 44), (92, 56), (78, 72), 3, z='f', light_left=False)],
    'side': [L(blob([(48, 94), (14, 92), (4, 62), (8, 30), (28, 8), (58, 4), (84, 14), (96, 34), (94, 58), (76, 56), (62, 56), (56, 72), (52, 90)])),
             spk((6, 80), (18, 90), (0, 98), 3),
             L(blob([(8, 50), (10, 88), (40, 92), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((44, 24), (76, 22), (100, 54), 8, z='f', light_left=False), spk((56, 40), (82, 42), (90, 64), 4, z='f', light_left=False),
             spk((48, 52), (60, 52), (54, 78), 3, z='f')],
    'back': [L(blob([(10, 82), (6, 46), (18, 16), (50, 6), (84, 16), (96, 46), (92, 82), (50, 90)])),
             spk((4, 72), (16, 82), (-2, 92), 3), spk((84, 82), (96, 72), (102, 92), 3, light_left=False),
             spk((20, 84), (40, 90), (24, 100), 3), spk((60, 90), (80, 84), (76, 100), 3, light_left=False),
             L(blob([(58, 12), (94, 44), (92, 80), (66, 88)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
             strand([(70, 14), (40, 40), (30, 80)], 'shade', 'b', 1.1)],
}

# ------------------------------------------------------------------ Sam Samurai: piel morena, pelo castaño corto peinado hacia
# atrás con un moño pequeño de samurái en lo alto (atado con una cinta morada) y un parche metálico en forma de shuriken sobre
# el ojo derecho, sujeto con una correa morada en diagonal
SAM_KNOT = [L(blob([(42, 4), (38, -10), (46, -20), (58, -18), (68, -8), (56, -4)]), 'mid', 'b', ln=True),
            L(blob([(52, -16), (66, -8), (56, -6)], 4), 'shade', 'b', False),
            L(blob([(45, 10), (45, 0), (55, 0), (55, 10)], 3), 'strap', 'b', ln=True)]
CHARS['sam-samurai'] = {
    'body': 'normal', 'pal': pal('#5a4030', '#d89a5a', strap='#6e5e90', strap_d='#4a3e66', shur='#6e6e78', shur_d='#4a4a54'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (56, 46)},
    'front': SAM_KNOT + [L(blob([(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)])),
                         L(blob([(60, 12), (86, 34), (84, 62), (70, 56)], 6), 'shade', 'b', False), sheen(26, 50, 18, 3),
                         strand([(50, 8), (40, 44)], 'deep', 'b', 1.0), strand([(56, 10), (62, 44)], 'deep', 'b', 1.0),
                         spk((16, 50), (24, 50), (18, 66), 2, z='f'), spk((76, 50), (84, 50), (82, 66), 2, z='f', light_left=False),
                         L(quad((88, 46), (64, 52), (42, 68)) + quad((46, 74), (66, 58), (88, 54)), 'strap', 'f', ln=True),
                         L([(26, 76), (16, 73)], 'strap', 'f', False, False, 2.6),
                         L(ell(36, 76, 11, 11, 8), 'shur', 'f', ln=True), L(star(36, 76, 8, 3, 0.4), 'shur_d', 'f', False),
                         L(ell(36, 76, 2, 2), OUTC, 'f', False)],
    'side': SAM_KNOT[:2] + [L(blob([(42, 8), (42, -2), (52, -2), (52, 8)], 3), 'strap', 'b', ln=True),
                            L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
                            strand([(78, 22), (50, 14), (24, 40)], 'deep', 'b', 1.0),
                            L(quad((14, 60), (50, 70), (82, 72)) + quad((82, 78), (50, 76), (14, 66)), 'strap', 'f', ln=True),
                            L(ell(86, 76, 5.6, 10, 8), 'shur', 'f', ln=True), L(ell(87, 76, 1.6, 2), OUTC, 'f', False)],
    'back': SAM_KNOT + [L(blob([(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]))] + back_hair() + [
             strand([(50, 10), (48, 80)], 'deep', 'b', 1.0),
             L(quad((10, 50), (40, 58), (90, 72)) + quad((90, 78), (40, 64), (10, 56)), 'strap', 'f', ln=True)],
}

# ------------------------------------------------------------------ Sail Bluesea: melena rosa salmón ondulada y salvaje, con
# mechones ondulados en todas direcciones; ojos rojos y un lunar en la frente
CHARS['sail-bluesea'] = {
    'body': 'normal', 'pal': pal('#c27c6c', '#fbe2c0', iris='#c03030', dot='#3a2a30'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': wavy((20, 12), (44, 2), (72, -14), 9) + wavy((48, 2), (72, 8), (102, -2), 9, light_left=False)
             + wavy((2, 44), (12, 24), (-16, 26), 11) + wavy((88, 22), (98, 44), (122, 32), -11, light_left=False)
             + wavy((0, 66), (4, 48), (-16, 74), 11) + wavy((96, 48), (100, 66), (118, 76), -11, light_left=False)
             + wavy((4, 82), (16, 90), (0, 106), -10) + wavy((84, 90), (96, 82), (104, 106), 10, light_left=False)
             + [L(blob([(8, 92), (0, 60), (8, 24), (30, 6), (50, 2), (72, 6), (92, 24), (100, 60), (92, 92), (82, 88), (82, 62), (18, 62), (18, 88)])),
                L(blob([(64, 8), (98, 46), (92, 88), (84, 86)], 6), 'shade', 'b', False), sheen(18, 44, 22, 3),
                strand([(30, 14), (14, 40), (12, 80)], 'shade', 'b', 1.0), strand([(70, 14), (88, 40), (88, 80)], 'shade', 'b', 1.0)]
             + wavy((12, 44), (30, 38), (16, 74), -5, z='f') + wavy((28, 38), (48, 36), (38, 64), -4, z='f')
             + wavy((52, 36), (70, 38), (62, 64), 4, z='f', light_left=False) + wavy((70, 40), (88, 44), (86, 76), 5, z='f', light_left=False)
             + [L(ell(44, 62, 1.8, 1.8), 'dot', 'f', False)],
    'side': wavy((40, 6), (62, 2), (40, -18), 10) + wavy((16, 18), (34, 6), (0, -6), 10) + wavy((4, 40), (12, 22), (-22, 24), 11)
            + wavy((2, 60), (6, 42), (-24, 56), -10) + wavy((6, 78), (8, 60), (-20, 84), 10) + wavy((16, 90), (18, 76), (-4, 106), -9)
            + [L(blob([(48, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
               L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
               strand([(70, 12), (40, 20), (12, 60)], 'shade', 'b', 1.0)]
            + wavy((56, 30), (88, 40), (94, 76), 6, z='f', light_left=False) + wavy((50, 56), (62, 56), (56, 92), -3, z='f'),
    'back': wavy((56, 2), (80, 12), (28, -14), -9) + wavy((28, 8), (52, 2), (-2, -2), -9)
            + wavy((88, 24), (98, 44), (116, 26), -11, light_left=False) + wavy((2, 44), (12, 22), (-22, 32), 11)
            + wavy((96, 48), (100, 66), (116, 74), -11, light_left=False) + wavy((0, 66), (4, 48), (-18, 76), 11)
            + [L(blob([(8, 92), (0, 60), (8, 24), (30, 6), (50, 2), (72, 6), (92, 24), (100, 60), (92, 92), (50, 98)]))]
            + wavy((4, 82), (22, 92), (-4, 106), -10) + wavy((24, 92), (42, 96), (22, 112), 9) + wavy((42, 96), (60, 96), (56, 116), -9)
            + wavy((60, 96), (78, 92), (80, 112), 9, light_left=False) + wavy((78, 92), (96, 82), (104, 106), 10, light_left=False)
            + [L(blob([(58, 8), (98, 46), (92, 88), (66, 94)], 6), 'shade', 'b', False), sheen(20, 46, 22, 3),
               strand([(40, 10), (30, 50), (34, 90)], 'shade', 'b', 1.0), strand([(64, 10), (70, 50), (66, 90)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ John Reynolds: piel morena, media melena castaña abombada
# con las puntas hacia fuera y una cinta naranja ancha que le cubre la frente; marcas en las mejillas
CHARS['john-reynolds'] = {
    'body': 'normal', 'pal': pal('#7a5040', '#b8703a', band='#d0661e', band_d='#a04a10', mark='#4a2418'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (52, 46)},
    'front': [L(blob([(4, 84), (2, 48), (16, 16), (50, 4), (84, 16), (98, 48), (96, 84), (82, 78), (82, 60), (18, 60), (18, 78)])),
              spk((0, 72), (10, 84), (-4, 92), 3), spk((90, 84), (100, 72), (104, 92), 3, light_left=False),
              L(blob([(62, 10), (96, 46), (94, 82), (84, 80)], 6), 'shade', 'b', False), sheen(20, 46, 20, 3),
              strand([(36, 10), (22, 44)], 'shade', 'b', 1.0), strand([(64, 10), (78, 44)], 'shade', 'b', 1.0),
              L([(18, 48), (82, 48), (82, 66), (18, 66)], 'band', 'f', ln=True), L([(18, 61), (82, 61), (82, 66), (18, 66)], 'band_d', 'f', False),
              spk((14, 40), (30, 38), (18, 56), 4, z='f'), spk((70, 38), (86, 40), (84, 56), 4, z='f', light_left=False),
              spk((28, 38), (46, 34), (38, 52), 4, z='f'), spk((54, 34), (72, 38), (62, 52), 4, z='f', light_left=False),
              spk((12, 56), (20, 56), (14, 80), 2.5, z='f'), spk((80, 56), (88, 56), (86, 80), 2.5, z='f', light_left=False),
              L([(25, 84), (31, 86)], 'mark', 'f', False, False, 1.2), L([(26, 88), (31, 89)], 'mark', 'f', False, False, 1.2),
              L([(75, 84), (69, 86)], 'mark', 'f', False, False, 1.2), L([(74, 88), (69, 89)], 'mark', 'f', False, False, 1.2)],
    'side': [L(blob([(48, 92), (12, 92), (0, 60), (6, 26), (28, 6), (58, 2), (84, 12), (98, 32), (94, 54), (78, 52), (62, 54), (56, 70), (52, 88)])),
             spk((2, 76), (14, 88), (0, 96), 3),
             L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 12, 3),
             L(quad((10, 46), (50, 40), (92, 48)) + quad((92, 64), (50, 58), (10, 62)), 'band', 'f', ln=True),
             spk((60, 30), (94, 38), (98, 52), 5, z='f', light_left=False), spk((52, 56), (62, 56), (58, 82), 2.5, z='f'),
             L([(76, 86), (81, 88)], 'mark', 'f', False, False, 1.2)],
    'back': [L(blob([(4, 84), (2, 48), (16, 16), (50, 4), (84, 16), (98, 48), (96, 84), (50, 92)])),
             spk((0, 72), (10, 84), (-4, 92), 3), spk((90, 84), (100, 72), (104, 92), 3, light_left=False),
             spk((10, 82), (30, 90), (12, 100), 4), spk((30, 90), (50, 92), (40, 104), 4), spk((50, 92), (70, 90), (62, 104), 4, light_left=False),
             spk((70, 90), (90, 82), (88, 100), 4, light_left=False),
             L(blob([(58, 10), (96, 46), (94, 82), (66, 90)], 6), 'shade', 'b', False), sheen(20, 48, 20, 3),
             strand([(40, 10), (34, 86)], 'shade', 'b', 1.0), strand([(62, 10), (68, 86)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Dan Hopper: corpulento, pelo verde muy oscuro corto y
# tupido en mechones; ceño fruncido y marcas en las mejillas
CHARS['dan-hopper'] = {
    'body': 'corpulento', 'pal': pal('#3e6a54', '#f0a868', mark='#7a4a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 48)},
    'front': [L(bumpy(50, 30, 42, 26, 12, 0.08)),
              L(blob([(10, 66), (8, 36), (92, 36), (90, 66), (80, 58), (20, 58)])),
              L(bumpy(68, 32, 20, 18, 7, 0.08), 'shade', 'b', False), L(ell(32, 14, 10, 4), 'light', 'b', False),
              spk((14, 44), (30, 40), (18, 60), 4, z='f'), spk((30, 40), (48, 38), (40, 56), 4, z='f'),
              spk((52, 38), (70, 40), (62, 56), 4, z='f', light_left=False), spk((70, 40), (86, 44), (84, 60), 4, z='f', light_left=False),
              L([(26, 82), (31, 85)], 'mark', 'f', False, False, 1.2), L([(74, 82), (69, 85)], 'mark', 'f', False, False, 1.2)],
    'side': [L(bumpy(44, 32, 40, 26, 12, 0.08)),
             L(blob(SIDE_SKULL)), L(bumpy(26, 44, 16, 18, 7, 0.08), 'shade', 'b', False),
             spk((58, 30), (88, 38), (92, 56), 5, z='f', light_left=False),
             L([(78, 82), (82, 84)], 'mark', 'f', False, False, 1.2)],
    'back': [L(bumpy(50, 34, 42, 28, 12, 0.08)),
             L(blob([(10, 70), (8, 38), (92, 38), (90, 70), (70, 86), (30, 86)])),
             L(bumpy(68, 50, 20, 24, 7, 0.08), 'shade', 'b', False), L(ell(30, 16, 10, 4), 'light', 'b', False),
             spk((14, 72), (32, 84), (8, 90), 4), spk((68, 84), (86, 72), (92, 90), 4, light_left=False)],
}

# ------------------------------------------------------------------ Cal Trops: pelo verde oliva peinado hacia atrás, pegado a la
# cabeza a un lado y con una melena larga y lisa que le cae por el otro hasta la barbilla; frente alta, nariz grande y ceño
CHARS['cal-trops'] = {
    'body': 'normal', 'pal': pal('#5e5c26', '#f8b884', nose='#e8946a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'nose': (50, 81, 5), 'nose_side': (92, 80, 4.6),
             'hairline': (52, 40)},
    'front': [L(blob([(14, 62), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (86, 62)])),
              L(blob([(60, 10), (86, 32), (84, 60), (70, 54)], 6), 'shade', 'b', False),
              strand([(30, 14), (22, 44)], 'deep', 'b', 1.0), strand([(42, 8), (36, 40)], 'deep', 'b', 1.0), strand([(56, 8), (60, 40)], 'deep', 'b', 1.0),
              L(blob([(62, 10), (84, 22), (96, 52), (98, 98), (90, 100), (84, 76), (76, 50), (64, 30)]), 'mid', 'f'),
              L(blob([(84, 30), (96, 56), (96, 96), (90, 94)], 6), 'shade', 'f', False),
              strand([(66, 30), (77, 50), (85, 76), (90, 99)], OUTC, 'f', 1.1),
              strand([(72, 20), (88, 52), (92, 94)], 'deep', 'f', 1.0)],
    'side': [L(blob([(48, 92), (16, 92), (4, 60), (8, 28), (28, 8), (56, 2), (80, 10), (92, 28), (86, 40), (64, 42), (56, 60), (52, 86)])),
             L(blob([(8, 50), (10, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False),
             strand([(84, 22), (50, 12), (20, 40), (16, 84)], 'deep', 'b', 1.0), strand([(86, 32), (52, 24), (30, 50), (28, 86)], 'deep', 'b', 1.0),
             strand([(70, 38), (42, 34), (36, 80)], 'deep', 'b', 1.0)],
    'back': [L(blob([(14, 66), (10, 34), (22, 12), (50, 4), (78, 12), (90, 34), (92, 70), (86, 96), (74, 100), (62, 92), (50, 100), (38, 92), (26, 100),
                     (14, 94)])),
             L(blob([(58, 12), (90, 36), (90, 94), (70, 96)], 6), 'shade', 'b', False)]
            + [strand([(x, 8), (x + (x - 50) * 0.15, 92)], 'deep', 'b', 1.0) for x in (30, 42, 54, 66, 78)],
}

# ------------------------------------------------------------------ Winston Falls: casco castaño muy oscuro con flequillo recto y
# las puntas vueltas hacia dentro junto a las mejillas, pendientes de shuriken y ojos medio cerrados
WIN_CURL = [(10, 68), (22, 72), (31, 82), (27, 91), (17, 92), (10, 82)]
CHARS['winston-falls'] = {
    'body': 'normal', 'pal': pal('#3a2a26', '#f8b06a', shur='#a0a0a8', shur_d='#70707a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'eye_y': 77, 'hairline': (62, 56)},
    'front': [L(blob([(6, 80), (4, 46), (16, 14), (50, 4), (84, 14), (96, 46), (94, 80), (80, 76), (80, 62), (20, 62), (20, 76)])),
              L(blob([(62, 10), (94, 44), (92, 80), (84, 78)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              strand([(50, 8), (48, 60)], 'shade', 'b', 1.0), strand([(34, 12), (30, 60)], 'shade', 'b', 1.0), strand([(66, 12), (70, 60)], 'shade', 'b', 1.0),
              L(blob(WIN_CURL), 'mid', 'f'), L(blob([(100 - x, y) for x, y in WIN_CURL]), 'mid', 'f'),
              L(blob([(80, 72), (90, 76), (90, 86), (82, 90), (74, 84)], 5), 'shade', 'f', False),
              strand([(22, 74), (30, 83), (26, 90)], OUTC, 'f', 1.1), strand([(78, 74), (70, 83), (74, 90)], OUTC, 'f', 1.1),
              L([(42, 72), (30, 70)], OUTC, 'f', False, False, 2.4), L([(58, 72), (70, 70)], OUTC, 'f', False, False, 2.4)]
             + shuriken(4, 66, 7, 0.3) + shuriken(96, 66, 7, -0.3),
    'side': [L(blob([(48, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 56), (56, 74), (54, 92)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(blob([(52, 80), (62, 82), (66, 90), (60, 95), (52, 92)]), 'mid', 'f'),
             strand([(61, 83), (65, 90), (60, 94)], OUTC, 'f', 1.0),
             spk((56, 30), (90, 40), (94, 60), 5, z='f', light_left=False),
             L([(84, 70), (74, 70)], OUTC, 'f', False, False, 2.4)]
            + shuriken(40, 60, 8, 0.3),
    'back': [L(blob([(6, 82), (4, 46), (16, 14), (50, 4), (84, 14), (96, 46), (94, 82), (50, 90)])),
             L(blob(WIN_CURL)), L(blob([(100 - x, y) for x, y in WIN_CURL])),
             L(blob([(58, 10), (94, 44), (92, 80), (66, 88)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)]
            + shuriken(4, 66, 7, 0.3) + shuriken(96, 66, 7, -0.3),
}

# ------------------------------------------------------------------ Kevin Castle (portero suplente): pelo castaño rojizo de
# pinchos, dos coletas a los lados envueltas en vendas blancas que acaban en puntas; ojeras y mirada cansada
KEVIN_TOP = [spk((10, 50), (16, 36), (-14, 36), 6), spk((14, 36), (26, 22), (-6, 8), 6), spk((24, 22), (42, 12), (22, -12), 6),
             spk((42, 12), (58, 10), (50, -16), 6), spk((56, 10), (74, 18), (78, -12), 6, light_left=False),
             spk((72, 20), (86, 34), (108, 12), 6, light_left=False), spk((84, 36), (90, 50), (114, 40), 6, light_left=False)]


def kevin_tail(x, flip=1):
    s = -flip
    return [L([(x - 5, 64), (x + 5, 64), (x + 5, 96), (x - 5, 96)], 'wrap', 'f', ln=True)] + \
           [L([(x - 5, y), (x + 5, y + 2)], 'wrap_d', 'f', False, False, 1.0) for y in (70, 77, 84, 91)] + \
           spk((x - 6, 96), (x, 96), (x - 6 + s * 8, 112), 3, z='f') + spk((x, 96), (x + 6, 96), (x + 6 - s * 4, 112), 3, z='f', light_left=False)


CHARS['kevin-castle'] = {
    'body': 'normal', 'pal': pal('#8a3a1e', '#f6c08e', wrap='#ece4dc', wrap_d='#b8aca0', bag='#c88a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 48)},
    'front': KEVIN_TOP + [L(blob([(10, 66), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 66)])),
                          L(blob([(60, 12), (90, 36), (88, 62), (74, 58)], 6), 'shade', 'b', False),
                          spk((12, 44), (30, 38), (16, 66), 5, z='f'), spk((28, 38), (46, 34), (36, 58), 4, z='f'),
                          spk((54, 34), (72, 38), (64, 58), 4, z='f', light_left=False), spk((70, 38), (88, 44), (84, 66), 5, z='f', light_left=False),
                          L(quad((30, 82), (36, 85), (42, 82)), 'bag', 'f', False, False, 1.2), L(quad((58, 82), (64, 85), (70, 82)), 'bag', 'f', False, False, 1.2)]
             + kevin_tail(12, 1) + kevin_tail(88, -1),
    'side': [spk((16, 40), (24, 24), (-18, 18), 7), spk((24, 26), (40, 14), (10, -14), 7), spk((40, 12), (60, 8), (52, -16), 6),
             spk((14, 56), (16, 40), (-18, 46), 6), spk((16, 70), (20, 58), (-12, 74), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((58, 14), (80, 22), (96, 6), 5, light_left=False),
             spk((56, 30), (88, 40), (92, 64), 5, z='f', light_left=False)]
            + kevin_tail(36, 1),
    'back': KEVIN_TOP + [L(blob([(10, 70), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 70), (72, 84), (28, 84)])),
                         spk((14, 72), (32, 84), (8, 94), 4), spk((32, 84), (50, 86), (40, 100), 4), spk((50, 86), (68, 84), (62, 100), 4, light_left=False),
                         spk((68, 84), (86, 72), (94, 94), 4, light_left=False),
                         L(blob([(58, 12), (90, 36), (88, 66), (70, 82)], 6), 'shade', 'b', False)]
            + kevin_tail(14, 1) + kevin_tail(86, -1),
}
