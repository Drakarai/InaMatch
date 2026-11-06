"""Kasamino / Instituto Umbrella (IE1): gafas de mosca de Greg, cinta tapaojos de Joe, tupé de Lou y demás peinados, con sus
modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
# media melena genérica (frente, perfil, espalda) para los que la llevan
BOB_F = [(8, 84), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 84), (80, 80), (80, 62), (20, 62), (20, 80)]
BOB_S = [(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)]
BOB_B = [(8, 86), (4, 48), (14, 16), (50, 6), (86, 16), (96, 48), (92, 86), (50, 92)]


def bob_shade(view):
    if view == 'front':
        return [L(blob([(62, 12), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)]
    if view == 'side':
        return [L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3)]
    return [L(blob([(58, 12), (94, 46), (92, 84), (66, 90)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)]


def fringe(n=4, y0=40, y1=66, x0=12, x1=88):
    """Flequillo de mechones en punta."""
    w = (x1 - x0) / n
    out = []
    for i in range(n):
        a, b = (x0 + w * i, y0 + abs(i - (n - 1) / 2) * 1.5), (x0 + w * (i + 1), y0 + abs(i + 1 - n / 2) * 1.5)
        out += spk(a, b, ((a[0] + b[0]) / 2 + (-3 if i < n / 2 else 3), y1), 5, z='f', light_left=i < n / 2)
    return out


def spiky(view, n_back=4):
    """Pelo de pinchos medianos: arriba y a los lados (frente/espalda) o hacia atrás (perfil)."""
    if view == 'side':
        return [spk((16, 40), (22, 22), (-12, 22), 6), spk((24, 22), (42, 10), (14, -12), 6), spk((42, 10), (62, 6), (52, -16), 6),
                spk((14, 58), (16, 40), (-12, 54), 5), spk((18, 74), (22, 58), (-4, 80), 4)]
    return [spk((8, 58), (12, 40), (-10, 46), 6), spk((14, 36), (28, 18), (0, 6), 6), spk((28, 18), (46, 8), (30, -14), 6),
            spk((46, 8), (62, 10), (62, -16), 6, light_left=False), spk((62, 12), (78, 22), (94, 0), 6, light_left=False),
            spk((80, 28), (90, 46), (110, 38), 6, light_left=False)]


# ------------------------------------------------------------------ Joe Ingram (portero): un pañuelo rojo enrollado en la cabeza
# que le tapa los ojos (con un parche amarillo a un lado) y pelo gris verdoso que asoma abultado por los lados y la nuca;
# nariz y sonrisa con un diente
CHARS['joe-ingram'] = {
    'body': 'normal', 'pal': pal('#3e4440', '#fcc080', wrap='#b0300c', wrap_d='#7a1e06', patch='#e8c830'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'buck', 'mouth_y': 93, 'nose': (50, 82, 3), 'nose_side': (92, 80, 3), 'hairline': False},
    'front': [L(bumpy(10, 74, 12, 14, 6, 0.1)), L(bumpy(90, 74, 12, 14, 6, 0.1)),
              L(blob([(10, 80), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 80)]), 'shade'),
              L(blob([(10, 78), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (90, 78), (50, 82)]), 'wrap', 'f', ln=True),
              L(blob([(60, 6), (90, 34), (90, 76), (70, 78)], 6), 'wrap_d', 'f', False)]
             + [L(quad((10, y), (50, y - 8), (90, y)), 'wrap_d', 'f', False, False, 1.2) for y in (30, 48, 64)]
             + [L(blob([(74, 14), (90, 26), (92, 50), (80, 40)], 5), 'patch', 'f', ln=True)],
    'side': [L(bumpy(22, 76, 18, 16, 8, 0.1)), L(blob(SIDE_SKULL), 'shade'),
             L(blob([(12, 78), (8, 40), (20, 12), (50, 2), (80, 8), (94, 30), (96, 78), (60, 80)]), 'wrap', 'f', ln=True),
             L(blob([(12, 40), (24, 14), (30, 60), (20, 76)], 6), 'wrap_d', 'f', False)]
            + [L(quad((10, y), (50, y - 6), (96, y)), 'wrap_d', 'f', False, False, 1.2) for y in (30, 48, 64)],
    'back': [L(bumpy(50, 82, 40, 16, 12, 0.08)), L(bumpy(66, 86, 18, 10, 6, 0.08), 'shade', 'b', False),
             L(blob([(10, 80), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (90, 80), (50, 84)]), 'wrap', 'f', ln=True),
             L(blob([(56, 6), (90, 34), (90, 78), (64, 82)], 6), 'wrap_d', 'f', False)]
            + [L(quad((10, y), (50, y - 8), (90, y)), 'wrap_d', 'f', False, False, 1.2) for y in (30, 48, 64)],
}

# ------------------------------------------------------------------ Kendall Sefton: pelo gris morado oscuro de pinchos despeinados
# en todas direcciones; ojos grandes y ceño
CHARS['kendall-sefton'] = {
    'body': 'normal', 'pal': pal('#3e3440', '#fcc8a0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': spiky('front') + [L(blob([(8, 74), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 74), (80, 66), (20, 66)])),
                               spk((4, 64), (12, 76), (-6, 84), 4), spk((88, 76), (96, 64), (106, 84), 4, light_left=False),
                               L(blob([(62, 12), (92, 38), (90, 70), (78, 66)], 6), 'shade', 'b', False)] + fringe(5),
    'side': spiky('side') + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
                             spk((60, 12), (80, 22), (90, -4), 5, light_left=False), spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False)],
    'back': spiky('back') + [L(blob([(8, 76), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 76), (66, 88), (34, 88)])),
                             spk((10, 74), (30, 86), (6, 98), 5), spk((30, 88), (50, 90), (40, 106), 5), spk((50, 90), (70, 88), (62, 106), 5, light_left=False),
                             spk((70, 86), (90, 74), (94, 98), 5, light_left=False),
                             L(blob([(58, 12), (92, 38), (90, 74), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Jason Strike: melena lisa castaña hasta la mandíbula peinada
# con raya en medio y mechones marcados; ojos afilados y sonrisa
CHARS['jason-strike'] = {
    'body': 'normal', 'pal': pal('#6a4024', '#fcb878'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(10, 66), (24, 54), (40, 48), (50, 52), (60, 48), (76, 54), (90, 66)]},
    'front': [L(blob(BOB_F))] + bob_shade('front') + [strand([(x, 8 + abs(x - 50) * 0.3), (x + (x - 50) * 0.25, 50)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)]
             + [L(blob([(10, 58), (20, 58), (22, 86), (12, 86)]), 'mid', 'f'), L(blob([(90, 58), (80, 58), (78, 86), (88, 86)]), 'mid', 'f'),
                strand([(20, 60), (21, 86)], OUTC, 'f', 1.0), strand([(80, 60), (79, 86)], OUTC, 'f', 1.0)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [strand([(84, 20 + k * 6), (50, 12 + k * 6), (24, 40 + k * 10), (20, 88)], 'deep', 'b', 1.0) for k in range(3)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [strand([(x, 10), (x + (x - 50) * 0.15, 86)], 'deep', 'b', 1.0) for x in (26, 38, 50, 62, 74)],
}

# ------------------------------------------------------------------ Norman Porter: corpulento, pelo gris muy corto en cepillo con
# una franja más oscura arriba; ojos pequeños, nariz roja y boca enfurruñada
CHARS['norman-porter'] = {
    'body': 'corpulento', 'pal': pal('#7a8278', '#fcc080', top='#4a4e58', nose='#d0603a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 1, 'ear_out': 3, 'nose': (50, 84, 3.2),
             'nose_side': (92, 82, 3), 'hairline': (54, 44)},
    'front': [L(blob([(14, 60), (12, 34), (24, 14), (50, 8), (76, 14), (88, 34), (86, 60)])),
              L(blob([(62, 14), (88, 34), (86, 58), (74, 54)], 6), 'shade', 'b', False),
              L(blob([(24, 16), (50, 6), (76, 16), (72, 24), (50, 18), (28, 24)]), 'top', 'b', ln=True)],
    'side': [L(blob([(44, 70), (20, 70), (12, 50), (16, 30), (30, 14), (56, 8), (78, 16), (88, 32), (76, 38), (60, 40), (50, 52)])),
             L(blob([(16, 40), (20, 64), (38, 68), (28, 50)], 6), 'shade', 'b', False),
             L(blob([(26, 18), (50, 4), (80, 12), (76, 20), (50, 14), (30, 26)]), 'top', 'b', ln=True),
             L([(78, 82), (84, 84)], OUTC, 'f', False, False, 1.0), L([(78, 86), (84, 87)], OUTC, 'f', False, False, 1.0)],
    'back': [L(blob(SKULL_B))] + back_hair() + [L(blob([(24, 16), (50, 6), (76, 16), (72, 24), (50, 18), (28, 24)]), 'top', 'b', ln=True)],
}

# ------------------------------------------------------------------ Maxwell Claus: piel tostada y cara alargada, con un pelo rosa
# parduzco abombado y alto como una seta y un brote de pelo en lo alto; ojos redondos y boca hacia abajo
MAX_FACE = quad((20, 54), (17, 102), (50, 110)) + quad((50, 110), (83, 102), (80, 54))[1:] + quad((80, 54), (50, 30), (20, 54))[1:-1]
CHARS['maxwell-claus'] = {
    'body': 'normal', 'pal': pal('#a86a64', '#c8903e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'eye_y': 74, 'face_front': MAX_FACE, 'nose': (50, 86, 2.4),
             'hairline': (60, 54)},
    'front': [spk((46, -8), (52, -8), (54, -18), 2, light_left=False),
              L(bumpy(50, 30, 46, 34, 16, 0.07)), L(bumpy(66, 32, 22, 26, 8, 0.06), 'shade', 'b', False), L(ell(32, 12, 10, 5), 'light', 'b', False)],
    'side': [spk((44, -8), (50, -8), (50, -18), 2), L(bumpy(46, 30, 44, 34, 14, 0.06)),
             L(bumpy(28, 40, 22, 26, 8, 0.06), 'shade', 'b', False)],
    'back': [spk((46, -8), (52, -8), (54, -18), 2, light_left=False),
             L(bumpy(50, 34, 46, 40, 16, 0.07)), L(bumpy(66, 36, 22, 28, 8, 0.06), 'shade', 'b', False), L(ell(32, 14, 10, 5), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Alan Most: corpulento, pelo castaño oliva con mechones rizados
# que salen hacia los lados como alas y un rizo en lo alto; ojos redondos pequeños
CHARS['alan-most'] = {
    'body': 'corpulento', 'pal': pal('#7a6a30', '#fcc080'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 94, 'hairline': (56, 46)},
    'front': [L(blob([(48, 10), (44, -4), (50, -12), (58, -10), (54, -4), (54, 10)]), 'mid', 'b', ln=True),
              L(blob([(16, 60), (14, 34), (26, 14), (50, 8), (74, 14), (86, 34), (84, 60)])),
              L(blob([(62, 14), (86, 34), (84, 58), (72, 54)], 6), 'shade', 'b', False),
              L(blob([(16, 50), (4, 42), (-8, 46), (2, 50), (-4, 58), (8, 58), (18, 60)]), 'mid', 'b', ln=True),
              L(blob([(84, 50), (96, 42), (108, 46), (98, 50), (104, 58), (92, 58), (82, 60)]), 'mid', 'b', ln=True)],
    'side': [L(blob([(44, 8), (44, -6), (52, -12), (58, -6), (52, -4), (52, 8)]), 'mid', 'b', ln=True),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(48, 52), (58, 40), (72, 38), (62, 46), (64, 60), (54, 60)]), 'mid', 'f', ln=True)],
    'back': [L(blob([(48, 10), (44, -4), (50, -12), (58, -10), (54, -4), (54, 10)]), 'mid', 'b', ln=True),
             L(blob(SKULL_B))] + back_hair() + [
             L(blob([(16, 50), (4, 42), (-8, 46), (2, 50), (-4, 58), (8, 58), (18, 60)]), 'mid', 'b', ln=True),
             L(blob([(84, 50), (96, 42), (108, 46), (98, 50), (104, 58), (92, 58), (82, 60)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Bruce Chaney: piel tostada, pelo gris azulado oscuro abultado
# y despeinado hacia un lado, con un flequillo de mechones largos sobre los ojos; mirada afilada
CHARS['bruce-chaney'] = {
    'body': 'normal', 'pal': pal('#3e4a5e', '#c8904a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': [L(blob([(4, 76), (0, 44), (12, 14), (50, 4), (88, 14), (100, 44), (96, 76), (82, 68), (82, 62), (18, 62), (18, 68)])),
              spk((0, 60), (8, 70), (-16, 62), 4), spk((92, 70), (100, 58), (114, 66), 4, light_left=False),
              L(blob([(62, 10), (98, 44), (96, 74), (84, 70)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3),
              spk((10, 44), (30, 36), (16, 68), 5, z='f'), spk((30, 36), (52, 32), (40, 68), 6, z='f'),
              spk((52, 32), (72, 36), (64, 66), 5, z='f', light_left=False), spk((70, 38), (92, 44), (90, 70), 5, z='f', light_left=False)],
    'side': [L(blob(BOB_S)), spk((4, 66), (10, 80), (-12, 84), 4)] + bob_shade('side') + [spk((56, 30), (90, 40), (94, 70), 6, z='f', light_left=False)],
    'back': [L(blob([(4, 80), (0, 44), (12, 14), (50, 4), (88, 14), (100, 44), (96, 80), (50, 88)])),
             spk((0, 60), (8, 70), (-16, 62), 4), spk((92, 70), (100, 58), (114, 66), 4, light_left=False),
             spk((10, 78), (30, 86), (12, 98), 5), spk((30, 86), (50, 88), (40, 102), 5), spk((50, 88), (70, 86), (62, 102), 5, light_left=False),
             spk((70, 86), (90, 78), (90, 98), 5, light_left=False)] + bob_shade('back'),
}

# ------------------------------------------------------------------ Leroy Rhymes: bajito, pelo verde oliva muy oscuro de pinchos
# hacia arriba; ojos redondos, nariz roja y pecas
CHARS['leroy-rhymes'] = {
    'body': 'bajito', 'pal': pal('#32301e', '#fcc090', nose='#e0603a', freckle='#c88a5a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 83, 2.4), 'hairline': (58, 50)},
    'front': spiky('front') + [L(blob([(10, 70), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
                               L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False)] + fringe(4)
             + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (74, 86), (70, 88))],
    'side': spiky('side') + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
                             spk((60, 12), (80, 22), (92, -4), 5, light_left=False), spk((56, 30), (88, 40), (92, 64), 6, z='f', light_left=False)],
    'back': spiky('back') + [L(blob([(10, 72), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
                             spk((12, 72), (30, 84), (10, 96), 5), spk((30, 86), (50, 88), (40, 102), 5), spk((50, 88), (70, 86), (62, 102), 5, light_left=False),
                             spk((70, 84), (88, 72), (90, 96), 5, light_left=False),
                             L(blob([(58, 12), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Mildford Scott: pelo castaño rojizo abombado como una seta,
# gafas redondas de montura roja con los ojos muy abiertos y una sonrisa de oreja a oreja
CHARS['mildford-scott'] = {
    'body': 'normal', 'pal': pal('#6a2e14', '#fcc08a', rim='#c03a2a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 91, 'mouth_w': 12, 'hairline': (62, 56)},
    'front': [L(blob([(2, 70), (0, 40), (14, 12), (50, 4), (86, 12), (100, 40), (98, 70), (82, 64), (82, 62), (18, 62), (18, 64)])),
              L(blob([(62, 10), (98, 40), (96, 68), (84, 64)], 6), 'shade', 'b', False), sheen(18, 46, 16, 3)]
             + [strand([(x, 16 + abs(x - 50) * 0.2), (x + (x - 50) * 0.1, 60)], 'deep', 'b', 1.0) for x in (24, 40, 60, 76)]
             + [L(ell(36, 75, 9.4, 8.4), 'rim', 'f', False), L(ell(64, 75, 9.4, 8.4), 'rim', 'f', False),
                L(ell(36, 75, 7, 6.2), WHITE, 'f', False), L(ell(64, 75, 7, 6.2), WHITE, 'f', False),
                L(ell(37, 75, 2.6, 2.8), OUTC, 'f', False), L(ell(63, 75, 2.6, 2.8), OUTC, 'f', False),
                L([(45, 74), (55, 74)], 'rim', 'f', False, False, 1.6), L(quad((34, 88), (50, 98), (66, 88)), (130, 70, 50, 255), 'f', False, False, 1.6)],
    'side': [L(blob([(46, 84), (12, 82), (0, 54), (6, 24), (28, 6), (60, 2), (88, 14), (100, 36), (96, 58), (76, 56), (62, 58), (54, 70)])),
             L(blob([(6, 44), (10, 78), (40, 82), (22, 58)], 6), 'shade', 'b', False), sheen(30, 64, 12, 3),
             L(ell(84, 75, 6, 8), 'rim', 'f', False), L(ell(85, 75, 4, 6), WHITE, 'f', False), L(ell(86, 75, 1.8, 2.4), OUTC, 'f', False),
             L([(78, 73), (52, 70)], 'rim', 'f', False, False, 1.4)],
    'back': [L(blob([(2, 74), (0, 40), (14, 12), (50, 4), (86, 12), (100, 40), (98, 74), (50, 82)])),
             L(blob([(58, 10), (98, 40), (96, 72), (66, 80)], 6), 'shade', 'b', False), sheen(18, 46, 16, 3),
             L(blob([(14, 70), (86, 70), (82, 80), (18, 80)]), 'deep', 'b', False)],
}

# ------------------------------------------------------------------ Lou Edmonds: tupé rubio enrollado altísimo que sale hacia
# delante, lados cortos; ojos cerrados de felicidad y sonrisa
CHARS['lou-edmonds'] = {
    'body': 'normal', 'pal': pal('#dcc890', '#f6b878'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'big_ears': 1, 'hairline': (56, 46)},
    'front': [L(blob([(16, 60), (14, 34), (26, 16), (50, 10), (74, 16), (86, 34), (84, 60)])),
              L(blob([(62, 16), (86, 34), (84, 58), (72, 54)], 6), 'shade', 'b', False),
              L(blob([(32, 40), (28, 16), (34, -4), (50, -14), (66, -4), (72, 16), (68, 40), (50, 46)]), 'mid', 'b', ln=True),
              L(blob([(54, -10), (66, -4), (70, 18), (62, 38), (58, 14)], 5), 'shade', 'b', False),
              L(quad((36, 34), (50, 28), (64, 34)), 'shade', 'b', False, False, 1.4), L(ell(42, 4, 5, 3), 'light', 'b', False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(28, 30), (24, 10), (40, -4), (66, -8), (88, -2), (100, 10), (96, 22), (82, 26), (70, 36), (50, 34)]), 'mid', 'b', ln=True),
             L(blob([(30, 24), (40, 4), (60, 0), (50, 14), (44, 30)], 5), 'shade', 'b', False),
             L(quad((90, 6), (96, 16), (88, 22)), 'shade', 'b', False, False, 1.4)],
    'back': [L(blob(SKULL_B))] + back_hair() + [
             L(blob([(28, 50), (24, 16), (34, -4), (50, -14), (66, -4), (76, 16), (72, 50), (50, 58)]), 'mid', 'b', ln=True),
             L(blob([(54, -10), (66, -4), (74, 18), (68, 48), (56, 54)], 5), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Greg Bernard: pelo rubio de pinchos hacia arriba, una cinta
# negra con rayas doradas en la frente y unas gafas enormes de cristal verde reticulado, como ojos de mosca; sonrisa
CHARS['greg-bernard'] = {
    'body': 'normal', 'pal': pal('#d8b040', '#f6b878', band='#22201e', gold='#c8a040', lens='#5a7a4a', lens_d='#2e4a2a', rim='#c8b8a0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [spk((14, 44), (24, 26), (2, 4), 5), spk((24, 26), (40, 18), (26, -14), 5), spk((40, 18), (56, 16), (46, -22), 5),
              spk((54, 16), (70, 20), (72, -14), 5, light_left=False), spk((68, 22), (82, 30), (98, 4), 5, light_left=False),
              spk((80, 34), (88, 46), (106, 30), 4, light_left=False),
              L(blob([(14, 62), (12, 40), (24, 24), (50, 18), (76, 24), (88, 40), (86, 62)])),
              L(quad((10, 46), (50, 38), (90, 46)) + quad((90, 64), (50, 56), (10, 64)), 'band', 'f', ln=True),
              L(quad((10, 52), (50, 44), (90, 52)), 'gold', 'f', False, False, 1.4), L(quad((10, 58), (50, 50), (90, 58)), 'gold', 'f', False, False, 1.4)]
             + [x for cx in (32, 68) for x in (L(ell(cx, 76, 15, 11), 'rim', 'f', ln=True), L(ell(cx, 76, 12.5, 9), 'lens', 'f', False),
                                               L(quad((cx - 11, 72), (cx, 82), (cx + 11, 72)), 'lens_d', 'f', False, False, 1.0),
                                               L(quad((cx - 11, 80), (cx, 70), (cx + 11, 80)), 'lens_d', 'f', False, False, 1.0),
                                               L([(cx, 67), (cx, 85)], 'lens_d', 'f', False, False, 1.0))],
    'side': [spk((22, 30), (36, 20), (8, 2), 5), spk((36, 20), (52, 16), (34, -14), 5), spk((52, 16), (68, 18), (62, -16), 5, light_left=False),
             spk((14, 46), (22, 30), (-4, 26), 5),
             L(blob(SIDE_SKULL), 'band'), L(blob([(20, 30), (40, 16), (66, 16), (84, 26), (60, 30), (34, 40)])),
             L(quad((14, 44), (50, 36), (90, 42)) + quad((90, 60), (50, 54), (14, 64)), 'band', 'f', ln=True),
             L(quad((14, 52), (50, 44), (90, 50)), 'gold', 'f', False, False, 1.4),
             L(ell(86, 76, 8, 11), 'rim', 'f', ln=True), L(ell(88, 76, 5.4, 8.4), 'lens', 'f', False)],
    'back': [spk((14, 44), (24, 26), (2, 4), 5), spk((24, 26), (40, 18), (26, -14), 5), spk((40, 18), (56, 16), (46, -22), 5),
             spk((54, 16), (70, 20), (72, -14), 5, light_left=False), spk((68, 22), (82, 30), (98, 4), 5, light_left=False),
             L(blob(SKULL_B), 'band'), L(blob([(14, 50), (12, 36), (24, 22), (50, 16), (76, 22), (88, 36), (86, 50)])),
             L(quad((10, 48), (50, 42), (90, 48)) + quad((90, 66), (50, 60), (10, 66)), 'band', 'f', ln=True),
             L(quad((10, 54), (50, 48), (90, 54)), 'gold', 'f', False, False, 1.4), L(quad((10, 60), (50, 54), (90, 60)), 'gold', 'f', False, False, 1.4)],
}

# ------------------------------------------------------------------ Cameron Morefield: pelo castaño claro con un gran flequillo
# barrido hacia un lado y puntas sueltas en la nuca; ojos afilados y sonrisa
CHARS['cameron-morefield'] = {
    'body': 'normal', 'pal': pal('#9a7460', '#fcc08a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + [
              spk((86, 50), (94, 40), (108, 52), 4, light_left=False),
              spk((24, 28), (56, 20), (12, 64), 7, z='f'), spk((50, 22), (78, 26), (24, 58), 7, z='f', light_left=False),
              spk((72, 30), (90, 40), (102, 34), 6, z='f', light_left=False), spk((80, 42), (90, 50), (84, 74), 3, z='f', light_left=False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((50, 22), (80, 28), (102, 30), 7, z='f', light_left=False),
             spk((58, 34), (88, 40), (92, 66), 5, z='f', light_left=False), spk((2, 74), (12, 86), (-8, 92), 4)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [
             spk((10, 80), (28, 88), (4, 98), 5), spk((28, 88), (48, 90), (34, 106), 5), spk((52, 90), (72, 88), (64, 106), 5, light_left=False),
             spk((72, 88), (90, 80), (98, 98), 5, light_left=False), spk((14, 50), (6, 40), (-8, 54), 4, light_left=False)],
}

# ------------------------------------------------------------------ Peter Banker (portero suplente): media melena azul marino muy
# oscura con flequillo de mechones largos y mirada aburrida de párpados caídos
CHARS['peter-banker'] = {
    'body': 'normal', 'pal': pal('#2e2a48', '#fcc08a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'eye_y': 77, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 38, 70) + [
              L([(28, 73), (44, 74)], OUTC, 'f', False, False, 2.4), L([(72, 73), (56, 74)], OUTC, 'f', False, False, 2.4),
              spk((10, 76), (20, 78), (14, 96), 3), spk((80, 78), (90, 76), (86, 96), 3, light_left=False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 76), 6, z='f', light_left=False), spk((50, 54), (60, 54), (56, 92), 3, z='f')],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [spk((30, 86), (50, 92), (40, 104), 4), spk((50, 92), (70, 86), (60, 104), 4, light_left=False)],
}

# ------------------------------------------------------------------ Saul Tunk: corpulento, piel morena, pelo verde oliva muy
# oscuro en punta hacia arriba con dos puntas a los lados; ojos entornados y una sonrisa enorme de labios gruesos
CHARS['saul-tunk'] = {
    'body': 'corpulento', 'pal': pal('#3a3a1e', '#b0703a'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 90, 'mouth_w': 12, 'hairline': (56, 50)},
    'front': [spk((34, 14), (66, 14), (50, -10), 8),
              L(blob([(16, 60), (14, 34), (26, 14), (50, 8), (74, 14), (86, 34), (84, 60)])),
              spk((12, 52), (16, 38), (-6, 46), 4), spk((84, 38), (88, 52), (106, 46), 4, light_left=False),
              L(blob([(62, 14), (86, 34), (84, 58), (72, 54)], 6), 'shade', 'b', False)],
    'side': [spk((30, 16), (60, 10), (40, -12), 8), spk((14, 52), (18, 38), (-4, 44), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 26), (84, 34), (90, 50), 5, z='f', light_left=False)],
    'back': [spk((34, 14), (66, 14), (50, -10), 8),
             L(blob(SKULL_B)), spk((12, 52), (16, 38), (-6, 46), 4), spk((84, 38), (88, 52), (106, 46), 4, light_left=False)] + back_hair(),
}

# ------------------------------------------------------------------ Paul Caperock: pelo verde de pinchos con mechones en punta sobre
# la frente, una cicatriz en la frente, arañazos en las mejillas y ojos entornados
CHARS['paul-caperock'] = {
    'body': 'normal', 'pal': pal('#5a8a3a', '#fcc08a', scar='#b06040'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': [spk((38, 12), (48, 8), (32, -8), 4), spk((46, 8), (56, 8), (52, -16), 4), spk((54, 8), (64, 12), (70, -6), 4, light_left=False),
              L(blob([(10, 68), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 68), (80, 62), (20, 62)])),
              L(blob([(62, 12), (90, 38), (88, 64), (78, 60)], 6), 'shade', 'b', False)] + fringe(4, 36, 66) + [
              L([(32, 58), (44, 52)], 'scar', 'f', False, False, 1.4), L([(36, 52), (38, 60)], 'scar', 'f', False, False, 1.0),
              L([(22, 84), (30, 88)], 'scar', 'f', False, False, 1.1), L([(22, 88), (30, 92)], 'scar', 'f', False, False, 1.1),
              L([(78, 84), (70, 88)], 'scar', 'f', False, False, 1.1), L([(78, 88), (70, 92)], 'scar', 'f', False, False, 1.1)],
    'side': [spk((34, 12), (46, 6), (30, -8), 4), spk((44, 8), (56, 6), (50, -14), 4), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 30), (88, 40), (92, 64), 6, z='f', light_left=False), L([(78, 84), (86, 88)], 'scar', 'f', False, False, 1.1)],
    'back': [spk((38, 12), (48, 8), (32, -8), 4), spk((46, 8), (56, 8), (52, -16), 4), spk((54, 8), (64, 12), (70, -6), 4, light_left=False),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Julius Molehill: bajito, corte de tazón castaño oscuro con el
# flequillo recto un poco por encima de las cejas; mirada afilada
CHARS['julius-molehill'] = {
    'body': 'bajito', 'pal': pal('#3a2a20', '#fcc08a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 68), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 68), (80, 64), (20, 64)])),
              L(blob([(62, 12), (90, 38), (88, 64), (78, 62)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              L(blob([(12, 62), (10, 40), (24, 22), (50, 16), (76, 22), (90, 40), (88, 62), (50, 60)]), 'mid', 'f', ln=True),
              L(blob([(60, 22), (86, 40), (86, 60), (70, 60)], 6), 'shade', 'f', False)]
             + [strand([(x, 30 + abs(x - 50) * 0.2), (x, 60)], 'deep', 'f', 0.9) for x in (30, 42, 54, 66)],
    'side': [L(blob([(46, 78), (16, 76), (6, 54), (10, 26), (30, 8), (58, 4), (82, 14), (94, 34), (94, 58), (78, 58), (60, 56), (52, 66)])),
             L(blob([(8, 46), (12, 72), (40, 76), (24, 58)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3)],
    'back': [L(blob([(10, 76), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 76), (50, 80)])),
             L(blob([(58, 12), (90, 38), (88, 74), (66, 78)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3)],
}
