"""Correcciones de la revisión de diseños (grupo sc_ie3a): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS, L, OUTC, blob, ell, outline, strand  # noqa: F401
from heads import quad  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_03 import big_grin, stache, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie2_04 import lashes, lash_side  # noqa: F401
from chars_scouts_ie3_06 import bush, cap  # noqa: F401

K = 'scouts-ie3:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)


def _get(pid):
    return copy.deepcopy(CHARS[K + pid])


def _set(pid, c):
    CHARS[K + pid] = c


# --------------------------------------------------------------------------------------------------------------------
# Sue Chirpy Accharin: el sombrero de copa es de RAYAS VERTICALES anchas rojas y blancas (no a cuadros), con la copa
# abombada, la franja azul marino y el ala roja.
RDH, NV2 = _c('#b81818'), _c('#2e3a5e')


def _sue_hat(view):
    if view == 'side':
        crown = [(8, 40), (4, 10), (10, -14), (28, -26), (50, -28), (72, -26), (88, -14), (92, 10), (88, 40)]
        stripes = [[(24, 40), (20, 8), (24, -18), (32, -25), (40, -27), (38, 0), (38, 40)],
                   [(58, 40), (60, 0), (60, -27), (68, -26), (76, -20), (76, 8), (72, 40)]]
        band_ = [(6, 22), (90, 20), (90, 32), (6, 34)]
        brim = [(-4, 48), (50, 40), (100, 40), (98, 50), (50, 50), (-2, 58)]
    else:
        crown = [(10, 42), (6, 10), (12, -14), (28, -26), (50, -29), (72, -26), (88, -14), (94, 10), (90, 42)]
        stripes = [[(24, 42), (21, 8), (24, -18), (30, -24), (38, -27), (37, 0), (38, 42)],
                   [(62, 42), (63, 0), (62, -27), (70, -24), (76, -18), (79, 8), (76, 42)]]
        band_ = [(8, 22), (92, 22), (92, 34), (8, 34)]
        brim = [(2, 44), (50, 38), (98, 44), (96, 54), (50, 48), (4, 54)] if view == 'front' else \
            [(2, 44), (50, 40), (98, 44), (96, 54), (50, 50), (4, 54)]
    return ([L(outline(crown), RDH, 'f', True, True)] + [L(outline(s), WHITE, 'f', False) for s in stripes] +
            [L(outline(band_), NV2, 'f', True, True), L(outline(brim), RDH, 'f', True, True)])


def _sue():
    c = _get('sue-chirpy-accharin')
    kw = dict(top=30, w=48, cy=58, n=6, amp=6, seed=21)
    c['front'] = (bush('front', long=104, flare=12, **kw) + _sue_hat('front') +
                  [L(ell(x, y, 0.8, 0.8), _c('#b07848'), 'f', False) for x, y in ((26, 86), (30, 88), (33, 85), (74, 86), (70, 88), (67, 85))])
    c['side'] = bush('side', long=102, flare=10, fr=62, **kw) + _sue_hat('side')
    c['back'] = bush('back', long=102, flare=12, ends=5, **kw) + _sue_hat('back')
    _set('sue-chirpy-accharin', c)


_sue()


# Pasha Lomo: lleva un ANTIFAZ negro que le cruza los ojos (ojos blancos en él) y una sonrisa enorme de dientes que ocupa
# media cara (antes: dos rayas sobre unos ojos normales y una boquita de dientes).
def _pasha():
    c = _get('pasha-lomo')
    c['face']['eyes'] = 'none'
    fr = c['front'][:-4]  # fuera las dos rayas y los dientes pequeños
    mask = [(14, 70), (22, 64), (36, 64), (46, 68), (50, 72), (54, 68), (64, 64), (78, 64), (86, 70), (82, 80), (66, 82), (54, 78), (50, 80),
            (46, 78), (34, 82), (18, 80)]
    fr += [L(blob(mask, 6), BLACK, 'f', False),
           L(blob([(24, 74), (34, 70), (44, 73), (38, 77), (28, 77)], 4), WHITE, 'f', False),
           L(blob([(76, 74), (66, 70), (56, 73), (62, 77), (72, 77)], 4), WHITE, 'f', False)]
    fr += big_grin(y=94, w=17, h=10)
    c['front'] = fr
    sd = c['side']
    sd += [L(blob([(60, 66), (76, 64), (90, 68), (90, 80), (74, 82), (62, 78)], 5), BLACK, 'f', False),
           L(blob([(76, 72), (86, 70), (88, 76), (78, 77)], 4), WHITE, 'f', False)]
    _set('pasha-lomo', c)


_pasha()


# Maasa Sudou: ojos grandes de anime con pestañas (no puntitos) y el flequillo echado a un lado (de su izquierda a su
# derecha), no con raya en medio.
def _maasa():
    c = _get('maasa-maa-sudou')
    c['face']['eyes'] = 'big'
    c['pal']['iris'] = _c('#2a1e18')
    c['face']['hairline'] = [c['face']['hairline'][0], (16, 50), (30, 44), (44, 50), (60, 58), (74, 62), (86, 58), c['face']['hairline'][-1]]
    base = dome('front', top=0, w=46, cy=44, long=120, flare=8)
    c['front'] = base + [
        L(outline([(14, 50), (24, 26), (46, 14), (70, 18), (86, 34), (92, 60), (84, 70), (74, 60), (58, 56), (44, 48), (30, 50), (22, 64), (16, 80)]), 'mid', 'f'),
        strand([(40, 18), (60, 40), (78, 60)], 'shade', 'f', 1.0), strand([(30, 26), (22, 50)], 'shade', 'f', 1.0)] + lashes()
    c['side'] = c['side'] + lash_side()
    _set('maasa-maa-sudou', c)


_maasa()


# Marshall Artison: ojos furiosos medio cerrados (blancos con la pupila, párpado recto) y un bigote ancho sobre los dientes.
def _marshall():
    c = _get('marshall-artison')
    c['face']['eyes'] = 'sharp'
    c['front'] += [L([(28, 93), (36, 88), (44, 88.5), (50, 90), (56, 88.5), (64, 88), (72, 93)], _c('#8a5034'), 'f', False, False, 2.6)]
    c['side'] += [L([(70, 92), (78, 88), (88, 89)], _c('#8a5034'), 'f', False, False, 2.4)]
    _set('marshall-artison', c)


_marshall()


# T. T. Mann: la cresta rubia es un abanico de pinchos hacia arriba más ancho que la cabeza, con un pico en V que baja a la
# frente; los lados van rapados (más oscuros) con dos rayas afeitadas.
def _ttmann():
    c = _get('t-t-mann')
    c['face']['hairline'] = [c['face']['hairline'][0], (16, 54), (30, 46), (42, 50), (50, 58), (58, 50), (70, 46), (84, 54), c['face']['hairline'][-1]]
    c['pal']['mid'], c['pal']['shade'] = _c('#c8a058'), _c('#8a6430')
    c['front'] = [cap('front', 'shade', top=22, rim=56, w=39)] + dome('front', top=-26, w=46, cy=34, n=7, amp=20, seed=23, sb=50) + [
        L(outline([(28, 36), (40, 40), (50, 60, 1), (60, 40), (72, 36), (66, 26), (34, 26)]), 'mid', 'f', False),
        strand([(50, 54), (46, 20), (40, -6)], 'shade', 'f', 1.2), strand([(50, 54), (56, 20), (62, -8)], 'shade', 'f', 1.2),
        strand([(14, 52), (22, 34)], 'deep', 'b', 1.6), strand([(18, 56), (26, 38)], 'deep', 'b', 1.6),
        strand([(86, 52), (78, 34)], 'deep', 'b', 1.6), strand([(82, 56), (74, 38)], 'deep', 'b', 1.6)]
    c['side'] = [cap('side', 'shade', top=20, rim=60, w=46, drop=20)] + dome('side', top=-22, w=42, cy=32, n=6, amp=20, sweep=-0.5, seed=23, nape=56,
                                                                             fr=44, shade=False) + \
        [strand([(20, 52), (46, 30)], 'deep', 'b', 1.6), strand([(24, 58), (50, 36)], 'deep', 'b', 1.6)]
    c['back'] = [cap('back', 'shade', top=22, rim=62, w=42, drop=10)] + dome('back', top=-24, w=44, cy=34, n=7, amp=20, seed=23, nape=48, shade=False) + \
        [strand([(12, 54), (20, 36)], 'deep', 'b', 1.6), strand([(88, 54), (80, 36)], 'deep', 'b', 1.6)]
    _set('t-t-mann', c)


_ttmann()


# Devlin Ogor: las cejas tatuadas son arcos negros GRUESOS que suben desde el antifaz; los colmillos son grandes (salen de
# las comisuras y suben por las mejillas) y la boca es un morro ancho enfurruñado.
def _devlin():
    c = _get('devlin-grrrar-ogor')
    c['face']['mouth'] = 'none'
    fr = []
    for l in c['front']:
        if l['w'] == 2.2 and l['c'] == BLACK[:3] + (255,):
            l['w'] = 4.4
        fr.append(l)
    fr = [l for l in fr if not (l['c'] == _c('#efe4c8'))]
    fr += [L(quad((22, 46), (40, 30), (46, 54)), (30, 26, 30, 255), 'f', False, False, 6.0),
           L(quad((78, 46), (60, 30), (54, 54)), (30, 26, 30, 255), 'f', False, False, 6.0),
           L(outline([(30, 104), (16, 96), (12, 80, 1), (24, 90), (34, 98)]), _c('#efe4c8'), 'f'),
           L(outline([(70, 104), (84, 96), (88, 80, 1), (76, 90), (66, 98)]), _c('#efe4c8'), 'f'),
           L(quad((34, 104), (50, 92), (66, 104)), OUTC, 'f', False, False, 2.6),
           L(quad((40, 106), (50, 103), (60, 106)), _c('#c86a60'), 'f', False, False, 1.6)]
    c['front'] = fr
    c['side'] = [l for l in c['side'] if not (l['c'] == _c('#efe4c8'))] + [
        L(outline([(76, 104), (68, 90), (70, 78, 1), (76, 90), (82, 98)]), _c('#efe4c8'), 'f'),
        L([(78, 104), (88, 100)], OUTC, 'f', False, False, 2.4)]
    _set('devlin-grrrar-ogor', c)


_devlin()


def _slit_eyes(ey=75, sep=14, iris=BLACK, w=7.0, h=2.6):
    """Ojos entornados: medio ojo blanco con la pupila bajo un párpado de arriba recto y grueso."""
    out = []
    for cx in (50 - sep, 50 + sep):
        out += [L(ell(cx, ey + h * 0.2, w * 0.85, h), WHITE, 'f', False),
                L(ell(cx, ey + h * 0.3, 2.0, min(2.4, h * 0.85)), iris, 'f', False),
                L([(cx - w - 1, ey - h * 0.55), (cx + w + 1, ey - h * 0.55)], OUTC, 'f', False, False, 2.6)]
    return out


def _slit_side(ey=75, iris=BLACK):
    return [L(blob([(76, ey), (81, ey - 2.4), (86, ey), (81, ey + 2.4)], 4), WHITE, 'f', False), L(ell(82.5, ey, 1.6, 2), iris, 'f', False),
            L([(75, ey - 1.6), (87, ey - 1.6)], OUTC, 'f', False, False, 2.4)]


# Fez Monkton: ojos entornados de enfado (gajo blanco con la pupila), no cerrados.
def _fez():
    c = _get('fez-monkton')
    c['face']['eyes'] = 'none'
    c['front'] += _slit_eyes(ey=74, sep=15)
    c['side'] += _slit_side(ey=74)
    _set('fez-monkton', c)


_fez()


# Penny Linguine: ojos medio cerrados (gajo blanco con la pupila) y la boca abierta más grande.
def _penny():
    c = _get('penny-linguine')
    c['face']['eyes'] = 'none'
    c['front'] = [l for l in c['front'] if l['c'] != _c('#e07850')] + _slit_eyes(ey=75, sep=15, w=6.0, h=3.8) + [
        L(blob([(42, 91), (50, 90), (58, 91), (54, 99), (50, 103), (46, 99)], 4), _c('#e07850'), 'f', False, True)]
    c['side'] += _slit_side(ey=75)
    _set('penny-linguine', c)


_penny()


# Karl Kappa (modelo 3D): el pelo es una media melena de mechones pegada a la cabeza, no una bola enorme.
def _karl():
    c = _get('karl-kappa')
    n_old = len(dome('front', top=4, w=50, cy=48, n=9, amp=10, seed=61, sb=86))
    c['front'] = dome('front', top=6, w=47, cy=48, n=10, amp=7, seed=61, sb=86) + c['front'][n_old:]
    n_old = len(dome('side', top=4, w=48, cy=48, n=9, amp=10, seed=61, nape=92, fr=56))
    c['side'] = dome('side', top=6, w=46, cy=48, n=10, amp=7, seed=61, nape=92, fr=56) + c['side'][n_old:]
    n_old = len(dome('back', top=4, w=50, cy=48, n=9, amp=10, seed=61, nape=92))
    c['back'] = dome('back', top=6, w=47, cy=48, n=10, amp=7, seed=61, nape=92) + c['back'][n_old:]
    _set('karl-kappa', c)


_karl()


# Maxtor Lunde (modelo 3D): barba de tres días castaña por la mandíbula y la barbilla.
def _maxtor():
    c = _get('maxtor-lunde')
    c['front'].insert(len(c['front']) - 4, L(blob([(16, 86), (24, 100), (38, 108), (50, 110), (62, 108), (76, 100), (84, 86), (76, 92), (64, 99), (50, 100),
                                                    (36, 99), (24, 92)], 6), _c('#d8a07c'), 'f', False))
    c['front'] += thick_brows(y=63, c='mid', h=4.4, sep=15, w=14)
    c['side'] += side_brow(y=63, c='mid', h=4.4)
    c['side'].append(L(blob([(56, 90), (64, 102), (78, 108), (84, 104), (76, 100), (66, 94)], 5), _c('#d8a07c'), 'f', False))
    _set('maxtor-lunde', c)


_maxtor()


# Ezio (Chopper) Ryder: las gafas de sol redondas son enormes (casi se tocan y llegan a las mejillas), de cristal negro con
# brillos en diagonal y montura verde azulada.
def _ezio():
    c = _get('ezio-chopper-ryder')
    fr = [l for l in c['front'] if l['c'] not in (BLACK, WHITE, (24, 18, 20, 255), (248, 248, 248, 255), (30, 26, 30, 255))]
    frame = _c('#3a5a5e')
    for cx in (31, 69):
        fr += [L(ell(cx, 75, 18, 15.5), frame, 'f'), L(ell(cx, 75, 15.5, 13), BLACK, 'f', False),
               L([(cx - 8, 82), (cx - 1, 64)], WHITE, 'f', False, False, 2.6), L([(cx - 1, 84), (cx + 7, 68)], WHITE, 'f', False, False, 1.8)]
    c['front'] = fr
    c['side'] = [l for l in c['side'] if l['c'] not in (BLACK, (24, 18, 20, 255), (248, 248, 248, 255), (30, 26, 30, 255))] + [
        L(ell(84, 74, 7, 11), frame, 'f'), L(ell(84.5, 74, 5.2, 9), BLACK, 'f', False), L([(78, 70), (50, 66)], frame, 'f', False, False, 2.2)]
    _set('ezio-chopper-ryder', c)


_ezio()


# Kay "KMC" Emcee: en su retrato tiene la piel clara (no tostada) y el mechón rubio es grande y le cruza todo el flequillo.
def _kay():
    c = _get('kay-kmc-emcee')
    c['pal']['skin'], c['pal']['skin_d'] = _c('#f4cca4'), _c('#dcae88')
    c['front'] += [L(outline([(30, 18), (44, -2), (58, -16, 1), (64, 2), (84, -2, 1), (80, 14), (94, 26, 1), (78, 32), (70, 52, 1), (62, 40), (52, 58, 1),
                              (46, 40), (34, 48, 1), (36, 32)]), 'light', 'f')]
    _set('kay-kmc-emcee', c)


_kay()


# Gene Bulge: ojos negros GRANDES y redondos (no puntitos) y el flequillo esponjoso le cae hasta las cejas.
def _gene():
    c = _get('gene-bulge')
    c['face'].update(eyes='big', eye_y=77)
    c['face']['hairline'] = [c['face']['hairline'][0], (16, 62), (26, 68), (36, 60), (48, 66), (58, 60), (70, 66), (82, 62), c['face']['hairline'][-1]]
    c['front'] += [L(outline([(14, 50), (30, 40), (50, 36), (72, 40), (88, 52), (84, 64), (76, 58), (70, 68, 1), (62, 58), (52, 66, 1), (46, 58),
                              (36, 62, 1), (30, 56), (22, 64, 1)]), 'mid', 'f')]
    _set('gene-bulge', c)


_gene()


# Paddy Filler: ojos de loco (blanco grande con un aro negro grueso y la pupila pequeña) bajo unas cejas gruesas, y el tupé
# es un solo mechón grande barrido hacia arriba y a un lado (no una corona de pinchos).
def _paddy():
    c = _get('paddy-filler')
    c['face']['eyes'] = 'none'
    eyes = []
    for cx in (36, 64):
        eyes += [L(ell(cx, 76, 7.4, 6.4), BLACK, 'f', False), L(ell(cx, 76, 5.0, 4.2), WHITE, 'f', False), L(ell(cx, 76, 1.8, 1.8), BLACK, 'f', False)]
    eyes += thick_brows(y=64, c=_c('#3a3028'), h=3.6, sep=14, tilt=0.6, w=16)
    c['front'] = [c['front'][0], L(outline([(22, 42), (20, 24), (10, 4), (2, -14, 1), (24, -8), (44, -4), (60, 4), (74, 12), (82, 26), (78, 42), (60, 38),
                                            (40, 40)])),
                  strand([(30, 34), (20, 6)], 'shade', 'f', 1.0), strand([(50, 34), (36, 2)], 'shade', 'f', 1.0)] + c['front'][2:] + eyes
    c['side'] = [c['side'][0], L(outline([(28, 30), (24, 10), (40, -4), (62, -12), (84, -18, 1), (80, 0), (88, 16), (84, 30), (60, 36)]))]
    c['side'] += [L(ell(82, 76, 4.6, 6), BLACK, 'f', False), L(ell(82.5, 76, 3, 4.2), WHITE, 'f', False), L(ell(83, 76, 1.4, 1.6), BLACK, 'f', False)] + \
        side_brow(y=64, c=_c('#3a3028'), h=3.6)
    c['back'] = [c['back'][0], L(outline([(16, 40), (18, 20), (28, 6), (22, -10, 1), (40, -4), (62, -6), (78, 6), (84, 22), (84, 40), (50, 44)]))]
    _set('paddy-filler', c)


_paddy()


# Placido Cans Cannes: bajo el casco lleva una sombra gris oscura alrededor de los ojos (como un antifaz) y los ojos son
# blancos, grandes y de enfado.
def _placido():
    c = _get('placido-cans-cannes')
    c['front'] += [L(blob([(20, 68), (36, 64), (50, 68), (64, 64), (80, 68), (78, 82), (60, 84), (50, 80), (40, 84), (22, 82)], 6), _c('#5e5650'), 'f', False),
                   L(blob([(28, 74), (38, 71), (46, 75), (40, 80), (30, 79)], 4), WHITE, 'f', False),
                   L(blob([(72, 74), (62, 71), (54, 75), (60, 80), (70, 79)], 4), WHITE, 'f', False),
                   L(ell(39, 76.5, 1.6, 1.8), BLACK, 'f', False), L(ell(61, 76.5, 1.6, 1.8), BLACK, 'f', False),
                   L([(26, 70), (46, 74)], OUTC, 'f', False, False, 2.8), L([(74, 70), (54, 74)], OUTC, 'f', False, False, 2.8)]
    c['side'] += [L(blob([(66, 68), (90, 68), (90, 84), (68, 84)], 5), _c('#5e5650'), 'f', False), L(blob([(76, 74), (88, 73), (86, 80), (78, 79)], 4), WHITE, 'f', False),
                  L(ell(83, 76.5, 1.4, 1.8), BLACK, 'f', False), L([(72, 70), (88, 73)], OUTC, 'f', False, False, 2.8)]
    _set('placido-cans-cannes', c)


_placido()


# Phineas Hudd: las gafas de encima del casco son una visera blanca GRANDE (más ancha que la cabeza) con unas rayas
# rosadas en diagonal, no una tirita rosa.
def _phineas():
    c = _get('phineas-phones-hudd')
    pink = _c('#d8a8b0')
    c['front'] = [l for l in c['front'] if l['c'] != pink]
    c['front'] += [L(blob([(14, 14), (86, 14), (80, 42), (20, 42)], 3), WHITE, 'f'),
                   L([(24, 18), (32, 18), (40, 38), (32, 38)], pink, 'f', False), L([(46, 18), (54, 18), (54, 38), (46, 38)], pink, 'f', False),
                   L([(68, 18), (76, 18), (68, 38), (60, 38)], pink, 'f', False),
                   L(quad((16, 46), (50, 30), (84, 46)), _c('#e8c040'), 'f', False, False, 3.0),
                   L(ell(12, 44, 7, 7), _c('#e8901e'), 'f'), L(ell(88, 44, 7, 7), _c('#e8901e'), 'f')]
    _set('phineas-phones-hudd', c)


_phineas()


# Doug Boateng: el pañuelo rojo es ancho, le cubre toda la parte de arriba de la cabeza de lado a lado sobre la frente.
def _doug():
    c = _get('doug-boateng')
    RB = _c('#ba0202')
    i = next(k for k, l in enumerate(c['front']) if l['c'] == RB and not l['w'])
    c['front'][i] = L(blob([(8, 64), (8, 40), (26, 22), (50, 18), (74, 22), (92, 40), (92, 64), (50, 58)], 6), RB, 'f')
    _set('doug-boateng', c)


_doug()


# Strama Dakoto: ojos grandes y redondos castaños (con su sombra gris), no afilados.
def _strama():
    c = _get('strama-dakoto')
    c['face']['eyes'] = 'normal'
    c['front'] += lashes()
    _set('strama-dakoto', c)


_strama()


def _recolor(layers, old, new):
    for l in layers:
        if l['c'] == old:
            l['c'] = new
    return layers


# Campen Allerjee: la lámpara del casco es grande (redonda, con el aro crema y la rejilla), no un circulito con una cruz.
def _campen():
    c = _get('campen-allerjee')
    lamp = _c('#f6e6b0')
    c['front'] += [L(ell(50, 26, 15, 14), _c('#e8d8b8'), 'f'), L(ell(50, 26, 11, 10.5), lamp, 'f', False)] + \
        [L([(50 + dx, 16.5), (50 + dx, 35.5)], _c('#b8a070'), 'f', False, False, 1.0) for dx in (-5, 0, 5)] + \
        [L([(40, 26 + dy), (60, 26 + dy)], _c('#b8a070'), 'f', False, False, 1.0) for dy in (-5, 0, 5)]
    _set('campen-allerjee', c)


_campen()


# Laurie Driver: el pelo es verde claro amarillento (no verde oscuro) y las gafas de aviador naranjas son grandes.
def _laurie():
    c = _get('laurie-driver')
    c['pal'].update(mid=_c('#8eb45a'), shade=_c('#68903a'), deep=_c('#44662a'), light=_c('#bcd894'))
    GGF, GGL = _c('#e8d0a8'), _c('#f08a20')
    c['front'] = [l for l in c['front'] if l['c'] not in (GGF, GGL)]
    for cx in (33, 67):
        c['front'] += [L(ell(cx, 50, 13, 11.5), GGF, 'f', True, True), L(ell(cx, 50, 9.5, 8.5), GGL, 'f', False),
                       L(ell(cx - 3, 47, 3, 2), _c('#ffd8a0'), 'f', False)]
    _set('laurie-driver', c)


_laurie()


# Springer Boreham: las gafas de aviador tienen la montura NARANJA (como la visera) y los cristales marrón oscuro.
def _springer():
    c = _get('springer-boreham')
    for v in ('front', 'side', 'back'):
        _recolor(c[v], _c('#5a3a1e'), _c('#d0702e'))
        _recolor(c[v], _c('#3a3a32'), _c('#4a3020'))
    _set('springer-boreham', c)


_springer()


# Lyle Covet: las gafas de piloto azules son anchas (casi de lado a lado de la cara), no dos lentes pequeñas.
def _lyle():
    from chars_scouts_ie3_04 import goggles as gg4
    c = _get('lyle-covet')
    BLU = next(l['c'] for l in c['front'] if l['c'][2] > 150 and l['c'][0] < 140)
    MET = c['front'][0]['c']
    i = next(k for k, l in enumerate(c['front']) if l['c'] == BLU)
    c['front'][i - 3:i + 4] = gg4(68, BLU, frame=MET, sep=19, rx=15, ry=9)
    _set('lyle-covet', c)


_lyle()


# Ba Branssen: las gafas de aviador del casco son grandes: dos cristales redondos oscuros con la montura gris claro.
def _ba():
    c = _get('ba-branssen')
    fr = _c('#a8a8a4')
    for cx in (32, 68):
        c['front'] += [L(ell(cx, 40, 13, 11), fr, 'f'), L(ell(cx, 40, 9, 7.5), _c('#3a3640'), 'f', False), L(ell(cx - 3, 37, 2.6, 1.8), WHITE, 'f', False)]
    c['front'].append(L([(45, 40), (55, 40)], fr, 'f', False, False, 3.0))
    c['side'] += [L(ell(78, 40, 9, 11), fr, 'f'), L(ell(79, 40, 6, 7.5), _c('#3a3640'), 'f', False)]
    _set('ba-branssen', c)


_ba()


# Florence Tripps: las gafas redondas verdes son ENORMES (le cubren media cara) y de montura gruesa.
def _florence():
    from chars_scouts_ie1_03 import round_specs
    c = _get('florence-tripps')
    G = _c('#5aa030')
    c['front'] = [l for l in c['front'] if l['c'] != G] + round_specs('front', G, 77, 16, 13.5, 11.5, 3.4)
    c['side'] = [l for l in c['side'] if l['c'] != G] + round_specs('side', G, 77, 16, 13.5, 11.5, 3.4)
    _set('florence-tripps', c)


_florence()


# Orion Tearing: el antifaz negro es un triángulo grande que sube en punta hasta la frente y baja hasta las mejillas, con
# los ojos blancos grandes.
def _orion():
    c = _get('orion-bearings-tearing')
    c['front'] += [L(outline([(50, 34, 1), (64, 46), (78, 62), (80, 80), (50, 84), (20, 80), (22, 62), (36, 46)]), BLACK, 'f'),
                   L(blob([(26, 70), (34, 62), (44, 68), (42, 76), (30, 77)], 4), WHITE, 'f', False),
                   L(blob([(74, 70), (66, 62), (56, 68), (58, 76), (70, 77)], 4), WHITE, 'f', False)]
    _set('orion-bearings-tearing', c)


_orion()


# Rio Shoring: las mechas verde lima son bandas anchas que se enroscan por el moño y bajan por el pelo, no rayitas finas.
def _rio():
    c = _get('rio-g-peas-shoring')
    LIM2 = _c('#83ca2e')
    for l in c['front'] + c['side'] + c['back']:
        if l['c'] == LIM2 and l['w']:
            l['w'] = max(l['w'], 5.0)
    c['front'] += [L(quad((22, 58), (24, 30), (42, 12)), LIM2, 'f', False, False, 5.0), L(quad((78, 58), (76, 30), (58, 12)), LIM2, 'f', False, False, 5.0)]
    c['side'] += [L(quad((30, 56), (34, 30), (46, 12)), LIM2, 'f', False, False, 5.0)]
    _set('rio-g-peas-shoring', c)


_rio()


# ---------------------------------------------------------------------------------------------------- segunda tanda
def _big_eyes(c, ey=76, sep=14, r=7.0, pr=4.4, dy=0.0, side_ey=None):
    """Ojos grandes redondos (blanco grande con la pupila negra), como capas de delante."""
    c['face']['eyes'] = 'none'
    for cx in (50 - sep, 50 + sep):
        c['front'] += [L(ell(cx, ey, r, r * 1.05), WHITE, 'f'), L(ell(cx, ey + dy, pr, pr * 1.05), BLACK, 'f', False),
                       L(ell(cx - pr * 0.35, ey + dy - pr * 0.4, pr * 0.3, pr * 0.3), WHITE, 'f', False)]
    sy = ey if side_ey is None else side_ey
    c['side'] += [L(ell(81, sy, r * 0.65, r), WHITE, 'f'), L(ell(83, sy + dy, pr * 0.65, pr), BLACK, 'f', False)]


# Urbana Street: los dos moños de arriba son conos puntiagudos (como cuernecillos), no bolas.
def _urbana():
    c = _get('urbana-street')
    PK2 = _c('#e47898')
    cone_l = [(8, 22), (8, 4), (16, -14, 1), (30, 0), (34, 18)]
    cone_r = [(100 - x, y) + p[2:] for (x, y, *_), p in zip(cone_l, cone_l)]
    for v in ('front', 'back'):
        c[v] = [l for l in c[v] if l['c'] != PK2]
        c[v] = [L(outline(cone_l), PK2, 'b', True, True), L(outline(cone_r), PK2, 'b', True, True)] + c[v]
    c['side'] = [l for l in c['side'] if l['c'] != PK2]
    c['side'] = [L(outline([(24, 20), (24, 2), (32, -16, 1), (46, -2), (48, 16)]), PK2, 'b', True, True)] + c['side']
    _set('urbana-street', c)


_urbana()


# Wanda Mage Spelling: la cinta dorada del sombrero es ancha y la estrella amarilla es grande.
def _wanda():
    from chars_scouts_ie3_06 import WB, STR
    c = _get('wanda-mage-spelling')

    def star(cx, cy, r):
        import math
        pts = []
        for i in range(10):
            a = math.radians(90 + i * 36)
            rr = r if i % 2 == 0 else r * 0.45
            pts.append((cx + rr * math.cos(a), cy - rr * math.sin(a)))
        return pts
    c['front'] = [l for l in c['front'] if l['c'] != STR]
    c['front'] += [L(outline([(16, 26), (50, 24), (84, 26), (86, 46), (50, 44), (14, 46)]), WB, 'f', True, True),
                   L(star(70, 36, 14), STR, 'f', True, True)]
    c['side'] += [L(outline([(10, 26), (80, 24), (82, 44), (10, 46)]), WB, 'f', True, True), L(star(74, 34, 10), STR, 'f', True, True)]
    c['back'] += [L(outline([(16, 26), (50, 24), (84, 26), (86, 46), (50, 44), (14, 46)]), WB, 'f', True, True)]
    _set('wanda-mage-spelling', c)


_wanda()


# Raine Walker: la cinta de la capucha es ancha, amarilla con una fila de triángulos rojos (dientes de sierra).
def _raine():
    from chars_scouts_ie3_05 import ZZO, ZZY
    c = _get('raine-walker')
    RED_ = _c('#b8281e')
    c['front'] = [l for l in c['front'] if l['c'] != ZZO]
    band_ = L(outline([(12, 58), (12, 44), (30, 38), (50, 36), (70, 38), (88, 44), (88, 58), (50, 52)]), ZZY, 'f', True, True)
    tris = []
    for i in range(8):
        x0 = 13 + i * 9.25
        yb = 55 - 4 * (1 - abs((x0 + 4.6 - 50) / 40))
        tris.append(L([(x0, yb), (x0 + 4.6, yb - 11), (x0 + 9.25, yb)], RED_, 'f', False))
    c['front'] += [band_] + tris
    c['side'] += [L(outline([(64, 56), (66, 42), (86, 44), (86, 58)]), ZZY, 'f', True, True),
                  L([(68, 56), (72, 45), (76, 56)], RED_, 'f', False), L([(77, 57), (81, 46), (85, 57)], RED_, 'f', False)]
    _set('raine-walker', c)


_raine()


# Cuba Libra: las orejas son enormes (le sobresalen mucho a los lados de la cabeza).
def _cuba():
    c = _get('cuba-libra')
    c['face']['big_ears'] = 7
    c['face']['ear_out'] = 13
    _set('cuba-libra', c)


_cuba()


# Keenan Kigu Guru, Cole Tivator y Artie Xan: ojos grandes y redondos (blanco grande con la pupila negra), no puntitos.
def _keenan():
    c = _get('keenan-kigu-guru')
    _big_eyes(c, ey=77, sep=15, r=7.4, pr=4.0)
    _set('keenan-kigu-guru', c)


def _coletiv():
    c = _get('cole-tivator')
    _big_eyes(c, ey=77, sep=14, r=6.6, pr=3.8, dy=-1.6)
    _set('cole-tivator', c)


def _artie():
    c = _get('artie-xan')
    _big_eyes(c, ey=77, sep=14, r=6.8, pr=4.0)
    _set('artie-xan', c)


_keenan()
_coletiv()
_artie()


# Tom Dark (modelo 3D): el pelo va peinado hacia atrás con la frente muy despejada y entradas en las sienes.
def _tomdark():
    c = _get('tom-dark')
    hl_ = c['face']['hairline']
    c['face']['hairline'] = [hl_[0], (16, 36), (24, 26), (36, 28), (50, 24), (64, 28), (76, 26), (84, 36), hl_[-1]]
    _set('tom-dark', c)


_tomdark()


# Piel y tono de pelo medidos en el retrato (grupo de color de la zona de la cabeza): se corrigen los que se alejaban más
# de 30 (suma de |dR|+|dG|+|dB|). Los colores derivados (sombra, piel en sombra...) se recalculan si eran los automáticos.
def _recolor_pal(pid, skin=None, hair=None):
    from chars import hexc, tone, mix
    c = _get(pid)
    p = c['pal']
    if skin:
        old = p['skin']
        p['skin'] = hexc(skin)
        if p.get('skin_d') == tone(old, 0.86):
            p['skin_d'] = tone(p['skin'], 0.86)
        for l in c['front'] + c['side'] + c['back']:  # capas pintadas con el color de piel a mano
            if l['c'] == old:
                l['c'] = p['skin']
    if hair:
        old = p['mid']
        p['mid'] = hexc(hair)
        for k, f in (('shade', 0.78), ('deep', 0.6)):
            if p.get(k) == tone(old, f):
                p[k] = tone(p['mid'], f)
        if p.get('light') == mix(old, (255, 255, 255), 0.38):
            p['light'] = mix(p['mid'], (255, 255, 255), 0.38)
    _set(pid, c)


for _pid, _skin, _hair in (
        ('zahida-afif-zahid', '#dcaf77', None), ('kandhul-lai', '#ffc370', None), ('joe-java', '#a6846f', None),
        ('bombasta-flambo-flamboyanzi', '#804b36', None), ('joe-pigsy-bajie', '#eb9082', '#552a4c'),
        ('isodoura-bouquet', '#f9c79d', '#74c5c0'), ('kay-kmc-emcee', '#ecc091', '#322013'), ('karl-kappa', '#f8d08b', '#184a95'),
        ('ian-flappable', '#fbe8b8', None), ('falah-hazbin', '#cf9668', None), ('gudrun-lodestone', '#f0c19a', None),
        ('eveline-vicked-veitch', '#e2cdb3', '#76217e'), ('wulf-blackbean', '#d4ab89', None), ('wesley-pro-provolone', '#e09f50', None),
        ('severin-volley-volei', '#d0a162', None), ('gracey-grapples', '#c38b64', None), ('lucien-shiny-rarey', '#fcbc7c', None),
        ('gustav-weather-weathervane', '#fcecc4', None), ('leo-maine', '#b6753a', None), ('niall-kunai-kuhn', '#fcbc7a', None),
        ('lenton-gouger', '#f7c49a', None),
        ('sue-chirpy-accharin', None, '#d8b480'), ('heidi-li-l-red-rood', None, '#df9b13'), ('penny-linguine', None, '#8f6748'),
        ('haydn-bluey-woe', None, '#24585f'), ('norton-aquarius-waters', None, '#5f7b93'), ('holly-marx', None, '#5ea99e'),
        ('keenan-kigu-guru', None, '#ddddb0'), ('ian-infantry-fountry', None, '#dd4f06')):
    _recolor_pal(_pid, _skin, _hair)
