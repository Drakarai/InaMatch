"""Academia Polaris (Seishou Gakuen, ares-seishou-gakuen): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de
frente, perfil y espalda, y el cuerpo entero cuando el busto viene mal encuadrado).

Kidou juega aquí con su aspecto de Ares: pelo castaño rizado recogido atrás en un moño enorme, las gafas redondas verdes y la
capa roja ('ares-seishou-gakuen:jude-sharp'). 'oscar-pio' (Sasotsuka Eiji) cogía por prefijo el dibujo de Oscar de IE3: lleva
el suyo con su id.
"""
from chars import CHARS, L, OUTC, ell, messy, outline, pal, strand  # noqa: F401
from heads import quad

T = 'ares-seishou-gakuen'
WHITE = (246, 246, 246, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def spikes(cx, cy, rx, ry, n, amp, a0=0.0, a1=360.0, inner=1.0):
    """Contorno de pinchos alrededor de (cx, cy): n puntas de largo amp entre los ángulos a0 y a1 (grados)."""
    import math
    pts = []
    for i in range(n):
        ta = math.radians(a0 + (a1 - a0) * i / n)
        tb = math.radians(a0 + (a1 - a0) * (i + 0.5) / n)
        pts.append((cx + rx * inner * math.cos(ta), cy - ry * inner * math.sin(ta)))
        pts.append((cx + (rx + amp) * math.cos(tb), cy - (ry + amp) * math.sin(tb), 1))
    return pts


# Amano Masamichi (portero): una melena castaño muy oscuro enorme y salvaje, de pinchos irregulares que le abultan la
# cabeza y le caen por los lados hasta los hombros; piel morena, mirada afilada y sonrisa confiada
CHARS['mickey-way'] = {
    'body': 'corpulento', 'pal': pal('#2a1c16', '#9a6a44', iris='#2a1e14', shade='#1e1410'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 18, 15, seed=611, rx=62, ry=54, cy=46, lo=104) + [
        fringe([(14, 64), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (86, 64), (78, 52), (72, 60, 1), (64, 46), (56, 56, 1), (50, 42), (44, 56, 1),
                (36, 46), (28, 60, 1), (22, 50)])],
    'side': messy('side', 18, 13, seed=611, rx=58, ry=54, cy=44, nape=108, sweep=-0.4) + [
        fringe([(66, 2), (90, 18), (96, 42), (94, 62, 1), (86, 50), (78, 36)])],
    'back': messy('back', 18, 15, seed=611, rx=62, ry=54, cy=46, nape=110),
}

# Kotono Tomio: pelo granate rosado alborotado y abultado, de mechones que se levantan hacia todos lados; cara redonda, ojos
# grandes y redondos de pupila pequeña y media sonrisa
CHARS['kotono-tomio'] = {
    'body': 'normal', 'pal': pal('#b0485e', '#fcdcc0', iris='#3a3a3a', shade='#8a3448'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 13, seed=612, rx=50, ry=42, cy=40, lo=74) + [
        fringe([(12, 70), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 70), (80, 54), (74, 64, 1), (68, 48), (60, 60, 1), (54, 46), (48, 62, 1),
                (42, 46), (34, 60, 1), (28, 48), (20, 66, 1)]),
        strand([(30, 30), (24, 54)], 'shade', 'f', 1.0), strand([(66, 30), (72, 52)], 'shade', 'f', 1.0)],
    'side': messy('side', 12, 11, seed=612, rx=48, ry=42, cy=40, nape=94, sweep=-0.3) + [
        fringe([(64, 4), (88, 18), (96, 42), (94, 66, 1), (86, 52), (80, 62, 1), (76, 44), (66, 30)])],
    'back': messy('back', 12, 13, seed=612, rx=50, ry=42, cy=40, nape=94),
}

# Shiratori Tsumuki: media melena plateada en casco, con raya en medio y los mechones de los lados cayendo hasta la mandíbula
# y abiertos en las puntas; ojos lila tranquilos y sonrisa suave
CHARS['cygnus-starkey'] = {
    'body': 'delgado', 'pal': pal('#e6e6ec', '#fce2cc', iris='#7a78b8', shade='#b4aec0', deep='#8a8498'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 92), (6, 60), (8, 30), (22, 10), (50, 2), (78, 10), (94, 30), (96, 60), (90, 92), (84, 70), (84, 60), (16, 60), (16, 72)])),
              L(outline([(58, 6), (84, 16), (96, 44), (92, 86), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 90), (10, 56), (18, 32), (34, 18), (48, 14), (50, 26), (54, 14), (70, 18), (84, 32), (90, 56), (88, 90), (82, 68), (76, 50), (64, 36),
                      (54, 34), (50, 44), (46, 34), (34, 38), (24, 52), (18, 70)]),
              strand([(50, 4), (50, 20)], 'deep', 'f', 1.2), strand([(30, 22), (20, 60)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 14), (68, 0), (40, -2), (16, 12), (4, 36), (4, 66), (12, 88), (26, 94), (40, 88), (46, 76)])),
             L(outline([(6, 40), (28, 46), (34, 88), (14, 86)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (96, 40), (92, 76, 1), (86, 56), (78, 40), (66, 30)])],
    'back': [L(outline([(12, 86), (6, 50), (12, 18), (50, 2), (88, 18), (94, 50), (88, 86), (70, 96), (50, 92), (30, 96)])),
             L(outline([(56, 4), (86, 18), (94, 50), (88, 84), (66, 94)]), 'shade', 'b', False),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Yagihara Katsumi: melena castaño violáceo hasta la nuca con el flequillo echado a un lado, una cinta turquesa en la frente
# y gafas blancas grandes; cara de susto, dientes apretados
CHARS['ari-zimmerman'] = {
    'body': 'normal', 'pal': pal('#6a4a58', '#fce2cc', iris='#4a4a5a', shade='#4e3442', band='#4ab0a8', band_d='#2e8a82'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'glasses': WHITE, 'glasses_rect': True},
    'front': [L(outline([(12, 96), (2, 64), (2, 30), (14, 8), (40, -6), (66, -4), (88, 10), (100, 34), (98, 70), (92, 98), (84, 76), (84, 60), (16, 60), (18, 76)])),
              L(outline([(60, -2), (88, 12), (100, 40), (96, 90), (86, 60)]), 'shade', 'b', False),
              L(outline([(4, 36), (8, 26), (50, 20), (94, 26), (98, 36), (50, 30)]), 'band', 'f', ln=True),
              fringe([(14, 70), (12, 40), (40, 30), (64, 30), (88, 36), (92, 70), (86, 58), (80, 44), (64, 42), (54, 48), (40, 50), (28, 56), (20, 72)]),
              L(outline([(78, 40), (90, 44), (92, 96, 1), (84, 74), (80, 56)]), 'mid', 'f')],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (94, 34), (88, 12), (64, -4), (34, -4), (12, 10), (0, 36), (-6, 70), (-10, 92, 1), (8, 86), (20, 98, 1),
                        (30, 88), (42, 80)])),
             L(outline([(0, 40), (24, 46), (30, 86), (6, 84)]), 'shade', 'b', False),
             L(outline([(2, 30), (96, 26), (96, 34), (4, 38)]), 'band', 'f', ln=True),
             fringe([(64, 34), (90, 34), (96, 46), (94, 72, 1), (86, 54), (76, 44)])],
    'back': [L(outline([(10, 92), (4, 50), (10, 16), (40, -6), (66, -4), (90, 16), (96, 50), (92, 92), (74, 98), (64, 88), (56, 98), (44, 88), (34, 98),
                        (24, 88)])),
             L(outline([(56, -2), (88, 16), (96, 50), (90, 90), (66, 96)]), 'shade', 'b', False),
             L(outline([(6, 32), (50, 26), (94, 32), (94, 40), (50, 34), (6, 40)]), 'band', 'f', ln=True)],
}

# Mizukamiya Seiryuu: media melena azul ondulada, de raíces azul claro que oscurecen hacia las puntas, rizadas a la altura
# de la mandíbula; flequillo partido y ojos violeta afilados
CHARS['acker-reese'] = {
    'body': 'normal', 'pal': pal('#3e4ec8', '#fce2cc', iris='#6a5aa8', shade='#26308a', light='#7a8af0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 96), (-4, 84, 1), (4, 70), (0, 40), (10, 10), (34, -10), (64, -10), (88, 6), (100, 36), (98, 70), (106, 84, 1), (92, 96), (84, 74),
                         (84, 60), (16, 60), (16, 74)])),
              L(outline([(60, -6), (88, 8), (100, 40), (98, 84), (86, 60)]), 'shade', 'b', False),
              L(outline([(24, 4), (50, -6), (74, 2), (60, 8), (40, 8)]), 'light', 'b', False),
              fringe([(12, 72), (12, 40), (26, 20), (44, 12), (62, 14), (80, 24), (88, 42), (88, 72), (80, 58), (72, 46), (60, 42), (52, 62, 1), (48, 44), (36, 40),
                      (26, 50), (20, 70, 1)])],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (92, 14), (72, -6), (40, -10), (14, 4), (0, 30), (-8, 60), (-2, 84), (-12, 100, 1), (8, 94),
                        (20, 104, 1), (30, 92), (44, 84)])),
             L(outline([(-4, 44), (22, 48), (28, 90), (2, 88)]), 'shade', 'b', False),
             L(outline([(30, -4), (60, -6), (48, 6)]), 'light', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 68, 1), (86, 52), (80, 62, 1), (76, 44), (66, 30)])],
    'back': [L(outline([(8, 96), (-4, 86, 1), (4, 70), (0, 40), (10, 10), (34, -10), (64, -10), (88, 6), (100, 36), (100, 70), (106, 86, 1), (94, 96), (78, 104, 1),
                        (64, 96), (50, 106, 1), (36, 96), (22, 104, 1)])),
             L(outline([(56, -8), (88, 8), (100, 44), (96, 94), (70, 100), (70, 50)]), 'shade', 'b', False),
             L(outline([(24, 0), (50, -8), (74, 0), (50, 10)]), 'light', 'b', False)],
}

# Futagotamagawa Tetsuya: una mata enorme de pelo pardo grisáceo en pinchos hacia todos lados, con mechones que le caen por
# la frente; ojos blancos de pupila gris pequeña y boca apretada
CHARS['jimmy-nigh'] = {
    'body': 'normal', 'pal': pal('#8a7a6a', '#fcdcc0', iris='#7a7a80', shade='#6a5a4c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline(spikes(50, 34, 46, 40, 13, 18, -30, 210) + [(90, 80), (84, 66), (16, 66), (10, 80)])),
              L(outline([(60, -6), (90, 10), (104, 40), (92, 76), (84, 50)]), 'shade', 'b', False),
              fringe([(10, 72), (12, 42), (26, 24), (50, 18), (74, 24), (88, 42), (90, 72), (82, 56), (76, 66, 1), (68, 48), (60, 60, 1), (54, 46), (46, 70, 1),
                      (42, 48), (34, 62, 1), (28, 50), (20, 68, 1)])],
    'side': [L(outline(spikes(40, 34, 48, 40, 11, 18, 40, 250) + [(30, 88), (44, 80), (54, 62), (66, 50), (88, 40)])),
             L(outline([(0, 40), (24, 46), (28, 76), (6, 70)]), 'shade', 'b', False),
             fringe([(66, 4), (92, 18), (98, 42), (96, 66, 1), (88, 52), (80, 62, 1), (76, 44), (66, 30)])],
    'back': [L(outline(spikes(50, 36, 46, 42, 15, 18, -50, 230)))],
}

# Uoshima Sameharu: un tupé negro altísimo en punta, como una aleta de tiburón, peinado hacia atrás y que cae largo por la
# nuca en mechones abiertos; piel morena, orejas grandes y cara seria de nariz chata
CHARS['caesar-pike'] = {
    'body': 'corpulento', 'pal': pal('#1e2a2e', '#a06a46', iris='#7a7a80', shade='#121a1e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(14, 50), (20, 40), (36, 34), (50, 38), (64, 34), (80, 40), (86, 50)],
             'big_ears': 2},
    'front': [L(outline([(10, 104), (2, 96, 1), (8, 80), (10, 50), (16, 20), (30, 6), (42, -30, 1), (56, 4), (76, 8), (88, 22), (92, 50), (92, 80), (98, 96, 1), (90, 104),
                         (84, 70), (84, 50), (16, 50), (16, 70)])),
              L(outline([(48, -14), (60, 6), (80, 12), (90, 40), (88, 70), (80, 46)]), 'shade', 'b', False),
              strand([(30, 10), (26, 40)], 'shade', 'b', 1.0), strand([(70, 12), (74, 40)], 'shade', 'b', 1.0)],
    'side': [L(outline([(58, 46), (66, 36), (84, 30), (90, 18), (70, 4), (50, -6), (26, -40, 1), (20, -6), (6, 20), (-2, 60), (-6, 100), (-18, 116, 1), (6, 108),
                        (16, 118, 1), (26, 100), (36, 84), (44, 64)])),
             L(outline([(-2, 50), (20, 54), (24, 100), (0, 100)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 100), (6, 112, 1), (8, 70), (14, 30), (30, 8), (46, -28, 1), (56, 8), (74, 14), (88, 34), (92, 70), (94, 112, 1), (84, 100), (70, 110, 1),
                        (58, 100), (46, 112, 1), (34, 100), (24, 110, 1)])),
             L(outline([(52, -12), (58, 8), (80, 20), (90, 60), (84, 104), (66, 104), (64, 50)]), 'shade', 'b', False)],
}

# Saotome Seiya: media melena azul grisáceo claro, lisa y en capas, con flequillo largo de mechones que le cae entre los
# ojos y las puntas abiertas a la altura de la barbilla; ojos azules grandes y sonrisa
CHARS['oliver-golightly'] = {
    'body': 'delgado', 'pal': pal('#9ab0c0', '#fce2cc', iris='#3a7ad0', shade='#76889a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (-2, 86, 1), (6, 70), (4, 36), (16, 12), (40, 0), (60, 0), (84, 12), (96, 36), (94, 70), (102, 86, 1), (88, 96), (84, 72), (84, 60),
                         (16, 60), (16, 74)])),
              L(outline([(58, 2), (84, 14), (96, 40), (94, 84), (86, 60)]), 'shade', 'b', False),
              fringe([(12, 80), (10, 46), (22, 24), (40, 14), (50, 20), (60, 14), (78, 24), (90, 46), (90, 80), (82, 62), (74, 72, 1), (68, 52), (58, 64, 1), (54, 48),
                      (50, 76, 1), (46, 48), (40, 64, 1), (32, 52), (26, 72, 1), (18, 62)])],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 14), (68, 0), (38, 0), (16, 12), (4, 36), (2, 64), (-8, 78, 1), (10, 82), (18, 96, 1), (30, 86),
                        (42, 80)])),
             L(outline([(4, 40), (26, 46), (30, 82), (8, 78)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (96, 42), (94, 70, 1), (86, 54), (80, 64, 1), (76, 44), (66, 30)])],
    'back': [L(outline([(10, 88), (-4, 84, 1), (6, 70), (4, 36), (16, 12), (40, 0), (60, 0), (84, 12), (96, 36), (94, 70), (104, 84, 1), (90, 88), (72, 96), (50, 92),
                        (28, 96)])),
             L(outline([(56, 2), (84, 14), (96, 44), (90, 86), (66, 94)]), 'shade', 'b', False)],
}

# Sasotsuka Eiji: una explosión de pinchos rojos en todas direcciones, como un sol, con mechones de punta que le caen por la
# frente hasta los ojos; ojos entornados y una sonrisa torcida
CHARS['oscar-pio'] = {
    'body': 'normal', 'pal': pal('#c0302a', '#fce4cc', iris='#3a3a4a', shade='#8a1e1a', light='#e86a5a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline(spikes(50, 42, 46, 44, 16, 22, -40, 220) + [(80, 72), (20, 72)])),
              L(outline([(60, -6), (96, 14), (110, 50), (90, 76), (84, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 70), (80, 58), (76, 74, 1), (68, 52), (62, 70, 1), (56, 50), (50, 76, 1),
                      (44, 50), (38, 70, 1), (32, 52), (24, 72, 1), (18, 58)])],
    'side': [L(outline(spikes(44, 40, 46, 44, 14, 22, 30, 260) + [(36, 92), (46, 80), (54, 62), (70, 52)])),
             L(outline([(0, 40), (24, 46), (28, 80), (6, 74)]), 'shade', 'b', False),
             fringe([(66, 4), (92, 18), (98, 42), (96, 72, 1), (88, 54), (80, 66, 1), (76, 44), (66, 30)])],
    'back': [L(outline(spikes(50, 42, 46, 44, 18, 22, 0, 360)))],
}

# Orio Fuyuki: una mata enorme de pelo morado esponjoso en capas de pinchos redondeados, que se aclara a lila por debajo y
# por la nuca; ojos castaños y cara seria
CHARS['eddy-o-ryan'] = {
    'body': 'normal', 'pal': pal('#7a5ac8', '#fce2cc', iris='#6a3a22', shade='#5a40a0', low='#b8a0d4', low_d='#9a84bc'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline(spikes(50, 70, 50, 26, 9, 14, 190, 350)), 'low', 'b'),
              L(outline(spikes(50, 30, 52, 40, 12, 14, -20, 200) + [(92, 66), (84, 62), (16, 62), (8, 66)])),
              L(outline([(60, -10), (92, 6), (106, 40), (92, 62), (84, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (88, 66), (80, 54), (74, 62, 1), (68, 48), (60, 58, 1), (54, 44), (48, 60, 1),
                      (42, 46), (34, 58, 1), (28, 48), (20, 62, 1)])],
    'side': [L(outline(spikes(26, 70, 34, 30, 7, 14, 160, 330)), 'low', 'b'),
             L(outline(spikes(40, 30, 52, 42, 12, 14, 30, 250) + [(30, 70), (48, 64), (60, 50), (88, 40)])),
             fringe([(66, 4), (92, 18), (98, 42), (96, 64, 1), (88, 50), (78, 36)])],
    'back': [L(outline(spikes(50, 74, 52, 28, 9, 14, 180, 360)), 'low', 'b'),
             L(outline(spikes(50, 30, 52, 40, 12, 14, -10, 190) + [(90, 60), (50, 54), (10, 60)])),
             L(outline([(50, 80), (54, 100), (50, 110, 1), (46, 100)]), 'low_d', 'b', False)],
}

# Haizaki Ryouhei: melena larga gris ondulada que le cae hasta el pecho y le tapa el ojo derecho, con un mechón suelto que se
# riza hacia arriba y un mechón rojo en el flequillo; piel morena, ojo rojo y sonrisa de dientes
CHARS['elliot-ember'] = {
    'body': 'normal', 'pal': pal('#8a8a8c', '#9a6a48', iris='#c0201e', shade='#5e5e60', red='#c81e24'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(10, 120), (0, 90), (2, 50), (14, 18), (40, 4), (66, 6), (88, 22), (98, 56), (96, 96), (102, 124, 1), (88, 110), (84, 70), (16, 70), (18, 110)])),
              L(quad((14, 24), (-2, 10), (6, -6)), 'mid', 'b', False, False, 2.6),
              L(outline([(60, 6), (88, 22), (100, 60), (98, 112), (86, 80)]), 'shade', 'b', False),
              fringe([(12, 96), (8, 56), (20, 26), (44, 14), (70, 18), (88, 38), (90, 74), (82, 60), (74, 56), (62, 50), (56, 60), (52, 96, 1), (42, 92), (30, 104, 1),
                      (22, 96)]),
              L(outline([(46, 18), (54, 16), (52, 60), (48, 64)]), 'red', 'f', False)],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 14), (68, 0), (38, 2), (14, 16), (2, 44), (-4, 80), (-10, 116, 1), (6, 108), (16, 124, 1),
                        (28, 110), (40, 88), (46, 76)])),
             L(quad((20, 10), (6, -6), (14, -20)), 'mid', 'b', False, False, 2.6),
             L(outline([(0, 46), (24, 50), (30, 104), (6, 104)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (96, 44), (94, 80, 1), (86, 58), (78, 40), (66, 30)])],
    'back': [L(outline([(8, 116), (2, 80), (6, 40), (18, 12), (44, 2), (66, 4), (88, 16), (98, 48), (100, 90), (98, 124, 1), (84, 112), (70, 126, 1), (58, 112),
                        (46, 126, 1), (34, 112), (20, 124, 1)])),
             L(quad((86, 20), (100, 6), (94, -10)), 'mid', 'b', False, False, 2.6),
             L(outline([(56, 4), (88, 16), (100, 50), (96, 116), (68, 116), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 70), (30, 112)], 'deep', 'b', 1.0), strand([(60, 10), (64, 70), (58, 114)], 'deep', 'b', 1.0)],
}

# Okuma Hokuto: pelo verde menta muy claro en casco de seta, con flequillo recto cortado sobre las cejas y la capa de debajo
# castaña que asoma por la nuca; ojos rosas de párpados caídos
CHARS['holt-northam'] = {
    'body': 'normal', 'pal': pal('#cce0b0', '#fce2cc', iris='#c04a70', shade='#a8bc8c', low='#8a6a5a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (4, 62), (8, 30), (24, 8), (50, 0), (76, 8), (92, 30), (96, 62), (88, 96), (84, 70), (84, 60), (16, 60), (16, 72)])),
              L(outline([(58, 4), (84, 16), (96, 44), (90, 88), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (26, 20), (50, 12), (74, 20), (88, 40), (88, 66), (80, 64), (80, 58), (72, 64), (72, 58), (64, 64), (64, 58), (56, 64),
                      (56, 58), (48, 64), (48, 58), (40, 64), (40, 58), (32, 64), (32, 58), (24, 64), (24, 58), (18, 64)]),
              strand([(30, 22), (28, 56)], 'shade', 'f', 1.0), strand([(50, 14), (50, 56)], 'shade', 'f', 1.0), strand([(70, 22), (72, 56)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 62), (60, 50), (82, 50), (94, 36), (90, 14), (68, 0), (40, -2), (16, 12), (4, 40), (4, 70), (14, 94), (32, 98), (44, 84)])),
             L(outline([(4, 56), (40, 56), (44, 86), (30, 98), (12, 94), (4, 74)]), 'low', 'b', False),
             fringe([(64, 4), (90, 18), (96, 44), (96, 66), (86, 66), (82, 46), (70, 34)])],
    'back': [L(outline([(10, 90), (4, 50), (12, 18), (50, 2), (88, 18), (96, 50), (90, 90), (70, 100), (50, 96), (30, 100)])),
             L(outline([(8, 60), (50, 50), (92, 60), (92, 88), (70, 98), (50, 94), (30, 98), (10, 88)]), 'low', 'b', False)],
}

# Shishitani Yuusuke: pelo negro despeinado hasta la nuca con un gran mechón rubio que le sale de la frente, peinado hacia un
# lado y hacia arriba en dos picos; ojos rojos y sonrisa de pillo
CHARS['braveon-halvors'] = {
    'body': 'normal', 'pal': pal('#262c30', '#fce2cc', iris='#d02a40', shade='#161a1e', gold='#e8d040', gold_d='#b8a020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 96), (-2, 86, 1), (6, 72), (2, 40), (12, 12), (36, -6), (64, -6), (88, 8), (100, 36), (96, 72), (104, 86, 1), (90, 96), (84, 72), (84, 60),
                         (16, 60), (16, 74)])),
              L(outline([(58, -2), (88, 10), (100, 40), (96, 84), (86, 60)]), 'shade', 'b', False),
              L(outline([(12, 70), (14, 40), (24, 14), (36, -14, 1), (46, 4), (58, -10, 1), (66, 6), (80, 14), (88, 36), (82, 50), (72, 36), (58, 30), (46, 34),
                         (34, 46), (24, 60, 1)]), 'gold', 'f', ln=True),
              L(outline([(40, 6), (52, 2), (48, 22), (40, 30)]), 'gold_d', 'f', False),
              fringe([(86, 46), (90, 70, 1), (82, 60), (78, 46)])],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 14), (68, -6), (36, -6), (12, 8), (0, 36), (-6, 70), (-14, 90, 1), (6, 86), (2, 104, 1), (20, 94),
                        (30, 104, 1), (40, 86)])),
             L(outline([(0, 40), (24, 46), (28, 86), (4, 84)]), 'shade', 'b', False),
             L(outline([(62, 30), (66, 4), (80, -12, 1), (78, 6), (94, 16), (98, 40), (94, 60, 1), (86, 46), (76, 40)]), 'gold', 'f', ln=True)],
    'back': [L(outline([(8, 96), (-4, 88, 1), (4, 70), (2, 40), (12, 12), (36, -6), (64, -6), (88, 8), (100, 36), (98, 70), (106, 88, 1), (92, 96), (76, 104, 1),
                        (64, 96), (50, 106, 1), (36, 96), (22, 104, 1)])),
             L(outline([(56, -4), (88, 10), (100, 44), (96, 94), (68, 98), (70, 50)]), 'shade', 'b', False)],
}

# Kani Kenzou (portero suplente): pelo rojo salmón corto con una coleta alta y tiesa que sale disparada hacia atrás, y unas
# patillas en zigzag que le bajan por las mejillas; ojos enfadados y orejas grandes
CHARS['konrad-hardin'] = {
    'body': 'corpulento', 'pal': pal('#e85a5a', '#fcd8b4', iris='#3a4a6a', shade='#c03e40'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(30, 4), (16, -12), (0, -16, 1), (22, -4), (14, 6, 1), (34, 6)])),
              L(outline([(16, 70), (12, 36), (22, 12), (50, 4), (78, 12), (88, 36), (84, 70), (80, 56), (20, 56)])),
              L(outline([(56, 6), (80, 14), (88, 40), (84, 60), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 36), (30, 22), (50, 30, 1), (70, 22), (84, 36), (86, 56), (76, 44), (64, 42), (56, 50, 1), (50, 40), (44, 50, 1), (36, 42),
                      (24, 44)]),
              L(outline([(14, 54), (22, 56), (22, 66), (28, 70), (22, 76), (28, 82), (20, 92), (16, 80)]), 'mid', 'f'),
              L(outline([(86, 54), (78, 56), (78, 66), (72, 70), (78, 76), (72, 82), (80, 92), (84, 80)]), 'mid', 'f'),
              L(ell(50, 8, 6, 3), WHITE, 'f', ln=True)],
    'side': [L(outline([(36, 6), (20, -20), (-6, -30, 1), (12, -10), (-8, -4, 1), (20, 4), (30, 14)])),
             L(outline([(56, 56), (62, 46), (80, 40), (90, 26), (82, 10), (60, 2), (36, 4), (16, 16), (8, 40), (10, 64), (22, 80), (36, 76), (46, 66)])),
             L(outline([(52, 60), (58, 62), (56, 78), (62, 84), (54, 90), (50, 76)]), 'mid', 'f'),
             L(outline([(10, 36), (28, 40), (30, 66), (14, 62)]), 'shade', 'b', False), L(ell(34, 6, 4, 4), WHITE, 'f', ln=True)],
    'back': [L(outline([(16, 74), (12, 36), (22, 12), (50, 4), (78, 12), (88, 36), (84, 74), (50, 80)])),
             L(outline([(56, 6), (80, 14), (88, 44), (84, 70), (62, 78)]), 'shade', 'b', False),
             L(outline([(44, 12), (40, -14), (30, -30, 1), (50, -16), (66, -34, 1), (62, -12), (56, 12)])),
             L(ell(50, 10, 6, 3), WHITE, 'f', ln=True)],
}

# Yazu Meita: pelo verde salvia en capas de mechones despeinados que se abren hacia los lados y la nuca, más oscuro por debajo;
# piel morena clara, ojos grises y cara seria
CHARS['aren-yarrow'] = {
    'body': 'normal', 'pal': pal('#9aa878', '#d8a074', iris='#6a6a70', shade='#6e7a52', low='#5e5040'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 12, seed=615, rx=50, ry=40, cy=40, lo=78, sweep=0.3) + [
        L(outline([(14, 82), (10, 92, 1), (18, 86), (20, 70)]), 'low', 'b'), L(outline([(86, 82), (90, 92, 1), (82, 86), (80, 70)]), 'low', 'b'),
        fringe([(12, 76), (12, 42), (26, 24), (50, 16), (74, 24), (88, 42), (88, 74), (80, 58), (74, 68, 1), (68, 50), (58, 62, 1), (54, 46), (48, 66, 1),
                (42, 48), (34, 62, 1), (28, 50), (20, 70, 1)])],
    'side': messy('side', 14, 11, seed=615, rx=48, ry=40, cy=40, nape=96, sweep=-0.5) + [
        fringe([(64, 4), (90, 18), (96, 42), (94, 68, 1), (86, 52), (80, 62, 1), (76, 44), (66, 30)])],
    'back': messy('back', 12, 13, seed=615, rx=50, ry=40, cy=40, nape=98) + [
        L(outline([(30, 80), (50, 86), (70, 80), (60, 98, 1), (50, 90), (40, 98, 1)]), 'low', 'f', False)],
}

# Kidou en Ares: pelo castaño claro rizado, de bucles abultados por arriba, recogido atrás en un moño enorme de rizos; las
# gafas redondas verdes de cristal grueso con la correa azul y la capa roja
CHARS[f'{T}:jude-sharp'] = {
    'body': 'normal', 'cape': '#d81e24', 'pal': pal('#9a7a3e', '#fcdcbc', shade='#7a5c2a', light='#c8a464', strap='#2a5a8a', lens='#3a6a2a', lens_l='#8ac880',
                                                  rim='#e8e8e8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline(spikes(50, 34, 44, 36, 14, 8, -30, 210) + [(90, 70), (84, 60), (16, 60), (10, 70)])),
              L(outline([(60, 0), (88, 14), (100, 44), (90, 66), (84, 44)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (76, 54), (68, 60), (60, 52), (50, 58), (40, 52), (32, 60), (24, 54)]),
              strand([(30, 4), (36, 14), (30, 24)], 'shade', 'f', 1.2), strand([(56, 0), (62, 10), (56, 20)], 'shade', 'f', 1.2),
              L(outline([(10, 72), (90, 72), (90, 82), (10, 82)]), 'strap', 'f', ln=True),
              L(ell(34, 77, 12, 11), 'rim', 'f', ln=True), L(ell(66, 77, 12, 11), 'rim', 'f', ln=True),
              L(ell(34, 77, 8.6, 8), 'lens', 'f', ln=True), L(ell(66, 77, 8.6, 8), 'lens', 'f', ln=True),
              L(ell(31, 74, 3, 2.6), 'lens_l', 'f', False), L(ell(63, 74, 3, 2.6), 'lens_l', 'f', False)],
    'side': [L(outline(spikes(-4, 44, 30, 36, 11, 7, 0, 360)), 'mid', 'b'),
             L(outline(spikes(46, 34, 44, 36, 12, 8, 20, 200) + [(30, 70), (48, 62), (60, 52), (86, 46)])),
             L(outline([(-20, 30), (0, 20), (14, 40), (-4, 60)]), 'shade', 'b', False),
             L(outline([(20, 74), (96, 70), (96, 80), (22, 82)]), 'strap', 'f', ln=True),
             L(ell(90, 76, 7, 10), 'rim', 'f', ln=True), L(ell(92, 76, 4, 7), 'lens', 'f', ln=True)],
    'back': [L(outline(spikes(50, 40, 44, 38, 16, 8, 0, 360))),
             L(outline(spikes(50, 60, 34, 32, 12, 7, 0, 360)), 'shade', 'f', ln=True),
             L(outline([(10, 74), (50, 80), (90, 74), (90, 82), (50, 88), (10, 82)]), 'strap', 'b', ln=True)],
}
