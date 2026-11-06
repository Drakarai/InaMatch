"""Equipos que no son personas, sin modelo en Victory Road: los Robots Guardias (IE2), los Futboloides (Chrono Stones) y
las Sombras Terribles (Galaxy), dibujados con las imágenes 2D/3D de la wiki. La "piel" es el metal o la sombra y la
equipación, la carcasa del robot o el cuerpo negro."""
from chars import CHARS, L, OUTC, blob, ell, pal, spk, strand
from heads import quad

NOFACE = {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False, 'no_head': True}


def shrink(spec, k, cy=104):
    """Encoge la cabeza (todas sus capas) hacia el cuello: estas cabezas son más pequeñas que las de un jugador."""
    for v in ('front', 'side', 'back'):
        out = []
        for item in spec[v]:
            for l in (item if isinstance(item, list) else [item]):
                out.append(dict(l, s=[(50 + (x - 50) * k, cy + (y - cy) * k) for x, y in l['s']], w=l['w'] * k if l['w'] else 0))
        spec[v] = out
    return spec

# ------------------------------------------------------------------ Robots Guardias: cabeza de bala de metal gris rosado con una
# antena, un visor oscuro con el ojo y una rejilla (cian; el portero Robo S, oscuro con el ojo y la rejilla rojos)
BULLET_F = [(14, 100), (12, 50), (20, 16), (38, 0), (50, -4), (62, 0), (80, 16), (88, 50), (86, 100), (50, 104)]


def guard(dark=False):
    c = pal('#000000', '#4a3e40' if dark else '#c8b4b0', metal='#4a3e40' if dark else '#c8b4b0', metal_d='#2e2628' if dark else '#9a8480',
            visor='#14141e', glow='#ff2a2a' if dark else '#40e8e8', ant='#2a2a34')
    front = [L([(60, 4), (64, -30)], 'ant', 'b', False, False, 2), L(blob(BULLET_F), 'metal', 'f', ln=True),
             L(blob([(58, 0), (82, 18), (84, 96), (64, 100)], 6), 'metal_d', 'f', False),
             L(blob([(24, 46), (54, 42), (56, 96), (26, 96)]), 'visor', 'f', ln=True),
             L(ell(36, 58, 6, 6), 'glow', 'f', False)] + [L([(x, 74), (x, 92)], 'glow', 'f', False, False, 2.2) for x in (32, 39, 46)] \
            + [L(ell(66, 58, 2.4, 2.4), 'glow', 'f', False)]
    side = [L([(44, 4), (40, -30)], 'ant', 'b', False, False, 2),
            L(blob([(18, 100), (10, 50), (22, 14), (46, -4), (66, 2), (84, 22), (92, 54), (92, 100), (56, 104)]), 'metal', 'f', ln=True),
            L(blob([(14, 50), (24, 18), (40, 56), (28, 98)], 6), 'metal_d', 'f', False),
            L(blob([(70, 46), (94, 46), (94, 96), (72, 96)]), 'visor', 'f', ln=True), L(ell(86, 58, 4, 6), 'glow', 'f', False)]
    back = [L([(40, 4), (36, -30)], 'ant', 'b', False, False, 2), L(blob(BULLET_F), 'metal', 'f', ln=True),
            L(blob([(56, 0), (82, 18), (84, 96), (60, 100)], 6), 'metal_d', 'f', False)]
    return {'body': 'corpulento', 'pal': c, 'face': NOFACE, 'front': front, 'side': side, 'back': back}


CHARS['robot-s'] = shrink(guard(True), 0.62)
for _r in 'ptvclobgkf':
    CHARS[f'robot-{_r}'] = shrink(guard(), 0.62)

# ------------------------------------------------------------------ Futboloides: cabeza ancha y redonda de metal con un visor oscuro
# lateral (un ojo y una rejilla) y dos aletas grandes a los lados; los hombros enormes (el portero, gris oscuro y rojo)
def footbot(dark=False):
    c = pal('#000000', '#5a4c4c' if dark else '#d4bab4', metal='#5a4c4c' if dark else '#d4bab4', metal_d='#3a3030' if dark else '#a88c86',
            visor='#14141e', glow='#ff3030' if dark else '#40e0d8', core='#a040c0' if dark else '#e83020')
    fins_f = [L(blob([(-10, 30), (2, 10), (14, 30), (12, 96), (0, 100), (-12, 70)]), 'metal', 'b', ln=True),
              L(blob([(110, 30), (98, 10), (86, 30), (88, 96), (100, 100), (112, 70)]), 'metal', 'b', ln=True),
              L(blob([(98, 14), (110, 32), (110, 70), (100, 96)], 4), 'metal_d', 'b', False)]
    head = [(10, 90), (8, 50), (20, 22), (50, 12), (80, 22), (92, 50), (90, 90), (50, 100)]
    front = fins_f + [L(blob(head), 'metal', 'f', ln=True), L(blob([(60, 16), (88, 40), (88, 88), (66, 96)], 6), 'metal_d', 'f', False),
                      L(blob([(30, 44), (62, 40), (64, 64), (32, 66)]), 'visor', 'f', ln=True), L(ell(40, 52, 4.4, 4.4), 'glow', 'f', False)] \
        + [L([(x, 50), (x, 60)], 'glow', 'f', False, False, 1.8) for x in (50, 55, 60)] + [L(ell(50, 84, 6, 6), 'core', 'f', ln=True)]
    side = [L(blob([(30, 30), (44, 8), (58, 30), (56, 96), (44, 100), (28, 70)]), 'metal', 'b', ln=True),
            L(blob([(14, 92), (8, 50), (24, 20), (54, 12), (80, 22), (94, 50), (92, 90), (52, 100)]), 'metal', 'f', ln=True),
            L(blob([(70, 42), (96, 42), (96, 64), (72, 66)]), 'visor', 'f', ln=True), L(ell(88, 52, 3.4, 4.4), 'glow', 'f', False)]
    back = fins_f + [L(blob(head), 'metal', 'f', ln=True), L(blob([(56, 16), (88, 40), (88, 88), (60, 96)], 6), 'metal_d', 'f', False)]
    return {'body': 'corpulento', 'pal': c, 'face': NOFACE, 'front': front, 'side': side, 'back': back}


CHARS['fb-101x'] = shrink(footbot(True), 0.78)
for _n in range(102, 112):
    CHARS[f'fb-{_n}x'] = shrink(footbot(), 0.78)

# ------------------------------------------------------------------ Sombras Terribles: siluetas negras de bordes cian brillantes,
# una cara blanca de máscara con dos ojos negros y una raya, y llamas de sombra en lo alto de la cabeza
SHADOW = pal('#0c1a22', '#0c1a22', mask='#f4fafc', glow='#40d8f0', shade='#0c1a22', skin_d='#08121a')
FLAMES = [spk((30, 16), (42, 8), (24, -22), 4), spk((44, 6), (56, 6), (52, -30), 4), spk((58, 8), (70, 14), (74, -18), 4, light_left=False)]
HEADBLOB = [(10, 100), (8, 50), (18, 18), (50, 4), (82, 18), (92, 50), (90, 100), (50, 106)]
CHARS['osoroshii-kage'] = {
    'body': 'delgado', 'pal': SHADOW, 'face': NOFACE,
    'front': FLAMES + [L(blob(HEADBLOB), 'mid', 'f', ln=True), L(quad((10, 96), (4, 50), (20, 16)), 'glow', 'f', False, False, 1.6),
                       L(quad((90, 96), (96, 50), (80, 16)), 'glow', 'f', False, False, 1.6),
                       L(blob([(22, 50), (50, 26), (78, 50), (74, 80), (50, 90), (26, 80)]), 'mask', 'f', False),
                       L(ell(36, 58, 4.4, 5.4), 'mid', 'f', False), L(ell(64, 58, 4.4, 5.4), 'mid', 'f', False),
                       L(quad((52, 40), (46, 60), (52, 82)), 'mid', 'f', False, False, 1.6)],
    'side': FLAMES + [L(blob([(14, 100), (6, 50), (20, 14), (50, 2), (80, 14), (94, 50), (92, 100), (50, 106)]), 'mid', 'f', ln=True),
                      L(quad((12, 96), (2, 50), (22, 12)), 'glow', 'f', False, False, 1.6),
                      L(blob([(62, 34), (90, 46), (92, 76), (70, 86)]), 'mask', 'f', False), L(ell(84, 58, 3, 5), 'mid', 'f', False)],
    'back': FLAMES + [L(blob(HEADBLOB), 'mid', 'f', ln=True), L(quad((10, 96), (4, 50), (20, 16)), 'glow', 'f', False, False, 1.6),
                      L(quad((90, 96), (96, 50), (80, 16)), 'glow', 'f', False, False, 1.6)],
}
shrink(CHARS['osoroshii-kage'], 0.85)
for _n in range(1, 12):
    CHARS[f'osoroshii-kage-{_n}'] = CHARS['osoroshii-kage']
