"""Goleadores del Callejón (vr-rojiura-backkicks): el Rojiura Backkicks de Victory Road, con sus modelos 3D de la
enciclopedia (英雄たちのヴィクトリーロード). Son todos personajes nuevos de VR, con una sola forma; varios salen en la
enciclopedia con ropa de calle (la cabeza es la misma y llevan la equipación del equipo). Ojo: en la wiki Shiwasu Naota
(cobb-hightail) tiene copiado el nombre japonés de Umino Choujuurou; su modelo es el de 師走直大."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import BROWN_LINE, WIDE, blush, brow_side, brows, crop  # noqa: F401
from chars_vr_nishinomiya import rect
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (24, 22, 24, 255)


def shades(view, y=76, c=BLACK, lens=(22, 22, 26, 255), w=1.6):
    """Gafas de sol: dos cristales grandes y oscuros."""
    if view == 'front':
        out = []
        for s in (1, -1):
            x0, x1 = 50 - s * 4, 50 - s * 27
            pts = [(x0, y - 5), (x1, y - 6), (x1 + s * 1, y + 3), (50 - s * 15, y + 7), (x0 - s * 1, y + 3)]
            out.append(L(blob(pts, 5), lens, 'f', False))
            out.append(L(blob(pts, 5) + [blob(pts, 5)[0]], c, 'f', False, False, w))
        out.append(L([(46, y - 4), (54, y - 4)], c, 'f', False, False, w))
        return out
    if view == 'side':
        pts = [(76, y - 5), (90, y - 5), (90, y + 3), (84, y + 7), (77, y + 3)]
        return [L(blob(pts, 5), lens, 'f', False), L([(50, y - 4), (76, y - 4)], c, 'f', False, False, w)]
    return []


def stubble(y=100, c=(120, 80, 60, 255)):
    return [L(ell(x, yy, 0.6, 0.6), c, 'f', False) for x, yy in ((38, y), (42, y + 2), (46, y + 3), (54, y + 3), (58, y + 2), (62, y), (44, y - 2), (56, y - 2))]


# Cobb Hightail (Shiwasu Naota, portero): grandullón de piel morena; la cabeza rapada gris con solo una tapa de pelo negro
# arriba, una tirita en la frente, ojos rojos redondos con ojeras y boca enfurruñada
BUZZ = (168, 160, 160, 255)
CHARS['cobb-hightail'] = {
    'body': 'corpulento', 'pal': pal('#262424', '#a8705a', iris='#a03030', shade='#1c1a1a', deep='#121010', buzz='#a8a0a0'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 60), (17, 46), (30, 40), (50, 38), (70, 40), (83, 46), (86, 60)]},
    'front': crop('front', top=10, side=62, w=1, c='buzz', shade=False, flat=6)
             + [L(outline([(20, 30), (22, 16), (50, 10), (78, 16), (80, 30), (50, 26)])), L(quad((24, 62), (34, 58), (42, 62)), OUTC, 'f', False, False, 2.0),
                L(quad((58, 62), (66, 58), (76, 62)), OUTC, 'f', False, False, 2.0),
                L([(62, 52), (74, 46), (77, 50), (65, 56)], (244, 236, 228, 255), 'f', ln=True)],
    'side': crop('side', top=8, nape=86, w=1, c='buzz', shade=False, flat=6)
            + [L(outline([(30, 12), (52, 6), (78, 10), (82, 22), (52, 20), (30, 22)])), L(quad((72, 62), (78, 58), (86, 60)), OUTC, 'f', False, False, 2.0)],
    'back': crop('back', top=10, nape=86, w=1, c='buzz', shade=False, flat=6) + [L(outline([(20, 28), (22, 16), (50, 10), (78, 16), (80, 28), (50, 32)]))],
}

# June Davidson: adulto; pelo castaño verdoso corto de punta hacia arriba con pico en la frente, barba y bigote del mismo
# color y gafas de sol negras
CHARS['june-davidson'] = {
    'body': 'normal', 'pal': pal('#7a7058', '#fcd2b4', iris='#2a2a2a', shade='#625a46', deep='#4a4434'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 1,
             'hairline': [(15, 64), (18, 48), (30, 42), (44, 46), (50, 56), (56, 46), (70, 42), (82, 48), (85, 64)]},
    'front': [L(outline([(16, 66), (12, 44), (16, 20), (30, 4), (44, -6), (50, -18, 1), (56, -6), (70, 4), (84, 20), (88, 44), (84, 66), (80, 50), (20, 50)])),
              L(outline([(56, -6), (72, 6), (86, 22), (88, 44), (82, 62), (76, 36)]), 'shade', 'b', False),
              strand([(36, 6), (40, 30)], 'deep', 'b', 1.0), strand([(64, 6), (60, 30)], 'deep', 'b', 1.0),
              L(outline([(19, 70), (22, 92), (34, 104), (50, 108), (66, 104), (78, 92), (81, 70), (78, 88), (64, 96), (60, 92), (50, 90), (40, 92), (36, 96), (22, 88)]), 'mid', 'f'),
              L(quad((40, 96), (50, 92), (60, 96)), (230, 210, 200, 255), 'f', False, False, 1.4)]
             + shades('front', 75),
    'side': [L(outline([(70, 50), (80, 44), (88, 30), (84, 6), (66, -8), (54, -18, 1), (42, -6), (22, 2), (8, 22), (4, 48), (10, 70), (22, 82), (34, 80), (38, 64),
                        (46, 56), (58, 52)])),
             L(outline([(4, 42), (30, 44), (44, 56), (36, 64), (34, 80), (22, 82), (10, 70)]), 'shade', 'b', False),
             L(outline([(58, 62), (64, 84), (76, 100), (86, 102), (90, 92), (80, 90), (70, 82), (62, 64)]), 'mid', 'f')]
            + shades('side', 75),
    'back': crop('back', top=0, nape=82, w=2)
            + [L(outline([(36, 6), (50, -16, 1), (64, 6)])), L([(14, 72), (19, 74)], BLACK, 'f', False, False, 2.0), L([(86, 72), (81, 74)], BLACK, 'f', False, False, 2.0)],
}

# Moray Delmar (Umino Choujuurou): pelo castaño muy oscuro, liso y largo hasta los hombros, con un pico agudo en medio de la
# frente; ojos cansados de párpados gruesos con ojeras, nariz de cerdito y boca recta; cara alargada
CHARS['moray-delmar'] = {
    'body': 'delgado', 'pal': pal('#4a3a36', '#fcd4b0', iris='#4a4a6a', shade='#3a2c2a', deep='#2a2020'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'nose': (50, 86, 2.6),
             'hairline': [(19, 110), (19, 48), (30, 40), (44, 40), (50, 56), (56, 40), (70, 40), (81, 48), (81, 110)]},
    'front': [L(outline([(12, 112, 1), (10, 70), (10, 30), (20, 6), (50, -4), (80, 6), (90, 30), (90, 70), (88, 112, 1), (82, 104), (82, 52), (18, 52), (18, 104)])),
              L(outline([(60, 0), (84, 10), (90, 34), (90, 70), (88, 108), (82, 100), (82, 50)]), 'shade', 'b', False),
              L(quad((26, 72), (34, 68), (44, 72)), OUTC, 'f', False, False, 3.0), L(quad((74, 72), (66, 68), (56, 72)), OUTC, 'f', False, False, 3.0),
              L(quad((26, 82), (35, 85), (44, 82)), OUTC, 'f', False, False, 1.8), L(quad((74, 82), (65, 85), (56, 82)), OUTC, 'f', False, False, 1.8),
              L(ell(48.4, 86.4, 0.7, 0.9), OUTC, 'f', False), L(ell(51.6, 86.4, 0.7, 0.9), OUTC, 'f', False)],
    'side': [L(outline([(70, 52), (82, 44), (88, 28), (82, 6), (60, -6), (34, -4), (14, 8), (4, 32), (2, 70), (-2, 110, 1), (14, 100), (24, 112, 1), (34, 92), (38, 70),
                        (44, 60), (50, 76, 1), (54, 56)])),
             L(outline([(2, 40), (30, 44), (42, 60), (36, 90), (14, 100), (0, 104)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 112, 1), (8, 70), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (92, 70), (90, 112, 1), (70, 106), (50, 112), (30, 106)])),
             L(outline([(56, 0), (82, 8), (92, 32), (92, 70), (90, 110), (64, 108), (58, 50)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x, 104)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Jazzmine Skylark (Amakura Maasa): gorro de lana rosa morado calado hasta las cejas, del que asoma una melena corta rubia
# ondulada a los lados con un mechón gris; ojos azules
BEANIE = (192, 112, 192, 255)
BEANIE_D = (150, 82, 150, 255)
CHARS['jazzmine-skylark'] = {
    'body': 'chica', 'pal': pal('#f0d890', '#fcdcc8', iris='#3a5a9a', shade='#d4bc72', deep='#b09a58'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 64), (6, 74), (-6, 80, 1), (4, 86), (0, 98, 1), (12, 94), (22, 100, 1), (24, 82)])),
              L(outline([(84, 64), (94, 74), (106, 80, 1), (96, 86), (100, 98, 1), (88, 94), (78, 100, 1), (76, 82)])),
              L(outline([(70, 60), (84, 60), (90, 72), (80, 76)]), (150, 150, 156, 255)),
              L(outline([(12, 66), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (88, 66), (50, 70)]), BEANIE),
              L(outline([(10, 54), (50, 58), (90, 54), (88, 68), (50, 72), (12, 68)]), BEANIE_D, 'b', ln=True),
              L(outline([(60, 6), (82, 16), (90, 38), (88, 54), (76, 40)]), BEANIE_D, 'b', False),
              L(outline([(20, 64), (30, 60), (40, 70), (32, 76, 1), (26, 70)]), 'mid', 'f')],
    'side': [L(outline([(36, 66), (24, 76), (12, 90, 1), (24, 88), (20, 100, 1), (36, 92), (46, 98, 1), (48, 78)])),
             L(outline([(80, 62), (90, 66), (92, 76), (84, 76)]), (150, 150, 156, 255)),
             L(outline([(84, 60), (90, 36), (80, 10), (50, 0), (22, 6), (6, 30), (4, 58), (20, 66), (50, 66)]), BEANIE),
             L(outline([(4, 46), (50, 52), (88, 50), (86, 62), (50, 66), (6, 60)]), BEANIE_D, 'b', ln=True)],
    'back': [L(outline([(16, 62), (2, 74), (-6, 82, 1), (6, 84), (2, 98, 1), (16, 94), (30, 100, 1), (40, 92), (50, 100, 1), (60, 92), (70, 100, 1), (84, 94), (98, 98, 1),
                        (94, 84), (106, 82, 1), (98, 74), (84, 62)])),
             L(outline([(12, 68), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (88, 68), (50, 72)]), BEANIE),
             L(outline([(10, 54), (50, 58), (90, 54), (88, 70), (50, 74), (12, 70)]), BEANIE_D, 'b', ln=True)],
}

# Caius Rushford (Hinode Rikiya): grandullón de cara ancha; pelo gris morado con pico en la frente en picos, recogido en una
# coleta gruesa que le cae por la espalda, y franjas de barba en las mejillas; dientes apretados y ceño
CHARS['caius-rushford'] = {
    'body': 'corpulento', 'pal': pal('#5a5070', '#e8c0a0', iris='#3a3a4a', shade='#483f5a', deep='#363044'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 62), (17, 44), (28, 40), (34, 30), (40, 40), (50, 26), (60, 40), (66, 30), (72, 40), (83, 44), (86, 62)]},
    'front': crop('front', top=4, side=64, w=2)
             + [L([(14, 80), (30, 96)], 'deep', 'f', False, False, 4.0), L([(86, 80), (70, 96)], 'deep', 'f', False, False, 4.0),
                L(quad((36, 54), (44, 58), (48, 52)), (200, 150, 130, 255), 'f', False, False, 1.0), L(quad((64, 54), (56, 58), (52, 52)), (200, 150, 130, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(26, 70), (10, 92), (-8, 116, 1), (8, 108), (22, 92), (36, 80)]))] + crop('side', top=2, nape=84, w=2)
            + [L([(62, 70), (76, 92)], 'deep', 'f', False, False, 4.0)],
    'back': [L(outline([(10, 112, 1), (8, 70), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (92, 70), (90, 112, 1), (70, 116), (50, 120, 1), (30, 116)])),
             L(outline([(56, 4), (80, 12), (90, 36), (92, 70), (90, 110), (64, 114), (58, 50)]), 'shade', 'b', False),
             strand([(30, 40), (26, 70), (30, 100)], 'deep', 'b', 1.0), strand([(50, 30), (50, 110)], 'deep', 'b', 1.0), strand([(70, 40), (74, 70), (70, 100)], 'deep', 'b', 1.0)],
}

# Noctis Dunn (Meidou Kazuomi): adulto; pelo gris plata largo peinado hacia atrás, que le cae ondulado por la nuca hasta los
# hombros; gafas de sol verdes y boca recta
CHARS['noctis-dunn'] = {
    'body': 'delgado', 'pal': pal('#bababa', '#fcd4b4', iris='#2a2a2a', shade='#9a9a9a', deep='#7a7a7a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 97,
             'hairline': [(19, 100), (19, 54), (28, 44), (50, 40), (72, 44), (81, 54), (81, 100)]},
    'front': [L(outline([(4, 112, 1), (10, 80), (10, 40), (18, 14), (50, 4), (82, 14), (90, 40), (90, 80), (96, 112, 1), (82, 100), (82, 56), (18, 56), (18, 100)])),
              L(outline([(60, 6), (84, 16), (90, 42), (90, 80), (92, 108), (82, 96), (82, 54)]), 'shade', 'b', False),
              strand([(30, 16), (24, 40), (22, 70)], 'deep', 'b', 1.0), strand([(70, 16), (76, 40), (78, 70)], 'deep', 'b', 1.0),
              strand([(44, 8), (36, 30)], 'deep', 'b', 1.0), strand([(56, 8), (64, 30)], 'deep', 'b', 1.0)]
             + shades('front', 77, BLACK, (32, 180, 150, 255)),
    'side': [L(outline([(80, 40), (88, 28), (86, 8), (60, -2), (30, 4), (12, 18), (4, 44), (-2, 80), (-14, 110, 1), (6, 100), (20, 112, 1), (30, 94), (38, 74), (44, 58),
                        (56, 48)])),
             L(outline([(4, 46), (30, 44), (44, 58), (30, 94), (6, 100)]), 'shade', 'b', False),
             strand([(80, 14), (50, 20), (20, 40)], 'deep', 'b', 1.0)]
            + shades('side', 77, BLACK, (32, 180, 150, 255)),
    'back': [L(outline([(6, 112, 1), (8, 70), (10, 36), (20, 10), (50, 2), (80, 10), (90, 36), (92, 70), (94, 112, 1), (70, 104), (50, 110), (30, 104)])),
             L(outline([(56, 4), (82, 12), (90, 38), (92, 70), (92, 108), (62, 106), (58, 50)]), 'shade', 'b', False)]
            + [strand([(x, 14), (x + (x - 50) * 0.2, 104)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Veril Golding (Kanabuchi Makoto, "Buchi"): piel tostada; los lados y la nuca negros y rapados y arriba un tupé verde menta
# echado hacia delante; gafas finas, ojos cansados, cejas fruncidas y barba de tres días
MINT = (90, 216, 192, 255)
MINT_D = (64, 176, 156, 255)
CHARS['veril-golding'] = {
    'body': 'normal', 'pal': pal('#1e1e1e', '#b07a54', iris='#3a4a7a', shade='#161616', deep='#0e0e0e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'ear_out': 2,
             'hairline': [(15, 64), (18, 48), (30, 46), (50, 46), (70, 46), (82, 48), (85, 64)]},
    'front': crop('front', top=8, side=66, w=1)
             + [L(outline([(8, 42), (10, 24), (24, 4), (50, -4), (76, 2), (90, 18), (92, 36), (80, 40), (50, 40), (20, 44)]), MINT, 'f', ln=True),
                L(outline([(56, 0), (78, 4), (90, 20), (90, 34), (72, 34)]), MINT_D, 'f', False),
                L(quad((24, 36), (50, 30), (76, 34)), MINT_D, 'f', False, False, 1.0)]
             + rect('front', 78, (90, 80, 70, 255), 1.2, 24, 45, 4, 4) + stubble(101),
    'side': crop('side', top=6, nape=86, w=1)
            + [L(outline([(94, 30), (88, 10), (66, -6), (40, -8), (20, 0), (12, 14), (20, 22), (50, 22), (80, 28)]), MINT, 'f', ln=True)]
            + rect('side', 78, (90, 80, 70, 255), 1.2, h0=4, h1=4),
    'back': crop('back', top=8, nape=86, w=1)
            + [L(outline([(20, 30), (24, 10), (50, 0), (76, 8), (90, 22), (84, 30), (60, 26), (40, 30)]), MINT, 'f', ln=True)],
}

# Holden Monday (Tsukigawara Gensaku): pelo azul marino peinado con raya a un lado y un mechón en curva sobre la frente;
# gafas finas doradas, ojos cerrados de sonrisa y una sonrisa enorme
GOLD = (190, 160, 90, 255)
CHARS['holden-monday'] = {
    'body': 'delgado', 'pal': pal('#22306a', '#fcd4b4', iris='#2a2a2a', shade='#1a2554', deep='#121a3e'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(16, 70), (10, 44), (14, 16), (30, 0), (50, -6), (72, 0), (88, 16), (92, 44), (86, 70), (80, 52), (20, 52)])),
              L(outline([(60, -2), (84, 12), (92, 40), (86, 66), (78, 30)]), 'shade', 'b', False),
              L(outline([(14, 56), (16, 34), (30, 20), (48, 16), (62, 20), (76, 30), (88, 46), (86, 60), (78, 46), (68, 40), (58, 38), (66, 54, 1), (52, 40), (38, 38), (26, 44)]), 'mid', 'f'),
              L(quad((36, 92), (50, 104), (64, 92)) + [(36, 92)], (255, 255, 255, 255), 'f', ln=True)]
             + rect('front', 76, GOLD, 1.2, 24, 45, 5, 4),
    'side': [L(outline([(76, 50), (88, 42), (94, 24), (86, 4), (62, -6), (36, -6), (14, 6), (4, 30), (2, 56), (10, 76), (24, 86), (36, 80), (38, 64), (46, 56), (60, 52)])),
             L(outline([(2, 42), (30, 46), (44, 58), (36, 80), (24, 86), (10, 74)]), 'shade', 'b', False),
             L(outline([(74, 20), (94, 30), (94, 46), (86, 52, 1), (82, 36)]), 'mid', 'f')]
            + rect('side', 76, GOLD, 1.2, h0=5, h1=4),
    'back': [L(outline([(18, 82), (10, 50), (14, 18), (30, 0), (50, -6), (70, 0), (86, 18), (90, 50), (82, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(58, -2), (82, 14), (90, 48), (82, 82), (66, 90), (60, 40)]), 'shade', 'b', False)],
}

# Frederick Brandt (Kajiwara Heiji, "Kaji"): melena rubia lacia en casco, con un flequillo largo de mechones que le tapa los
# ojos; barba de tres días y labios gruesos
CHARS['frederick-brandt'] = {
    'body': 'normal', 'pal': pal('#f0d880', '#fcd2b0', iris='#2a2a2a', shade='#d4ba62', deep='#b09848'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(14, 90), (8, 60), (8, 30), (20, 6), (50, -6), (80, 6), (92, 30), (92, 60), (86, 90), (82, 70), (18, 70)])),
              L(outline([(60, -2), (84, 8), (92, 34), (90, 66), (86, 86), (80, 40)]), 'shade', 'b', False),
              L(outline([(14, 74, 1), (16, 42), (30, 24), (50, 18), (70, 24), (84, 42), (86, 74, 1), (78, 68), (72, 82, 1), (64, 70), (56, 84, 1), (50, 72), (44, 84, 1), (36, 70),
                         (28, 82, 1), (22, 68)]), 'mid', 'f'),
              strand([(30, 26), (30, 60)], 'shade', 'f', 1.0), strand([(50, 20), (50, 62)], 'shade', 'f', 1.0), strand([(70, 26), (70, 60)], 'shade', 'f', 1.0),
              L(quad((40, 96), (50, 93), (60, 96)), (196, 120, 100, 255), 'f', False, False, 3.0)]
             + stubble(91, (150, 110, 80, 255)),
    'side': [L(outline([(74, 56), (86, 50), (92, 30), (84, 8), (60, -4), (34, -4), (14, 8), (4, 32), (2, 62), (8, 84), (14, 96, 1), (26, 88), (36, 84), (38, 66), (46, 58),
                        (60, 56), (68, 80, 1), (74, 60)])),
             L(outline([(2, 44), (30, 46), (44, 58), (36, 84), (14, 92), (6, 74)]), 'shade', 'b', False),
             L(outline([(74, 24), (92, 34), (94, 56), (88, 80, 1), (84, 60), (78, 44)]), 'mid', 'f')],
    'back': [L(outline([(14, 90), (8, 60), (8, 30), (20, 6), (50, -6), (80, 6), (92, 30), (92, 60), (86, 90), (70, 94), (56, 106, 1), (50, 96), (44, 106, 1), (30, 94)])),
             L(outline([(56, -2), (82, 8), (92, 32), (92, 60), (86, 90), (60, 96), (54, 40)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x, 92)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Bogdan Berglund (Kiyama Yoichi, "Moku"): pelo castaño oscuro corto de puntas, con pico en la frente; una barba cerrada
# por toda la mandíbula; orejas puntiagudas, ojos afilados, ceño fruncido y boca torcida
BEARD = (42, 28, 22, 255)
CHARS['bogdan-berglund'] = {
    'body': 'normal', 'pal': pal('#4a2e22', '#fcd0a8', iris='#3a4a6a', shade='#3a241a', deep='#2a1a12'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 2,
             'hairline': [(15, 62), (18, 46), (30, 40), (44, 42), (50, 52), (56, 42), (70, 40), (82, 46), (85, 62)]},
    'front': [L(outline([(16, 64), (12, 44), (16, 20), (26, 6), (36, 0), (40, -10, 1), (48, -2), (60, -10, 1), (64, 2), (78, 8), (88, 26), (88, 44), (84, 64), (80, 50),
                         (20, 50)])),
              L(outline([(60, -4), (78, 8), (88, 28), (86, 58), (76, 34)]), 'shade', 'b', False),
              L(outline([(19, 68), (20, 90), (32, 104), (50, 110), (68, 104), (80, 90), (81, 68), (76, 86), (64, 100), (58, 92), (50, 90), (42, 92), (36, 100), (24, 86)]), BEARD, 'f'),
              L(quad((40, 96), (50, 92), (60, 96)), (220, 170, 140, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(70, 50), (80, 44), (88, 28), (90, 10, 1), (78, 8), (74, -8, 1), (60, 0), (44, -6), (22, 2), (8, 22), (4, 48), (10, 70), (22, 82), (34, 80), (38, 64),
                        (46, 56), (58, 52)])),
             L(outline([(4, 42), (30, 44), (44, 56), (36, 64), (34, 80), (22, 82), (10, 70)]), 'shade', 'b', False),
             L(outline([(56, 60), (60, 84), (72, 102), (86, 104), (90, 94), (80, 92), (66, 80), (60, 60)]), BEARD, 'f')],
    'back': crop('back', top=0, nape=82, w=2) + [L(outline([(36, 4), (40, -10, 1), (50, 0), (60, -10, 1), (64, 4)]))],
}

# Saburo Mizuki ("Aniki"): grandullón de piel morena; una tapa plana de pelo azul marino arriba con los lados rapados; bigote
# negro grueso, perilla, ojos de párpado caído y la boca entreabierta
CHARS['saburo-mizuki'] = {
    'body': 'corpulento', 'pal': pal('#262c48', '#b07850', iris='#5a5a5a', shade='#1e223a', deep='#14182a', buzz='#7a5a44'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 60), (17, 44), (26, 38), (74, 38), (83, 44), (86, 60)]},
    'front': crop('front', top=10, side=62, w=2, c='buzz', shade=False, flat=8)
             + [L(outline([(12, 36), (14, 18), (30, 10), (50, 8), (70, 10), (86, 18), (88, 36), (50, 32)])),
                L(outline([(60, 10), (84, 16), (88, 34), (70, 32)]), 'shade', 'b', False),
                L(quad((26, 68), (35, 64), (44, 68)), OUTC, 'f', False, False, 2.2), L(quad((74, 68), (65, 64), (56, 68)), OUTC, 'f', False, False, 2.2),
                L(outline([(34, 94), (40, 88), (50, 87), (60, 88), (66, 94), (62, 96), (50, 92), (38, 96)]), BLACK, 'f'),
                L([(44, 99), (56, 99), (55, 102), (45, 102)], (150, 70, 60, 255), 'f', ln=True),
                L(ell(50, 108, 3, 1.6), BLACK, 'f', False)],
    'side': crop('side', top=8, nape=86, w=2, c='buzz', shade=False, flat=8)
            + [L(outline([(16, 22), (30, 8), (60, 6), (84, 14), (86, 28), (50, 26), (20, 30)])),
               L(outline([(80, 88), (88, 86), (92, 92), (86, 96)]), BLACK, 'f')],
    'back': crop('back', top=10, nape=86, w=2, c='buzz', shade=False, flat=8)
            + [L(outline([(12, 34), (14, 18), (30, 10), (50, 8), (70, 10), (86, 18), (88, 34), (50, 38)]))],
}

# Jaxon Taggart (Kunieda Daiju, portero): gorra negra calada con un botón gris en la frente; melena rosa roja lisa que le cae
# por debajo hasta los hombros y le tapa el ojo derecho; ojo afilado y boca seria
CAP = (40, 40, 42, 255)
CAP_D = (24, 24, 26, 255)
CHARS['jaxon-taggart'] = {
    'body': 'normal', 'pal': pal('#e05a6a', '#fcd8bc', iris='#3a3a5a', shade='#c04656', deep='#a03444'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'hairline': False},
    'front': [L(outline([(8, 112, 1), (8, 70), (12, 50), (88, 50), (92, 70), (92, 112, 1), (82, 104), (82, 60), (18, 60), (18, 104)])),
              L(outline([(14, 54), (16, 80), (26, 96), (34, 84), (44, 92, 1), (50, 64), (44, 56)]), 'mid', 'f'),
              L(outline([(12, 52), (12, 28), (24, 8), (50, 0), (76, 8), (88, 28), (88, 52), (50, 56)]), CAP),
              L(outline([(8, 50), (50, 54), (92, 50), (92, 58), (50, 62), (8, 58)]), CAP_D, 'b', ln=True),
              L(ell(50, 24, 7, 7), (190, 196, 200, 255), 'f', ln=True)],
    'side': [L(outline([(54, 60), (40, 110), (14, 116, 1), (4, 80), (6, 56)])),
             L(outline([(86, 52), (90, 30), (80, 8), (50, 0), (22, 6), (6, 30), (4, 56), (50, 58)]), CAP),
             L(outline([(70, 52), (104, 54), (104, 60), (70, 60)]), CAP_D, 'b', ln=True)],
    'back': [L(outline([(8, 112, 1), (6, 70), (10, 50), (90, 50), (94, 70), (92, 112, 1), (70, 108), (50, 112), (30, 108)])),
             L(outline([(56, 54), (90, 52), (94, 70), (92, 110), (64, 108)]), 'shade', 'b', False),
             L(outline([(12, 54), (12, 28), (24, 8), (50, 0), (76, 8), (88, 28), (88, 54), (50, 58)]), CAP),
             L(outline([(40, 54), (44, 44), (56, 44), (60, 54)]), (200, 60, 60, 255), 'f', ln=True)],
}

# Anson Barker (Tsuchigami Isamu): piel morena; una mata grande de pelo gris revuelto en pinchos que salen hacia todos los
# lados, más oscuro por debajo; ojillos negros y media sonrisa
CHARS['anson-barker'] = {
    'body': 'normal', 'pal': pal('#9a9a9a', '#9a6a4a', iris='#1e1e1e', shade='#7a7a7a', deep='#3a3a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(15, 64), (18, 50), (30, 46), (44, 44), (50, 50), (56, 44), (70, 46), (82, 50), (85, 64)]},
    'front': [L(outline([(16, 90), (6, 86, 1), (10, 76), (-6, 70, 1), (8, 62), (-8, 50, 1), (8, 44), (-2, 30, 1), (14, 26), (10, 10, 1), (26, 12), (28, -4, 1), (40, 6),
                         (48, -8, 1), (56, 4), (68, -6, 1), (70, 10), (86, 6, 1), (84, 22), (100, 26, 1), (90, 38), (106, 46, 1), (92, 54), (106, 66, 1), (92, 72), (96, 86, 1),
                         (84, 90), (80, 60), (20, 60)]), 'deep'),
              L(outline([(16, 60), (6, 54, 1), (10, 44), (-2, 30, 1), (14, 26), (10, 10, 1), (26, 12), (28, -4, 1), (40, 6), (48, -8, 1), (56, 4), (68, -6, 1), (70, 10),
                         (86, 6, 1), (84, 22), (100, 26, 1), (90, 38), (96, 52, 1), (84, 56), (80, 50), (20, 50)])),
              L(outline([(56, 4), (68, -6), (70, 10), (86, 6), (84, 22), (98, 26), (90, 38), (94, 50), (80, 44)]), 'shade', 'b', False),
              strand([(36, 12), (42, 28), (40, 44)], 'shade', 'b', 1.0), strand([(56, 10), (58, 26), (62, 44)], 'shade', 'b', 1.0)],
    'side': [L(outline([(70, 52), (80, 44), (86, 30), (94, 22, 1), (84, 14), (88, 0, 1), (72, 2), (70, -14, 1), (56, -2), (44, -12, 1), (36, 2), (20, 0, 1), (18, 14),
                        (2, 14, 1), (8, 28), (-8, 36, 1), (4, 46), (-8, 60, 1), (6, 64), (-2, 80, 1), (12, 80), (10, 96, 1), (24, 86), (36, 84), (38, 66), (46, 58), (58, 54)])),
             L(outline([(4, 46), (30, 46), (44, 58), (36, 84), (12, 90), (-2, 78), (6, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 92), (6, 88, 1), (10, 78), (-6, 72, 1), (8, 64), (-8, 52, 1), (8, 46), (-2, 30, 1), (14, 26), (10, 10, 1), (26, 12), (28, -4, 1), (40, 6),
                        (48, -8, 1), (56, 4), (68, -6, 1), (70, 10), (86, 6, 1), (84, 22), (100, 26, 1), (90, 38), (106, 48, 1), (92, 54), (106, 66, 1), (92, 72), (96, 88, 1),
                        (82, 92), (66, 96), (56, 108, 1), (50, 96), (44, 108, 1), (34, 96)])),
             L(outline([(56, 4), (68, -6), (70, 10), (86, 6), (84, 22), (98, 26), (90, 38), (104, 48), (92, 56), (104, 66), (92, 74), (94, 88), (66, 94), (60, 40)]), 'shade', 'b', False),
             L(outline([(20, 70), (80, 70), (78, 92), (50, 98), (22, 92)]), 'shade', 'b', False)],
}

# Deor Rummond (Nagamine Kingo): piel muy morena; una mata enorme de pelo negro en pinchos, con dos pinchos larguísimos que
# salen en horizontal a los lados; pintura roja alrededor de los ojos, cejas gruesas, ceño y barba de tres días
FACE_RED = (196, 52, 48, 255)
CHARS['deor-rummond'] = {
    'body': 'corpulento', 'pal': pal('#2a1a1a', '#7a4a34', iris='#a8b8c8', shade='#201414', deep='#160e0e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'face_front': WIDE, 'hairline': False},
    'front': [L(outline([(12, 86), (4, 80, 1), (10, 70), (-30, 64, 1), (6, 56), (-6, 44, 1), (8, 38), (-2, 22, 1), (14, 22), (12, 4, 1), (26, 12), (30, -4, 1), (40, 6),
                         (48, -8, 1), (56, 4), (66, -6, 1), (72, 8), (88, 4, 1), (86, 20), (102, 22, 1), (92, 36), (106, 44, 1), (94, 56), (130, 64, 1), (90, 70), (96, 80, 1),
                         (88, 86), (84, 60), (16, 60)])),
              L(outline([(56, 4), (66, -6), (72, 8), (88, 4), (86, 20), (100, 22), (92, 36), (104, 44), (92, 56), (84, 48)]), 'shade', 'b', False),
              L(outline([(14, 60), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (86, 60), (78, 52), (70, 58, 1), (62, 48), (54, 56, 1), (50, 46), (46, 56, 1), (38, 48),
                         (30, 58, 1), (22, 52)]), 'mid', 'f'),
              L(quad((22, 82), (34, 88), (46, 82)), FACE_RED, 'f', False, False, 3.4), L(quad((78, 82), (66, 88), (54, 82)), FACE_RED, 'f', False, False, 3.4),
              L([(19, 72), (22, 80)], FACE_RED, 'f', False, False, 3.0), L([(81, 72), (78, 80)], FACE_RED, 'f', False, False, 3.0),
              L([(24, 64), (44, 70)], BLACK, 'f', False, False, 4.0), L([(76, 64), (56, 70)], BLACK, 'f', False, False, 4.0)]
             + stubble(102, (60, 36, 26, 255)),
    'side': [L(outline([(70, 52), (80, 46), (88, 32), (96, 20, 1), (84, 16), (92, 0, 1), (74, 4), (70, -14, 1), (56, -2), (40, -16, 1), (34, 2), (14, -4, 1), (16, 14),
                        (-4, 14, 1), (6, 28), (-14, 38, 1), (4, 46), (-12, 62, 1), (6, 66), (0, 82, 1), (14, 82), (16, 98, 1), (26, 86), (36, 84), (38, 66), (46, 58), (58, 54)])),
             L(outline([(4, 44), (30, 46), (44, 58), (36, 84), (14, 92), (2, 78), (6, 66)]), 'shade', 'b', False),
             L(quad((72, 82), (80, 88), (88, 84)), FACE_RED, 'f', False, False, 3.4), L([(70, 64), (86, 68)], BLACK, 'f', False, False, 4.0)],
    'back': [L(outline([(16, 86), (4, 80, 1), (10, 70), (-30, 64, 1), (6, 56), (-6, 44, 1), (8, 38), (-2, 22, 1), (14, 22), (12, 4, 1), (26, 12), (30, -4, 1), (40, 6),
                        (48, -8, 1), (56, 4), (66, -6, 1), (72, 8), (88, 4, 1), (86, 20), (102, 22, 1), (92, 36), (106, 44, 1), (94, 56), (130, 64, 1), (90, 70), (96, 80, 1),
                        (84, 86), (66, 92), (50, 98, 1), (34, 92)])),
             L(outline([(56, 4), (66, -6), (72, 8), (88, 4), (86, 20), (100, 22), (92, 36), (104, 44), (92, 56), (124, 64), (88, 70), (84, 86), (66, 92), (60, 40)]), 'shade', 'b', False)],
}

# Drako Bonner (Mutsui Tatsunosuke): pelo azul petróleo oscuro peinado hacia arriba y atrás en un tupé, con las puntas
# levantadas; una marca roja en la frente, ojos afilados y boca seria
CHARS['drako-bonner'] = {
    'body': 'normal', 'pal': pal('#244e66', '#fcd2b0', iris='#2a2a3a', shade='#1c3e52', deep='#142e3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(15, 60), (18, 42), (28, 34), (50, 30), (72, 34), (82, 42), (85, 60)]},
    'front': [L(outline([(16, 62), (12, 40), (14, 18), (26, 2), (36, -6), (40, -22, 1), (48, -8), (60, -14), (66, -6), (80, -4, 1), (76, 6), (86, 18), (88, 40), (84, 62),
                         (80, 46), (20, 46)])),
              L(outline([(58, -10), (78, -4), (76, 8), (86, 20), (88, 40), (84, 56), (76, 30)]), 'shade', 'b', False),
              strand([(40, -4), (36, 14), (30, 30)], 'deep', 'b', 1.0), strand([(56, -6), (60, 14), (68, 30)], 'deep', 'b', 1.0),
              L([(46, 52), (50, 60), (54, 52)], FACE_RED, 'f', False, False, 1.4)],
    'side': [L(outline([(70, 48), (82, 42), (90, 26), (92, 6), (96, -12, 1), (82, -4), (66, -10), (40, -8), (18, 2), (6, 24), (2, 50), (8, 72), (20, 86), (34, 84), (38, 64),
                        (46, 56), (58, 52)])),
             L(outline([(2, 40), (30, 44), (44, 56), (36, 64), (34, 84), (20, 86), (8, 70)]), 'shade', 'b', False),
             strand([(88, 0), (60, 4), (30, 14)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 80), (12, 50), (14, 18), (28, 2), (40, -8), (36, -18, 1), (50, -10), (64, -16, 1), (66, -6), (80, 4), (88, 22), (88, 50), (82, 80), (66, 88),
                        (50, 90), (34, 88)])),
             L(outline([(58, -6), (80, 6), (88, 24), (88, 50), (82, 80), (66, 88), (60, 40)]), 'shade', 'b', False)],
}

# Chancer Cosgrave (Inseki Gouhei): grandullón de piel morena; pelo como una llama, crema por debajo con las puntas rojo
# anaranjado de pinchos hacia arriba y una mancha oscura en medio de la frente; ojos ámbar, cejas gruesas y boca abierta
FLAME = (224, 112, 80, 255)
CHARS['chancer-cosgrave'] = {
    'body': 'corpulento', 'pal': pal('#e8c890', '#9a6040', iris='#d09030', shade='#ccac74', deep='#3a2418'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 62), (17, 48), (28, 44), (40, 46), (50, 54), (60, 46), (72, 44), (83, 48), (86, 62)]},
    'front': [L(outline([(16, 64), (10, 44), (12, 22), (20, 10), (16, -4, 1), (28, 2), (32, -14, 1), (42, -2), (50, -18, 1), (58, -2), (68, -14, 1), (72, 2), (84, -4, 1),
                         (80, 10), (88, 22), (90, 44), (84, 64), (80, 50), (20, 50)])),
              L(outline([(16, -4), (28, 2), (32, -14), (42, -2), (50, -18), (58, -2), (68, -14), (72, 2), (84, -4), (80, 10), (66, 14), (50, 10), (34, 14), (20, 10)]), FLAME, 'b', False),
              L(outline([(40, 20), (50, 14), (60, 20), (58, 34), (50, 46), (42, 34)]), 'deep', 'b', False),
              L([(40, 98), (60, 98), (58, 104), (42, 104)], (120, 40, 40, 255), 'f', ln=True),
              L([(22, 64), (44, 70)], BLACK, 'f', False, False, 4.0), L([(78, 64), (56, 70)], BLACK, 'f', False, False, 4.0)],
    'side': [L(outline([(70, 50), (80, 44), (88, 30), (92, 12), (98, -2, 1), (84, 2), (82, -14, 1), (68, -4), (60, -20, 1), (48, -4), (36, -14, 1), (30, 2), (14, 6), (6, 26),
                        (4, 50), (10, 70), (22, 82), (34, 80), (38, 64), (46, 56), (58, 52)])),
             L(outline([(98, -2), (84, 2), (82, -14), (68, -4), (60, -20), (48, -4), (36, -14), (30, 2), (50, 10), (76, 12), (90, 14)]), FLAME, 'b', False),
             L(outline([(4, 42), (30, 44), (44, 56), (36, 64), (34, 80), (22, 82), (10, 70)]), 'shade', 'b', False),
             L([(70, 64), (86, 68)], BLACK, 'f', False, False, 4.0)],
    'back': [L(outline([(18, 78), (12, 44), (14, 22), (20, 8), (16, -6, 1), (28, 2), (32, -14, 1), (42, -2), (50, -18, 1), (58, -2), (68, -14, 1), (72, 2), (84, -6, 1),
                        (80, 8), (88, 22), (88, 44), (82, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(16, -6), (28, 2), (32, -14), (42, -2), (50, -18), (58, -2), (68, -14), (72, 2), (84, -6), (80, 10), (66, 18), (50, 14), (34, 18), (20, 10)]), FLAME, 'b', False),
             L(outline([(58, 16), (80, 12), (88, 26), (88, 46), (82, 76), (66, 84), (60, 40)]), 'shade', 'b', False)],
}
