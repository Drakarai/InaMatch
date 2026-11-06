"""Team K / Equipo D (IE3): con sus modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_firedragon import bowl
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)

# Indigo Lazuli (portero): pelo castaño en mechones gruesos y planos como tejas, abiertos en dos alas a los lados; cara
# ancha, ojos blancos de enfado y la boca seria
CHARS['indigo-lazuli'] = {
    'body': 'corpulento', 'pal': pal('#6a4a34', '#e0a060', shade='#4e3424'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'nose': (50, 86, 4), 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': bald('front') + [L(outline([(-12, 48), (-6, 30), (10, 32), (18, 14), (30, -2), (50, -8), (70, -2), (82, 14), (90, 32), (106, 30), (112, 48), (90, 50), (78, 38), (64, 40),
                                         (50, 30), (36, 40), (22, 38), (10, 50)]), 'mid', 'f', ln=True),
                              L(outline([(56, -4), (80, 10), (100, 34), (90, 46), (70, 30)]), 'shade', 'f', False),
                              strand([(30, 4), (40, 30)], 'shade', 'f', 1.2), strand([(60, 0), (54, 28)], 'shade', 'f', 1.2)]
             + white_eyes(76, 14, 6, 4.6, 2) + [L([(22, 66), (42, 72)], OUTC, 'f', False, False, 2.4), L([(78, 66), (58, 72)], OUTC, 'f', False, False, 2.4)],
    'side': bald('side') + [L(outline([(14, 60), (-6, 30), (6, 20), (2, 4, 1), (20, 6), (30, -8, 1), (44, 0), (60, -8), (80, 4), (90, 24), (70, 28), (46, 34), (28, 50)]), 'mid', 'f', ln=True)]
            + side_eye(76),
    'back': bald('back') + [L(outline([(-14, 46), (-6, 26), (10, 30), (18, 10), (40, -4), (60, -4), (82, 10), (90, 30), (106, 26), (114, 46), (90, 54), (84, 80), (50, 88), (16, 80), (10, 54)]),
                              'mid', 'f', ln=True)],
}
# Roseo Diamante: pelo rosa en media melena lisa con raya a un lado y las puntas abiertas en la nuca y las sienes; cara
# pálida, ojos negros rasgados y la boca seria
CHARS['roseo-diamante'] = {
    'body': 'delgado', 'pal': pal('#e898b0', '#fce8d8', iris='#1e1e1e', shade='#c07890'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(14, 68), (18, 46), (34, 34), (50, 40), (66, 34), (82, 46), (86, 68)]},
    'front': longhair('front', 92, 12, top=-2, part=True)
             + [L(outline([(16, 46), (4, 30, 1), (22, 32), (36, 34)]), 'mid', 'f', ln=True), L(outline([(84, 46), (96, 30, 1), (78, 32), (64, 34)]), 'mid', 'f', ln=True)],
    'side': longhair('side', 92, 10, top=-2),
    'back': longhair('back', 92, 12, top=-2, ends=3),
}
# Azubel Turchese: un gorro abultado naranja rojizo con una cinta crema ancha, calado hasta los ojos; un antifaz negro de
# ladrón sobre los ojos blancos, pecas y la boca torcida
CHARS['azubel-turchese'] = {
    'body': 'corpulento', 'pal': pal('#c8501e', '#f0b070', hat='#c8501e', hat_d='#9a3a14', band='#e8d090', freckle='#a8603a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(4, 60), (0, 30), (10, 6), (40, -6), (70, -4), (92, 8), (100, 32), (96, 60), (50, 58)]), 'hat', 'f', ln=True),
              L(outline([(56, -2), (90, 10), (98, 34), (94, 56), (70, 52)]), 'hat_d', 'f', False),
              L(outline([(6, 62), (6, 48), (50, 44), (94, 48), (94, 62), (50, 58)]), 'band', 'f', ln=True),
              L(outline([(16, 66), (34, 62), (50, 70), (66, 62), (84, 66), (80, 80), (64, 80), (50, 74), (36, 80), (20, 80)]), OUTC, 'f', False),
              L(ell(34, 72, 4, 3.6), WHITE, 'f', False), L(ell(66, 72, 4, 3.6), WHITE, 'f', False),
              L(ell(34, 72, 1.6, 1.6), OUTC, 'f', False), L(ell(66, 72, 1.6, 1.6), OUTC, 'f', False)]
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((24, 88), (28, 90), (72, 90), (76, 88))],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(2, 64), (0, 30), (14, 6), (46, -6), (80, -2), (98, 16), (100, 40), (96, 54), (60, 52), (30, 64)]), 'hat', 'f', ln=True),
             L(outline([(4, 54), (4, 42), (98, 40), (98, 52)]), 'band', 'f', ln=True), L(outline([(74, 64), (94, 62), (94, 78), (78, 78)]), OUTC, 'f', False)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(2, 76), (0, 30), (12, 6), (40, -6), (70, -4), (92, 8), (102, 32), (100, 76), (50, 80)]), 'hat', 'f', ln=True),
             L(outline([(4, 56), (50, 50), (98, 56), (98, 68), (50, 62), (4, 68)]), 'band', 'f', ln=True)],
}
# Nello Agata: pelo castaño muy oscuro en un casquete con forma de V que se abre en dos alas puntiagudas a los lados; cejas
# negras gruesas en punta, ojos blancos de furia, nariz redonda y la boca torcida
CHARS['nello-agata'] = {
    'body': 'normal', 'pal': pal('#3a3430', '#f8c080', shade='#28241e', lip='#c8705a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'nose': (50, 84, 4), 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': bald('front') + [L(outline([(-6, 50, 1), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (106, 50, 1), (80, 44), (64, 40), (50, 56, 1), (36, 40), (20, 44)]), 'mid', 'f', ln=True),
                              L(outline([(56, 6), (80, 24), (100, 46), (76, 40)]), 'shade', 'f', False)]
             + white_eyes(74, 14, 6, 5, 2.4) + [L([(22, 62), (42, 70)], OUTC, 'f', False, False, 2.8), L([(78, 62), (58, 70)], OUTC, 'f', False, False, 2.8),
                                                L(outline([(36, 98), (50, 94), (64, 98), (60, 104), (40, 104)]), 'lip', 'f', ln=True)],
    'side': bald('side') + [L(outline([(-6, 50, 1), (10, 30), (24, 10), (50, 2), (78, 8), (92, 24), (70, 28), (44, 34), (26, 44)]), 'mid', 'f', ln=True)] + side_eye(74),
    'back': bald('back') + [L(outline([(-10, 44, 1), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (110, 44, 1), (84, 50), (70, 60), (50, 64), (30, 60), (16, 50)]), 'mid', 'f', ln=True)],
}
# Azzurro Zaffiro: una mata enorme de pelo magenta en ondas abultadas que le cae hasta las cejas; ojos de sueño con pestañas,
# arrugas y la boca torcida en una mueca
CHARS['azzurro-zaffiro'] = {
    'body': 'normal', 'pal': pal('#b03a6a', '#f8c890', shade='#8a2a52', light='#d06a90'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(8, 76), (-4, 50), (-4, 24), (10, 4), (36, -10), (66, -10), (90, 4), (104, 24), (104, 50), (92, 76), (82, 60), (66, 50), (50, 56), (34, 50), (18, 60)])),
              L(outline([(60, -6), (88, 6), (102, 30), (98, 60), (84, 56), (74, 26)]), 'shade', 'b', False),
              L(outline([(14, 30), (30, 14), (50, 14), (40, 24), (24, 36)]), 'light', 'b', False)],
    'side': [L(outline([(44, 92), (22, 88), (2, 70), (-6, 40), (6, 10), (36, -8), (70, -6), (92, 10), (98, 34), (90, 50), (70, 48), (56, 56), (52, 70), (50, 82)])),
             L(outline([(0, 44), (34, 44), (42, 84), (16, 84)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 84), (-4, 50), (-4, 24), (10, 4), (36, -10), (66, -10), (90, 4), (104, 24), (104, 50), (94, 84), (50, 92)])),
             L(outline([(56, -6), (88, 6), (102, 34), (98, 80), (64, 88)]), 'shade', 'b', False)],
}
# Pardo Berillo: pelo verde azulado oscuro de pinchos largos echados a un lado, con un mechón grande que le cae sobre un ojo;
# el otro ojo blanco de enfado y una media sonrisa de colmillo
CHARS['pardo-berillo'] = {
    'body': 'normal', 'pal': pal('#1e4a44', '#f8c080', shade='#143630'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 13, 9, seed=1801, rx=54, ry=42, cy=40, lo=80, sweep=-0.6)
             + [L(outline([(10, 74, 1), (14, 42), (30, 24), (54, 18), (76, 24), (88, 38), (90, 54), (78, 46), (62, 48), (50, 58), (42, 78, 1), (36, 60), (24, 68, 1), (18, 56)]), 'mid', 'f', ln=True)]
             + [L(outline([(58, 74), (76, 72), (74, 80), (60, 80)]), WHITE, 'f', ln=True), L(ell(66, 76, 1.6, 2), OUTC, 'f', False)],
    'side': messy('side', 20, 8, seed=1801, rx=50, ry=42, cy=40, nape=96, sweep=-0.8),
    'back': messy('back', 13, 9, seed=1801, rx=54, ry=42, cy=40, nape=98, sweep=0.4),
}
# Beldio Smeraldo: pelo verde lima con un mechón largo que le baja por la frente y rodea los ojos como unas gafas, un penacho
# de hojas atado en lo alto y dos pinchos a los lados; ojos naranjas de enfado
CHARS['beldio-smeraldo'] = {
    'body': 'normal', 'pal': pal('#8ac83a', '#f8c080', iris='#d0601a', shade='#6a9a28', leaf='#5a8a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': (50, 40)},
    'front': [L(outline([(50, 6), (36, -8), (22, -14, 1), (40, -14), (46, -26, 1), (52, -14), (62, -26, 1), (62, -12), (80, -16, 1), (64, -4)]), 'leaf', 'b', ln=True),
              L(outline([(16, 60), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (84, 60), (80, 50), (20, 50)])),
              L(outline([(60, 6), (82, 18), (86, 46), (76, 36)]), 'shade', 'b', False),
              L(outline([(14, 54), (-4, 50, 1), (16, 46)]), 'mid', 'f', ln=True), L(outline([(86, 54), (104, 50, 1), (84, 46)]), 'mid', 'f', ln=True),
              L(quad((48, 6), (44, 40), (40, 66)), 'mid', 'f', False, False, 3),
              L(ell(34, 76, 11, 8) + [ell(34, 76, 11, 8)[0]], 'mid', 'f', False, False, 2.6), L(ell(66, 76, 11, 8) + [ell(66, 76, 11, 8)[0]], 'mid', 'f', False, False, 2.6)],
    'side': [L(outline([(54, 2), (50, -14), (54, -28, 1), (62, -12), (62, 2)]), 'leaf', 'b', ln=True),
             L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 8), (52, 0), (78, 8), (92, 26), (88, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False), L(ell(84, 76, 8, 8) + [ell(84, 76, 8, 8)[0]], 'mid', 'f', False, False, 2.6)],
    'back': [L(outline([(50, 6), (36, -8), (22, -14, 1), (40, -14), (46, -26, 1), (52, -14), (62, -26, 1), (62, -12), (80, -16, 1), (64, -4)]), 'leaf', 'b', ln=True),
             L(outline([(14, 84), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (86, 84), (50, 90)])),
             L(outline([(20, 50), (50, 40), (86, 50), (86, 82), (50, 90), (14, 82)]), 'shade', 'b', False),
             L(outline([(14, 54), (-4, 50, 1), (16, 46)]), 'mid', 'f', ln=True), L(outline([(86, 54), (104, 50, 1), (84, 46)]), 'mid', 'f', ln=True)],
}
# Rosso Granato: piel morena; pelo blanco rosado peinado hacia atrás en ondas, con un mechón grande que le cae en punta por
# el medio de la cara entre los ojos; ojos rojos de enfado
CHARS['rosso-granato'] = {
    'body': 'normal', 'pal': pal('#f0dcdc', '#b07848', iris='#b01e2a', shade='#c8b0b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (50, 40)},
    'front': [L(outline([(14, 66), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (86, 66), (82, 56), (18, 56)])),
              L(outline([(60, 4), (84, 16), (90, 40), (86, 62), (76, 36)]), 'shade', 'b', False),
              L(outline([(44, 8), (56, 8), (60, 50), (50, 92, 1), (40, 50)]), 'mid', 'f', ln=True), L(outline([(50, 10), (56, 12), (56, 50), (50, 80)]), 'shade', 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 8), (52, 0), (78, 8), (92, 26), (90, 40), (96, 70, 1), (84, 48), (70, 44), (58, 50), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 84), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (86, 84), (60, 88), (50, 96, 1), (40, 88)])),
             L(outline([(56, 4), (84, 16), (90, 44), (86, 82), (64, 88)]), 'shade', 'b', False)],
}
# Giallo Topazio: pelo amarillo en forma de cono alto y liso que le tapa los ojos, rematado abajo por una fila de rizos en
# espiral; una sonrisa enorme de dientes
CHARS['giallo-topazio'] = {
    'body': 'normal', 'pal': pal('#e8d040', '#fcd8b0', shade='#b8a02a', curl='#b89a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(6, 70), (10, 40), (30, 6), (50, -30, 1), (70, 6), (90, 40), (94, 70), (70, 76), (50, 70), (30, 76)]), 'mid', 'f', ln=True),
              L(outline([(54, -20), (70, 6), (90, 40), (92, 66), (70, 70), (64, 20)]), 'shade', 'f', False)]
             + [L(ell(x, y, 8, 8), 'curl', 'f', ln=True) for x, y in ((4, 64), (20, 72), (80, 72), (96, 64))]
             + [L(ell(x, y, 3.4, 3.4) + [ell(x, y, 3.4, 3.4)[0]], OUTC, 'f', False, False, 1.0) for x, y in ((4, 64), (20, 72), (80, 72), (96, 64))]
             + [L(outline([(24, 88), (50, 94), (76, 88), (68, 102), (50, 108), (32, 102)]), WHITE, 'f', ln=True), L(quad((26, 92), (50, 100), (74, 92)), OUTC, 'f', False, False, 1.0)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(10, 70), (12, 40), (34, 4), (54, -30, 1), (74, 4), (92, 40), (96, 64), (60, 70), (30, 74)]), 'mid', 'f', ln=True)]
            + [L(ell(x, 68, 8, 8), 'curl', 'f', ln=True) for x in (10, 26, 42, 58, 74)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(6, 70), (10, 40), (30, 6), (50, -30, 1), (70, 6), (90, 40), (94, 70), (50, 76)]), 'mid', 'f', ln=True),
             L(outline([(56, -14), (72, 8), (90, 40), (92, 68), (64, 72)]), 'shade', 'f', False)]
            + [L(ell(x, 72, 9, 8), 'curl', 'f', ln=True) for x in (6, 22, 40, 60, 78, 94)],
}
# Violetto Ametista: melena gris lila lisa y larga hasta el pecho, peinada hacia atrás con una diadema crema ancha; cejas
# claras, ojos azules y la boca seria
CHARS['violetto-ametista'] = {
    'body': 'delgado', 'pal': pal('#b0a0b8', '#fce4c8', iris='#2a6ab0', shade='#8a7e94', band='#f8ecd8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (46, 40)},
    'front': longhair('front', 122, 6, top=-6) + [L(outline([(14, 52), (16, 40), (50, 34), (84, 40), (86, 52), (50, 46)]), 'band', 'f', ln=True)]
             + [strand([(x, -2), (x, 34)], 'shade', 'b', 1.0) for x in (30, 42, 58, 70)],
    'side': longhair('side', 122, 6, top=-6) + [L(outline([(52, 46), (54, 34), (90, 36), (90, 46)]), 'band', 'f', ln=True)],
    'back': longhair('back', 122, 6, top=-6, ends=4),
}
# Bianco Perla: pelo verde salvia corto con las sienes cortas y un tupé grande que se levanta en punta hacia un lado; cara
# alargada, ojos verdes y una media sonrisa
CHARS['bianco-perla'] = {
    'body': 'normal', 'pal': pal('#a8b090', '#fcd0a8', iris='#5a7a2a', shade='#7e8a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG_FACE, 'nose': (50, 88, 3), 'hairline': False},
    'front': bald('front') + buzz('front', front_y=40)
             + [L(outline([(16, 40), (20, 18), (40, 6), (70, 2), (96, -10, 1), (84, 10), (90, 18, 1), (80, 30), (60, 36), (40, 40)]), 'mid', 'f', ln=True)],
    'side': bald('side') + buzz('side') + [L(outline([(30, 20), (50, 4), (80, 0), (104, -10, 1), (92, 10), (70, 16), (50, 22)]), 'mid', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=84) + [L(outline([(16, 20), (6, -6, 1), (24, 4), (30, -16, 1), (40, 6)]), 'mid', 'f', ln=True)],
}
# Giulio Acuto: el pelo castaño en trenzas pegadas que se recogen en un moño trenzado atrás; unas gafas de aviador rojas con
# lentes negras sobre los ojos y una sonrisa
CHARS['giulio-acuto'] = {
    'body': 'normal', 'pal': pal('#8a7230', '#f8c088', shade='#6a5420', band='#c81e2a', lens='#1e1e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': bald('front') + buzz('front', front_y=46) + [strand([(x, 6), (x + (x - 50) * 0.2, 46)], 'shade', 'f', 1.4) for x in (26, 38, 50, 62, 74)]
             + [L(outline([(12, 68), (50, 62), (88, 68), (88, 82), (50, 76), (12, 82)]), 'band', 'f', ln=True),
                L(ell(34, 74, 7, 6.4), WHITE, 'f', ln=True), L(ell(66, 74, 7, 6.4), WHITE, 'f', ln=True),
                L(ell(34, 74, 4.6, 4.2), 'lens', 'f', False), L(ell(66, 74, 4.6, 4.2), 'lens', 'f', False)],
    'side': bald('side') + buzz('side') + [L(outline([(48, 68), (96, 68), (96, 80), (50, 80)]), 'band', 'f', ln=True), L(ell(90, 74, 5, 6), 'lens', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=80) + [L(ell(50, 64, 16, 14), 'mid', 'f', ln=True)] + [strand([(x, 4), (50, 56)], 'shade', 'f', 1.4) for x in (20, 34, 66, 80)]
            + [L(quad((8, 70), (50, 64), (92, 70)), 'band', 'f', False, False, 3)],
}
# Grigio Quarzo (portero suplente): cara enorme y pálida de nariz gorda y mandíbula marcada; pelo castaño oscuro muy corto
# arriba que se abre a los lados de la nuca en dos matas rizadas; ojos de sueño con pestañas y la boca en una raya
CHARS['grigio-quarzo'] = {
    'body': 'corpulento', 'pal': pal('#3a3628', '#fce0c8', shade='#28241a', nose='#f0b090', jaw='#e0a070'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 8},
    'front': bald('front') + buzz('front', front_y=24)
             + [L(outline([(10, 76), (-6, 80), (-8, 92), (6, 96), (14, 88)]), 'mid', 'f', ln=True), L(outline([(90, 76), (106, 80), (108, 92), (94, 96), (86, 88)]), 'mid', 'f', ln=True),
                L(quad((24, 72), (32, 76), (40, 72)), OUTC, 'f', False, False, 2), L(quad((60, 72), (68, 76), (76, 72)), OUTC, 'f', False, False, 2),
                L(outline([(36, 76), (64, 76), (70, 96), (30, 96)]), 'nose', 'f', ln=True),
                L(outline([(28, 100), (72, 100), (70, 116), (30, 116)]), 'jaw', 'f', ln=True), L([(34, 106), (66, 106)], OUTC, 'f', False, False, 1.2)],
    'side': bald('side') + buzz('side') + [L(outline([(24, 76), (6, 78), (2, 92), (18, 98), (30, 90)]), 'mid', 'f', ln=True), L(outline([(84, 76), (104, 96), (88, 98)]), 'nose', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=74) + [L(outline([(-6, 74), (106, 74), (110, 92), (96, 100), (4, 100), (-10, 92)]), 'mid', 'f', ln=True)],
}
# Marrone Corniola: pelo crema cortado en forma de seta, liso y abombado, que le cae hasta las cejas; piel morena, ojos verdes
# grandes de enfado y la boca en una O pequeña
CHARS['marrone-corniola'] = {
    'body': 'normal', 'pal': pal('#e8e0c0', '#a8703e', iris='#4a8a3a', shade='#c0b898'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(-4, 66), (-2, 40), (14, 10), (50, -6), (86, 10), (102, 40), (104, 66), (80, 60), (50, 62), (20, 60)]), 'mid', 'f', ln=True),
              L(outline([(56, -2), (88, 12), (100, 40), (100, 62), (70, 60)]), 'shade', 'f', False)]
             + [strand([(x, -2 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 60)], 'shade', 'f', 1.0) for x in (16, 32, 50, 68, 84)]
             + [L(ell(50, 96, 3.4, 3), (120, 40, 40, 255), 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(-6, 70), (-6, 40), (10, 8), (50, -6), (86, 6), (102, 30), (104, 56), (70, 60), (40, 64)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-4, 66), (-2, 40), (14, 10), (50, -6), (86, 10), (102, 40), (104, 66), (50, 70)]), 'mid', 'f', ln=True),
             L(outline([(10, 66), (90, 66), (86, 84), (50, 88), (14, 84)]), 'shade', 'b', ln=True)],
}
# Amaranto Rubino: pelo rojo de pinchos largos hacia arriba y a los lados en forma de llama; cara alargada, ojos azules de
# enfado y la boca seria
CHARS['amaranto-rubino'] = {
    'body': 'normal', 'pal': pal('#c81e1e', '#fcd0a8', iris='#3a6aa8', shade='#9a1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': (52, 44)},
    'front': [L(outline([(14, 66), (12, 44), (-10, 40, 1), (8, 30), (14, 8), (22, -14, 1), (34, 0), (44, -22, 1), (52, -2), (60, -20, 1), (66, 2), (78, -6, 1), (84, 12), (90, 30),
                         (110, 40, 1), (88, 44), (86, 66), (80, 56), (20, 56)])),
              L(outline([(56, -4), (60, -16, 1), (68, 4), (80, 0, 1), (88, 30), (100, 40, 1), (84, 46), (74, 24)]), 'shade', 'b', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-6, 50, 1), (10, 42), (6, 22), (-6, 8, 1), (16, 8), (22, -14, 1), (36, 0), (50, -20, 1), (58, 2), (76, 4), (90, 24), (84, 40),
                        (68, 44), (56, 52), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 84), (12, 44), (-10, 40, 1), (8, 30), (14, 8), (22, -14, 1), (34, 0), (44, -22, 1), (52, -2), (60, -20, 1), (66, 2), (78, -6, 1), (84, 12), (90, 30),
                        (110, 40, 1), (88, 44), (86, 84), (60, 90), (50, 100, 1), (40, 90)])),
             L(outline([(56, -2), (80, 4), (90, 40), (86, 82), (62, 90)]), 'shade', 'b', False)],
}
# Avorio Opale: melena beige lisa y larga con raya en medio que le cae a los lados de una cara alargada y pálida, recogida
# atrás en una coleta baja; ojos de sueño con ojeras y la boca seria
CHARS['avorio-opale'] = {
    'body': 'delgado', 'pal': pal('#d0b090', '#fcdcc0', shade='#a88a6e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': [(16, 90), (18, 60), (30, 36), (50, 28), (70, 36), (82, 60), (84, 90)]},
    'front': longhair('front', 116, 4, part=True)
             + [L(outline([(24, 70), (42, 70), (40, 80), (26, 78)]), WHITE, 'f', ln=True), L(outline([(76, 70), (58, 70), (60, 80), (74, 78)]), WHITE, 'f', ln=True),
                L(ell(34, 75, 1.6, 2), OUTC, 'f', False), L(ell(66, 75, 1.6, 2), OUTC, 'f', False),
                L([(22, 66), (42, 70)], OUTC, 'f', False, False, 2.2), L([(78, 66), (58, 70)], OUTC, 'f', False, False, 2.2)],
    'side': longhair('side', 106, 4) + side_eye(76),
    'back': longhair('back', 100, 4, part=True, ends=0) + [L(rope((50, 90), (50, 106), (50, 120), 8), 'mid', 'f', ln=True)],
}
