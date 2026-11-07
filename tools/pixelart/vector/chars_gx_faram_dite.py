"""Falam Medius (gx-faram-dite): sus modelos 3D de Inazuma Eleven GO Galaxy como referencia (busto de frente, perfil y espalda).

La selección de los capitanes de los planetas de la Grand Celesta Galaxy: casi todos tienen las orejas puntiagudas de los
faramianos (elf_ears). 'ray-dark' es Kuroiwa Ryuusei (el Kageyama de Galaxy, que juega como androide): pelo blanco peinado
hacia atrás con coleta, barba blanca y gafas de sol, no el Ray Dark de IE. Ryugel y Gandares tienen las vistas del modelo
3D rotas en la enciclopedia: el frente sale del retrato y el resto, de lo que se ve del modelo.
"""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from heads import quad

T = 'gx-faram-dite'
WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def elf_ears(view, tip=(-12, 52), stip=(24, 50), z='b'):
    """Orejas puntiagudas: de frente, una a cada lado con la punta en tip (la derecha, simétrica); de perfil, una con la
    punta hacia atrás en stip; de espaldas, las dos asomando."""
    if view == 'front':
        tx, ty = tip
        out = []
        for m in (False, True):
            f = (lambda p: (100 - p[0], p[1]) + p[2:]) if m else (lambda p: p)
            out.append(L(outline([f((20, 60)), f((tx, ty, 1)), f((18, 86))]), 'skin', z, ln=True))
            out.append(L(outline([f((18, 66)), f(((tx + 18) / 2 + 2, (ty + 66) / 2 + 2, 1)), f((18, 78))]), 'skin_d', z, False))
        return out
    if view == 'side':
        sx, sy = stip
        return [L(outline([(52, 62), (sx, sy, 1), (48, 84)]), 'skin', 'f', ln=True),
                L(outline([(48, 66), ((sx + 48) / 2 + 2, (sy + 66) / 2 + 2, 1), (46, 78)]), 'skin_d', 'f', False)]
    tx, ty = tip
    out = []
    for m in (False, True):
        f = (lambda p: (100 - p[0], p[1]) + p[2:]) if m else (lambda p: p)
        out.append(L(outline([f((20, 58)), f((tx + 2, ty, 1)), f((20, 84))]), 'skin_d', z, ln=True))
    return out


def gem(x=50, y=50, r=3.4, c='gem'):
    return L(outline([(x, y - r * 1.6, 1), (x + r, y, 1), (x, y + r * 1.6, 1), (x - r, y, 1)]), c, 'f', ln=True)


# Argo Burgess (portero): cabeza de piel beis sin pelo, con dos crestas en punta en lo alto, aletas grandes a los lados en
# vez de orejas y una franja de pelo negro peinada de la frente a la coronilla; gema morada en la frente, sombra morada en
# los ojos ámbar y nariz larga
CHARS['argon-bulgess'] = {
    'body': 'corpulento', 'pal': pal('#2c3434', '#e6d0aa', iris='#c8862a', gem='#8a4ab8', paint='#8a5ab8', skin_d='#c8ae86'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'ears': False},
    'front': [L(outline([(14, 50), (-8, 28, 1), (-2, 58), (10, 80), (18, 80)]), 'skin_d', 'b', ln=True),
              L(outline([(86, 50), (108, 28, 1), (102, 58), (90, 80), (82, 80)]), 'skin_d', 'b', ln=True),
              L(outline([(18, 70), (12, 40), (16, 16), (24, -14, 1), (34, 10), (50, 4), (66, 10), (76, -14, 1), (84, 16), (88, 40), (82, 70)]), 'skin'),
              L(outline([(60, 8), (74, -4), (84, 18), (88, 44), (82, 64), (76, 36)]), 'skin_d', 'b', False),
              L(outline([(40, 8), (50, 2), (60, 8), (55, 32), (50, 42, 1), (45, 32)]), 'mid', 'f', ln=True),
              strand([(47, 8), (49, 34)], 'light', 'f', 0.8), strand([(53, 8), (51, 34)], 'light', 'f', 0.8),
              gem(50, 52),
              L(quad((24, 68), (32, 64), (42, 68)), 'paint', 'f', False, False, 2.2), L(quad((76, 68), (68, 64), (58, 68)), 'paint', 'f', False, False, 2.2),
              L([(50, 60), (50, 90)], 'skin_d', 'f', False, False, 2.0), L([(48, 88), (52, 92), (55, 88)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(52, 74), (56, 58), (80, 52), (92, 36), (88, 14), (72, 2), (66, -16, 1), (58, 4), (38, 2), (16, 12), (6, 36), (8, 62), (22, 80), (40, 82)]), 'skin'),
             L(outline([(36, 2), (58, 2), (70, 4), (62, 10), (40, 10), (18, 18), (16, 12)]), 'mid', 'f', ln=True),
             L(outline([(44, 52), (22, 36, 1), (24, 70), (42, 76)]), 'skin_d', 'f', ln=True),
             L(outline([(8, 36), (26, 44), (28, 74), (12, 64)]), 'skin_d', 'b', False),
             L(outline([(84, 60), (102, 84), (88, 92)]), 'skin', 'f', ln=True)],
    'back': [L(outline([(14, 50), (-8, 28, 1), (-2, 58), (10, 80), (18, 80)]), 'skin_d', 'b', ln=True),
             L(outline([(86, 50), (108, 28, 1), (102, 58), (90, 80), (82, 80)]), 'skin_d', 'b', ln=True),
             L(outline([(20, 86), (12, 40), (16, 16), (24, -14, 1), (34, 10), (66, 10), (76, -14, 1), (84, 16), (88, 40), (80, 86), (50, 94)]), 'skin'),
             L(outline([(56, 12), (84, 18), (88, 44), (80, 82), (56, 92)]), 'skin_d', 'b', False),
             L(outline([(32, 10), (68, 10), (50, 50, 1)]), 'mid', 'f', ln=True)],
}

# Xeno Wolf: pelo gris claro revuelto con dos rizos que se enroscan hacia arriba a los lados de lo alto, flequillo de
# mechones en punta hasta las cejas y nuca en punta; piel morena clara, orejas puntiagudas y ojos morados afilados
CHARS['xenon-reith'] = {
    'body': 'normal', 'pal': pal('#c8c8ce', '#f6c08a', iris='#7a4aa8', shade='#9a909c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(12, 70), (6, 40), (8, 18), (-8, 8, 1), (4, 2), (14, -4), (30, -8), (50, -10), (70, -8), (86, -4), (96, 2), (108, 8, 1), (92, 18), (94, 40), (88, 70),
                         (82, 60), (18, 60)])),
              L(outline([(60, -6), (86, 2), (94, 40), (88, 64), (78, 40)]), 'shade', 'b', False),
              L(ell(4, 4, 5, 4) + [ell(4, 4, 5, 4)[0]], 'shade', 'b', False, False, 1.6), L(ell(96, 4, 5, 4) + [ell(96, 4, 5, 4)[0]], 'shade', 'b', False, False, 1.6)]
             + elf_ears('front', (-16, 48))
             + [fringe([(12, 64), (14, 40), (26, 22), (50, 14), (74, 22), (86, 40), (88, 64), (80, 56), (74, 66, 1), (66, 48), (58, 60, 1), (52, 46), (46, 62, 1), (40, 48),
                        (32, 60, 1), (26, 50), (20, 64, 1)]),
                L(outline([(28, 22), (46, 16), (38, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 36), (90, 14), (76, 0), (52, -10), (28, -6), (10, 6), (-6, 18, 1), (4, 30), (2, 56), (12, 76), (30, 80), (46, 70)])),
             L(outline([(4, 34), (24, 40), (26, 72), (10, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 62, 1), (86, 48), (80, 58, 1), (76, 40), (66, 30)])] + elf_ears('side', stip=(22, 50)),
    'back': elf_ears('back', (-16, 48))
            + [L(outline([(14, 84), (8, 40), (8, 18), (-8, 8, 1), (4, 2), (14, -6), (50, -12), (86, -6), (96, 2), (108, 8, 1), (92, 18), (92, 40), (86, 84), (72, 94, 1),
                          (62, 86), (50, 96, 1), (38, 86), (28, 94, 1)])),
               L(outline([(56, -8), (86, 0), (92, 44), (84, 82), (62, 88)]), 'shade', 'b', False)],
}

# Varga Sachs: grandullón de piel amarilla con una melena roja enorme de león, de mechones gruesos en punta que le abultan
# a los lados y por detrás hasta los hombros; dos cuernos amarillos encima de la frente, gema roja, rayas naranjas en las
# mejillas y una sonrisa enorme
_mane_f = [(10, 110), (-30, 104, 1), (-16, 90), (-34, 76, 1), (-12, 66), (-24, 48, 1), (-2, 40), (-6, 20, 1), (14, 18), (14, 0, 1), (30, 8), (50, -2), (70, 8), (86, 0, 1),
           (86, 18), (106, 20, 1), (102, 40), (124, 48, 1), (112, 66), (134, 76, 1), (116, 90), (130, 104, 1), (90, 110), (84, 70), (16, 70)]
CHARS['ogar-circes'] = {
    'body': 'corpulento', 'pal': pal('#c81e14', '#e8c840', iris='#2a1a10', shade='#961610', mark='#e07020', horn='#ecd25a', gem='#d02a2a', skin_d='#c8a830'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline(_mane_f)), L(outline([(60, 0), (86, 18), (108, 46), (128, 100), (96, 104), (84, 40)]), 'shade', 'b', False)]
             + elf_ears('front', (-2, 58))
             + [L(outline([(12, 52), (14, 30), (30, 18), (50, 14), (70, 18), (86, 30), (88, 52), (76, 44), (62, 48), (50, 42), (38, 48), (24, 44)]), 'mid', 'f'),
                L(outline([(14, 52), (16, 36), (28, 46)]), 'shade', 'f', False), L(outline([(86, 52), (84, 36), (72, 46)]), 'shade', 'f', False),
                L(outline([(30, 34), (20, 12, 1), (38, 28)]), 'horn', 'f', ln=True), L(outline([(70, 34), (80, 12, 1), (62, 28)]), 'horn', 'f', ln=True),
                gem(50, 54, 3.0),
                L([(22, 84), (36, 86)], 'mark', 'f', False, False, 2.2), L([(24, 90), (36, 90)], 'mark', 'f', False, False, 2.2),
                L([(78, 84), (64, 86)], 'mark', 'f', False, False, 2.2), L([(76, 90), (64, 90)], 'mark', 'f', False, False, 2.2)],
    'side': [L(outline([(56, 60), (60, 48), (80, 48), (92, 34), (88, 14), (70, 0), (46, -6), (20, 0), (0, 12), (-24, 30, 1), (-10, 40), (-34, 60, 1), (-12, 66), (-30, 90, 1),
                        (-6, 88), (-10, 110, 1), (14, 98), (24, 112, 1), (36, 96), (48, 80)])),
             L(outline([(-10, 40), (14, 46), (24, 92), (-4, 92)]), 'shade', 'b', False),
             L(outline([(60, 4), (86, 14), (94, 34), (80, 30), (64, 20)]), 'mid', 'f', ln=True),
             L(outline([(66, 12), (76, -8, 1), (76, 16)]), 'horn', 'f', ln=True),
             L([(80, 86), (90, 86)], 'mark', 'f', False, False, 2.2)] + elf_ears('side', stip=(30, 54)),
    'back': [L(outline([(0, 110), (-30, 100, 1), (-14, 84), (-34, 66, 1), (-12, 56), (-22, 36, 1), (0, 30), (4, 8), (22, -2, 1), (30, 8), (50, 0), (70, 8), (78, -2, 1), (96, 8),
                        (100, 30), (122, 36, 1), (112, 56), (134, 66, 1), (114, 84), (130, 100, 1), (100, 110), (80, 118, 1), (64, 108), (50, 120, 1), (36, 108), (20, 118, 1)])),
             L(outline([(56, 2), (96, 10), (120, 60), (110, 104), (66, 108), (70, 50)]), 'shade', 'b', False),
             strand([(20, 40), (10, 70), (16, 104)], 'shade', 'b', 1.2), strand([(50, 20), (50, 110)], 'shade', 'b', 1.2), strand([(80, 40), (90, 70), (84, 104)], 'shade', 'b', 1.2),
             L(outline([(30, 14), (22, -6, 1), (38, 10)]), 'horn', 'f', ln=True), L(outline([(70, 14), (78, -6, 1), (62, 10)]), 'horn', 'f', ln=True)],
}

# Radon Morm: pelo verde oliva largo como un casco, con el flequillo de mechones en punta que le tapa los ojos, dos cuernos
# en lo alto y la melena hasta los hombros; orejas puntiagudas grandes hacia fuera
CHARS['radon-mons'] = {
    'body': 'normal', 'pal': pal('#9a9450', '#fcd8a8', iris='#3a2a1a', shade='#76703c', horn='#6a5a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(28, 8), (30, -18, 1), (40, 4)]), 'horn', 'b', ln=True), L(outline([(72, 8), (70, -18, 1), (60, 4)]), 'horn', 'b', ln=True),
              L(outline([(8, 104), (4, 60), (10, 24), (30, 4), (50, 0), (70, 4), (90, 24), (96, 60), (92, 104), (80, 96), (20, 96)])),
              L(outline([(60, 4), (88, 22), (96, 60), (90, 100), (80, 50)]), 'shade', 'b', False)]
             + elf_ears('front', (-14, 56))
             + [fringe([(12, 84), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 84), (80, 70), (72, 84, 1), (66, 70), (58, 82, 1), (50, 70), (42, 82, 1), (34, 70),
                        (26, 84, 1), (20, 70)]),
                L(outline([(56, 12), (80, 22), (88, 46), (84, 72), (74, 40)]), 'shade', 'f', False),
                strand([(36, 20), (34, 66)], 'shade', 'f', 1.0), strand([(64, 20), (66, 66)], 'shade', 'f', 1.0)],
    'side': [L(outline([(58, 8), (66, -18, 1), (68, 8)]), 'horn', 'b', ln=True),
             L(outline([(54, 80), (56, 60), (76, 56), (92, 40), (90, 16), (76, 2), (50, -2), (30, 0), (14, 10), (4, 40), (0, 80), (-6, 104, 1), (10, 96), (20, 110, 1), (30, 96),
                        (44, 90)])),
             L(outline([(4, 40), (26, 46), (30, 92), (8, 94)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 16), (94, 40), (94, 74, 1), (86, 62), (80, 74, 1), (76, 50), (66, 36)])] + elf_ears('side', stip=(18, 56)),
    'back': elf_ears('back', (-14, 56))
            + [L(outline([(28, 8), (30, -18, 1), (40, 4)]), 'horn', 'b', ln=True), L(outline([(72, 8), (70, -18, 1), (60, 4)]), 'horn', 'b', ln=True),
               L(outline([(10, 104), (4, 60), (10, 24), (30, 4), (50, 0), (70, 4), (90, 24), (96, 60), (90, 104), (70, 110, 1), (50, 100), (30, 110, 1)])),
               L(outline([(56, 4), (88, 22), (96, 60), (88, 102), (64, 104)]), 'shade', 'b', False)],
}

# Selen Melvil: pelo malva con raya en medio y dos coletas largas a los lados, atadas arriba con gomas verdes y que caen en
# mechones gruesos hasta el pecho; orejas puntiagudas y ojos grandes azules
_sel_tail = [(16, 22), (2, 26), (-6, 50), (0, 74), (-6, 112, 1), (8, 100), (14, 114, 1), (18, 80), (14, 56), (20, 40)]
CHARS['selenia'] = {
    'body': 'chica', 'pal': pal('#b04a78', '#fcdcc0', iris='#2a7ab8', shade='#8a3a5e', tie='#a8c860'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(14, 70), (10, 40), (18, 10), (50, -6), (82, 10), (90, 40), (86, 70)])),
              L(outline(_sel_tail)), L(outline([(100 - x, y) + p[2:] for (x, y, *p) in [tuple(t) for t in _sel_tail]])),
              L(outline([(8, 60), (16, 70), (8, 104), (4, 90)]), 'shade', 'b', False), L(outline([(92, 60), (84, 70), (92, 104), (96, 90)]), 'shade', 'b', False),
              L(outline([(60, -2), (82, 10), (90, 40), (86, 66), (78, 36)]), 'shade', 'b', False),
              L(ell(12, 24, 3.4, 4), 'tie', 'f', ln=True), L(ell(88, 24, 3.4, 4), 'tie', 'f', ln=True)]
             + elf_ears('front', (-8, 54))
             + [fringe([(12, 60), (12, 36), (24, 14), (48, 4), (50, 14), (52, 4), (76, 14), (88, 36), (88, 60), (82, 48), (74, 56, 1), (68, 36), (56, 22), (50, 30), (44, 22),
                        (32, 36), (26, 56, 1), (18, 48)])],
    'side': [L(outline([(16, 20), (-6, 30), (-14, 60), (-10, 112, 1), (4, 100), (8, 114, 1), (14, 80), (10, 56), (22, 36)])),
             L(outline([(52, 72), (56, 56), (78, 52), (92, 38), (88, 12), (66, -6), (36, -6), (14, 8), (4, 34), (6, 64), (20, 80), (36, 80)])),
             L(outline([(4, 34), (26, 40), (30, 72), (10, 68)]), 'shade', 'b', False),
             L(ell(18, 24, 3.4, 4), 'tie', 'f', ln=True),
             fringe([(62, 2), (88, 14), (94, 38), (92, 58, 1), (84, 46), (78, 36)])] + elf_ears('side', stip=(28, 52)),
    'back': elf_ears('back', (-8, 54))
            + [L(outline([(14, 74), (10, 40), (18, 10), (50, -6), (82, 10), (90, 40), (86, 74), (50, 82)])),
               L(outline([(56, -2), (82, 10), (90, 44), (84, 72), (60, 80)]), 'shade', 'b', False),
               L(outline(_sel_tail), 'mid', 'f'), L(outline([(100 - x, y) + p[2:] for (x, y, *p) in [tuple(t) for t in _sel_tail]]), 'mid', 'f'),
               L(ell(12, 24, 3.4, 4), 'tie', 'f', ln=True), L(ell(88, 24, 3.4, 4), 'tie', 'f', ln=True),
               strand([(50, -4), (50, 76)], 'shade', 'b', 1.2)],
}

# Hilary Flail: melena larga celeste que vuela hacia un lado, con las puntas moradas, un mechón (antena) que se curva por
# encima de la cabeza, cinta negra fina y un parche negro en el ojo izquierdo; orejas puntiagudas y labios pintados
CHARS['rondula-flehl'] = {
    'body': 'chica', 'pal': pal('#7ad8e0', '#fcdcc0', iris='#2a8ab8', shade='#5aaab8', tip='#8a5ac8', patch='#1e1e24'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 110), (-16, 104, 1), (-4, 90), (0, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (98, 60), (96, 110), (84, 104), (84, 66), (16, 66)])),
              L(outline([(-16, 104), (-4, 90), (12, 98), (6, 112)]), 'tip', 'b', False),
              L(outline([(60, 4), (84, 12), (96, 46), (94, 104), (84, 64)]), 'shade', 'b', False)]
             + elf_ears('front', (-8, 56))
             + [fringe([(12, 72), (12, 40), (26, 18), (50, 10), (74, 18), (88, 40), (90, 72), (82, 56), (76, 64, 1), (70, 46), (56, 40), (44, 48), (36, 62, 1), (30, 46),
                        (22, 62, 1), (16, 56)]),
                L(quad((48, 4), (60, -30), (84, -14)), 'mid', 'f', False, False, 3.2),
                L(quad((14, 32), (50, 12), (86, 32)), OUTC, 'f', False, False, 1.8),
                L(ell(64, 76, 8.4, 7.4), 'patch', 'f', ln=True), L([(54, 64), (84, 94)], 'patch', 'f', False, False, 2.0)],
    'side': [L(outline([(52, 74), (56, 58), (78, 54), (92, 40), (88, 16), (68, 0), (40, -2), (16, 10), (4, 36), (-2, 70), (-12, 110, 1), (6, 100), (14, 114, 1), (26, 96),
                        (40, 90), (48, 82)])),
             L(outline([(-12, 110), (4, 98), (14, 114)]), 'tip', 'b', False),
             L(outline([(4, 40), (28, 46), (32, 92), (8, 96)]), 'shade', 'b', False),
             L(quad((60, 2), (72, -28), (94, -10)), 'mid', 'f', False, False, 3.2),
             L(quad((40, 2), (70, 4), (92, 22)), OUTC, 'f', False, False, 1.8),
             fringe([(64, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])] + elf_ears('side', stip=(28, 52)),
    'back': elf_ears('back', (-8, 56))
            + [L(outline([(8, 110), (0, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (100, 60), (98, 110), (84, 118, 1), (68, 106), (50, 118, 1), (32, 106), (16, 118, 1)])),
               L(outline([(84, 100), (106, 116, 1), (98, 104)]), 'tip', 'b', False),
               L(outline([(56, 4), (84, 12), (98, 50), (96, 108), (66, 108)]), 'shade', 'b', False),
               L(quad((50, 2), (62, -28), (84, -12)), 'mid', 'f', False, False, 3.2)],
}

# Neol Lotz: pelo verde menta muy claro en champiñón abultado, flequillo recto sobre los ojos y dos moños bajos a los lados
# de la barbilla; orejas puntiagudas, ojos castaños y una sonrisa
CHARS['neon'] = {
    'body': 'bajito', 'pal': pal('#a8dcb0', '#fcdcc0', iris='#9a3a1e', shade='#8a9a84'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(ell(10, 94, 13, 9)), L(ell(90, 94, 13, 9)),
              L(outline([(12, 72), (0, 60), (-2, 40), (6, 16), (26, 2), (50, -2), (74, 2), (94, 16), (102, 40), (100, 60), (88, 72)])),
              L(outline([(60, 0), (90, 14), (100, 46), (92, 68), (82, 40)]), 'shade', 'b', False),
              L(ell(94, 96, 9, 6), 'shade', 'b', False)]
             + elf_ears('front', (-6, 58))
             + [fringe([(10, 62), (10, 40), (24, 20), (50, 12), (76, 20), (90, 40), (90, 62), (82, 60), (76, 62), (70, 58), (60, 62), (50, 58), (40, 62), (30, 58), (22, 62),
                        (16, 60)]),
                L(outline([(30, 20), (48, 14), (40, 26)]), 'light', 'f', False), L(quad((48, 0), (52, -8), (58, -6)), 'mid', 'f', False, False, 1.6)],
    'side': [L(ell(18, 96, 14, 9)),
             L(outline([(54, 64), (58, 52), (80, 48), (98, 36), (96, 16), (80, 2), (52, -4), (26, 0), (6, 14), (-4, 36), (-4, 60), (10, 72), (30, 74), (46, 72)])),
             L(outline([(-4, 36), (22, 40), (26, 70), (2, 64)]), 'shade', 'b', False),
             fringe([(64, 4), (92, 18), (100, 38), (96, 52), (86, 50), (78, 40)])] + elf_ears('side', stip=(30, 56)),
    'back': elf_ears('back', (-6, 58))
            + [L(outline([(12, 78), (-2, 60), (-4, 40), (6, 16), (26, 2), (50, -2), (74, 2), (94, 16), (104, 40), (102, 60), (88, 78), (50, 84)]), 'shade'),
               L(outline([(6, 16), (26, 2), (50, -2), (74, 2), (94, 16), (100, 34), (50, 30), (0, 34)]), 'mid', 'b', False),
               L(ell(14, 96, 13, 9), 'shade', 'f', ln=True), L(ell(86, 96, 13, 9), 'shade', 'f', ln=True)],
}

# Ryugel Baran: pelo rosa muy pálido de pinchos largos hacia arriba y a los lados, con mechones finos que le caen por la cara;
# piel blanca, gema morada en la frente y ojos lila (el modelo 3D tiene el perfil y la espalda rotos: del retrato)
CHARS['ruger-baran'] = {
    'body': 'normal', 'pal': pal('#f2d8e0', '#fcf2ec', iris='#7a6ac8', shade='#d0a4b4', gem='#8a4ab8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(14, 74), (2, 62, 1), (10, 50), (-6, 34, 1), (10, 28), (6, 4, 1), (22, 12), (28, -16, 1), (36, 4), (44, -34, 1), (54, 0), (66, -20, 1), (70, 6), (88, -4, 1),
                         (86, 18), (106, 24, 1), (92, 36), (106, 50, 1), (92, 58), (98, 72, 1), (86, 74), (84, 56), (16, 56)])),
              L(outline([(56, -2), (86, 8), (94, 40), (88, 66), (76, 38)]), 'shade', 'b', False)]
             + elf_ears('front', (-12, 50))
             + [fringe([(12, 66), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 66), (80, 56), (76, 72, 1), (70, 50), (62, 46), (58, 56, 1), (52, 44), (46, 44),
                        (40, 56, 1), (34, 46), (24, 72, 1), (18, 58)]),
                strand([(30, 30), (24, 66)], 'shade', 'f', 1.0), strand([(70, 30), (76, 66)], 'shade', 'f', 1.0),
                gem(50, 56, 3.0)],
    'side': [L(outline([(54, 60), (60, 48), (82, 46), (94, 32), (90, 12), (100, -4, 1), (78, 0), (70, -22, 1), (58, -4), (46, -32, 1), (36, -2), (8, -8, 1), (14, 14), (-12, 24, 1),
                        (6, 36), (-12, 52, 1), (8, 58), (0, 78, 1), (18, 72), (24, 88, 1), (36, 76), (46, 70)])),
             L(outline([(4, 36), (24, 42), (26, 70), (8, 64)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 68, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])] + elf_ears('side', stip=(22, 48)),
    'back': elf_ears('back', (-12, 50))
            + [L(outline([(14, 82), (0, 74, 1), (8, 60), (-8, 44, 1), (8, 36), (4, 10, 1), (22, 14), (28, -14, 1), (36, 4), (44, -32, 1), (54, 0), (66, -18, 1), (70, 6),
                          (88, -2, 1), (86, 18), (106, 24, 1), (92, 40), (108, 56, 1), (92, 64), (98, 80, 1), (84, 84), (68, 94, 1), (60, 86), (50, 96, 1), (40, 86), (30, 94, 1)])),
               L(outline([(56, 0), (86, 10), (94, 46), (86, 80), (62, 88)]), 'shade', 'b', False)],
}

# Gandares Baran: melena negra verdosa larga y ondulada hasta los hombros, con un único pincho altísimo en lo alto; piel
# blanca, ojos magenta y rayas moradas y rojas pintadas en las mejillas (el modelo 3D está roto: del retrato y la espalda)
CHARS['gandares-baran'] = {
    'body': 'normal', 'pal': pal('#1e2a2a', '#f6f0f2', iris='#c83a8a', shade='#141c1c', light='#3a4a4a', paint='#8a3ab0', red='#c81e3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 110), (-8, 100, 1), (0, 86), (-10, 72, 1), (4, 62), (4, 30), (18, 10), (40, 2), (46, -36, 1), (56, 2), (80, 8), (94, 28), (96, 62), (110, 72, 1),
                         (100, 86), (108, 100, 1), (90, 110), (84, 64), (16, 64)])),
              L(outline([(60, 4), (84, 12), (96, 44), (96, 104), (84, 64)]), 'shade', 'b', False)]
             + elf_ears('front', (-10, 56))
             + [fringe([(12, 70), (12, 40), (26, 20), (50, 14), (74, 20), (88, 40), (88, 70), (80, 58), (74, 66, 1), (66, 46), (56, 60, 1), (52, 44), (48, 76, 1), (44, 44),
                        (34, 62, 1), (28, 48), (20, 70, 1)]),
                L(outline([(46, -30), (50, -10), (48, 6)]), 'light', 'f', False),
                L([(26, 84), (34, 92)], 'paint', 'f', False, False, 2.2), L([(30, 82), (38, 90)], 'red', 'f', False, False, 1.8),
                L([(74, 84), (66, 92)], 'paint', 'f', False, False, 2.2), L([(70, 82), (62, 90)], 'red', 'f', False, False, 1.8)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (90, 12), (70, 0), (56, 2), (48, -36, 1), (40, 0), (16, 8), (4, 32), (-2, 64), (-12, 100, 1), (4, 94), (8, 112, 1),
                        (22, 98), (32, 108, 1), (40, 90), (48, 78)])),
             L(outline([(0, 40), (24, 46), (30, 92), (4, 92)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 16), (96, 42), (94, 68, 1), (86, 52), (80, 62, 1), (76, 42), (66, 30)]),
             L([(80, 84), (88, 90)], 'paint', 'f', False, False, 2.2)] + elf_ears('side', stip=(22, 54)),
    'back': elf_ears('back', (-10, 56))
            + [L(outline([(8, 110), (-10, 96, 1), (0, 82), (-8, 66, 1), (4, 56), (4, 30), (18, 10), (40, 2), (46, -36, 1), (56, 2), (80, 8), (96, 30), (96, 56), (108, 66, 1),
                          (100, 82), (110, 96, 1), (92, 110), (78, 120, 1), (64, 106), (50, 120, 1), (36, 106), (22, 120, 1)])),
               L(outline([(56, 4), (84, 12), (98, 50), (98, 104), (70, 110), (72, 50)]), 'shade', 'b', False),
               strand([(26, 30), (18, 70), (24, 108)], 'light', 'b', 1.0), strand([(74, 30), (82, 70), (76, 108)], 'light', 'b', 1.0)],
}

# Rodan Gasgus: capucha verde grisácea en punta que le tapa la cabeza, con rombos verdes oscuros y uno rojo en la frente y dos
# cuernos que salen por los lados (rojo a la derecha de la imagen... a su derecha, blanco a la izquierda); cara blanca con
# media cara pintada de rojo, ojos rosas y sonrisa de colmillos
CHARS['bala-gasgula'] = {
    'body': 'bajito', 'pal': pal('#7aa890', '#f6f2f0', iris='#c84a6a', shade='#5a7a68', deep='#3a5444', red='#d02a2a', horn_w='#f0e8e4', hairc='#3a2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 110), (2, 60), (10, 20), (30, 0), (50, -16, 1), (70, 0), (90, 20), (98, 60), (96, 110), (84, 104), (84, 60), (16, 60), (16, 104)])),
              L(outline([(60, -4), (88, 18), (98, 60), (96, 106), (84, 60)]), 'shade', 'b', False),
              L(outline([(80, 60), (88, 80), (84, 98), (78, 80)]), 'hairc', 'b', False),
              L(outline([(14, 58), (28, 58), (32, 70), (26, 96), (16, 86)]), 'red', 'f', False),
              L(outline([(10, 58), (12, 30), (30, 12), (50, 4), (70, 12), (88, 30), (90, 58), (78, 52), (64, 44), (50, 50, 1), (36, 44), (22, 52)]), 'mid', 'f', ln=True),
              L(outline([(44, 14), (48, 18), (44, 22), (40, 18)]), 'deep', 'f', False), L(outline([(56, 14), (60, 18), (56, 22), (52, 18)]), 'deep', 'f', False),
              L(outline([(50, 6), (54, 10), (50, 14), (46, 10)]), 'deep', 'f', False), L(outline([(50, 24), (55, 30), (50, 36), (45, 30)]), 'red', 'f', False),
              L(outline([(18, 46), (8, 22, 1), (26, 38)]), 'red', 'f', ln=True), L(outline([(82, 46), (92, 22, 1), (74, 38)]), 'horn_w', 'f', ln=True)],
    'side': [L(outline([(54, 92), (58, 62), (80, 52), (92, 36), (88, 14), (66, -6), (36, -10), (2, -10, 1), (10, 10), (0, 40), (2, 80), (20, 100), (40, 104)])),
             L(outline([(4, 20), (36, 40), (40, 96), (6, 84)]), 'shade', 'b', False),
             L(outline([(62, 0), (88, 14), (94, 36), (88, 54), (80, 40), (70, 20)]), 'mid', 'f', ln=True),
             L(outline([(80, 50), (90, 26, 1), (86, 56)]), 'red', 'f', ln=True), L([(82, 74), (86, 90)], 'red', 'f', False, False, 3.0)],
    'back': [L(outline([(8, 110), (6, 60), (14, 24), (34, 0), (50, -20, 1), (66, 0), (86, 24), (94, 60), (92, 110), (50, 116)])),
             L(outline([(56, 0), (86, 24), (94, 70), (88, 108), (60, 112), (66, 50)]), 'shade', 'b', False),
             L(outline([(14, 46), (4, 22, 1), (22, 38)]), 'horn_w', 'b', ln=True), L(outline([(86, 46), (96, 22, 1), (78, 38)]), 'red', 'b', ln=True)],
}

# Sulfer Berg: pelo rosa muy pálido corto y revuelto, con dos cuernos largos de pelo hacia arriba y mechones finos que le
# enmarcan la cara hasta la barbilla; piel morena, orejas puntiagudas y ojos verdes afilados
CHARS['brimstone'] = {
    'body': 'normal', 'pal': pal('#f2c8d0', '#a86a40', iris='#a8b030', shade='#c898a4', skin_d='#8a5430'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 20), (2, -34, 1), (32, 8)])), L(outline([(84, 20), (98, -34, 1), (68, 8)])),
              L(outline([(14, 80), (10, 40), (14, 16), (30, 4), (50, 0), (70, 4), (86, 16), (90, 40), (86, 80), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (92, 44), (86, 76), (78, 40)]), 'shade', 'b', False),
              L(outline([(88, 16), (96, -24, 1), (76, 8)]), 'shade', 'b', False)]
             + elf_ears('front', (-12, 50))
             + [fringe([(12, 66), (12, 40), (26, 20), (50, 14), (74, 20), (88, 40), (88, 66), (80, 54), (74, 62, 1), (68, 44), (58, 56, 1), (54, 40), (48, 58, 1), (42, 40),
                        (34, 58, 1), (28, 46), (20, 64, 1)]),
                L(outline([(14, 58), (12, 98, 1), (22, 78)]), 'mid', 'f', ln=True), L(outline([(86, 58), (88, 98, 1), (78, 78)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (90, 14), (72, 2), (64, -32, 1), (56, 2), (36, 0), (14, 12), (2, 36), (4, 64), (14, 82), (30, 86), (46, 74)])),
             L(outline([(4, 36), (24, 42), (28, 78), (10, 72)]), 'shade', 'b', False),
             fringe([(62, 4), (90, 16), (96, 40), (94, 70, 1), (86, 52), (80, 60, 1), (76, 42), (66, 30)])] + elf_ears('side', stip=(22, 50)),
    'back': elf_ears('back', (-12, 50))
            + [L(outline([(16, 20), (2, -34, 1), (32, 8)])), L(outline([(84, 20), (98, -34, 1), (68, 8)])),
               L(outline([(14, 88), (8, 40), (14, 16), (30, 4), (50, 0), (70, 4), (86, 16), (92, 40), (86, 88), (72, 96, 1), (62, 86), (50, 94, 1), (38, 86), (28, 96, 1)])),
               L(outline([(56, 4), (86, 16), (92, 46), (86, 84), (62, 88)]), 'shade', 'b', False)],
}

# Kuroiwa Ryuusei (el Kageyama de Galaxy, que en Falam Medius juega como androide): pelo blanco peinado hacia atrás con una
# coleta baja, barba y bigote blancos, gafas de sol negras, nariz larga, una cicatriz en la frente y piel morena anaranjada
CHARS[f'{T}:ray-dark'] = {
    'body': 'delgado', 'pal': pal('#e8e4e0', '#e0984e', iris='#1e1414', shade='#b8b0ac', glass='#1e1e22', skin_d='#b8743a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 2, 'ear_out': 2},
    'front': [L(outline([(14, 64), (10, 30), (16, 4), (32, -14), (50, -18), (68, -14), (84, 4), (90, 30), (86, 64), (80, 44), (20, 44)])),
              L(outline([(14, 50), (12, 24), (20, 2), (36, -12), (50, -16), (64, -12), (80, 2), (88, 24), (86, 50), (78, 34), (64, 26), (50, 28), (36, 26), (22, 34)]), 'mid', 'f',
                ln=True),
              strand([(30, 0), (28, 30)], 'shade', 'f', 1.0), strand([(44, -10), (42, 26)], 'shade', 'f', 1.0), strand([(58, -10), (58, 26)], 'shade', 'f', 1.0),
              strand([(72, 0), (74, 30)], 'shade', 'f', 1.0),
              L(quad((32, 40), (44, 38), (54, 30)), OUTC, 'f', False, False, 1.4),
              L(outline([(20, 88), (30, 96), (40, 92), (50, 98), (60, 92), (70, 96), (80, 88), (86, 104), (74, 122), (50, 128), (26, 122), (14, 104)]), 'mid', 'f', ln=True),
              L(outline([(36, 92), (50, 88), (64, 92), (60, 98), (50, 94), (40, 98)]), 'shade', 'f', False),
              L(outline([(46, 64), (54, 64), (58, 88), (50, 92), (42, 88)]), 'skin_d', 'f', ln=True),
              L(ell(36, 72, 10, 6), 'glass', 'f', ln=True), L(ell(64, 72, 10, 6), 'glass', 'f', ln=True),
              L([(46, 71), (54, 71)], 'glass', 'f', False, False, 1.6), L([(26, 70), (16, 68)], 'glass', 'f', False, False, 1.6), L([(74, 70), (84, 68)], 'glass', 'f', False, False, 1.6)],
    'side': [L(outline([(10, 62), (-6, 72), (-10, 96), (2, 106), (10, 88), (20, 76)])),
             L(outline([(56, 40), (76, 30), (86, 16), (80, 0), (60, -14), (30, -12), (10, 0), (2, 24), (4, 50), (10, 70), (18, 84), (28, 84), (36, 70), (44, 52)])),
             strand([(70, 4), (30, 2), (10, 30)], 'shade', 'b', 1.0), strand([(76, 18), (40, 14), (16, 50)], 'shade', 'b', 1.0),
             L([(14, 64), (18, 72)], 'glass', 'f', False, False, 3.0),
             L(outline([(58, 86), (84, 90), (92, 100), (78, 122), (56, 118), (50, 100)]), 'mid', 'f', ln=True),
             L(outline([(84, 64), (104, 94), (86, 92)]), 'skin', 'f', ln=True),
             L(ell(82, 72, 6, 6), 'glass', 'f', ln=True), L([(76, 70), (48, 66)], 'glass', 'f', False, False, 1.6)],
    'back': [L(outline([(14, 90), (8, 40), (14, 8), (30, -12), (50, -18), (70, -12), (86, 8), (92, 40), (86, 90), (66, 96), (34, 96)])),
             L(outline([(56, -14), (86, 8), (92, 50), (84, 88), (62, 94)]), 'shade', 'b', False),
             L(outline([(40, 84), (60, 84), (62, 104), (54, 122), (46, 104)]), 'mid', 'f', ln=True), L([(42, 86), (58, 86)], 'glass', 'f', False, False, 2.4),
             strand([(30, -6), (34, 80)], 'shade', 'b', 1.0), strand([(70, -6), (66, 80)], 'shade', 'b', 1.0)],
}
