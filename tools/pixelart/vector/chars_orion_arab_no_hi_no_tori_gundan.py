"""Ejército del Fénix Árabe (orion-arab-no-hi-no-tori-gundan): sus modelos 3D de Inazuma Eleven: Orion no Kokuin
(オリオンの刻印) en la enciclopedia, de frente, perfil y espalda. Todos tienen una sola forma y ninguno coge por prefijo el
dibujo de otro personaje. Aquí también van las ayudas de dibujo que usan los otros dos equipos de Orion de este lote."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (28, 24, 26, 255)
RED = (206, 44, 40, 255)


def curls(cx, cy, r, n=8, a0=0.0, k2=0.8):
    """Contorno de nube de rizos (bultos redondos alrededor de un centro)."""
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else k2
        pts.append((cx + r[0] * k * math.cos(a), cy + r[1] * k * math.sin(a)))
    return blob(pts, 6)


def knobby(cx, cy, rx, ry, n=14, depth=9, half=0.32, a0=0.0):
    """Masa redonda con salientes cuadrados alrededor (pelo de nudos/bloques)."""
    pts = []
    for i in range(n):
        a = a0 + math.pi * 2 * i / n
        for da, dr in ((-0.5, 0), (-half, 0), (-half, 1), (half, 1), (half, 0)):
            b = a + da * math.pi * 2 / n
            rr = 1 + dr * depth / max(rx, ry)
            pts.append((cx + rx * rr * math.cos(b), cy + ry * rr * math.sin(b)))
    return pts


def clipy(poly, y0, y1):
    """Recorta un polígono a la franja y0 <= y <= y1 (Sutherland-Hodgman)."""
    def clip(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            a, b = pts[i - 1], pts[i]
            if inside(b):
                if not inside(a):
                    out.append(inter(a, b))
                out.append(b)
            elif inside(a):
                out.append(inter(a, b))
        return out

    def at(y):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (y - a[1]) / ((b[1] - a[1]) or 1e-9), y)
    p = clip(list(poly), lambda q: q[1] >= y0, at(y0))
    return clip(p, lambda q: q[1] <= y1, at(y1)) if p else []


def clipx(poly, x0, x1):
    sw = [(y, x) for x, y in poly]
    return [(x, y) for y, x in clipy(sw, x0, x1)]


def patch(cx, cy, rx=11, ry=8.5, tilt=0.0, studs=WHITE, view='front', strap_to=None):
    """Parche de ojo negro ovalado con tres tachuelas y la cinta."""
    out = []
    if strap_to:
        out.append(L([(cx, cy - ry * 0.6), strap_to], BLACK, 'f', False, False, 1.4))
    sh = [(cx + rx * math.cos(a) * math.cos(tilt) - ry * math.sin(a) * math.sin(tilt),
           cy + rx * math.cos(a) * math.sin(tilt) + ry * math.sin(a) * math.cos(tilt)) for a in [2 * math.pi * i / 36 for i in range(36)]]
    out.append(L(sh, BLACK, 'f'))
    for k in (-1, 0, 1):
        out.append(L(ell(cx + k * rx * 0.42, cy + k * rx * 0.42 * math.sin(tilt), 1.5, 1.5), studs, 'f', False))
    return out


def lids(cx, s, ey=75, iris=(240, 230, 150, 255), lid=OUTC):
    """Ojo entornado (párpado gordo que tapa media pupila): para caras de sueño o de chulería."""
    eye = [(cx - 7 * s, ey - 1), (cx + 7 * s, ey - 1), (cx + 6 * s, ey + 3.5), (cx - 6 * s, ey + 3.5)]
    return [L(blob(eye, 4), iris, 'f', False), L(ell(cx + s, ey + 1.5, 1.4, 1.8), OUTC, 'f', False),
            L([(cx - 8 * s, ey - 1.5), (cx + 8 * s, ey - 1.5)], lid, 'f', False, False, 2.6)]


# Falcon (Falcon Ali, portero): pelo verde azulado en pinchos revueltos hacia arriba y a los lados, con mechones que le
# caen entre los ojos; cejas azul marino gruesas y enfadadas, ojos color oliva y el ceño fruncido
BROW_NAVY = (34, 52, 120, 255)
CHARS['falcon'] = {
    'body': 'normal', 'pal': pal('#1c8c98', '#fcd4b2', iris='#9c8c3c', shade='#146a76', deep='#0e4c56'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'hairline': [(14, 64), (26, 54), (40, 50), (50, 56), (60, 50), (74, 54), (86, 64)]},
    'front': [L(outline([(16, 66), (8, 50), (0, 42, 1), (8, 32), (-2, 18, 1), (12, 12), (12, -4, 1), (28, 2), (36, -12, 1), (44, -2), (50, -24, 1), (56, -4),
                         (68, -8, 1), (70, 4), (88, -2, 1), (84, 14), (100, 20, 1), (90, 30), (100, 44, 1), (88, 46), (86, 66), (78, 56), (22, 56)])),
              L(outline([(56, -4), (68, -8), (70, 4), (88, -2), (84, 14), (100, 20), (90, 30), (100, 44), (88, 50), (76, 30), (62, 14)]), 'shade', 'b', False),
              strand([(30, 10), (36, 26), (32, 40)], 'deep', 'b', 1.0), strand([(56, 6), (62, 24), (70, 34)], 'deep', 'b', 1.0),
              L(outline([(38, 46), (46, 46), (50, 72, 1), (54, 46), (62, 46), (52, 40)]), 'mid', 'f', ln=True),
              L(outline([(22, 50), (32, 48), (20, 68, 1)]), 'mid', 'f', ln=True), L(outline([(68, 48), (78, 50), (80, 66, 1)]), 'mid', 'f', ln=True),
              L(outline([(24, 61), (44, 67, 1), (43, 71), (26, 67)]), BROW_NAVY, 'f', False),
              L(outline([(76, 61), (56, 67, 1), (57, 71), (74, 67)]), BROW_NAVY, 'f', False)],
    'side': [L(outline([(74, 58), (80, 46), (86, 36), (94, 30, 1), (86, 22), (94, 8, 1), (80, 4), (78, -14, 1), (66, -6), (54, -24, 1), (48, -6), (30, -10, 1),
                        (30, 2), (10, 2, 1), (16, 14), (-6, 22, 1), (8, 32), (-6, 46, 1), (10, 50), (2, 64, 1), (16, 64), (22, 82, 1), (32, 72), (40, 72),
                        (44, 60), (56, 56), (64, 60)])),
             L(outline([(-6, 46), (10, 50), (2, 64), (16, 64), (22, 82), (32, 72), (40, 72), (44, 60), (28, 54), (12, 40)]), 'shade', 'b', False),
             strand([(60, 0), (70, 16), (80, 26)], 'deep', 'b', 1.0), strand([(36, 4), (40, 22), (36, 40)], 'deep', 'b', 1.0),
             L(outline([(74, 50), (84, 52), (82, 70, 1)]), 'mid', 'f', ln=True),
             L(outline([(72, 61), (86, 66, 1), (85, 69), (73, 65)]), BROW_NAVY, 'f', False)],
    'back': [L(outline([(16, 66), (4, 52, 1), (10, 40), (-2, 28, 1), (12, 20), (10, 4, 1), (26, 6), (32, -10, 1), (44, 0), (52, -22, 1), (56, -2), (70, -6, 1),
                        (72, 8), (90, 4, 1), (86, 20), (100, 30, 1), (88, 40), (96, 54, 1), (84, 62), (80, 80), (66, 88), (56, 96, 1), (50, 88), (42, 96, 1),
                        (36, 88), (22, 82)])),
             L(outline([(56, -2), (70, -6), (72, 8), (90, 4), (86, 20), (100, 30), (88, 40), (96, 54), (84, 62), (80, 80), (66, 88), (62, 40)]), 'shade', 'b', False),
             strand([(40, 10), (44, 40), (40, 70)], 'deep', 'b', 1.0), strand([(28, 30), (26, 60)], 'deep', 'b', 1.0)],
}

# Osprey Al-Bahar (Gala Magos): grandullón de piel oscura; una mata negra de nudos cuadrados alrededor de toda la cabeza,
# barba negra cerrada que le enmarca la cara, cejas negras de bloque en forma de escuadra y ojitos redondos
OSP_HAIR = blob(knobby(50, 42, 44, 40, 12, 13, 0.36, -math.pi / 2), 3)
CHARS['osprey-al-bahar'] = {
    'body': 'corpulento', 'pal': pal('#1e1c22', '#7a5038', shade='#141218', deep='#0a0a0e', light='#3a3840'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'eye_sep': 13, 'hairline': [(14, 66), (20, 58), (44, 56), (50, 62), (56, 56), (80, 58), (86, 66)]},
    'front': [L(OSP_HAIR), L(clipx(OSP_HAIR, 56, 110), 'shade', 'b', False),
              L(outline([(18, 64), (24, 82), (36, 96), (50, 100), (64, 96), (76, 82), (82, 64), (86, 74), (82, 92), (66, 106), (50, 110), (34, 106), (18, 92),
                         (14, 74)]), 'mid', 'f'),
              L([(24, 62), (44, 62), (44, 68), (30, 68), (30, 76), (24, 76)], 'mid', 'f', False),
              L([(76, 62), (56, 62), (56, 68), (70, 68), (70, 76), (76, 76)], 'mid', 'f', False),
              L([(47, 70), (53, 70), (53, 82), (47, 82)], 'skin_d', 'f', False)],
    'side': [L(blob(knobby(34, 40, 42, 40, 12, 13, 0.36, -math.pi / 2 + 0.2), 3)),
             L(outline([(46, 74), (52, 86), (66, 98), (82, 100), (86, 92), (74, 92), (62, 84), (56, 70)]), 'mid', 'f'),
             L([(76, 62), (86, 62), (86, 68), (82, 68), (82, 76), (76, 76)], 'mid', 'f', False)],
    'back': [L(blob(knobby(50, 46, 44, 42, 12, 13, 0.36, -math.pi / 2 + 0.26), 3)), L(clipx(blob(knobby(50, 46, 44, 42, 12, 13, 0.36, -math.pi / 2 + 0.26), 3), 58, 110), 'shade', 'b', False)],
}

# Merlin Al-Yaman (Pecka Rheam): melena afro enorme de rizos, roja arriba y que se oscurece hasta casi negra por abajo,
# hasta los hombros, con raya en medio; cara alargada, ojos amarillos con pintura roja alrededor
MER_TOP = '#c8282c'
CHARS['merlin-al-yaman'] = {
    'body': 'normal', 'pal': pal('#4a0e18', '#a86c48', iris='#e2c42a', shade='#300810', deep='#22060c', top=MER_TOP, top_d='#8e1a22'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': [(16, 84), (20, 62), (34, 52), (48, 50), (50, 56), (52, 50), (66, 52), (80, 62), (84, 84)]},
    'front': [L(curls(50, 54, (62, 60), 11, 0.1)), L(curls(50, 30, (54, 36), 9, 0.3), 'top_d', 'b', False), L(curls(50, 22, (44, 28), 8), 'top', 'b', False),
              L(outline([(14, 60), (26, 56), (24, 80), (22, 104), (12, 96)]), 'mid', 'f'), L(outline([(86, 60), (74, 56), (76, 80), (78, 104), (88, 96)]), 'mid', 'f'),
              L(outline([(28, 54), (48, 50), (36, 62), (26, 70)]), 'top_d', 'f', False), L(outline([(72, 54), (52, 50), (64, 62), (74, 70)]), 'top_d', 'f', False),
              L([(30, 80), (28, 88)], RED, 'f', False, False, 1.6), L([(34, 81), (34, 90)], RED, 'f', False, False, 1.6),
              L([(70, 80), (72, 88)], RED, 'f', False, False, 1.6), L([(66, 81), (66, 90)], RED, 'f', False, False, 1.6),
              L([(26, 72), (44, 76)], RED, 'f', False, False, 1.0), L([(74, 72), (56, 76)], RED, 'f', False, False, 1.0)],
    'side': [L(curls(40, 54, (54, 60), 10, 0.2)), L(curls(42, 28, (48, 34), 8), 'top_d', 'b', False), L(curls(44, 20, (38, 26), 7, 0.4), 'top', 'b', False),
             L(outline([(70, 54), (80, 58), (78, 80), (70, 100), (62, 84)]), 'mid', 'f'),
             L([(80, 81), (80, 89)], RED, 'f', False, False, 1.6)],
    'back': [L(curls(50, 56, (62, 58), 11, 0.1)), L(curls(50, 30, (54, 34), 9, 0.3), 'top_d', 'b', False), L(curls(50, 20, (44, 26), 8), 'top', 'b', False)],
}

# Kestrel Al-Sahir (Sami Luis): piel morena, pelo blanco con sombras rosadas en pinchos revueltos muy altos y abiertos
# a los lados, con dos mechones gris oscuro en las sienes; ojos rojos, ceño fruncido y media sonrisa
GRAYLOCK = (70, 66, 70, 255)
CHARS['kestrel-al-sahir'] = {
    'body': 'normal', 'pal': pal('#f4f0f2', '#b47848', iris='#d4401c', shade='#cdb8be', deep='#a8929a', light='#ffffff'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': [(16, 64), (24, 52), (40, 50), (50, 58), (60, 50), (76, 52), (84, 64)]},
    'front': [L(outline([(18, 66), (14, 50), (0, 42, 1), (10, 34), (4, 20, 1), (16, 18), (14, 2, 1), (28, 8), (32, -6, 1), (42, 4), (50, -6, 1), (56, 4), (66, -6, 1),
                         (70, 8), (84, 2, 1), (84, 18), (98, 20, 1), (88, 32), (100, 44, 1), (86, 50), (82, 66), (76, 56), (24, 56)])),
              L(outline([(56, 4), (66, -6), (70, 8), (84, 2), (84, 18), (98, 20), (88, 32), (100, 44), (86, 52), (74, 30), (62, 16)]), 'shade', 'b', False),
              strand([(26, 16), (32, 30), (30, 42)], 'deep', 'b', 1.0), strand([(46, 8), (48, 24)], 'deep', 'b', 1.0), strand([(64, 12), (68, 28), (74, 38)], 'deep', 'b', 1.0),
              L(outline([(30, 50), (40, 48), (50, 60, 1), (56, 48), (68, 50), (52, 42)]), 'mid', 'f', ln=True),
              L(quad((20, 52), (16, 58), (22, 66)), GRAYLOCK, 'f', False, False, 2.6), L(quad((80, 52), (84, 58), (78, 66)), GRAYLOCK, 'f', False, False, 2.6)],
    'side': [L(outline([(74, 58), (80, 46), (90, 40, 1), (82, 32), (92, 18, 1), (78, 16), (82, 0, 1), (66, 8), (60, -8, 1), (50, 6), (34, -6, 1), (32, 10), (12, 8, 1),
                        (18, 22), (-4, 30, 1), (10, 40), (-2, 56, 1), (12, 58), (14, 76, 1), (26, 68), (36, 70), (44, 60), (56, 56), (64, 60)])),
             L(outline([(-4, 30), (10, 40), (-2, 56), (12, 58), (14, 76), (26, 68), (36, 70), (44, 60), (26, 50), (12, 34)]), 'shade', 'b', False),
             strand([(56, 8), (64, 22), (76, 30)], 'deep', 'b', 1.0), strand([(36, 10), (38, 30)], 'deep', 'b', 1.0),
             L(quad((70, 50), (76, 56), (72, 64)), GRAYLOCK, 'f', False, False, 2.6)],
    'back': [L(outline([(18, 66), (4, 54, 1), (12, 44), (0, 32, 1), (14, 26), (8, 8, 1), (24, 12), (30, -4, 1), (42, 6), (52, -6, 1), (58, 6), (70, -4, 1), (72, 12),
                        (90, 8, 1), (86, 24), (100, 32, 1), (88, 42), (96, 56, 1), (84, 62), (80, 82), (64, 90), (50, 100, 1), (36, 90), (22, 82)])),
             L(outline([(58, 6), (70, -4), (72, 12), (90, 8), (86, 24), (100, 32), (88, 42), (96, 56), (84, 62), (80, 82), (64, 90), (62, 40)]), 'shade', 'b', False),
             L(curls(50, 50, (22, 20), 6), 'light', 'b', False),
             strand([(36, 70), (50, 98)], 'deep', 'b', 1.0), strand([(64, 70), (50, 98)], 'deep', 'b', 1.0)],
}

# Buzzard Al-Sahma (Dorgan Butler): una melena roja oscura enorme como una capucha que le envuelve la cabeza y le cae
# hasta los hombros, con las puntas de delante naranjas; de perfil, una cola larguísima hacia atrás; cinta fina azul en la
# frente, ojos entornados de chulo y la lengua fuera
TIP = (236, 96, 36, 255)
BAND = (60, 60, 120, 255)
BUZ_HOOD = outline([(-4, 108), (-4, 80), (6, 50), (22, 26), (50, 16), (78, 26), (94, 50), (104, 80), (104, 108), (84, 108), (82, 86), (78, 64), (50, 54), (22, 64),
                    (18, 86), (16, 108)])
CHARS['buzzard-al-sahma'] = {
    'body': 'normal', 'pal': pal('#8a1010', '#a8744e', iris='#d8b434', shade='#6a0a0c', deep='#4a0608', tongue='#e07070'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'hairline': [(14, 66), (30, 58), (50, 54), (70, 58), (86, 66)]},
    'front': [L(BUZ_HOOD), L(clipx(BUZ_HOOD, 62, 110), 'shade', 'b', False),
              L(clipy(BUZ_HOOD, 96, 130), TIP, 'b', False), L(clipy(clipx(BUZ_HOOD, -20, 20), 90, 96), (190, 50, 30, 255), 'b', False),
              L(clipy(clipx(BUZ_HOOD, 80, 120), 90, 96), (190, 50, 30, 255), 'b', False),
              L(quad((16, 64), (50, 54), (84, 64)), BAND, 'f', False, False, 1.2)]
             + lids(36, 1, 76, (232, 210, 90, 255)) + lids(64, -1, 76, (232, 210, 90, 255))
             + [L(quad((26, 70), (34, 66), (44, 70)), OUTC, 'f', False, False, 1.6), L(quad((74, 70), (66, 66), (56, 70)), OUTC, 'f', False, False, 1.6),
                L(ell(53, 95, 3, 2.4), 'tongue', 'f')],
    'side': [L(outline([(80, 66), (86, 44), (78, 24), (62, 14), (40, 12), (20, 22), (4, 44), (-6, 74), (-14, 102), (-18, 120), (-6, 122), (4, 94), (14, 74), (28, 64),
                        (44, 60), (60, 58), (72, 62)])),
             L(outline([(4, 44), (-6, 74), (-14, 102), (-18, 120), (-6, 122), (4, 94), (14, 74), (28, 64), (20, 46)]), 'shade', 'b', False),
             L(outline([(74, 56), (84, 60), (88, 84), (84, 102), (76, 86)]), 'mid', 'f'),
             L(clipy(outline([(74, 56), (84, 60), (88, 84), (84, 102), (76, 86)]), 86, 110), TIP, 'f', False),
             L([(74, 62), (86, 60)], BAND, 'f', False, False, 1.2)]
            + [L([(76, 75), (85, 75)], OUTC, 'f', False, False, 2.4), L(ell(84, 94, 2.4, 2), 'tongue', 'f')],
    'back': [L(outline([(-4, 104), (-6, 80), (6, 50), (22, 26), (50, 16), (78, 26), (94, 50), (106, 80), (104, 104), (50, 108)])),
             L(outline([(58, 18), (80, 30), (96, 56), (104, 102), (66, 106)]), 'shade', 'b', False),
             L(clipy(outline([(-4, 104), (-6, 80), (6, 50), (22, 26), (50, 16), (78, 26), (94, 50), (106, 80), (104, 104), (50, 108)]), 76, 120), 'deep', 'b', False)],
}

# Griffon Al-Qahir (Ghaddar Ghana): piel muy oscura, pelo rubio claro en llamas: pinchos altos arriba y dos largos a los
# lados, y un flequillo de mechones finos que le tapa la frente hasta los ojos; ojos rosas y sonrisa de dientes
CHARS['griffon-al-qahir'] = {
    'body': 'normal', 'pal': pal('#ead6a4', '#6a4430', iris='#c84488', shade='#c8a87c', deep='#a08060'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'hairline': [(14, 70), (24, 66), (50, 64), (76, 66), (86, 70)]},
    'front': [L(outline([(16, 70), (10, 58), (-6, 52, 1), (8, 44), (4, 30, 1), (16, 28), (18, 6, 1), (30, 16), (36, -6, 1), (44, 10), (50, 0), (56, 10), (64, -6, 1),
                         (70, 16), (82, 6, 1), (84, 28), (96, 30, 1), (92, 44), (106, 52, 1), (90, 58), (84, 70), (76, 60), (24, 60)])),
              L(outline([(56, 10), (64, -6), (70, 16), (82, 6), (84, 28), (96, 30), (92, 44), (106, 52), (88, 58), (76, 34)]), 'shade', 'b', False),
              L(outline([(46, 14), (50, 4), (54, 14), (50, 30)]), 'deep', 'b', False),
              L(outline([(16, 62), (20, 46), (34, 36), (50, 34), (66, 36), (80, 46), (84, 62), (78, 70, 1), (72, 60), (66, 72, 1), (60, 60), (54, 72, 1), (48, 60),
                         (42, 72, 1), (36, 60), (30, 72, 1), (24, 62), (20, 72, 1)]), 'mid', 'f', ln=True),
              strand([(36, 44), (40, 62)], 'shade', 'f', 1.0), strand([(50, 40), (52, 62)], 'shade', 'f', 1.0), strand([(64, 44), (62, 62)], 'shade', 'f', 1.0)],
    'side': [L(outline([(74, 66), (80, 52), (92, 50, 1), (84, 40), (92, 26, 1), (78, 24), (80, 6, 1), (64, 12), (56, -6, 1), (48, 10), (30, 0, 1), (32, 18), (12, 18, 1),
                        (20, 30), (-8, 44, 1), (12, 48), (4, 64, 1), (18, 64), (24, 80, 1), (34, 70), (42, 70), (44, 60), (56, 56), (66, 58)])),
             L(outline([(-8, 44), (12, 48), (4, 64), (18, 64), (24, 80), (34, 70), (42, 70), (44, 60), (26, 52), (14, 40)]), 'shade', 'b', False),
             L(outline([(70, 46), (84, 50), (86, 70, 1), (80, 60), (76, 72, 1), (70, 58)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(18, 70), (8, 60), (-6, 52, 1), (8, 44), (4, 30, 1), (16, 28), (18, 6, 1), (30, 16), (36, -6, 1), (44, 10), (50, -2, 1), (56, 10), (64, -6, 1),
                        (70, 16), (82, 6, 1), (84, 28), (96, 30, 1), (92, 44), (106, 52, 1), (92, 60), (82, 70), (78, 84), (60, 90), (50, 96, 1), (40, 90), (22, 84)])),
             L(outline([(56, 10), (64, -6), (70, 16), (82, 6), (84, 28), (96, 30), (92, 44), (106, 52), (92, 60), (82, 70), (78, 84), (60, 90), (62, 40)]), 'shade', 'b', False),
             L(outline([(44, 14), (50, 6), (56, 14), (50, 34)]), 'deep', 'b', False),
             strand([(30, 40), (40, 60)], 'deep', 'b', 1.2), strand([(70, 40), (60, 60)], 'deep', 'b', 1.2)],
}

# Shrike Al-Jazzar (Hisoka Masoka): cresta en cono muy alta granate oscuro con el borde de delante en dientes de sierra
# sobre la frente; los lados y la nuca rapados (gris violáceo); orejas grandes en punta, ojos verdes azulados con rayas
# negras que le bajan por las mejillas, sonrisa enorme de dientes y perilla fina
SHAVE = (106, 92, 110, 255)
CHARS['shrike-al-jazzar'] = {
    'body': 'normal', 'pal': pal('#7a2a26', '#b88058', iris='#2a9ab0', shade='#5e1e1c', deep='#461412', shave=SHAVE),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 91, 'big_ears': 2, 'ear_out': 2,
             'hairline': [(14, 56), (20, 44), (28, 52), (34, 42), (42, 50), (50, 40), (58, 50), (66, 42), (72, 52), (80, 44), (86, 56)]},
    'front': [L(DOME := blob([(16, 62), (13, 42), (22, 24), (50, 16), (78, 24), (87, 42), (84, 62)]), 'shave'),
              L(outline([(16, 52), (18, 30), (26, 20, 1), (50, -32, 1), (74, 20, 1), (82, 30), (84, 52), (78, 42), (72, 52), (66, 42), (58, 50), (50, 40),
                         (42, 50), (34, 42), (28, 52), (22, 42)])),
              L(outline([(52, 0), (50, -32), (74, 20), (82, 32), (84, 50), (72, 32)]), 'shade', 'b', False),
              L(outline([(26, 60), (44, 66, 1), (42, 70), (28, 66)]), 'mid', 'f', False), L(outline([(74, 60), (56, 66, 1), (58, 70), (72, 66)]), 'mid', 'f', False),
              L([(30, 80), (28, 92)], OUTC, 'f', False, False, 2.0), L([(34, 81), (34, 88)], OUTC, 'f', False, False, 1.4),
              L([(70, 80), (72, 92)], OUTC, 'f', False, False, 2.0), L([(66, 81), (66, 88)], OUTC, 'f', False, False, 1.4),
              L([(50, 96), (50, 104)], OUTC, 'f', False, False, 2.2)],
    'side': [L(blob([(44, 90), (22, 92), (14, 66), (16, 38), (34, 20), (60, 18), (80, 28), (86, 50), (64, 54)]), 'shave'),
             L(outline([(80, 46), (82, 30), (70, 18, 1), (44, -32, 1), (18, 14, 1), (8, 26), (8, 36), (30, 34), (50, 30), (66, 32), (74, 40)])),
             L(outline([(44, -32), (18, 14), (8, 26), (10, 34), (28, 30)]), 'shade', 'b', False),
             L([(70, 62), (84, 66)], 'mid', 'f', False, False, 2.4),
             L([(80, 80), (78, 90)], OUTC, 'f', False, False, 1.8), L([(84, 98), (84, 104)], OUTC, 'f', False, False, 2.0)],
    'back': [L(blob([(16, 66), (14, 40), (24, 22), (50, 16), (76, 22), (86, 40), (84, 66), (70, 90), (50, 96), (30, 90)]), 'skin'),
             L(blob([(16, 62), (14, 40), (24, 22), (50, 16), (76, 22), (86, 40), (84, 62), (70, 74), (50, 78), (30, 74)]), 'shave'),
             L(outline([(18, 32), (26, 20, 1), (50, -32, 1), (74, 20, 1), (82, 32), (50, 28)])),
             L(outline([(52, -26), (50, -32), (74, 20), (82, 32), (60, 30)]), 'shade', 'b', False)],
}

# Hawke Al-Bazzar (Hulk Laios): piel oscura, pelo corto en forma de huevo alto con franjas: negro arriba, dos rayas verdes
# y la parte de abajo rapada en gris; orejas grandes, ojos amarillo pálido entornados y boca de enfado
GREEN = (26, 160, 112, 255)
GRAY = (104, 110, 120, 255)
HAWK_EGG = blob([(15, 64), (14, 40), (22, 18), (36, 2), (50, -4), (64, 2), (78, 18), (86, 40), (85, 64)], 10)
HAWK_SIDE = blob([(70, 50), (80, 30), (72, 10), (56, -2), (40, -2), (22, 8), (10, 28), (6, 52), (10, 76), (22, 86), (40, 84), (44, 70), (42, 58), (54, 54)], 10)
HAWK_BACK = blob([(16, 84), (14, 44), (22, 18), (36, 2), (50, -4), (64, 2), (78, 18), (86, 44), (84, 84), (50, 88)], 10)


def bands(egg, y_cut):
    return [L(clipy(egg, -20, 12), 'mid', 'b', False), L(clipy(egg, 12, 19), GREEN, 'b', False), L(clipy(egg, 22, 32), GREEN, 'b', False),
            L(clipy(egg, y_cut, 120), GRAY, 'b', False)]


CHARS['hawke-al-bazzar'] = {
    'body': 'corpulento', 'pal': pal('#1e1e26', '#7a5640', shade='#14141a', deep='#0c0c10'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 3, 'ear_out': 3, 'hairline': (52, 50),
             'nose': (50, 84, 2.2)},
    'front': [L(HAWK_EGG), L(clipy(HAWK_EGG, -20, 13), 'mid', 'b', False), L(clipy(HAWK_EGG, 13, 21), GREEN, 'b', False),
              L(clipy(HAWK_EGG, 25, 80), GREEN, 'b', False), L(clipx(clipy(HAWK_EGG, 36, 80), -20, 22), GRAY, 'b', False), L(clipx(clipy(HAWK_EGG, 36, 80), 78, 120), GRAY, 'b', False)]
             + lids(36, 1, 75, (240, 232, 160, 255)) + lids(64, -1, 75, (240, 232, 160, 255))
             + [L([(26, 66), (44, 68)], OUTC, 'f', False, False, 2.0), L([(74, 66), (56, 68)], OUTC, 'f', False, False, 2.0)],
    'side': [L(HAWK_SIDE)] + [L(clipy(HAWK_SIDE, -20, 10), 'mid', 'b', False), L(clipy(HAWK_SIDE, 10, 17), GREEN, 'b', False),
                              L(clipy(HAWK_SIDE, 20, 30), GREEN, 'b', False), L(clipy(HAWK_SIDE, 30, 120), GRAY, 'b', False)]
            + [L([(76, 74), (86, 74)], (240, 232, 160, 255), 'f', False, False, 3.0), L([(74, 72), (87, 72)], OUTC, 'f', False, False, 2.2)],
    'back': [L(HAWK_BACK)] + bands(HAWK_BACK, 34) + [L(outline([(50, 34), (60, 60), (50, 84), (40, 60)]), (88, 94, 104, 255), 'b', False)],
}

# Robin Al-Ahmar (Silva Leol): pelo naranja rojizo abultado y ondulado como una boina sobre la cabeza; cejas naranjas
# gruesas, ojos grises grandes de susto y los dos dientes de delante
CHARS['robin-al-ahmar'] = {
    'body': 'bajito', 'pal': pal('#d2561e', '#b47a50', iris='#c4c8cc', shade='#a8401a', deep='#842e12'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'buck', 'mouth_y': 92, 'hairline': [(14, 62), (24, 54), (36, 56), (50, 52), (64, 56), (76, 54), (86, 62)]},
    'front': [L(curls(50, 30, (50, 34), 11, 0.2, 0.84)), L(outline([(10, 40), (16, 58), (18, 66), (24, 56), (36, 58), (50, 52), (64, 58), (76, 56), (82, 66), (84, 58),
                                                                  (90, 40), (50, 30)])),
              L(clipx(curls(50, 30, (50, 34), 11, 0.2, 0.84), 58, 120), 'shade', 'b', False),
              strand([(30, 14), (44, 22), (58, 14)], 'deep', 'b', 1.0), strand([(24, 34), (36, 40)], 'deep', 'b', 1.0), strand([(66, 32), (78, 40)], 'deep', 'b', 1.0),
              L(outline([(24, 62), (44, 64, 1), (44, 68), (26, 67)]), 'mid', 'f', False), L(outline([(76, 62), (56, 64, 1), (56, 68), (74, 67)]), 'mid', 'f', False)],
    'side': [L(curls(42, 34, (46, 36), 11, 0.2, 0.84)), L(outline([(70, 56), (78, 46), (60, 40), (40, 44), (18, 40), (8, 56), (12, 74), (24, 80), (36, 72), (44, 60), (56, 56)])),
             L(clipx(curls(42, 34, (46, 36), 11, 0.2, 0.84), -20, 26), 'shade', 'b', False),
             L(outline([(72, 61), (86, 63, 1), (86, 66), (73, 66)]), 'mid', 'f', False)],
    'back': [L(curls(50, 36, (50, 40), 11, 0.2, 0.84)), L(outline([(16, 50), (14, 70), (24, 84), (50, 88), (76, 84), (86, 70), (84, 50)])),
             L(clipx(curls(50, 36, (50, 40), 11, 0.2, 0.84), 60, 120), 'shade', 'b', False), strand([(34, 30), (50, 40), (64, 30)], 'deep', 'b', 1.0)],
}

# Condor (Condor Willy): piel morena, pelo negro largo y revuelto con un tupé de pinchos hacia arriba y las puntas de
# abajo que salen hacia fuera a la altura de la barbilla; ojos azul grisáceo con dos puntitos debajo
CHARS['condor'] = {
    'body': 'normal', 'pal': pal('#2c2828', '#aa7250', iris='#6a8aa4', shade='#1e1a1a', deep='#121010', light='#4a4444'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': [(14, 62), (24, 52), (36, 50), (44, 60), (50, 50), (64, 50), (76, 54), (86, 62)]},
    'front': [L(outline([(14, 100), (2, 104, 1), (8, 90), (8, 70), (2, 58, 1), (8, 48), (2, 20, 1), (14, 18), (16, 4, 1), (28, 10), (34, -18, 1), (44, 2), (52, 4),
                         (64, -2, 1), (66, 10), (84, 8, 1), (82, 22), (98, 22, 1), (88, 36), (94, 52, 1), (90, 60), (92, 78), (98, 98, 1), (86, 96), (84, 84), (80, 70),
                         (76, 56), (24, 56), (20, 70), (18, 86)])),
              L(outline([(52, 4), (64, -2), (66, 10), (84, 8), (82, 22), (98, 22), (88, 36), (94, 52), (90, 60), (92, 78), (98, 98), (86, 96), (84, 84), (80, 66),
                         (74, 34)]), 'shade', 'b', False),
              L(outline([(28, 48), (40, 44), (46, 64, 1), (50, 46), (60, 44), (66, 50), (72, 62, 1), (74, 46), (50, 38)]), 'mid', 'f', ln=True),
              L(outline([(20, 54), (28, 50), (22, 72, 1)]), 'mid', 'f', ln=True),
              L(ell(28, 84, 0.9, 0.9), OUTC, 'f', False), L(ell(31, 86, 0.9, 0.9), OUTC, 'f', False),
              L(ell(72, 84, 0.9, 0.9), OUTC, 'f', False), L(ell(69, 86, 0.9, 0.9), OUTC, 'f', False)],
    'side': [L(outline([(74, 58), (80, 46), (88, 38), (84, 28), (90, 18, 1), (76, 16), (80, -2, 1), (64, 6), (60, -22, 1), (48, 2), (30, -10, 1), (28, 8), (6, 2, 1),
                        (14, 20), (-10, 26, 1), (6, 38), (-10, 52, 1), (6, 58), (-2, 76, 1), (12, 76), (10, 96, 1), (24, 84), (30, 96, 1), (36, 80), (44, 62), (56, 56),
                        (64, 58)])),
             L(outline([(-10, 52), (6, 58), (-2, 76), (12, 76), (10, 96), (24, 84), (30, 96), (36, 80), (44, 62), (26, 54)]), 'shade', 'b', False),
             L(outline([(72, 50), (84, 52), (82, 70, 1)]), 'mid', 'f', ln=True),
             L(ell(80, 85, 0.9, 0.9), OUTC, 'f', False)],
    'back': [L(outline([(16, 96), (4, 100, 1), (10, 84), (6, 66), (0, 54, 1), (8, 44), (2, 18, 1), (16, 18), (18, 0, 1), (30, 8), (36, -18, 1), (48, 2), (60, 0),
                        (70, -12, 1), (72, 6), (90, 4, 1), (86, 20), (100, 24, 1), (92, 40), (98, 54, 1), (92, 64), (94, 84), (98, 100, 1), (84, 96), (70, 98), (62, 104),
                        (50, 96), (38, 104), (30, 98)])),
             L(outline([(60, 0), (70, -12), (72, 6), (90, 4), (86, 20), (100, 24), (92, 40), (98, 54), (92, 64), (94, 84), (98, 100), (84, 96), (70, 98), (66, 40)]),
               'shade', 'b', False)],
}

# Perry Al-Surah (Andreas Bebo): cabeza rapada (pelusa oscura) con una cresta ancha de mechones rosas abultados como
# una flor, y un mechón grande que le cae sobre la frente con rayas granates; orejas grandes, ojos azules y ceño fruncido
PINK = '#ea7c7a'
CHARS['perry-al-surah'] = {
    'body': 'normal', 'pal': pal(PINK, '#a26a44', iris='#3a6ab8', shade='#c45a5a', deep='#8e1e24', fuzz='#4a3028', fuzz_d='#3a241e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'big_ears': 2, 'ear_out': 2, 'hairline': (58, 52)},
    'front': [L(blob([(17, 60), (15, 42), (24, 24), (50, 18), (76, 24), (85, 42), (83, 60)]), 'fuzz'),
              L(curls(50, 20, (44, 20), 9, 0.3, 0.75)), L(clipx(curls(50, 20, (44, 20), 9, 0.3, 0.75), 60, 120), 'shade', 'b', False),
              L(outline([(36, 22), (50, 18), (62, 24), (60, 46), (52, 56, 1), (46, 44), (36, 36)]), 'mid', 'f', ln=True),
              strand([(42, 28), (50, 44)], 'deep', 'f', 2.0), strand([(48, 26), (54, 40)], 'deep', 'f', 1.6)],
    'side': [L(blob([(44, 90), (22, 92), (14, 66), (16, 38), (34, 20), (60, 18), (80, 28), (86, 50), (64, 54)]), 'fuzz'),
             L(curls(50, 18, (48, 18), 9, 0.2, 0.75)), L(clipx(curls(50, 18, (48, 18), 9, 0.2, 0.75), -20, 30), 'shade', 'b', False),
             L(curls(86, 34, (12, 14), 5), 'mid', 'f'), strand([(86, 26), (90, 40)], 'deep', 'f', 2.0)],
    'back': [L(blob([(16, 66), (14, 40), (24, 22), (50, 16), (76, 22), (86, 40), (84, 66), (70, 90), (50, 96), (30, 90)]), 'fuzz'),
             L(curls(50, 22, (44, 20), 9, 0.3, 0.75)), L(clipx(curls(50, 22, (44, 20), 9, 0.3, 0.75), 60, 120), 'shade', 'b', False),
             L(curls(50, 40, (16, 10), 5), 'mid', 'b')],
}

# Harris Al-Suhra (Pedro Amida) y Eagle Al-Suhra (Samir Amida), gemelos: pelo en pinchos revueltos (morado él, verde
# oliva su hermano), parche negro con tres tachuelas en un ojo (en lados contrarios), patillas largas y labios grises


def twin(hair, shade, deep, side):
    """side = 1: parche en el ojo de la izquierda de la imagen (Harris); -1: en el de la derecha (Eagle)."""
    px = 50 - 14 * side
    sx = 50 + 14 * side
    fr = [(24, 50), (34, 44), (40, 66, 1), (46, 48), (56, 46), (62, 60, 1), (66, 48), (78, 52), (50, 38)]
    if side < 0:
        fr = [(100 - x, y) + ((1,) if len(p) > 2 else ()) for p in fr for x, y in [p[:2]]]
    return {
        'body': 'normal', 'pal': pal(hair, '#fcdcc0', iris='#5a7a8e', shade=shade, deep=deep, lip='#8c8488'),
        'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 62), (24, 50), (40, 48), (50, 54), (60, 48), (76, 50), (86, 62)]},
        'front': [L(outline([(16, 66), (8, 50), (0, 40, 1), (8, 32), (0, 16, 1), (14, 12), (14, -4, 1), (28, 2), (34, -14, 1), (44, -2), (54, -12, 1), (60, 0),
                             (72, -6, 1), (74, 6), (90, 6, 1), (86, 18), (100, 26, 1), (90, 34), (98, 46, 1), (88, 50), (84, 66), (76, 56), (24, 56)])),
                  L(outline([(60, 0), (72, -6), (74, 6), (90, 6), (86, 18), (100, 26), (90, 34), (98, 46), (88, 52), (74, 30)]), 'shade', 'b', False),
                  strand([(30, 8), (36, 24), (32, 40)], 'deep', 'b', 1.0), strand([(56, 4), (62, 22), (70, 32)], 'deep', 'b', 1.0),
                  L(outline(fr), 'mid', 'f', ln=True),
                  L(outline([(16, 60), (22, 58), (20, 96, 1)]), 'mid', 'f'), L(outline([(84, 60), (78, 58), (80, 96, 1)]), 'mid', 'f')]
                 + patch(px, 76, 11, 8.5, 0.2 * side, strap_to=(sx + 12 * side, 58))
                 + [L(blob([(44, 93), (50, 91), (56, 93), (50, 97)], 4), 'lip', 'f', False), L([(44, 93), (56, 93)], OUTC, 'f', False, False, 1.0)],
        'side': [L(outline([(74, 58), (80, 46), (90, 42, 1), (82, 34), (94, 22, 1), (78, 18), (84, 2, 1), (66, 8), (64, -10, 1), (50, 4), (32, -8, 1), (30, 8), (8, 6, 1),
                            (16, 20), (-6, 28, 1), (8, 38), (-6, 50, 1), (8, 54), (0, 68, 1), (14, 68), (18, 84, 1), (28, 72), (38, 72), (44, 60), (56, 56), (64, 60)])),
                 L(outline([(-6, 50), (8, 54), (0, 68), (14, 68), (18, 84), (28, 72), (38, 72), (44, 60), (24, 52), (10, 40)]), 'shade', 'b', False),
                 strand([(58, 6), (66, 22), (78, 30)], 'deep', 'b', 1.0),
                 L(outline([(72, 50), (84, 52), (80, 68, 1)]), 'mid', 'f', ln=True), L(outline([(54, 62), (58, 60), (58, 92, 1)]), 'mid', 'f')]
                + ([L([(82, 70), (50, 62)], BLACK, 'f', False, False, 1.4), L(ell(84, 76, 5, 7.5), BLACK, 'f'),
                    L(ell(85, 72, 1.2, 1.2), WHITE, 'f', False), L(ell(85, 76, 1.2, 1.2), WHITE, 'f', False), L(ell(85, 80, 1.2, 1.2), WHITE, 'f', False)])
                + [L([(82, 93), (86, 92)], 'lip', 'f', False, False, 2.0)],
        'back': [L(outline([(18, 66), (6, 54, 1), (12, 44), (0, 32, 1), (14, 24), (8, 8, 1), (24, 10), (30, -6, 1), (42, 4), (52, -10, 1), (58, 4), (70, -6, 1), (72, 8),
                            (90, 6, 1), (86, 22), (100, 30, 1), (88, 40), (96, 54, 1), (84, 62), (82, 80), (50, 86), (18, 80)])),
                 L(outline([(58, 4), (70, -6), (72, 8), (90, 6), (86, 22), (100, 30), (88, 40), (96, 54), (84, 62), (82, 80), (62, 84), (62, 40)]), 'shade', 'b', False),
                 L(outline([(20, 60), (26, 60), (24, 96, 1)]), 'mid', 'b'), L(outline([(80, 60), (74, 60), (76, 96, 1)]), 'mid', 'b'),
                 L(quad((36, 34), (50, 30), (64, 34)), BLACK, 'b', False, False, 1.2)],
    }


CHARS['harris-al-suhra'] = twin('#7a5a8c', '#5e446e', '#46324f', 1)
CHARS['eagle-al-suhra'] = twin('#a8ba72', '#86945a', '#6a7444', -1)

# Anqa Qushchi (Eva Gordon, portera): pelo negro larguísimo por la espalda con raya en medio, dos plumas (azul y
# magenta) a un lado; ojos rojos con sombra azul y triangulitos rojos pintados en las mejillas
FEATHER_B = (32, 160, 210, 255)
FEATHER_M = (180, 32, 96, 255)


def feather(x0, y0, x1, y1, c, w=4.5):
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1
    nx, ny = -dy / n * w, dx / n * w
    return L(outline([(x0, y0, 1), (x0 + dx * 0.5 + nx, y0 + dy * 0.5 + ny), (x1, y1, 1), (x0 + dx * 0.5 - nx * 0.4, y0 + dy * 0.5 - ny * 0.4)]), c, 'f')


CHARS['anqa-qushchi'] = {
    'body': 'chica', 'pal': pal('#1c181a', '#fcd8b8', iris='#c82828', shade='#121012', deep='#0a080a', light='#3a3438'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': [(14, 76), (22, 58), (36, 50), (48, 48), (50, 54), (52, 48), (64, 50), (78, 58), (86, 76)]},
    'front': [L(outline([(-2, 124), (2, 90), (6, 56), (14, 28), (30, 12), (50, 8), (70, 12), (86, 28), (94, 56), (98, 90), (102, 124), (84, 124), (82, 96), (50, 96),
                         (18, 96), (16, 124)])),
              L(outline([(56, 10), (78, 20), (92, 50), (98, 90), (102, 124), (84, 124), (82, 96), (76, 60)]), 'shade', 'b', False),
              L(outline([(14, 58), (24, 54), (20, 84), (16, 110), (10, 90)]), 'mid', 'f'), L(outline([(86, 58), (76, 54), (80, 84), (84, 110), (90, 90)]), 'mid', 'f'),
              feather(80, 50, 96, 18, FEATHER_B), feather(80, 54, 104, 36, FEATHER_M),
              L(quad((26, 67), (36, 63), (46, 69)), (40, 160, 210, 255), 'f', False, False, 2.0), L(quad((74, 67), (64, 63), (54, 69)), (40, 160, 210, 255), 'f', False, False, 2.0),
              L([(26, 84), (30, 84), (28, 88)], RED, 'f', False), L([(74, 84), (70, 84), (72, 88)], RED, 'f', False),
              L([(30, 88), (33, 88), (31.5, 91)], RED, 'f', False), L([(70, 88), (67, 88), (68.5, 91)], RED, 'f', False)],
    'side': [L(outline([(74, 58), (82, 44), (82, 26), (66, 12), (44, 10), (22, 18), (8, 38), (0, 70), (-10, 110), (-16, 128), (40, 128), (40, 100), (44, 62), (56, 56),
                        (64, 58)])),
             L(outline([(8, 38), (0, 70), (-10, 110), (-16, 128), (10, 128), (14, 90), (20, 56)]), 'shade', 'b', False),
             L(outline([(74, 52), (84, 54), (90, 90), (88, 124), (80, 100)]), 'mid', 'f'),
             L([(76, 85), (79, 85), (77.5, 88)], RED, 'f', False)],
    'back': [L(outline([(-6, 124), (0, 90), (4, 56), (12, 30), (30, 14), (50, 10), (70, 14), (88, 30), (96, 56), (100, 90), (106, 124)])),
             L(outline([(56, 12), (80, 24), (94, 54), (100, 90), (106, 124), (66, 124), (66, 60)]), 'shade', 'b', False),
             feather(20, 50, 6, 18, FEATHER_B), feather(20, 54, -2, 36, FEATHER_M)],
}

# Roc Nasr (Flash Haniwa): hombre hecho y derecho; pelo castaño oscuro altísimo en forma de bulbo con la punta arriba,
# estrecho en las sienes; ojos verdes rasgados, arrugas en las mejillas, bigote de manillar y perilla larga
CHARS['roc-nasr'] = {
    'body': 'normal', 'pal': pal('#4c2618', '#e8a674', iris='#2a9a8a', shade='#3a1c12', deep='#2a140c', stache='#5a2e1a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'big_ears': 2, 'ear_out': 2, 'hairline': [(22, 62), (28, 54), (50, 52), (72, 54), (78, 62)],
             'nose': (50, 84, 2.4)},
    'front': [L(outline([(24, 64), (22, 56), (6, 48), (2, 32), (14, 16), (32, 8), (50, -10, 1), (68, 8), (86, 16), (98, 32), (94, 48), (78, 56), (76, 64), (70, 56),
                         (30, 56)])),
              L(outline([(50, -10), (68, 8), (86, 16), (98, 32), (94, 48), (78, 56), (70, 30), (56, 10)]), 'shade', 'b', False),
              L(outline([(50, 88), (38, 89), (28, 94), (22, 90, 1), (30, 86), (42, 85)]), 'stache', 'f'),
              L(outline([(50, 88), (62, 89), (72, 94), (78, 90, 1), (70, 86), (58, 85)]), 'stache', 'f'),
              L(outline([(47, 97), (53, 97), (51, 110, 1), (49, 110, 1)]), 'stache', 'f'),
              L([(30, 84), (34, 92)], 'skin_d', 'f', False, False, 1.0), L([(70, 84), (66, 92)], 'skin_d', 'f', False, False, 1.0)],
    'side': [L(outline([(76, 56), (86, 48), (96, 34), (92, 18), (74, 6), (54, -10, 1), (30, 4), (10, 18), (0, 36), (8, 56), (26, 66), (40, 70), (46, 58), (60, 54)])),
             L(outline([(0, 36), (8, 56), (26, 66), (40, 70), (46, 58), (28, 50), (12, 34)]), 'shade', 'b', False),
             L(outline([(52, 60), (56, 58), (56, 76), (52, 76)]), 'mid', 'f', False),
             L(outline([(86, 88), (78, 90), (70, 92, 1), (78, 86)]), 'stache', 'f'), L(outline([(82, 97), (86, 97), (84, 110, 1)]), 'stache', 'f')],
    'back': [L(outline([(26, 72), (22, 56), (6, 48), (2, 32), (14, 16), (32, 8), (50, -10, 1), (68, 8), (86, 16), (98, 32), (94, 48), (78, 56), (74, 72), (50, 78)])),
             L(outline([(50, -10), (68, 8), (86, 16), (98, 32), (94, 48), (78, 56), (74, 72), (56, 76), (62, 30)]), 'shade', 'b', False)],
}
