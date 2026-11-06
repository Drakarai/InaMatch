"""Mar de Árboles y Robots Guardias (IE2). Los del Mar de Árboles llevan máscaras antigás de piedra cubiertas de musgo
(con orejas, una seta o un árbol encima); los Robots Guardias son todos el mismo robot (pelo rosa, cinta y gafas)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

DARK = (24, 30, 34, 255)
MASK_F = [(10, 98), (8, 50), (16, 18), (50, 4), (84, 18), (92, 50), (90, 98), (70, 108), (50, 110), (30, 108)]
MASK_S = [(14, 100), (8, 52), (18, 18), (50, 4), (80, 14), (94, 40), (98, 70), (92, 100), (70, 108), (40, 108)]


def gasmask(view, eyes=(30, 66, 10, 9), filt=None, moss=True, extra_f=(), extra_s=(), extra_b=(), jaw=False):
    """Máscara antigás de piedra que cubre toda la cabeza: dos ojos de cristal oscuro, el filtro y manchas de musgo."""
    ex, ey, rx, ry = eyes
    if view == 'front':
        out = [L(blob(MASK_F), 'mask', 'f', ln=True), L(blob([(62, 8), (90, 48), (88, 96), (70, 104)], 6), 'mask_d', 'f', False)]
        if moss:
            out += [L(bumpy(34, 18, 20, 10, 6, 0.15), 'moss', 'f', False), L(bumpy(78, 40, 10, 12, 6, 0.15), 'moss', 'f', False),
                    L(bumpy(18, 84, 8, 10, 6, 0.15), 'moss', 'f', False)]
        for cx in (ex, 100 - ex):
            out += [L(ell(cx, ey, rx + 2.4, ry + 2.4), 'mask_d', 'f', ln=True), L(ell(cx, ey, rx, ry), 'lens', 'f', False),
                    L(ell(cx - rx * 0.3, ey - ry * 0.3, rx * 0.3, ry * 0.25), (150, 190, 200, 255), 'f', False)]
        if jaw:
            out.append(L(blob([(34, 88), (66, 88), (62, 104), (38, 104)]), 'skin', 'f', ln=True))
        elif filt:
            out += [L(ell(50, 92, filt, filt * 0.9), 'filt', 'f', ln=True), L(ell(50, 92, filt * 0.45, filt * 0.4), DARK, 'f', False)]
        return out + list(extra_f)
    if view == 'side':
        out = [L(blob(MASK_S), 'mask', 'f', ln=True), L(blob([(16, 50), (24, 22), (36, 60), (24, 96)], 6), 'mask_d', 'f', False)]
        if moss:
            out += [L(bumpy(40, 14, 22, 9, 6, 0.15), 'moss', 'f', False), L(bumpy(26, 70, 8, 10, 6, 0.15), 'moss', 'f', False)]
        out += [L(ell(86, ey, rx * 0.6 + 2, ry + 2), 'mask_d', 'f', ln=True), L(ell(87, ey, rx * 0.6, ry), 'lens', 'f', False)]
        if filt and not jaw:
            out.append(L(ell(96, 92, filt * 0.6, filt * 0.9), 'filt', 'f', ln=True))
        return out + list(extra_s)
    out = [L(blob(MASK_F[:7] + [(50, 112)]), 'mask', 'f', ln=True), L(blob([(58, 8), (90, 48), (88, 96), (62, 106)], 6), 'mask_d', 'f', False),
           L(quad((10, 70), (50, 76), (90, 70)), 'strap', 'f', False, False, 3)]
    if moss:
        out += [L(bumpy(50, 22, 26, 12, 6, 0.15), 'moss', 'f', False), L(bumpy(76, 70, 10, 12, 6, 0.15), 'moss', 'f', False)]
    return out + list(extra_b)


def mpal(mask='#c8c2ae', moss='#7a9a3a', lens='#1e3a4a', filt='#d8cc8a', skin='#f0b07a', hair='#4a3a2a', **kw):
    return pal(hair, skin, mask=mask, mask_d='#9a9484', moss=moss, lens=lens, filt=filt, strap='#3a3a2a', **kw)


NOFACE = {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False}

# Cam Mando (portero): máscara oscura con orejas de gato rosas, ojos grandes y un filtro triangular crema
CHARS['cam-mando'] = {
    'body': 'normal', 'pal': mpal(mask='#2a3a3e', moss='#2a3a3e', filt='#e8dcb4', ear='#e8909a'), 'face': NOFACE,
    'front': [L([(12, 28), (18, -8), (40, 14)], 'ear', 'b', ln=True), L([(88, 28), (82, -8), (60, 14)], 'ear', 'b', ln=True)]
             + gasmask('front', (32, 56, 13, 11), 13, moss=False, extra_f=[L([(40, 28), (60, 28), (56, 40), (44, 40)], 'filt', 'f', ln=True)]),
    'side': [L([(30, 20), (36, -12), (56, 10)], 'ear', 'b', ln=True)] + gasmask('side', (32, 56, 13, 11), 13, moss=False),
    'back': [L([(12, 28), (18, -8), (40, 14)], 'ear', 'b', ln=True), L([(88, 28), (82, -8), (60, 14)], 'ear', 'b', ln=True)] + gasmask('back', moss=False),
}
# Harry Boufante: melena castaña larga a los lados de una máscara musgosa con gafas grandes y un tubo de respiración
CHARS['harry-boufante'] = {
    'body': 'normal', 'pal': mpal(hair='#5a4a34', filt='#6a6070'), 'face': NOFACE,
    'front': [L(blob([(4, 120), (0, 50), (14, 10), (50, 0), (86, 10), (100, 50), (96, 120), (82, 116), (84, 60), (16, 60), (18, 116)]))]
             + gasmask('front', (32, 56, 13, 9), None, extra_f=[L(blob([(42, 82), (58, 82), (60, 120), (40, 120)]), 'filt', 'f', ln=True)]
                                                               + [L([(41, y), (59, y)], (70, 60, 80, 255), 'f', False, False, 1.2) for y in (90, 98, 106, 114)]),
    'side': [L(blob([(30, 120), (0, 110), (-4, 50), (14, 10), (40, 6), (30, 60)]))] + gasmask('side', (32, 56, 13, 9), None),
    'back': [L(blob([(4, 122), (0, 50), (14, 10), (50, 0), (86, 10), (100, 50), (96, 122), (50, 126)]))] + gasmask('back')
            + [strand([(x, 40), (x, 120)], 'shade', 'f', 1.0) for x in (20, 36, 64, 80)],
}
# Todd Stuhl (corpulento): máscara gris verdosa con un sombrerito, ojos amarillos enormes y filtro redondo negro
CHARS['todd-stuhl'] = {
    'body': 'corpulento', 'pal': mpal(mask='#d8d0bc', moss='#3e6a5a', lens='#e8c020', filt='#2a2a2a', hat='#3e6a5a'), 'face': NOFACE,
    'front': gasmask('front', (30, 58, 13, 10), 14, moss=False) + [L(blob([(14, 22), (50, 8), (86, 22), (92, 30), (8, 30)]), 'hat', 'f', ln=True)],
    'side': gasmask('side', (30, 58, 13, 10), 14, moss=False) + [L(blob([(16, 20), (50, 6), (90, 18), (96, 28), (14, 30)]), 'hat', 'f', ln=True)],
    'back': gasmask('back', moss=False) + [L(blob([(14, 22), (50, 8), (86, 22), (92, 30), (8, 30)]), 'hat', 'f', ln=True)],
}
# Aspen Blewit: máscara de tela con orejas de gato y manchas rosas, ojos oscuros; la boca al aire
CHARS['aspen-blewit'] = {
    'body': 'chica', 'pal': mpal(moss='#b06a6a'), 'face': {**NOFACE, 'mouth': 'frown', 'mouth_y': 98},
    'front': [L([(0, 30), (2, 0), (30, 12)], 'mask', 'b', ln=True), L([(100, 30), (98, 0), (70, 12)], 'mask', 'b', ln=True)] + gasmask('front', (32, 58, 11, 10), None, jaw=True),
    'side': [L([(26, 20), (30, -8), (54, 10)], 'mask', 'b', ln=True)] + gasmask('side', (32, 58, 11, 10), None, jaw=True),
    'back': [L([(0, 30), (2, 0), (30, 12)], 'mask', 'b', ln=True), L([(100, 30), (98, 0), (70, 12)], 'mask', 'b', ln=True)] + gasmask('back'),
}
# Marismus Oregon (corpulento): calavera de piedra con musgo, ojos hundidos y una dentadura enorme
CHARS['marismus-oregon'] = {
    'body': 'corpulento', 'pal': mpal(lens='#1e2a2a'), 'face': NOFACE,
    'front': gasmask('front', (32, 58, 11, 10), None, extra_f=[L(blob([(28, 86), (72, 86), (68, 104), (32, 104)]), (240, 230, 200, 255), 'f', ln=True)]
                                                         + [L([(x, 86), (x, 104)], OUTC, 'f', False, False, 1.0) for x in (38, 46, 54, 62)]),
    'side': gasmask('side', (32, 58, 11, 10), None), 'back': gasmask('back'),
}
# Scaber Enoki (corpulento): piel morena, gafas de soldador con cristales rojos sobre un casco musgoso con hierbas
CHARS['scaber-enoki'] = {
    'body': 'corpulento', 'pal': mpal(lens='#c02020', skin='#a06a44'), 'face': {**NOFACE, 'mouth': 'frown', 'mouth_y': 96, 'ears': True},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(10, 50), (12, 18), (50, 4), (88, 18), (90, 50), (50, 40)]), 'mask', 'f', ln=True),
              L(bumpy(40, 20, 22, 10, 6, 0.15), 'moss', 'f', False), spk((20, 14), (26, 12), (14, -6), 2), spk((76, 12), (82, 14), (88, -6), 2, light_left=False),
              L(ell(34, 66, 11, 10), DARK, 'f', ln=True), L(ell(66, 66, 11, 10), DARK, 'f', ln=True),
              L(ell(34, 66, 7, 6), 'lens', 'f', False), L(ell(66, 66, 7, 6), 'lens', 'f', False), L([(45, 64), (55, 64)], DARK, 'f', False, False, 2)],
    'side': [L(blob(SIDE_SKULL), 'skin'), L(blob([(12, 52), (12, 20), (40, 4), (80, 10), (94, 34), (92, 50), (50, 44)]), 'mask', 'f', ln=True),
             L(ell(86, 66, 7, 10), DARK, 'f', ln=True), L(ell(87, 66, 4.6, 6), 'lens', 'f', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(10, 56), (12, 18), (50, 4), (88, 18), (90, 56), (50, 52)]), 'mask', 'f', ln=True),
             L(bumpy(50, 22, 24, 10, 6, 0.15), 'moss', 'f', False), L(quad((10, 64), (50, 70), (90, 64)), 'strap', 'f', False, False, 3)],
}
# Garjan Cypress: máscara tapada de musgo como un montículo, con un bonsái creciendo encima
TREE = [L(quad((56, 4), (60, -14), (66, -24)), (90, 60, 30, 255), 'f', False, False, 3),
        L(bumpy(70, -28, 18, 8, 7, 0.15), (40, 110, 40, 255), 'f', ln=True), L(bumpy(52, -22, 10, 5, 6, 0.15), (40, 110, 40, 255), 'f', ln=True)]
CHARS['garjan-cypress'] = {
    'body': 'normal', 'pal': mpal(mask='#8aa040', moss='#6a8a2a'), 'face': NOFACE,
    'front': gasmask('front', (32, 62, 11, 9), None) + TREE, 'side': gasmask('side', (32, 62, 11, 9), None) + TREE, 'back': gasmask('back') + TREE,
}
# Judas Deathcap: máscara musgosa con una seta roja de lunares en lo alto y un filtro amarillo
SHROOM = [L(blob([(20, 14), (40, -10), (70, -12), (90, 6), (86, 16), (24, 20)]), (200, 60, 30, 255), 'f', ln=True),
          L(ell(40, 0, 4, 3), (250, 230, 200, 255), 'f', False), L(ell(66, -2, 5, 3), (250, 230, 200, 255), 'f', False)]
CHARS['judas-deathcap'] = {
    'body': 'normal', 'pal': mpal(filt='#e8c040'), 'face': NOFACE,
    'front': gasmask('front', (32, 62, 11, 10), 13) + SHROOM, 'side': gasmask('side', (32, 62, 11, 10), 13) + SHROOM, 'back': gasmask('back') + SHROOM,
}
# Chase Faithfull (corpulento): máscara pequeña con un ojo rojo y bigote; piel morena
CHARS['chase-faithfull'] = {
    'body': 'corpulento', 'pal': mpal(skin='#b0703e', lens='#c03030'), 'face': NOFACE,
    'front': gasmask('front', (32, 60, 10, 9), None, jaw=True, extra_f=[L(blob([(32, 88), (50, 84), (68, 88), (60, 94), (40, 94)]), (80, 60, 90, 255), 'f', ln=True)]),
    'side': gasmask('side', (32, 60, 10, 9), None, jaw=True), 'back': gasmask('back'),
}
# Roy Daring: máscara de piedra con un cuerno en lo alto y dos alas de musgo a los lados; la barbilla al aire
CHARS['roy-daring'] = {
    'body': 'normal', 'pal': mpal(skin='#c08050', moss='#8a9a3a'), 'face': {**NOFACE, 'mouth': 'frown', 'mouth_y': 98},
    'front': [L([(0, 30), (-8, 8), (30, 14)], 'moss', 'b', ln=True), L([(100, 30), (108, 8), (70, 14)], 'moss', 'b', ln=True)]
             + gasmask('front', (32, 58, 11, 10), None, jaw=True) + [L([(44, 8), (50, -16), (56, 8)], 'mask', 'f', ln=True)],
    'side': [L([(26, 20), (14, 0), (50, 8)], 'moss', 'b', ln=True)] + gasmask('side', (32, 58, 11, 10), None, jaw=True) + [L([(44, 6), (52, -16), (60, 6)], 'mask', 'f', ln=True)],
    'back': [L([(0, 30), (-8, 8), (30, 14)], 'moss', 'b', ln=True), L([(100, 30), (108, 8), (70, 14)], 'moss', 'b', ln=True)]
            + gasmask('back') + [L([(44, 8), (50, -16), (56, 8)], 'mask', 'f', ln=True)],
}

# ------------------------------------------------------------------ Robots Guardias: todos el mismo robot con pelo rosa, un pelillo
# arriba, cinta oscura con un piloto rojo en la frente y gafas redondas de cristal blanco
ROBOT = {
    'body': 'normal', 'pal': pal('#d87a70', '#fcd0a4', band='#2a2440', led='#e04a4a', lens='#f4f4f8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (62, 54)},
    'front': [spk((46, 10), (54, 8), (58, -18), 3, light_left=False),
              L(blob([(10, 84), (6, 46), (16, 14), (50, 4), (84, 14), (94, 46), (90, 84), (80, 80), (80, 62), (20, 62), (20, 80)])),
              L(blob([(62, 12), (92, 44), (88, 82), (82, 80)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              L(blob([(12, 52), (12, 38), (50, 34), (88, 38), (88, 52), (50, 50)]), 'band', 'f', ln=True), L(ell(50, 42, 4, 4), 'led', 'f', ln=True),
              spk((12, 50), (24, 52), (16, 82), 4, z='f'), spk((76, 52), (88, 50), (84, 82), 4, z='f', light_left=False),
              L(ell(36, 74, 8, 7), 'lens', 'f', ln=True), L(ell(64, 74, 8, 7), 'lens', 'f', ln=True), L([(44, 73), (56, 73)], OUTC, 'f', False, False, 1.2),
              L(ell(36, 74, 3.4, 2.6), (160, 160, 170, 255), 'f', False), L(ell(64, 74, 3.4, 2.6), (160, 160, 170, 255), 'f', False)],
    'side': [spk((40, 8), (48, 6), (52, -18), 3, light_left=False),
             L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False),
             L(quad((8, 44), (50, 34), (94, 38)) + quad((94, 50), (50, 46), (8, 56)), 'band', 'f', ln=True),
             L(ell(86, 74, 5, 7), 'lens', 'f', ln=True), L([(80, 72), (56, 70)], OUTC, 'f', False, False, 1.2)],
    'back': [spk((46, 10), (54, 8), (58, -18), 3, light_left=False),
             L(blob([(10, 86), (6, 46), (16, 14), (50, 4), (84, 14), (94, 46), (90, 86), (50, 92)])),
             L(blob([(58, 12), (92, 44), (88, 84), (66, 90)], 6), 'shade', 'b', False),
             L(quad((6, 40), (50, 34), (94, 40)) + quad((94, 54), (50, 48), (6, 54)), 'band', 'f', ln=True)],
}
for _r in 'sptvclobgkf':
    CHARS[f'robot-{_r}'] = ROBOT

# Chris Ticker (sin modelo 3D; su retrato): casco redondo de piedra con enredaderas, una visera oscura ancha con un piloto
# rojo y un filtro verde bajo la barbilla
VINES = [L(quad((24, 20), (40, 40), (30, 86)), 'moss', 'f', False, False, 2.4), L(quad((60, 10), (80, 30), (74, 60)), 'moss', 'f', False, False, 2.4)]
CHARS['chris-ticker'] = {
    'body': 'normal', 'pal': mpal(filt='#3e6a3a', lens='#123040'), 'face': NOFACE,
    'front': gasmask('front', (32, 62, 1, 1), 12, moss=False)
             + [L(blob([(16, 50), (50, 42), (84, 50), (82, 76), (50, 82), (18, 76)]), 'lens', 'f', ln=True), L(ell(60, 62, 4, 4), (230, 40, 30, 255), 'f', ln=True)] + VINES,
    'side': gasmask('side', (32, 62, 6, 12), 12, moss=False) + [L(ell(88, 62, 3, 3), (230, 40, 30, 255), 'f', False)],
    'back': gasmask('back') + VINES,
}
