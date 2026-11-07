"""Cascada Perfecta (cs-perfect-cascade): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente,
perfil y espalda). Los androides de El Dorado: pelo corto y pegado de colores lisos, orejas grandes y caras serias."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

BIG = {'big_ears': 2, 'ear_out': 3, 'hairline': False}


def short(view, top=2, w=0, nape=86, fr=None, frs=None, buzz=False):
    """Pelo corto y pegado: casco de altura top y anchura extra w, nuca hasta nape; fr / frs: flequillo de frente y de perfil
    (por delante de la cara). buzz: rapado (sin flequillo, el contorno sigue la cabeza)."""
    if view == 'front':
        out = [L(outline([(16 - w, 70), (12 - w, 40), (22, 14 + top / 2), (50, top), (78, 14 + top / 2), (88 + w, 40), (84 + w, 70), (80, 56), (20, 56)])),
               L(outline([(60, 4 + top), (84, 18), (90 + w, 42), (84 + w, 64), (78, 40)]), 'shade', 'b', False)]
        if fr:
            out.append(L(outline(fr), 'mid', 'f'))
        return out
    if view == 'side':
        out = [L(outline([(52, 62), (56, 50), (78, 48), (90, 34), (86, 14), (66, top), (40, top - 2), (18, 8), (6 - w, 30), (6 - w, 58), (16, nape - 8), (32, nape),
                          (46, 74)])),
               L(outline([(6 - w, 34), (24, 38), (30, nape - 10), (14, nape - 14)]), 'shade', 'b', False)]
        if frs:
            out.append(L(outline(frs), 'mid', 'f'))
        return out
    return [L(outline([(16 - w, nape - 6), (10 - w, 40), (20, 14 + top / 2), (50, top), (80, 14 + top / 2), (90 + w, 40), (84 + w, nape - 6), (50, nape + 2)])),
            L(outline([(56, 4 + top), (84, 18), (92 + w, 46), (84 + w, nape - 10), (60, nape - 2)]), 'shade', 'b', False)]


SIDE_FR = [(64, 2), (88, 14), (94, 40), (90, 56, 1), (82, 42), (72, 32)]


def ch(cid, hair, iris, fr, frs=SIDE_FR, body='normal', eyes='sharp', brows='angry', mouth='frown', top=2, w=0, nape=86, extra=None, **pk):
    face = dict(BIG, eyes=eyes, brows=brows, mouth=mouth, mouth_y=96)
    if extra:
        face.update(extra)
    CHARS[cid] = {'body': body, 'pal': pal(hair, '#fce4c8', iris=iris, **pk), 'face': face,
                  'front': short('front', top, w, nape, fr), 'side': short('side', top, w, nape, None, frs), 'back': short('back', top, w, nape)}
    return CHARS[cid]


# Vee Wai (portero): pelo malva oscuro con raya en medio y flequillo que cae en dos picos a los lados de la frente; ojos rojos
ch('vee-wai', '#7a5e62', '#c81e1e',
   [(12, 64), (14, 38), (26, 18), (50, 12), (74, 18), (86, 38), (88, 64), (82, 52), (76, 60, 1), (70, 44), (54, 40), (50, 30, 1), (46, 40), (30, 44), (24, 60, 1), (18, 52)],
   top=0)
# Dee Vee: pelo corto gris malva peinado hacia arriba en un tupé de puntas, los lados cortos
_dv = ch('dee-vee', '#8a7478', '#7a7a7a', [(14, 54), (16, 36), (28, 26), (50, 34), (72, 26), (84, 36), (86, 54), (80, 44), (20, 44)], top=4, nape=82)
_dv['front'] += [L(outline([(24, 20), (26, 4, 1), (34, 12), (40, -6, 1), (48, 8), (56, -8, 1), (62, 6), (72, -4, 1), (74, 12), (82, 4, 1), (78, 22), (50, 26)]), 'mid', 'f'),
                 L(outline([(40, 4), (60, 2), (54, 20), (44, 22)]), 'light', 'f', False)]
_dv['side'] += [L(outline([(30, 6), (34, -8, 1), (44, 2), (52, -10, 1), (58, 2), (68, -6, 1), (72, 8), (84, 4, 1), (80, 18), (50, 14)]), 'mid', 'f')]
_dv['back'] += [L(outline([(26, 16), (30, 0, 1), (40, 8), (50, -6, 1), (60, 8), (70, 0, 1), (74, 16), (50, 22)]), 'mid', 'f')]
# Ayt Bee: pelo azul claro en forma de cuenco con el flequillo recto cortado a la altura de las cejas; ojos blancos redondos
ch('ayt-bee', '#9ab8d8', '#2a2a2a',
   [(8, 66), (8, 36), (24, 12), (50, 4), (76, 12), (92, 36), (92, 66), (84, 58), (76, 60), (66, 56), (56, 60), (44, 56), (34, 60), (24, 56), (16, 60)],
   eyes='round', brows=True, top=-2, w=4, shade='#7a7a92')
# En Sicks: pelo castaño rojizo corto con el flequillo recto en escalón y las esquinas en pico sobre las sienes
ch('en-sicks', '#b0603a', '#3a5a7a',
   [(10, 66), (10, 36), (24, 12), (50, 4), (76, 12), (90, 36), (90, 66), (82, 50), (74, 54), (26, 54), (18, 50)], top=0)
# Wun Ell: pelo verde corto con el flequillo recto alto, que deja la frente al aire
ch('wun-ell', '#8ab040', '#8a6a4a', [(12, 56), (12, 34), (26, 14), (50, 8), (74, 14), (88, 34), (88, 56), (80, 46), (20, 46)], eyes='normal', brows=True,
   shade='#6a6a3a')
# Zed Kyu: pelo amarillo oliva en casco largo con raya en medio, que le tapa las cejas
ch('zed-kyu', '#b0aa50', '#5a6a9a',
   [(6, 70), (6, 36), (22, 10), (50, 2), (78, 10), (94, 36), (94, 70), (86, 62), (74, 66), (62, 60), (50, 64), (38, 60), (26, 66), (14, 62)], top=-2, w=4,
   eyes='sharp', brows=False, shade='#8a6a3a')
CHARS['zed-kyu']['front'].append(strand([(50, 4), (50, 60)], OUTC, 'f', 0.9))
# Kay Zirro: pelo gris oscuro corto y rizado, con dos lunares en la frente, ojos violeta y una sonrisa de dientes
_kz = ch('kay-zirro', '#4a4844', '#8a5aa0',
         [(10, 64), (8, 40), (20, 18), (36, 10), (50, 14), (64, 8), (80, 16), (92, 40), (90, 64), (84, 54), (76, 58), (70, 50), (60, 52), (54, 46), (46, 54), (38, 48),
          (28, 54), (20, 50)], top=-4, w=4, eyes='sharp', brows=False, mouth='grin')
_kz['front'] += [L(ell(42, 62, 3, 2.4), OUTC, 'f', False), L(ell(58, 62, 3, 2.4), OUTC, 'f', False)]
# Cee Eff: pelo castaño arena peinado de lado, con el flequillo en diagonal hacia la derecha que le tapa media frente
ch('cee-eff', '#c8925a', '#1e1e1e',
   [(10, 62), (12, 36), (26, 14), (50, 6), (76, 12), (90, 34), (92, 62), (86, 54), (76, 46), (60, 40), (40, 42), (24, 50), (16, 60)], eyes='sharp', brows='angry')
CHARS['cee-eff']['front'] += [strand([(22, 30), (50, 20), (80, 30)], 'deep', 'f', 1.0), strand([(20, 42), (50, 30), (84, 42)], 'deep', 'f', 1.0)]
# Ar Ecks: rapado gris malva, con el nacimiento del pelo en ángulos rectos sobre la frente; ojos verdes de rombo
ch('ar-ecks', '#a09094', '#2a9a8a',
   [(14, 56), (14, 34), (26, 14), (50, 8), (74, 14), (86, 34), (86, 56), (80, 46), (68, 46), (66, 40), (34, 40), (32, 46), (20, 46)], top=4, w=-2, nape=80)
# Em Tee: pelo gris oliva repeinado hacia atrás con la raya en medio y dos mechones que bajan por las sienes; ojos redondos
ch('em-tee', '#7a7462', '#2a2a2a',
   [(12, 72), (12, 36), (24, 14), (46, 6), (50, 14), (54, 6), (76, 14), (88, 36), (88, 72), (82, 56), (74, 34), (60, 26), (50, 30), (40, 26), (26, 34), (18, 56)],
   eyes='round', brows='angry', top=0)
# Ough Cee: pelo malva corto con el flequillo en picos
ch('ough-cee', '#a08088', '#a8401e',
   [(10, 64), (10, 36), (24, 14), (50, 6), (76, 14), (90, 36), (90, 64), (84, 52), (76, 54, 1), (70, 44), (60, 48, 1), (54, 38), (46, 50, 1), (40, 40), (30, 50, 1),
    (24, 44), (18, 58, 1)], top=0)
# Jay Yuu (portero): pelo naranja claro peinado de lado con un mechón en pico que baja sobre la frente; ojos naranjas
ch('jay-yuu', '#e88a5a', '#c8601e',
   [(10, 64), (12, 34), (26, 12), (50, 4), (76, 12), (90, 34), (90, 64), (84, 52), (74, 38), (58, 36), (40, 56, 1), (36, 40), (22, 46), (16, 58)], top=0)
# Faiv Ess: pelo lavanda corto con el flequillo largo peinado de lado hacia la derecha; ojos amarillos
ch('faiv-ess', '#a094c0', '#c8a01e',
   [(10, 64), (12, 34), (26, 12), (50, 4), (76, 12), (90, 34), (90, 70), (84, 64), (80, 50), (66, 36), (48, 30), (30, 36), (20, 50), (16, 60)], top=0, shade='#7a5a6a')
# Tu Eigh: pelo verde claro con el flequillo en mechones afilados que caen en diagonal; ojos castaños con raya
ch('tu-eigh', '#b8c890', '#6a3a1e',
   [(10, 66), (12, 36), (26, 12), (50, 4), (76, 12), (90, 36), (90, 66), (84, 54), (80, 64, 1), (72, 44), (60, 40), (44, 60, 1), (40, 44), (28, 50), (20, 64, 1)], top=0,
   shade='#8a7a5a')
# Aye Nort: pelo gris plata en casco con el flequillo recto de mechones que le tapa las cejas; ojos amarillos de sueño
ch('aye-nort', '#c8c4b8', '#b89a1e',
   [(8, 70), (8, 36), (22, 10), (50, 2), (78, 10), (92, 36), (92, 70), (86, 60), (78, 66, 1), (72, 56), (62, 62, 1), (56, 54), (50, 62, 1), (44, 54), (38, 62, 1),
    (28, 56), (22, 66, 1), (14, 60)], top=-2, w=4, brows=False, shade='#9a8a80')
# Ji Tenn: pelo azul verdoso en casco con el flequillo recto mellado en picos
ch('ji-tenn', '#3a9ab0', '#1e1e1e',
   [(8, 70), (8, 36), (22, 10), (50, 2), (78, 10), (92, 36), (92, 70), (84, 58), (78, 64, 1), (74, 54), (62, 56), (58, 62, 1), (54, 54), (46, 54), (42, 62, 1), (38, 56),
    (26, 54), (22, 64, 1), (16, 58)], top=-2, w=4, shade='#2a5a6a')
