"""Ojeadores de IE1 (scouts-ie1), tanda 08 (de matt-matickal a pascal-blaise): dibujados a partir de su retrato de Victory
Road (ninguno tiene modelo 3D en la enciclopedia); claves 'scouts-ie1:<id>'. Todos chicos según la wiki."""
import math

from chars import CHARS, L, OUTC, blob, ell, messy, longhair, outline, pal, rope, strand  # noqa: F401
from chars_vr_keizen_arashiyama import cloud, lashes
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
DARK = (44, 36, 36, 255)


def fr(pts, c='mid'):
    """Mechones de delante de la cara (encima de los ojos)."""
    return L(outline(pts), c, 'f')


def spikes_side(x, y, s=1, n=2, c='mid'):
    """Puntas que salen por detrás de la oreja (s=1 izquierda de la imagen, -1 derecha)."""
    out = []
    for i in range(n):
        yy = y + i * 9
        out.append(L(outline([(x, yy - 6), (x - s * 12, yy + 2, 1), (x, yy + 4)]), c))
    return out


def bowl(view, lo=52, w=8, top=0, c='mid', lines=True):
    """Corte de tazón (champiñón): ala recta y ancha a la altura lo."""
    if view == 'front':
        out = [L(outline([(-w + 6, lo), (-w + 8, 30), (14, 8 + top), (50, top), (86, 8 + top), (108 - w, 30), (106 - w, lo, 1), (50, lo + 2), (-w + 6, lo, 1)]), c),
               L(outline([(60, top + 2), (88, 10 + top), (106 - w, 34), (104 - w, lo - 2), (74, lo - 2)]), 'shade', 'b', False)]
        if lines:
            out += [strand([(x, top + 10 + abs(50 - x) * 0.2), (x + (x - 50) * 0.12, lo - 4)], 'deep', 'b', 0.9) for x in (24, 38, 50, 62, 76)]
        return out
    if view == 'side':
        return [L(outline([(98, lo), (92, 26), (70, 2 + top), (40, top), (12, 14 + top), (0, 40), (2, lo + 4, 1), (24, lo + 6), (60, lo + 2)]), c),
                L(outline([(4, 44), (10, 78), (28, 84), (40, 64), (30, 56)]), 'shade', 'b', False)]
    return [L(outline([(-w + 6, lo + 2), (-w + 8, 30), (14, 8 + top), (50, top), (86, 8 + top), (108 - w, 30), (106 - w, lo + 2, 1), (50, lo + 6), (-w + 6, lo + 2, 1)]), c),
            L(outline([(22, lo), (24, 78), (50, 84), (76, 78), (78, lo)]), 'shade', 'b', False),
            L(outline([(58, top + 2), (88, 10 + top), (106 - w, 34), (104 - w, lo), (70, lo + 2)]), 'shade', 'b', False)]


def flip_sides(view, y=96, c='mid'):
    """Puntas de la melena que se doblan hacia fuera a la altura de la barbilla."""
    if view == 'front':
        return [L(outline([(14, y - 22), (10, y - 4), (-2, y + 2, 1), (8, y + 4), (18, y - 6)]), c),
                L(outline([(86, y - 22), (90, y - 4), (102, y + 2, 1), (92, y + 4), (82, y - 6)]), c)]
    if view == 'side':
        return [L(outline([(20, y - 26), (14, y - 6), (2, y + 2, 1), (16, y + 2), (30, y - 10)]), c)]
    return [L(outline([(14, y - 22), (10, y - 4), (-2, y + 2, 1), (10, y + 4), (30, y - 2), (50, y), (70, y - 2), (90, y + 4), (102, y + 2, 1), (90, y - 4), (86, y - 22)]), c)]


# Matt Matickal (portero): pelo naranja con un flequillo enorme peinado hacia la izquierda de la imagen que acaba en punta
# junto a la mejilla, y puntas sueltas detrás de las orejas; gafas rectangulares oscuras, ojos afilados y sonrisa de dientes
CHARS[K + 'matt-matickal'] = {
    'body': 'normal', 'pal': pal('#e8862a', '#f8cc9a', iris='#5a6a3a', shade='#c06a1e', deep='#8e4a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'glasses': (52, 60, 44, 255), 'glasses_rect': True,
             'hairline': [(14, 66), (16, 50), (30, 44), (50, 46), (70, 44), (84, 50), (86, 66)]},
    'front': crop('front', top=4, side=66, w=3) + spikes_side(16, 74, 1, 2) + spikes_side(84, 74, -1, 2)
             + [fr([(88, 30), (64, 22), (36, 28), (16, 40), (2, 62, 1), (16, 52), (28, 54), (40, 50), (56, 52), (70, 46), (84, 50)]),
                strand([(70, 28), (40, 36), (20, 52)], 'shade', 'f', 1.0)],
    'side': crop('side', top=2, nape=84, w=2) + [fr([(62, 40), (78, 20), (94, 34), (100, 58, 1), (86, 48), (72, 50)]),
                                                 L(outline([(16, 80), (2, 92, 1), (22, 86)]))],
    'back': crop('back', top=4, nape=86, w=3) + spikes_side(16, 70, 1, 2) + spikes_side(84, 70, -1, 2),
}

# Matt Tudor: piel morena y pelo rojo teja corto y revuelto, con un mechón de punta arriba; cejas naranjas fruncidas
CHARS[K + 'matt-tudor'] = {
    'body': 'normal', 'pal': pal('#b4461c', '#c8885a', iris='#2a2020', shade='#8e3414', deep='#6a240c'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 92, 'hairline': [(14, 64), (18, 50), (30, 52), (40, 44), (50, 52), (60, 44), (72, 52), (84, 50), (86, 64)]},
    'front': messy('front', amp=7, n=10, seed=21, lo=60, rx=44, ry=38) + [L(outline([(48, 6), (54, -10, 1), (60, 6)])),
                                                                         fr([(20, 50), (30, 40), (40, 54, 1), (46, 40), (54, 54, 1), (60, 40), (70, 54, 1), (80, 44), (82, 52)])],
    'side': messy('side', amp=7, n=9, seed=21, nape=82) + [L(outline([(48, 2), (56, -12, 1), (62, 4)]))],
    'back': messy('back', amp=7, n=10, seed=21, nape=84),
}

# Matthew Pencil: corte de tazón verde oliva, como una seta, con el ala recta y ancha a media frente; cejas gruesas verdes,
# nariz grande, ojos pequeños y boca ondulada
CHARS[K + 'matthew-pencil'] = {
    'body': 'normal', 'pal': pal('#6a9a3c', '#f4c08a', iris='#2a2020', shade='#527a2c', deep='#3a5a1e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 4.6), 'hairline': [(10, 52), (90, 52)]},
    'front': bowl('front', lo=52, w=10) + brows(62, 'mid', 4.5, 15, -1.0, 13)
             + [L(quad((40, 96), (45, 99), (50, 95)) + quad((50, 95), (55, 99), (60, 96))[1:], OUTC, 'f', False, False, 1.4)],
    'side': bowl('side', lo=52) + brow_side(62, 'mid', 4.5),
    'back': bowl('back', lo=52, w=10),
}

# Max Bright: pelo verde largo peinado hacia atrás con raya, que cae por los lados y se dobla hacia fuera a la altura de la
# barbilla; cara larga, ojos entornados, nariz larga y media sonrisa con un colmillo
CHARS[K + 'max-bright'] = {
    'body': 'delgado', 'pal': pal('#4a9a5c', '#f2c48a', iris='#2a2020', shade='#3a7a48', deep='#2a5a34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 86, 3.0),
             'hairline': [(14, 70), (17, 50), (30, 36), (48, 30), (70, 36), (83, 50), (86, 70)]},
    'front': longhair('front', length=92, flare=4, top=2) + flip_sides('front', 96) + [strand([(44, 4), (40, 30)], 'deep', 'b', 1.2),
                                                                                       L([(54, 95), (55, 98)], WHITE, 'f', False, False, 1.4)],
    'side': longhair('side', length=92, flare=2, top=2) + flip_sides('side', 96),
    'back': longhair('back', length=92, flare=4, top=2, ends=0) + flip_sides('back', 96),
}

# Max Hurt (portero): pelo morado oscuro corto, con puntas que se abren hacia fuera a los lados, por encima de las orejas;
# piel tostada, ceño fruncido y boca seria
CHARS[K + 'max-hurt'] = {
    'body': 'normal', 'pal': pal('#5a4a7a', '#eab274', iris='#2a2020', shade='#463a60', deep='#302848'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 62), (18, 50), (30, 46), (40, 52), (50, 44), (62, 52), (72, 46), (84, 50), (86, 62)]},
    'front': crop('front', top=6, side=62, w=4) + [L(outline([(16, 46), (2, 50, 1), (12, 58), (0, 66, 1), (16, 64)])),
                                                   L(outline([(84, 46), (98, 50, 1), (88, 58), (100, 66, 1), (84, 64)])),
                                                   L(outline([(30, 10), (34, -2, 1), (42, 8), (54, -2, 1), (60, 8), (72, 2, 1), (74, 14)]))],
    'side': crop('side', top=4, nape=80, w=3) + [L(outline([(10, 40), (-6, 44, 1), (6, 54), (-4, 64, 1), (12, 66)])),
                                                 L(outline([(40, 6), (46, -6, 1), (56, 4), (66, -2, 1), (70, 8)]))],
    'back': crop('back', top=6, nape=82, w=4) + [L(outline([(16, 46), (2, 50, 1), (12, 58), (0, 66, 1), (16, 64)])),
                                                 L(outline([(84, 46), (98, 50, 1), (88, 58), (100, 66, 1), (84, 64)]))],
}

# Max Scara (portero): melena lisa verde menta muy clara, casi blanca, con un flequillo enorme que le tapa el ojo derecho y
# un mechón de punta a un lado; piel pálida, pestañas largas y labios azul oscuro
CHARS[K + 'max-scara'] = {
    'body': 'delgado', 'pal': pal('#cdeee2', '#efdcc6', iris='#2a2a34', shade='#a8b0b0', deep='#8a9494', lip='#2c3a52'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': longhair('front', length=94, flare=2, top=0) + [L(outline([(14, 34), (-4, 30, 1), (8, 46)])),
                                                              fr([(30, 20), (50, 12), (76, 18), (92, 40), (92, 84), (84, 96, 1), (72, 80), (60, 84, 1), (52, 62), (46, 46), (36, 40), (22, 44)])]
             + lashes(75, 14, 7) + [L(ell(50, 95, 4.2, 2.2), 'lip', 'f', False)],
    'side': longhair('side', length=94, flare=0, top=0) + [fr([(60, 30), (84, 20), (96, 40), (94, 84), (86, 92, 1), (82, 74), (74, 60)])],
    'back': longhair('back', length=94, flare=2, top=0, ends=3) + [L(outline([(14, 34), (-4, 30, 1), (8, 46)]))],
}

# Mel Lowe: cara ancha y mofletuda; pelo verde oscuro en ondas: un casquete con pico en el centro de la frente y dos matas
# de rizos a los lados hasta la barbilla; ojos entornados, nariz gorda y labios gruesos
WIDE = blob([(12, 52), (50, 42), (88, 52), (96, 76), (90, 100), (68, 112), (50, 114), (32, 112), (10, 100), (4, 76)])
CHARS[K + 'mel-lowe'] = {
    'body': 'corpulento', 'pal': pal('#2a7a5c', '#f2b474', iris='#2a2020', shade='#1e5e46', deep='#164634', lip='#8a4a2a'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 86, 5.4), 'face_front': WIDE, 'ear_out': 8, 'eye_y': 76,
             'hairline': [(10, 66), (16, 52), (30, 50), (44, 58), (50, 64), (56, 58), (70, 50), (84, 52), (90, 66)]},
    'front': [L(cloud(8, 86, 14, 22, 6, 0.3)), L(cloud(92, 86, 14, 22, 6, 0.6)),
              L(outline([(6, 70), (8, 40), (22, 16), (50, 8), (78, 16), (92, 40), (94, 70), (80, 56), (20, 56)])),
              L(outline([(60, 10), (84, 22), (94, 46), (92, 70), (80, 44)]), 'shade', 'b', False),
              L(ell(50, 100, 9, 5), 'lip', 'f', False), L([(42, 100), (58, 100)], OUTC, 'f', False, False, 1.2)],
    'side': [L(cloud(24, 84, 22, 22, 7)), L(outline([(70, 52), (84, 40), (88, 22), (66, 6), (36, 6), (12, 20), (2, 44), (8, 70), (40, 64), (56, 56)])),
             L(cloud(10, 60, 12, 18, 5), 'shade', 'b', False)],
    'back': [L(cloud(50, 80, 46, 28, 9)), L(outline([(6, 70), (8, 40), (22, 16), (50, 8), (78, 16), (92, 40), (94, 70), (50, 76)])),
             L(outline([(58, 10), (84, 22), (94, 50), (90, 92), (62, 96)]), 'shade', 'b', False)],
}

# Michael Angeloni (portero): una mata enorme de pelo rizado verde oliva con remolinos, que le abulta por encima y a los lados;
# cara ancha, cejas fruncidas, nariz de cerdito y sonrisa pequeña
CHARS[K + 'michael-angeloni'] = {
    'body': 'corpulento', 'pal': pal('#6e5e2a', '#f0b880', iris='#2a2020', shade='#54461e', deep='#3c3214'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 87, 4.2), 'face_front': WIDE, 'ear_out': 8,
             'hairline': [(10, 66), (14, 54), (30, 52), (50, 56), (70, 52), (86, 54), (90, 66)]},
    'front': [L(cloud(50, 30, 58, 40, 10, 0.2)), L(cloud(8, 64, 14, 18, 5)), L(cloud(92, 64, 14, 18, 5, 0.4)),
              L(outline([(62, -4), (98, 20), (104, 56), (94, 70), (84, 40)]), 'shade', 'b', False),
              strand([(30, 20), (36, 14), (40, 22), (34, 26)], 'deep', 'b', 1.0), strand([(64, 26), (70, 20), (74, 28)], 'deep', 'b', 1.0),
              L(ell(46, 87, 1, 1.4), OUTC, 'f', False), L(ell(54, 87, 1, 1.4), OUTC, 'f', False)],
    'side': [L(cloud(44, 34, 54, 40, 10)), L(cloud(18, 70, 18, 18, 5)), L(cloud(70, 50, 14, 12, 5), 'mid', 'b', False),
             L(cloud(18, 70, 12, 12, 4), 'shade', 'b', False)],
    'back': [L(cloud(50, 40, 58, 46, 11, 0.2)), L(cloud(50, 80, 36, 14, 6), 'shade', 'b', False)],
}


def whiskers(y=88, c=OUTC, w=1.0):
    """Tres rayas en cada mejilla (bigotes de gato)."""
    out = []
    for dy in (-4, 0, 4):
        out += [L([(14, y + dy - 2), (28, y + dy)], c, 'f', False, False, w), L([(86, y + dy - 2), (72, y + dy)], c, 'f', False, False, w)]
    return out


# Mick Thatcher (portero): pelo rubio dorado ondulado y abultado, con un tupé que se riza hacia un lado; ojos azules, ceño
# fruncido y boca apretada
CHARS[K + 'mick-thatcher'] = {
    'body': 'normal', 'pal': pal('#e8c236', '#fcd8b4', iris='#5a8ab0', shade='#c49a22', deep='#9a7414'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 62), (16, 48), (30, 46), (46, 50), (60, 44), (76, 46), (86, 50), (88, 62)]},
    'front': [L(outline([(16, 64), (6, 44), (10, 20), (26, 4), (46, -2), (66, 0), (84, 8), (94, 26), (92, 48), (84, 64), (80, 50), (20, 50)])),
              L(outline([(60, 2), (86, 12), (94, 30), (90, 52), (78, 34)]), 'shade', 'b', False),
              fr([(18, 48), (24, 34), (40, 26), (56, 28), (66, 38), (60, 46), (48, 40), (34, 40), (24, 50)]),
              strand([(30, 14), (46, 10), (60, 18)], 'shade', 'b', 1.2), strand([(70, 20), (80, 34)], 'shade', 'b', 1.0)],
    'side': [L(outline([(66, 50), (82, 40), (94, 26), (86, 6), (62, -4), (36, -2), (14, 8), (2, 30), (2, 56), (12, 78), (30, 86), (40, 64), (52, 56)])),
             L(outline([(4, 42), (28, 46), (38, 64), (28, 84), (12, 76)]), 'shade', 'b', False), strand([(40, 4), (60, 10), (78, 24)], 'shade', 'b', 1.2)],
    'back': [L(outline([(14, 78), (6, 46), (10, 20), (28, 4), (50, -2), (72, 4), (90, 20), (94, 46), (86, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 4), (86, 18), (94, 50), (86, 78), (62, 86)]), 'shade', 'b', False), strand([(30, 20), (40, 40), (36, 60)], 'shade', 'b', 1.0)],
}

# Mike Chequer (portero): melena rubia lisa con raya a un lado que le cae hasta la mandíbula; una nariz postiza naranja en
# triángulo, ojos afilados y sonrisa de pillo
CHARS[K + 'mike-chequer'] = {
    'body': 'normal', 'pal': pal('#dca82a', '#f2b47a', iris='#3a4a7a', shade='#b4861c', deep='#8a6410', nose='#f08a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': longhair('front', length=98, flare=0, top=8) + [fr([(14, 60), (16, 34), (34, 18), (56, 16), (78, 22), (88, 40), (88, 66), (80, 50), (66, 46), (50, 52), (38, 46), (26, 54)]),
                                                              strand([(56, 18), (50, 40)], 'deep', 'f', 1.0),
                                                              L(outline([(45, 84), (55, 84), (50, 92, 1)]), 'nose', 'f', ln=True)],
    'side': longhair('side', length=98, flare=0, top=8) + [fr([(64, 30), (86, 30), (92, 50), (90, 64, 1), (80, 50)]),
                                                            L(outline([(86, 84), (96, 88, 1), (86, 92)]), 'nose', 'f', ln=True)],
    'back': longhair('back', length=98, flare=0, top=8, ends=3),
}

# Mike Creasey-Creasewell: pelo castaño peinado hacia atrás, pegado, con un pico en V muy marcado en el centro de la frente;
# cara alargada, cejas finas y una sonrisa ancha
CHARS[K + 'mike-creasey-creasewell'] = {
    'body': 'delgado', 'pal': pal('#6e5e3e', '#f2b474', iris='#2a2020', shade='#54462e', deep='#3c3220'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 3.0),
             'hairline': [(14, 64), (17, 46), (28, 36), (40, 34), (50, 50), (60, 34), (72, 36), (83, 46), (86, 64)]},
    'front': crop('front', top=0, side=64, w=0) + [strand([(34, 10), (30, 30)], 'deep', 'b', 1.0), strand([(66, 10), (70, 30)], 'deep', 'b', 1.0)],
    'side': crop('side', top=0, nape=82) + [strand([(80, 20), (50, 10), (20, 20)], 'deep', 'b', 1.0)],
    'back': crop('back', top=0, nape=82) + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.0)],
}

# Miles Ryan: melena rubia larga y ondulada hasta el pecho, con mechones sueltos sobre la frente; piel morena y ojos verdes
CHARS[K + 'miles-ryan'] = {
    'body': 'delgado', 'pal': pal('#eccc72', '#b8804e', iris='#4a8a5a', shade='#c8a450', deep='#9a7a34'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': longhair('front', length=118, flare=8, top=0, ends=5) + [fr([(12, 64), (14, 36), (30, 18), (50, 14), (70, 18), (86, 36), (88, 64), (82, 56), (76, 44), (70, 60, 1),
                                                                        (64, 44), (56, 58, 1), (50, 44), (42, 60, 1), (36, 44), (28, 58, 1), (22, 46)]),
                                                                    strand([(10, 70), (6, 90), (10, 108)], 'shade', 'b', 1.0), strand([(90, 70), (94, 90), (90, 108)], 'shade', 'b', 1.0)],
    'side': longhair('side', length=118, flare=6, top=0) + [fr([(66, 30), (88, 34), (94, 54), (90, 66, 1), (82, 52)])],
    'back': longhair('back', length=118, flare=8, top=0, ends=5) + [strand([(30, 30), (26, 70), (30, 110)], 'shade', 'b', 1.0), strand([(70, 30), (74, 70), (70, 110)], 'shade', 'b', 1.0)],
}

# Miles Seaford: pelo morado con dos puntas como cuernos en lo alto y un mechón en V que baja por la frente; maquillaje de
# payaso: rombos turquesa en los ojos, nariz roja y labios gruesos
TEAL = (110, 196, 190, 255)
CHARS[K + 'miles-seaford'] = {
    'body': 'normal', 'pal': pal('#6c5c8c', '#f4bc84', iris='#3a6a6a', shade='#544670', deep='#3c3254', lip='#d8606a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': [(12, 70), (16, 52), (30, 44), (44, 50), (50, 64), (56, 50), (70, 44), (84, 52), (88, 70)]},
    'front': [L(outline([(12, 76), (6, 46), (14, 22), (30, 10), (26, -6, 1), (42, 8), (58, 8), (74, -6, 1), (70, 10), (86, 22), (94, 46), (88, 76), (82, 56), (18, 56)])),
              L(outline([(58, 10), (84, 22), (94, 48), (88, 74), (80, 44)]), 'shade', 'b', False)]
             + [L([(cx, 64), (cx + 9, 75), (cx, 87), (cx - 9, 75), (cx, 64)], TEAL, 'f', False, False, 2.4) for cx in (36, 64)]
             + [fr([(40, 46), (50, 66, 1), (60, 46)])]
             + [L(ell(50, 87, 3.4, 3.0), (220, 70, 60, 255), 'f', False), L(ell(50, 97, 9, 4.2), 'lip', 'f', ln=True), L([(42, 97), (58, 97)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(66, 52), (82, 40), (90, 24), (76, 8), (66, -8, 1), (56, 6), (34, 4), (14, 14), (2, 40), (6, 70), (20, 84), (36, 80), (44, 62), (56, 56)])),
             L(outline([(4, 40), (28, 46), (40, 62), (32, 80), (14, 76)]), 'shade', 'b', False),
             L([(80, 64), (88, 75), (82, 87)], TEAL, 'f', False, False, 2.4)],
    'back': [L(outline([(12, 80), (6, 46), (14, 22), (30, 10), (26, -6, 1), (42, 8), (58, 8), (74, -6, 1), (70, 10), (86, 22), (94, 46), (88, 80), (50, 86)])),
             L(outline([(58, 10), (84, 22), (94, 50), (88, 80), (62, 86)]), 'shade', 'b', False)],
}

# Mitch Hett: pelo verde azulado con un flequillo grande en diagonal que le cruza la frente y una raya marcada; ojos grandes
# y redondos y sonrisa
CHARS[K + 'mitch-hett'] = {
    'body': 'normal', 'pal': pal('#5a9a92', '#f6c494', iris='#2a2020', shade='#467a74', deep='#325a56'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': crop('front', top=2, side=70, w=4) + [fr([(16, 66), (14, 40), (26, 18), (44, 10), (66, 12), (84, 26), (88, 50), (86, 66), (78, 50), (72, 64, 1), (62, 46), (52, 40),
                                                       (40, 50), (30, 54), (24, 62)]), strand([(44, 12), (40, 44)], 'deep', 'f', 1.2)],
    'side': crop('side', top=0, nape=84, w=3) + [fr([(62, 40), (80, 16), (94, 36), (90, 60, 1), (80, 46)])],
    'back': crop('back', top=2, nape=86, w=4),
}

# Mo Eisner (portero): pelo verde oliva con raya en medio, recogido en dos moños bajos junto a las orejas con gomas rojas;
# cejas muy gruesas, ojos de punto, nariz redonda y boca torcida hacia abajo
CHARS[K + 'mo-eisner'] = {
    'body': 'normal', 'pal': pal('#5e5a2c', '#f6c08a', iris='#2a2020', shade='#48441e', deep='#322e14', band='#c8302a'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 3.4),
             'hairline': [(14, 64), (17, 50), (30, 40), (50, 36), (70, 40), (83, 50), (86, 64)]},
    'front': [L(cloud(6, 72, 12, 16, 5, 0.3)), L(cloud(94, 72, 12, 16, 5, 0.5))] + crop('front', top=2, side=66, w=2)
             + [strand([(50, 4), (50, 30)], 'deep', 'b', 1.2), L([(16, 66), (18, 74)], 'band', 'f', False, False, 3.0), L([(84, 66), (82, 74)], 'band', 'f', False, False, 3.0)]
             + brows(64, (60, 54, 30, 255), 5.0, 15, -1.0, 15),
    'side': crop('side', top=0, nape=80, w=2) + [L(cloud(24, 82, 12, 14, 5)), L([(30, 74), (34, 82)], 'band', 'f', False, False, 3.0)] + brow_side(64, (60, 54, 30, 255), 5.0),
    'back': [L(cloud(8, 72, 12, 16, 5, 0.3)), L(cloud(92, 72, 12, 16, 5, 0.5))] + crop('back', top=2, nape=82, w=2)
            + [strand([(50, 4), (50, 70)], 'deep', 'b', 1.0), L([(16, 66), (18, 74)], 'band', 'f', False, False, 3.0), L([(84, 66), (82, 74)], 'band', 'f', False, False, 3.0)],
}

# Mo Hawkes: grandullón de piel oscura y cara ancha, con el pelo verde oscuro corto y plano arriba; ojos blancos afilados,
# rayas de bigote de gato en las mejillas y sonrisa de lado
CHARS[K + 'mo-hawkes'] = {
    'body': 'corpulento', 'pal': pal('#2a6a4c', '#9a6e50', iris='#f4f4f4', shade='#1e523a', deep='#143a28'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE, 'ear_out': 8,
             'hairline': [(10, 60), (14, 46), (30, 40), (50, 38), (70, 40), (86, 46), (90, 60)]},
    'front': crop('front', top=12, side=60, w=6, flat=12) + whiskers(88, (60, 36, 26, 255), 1.2),
    'side': crop('side', top=10, nape=78, w=4, flat=12) + [L([(70, 88), (84, 86)], (60, 36, 26, 255), 'f', False, False, 1.2)],
    'back': crop('back', top=12, nape=78, w=6, flat=12),
}


def lens_glasses(view, y=78, c=(40, 36, 50, 255), lens=(238, 226, 196, 255), r=10.5, sep=15):
    """Gafas redondas grandes con el cristal opaco (no se le ven los ojos)."""
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            out += [L(ell(cx, y, r, r * 0.9), lens, 'f', False), L(ell(cx, y, r, r * 0.9) + [ell(cx, y, r, r * 0.9)[0]], c, 'f', False, False, 1.8)]
        return out + [L([(50 - sep + r, y - 1), (50 + sep - r, y - 1)], c, 'f', False, False, 1.6)]
    return [L(ell(84, y, 4, r * 0.9), lens, 'f', False), L([(84, y - r * 0.9), (88, y), (84, y + r * 0.9)], c, 'f', False, False, 1.6),
            L([(82, y - 2), (52, y - 6)], c, 'f', False, False, 1.6)]


# Mo Lusk: grandullón de piel tostada y cara ancha, con el pelo rubio pálido rapado al cero; cejas claras, ojos pequeños
# y labios gruesos
CHARS[K + 'mo-lusk'] = {
    'body': 'corpulento', 'pal': pal('#eedcb4', '#c48a52', iris='#2a2020', shade='#d4c094', deep='#b4a074', lip='#8a4a2e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'ear_out': 8, 'nose': (50, 86, 3.6),
             'hairline': [(10, 50), (16, 40), (30, 30), (50, 28), (70, 30), (84, 40), (90, 50)]},
    'front': crop('front', top=12, side=48, w=0, flat=10, shade=False) + brows(66, (236, 220, 190, 255), 3.0, 15, -1.0, 12)
             + [L(ell(50, 99, 10, 5), 'lip', 'f', ln=True), L([(41, 99), (59, 99)], OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=10, nape=76, flat=10, shade=False),
    'back': crop('back', top=12, nape=76, flat=10, shade=False),
}

# Mo Zarella: pelo castaño verdoso peinado hacia atrás, pegado arriba y con dos matas rizadas que abultan a los lados; cejas
# negras enormes, nariz grande, boca ancha de labios gruesos y piel tostada
CHARS[K + 'mo-zarella'] = {
    'body': 'corpulento', 'pal': pal('#8a7a46', '#c8945a', iris='#2a2020', shade='#6c5e34', deep='#4e4424', lip='#8a4a2e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'ear_out': 8, 'nose': (50, 88, 5.0),
             'hairline': [(10, 62), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (90, 62)]},
    'front': [L(cloud(6, 74, 12, 16, 5, 0.2)), L(cloud(94, 74, 12, 16, 5, 0.6))] + crop('front', top=4, side=64, w=2)
             + [strand([(40, 6), (36, 30)], 'deep', 'b', 1.0), strand([(60, 6), (64, 30)], 'deep', 'b', 1.0)]
             + brows(66, DARK, 5.5, 15, 2.0, 15) + [L(ell(50, 101, 12, 4.6), 'lip', 'f', ln=True), L([(40, 101), (60, 101)], OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=2, nape=80, w=2) + [L(cloud(22, 78, 14, 16, 5)), strand([(80, 24), (50, 10), (20, 22)], 'deep', 'b', 1.0)] + brow_side(66, DARK, 5.5, 2.0),
    'back': [L(cloud(8, 74, 12, 16, 5, 0.2)), L(cloud(92, 74, 12, 16, 5, 0.6))] + crop('back', top=4, nape=82, w=2),
}

# Monty Burrows (portero): pelo azul marino corto a los lados y levantado en un tupé que acaba en una punta larga hacia la
# derecha de la imagen; ojos entornados, cejas azules, nariz redonda y sonrisa
CHARS[K + 'monty-burrows'] = {
    'body': 'normal', 'pal': pal('#2c4c6c', '#f6be88', iris='#2a2020', shade='#203a54', deep='#16283c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 3.2),
             'hairline': [(14, 62), (16, 46), (30, 40), (50, 38), (70, 38), (84, 44), (86, 62)]},
    'front': crop('front', top=6, side=62, w=0) + [L(outline([(14, 40), (20, 14), (40, 2), (64, -2), (86, -10), (102, -14, 1), (94, 4), (88, 20), (86, 40), (60, 30), (30, 34)])),
                                                   strand([(30, 20), (60, 6), (92, -8)], 'shade', 'b', 1.2)] + brows(66, 'shade', 3.2, 15, -1.0, 13),
    'side': crop('side', top=4, nape=80) + [L(outline([(30, 6), (56, -4), (86, -8), (104, -12, 1), (92, 8), (86, 26), (60, 16), (36, 16)])),
                                            strand([(36, 10), (70, 0), (98, -8)], 'shade', 'b', 1.2)],
    'back': crop('back', top=6, nape=80) + [L(outline([(20, 18), (40, 0), (64, -4), (90, -10), (100, -14, 1), (92, 6), (86, 30), (50, 20)]))],
}

# Monty Hillary: gorro de lana de rayas amarillas y verde agua calado hasta las cejas, con mechones morados que asoman por
# debajo; ojos grandes redondos y sonrisa
YEL, TQ = (232, 222, 130, 255), (110, 170, 150, 255)


def stripes_cap(view, top=0, lo=48):
    if view == 'front':
        base = [L(outline([(10, lo + 4), (8, 30), (20, 10 + top), (50, top), (80, 10 + top), (92, 30), (90, lo + 4), (50, lo + 2)]), YEL)]
        return base + [strand([(x, top + 6 + abs(50 - x) * 0.25), (x + (x - 50) * 0.15, lo)], TQ, 'b', 6.0) for x in (22, 42, 62, 82)]
    if view == 'side':
        base = [L(outline([(88, lo), (90, 28), (72, 6 + top), (44, top), (18, 10 + top), (4, 34), (6, lo + 6), (50, lo + 2)]), YEL)]
        return base + [strand([(x, top + 4 + abs(46 - x) * 0.3), (x - 2, lo + 2)], TQ, 'b', 6.0) for x in (20, 40, 60, 80)]
    base = [L(outline([(10, lo + 8), (8, 30), (20, 10 + top), (50, top), (80, 10 + top), (92, 30), (90, lo + 8), (50, lo + 10)]), YEL)]
    return base + [strand([(x, top + 6 + abs(50 - x) * 0.25), (x + (x - 50) * 0.15, lo + 6)], TQ, 'b', 6.0) for x in (22, 42, 62, 82)]


CHARS[K + 'monty-hillary'] = {
    'body': 'normal', 'pal': pal('#6c5a8c', '#f6c494', iris='#2a2020', shade='#544670', deep='#3c3254'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(10, 54), (90, 54)]},
    'front': [L(outline([(12, 90), (8, 60), (16, 44), (84, 44), (92, 60), (88, 90), (82, 78), (18, 78)]))] + stripes_cap('front')
             + [fr([(20, 50), (24, 66, 1), (30, 52), (40, 62, 1), (46, 52), (56, 64, 1), (62, 52), (72, 62, 1), (80, 50)])],
    'side': [L(outline([(30, 50), (8, 56), (6, 84, 1), (18, 80), (30, 90, 1), (40, 70)]))] + stripes_cap('side'),
    'back': [L(outline([(12, 90), (8, 60), (16, 48), (84, 48), (92, 60), (88, 90), (70, 84, 1), (50, 92, 1), (30, 84, 1)]))] + stripes_cap('back'),
}

# Monty Patten: casco redondo de pelo azul muy oscuro, como un champiñón, con el flequillo recto tapándole la frente;
# unas gafas redondas enormes de cristal opaco crema y la boca seria
CHARS[K + 'monty-patten'] = {
    'body': 'normal', 'pal': pal('#2c2a52', '#f2b47a', iris='#2a2020', shade='#201e3e', deep='#16142c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(10, 66), (14, 60), (50, 64), (86, 60), (90, 66)]},
    'front': [L(outline([(10, 70), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (90, 70), (50, 66)])),
              L(outline([(58, 0), (86, 14), (96, 42), (90, 66), (76, 40)]), 'shade', 'b', False), L(outline([(30, 14), (50, 6), (62, 12), (44, 18)]), 'light', 'b', False)]
             + lens_glasses('front', 78),
    'side': [L(outline([(88, 62), (94, 36), (80, 10), (54, -2), (26, 4), (6, 26), (2, 56), (10, 80), (30, 86), (40, 66), (60, 64)])),
             L(outline([(4, 46), (28, 52), (38, 66), (28, 84), (10, 78)]), 'shade', 'b', False)] + lens_glasses('side', 78),
    'back': [L(outline([(10, 80), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (90, 80), (50, 86)])),
             L(outline([(58, 0), (86, 14), (96, 46), (90, 80), (62, 86)]), 'shade', 'b', False)],
}

# Morgan Iser: pelo castaño claro corto en pinchos, con un mechón de punta arriba y el flequillo en picos; ojos azules,
# nariz larga y media sonrisa
CHARS[K + 'morgan-iser'] = {
    'body': 'normal', 'pal': pal('#9c7e4a', '#f2bc84', iris='#4a6a9a', shade='#7c6236', deep='#5a4624'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 3.0),
             'hairline': [(14, 62), (16, 48), (24, 54), (32, 44), (42, 56), (52, 44), (62, 56), (72, 44), (80, 54), (86, 48), (88, 62)]},
    'front': messy('front', amp=8, n=10, seed=33, lo=58, rx=44, ry=38) + [L(outline([(40, 8), (46, -14, 1), (54, 2), (62, -8, 1), (62, 10)])),
                                                                         fr([(18, 48), (24, 58, 1), (32, 44), (42, 58, 1), (50, 44), (60, 58, 1), (68, 44), (78, 56, 1), (84, 46), (70, 36), (30, 36)])],
    'side': messy('side', amp=8, n=9, seed=33, nape=80) + [L(outline([(44, 4), (52, -14, 1), (60, 2)]))],
    'back': messy('back', amp=8, n=10, seed=33, nape=82) + [L(outline([(40, 8), (46, -12, 1), (54, 4)]))],
}

# Moses Pumper: pelo verde con raya en medio recogido en dos moños a los lados atados con gomas azules; cejas negras gruesas
# y dos parches rojos cuadrados en las mejillas, como pintura de guerra
CHARS[K + 'moses-pumper'] = {
    'body': 'normal', 'pal': pal('#7aa84a', '#f2b47a', iris='#3a5a8a', shade='#5e8a36', deep='#466a26', band='#2c3a6a', paint='#c8301e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 64), (17, 48), (30, 40), (50, 36), (70, 40), (83, 48), (86, 64)]},
    'front': [L(outline([(-2, 54), (6, 44), (14, 52), (14, 92), (4, 94), (-4, 80)])), L(outline([(102, 54), (94, 44), (86, 52), (86, 92), (96, 94), (104, 80)]))]
             + crop('front', top=2, side=66, w=2) + [strand([(50, 4), (50, 34)], 'deep', 'b', 1.2), L([(4, 70), (16, 70)], 'band', 'f', False, False, 2.4), L([(96, 70), (84, 70)], 'band', 'f', False, False, 2.4)]
             + brows(66, DARK, 4.5, 15, 2.0, 15) + [L(outline([(24, 84, 1), (34, 84, 1), (34, 92, 1), (24, 92, 1)], 2), 'paint', 'f', False), L(outline([(66, 84, 1), (76, 84, 1), (76, 92, 1), (66, 92, 1)], 2), 'paint', 'f', False)],
    'side': crop('side', top=0, nape=80, w=2) + [L(outline([(16, 54), (34, 50), (36, 92), (18, 94), (10, 80)])), L([(16, 70), (36, 70)], 'band', 'f', False, False, 2.4)]
            + brow_side(66, DARK, 4.5, 2.0) + [L(outline([(76, 84, 1), (84, 84, 1), (84, 92, 1), (76, 92, 1)], 2), 'paint', 'f', False)],
    'back': [L(outline([(-2, 54), (6, 44), (14, 52), (14, 92), (4, 94), (-4, 80)])), L(outline([(102, 54), (94, 44), (86, 52), (86, 92), (96, 94), (104, 80)]))]
            + crop('back', top=2, nape=82, w=2) + [strand([(50, 4), (50, 70)], 'deep', 'b', 1.0), L([(4, 70), (16, 70)], 'band', 'f', False, False, 2.4), L([(96, 70), (84, 70)], 'band', 'f', False, False, 2.4)],
}

# Nat Picker: pelo rojo largo y liso, peinado hacia la derecha de la imagen con puntas que salen hacia arriba y un mechón
# largo que le baja por ese lado hasta la mandíbula; ojos afilados, ceño fruncido y sonrisa
CHARS[K + 'nat-picker'] = {
    'body': 'normal', 'pal': pal('#c8381c', '#f6c494', iris='#2a2020', shade='#a02a14', deep='#7a1e0c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': crop('front', top=4, side=70, w=2) + [L(outline([(60, 4), (88, -8, 1), (82, 8), (104, 10, 1), (92, 24), (98, 60), (96, 100, 1), (86, 80), (84, 40)])),
                                                   fr([(16, 66), (14, 40), (26, 18), (50, 10), (76, 14), (90, 34), (90, 50), (82, 44), (70, 52, 1), (64, 40), (52, 50, 1), (46, 40),
                                                       (34, 50, 1), (28, 42), (20, 56)])],
    'side': crop('side', top=2, nape=86, w=2) + [L(outline([(40, 4), (66, -10, 1), (66, 6), (90, 4, 1), (84, 20)])), fr([(62, 40), (82, 20), (96, 40), (92, 62, 1), (82, 48)])],
    'back': crop('back', top=4, nape=88, w=2) + [L(outline([(40, 4), (88, -8, 1), (82, 8), (104, 10, 1), (92, 24), (96, 60), (92, 96, 1), (84, 70)]))],
}


def happy_eyes(y=76, sep=14, c=OUTC, w=1.8):
    """Ojos cerrados de risa (dos arcos hacia arriba)."""
    return [L(quad((cx - 6, y + 2), (cx, y - 5), (cx + 6, y + 2)), c, 'f', False, False, w) for cx in (50 - sep, 50 + sep)]


def squares(y=86, dx=24, c='paint', h=7, w=9):
    return [L(outline([(cx - w / 2, y, 1), (cx + w / 2, y, 1), (cx + w / 2, y + h, 1), (cx - w / 2, y + h, 1)], 2), c, 'f', False) for cx in (50 - dx, 50 + dx)]


# Nathan Weyton: piel morena y pelo malva peinado de lado, con las puntas que se abren hacia fuera sobre las orejas; ojos
# redondos, ceño fruncido y boca de enfado
CHARS[K + 'nathan-weyton'] = {
    'body': 'normal', 'pal': pal('#b07e7e', '#c8885a', iris='#2a2020', shade='#8e6262', deep='#6e4848'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': crop('front', top=2, side=64, w=4) + [L(outline([(16, 58), (0, 72, 1), (14, 70)])), L(outline([(84, 58), (100, 72, 1), (86, 70)])),
                                                   fr([(16, 60), (14, 38), (26, 18), (50, 10), (76, 14), (88, 34), (88, 58), (80, 46), (66, 40), (50, 52, 1), (44, 40), (30, 44)]),
                                                   strand([(30, 20), (56, 14), (80, 28)], 'shade', 'f', 1.2)],
    'side': crop('side', top=0, nape=84, w=3) + [L(outline([(12, 60), (-4, 74, 1), (14, 72)])), fr([(62, 40), (80, 18), (94, 36), (92, 54, 1), (80, 46)])],
    'back': crop('back', top=2, nape=84, w=4) + [L(outline([(16, 58), (0, 72, 1), (14, 70)])), L(outline([(84, 58), (100, 72, 1), (86, 70)]))],
}

# Nathin Gaunt: pelo gris revuelto en pinchos con un mechón alto de punta y un flequillo largo que le tapa un ojo; piel
# morena con cicatrices en la mejilla, guiño y sonrisa de dientes
CHARS[K + 'nathin-gaunt'] = {
    'body': 'normal', 'pal': pal('#9c988c', '#c48a56', iris='#2a2020', shade='#7c786e', deep='#5c5a52', scar='#8a5a3a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=12, n=11, seed=44, lo=58, rx=48, ry=40) + [L(outline([(54, 4), (64, -20, 1), (64, 4)])),
                                                                          fr([(14, 56), (20, 36), (40, 24), (62, 24), (82, 34), (90, 56), (84, 80, 1), (76, 62), (66, 84, 1), (58, 60), (50, 50),
                                                                              (40, 58, 1), (34, 46), (24, 58, 1)]),
                                                                          L([(26, 84), (34, 92)], 'scar', 'f', False, False, 1.4), L([(30, 82), (24, 92)], 'scar', 'f', False, False, 1.2)],
    'side': messy('side', amp=12, n=10, seed=44, nape=84) + [L(outline([(52, 2), (62, -20, 1), (64, 4)])), fr([(60, 36), (82, 24), (96, 44), (92, 70, 1), (82, 52)])],
    'back': messy('back', amp=12, n=11, seed=44, nape=86) + [L(outline([(50, 4), (60, -18, 1), (62, 6)]))],
}

# Ness Lockley: media melena castaño rojizo con flequillo, que cae en capas hasta la mandíbula; gafas redondas verdes y
# sonrisa tranquila
CHARS[K + 'ness-lockley'] = {
    'body': 'normal', 'pal': pal('#a8482a', '#fcd2ae', iris='#2a2020', shade='#86381e', deep='#642a14'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'glasses': (70, 110, 60, 255), 'hairline': False},
    'front': longhair('front', length=92, flare=4, top=0, ends=3) + [fr([(14, 62), (14, 36), (30, 16), (50, 10), (70, 16), (86, 36), (86, 62), (80, 54), (74, 66, 1), (68, 50), (60, 62, 1),
                                                                       (54, 48), (46, 62, 1), (40, 48), (32, 62, 1), (26, 50), (20, 58)])],
    'side': longhair('side', length=92, flare=2, top=0) + [fr([(64, 30), (86, 30), (94, 50), (90, 64, 1), (80, 50)])],
    'back': longhair('back', length=92, flare=4, top=0, ends=4),
}

# Nester Damus (portero): turbante crema enrollado, con pliegues en diagonal y tonos tostados; piel morena, una piedra verde
# en la frente, ojos grandes y boquita en O
CHARS[K + 'nester-damus'] = {
    'body': 'normal', 'pal': pal('#eee6b6', '#c8885a', iris='#2a2020', shade='#d4c48e', deep='#a8946a', gem='#6ab04a', lip='#8a4a2e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'none', 'hairline': [(10, 58), (16, 50), (30, 50), (50, 52), (70, 50), (84, 50), (90, 58)]},
    'front': [L(outline([(10, 62), (4, 36), (14, 10), (36, -6), (64, -6), (86, 10), (96, 36), (90, 62), (50, 58)])),
              L(outline([(60, -4), (88, 12), (96, 40), (90, 60), (72, 36)]), 'shade', 'b', False),
              strand([(10, 50), (40, 20), (70, -2)], 'deep', 'b', 1.4), strand([(14, 30), (50, 4)], 'deep', 'b', 1.2), strand([(40, 54), (80, 20)], 'deep', 'b', 1.2),
              L(ell(50, 60, 2.6, 3.2), 'gem', 'f', ln=True), L(ell(50, 97, 3.4, 3.4), 'lip', 'f', ln=True)],
    'side': [L(outline([(86, 56), (92, 30), (76, 4), (48, -6), (20, 4), (4, 30), (2, 58), (14, 72), (40, 62), (60, 58)])),
             L(outline([(4, 40), (30, 44), (40, 60), (14, 70)]), 'shade', 'b', False),
             strand([(20, 60), (50, 20), (80, 8)], 'deep', 'b', 1.4), strand([(10, 36), (40, 4)], 'deep', 'b', 1.2)],
    'back': [L(outline([(10, 70), (4, 36), (14, 10), (36, -6), (64, -6), (86, 10), (96, 36), (90, 70), (50, 74)])),
             L(outline([(58, -4), (88, 12), (96, 44), (90, 70), (64, 74)]), 'shade', 'b', False),
             strand([(10, 56), (50, 20), (86, 6)], 'deep', 'b', 1.4), strand([(14, 30), (60, 0)], 'deep', 'b', 1.2), strand([(30, 70), (90, 36)], 'deep', 'b', 1.2)],
}

# Nev Erin: pelo naranja rojizo en pinchos largos echados hacia la derecha de la imagen, con un remolino alto; ojos verdes y
# sonrisa
CHARS[K + 'nev-erin'] = {
    'body': 'normal', 'pal': pal('#c84c1c', '#f8cca2', iris='#5a8a2a', shade='#a43a14', deep='#7c2a0c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=10, n=10, seed=55, lo=62, rx=46, ry=38, sweep=0.5) + [L(outline([(30, 6), (26, -20, 1), (42, 4)])),
                                                                                     fr([(14, 58), (18, 36), (36, 22), (60, 22), (84, 30), (100, 44, 1), (86, 46), (94, 60, 1), (78, 52),
                                                                                         (72, 64, 1), (62, 48), (52, 60, 1), (46, 46), (34, 56, 1), (28, 46), (20, 56)])],
    'side': messy('side', amp=10, n=9, seed=55, nape=82, sweep=0.5) + [L(outline([(36, 2), (30, -20, 1), (46, 0)])), fr([(60, 36), (84, 22), (100, 40, 1), (92, 50), (96, 62, 1), (80, 50)])],
    'back': messy('back', amp=10, n=10, seed=55, nape=84, sweep=0.5) + [L(outline([(30, 6), (26, -18, 1), (42, 4)]))],
}

# Neville List: pelo verde oliva corto y redondo, como un casco, con un mechón en pico en el centro de la frente; ojos
# cerrados de risa, parches rojos en las mejillas y sonrisa
CHARS[K + 'neville-list'] = {
    'body': 'normal', 'pal': pal('#6a6a2c', '#f6c08a', iris='#2a2020', shade='#52521e', deep='#3a3a14', paint='#c8301e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (16, 46), (30, 42), (44, 46), (50, 56), (56, 46), (70, 42), (84, 46), (86, 60)]},
    'front': crop('front', top=0, side=60, w=6) + happy_eyes(76) + squares(81, 21, 'paint', 6, 8) + [fr([(42, 44), (50, 58, 1), (58, 44)])],
    'side': crop('side', top=0, nape=82, w=4) + [L(quad((76, 78), (82, 71), (88, 78)), OUTC, 'f', False, False, 1.8)] + [L(outline([(78, 84, 1), (86, 84, 1), (86, 91, 1), (78, 91, 1)], 2), 'paint', 'f', False)],
    'back': crop('back', top=0, nape=82, w=6),
}

# Nick Crew (portero): pelo rizado celeste con un mechón ancho rosa coral cruzándole la cabeza en diagonal; ojos afilados y
# sonrisa de pillo
CHARS[K + 'nick-crew'] = {
    'body': 'normal', 'pal': pal('#a8d4d8', '#fcd8b8', iris='#2a2020', shade='#86b0b6', deep='#6a9298', pink='#cc6a6c', pink_d='#a8505a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 64), (16, 50), (30, 46), (50, 44), (70, 46), (84, 50), (86, 64)]},
    'front': [L(cloud(50, 36, 46, 30, 9, 0.2)), L(cloud(14, 62, 10, 12, 4)), L(cloud(86, 62, 10, 12, 4, 0.4))] + crop('front', top=8, side=60, w=4, shade=False)
             + [L(outline([(22, 66), (14, 40), (30, 14), (56, 8), (70, 14), (52, 30), (40, 50), (32, 70, 1)]), 'pink'), strand([(30, 30), (54, 14)], 'pink_d', 'b', 1.2)],
    'side': [L(cloud(44, 36, 46, 32, 9)), L(cloud(20, 70, 14, 14, 5))] + crop('side', top=6, nape=80, w=3, shade=False)
            + [L(outline([(60, 10), (84, 20), (92, 36), (76, 34), (60, 24)]), 'pink')],
    'back': [L(cloud(50, 40, 48, 36, 10, 0.2))] + crop('back', top=8, nape=82, w=4, shade=False) + [L(outline([(30, 10), (60, 4), (40, 30), (20, 50)]), 'pink')],
}

# Nick Knack: gorro ajustado azul marino calado hasta las cejas, con mechones esponjosos rosa crema que le asoman por los lados
# junto a las orejas; piel morena, gafas redondas marrones y sonrisa
CHARS[K + 'nick-knack'] = {
    'body': 'normal', 'pal': pal('#e8c4b8', '#c48a5a', iris='#2a2020', shade='#c8a094', deep='#a07a70', hat='#2c3c5c', hat_d='#1e2a42'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'glasses': (140, 60, 40, 255), 'hairline': [(10, 58), (90, 58)]},
    'front': [L(cloud(8, 80, 12, 12, 5, 0.3)), L(cloud(92, 80, 12, 12, 5, 0.5)),
              L(outline([(10, 62), (6, 36), (18, 12), (50, 2), (82, 12), (94, 36), (90, 62), (50, 58)]), 'hat'),
              L(outline([(60, 4), (86, 16), (94, 40), (90, 60), (74, 40)]), 'hat_d', 'b', False)],
    'side': [L(cloud(28, 82, 14, 12, 5)), L(outline([(86, 56), (90, 30), (72, 6), (44, 0), (18, 10), (4, 36), (6, 64), (30, 70), (60, 60)]), 'hat'),
             L(outline([(6, 44), (30, 50), (36, 66), (8, 62)]), 'hat_d', 'b', False)],
    'back': [L(cloud(10, 80, 12, 12, 5, 0.3)), L(cloud(90, 80, 12, 12, 5, 0.5)), L(cloud(50, 82, 30, 10, 6)),
             L(outline([(10, 72), (6, 36), (18, 12), (50, 2), (82, 12), (94, 36), (90, 72), (50, 76)]), 'hat'),
             L(outline([(58, 4), (86, 16), (94, 44), (90, 72), (64, 76)]), 'hat_d', 'b', False)],
}


def wink(y=76, sep=14):
    """Ojo derecho de la imagen cerrado en guiño (el izquierdo lo dibuja la cara)."""
    return [L(outline([(50 + sep - 8, y - 9), (50 + sep + 8, y - 9), (50 + sep + 8, y + 9), (50 + sep - 8, y + 9)], 2), 'skin', 'f', False),
            L([(50 + sep - 7, y - 3), (50 + sep + 1, y + 1), (50 + sep - 7, y + 4)], OUTC, 'f', False, False, 1.8)]


# Nick Orner (portero): pelo azul marino liso con un flequillo largo peinado de lado y más largo por detrás, hasta la
# mandíbula; guiño y boca abierta en mueca
CHARS[K + 'nick-orner'] = {
    'body': 'normal', 'pal': pal('#2c4a6c', '#f2b47a', iris='#2a2020', shade='#203a56', deep='#162a40', lip='#8a4a2e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': longhair('front', length=86, flare=0, top=2, ends=2) + [fr([(14, 60), (14, 34), (30, 14), (54, 8), (76, 14), (88, 34), (88, 56), (80, 44), (60, 40), (40, 52),
                                                                       (26, 60, 1), (22, 50)])]
             + wink(76) + [L(blob([(42, 94), (58, 94), (56, 100), (44, 100)], 4), 'lip', 'f', ln=True), L([(43, 97), (57, 97)], WHITE, 'f', False, False, 1.2)],
    'side': longhair('side', length=86, flare=0, top=2) + [fr([(62, 32), (86, 26), (94, 48), (90, 60, 1), (80, 48)])],
    'back': longhair('back', length=86, flare=0, top=2, ends=3),
}

# Nick Savers (portero): cara ancha y mofletuda; pelo verde oscuro en pinchos echados a un lado, con el otro lado rapado más
# claro; cejas verdes gruesas, ojos redondos, nariz redonda y sonrisa torcida
CHARS[K + 'nick-savers'] = {
    'body': 'corpulento', 'pal': pal('#2a7a4a', '#f6c08a', iris='#2a2020', shade='#1e5e38', deep='#144428', shaved='#7aa84a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'face_front': WIDE, 'ear_out': 6, 'nose': (50, 86, 3.6),
             'hairline': [(10, 60), (14, 46), (28, 40), (50, 38), (70, 40), (86, 46), (90, 60)]},
    'front': [L(outline([(10, 62), (8, 40), (22, 22), (34, 30), (32, 54)]), 'shaved')]
             + [L(outline([(30, 52), (30, 24), (26, 6, 1), (42, 10), (54, -4, 1), (62, 8), (82, 2, 1), (80, 16), (96, 18, 1), (90, 30), (94, 62), (86, 48), (40, 44)])),
                L(outline([(60, 8), (86, 18), (94, 40), (90, 58), (78, 36)]), 'shade', 'b', False)] + brows(64, 'mid', 4.6, 15, 0.0, 13),
    'side': [L(outline([(10, 70), (4, 44), (16, 24), (40, 22), (46, 50), (30, 70)]), 'shaved'),
             L(outline([(46, 44), (40, 16), (46, -4, 1), (60, 6), (74, -2, 1), (78, 14), (96, 16, 1), (90, 30), (88, 44), (64, 50)]))] + brow_side(64, 'mid', 4.6),
    'back': [L(outline([(12, 76), (8, 44), (20, 20), (50, 12), (80, 20), (92, 44), (88, 76), (50, 84)]), 'shaved'),
             L(outline([(30, 30), (30, 10), (46, -2, 1), (58, 8), (78, 2, 1), (80, 16), (94, 20, 1), (88, 40), (60, 36)]))],
}

# Nick Swagg (portero): melena crema enorme y erizada que le cae por los lados hasta los hombros; cinta azul marino en la
# frente con un círculo blanco; pintura naranja alrededor de los ojos, como una máscara, y labios naranjas
PAINT = (196, 82, 30, 255)
CHARS[K + 'nick-swagg'] = {
    'body': 'normal', 'pal': pal('#efe6c6', '#ecd6bc', iris='#2a2020', shade='#d4c4a0', deep='#b4a07c', band='#2c3a5c', lip='#d0602a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': [(10, 66), (90, 66)]},
    'front': [L(outline([(10, 120), (-8, 100, 1), (0, 80), (-12, 58, 1), (2, 44), (-6, 22, 1), (14, 14), (16, -8, 1), (34, 4), (50, -12, 1), (66, 4), (86, -6, 1), (86, 14),
                         (106, 22, 1), (98, 44), (112, 58, 1), (100, 80), (108, 100, 1), (90, 120), (84, 90), (82, 64), (18, 64), (16, 90)])),
              L(outline([(60, 0), (86, 10), (100, 40), (96, 90), (88, 116), (84, 60)]), 'shade', 'b', False),
              L(outline([(10, 58), (10, 48), (50, 46), (90, 48), (90, 58), (50, 56)]), 'band', 'f'),
              L(ell(50, 52, 4.4, 3.4), WHITE, 'f', False), L(ell(50, 52, 2, 1.6), 'band', 'f', False),
              L([(22, 68), (30, 84), (44, 82), (46, 70)], PAINT, 'f', False, False, 2.6), L([(78, 68), (70, 84), (56, 82), (54, 70)], PAINT, 'f', False, False, 2.6),
              L(blob([(42, 96), (50, 94), (58, 96), (50, 100)], 4), 'lip', 'f', ln=True)],
    'side': [L(outline([(54, 64), (58, 50), (80, 42), (90, 24), (96, 4, 1), (78, 6), (74, -10, 1), (58, 2), (40, -12, 1), (30, 6), (8, 4, 1), (8, 24), (-12, 36, 1), (0, 50),
                        (-12, 70, 1), (2, 80), (-6, 104, 1), (14, 96), (20, 120, 1), (32, 98), (44, 80)])),
             L(outline([(2, 40), (26, 44), (40, 70), (24, 100), (4, 90)]), 'shade', 'b', False),
             L(outline([(40, 56), (40, 46), (94, 46), (94, 56)]), 'band', 'f'), L([(80, 68), (72, 84), (84, 82)], PAINT, 'f', False, False, 2.6)],
    'back': [L(outline([(10, 120), (-8, 100, 1), (0, 80), (-12, 58, 1), (2, 44), (-6, 22, 1), (14, 14), (16, -8, 1), (34, 4), (50, -12, 1), (66, 4), (86, -6, 1), (86, 14),
                        (106, 22, 1), (98, 44), (112, 58, 1), (100, 80), (108, 100, 1), (90, 120), (70, 108, 1), (50, 122, 1), (30, 108, 1)])),
             L(outline([(58, 0), (86, 10), (100, 44), (96, 100), (70, 108)]), 'shade', 'b', False),
             L(outline([(4, 56), (4, 46), (96, 46), (96, 56)]), 'band', 'b')],
}

# Nick Templeton: pelo azul marino corto y redondo, rapado de cerca; piel morena, cejas gruesas y sonrisa
CHARS[K + 'nick-templeton'] = {
    'body': 'normal', 'pal': pal('#2c4a6c', '#c88a5a', iris='#2a2020', shade='#203a56', deep='#162a40'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (17, 46), (30, 40), (50, 38), (70, 40), (83, 46), (86, 60)]},
    'front': crop('front', top=2, side=60, w=1) + [L([(24, 86), (30, 84)], (90, 50, 30, 255), 'f', False, False, 1.0), L([(70, 84), (76, 86)], (90, 50, 30, 255), 'f', False, False, 1.0)],
    'side': crop('side', top=0, nape=80),
    'back': crop('back', top=2, nape=80),
}

# Nick Turine: la coronilla rapada gris azulada con un moñito castaño atado arriba, y el pelo castaño de los lados cortado en
# dos alas rectas que le tapan la frente; una cinta blanca con una flor de cerezo rosa; ojos azules y cara ancha
CHARS[K + 'nick-turine'] = {
    'body': 'corpulento', 'pal': pal('#8a5a2a', '#f2b47a', iris='#5a8ab0', shade='#6c441e', deep='#4e3014', shaved='#7a9cac', band='#f4ece0', flower='#e08a9a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'face_front': WIDE, 'ear_out': 6, 'nose': (50, 88, 3.4), 'hairline': [(10, 62), (90, 62)]},
    'front': [L(outline([(20, 30), (30, 6), (50, 0), (70, 6), (80, 30)]), 'shaved'), L(ell(50, -4, 6, 6)), L(outline([(50, -8), (60, -16, 1), (56, -6)])),
              L(outline([(4, 64), (2, 34), (20, 22), (46, 30), (50, 34), (54, 30), (80, 22), (98, 34), (96, 64), (50, 60)])),
              L(outline([(56, 30), (80, 24), (98, 36), (96, 62), (76, 44)]), 'shade', 'b', False),
              strand([(10, 40), (12, 60)], 'deep', 'b', 1.0), strand([(24, 36), (26, 60)], 'deep', 'b', 1.0), strand([(76, 36), (74, 60)], 'deep', 'b', 1.0), strand([(90, 40), (88, 60)], 'deep', 'b', 1.0),
              L(outline([(26, 36, 1), (74, 36, 1), (74, 58, 1), (26, 58, 1)], 2), 'band', 'f', ln=True), L(cloud(50, 47, 8, 8, 5), 'flower', 'f', False), L(ell(50, 47, 2, 2), 'band', 'f', False)],
    'side': [L(outline([(30, 30), (40, 6), (60, 2), (80, 14), (84, 32)]), 'shaved'), L(ell(56, -2, 6, 6)),
             L(outline([(90, 60), (94, 34), (70, 24), (40, 26), (8, 30), (2, 56), (10, 76), (34, 74), (56, 62)])),
             L(outline([(4, 40), (30, 44), (36, 70), (12, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(20, 34), (30, 8), (50, 2), (70, 8), (80, 34)]), 'shaved'), L(ell(50, -2, 6, 6)),
             L(outline([(4, 72), (2, 34), (24, 28), (50, 32), (76, 28), (98, 34), (96, 72), (50, 78)])),
             L(outline([(56, 32), (80, 28), (98, 38), (96, 70), (64, 76)]), 'shade', 'b', False)],
}

# Nick Washing: pelo ondulado gris beis con sombras malva, abultado y peinado hacia un lado; ojos afilados con ceño y media
# sonrisa
CHARS[K + 'nick-washing'] = {
    'body': 'normal', 'pal': pal('#c8bca8', '#f0b47a', iris='#2a2020', shade='#9c8c8c', deep='#7a6a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 62), (16, 48), (30, 44), (44, 48), (60, 40), (76, 44), (86, 50), (88, 62)]},
    'front': [L(cloud(50, 26, 50, 30, 8, 0.3)), L(outline([(14, 64), (8, 40), (20, 30), (80, 30), (92, 40), (86, 62), (80, 48), (20, 48)])),
              L(outline([(40, 4), (66, 0), (86, 16), (70, 26), (50, 18)]), 'shade', 'b', False), L(outline([(12, 30), (28, 22), (30, 40), (16, 50)]), 'shade', 'b', False),
              fr([(18, 50), (22, 36), (40, 28), (60, 30), (72, 40), (62, 44), (48, 40), (32, 44)])],
    'side': [L(cloud(46, 28, 46, 30, 8)), L(outline([(66, 50), (82, 40), (90, 30), (10, 30), (2, 56), (10, 76), (34, 80), (44, 60)])),
             L(outline([(4, 40), (30, 40), (40, 60), (30, 78), (10, 72)]), 'shade', 'b', False)],
    'back': [L(cloud(50, 30, 50, 32, 8, 0.3)), L(outline([(12, 78), (6, 40), (94, 40), (88, 78), (50, 86)])),
             L(outline([(58, 10), (88, 24), (94, 50), (88, 78), (62, 84)]), 'shade', 'b', False)],
}

# Nick Yergrub: piel oscura y pelo crema con dos alas de punta que le salen a los lados de la cabeza y un pincho alto en el
# centro; ojos amarillos, cejas claras y dos lágrimas pintadas de blanco en cada mejilla
CHARS[K + 'nick-yergrub'] = {
    'body': 'normal', 'pal': pal('#dcd2a8', '#a87a50', iris='#c8b43a', shade='#bcb088', deep='#9a906a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 60), (16, 48), (30, 42), (50, 40), (70, 42), (84, 48), (86, 60)]},
    'front': crop('front', top=6, side=60, w=2) + [L(outline([(16, 52), (-6, 38, 1), (2, 54), (-4, 64, 1), (16, 66)])), L(outline([(84, 52), (106, 38, 1), (98, 54), (104, 64, 1), (84, 66)])),
                                                   L(outline([(44, 10), (50, -22, 1), (56, 10)]))] + brows(66, (236, 226, 190, 255), 2.6, 15, -1.0, 12)
             + [L(outline([(cx - 1.4, 84), (cx + 1.4, 84), (cx, 92, 1)], 3), WHITE, 'f', False) for cx in (28, 33, 67, 72)],
    'side': crop('side', top=4, nape=80, w=2) + [L(outline([(16, 46), (-8, 36, 1), (2, 54), (-4, 64, 1), (18, 64)])), L(outline([(46, 6), (52, -22, 1), (58, 8)]))],
    'back': crop('back', top=6, nape=80, w=2) + [L(outline([(16, 52), (-6, 38, 1), (2, 54), (-4, 64, 1), (16, 66)])), L(outline([(84, 52), (106, 38, 1), (98, 54), (104, 64, 1), (84, 66)])),
                                                 L(outline([(44, 10), (50, -20, 1), (56, 10)]))],
}

# Nigel Bramel: pelo verde azulado muy erizado, en pinchos largos hacia todos lados; ojos redondos, ceño y boquita en O
CHARS[K + 'nigel-bramel'] = {
    'body': 'normal', 'pal': pal('#5c9ca2', '#f6c494', iris='#2a2020', shade='#467e84', deep='#325e62', lip='#8a4a2e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 62), (18, 48), (26, 56), (36, 46), (44, 58), (54, 46), (64, 58), (74, 46), (82, 56), (86, 62)]},
    'front': messy('front', amp=16, n=12, seed=66, lo=62, rx=48, ry=40) + [L(ell(50, 97, 2.6, 3.2), 'lip', 'f', ln=True)],
    'side': messy('side', amp=16, n=11, seed=66, nape=84),
    'back': messy('back', amp=16, n=12, seed=66, nape=86),
}


# Noah Gerkin (portero): grandullón de cara ancha; pelo castaño oliva corto en mechones de punta como hojas; ojos redondos
# mirando hacia arriba, nariz redonda y sonrisa ondulada
CHARS[K + 'noah-gerkin'] = {
    'body': 'corpulento', 'pal': pal('#7c6a3a', '#f2b47a', iris='#2a2020', shade='#5e5028', deep='#42381a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'none', 'face_front': WIDE, 'ear_out': 8, 'nose': (50, 86, 3.6), 'eye_y': 74,
             'hairline': [(10, 60), (14, 48), (24, 54), (34, 44), (44, 52), (56, 44), (66, 52), (76, 44), (86, 50), (90, 60)]},
    'front': messy('front', amp=8, n=9, seed=77, lo=58, rx=48, ry=38) + [fr([(16, 50), (24, 60, 1), (32, 46), (44, 58, 1), (52, 46), (62, 58, 1), (70, 46), (80, 56, 1), (86, 46), (70, 36), (30, 36)])]
             + [L(quad((36, 96), (43, 100), (50, 97)) + quad((50, 97), (57, 100), (64, 96))[1:], OUTC, 'f', False, False, 1.4)],
    'side': messy('side', amp=8, n=8, seed=77, nape=80),
    'back': messy('back', amp=8, n=9, seed=77, nape=82),
}

# Nobby Shinn: capucha de ninja azul verdoso que le tapa la cabeza y la cara hasta la nariz, con una placa gris con tres
# remaches en la frente; solo se le ven los ojos pequeños y unas cejas moradas
CHARS[K + 'nobby-shinn'] = {
    'body': 'normal', 'pal': pal('#4a8a9a', '#f6c494', iris='#2a2020', shade='#3a6e7c', deep='#2a525c', plate='#9c9a7c', plate_d='#7a785e'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': [(10, 62), (24, 56), (50, 54), (76, 56), (90, 62)]},
    'front': [L(outline([(10, 112), (4, 60), (8, 24), (24, 2), (50, -6), (76, 2), (92, 24), (96, 60), (90, 112), (50, 118)])),
              L(outline([(60, -2), (86, 10), (96, 50), (92, 110), (80, 80)]), 'shade', 'b', False),
              L(outline([(14, 84), (50, 82), (86, 84), (88, 114), (50, 118), (12, 114)]), 'mid', 'f'),
              L(outline([(60, 86), (86, 86), (88, 112), (66, 114)]), 'shade', 'f', False), strand([(46, 84), (40, 96), (50, 100)], 'deep', 'f', 1.0),
              L(outline([(28, 30, 1), (72, 30, 1), (70, 44, 1), (30, 44, 1)], 2), 'plate', 'f', ln=True)]
             + [L(ell(x, 37, 2, 2), 'plate_d', 'f', False) for x in (38, 50, 62)] + brows(68, (120, 100, 150, 255), 2.4, 14, 2.0, 10),
    'side': [L(outline([(94, 60), (92, 30), (74, 4), (44, -4), (18, 8), (2, 40), (4, 90), (20, 112), (60, 116), (90, 104), (94, 82)])),
             L(outline([(4, 50), (30, 50), (40, 90), (20, 110)]), 'shade', 'b', False),
             L(outline([(60, 84), (92, 84), (94, 104), (70, 114), (56, 100)]), 'mid', 'f'), L(outline([(66, 30), (92, 30), (92, 44), (66, 44)]), 'plate', 'f', ln=True)],
    'back': [L(outline([(10, 112), (4, 60), (8, 24), (24, 2), (50, -6), (76, 2), (92, 24), (96, 60), (90, 112), (50, 118)])),
             L(outline([(58, -2), (86, 10), (96, 50), (92, 110), (64, 116)]), 'shade', 'b', False), strand([(40, 40), (50, 50), (60, 40)], 'deep', 'b', 1.2)],
}

# Noel Vacancie (portero): pelo rosa crema muy claro, esponjoso y en mechones con un remolino arriba, que le cae por los
# lados de la cara; una franja malva debajo del flequillo; ojos rosas y sonrisa
CHARS[K + 'noel-vacancie-vacancies'] = {
    'body': 'normal', 'pal': pal('#f6d6c4', '#f2b47a', iris='#b45a6a', shade='#d8b0a0', deep='#a87a7a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 92), (2, 64), (-6, 40, 1), (8, 40), (10, 16), (30, 2), (44, 6), (50, -14, 1), (58, 4), (72, 4), (90, 16), (106, 36, 1), (94, 44), (96, 70), (90, 94),
                         (82, 76), (82, 60), (18, 60), (18, 76)])),
              L(outline([(60, 6), (88, 18), (96, 46), (92, 90), (84, 60)]), 'shade', 'b', False),
              fr([(16, 64), (18, 40), (34, 26), (58, 24), (78, 30), (88, 48), (86, 70), (80, 58), (76, 70, 1), (70, 52), (60, 48), (50, 52), (40, 48), (30, 56), (24, 70, 1), (20, 58)]),
              L(quad((32, 50), (50, 44), (68, 50)), 'deep', 'f', False, False, 2.4)],
    'side': [L(outline([(60, 50), (80, 40), (96, 30), (88, 8), (62, -4), (54, -14, 1), (44, 0), (20, 6), (4, 30), (-4, 60), (4, 88), (16, 84), (30, 90), (40, 66), (50, 56)])),
             L(outline([(2, 44), (28, 46), (38, 66), (26, 86), (8, 80)]), 'shade', 'b', False), fr([(64, 34), (88, 30), (94, 54), (90, 70, 1), (80, 54)])],
    'back': [L(outline([(10, 92), (2, 64), (-6, 40, 1), (8, 40), (10, 16), (30, 2), (44, 6), (50, -14, 1), (58, 4), (72, 4), (90, 16), (106, 36, 1), (94, 44), (96, 70), (90, 94),
                        (70, 86, 1), (50, 94, 1), (30, 86, 1)])),
             L(outline([(58, 6), (88, 18), (96, 46), (92, 90), (66, 88)]), 'shade', 'b', False)],
}

# Norm Drilling: melena dorada ondulada hasta la mandíbula, peinada hacia un lado con ondas grandes; nariz larga, ojos afilados
# y sonrisa ladeada
CHARS[K + 'norm-drilling'] = {
    'body': 'delgado', 'pal': pal('#e2b82c', '#f2b47a', iris='#2a2020', shade='#bc941c', deep='#8e6c10'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 3.0), 'hairline': False},
    'front': longhair('front', length=96, flare=8, top=0, ends=3) + [L(cloud(8, 80, 8, 14, 4, 0.2)), L(cloud(92, 80, 8, 14, 4, 0.6)),
                                                                       fr([(14, 62), (14, 36), (28, 14), (52, 6), (76, 12), (88, 32), (88, 52), (80, 40), (68, 34), (54, 36), (40, 44), (28, 54), (20, 66)]),
                                                                       strand([(30, 20), (50, 14), (72, 22)], 'shade', 'f', 1.2), strand([(24, 40), (40, 30), (60, 28)], 'shade', 'f', 1.0)],
    'side': longhair('side', length=96, flare=6, top=0) + [L(cloud(22, 86, 12, 14, 5)), fr([(62, 30), (86, 26), (94, 46), (90, 60, 1), (80, 48)])],
    'back': longhair('back', length=96, flare=8, top=0, ends=4) + [strand([(30, 20), (40, 50), (30, 80)], 'shade', 'b', 1.2), strand([(70, 20), (60, 50), (70, 80)], 'shade', 'b', 1.2)],
}

# Norry Sheets (portero): piel morena; pelo verde azulado con un pelo de antena arriba y mechones que le caen por los lados
# hasta la mandíbula; cejas gruesas fruncidas y boca grande en O de labios gruesos
CHARS[K + 'norry-sheets'] = {
    'body': 'normal', 'pal': pal('#4a8a8a', '#c48a56', iris='#2a2020', shade='#3a6e6e', deep='#2a5252', lip='#8a4a2e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 3.2), 'hairline': False},
    'front': longhair('front', length=88, flare=6, top=2, ends=3) + [L(quad((48, 2), (40, -18), (56, -22)), 'mid', 'b', False, False, 2.4),
                                                                       fr([(14, 60), (14, 36), (30, 16), (50, 10), (70, 16), (86, 36), (86, 60), (80, 48), (72, 58, 1), (66, 44), (56, 54, 1), (50, 42),
                                                                           (42, 54, 1), (36, 42), (28, 56, 1), (22, 48)])]
             + brows(66, DARK, 4.6, 15, 2.6, 14) + [L(ell(50, 98, 7, 6), 'lip', 'f', ln=True), L([(45, 98), (55, 98)], OUTC, 'f', False, False, 1.2)],
    'side': longhair('side', length=88, flare=4, top=2) + [L(quad((50, -2), (44, -20), (60, -24)), 'mid', 'b', False, False, 2.4), fr([(62, 30), (86, 30), (94, 50), (90, 62, 1), (80, 50)])]
            + brow_side(66, DARK, 4.6, 2.6),
    'back': longhair('back', length=88, flare=6, top=2, ends=4) + [L(quad((48, 2), (40, -18), (56, -22)), 'mid', 'b', False, False, 2.4)],
}

# Odo Cologne: pelo rubio peinado hacia atrás, con los lados que le bajan hasta el cuello; un antifaz morado de fiesta con
# los ojos rojos y lunares, que le tapa media cara; media sonrisa
MASK, MASK_D = (140, 120, 160, 255), (200, 50, 70, 255)
CHARS[K + 'odo-cologne'] = {
    'body': 'normal', 'pal': pal('#e8c862', '#f2b47a', iris='#2a2020', shade='#c4a444', deep='#9a7e2c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 88, 2.6),
             'hairline': [(14, 66), (17, 48), (30, 36), (50, 32), (70, 36), (83, 48), (86, 66)]},
    'front': longhair('front', length=96, flare=2, top=2, ends=2) + [strand([(40, 4), (36, 30)], 'deep', 'b', 1.0), strand([(60, 4), (64, 30)], 'deep', 'b', 1.0),
                                                                       L(outline([(10, 62, 1), (30, 70), (50, 76), (70, 70), (90, 62, 1), (86, 84), (66, 86), (50, 82), (34, 86), (14, 84)]), MASK, 'f', ln=True),
                                                                       L(outline([(26, 74), (42, 78), (38, 84, 1), (28, 82)]), MASK_D, 'f', False),
                                                                       L(outline([(74, 74), (58, 78), (62, 84, 1), (72, 82)]), MASK_D, 'f', False)]
             + [L(ell(x, y, 1.2, 1.2), MASK_D, 'f', False) for x, y in ((18, 70), (24, 72), (82, 70), (76, 72))],
    'side': longhair('side', length=96, flare=0, top=2) + [L(outline([(60, 68), (96, 66, 1), (92, 84), (70, 84)]), MASK, 'f', ln=True)],
    'back': longhair('back', length=96, flare=2, top=2, ends=3) + [strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Odo Toilette (portero): piel morena; pelo morado de tupé plano con dos picos como cuernos arriba y un mechón amarillo que le
# cae por delante de la cara; ojos verdes y sonrisa ladeada
CHARS[K + 'odo-toilette'] = {
    'body': 'normal', 'pal': pal('#6c5c8c', '#c48a56', iris='#5a7a3a', shade='#544670', deep='#3c3254', lock='#e2c444'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 64), (16, 46), (30, 42), (50, 44), (70, 42), (84, 46), (86, 64)]},
    'front': [L(outline([(16, 64), (8, 40), (10, 14), (6, -8, 1), (26, 4), (50, 8), (74, 4), (94, -8, 1), (90, 14), (92, 40), (84, 64), (80, 50), (20, 50)])),
              L(outline([(60, 8), (90, 0), (90, 40), (84, 62), (76, 36)]), 'shade', 'b', False), strand([(50, 10), (50, 40)], 'deep', 'b', 1.2),
              fr([(36, 40), (46, 36), (52, 50), (50, 80), (44, 90, 1), (44, 70), (38, 52)], 'lock')],
    'side': [L(outline([(66, 50), (82, 40), (92, 20), (96, -6, 1), (74, 6), (44, 6), (16, 12), (4, 36), (6, 66), (20, 82), (36, 78), (42, 60), (54, 54)])),
             L(outline([(4, 40), (28, 46), (40, 60), (30, 78), (12, 72)]), 'shade', 'b', False), fr([(76, 40), (86, 38), (90, 60), (86, 80, 1), (80, 56)], 'lock')],
    'back': [L(outline([(16, 80), (8, 40), (10, 14), (6, -8, 1), (26, 4), (50, 8), (74, 4), (94, -8, 1), (90, 14), (92, 40), (84, 80), (50, 86)])),
             L(outline([(58, 8), (90, 0), (92, 44), (84, 80), (62, 84)]), 'shade', 'b', False)],
}

# Olef Tennant: casco militar verde de camuflaje calado hasta las cejas, con una barba corta gris que le rodea la mandíbula;
# cejas rojas fruncidas, una cicatriz en cruz en la mejilla y boca seria
CAMO = (156, 200, 106, 255)
CHARS[K + 'olef-tennant'] = {
    'body': 'normal', 'pal': pal('#9a8c6c', '#f6c494', iris='#2a2020', shade='#7c7056', deep='#5a5240', helm='#6a9a4a', helm_d='#527a38'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(10, 58), (90, 58)]},
    'front': [L([(22, 80), (25, 90), (36, 95), (50, 97), (64, 95), (75, 90), (78, 80)], 'mid', 'f', False, False, 3.6),
              L(outline([(2, 62), (4, 34), (18, 10), (50, -2), (82, 10), (96, 34), (98, 62), (50, 58)]), 'helm'),
              L(outline([(60, 0), (86, 14), (96, 38), (96, 60), (78, 40)]), 'helm_d', 'b', False)]
             + [L(cloud(x, y, 7, 5, 4, 0.3), CAMO, 'b', False) for x, y in ((26, 22), (50, 12), (70, 30), (40, 40), (84, 48), (14, 46))]
             + brows(68, (200, 70, 40, 255), 3.4, 15, 2.0, 12)
             + [L([(66, 86), (74, 94)], OUTC, 'f', False, False, 1.4), L([(74, 86), (66, 94)], OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(70, 80), (80, 96), (70, 104), (56, 102), (52, 90)]), 'mid', 'f', False),
             L(outline([(94, 58), (94, 32), (76, 6), (46, -2), (18, 8), (2, 34), (0, 64), (40, 62)]), 'helm'),
             L(outline([(2, 44), (30, 48), (40, 62), (2, 64)]), 'helm_d', 'b', False)] + [L(cloud(x, y, 7, 5, 4, 0.3), CAMO, 'b', False) for x, y in ((30, 20), (60, 14), (76, 36), (20, 48))],
    'back': [L(outline([(2, 64), (4, 34), (18, 10), (50, -2), (82, 10), (96, 34), (98, 64), (50, 66)]), 'helm'),
             L(outline([(58, 0), (86, 14), (96, 40), (96, 62), (66, 64)]), 'helm_d', 'b', False)]
            + [L(cloud(x, y, 7, 5, 4, 0.3), CAMO, 'b', False) for x, y in ((26, 22), (50, 12), (72, 30), (40, 44), (84, 50), (14, 48))],
}


def freckles(y=88, c=(160, 90, 50, 255)):
    return [L(ell(x, y + dy, 0.9, 0.9), c, 'f', False) for x, dy in ((22, 0), (26, 3), (30, 0), (70, 0), (74, 3), (78, 0))]


def pig_nose(y=88, c=(200, 120, 90, 255)):
    return [L(ell(50, y, 5, 3.2), c, 'f', ln=True), L(ell(47.6, y, 0.9, 1.2), OUTC, 'f', False), L(ell(52.4, y, 0.9, 1.2), OUTC, 'f', False)]


# Ollie Seeker: cara ancha y mofletuda de piel tostada; pelo verde oliva oscuro corto con el flequillo en mechones de punta;
# cejas gruesas verdes, nariz de cerdito y sonrisa
CHARS[K + 'ollie-seeker'] = {
    'body': 'corpulento', 'pal': pal('#4c5c2c', '#c8985a', iris='#2a2020', shade='#3a481e', deep='#2a3414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'face_front': WIDE, 'ear_out': 8,
             'hairline': [(10, 60), (14, 46), (30, 40), (50, 38), (70, 40), (86, 46), (90, 60)]},
    'front': crop('front', top=4, side=60, w=6) + [fr([(30, 44), (36, 36), (44, 52, 1), (48, 36), (54, 50, 1), (58, 36), (64, 46, 1), (66, 38), (50, 30)]),
                                                   strand([(40, 10), (50, 28)], 'deep', 'b', 1.2)] + brows(66, 'mid', 5.0, 16, 1.0, 15) + pig_nose(88, (170, 110, 70, 255)),
    'side': crop('side', top=2, nape=80, w=4) + brow_side(66, 'mid', 5.0, 1.0),
    'back': crop('back', top=4, nape=80, w=6),
}

# Ollie Twister: pelo rosa malva con un moño alto y erizado atado con una goma roja, y mechones finos que le caen por los
# lados de la cara hasta la mandíbula; ojos grandes redondos y sonrisa
CHARS[K + 'ollie-twister'] = {
    'body': 'normal', 'pal': pal('#c8a6b2', '#f6c494', iris='#2a2020', shade='#a8848e', deep='#86646e', band='#c03a24'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': crop('front', top=6, side=74, w=0) + [L(outline([(36, 2), (24, -18, 1), (40, -14), (44, -30, 1), (52, -16), (62, -28, 1), (62, -14), (78, -16, 1), (66, 2)])),
                                                   L(outline([(38, -4, 1), (62, -4, 1), (64, 6, 1), (36, 6, 1)], 2), 'band', 'b'),
                                                   L(outline([(16, 60), (12, 90), (16, 100, 1), (22, 86), (24, 64)])), L(outline([(84, 60), (88, 90), (84, 100, 1), (78, 86), (76, 64)])),
                                                   fr([(16, 64), (18, 36), (36, 18), (56, 18), (74, 24), (86, 42), (84, 62), (76, 50), (66, 44), (56, 54, 1), (52, 40), (40, 46), (30, 54), (24, 64, 1)])],
    'side': crop('side', top=4, nape=84) + [L(outline([(40, 0), (30, -20, 1), (46, -14), (52, -30, 1), (58, -14), (72, -20, 1), (62, 4)])),
                                            L(outline([(40, -6, 1), (62, -6, 1), (62, 4, 1), (40, 4, 1)], 2), 'band', 'b'), fr([(62, 40), (80, 20), (94, 40), (90, 60, 1), (80, 48)])],
    'back': crop('back', top=6, nape=86) + [L(outline([(36, 2), (24, -18, 1), (40, -14), (44, -30, 1), (52, -16), (62, -28, 1), (62, -14), (78, -16, 1), (66, 2)])),
                                            L(outline([(38, -4, 1), (62, -4, 1), (64, 6, 1), (36, 6, 1)], 2), 'band', 'b')],
}

# Olly Gammy: media melena lisa gris lavanda con raya en medio, recta por detrás y con un mechón largo a un lado hasta la
# mandíbula; ojos afilados y boca seria
CHARS[K + 'olly-gammy'] = {
    'body': 'normal', 'pal': pal('#9c8cac', '#f2b47a', iris='#2a2020', shade='#7c6e8c', deep='#5e526c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(14, 72), (17, 52), (30, 40), (50, 36), (70, 40), (83, 52), (86, 72)]},
    'front': crop('front', top=2, side=72, w=2) + [strand([(50, 4), (50, 38)], 'deep', 'b', 1.2), L(outline([(16, 58), (12, 92), (16, 104, 1), (22, 88), (22, 62)]))],
    'side': crop('side', top=0, nape=86, w=2),
    'back': crop('back', top=2, nape=88, w=2) + [strand([(50, 4), (50, 80)], 'deep', 'b', 1.0)],
}

# Olly Popman: grandullón de piel tostada y cara ancha; pelo rubio con flequillo recto cortado a tazón y los lados cortos;
# cejas rubias gruesas, pecas, nariz grande y sonrisa
CHARS[K + 'olly-popman'] = {
    'body': 'corpulento', 'pal': pal('#dcbc62', '#c8945a', iris='#2a2020', shade='#b89a44', deep='#8e742c'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE, 'ear_out': 8, 'nose': (50, 88, 5.0), 'hairline': [(10, 58), (90, 58)]},
    'front': [L(outline([(12, 60), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (88, 60), (50, 58)])),
              L(outline([(60, 2), (84, 12), (90, 36), (88, 58), (74, 40)]), 'shade', 'b', False)]
             + [strand([(x, 6 + abs(50 - x) * 0.3), (x + (x - 50) * 0.08, 56)], 'deep', 'b', 1.0) for x in (24, 38, 50, 62, 76)]
             + brows(66, 'mid', 5.0, 16, -1.0, 14) + freckles(88),
    'side': [L(outline([(88, 56), (90, 30), (70, 6), (40, 2), (14, 14), (4, 40), (8, 70), (28, 76), (40, 60), (60, 58)])),
             L(outline([(6, 44), (30, 48), (40, 62), (26, 76), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 74), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (88, 74), (50, 80)])),
             L(outline([(58, 2), (84, 12), (90, 40), (88, 74), (62, 78)]), 'shade', 'b', False)],
}

# Onslow Ball: piel muy clara y cara redonda y grande; pelo rubio claro con entradas, peinado hacia los lados; ojos afilados
# y sonrisa ancha
CHARS[K + 'onslow-ball'] = {
    'body': 'corpulento', 'pal': pal('#e2c67c', '#fbe2c8', iris='#2a2020', shade='#c4a85e', deep='#9a8240'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'face_front': WIDE, 'ear_out': 8, 'nose': (50, 88, 3.2),
             'hairline': [(10, 66), (14, 50), (24, 38), (36, 36), (50, 44), (64, 36), (76, 38), (86, 50), (90, 66)]},
    'front': crop('front', top=4, side=66, w=6) + [strand([(30, 10), (20, 40)], 'deep', 'b', 1.0), strand([(70, 10), (80, 40)], 'deep', 'b', 1.0)],
    'side': crop('side', top=2, nape=82, w=4) + [strand([(80, 24), (50, 12), (20, 26)], 'deep', 'b', 1.0)],
    'back': crop('back', top=4, nape=82, w=6),
}

# Orson Douvre (portero): un tupé castaño enorme que se adelanta hacia un lado, con un pañuelo verde atado detrás, y la melena
# ondulada hasta los hombros; piel clara, ojos afilados, nariz grande y labios en O
CHARS[K + 'orson-douvre'] = {
    'body': 'delgado', 'pal': pal('#8a5a2c', '#f8d4b0', iris='#2a2020', shade='#6c441e', deep='#4e3014', scarf='#5a8a6c', scarf_d='#466c54', lip='#e2a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 86, 3.4), 'hairline': [(14, 66), (17, 50), (30, 44), (50, 44), (70, 44), (83, 50), (86, 66)]},
    'front': longhair('front', length=110, flare=10, top=6, ends=4)
             + [L(outline([(40, 10), (70, 4), (92, 16), (92, 40), (84, 58), (76, 40), (60, 30)]), 'scarf'), L(outline([(84, 40), (100, 50, 1), (92, 60)]), 'scarf_d'),
                L(outline([(14, 50), (4, 30), (10, 4), (30, -12), (54, -10), (66, 4), (54, 14), (40, 24), (30, 40), (22, 56)])),
                L(outline([(30, -8), (54, -10), (64, 4), (50, 10), (36, 2)]), 'light', 'b', False),
                L(ell(50, 98, 4.4, 3.6), 'lip', 'f', ln=True), L([(47, 98), (53, 98)], OUTC, 'f', False, False, 1.0)],
    'side': longhair('side', length=110, flare=8, top=6) + [L(outline([(10, 30), (30, 6), (56, 4), (60, 26), (40, 36), (14, 44)]), 'scarf'),
                                                             L(outline([(56, 30), (66, 4), (90, -14), (110, -10, 1), (100, 4), (90, 28), (84, 44), (70, 40)]))],
    'back': longhair('back', length=110, flare=10, top=6, ends=4) + [L(outline([(20, 10), (50, 0), (80, 10), (88, 40), (50, 48), (12, 40)]), 'scarf'),
                                                                       L(outline([(44, 40), (50, 60, 1), (56, 40)]), 'scarf_d')],
}

# Ort Omaton (portero): pelo gris verdoso pegado y peinado hacia atrás, con una cresta en punta en el centro como una aleta;
# cara larga y cuadrada con arrugas, ojos azul grisáceo y boca seria
CHARS[K + 'ort-omaton'] = {
    'body': 'delgado', 'pal': pal('#a8ccc8', '#f2b47a', iris='#5a7a9a', shade='#86aca8', deep='#648a86'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'nose': (50, 88, 3.2),
             'face_front': blob([(18, 48), (50, 40), (82, 48), (84, 76), (82, 100), (66, 108), (50, 110), (34, 108), (18, 100), (16, 76)]),
             'hairline': [(16, 60), (18, 46), (30, 40), (50, 38), (70, 40), (82, 46), (84, 60)]},
    'front': crop('front', top=6, side=60, w=0, flat=6) + [L(outline([(44, 8), (50, -10, 1), (56, 8)])),
                                                           strand([(36, 10), (32, 34)], 'deep', 'b', 1.0), strand([(64, 10), (68, 34)], 'deep', 'b', 1.0),
                                                           L([(30, 66), (30, 72)], OUTC, 'f', False, False, 1.0), L([(70, 66), (70, 72)], OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=4, nape=80, flat=6) + [L(outline([(48, 4), (56, -12, 1), (64, 4)])), strand([(80, 22), (50, 12), (20, 24)], 'deep', 'b', 1.0)],
    'back': crop('back', top=6, nape=80, flat=6) + [L(outline([(44, 8), (50, -10, 1), (56, 8)]))],
}

# Oscar Esher (portero): capucha de bufón amarilla y verde que le tapa la cabeza, con dos orejas de punta a los lados como un
# perro; cara redonda morena, cejas grises, nariz de cerdito y sonrisa
CHARS[K + 'oscar-esher'] = {
    'body': 'normal', 'pal': pal('#e2b822', '#c8945a', iris='#2a2020', shade='#bc941a', deep='#8e6c10', green='#5c8a32', green_d='#466a24'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'ears': False, 'hairline': [(10, 60), (24, 54), (50, 52), (76, 54), (90, 60)]},
    'front': [L(outline([(8, 104), (2, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (98, 60), (92, 104), (82, 80), (82, 60), (18, 60), (18, 80)]), 'green'),
              L(outline([(12, 90), (8, 60), (14, 30), (30, 12), (50, 10), (70, 12), (86, 30), (92, 60), (88, 90), (80, 60), (20, 60)])),
              L(outline([(24, 16), (50, 40, 1), (76, 16), (50, 6)]), 'green'),
              L(outline([(20, 14), (-6, -4, 1), (-12, 20, 1), (8, 30)])), L(outline([(80, 14), (106, -4, 1), (112, 20, 1), (92, 30)])),
              L(outline([(60, 12), (86, 30), (92, 60), (88, 88), (80, 50)]), 'shade', 'b', False)]
             + brows(68, (190, 186, 176, 255), 3.0, 15, -1.6, 12) + pig_nose(90, (170, 110, 70, 255)),
    'side': [L(outline([(70, 44), (80, 22), (62, 2), (40, -4), (16, 8), (2, 40), (2, 90), (20, 110), (50, 104), (56, 80), (56, 62)]), 'green'),
             L(outline([(66, 40), (72, 22), (58, 8), (40, 4), (20, 14), (8, 40), (10, 84), (40, 80), (50, 62)])),
             L(outline([(30, 10), (16, -14, 1), (4, 6, 1), (16, 26)]))],
    'back': [L(outline([(8, 104), (2, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (98, 60), (92, 104), (50, 110)]), 'green'),
             L(outline([(12, 96), (8, 60), (14, 30), (30, 12), (50, 8), (70, 12), (86, 30), (92, 60), (88, 96), (50, 100)])),
             L(outline([(24, 14), (50, 50, 1), (76, 14), (50, 4)]), 'green'),
             L(outline([(20, 14), (-6, -4, 1), (-12, 20, 1), (8, 30)])), L(outline([(80, 14), (106, -4, 1), (112, 20, 1), (92, 30)]))],
}


# Oscar Petty (portero): peinado de samurái: la coronilla afeitada verde agua, el pelo oscuro de los lados pegado y un moño
# redondo en lo alto; cejas gruesas, ojos de punto y sonrisa
CHARS[K + 'oscar-petty'] = {
    'body': 'normal', 'pal': pal('#3c3a26', '#fbdcbc', iris='#2a2020', shade='#2c2a1a', deep='#1e1c10', bald='#c8eadc'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 66), (18, 46), (28, 34), (50, 30), (72, 34), (82, 46), (86, 66)]},
    'front': crop('front', top=4, side=66, w=0, shade=False) + [L(outline([(26, 34), (34, 12), (50, 6), (66, 12), (74, 34), (50, 28)]), 'bald', 'b', False),
                                                               L(ell(50, -2, 8, 7)), L(ell(48, -4, 3, 2), 'light', 'b', False)] + brows(64, DARK, 5.0, 15, 0.0, 14),
    'side': crop('side', top=2, nape=80, shade=False) + [L(outline([(70, 30), (66, 10), (50, 4), (34, 10), (30, 30), (50, 26)]), 'bald', 'b', False), L(ell(50, -2, 7, 7))]
            + brow_side(64, DARK, 5.0),
    'back': crop('back', top=4, nape=82, shade=False) + [L(outline([(28, 30), (34, 12), (50, 6), (66, 12), (72, 30), (50, 26)]), 'bald', 'b', False), L(ell(50, -2, 8, 7))],
}

# Owen Greenfield: un hombretón de cara larga y nariz grande, con el pelo crema casi blanco erizado en puntas que salen hacia
# los lados y hacia arriba; ojos blancos afilados y boca apretada
CHARS[K + 'owen-greenfield'] = {
    'body': 'corpulento', 'pal': pal('#efe6c6', '#f0b07a', iris='#f4f4f4', shade='#d4c8a2', deep='#b4a67c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'nose': (50, 86, 4.6),
             'face_front': blob([(16, 48), (50, 40), (84, 48), (88, 76), (84, 100), (66, 110), (50, 112), (34, 110), (16, 100), (12, 76)]),
             'hairline': [(14, 56), (18, 44), (30, 40), (50, 40), (70, 40), (82, 44), (86, 56)]},
    'front': crop('front', top=8, side=56, w=2) + [L(outline([(16, 44), (-8, 30, 1), (6, 28), (0, 10, 1), (20, 18), (24, -6, 1), (36, 8), (50, -10, 1), (62, 8), (78, -6, 1), (80, 18),
                                                             (100, 10, 1), (94, 28), (108, 30, 1), (84, 44), (70, 34), (30, 34)]))],
    'side': crop('side', top=6, nape=78, w=2) + [L(outline([(20, 30), (-6, 20, 1), (12, 10), (10, -6, 1), (30, 4), (44, -10, 1), (56, 4), (76, -4, 1), (76, 14), (94, 12, 1), (86, 30), (60, 26)]))],
    'back': crop('back', top=8, nape=78, w=2) + [L(outline([(16, 44), (-8, 30, 1), (6, 28), (0, 10, 1), (20, 18), (24, -6, 1), (36, 8), (50, -10, 1), (62, 8), (78, -6, 1), (80, 18),
                                                            (100, 10, 1), (94, 28), (108, 30, 1), (84, 44), (50, 40)]))],
}

# Pace Storey: grandullón de cara larga y ancha; pelo naranja con raya en medio, como un casco que se abre en las puntas sobre
# las orejas; ojos redondos, nariz larga y sonrisa ancha
CHARS[K + 'pace-storey'] = {
    'body': 'corpulento', 'pal': pal('#e27a2c', '#f2b47a', iris='#2a2020', shade='#bc5e1c', deep='#8e4410'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 86, 4.0), 'face_front': WIDE, 'ear_out': 8,
             'hairline': [(10, 62), (14, 48), (30, 40), (50, 44), (70, 40), (86, 48), (90, 62)]},
    'front': crop('front', top=2, side=62, w=8) + [L(outline([(6, 54), (0, 66, 1), (10, 62)])), L(outline([(94, 54), (100, 66, 1), (90, 62)])),
                                                   strand([(50, 4), (50, 40)], 'deep', 'b', 1.2), L(quad((34, 97), (50, 102), (66, 97)), OUTC, 'f', False, False, 1.8)],
    'side': crop('side', top=0, nape=80, w=6),
    'back': crop('back', top=2, nape=80, w=8) + [strand([(50, 4), (50, 70)], 'deep', 'b', 1.0)],
}

# Paddy Popper: pelo verde oscuro corto en pinchos, con un mechón largo que le baja por el centro de la frente hasta la nariz;
# nariz naranja postiza, ojos grandes y sonrisa de dientes
CHARS[K + 'paddy-popper'] = {
    'body': 'normal', 'pal': pal('#2a7a4a', '#f6c494', iris='#2a2020', shade='#1e5e38', deep='#144428', nose='#e88a2a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': [(14, 60), (18, 46), (30, 48), (40, 42), (50, 48), (60, 42), (72, 48), (82, 46), (86, 60)]},
    'front': messy('front', amp=10, n=10, seed=88, lo=58, rx=46, ry=38) + [fr([(40, 40), (50, 36), (58, 44), (54, 86, 1), (50, 60), (44, 50)]),
                                                                          L(ell(52, 87, 4.6, 3.6), 'nose', 'f', ln=True)],
    'side': messy('side', amp=10, n=9, seed=88, nape=82) + [fr([(66, 40), (86, 40), (90, 60), (88, 78, 1), (80, 56)]), L(ell(88, 87, 3.6, 3.4), 'nose', 'f', ln=True)],
    'back': messy('back', amp=10, n=10, seed=88, nape=84),
}

# Paddy Prunus (portero): piel morena y pelo rosa con un rizo enorme enroscado hacia arriba en lo alto de la cabeza, y
# mechones que caen por la frente; ojos entornados y boca abierta
CHARS[K + 'paddy-prunus'] = {
    'body': 'normal', 'pal': pal('#e2a0a2', '#c48a56', iris='#2a2020', shade='#c07e82', deep='#9a5e62', lip='#8a4a2e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': crop('front', top=8, side=68, w=4) + [L(outline([(40, 12), (44, -6), (60, -20), (70, -26, 1), (66, -12), (56, 0), (52, 12)])),
                                                   strand([(48, 6), (56, -8), (64, -18)], 'deep', 'b', 1.2),
                                                   fr([(16, 66), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (86, 66), (78, 52), (64, 46), (52, 60, 1), (48, 46), (36, 52), (24, 64, 1)]),
                                                   L(blob([(42, 96), (58, 96), (56, 101), (44, 101)], 4), 'lip', 'f', ln=True), L([(43, 98), (57, 98)], WHITE, 'f', False, False, 1.0)],
    'side': crop('side', top=6, nape=84, w=3) + [L(outline([(46, 8), (52, -8), (66, -22), (74, -26, 1), (70, -10), (60, 2), (58, 10)])), fr([(62, 40), (82, 22), (94, 40), (90, 60, 1), (80, 48)])],
    'back': crop('back', top=8, nape=86, w=4) + [L(outline([(40, 12), (44, -6), (60, -20), (70, -26, 1), (66, -12), (56, 0), (52, 12)]))],
}

# Paddy Rise: grandullón con un pañuelo naranja de cuadros amarillos atado a la cabeza, del que le salen mechones rubios
# en punta por los lados; ojos afilados y sonrisa torcida
CHARS[K + 'paddy-rise'] = {
    'body': 'corpulento', 'pal': pal('#f0d08e', '#f0b07a', iris='#2a3a5a', shade='#d4b06a', deep='#a8884a', scarf='#d8742a', scarf_d='#b45a1c', check='#f0c050'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'nose': (50, 86, 3.6), 'face_front': WIDE, 'ear_out': 8, 'hairline': [(10, 56), (90, 56)]},
    'front': [L(outline([(12, 62), (-4, 70, 1), (6, 56), (-6, 48, 1), (10, 46)])), L(outline([(88, 62), (104, 70, 1), (94, 56), (106, 48, 1), (90, 46)])),
              fr([(14, 52), (30, 50), (24, 64, 1), (38, 54), (40, 66, 1), (48, 52), (62, 54), (68, 64, 1), (72, 52), (84, 54)]),
              L(outline([(8, 56), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (92, 56), (50, 52)]), 'scarf'),
              L(outline([(60, 2), (86, 14), (94, 36), (92, 54), (76, 40)]), 'scarf_d', 'b', False)]
             + [strand([(x, 4 + abs(50 - x) * 0.3), (x + (x - 50) * 0.1, 54)], 'check', 'b', 1.6) for x in (28, 50, 72)]
             + [strand([(10, y), (50, y - 4), (90, y)], 'check', 'b', 1.6) for y in (24, 42)],
    'side': [L(outline([(40, 60), (20, 66, 1), (30, 54), (14, 50, 1), (34, 46)])),
             L(outline([(92, 54), (94, 30), (74, 4), (44, -2), (16, 10), (2, 34), (4, 56), (30, 60), (60, 54)]), 'scarf'),
             L(outline([(4, 40), (30, 44), (40, 58), (6, 58)]), 'scarf_d', 'b', False), L(outline([(4, 50), (-8, 64, 1), (4, 62), (-4, 74, 1), (12, 66)]), 'scarf_d')]
            + [strand([(x, 2 + abs(46 - x) * 0.3), (x - 2, 56)], 'check', 'b', 1.6) for x in (24, 48, 72)],
    'back': [L(outline([(12, 70), (-4, 76, 1), (6, 60), (94, 60), (104, 76, 1), (88, 70), (50, 76)])),
             L(outline([(8, 64), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (92, 64), (50, 60)]), 'scarf'),
             L(outline([(44, 60), (40, 84, 1), (50, 70), (60, 84, 1), (56, 60)]), 'scarf_d')]
            + [strand([(x, 4 + abs(50 - x) * 0.3), (x + (x - 50) * 0.1, 62)], 'check', 'b', 1.6) for x in (28, 50, 72)],
}

# Paddy Streehan (portero): piel morena y pelo verde oliva con raya en medio, recogido en dos moños bajos a los lados; ojos
# grandes amarillos y sonrisa
CHARS[K + 'paddy-streehan'] = {
    'body': 'normal', 'pal': pal('#7a7a3c', '#b8804e', iris='#c8b450', shade='#5e5e2a', deep='#42421c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 66), (17, 50), (30, 40), (50, 34), (70, 40), (83, 50), (86, 66)]},
    'front': [L(cloud(8, 64, 11, 12, 5, 0.3)), L(cloud(92, 64, 11, 12, 5, 0.5))] + crop('front', top=4, side=66, w=2) + [strand([(50, 6), (50, 32)], 'deep', 'b', 1.2)],
    'side': crop('side', top=2, nape=80, w=2) + [L(cloud(24, 66, 12, 12, 5))],
    'back': [L(cloud(10, 64, 11, 12, 5, 0.3)), L(cloud(90, 64, 11, 12, 5, 0.5))] + crop('back', top=4, nape=82, w=2) + [strand([(50, 6), (50, 70)], 'deep', 'b', 1.0)],
}

# Page Helper: piel morena y pelo verde lima corto y erizado; cejas lima gruesas fruncidas, ojos afilados y boca torcida
CHARS[K + 'page-helper'] = {
    'body': 'normal', 'pal': pal('#8ac852', '#b8804e', iris='#2a2020', shade='#6ca83a', deep='#4e8226'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'nose': (50, 87, 3.0),
             'hairline': [(14, 62), (18, 48), (30, 44), (50, 42), (70, 44), (82, 48), (86, 62)]},
    'front': messy('front', amp=7, n=12, seed=99, lo=60, rx=44, ry=40) + brows(66, 'mid', 5.0, 15, 2.6, 15),
    'side': messy('side', amp=7, n=11, seed=99, nape=80) + brow_side(66, 'mid', 5.0, 2.6),
    'back': messy('back', amp=7, n=12, seed=99, nape=82),
}


# Paisley Onepiece: pelo verde azulado oscuro ondulado y abultado, con puntas rizadas a los lados del cuello y un mechón
# naranja enroscado sobre un lado de la frente; cejas fruncidas y sonrisa
CHARS[K + 'paisley-onepiece'] = {
    'body': 'normal', 'pal': pal('#4a7a76', '#f2b47a', iris='#2a2020', shade='#3a605c', deep='#2a4644', lock='#e27a24', lock_d='#b45a14'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 3.2),
             'hairline': [(14, 62), (16, 48), (30, 42), (50, 44), (70, 40), (84, 46), (86, 62)]},
    'front': [L(cloud(50, 30, 48, 30, 9, 0.3)), L(cloud(10, 70, 10, 16, 4)), L(cloud(90, 70, 10, 16, 4, 0.5)),
              L(outline([(14, 70), (8, 40), (92, 40), (86, 70), (80, 50), (20, 50)])),
              L(outline([(60, 6), (90, 22), (96, 50), (90, 80), (82, 50)]), 'shade', 'b', False),
              fr([(50, 20), (64, 14), (78, 24), (82, 44), (80, 66, 1), (74, 50), (66, 40), (56, 34)], 'lock'),
              strand([(58, 22), (70, 30), (76, 48)], 'lock_d', 'f', 1.2)],
    'side': [L(cloud(44, 32, 46, 32, 9)), L(cloud(18, 74, 14, 18, 5)), L(outline([(66, 50), (82, 40), (90, 30), (10, 30), (4, 60), (30, 70), (44, 58)])),
             fr([(70, 20), (86, 26), (94, 44), (88, 58, 1), (80, 40)], 'lock')],
    'back': [L(cloud(50, 36, 50, 34, 9, 0.3)), L(cloud(50, 78, 40, 14, 7)),
             L(outline([(58, 8), (90, 24), (96, 54), (88, 84), (62, 88)]), 'shade', 'b', False)],
}

# Parker Leaper (portero): pelo castaño claro en pinchos largos que salen por encima de una cinta azul marino atada a la
# frente, con las puntas colgando por detrás; ojos grandes, cejas gruesas y sonrisa
CHARS[K + 'parker-leaper'] = {
    'body': 'normal', 'pal': pal('#9c7a3c', '#f2b47a', iris='#2a2020', shade='#7c5e2a', deep='#5a421c', band='#2c3c5c', band_d='#1e2a42'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(10, 58), (90, 58)]},
    'front': [L(outline([(10, 40), (-8, 20, 1), (14, 18), (16, -14, 1), (32, 6), (44, -8, 1), (54, 6), (78, -18, 1), (72, 6), (104, 4, 1), (86, 22), (106, 36, 1), (90, 40)])),
              L(outline([(56, 4), (78, -14), (74, 8), (96, 10), (88, 30), (70, 22)]), 'shade', 'b', False),
              L(outline([(8, 60), (6, 40), (50, 34), (94, 40), (92, 60), (50, 54)]), 'band'),
              L(outline([(40, 38), (44, 24), (52, 26), (56, 36), (48, 46, 1)]), 'mid', 'f')] + brows(66, DARK, 4.6, 15, 1.0, 14),
    'side': [L(outline([(30, 40), (6, 28, 1), (22, 18), (18, -8, 1), (40, 6), (52, -14, 1), (60, 6), (84, -10, 1), (80, 10), (100, 14, 1), (88, 36)])),
             L(outline([(94, 58), (94, 40), (50, 34), (4, 40), (4, 58), (50, 56)]), 'band'),
             L(outline([(8, 46), (-6, 66), (-2, 84, 1), (8, 64), (14, 54)]), 'band_d'), L(outline([(10, 50), (6, 76), (12, 90, 1), (16, 70)]), 'band')],
    'back': [L(outline([(10, 44), (-8, 24, 1), (14, 20), (16, -12, 1), (32, 8), (46, -8, 1), (56, 8), (78, -14, 1), (72, 8), (104, 6, 1), (88, 24), (106, 38, 1), (90, 44)])),
             L(outline([(12, 80), (8, 44), (92, 44), (88, 80), (50, 86)])),
             L(outline([(8, 60), (6, 42), (50, 38), (94, 42), (92, 60), (50, 58)]), 'band'),
             L(outline([(46, 56), (36, 80), (40, 92, 1), (50, 66)]), 'band_d'), L(outline([(52, 56), (62, 82), (58, 94, 1), (50, 66)]), 'band')],
}

# Pascal Blaise: piel clara y pelo verde grisáceo con raya en medio y un remolino arriba, que cae en melenita por los lados;
# gafas finas grises, ojos cerrados sonrientes y una sonrisa amable
CHARS[K + 'pascal-blaise'] = {
    'body': 'normal', 'pal': pal('#5c7e6c', '#fbdcb8', iris='#2a2020', shade='#486656', deep='#344c40'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'glasses': (120, 120, 124, 255), 'hairline': False},
    'front': longhair('front', length=80, flare=4, top=0, ends=3) + [L(outline([(46, 2), (50, -8, 1), (54, 2)])),
                                                                       fr([(14, 60), (14, 34), (30, 14), (50, 8), (70, 14), (86, 34), (86, 60), (80, 50), (72, 58, 1), (66, 46), (56, 54, 1), (50, 40),
                                                                           (44, 54, 1), (34, 46), (28, 58, 1), (20, 50)]),
                                                                       strand([(50, 8), (50, 30)], 'deep', 'f', 1.0)] + happy_eyes(76, 14, OUTC, 1.6),
    'side': longhair('side', length=80, flare=2, top=0) + [fr([(62, 30), (86, 30), (94, 50), (90, 62, 1), (80, 50)]), L(quad((76, 78), (82, 72), (88, 78)), OUTC, 'f', False, False, 1.6)],
    'back': longhair('back', length=80, flare=4, top=0, ends=4) + [L(outline([(46, 2), (50, -8, 1), (54, 2)]))],
}
