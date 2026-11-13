"""Correcciones de la revisión de diseños (grupo gxa): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401

# ======================================================================== Earth Eleven (gx-earth-eleven)
_T = 'gx-earth-eleven'

# Ibuki: la cinta negra de la frente se veía blanca (los pinchos del flequillo la tapaban casi entera); en el modelo es una
# banda negra ancha que rodea la cabeza por encima de las cejas, con el flequillo blanco asomando apenas por encima
_c = copy.deepcopy(CHARS['terry-archibald'])
for _v in ('front', 'side'):
    _band = [l for l in _c[_v] if l['c'] == 'band']
    _c[_v] = [l for l in _c[_v] if l['c'] != 'band'] + _band
from chars import L, outline, ell, strand, pal, messy, bumpy  # noqa: E402,F401
from heads import quad  # noqa: E402
_c['front'] = [l for l in _c['front'] if l['c'] != 'band'] + [
    L(outline([(11, 64), (12, 50), (50, 45), (88, 50), (89, 64), (50, 60)]), 'band', 'f', ln=True),
    # puntas del flequillo blanco que caen sobre el borde de la cinta
    L(outline([(30, 44), (36, 56, 1), (42, 46)]), 'mid', 'f'), L(outline([(46, 42), (52, 55, 1), (58, 43)]), 'mid', 'f'),
    L(outline([(60, 45), (66, 54, 1), (72, 47)]), 'mid', 'f')]
_c['side'] = [l for l in _c['side'] if l['c'] != 'band'] + [L(outline([(52, 62), (54, 50), (93, 52), (95, 64)]), 'band', 'f', ln=True)]
CHARS[f'{_T}:terry-archibald'] = _c

# Matatagi: su modelo 3D en el Earth Eleven es la forma Dark Side, con los mechones azul oscuro en las puntas del lado
# izquierdo (el dibujo base era la forma Pleasing, sin mechones); la mirada, la normal del modelo
_c = copy.deepcopy(CHARS['gx:falco-flashman-dark'])
_c['face'] = {**_c['face'], 'eyes': 'normal'}
CHARS[f'{_T}:falco-flashman'] = _c

# ======================================================================== Mach Tiger (gx-mach-tiger)
_T = 'gx-mach-tiger'

# Udom: de espaldas llevaba tres manchas ovaladas oscuras en el pelo (parecían agujeros); en el modelo la nuca es una masa
# de pinchos con las sombras en líneas: se cambian por mechones
_c = copy.deepcopy(CHARS['udom'])
_c['back'] = [l for l in _c['back'] if l['c'] != 'deep'] + [
    strand([(30, 20), (26, 46), (20, 70)], 'deep', 'b', 1.2), strand([(50, 14), (48, 46), (50, 84)], 'deep', 'b', 1.2),
    strand([(36, 56), (34, 80), (30, 94)], 'deep', 'b', 1.0), strand([(64, 30), (66, 58), (62, 88)], 'deep', 'b', 1.0)]
CHARS[f'{_T}:udom'] = _c

# ======================================================================== Fire Dragon (gx-fire-dragon-go)
_T = 'gx-fire-dragon-go'


def _braid(pts, w=8.0):
    """Trenza: una cadena de óvalos con línea, uno por punto (de arriba abajo)."""
    out = []
    for i, (x, y) in enumerate(pts):
        r = w * (1 - 0.25 * i / max(1, len(pts) - 1))
        out.append(L(ell(x, y, r, r * 1.05), 'mid', 'f', ln=True))
        out.append(L(ell(x + r * 0.35, y + r * 0.2, r * 0.45, r * 0.6), 'shade', 'f', False))
    return out


# Sung Ji-hoon: en el modelo lleva el pelo peinado hacia atrás con la frente despejada (no un flequillo de pinchos), la
# cinta en el nacimiento del pelo, mechones junto a las orejas y una trenza larga que le baja por la espalda hasta media
# espalda (el dibujo solo tenía un muñón)
_c = copy.deepcopy(CHARS['jihun-song'])
_c['face'] = {**_c['face'], 'hairline': (58, 34)}
_c['front'] = [_c['front'][0], _c['front'][1], _c['front'][2],
               strand([(30, 14), (22, 40)], 'shade', 'b', 1.0), strand([(70, 14), (78, 40)], 'shade', 'b', 1.0),
               L(quad((11, 50), (50, 18), (89, 50)) + quad((89, 57), (50, 26), (11, 57))[1:], 'band', 'f', ln=True),
               L(outline([(12, 56), (21, 58), (20, 80), (12, 98, 1), (9, 74)]), 'mid', 'f', ln=True),
               L(outline([(88, 56), (79, 58), (80, 80), (88, 98, 1), (91, 74)]), 'mid', 'f', ln=True)]
_c['side'] = [l for i, l in enumerate(_c['side']) if i != 2] + _braid([(12, 92), (8, 104), (4, 116), (0, 128), (-3, 140)], 7.0) + [
    L(ell(-4, 147, 3, 2.4), 'band', 'f', ln=True), L(outline([(-7, 149), (-1, 149), (-4, 160, 1)]), 'mid', 'f', ln=True)]
_c['back'] = [l for i, l in enumerate(_c['back']) if i < 3] + _braid([(50, 92), (48, 104), (46, 116), (44, 128), (42, 140)], 7.5) + [
    L(ell(41, 148, 3.2, 2.4), 'band', 'f', ln=True), L(outline([(38, 150), (44, 150), (41, 160, 1)]), 'mid', 'f', ln=True)]
CHARS[f'{_T}:jihun-song'] = _c

# ======================================================================== Storm Wolf (gx-storm-wolf)
_T = 'gx-storm-wolf'


# ======================================================================== Supernova (gx-supernova)
_T = 'gx-supernova'

# Indra Vayu: en el modelo la capucha de cobra tiene por dentro, a los dos lados de la cara, unas bandas marrón oscuro
# (el interior de la capucha); sin ellas la cabeza se leía como una bola dorada
_c = copy.deepcopy(CHARS['indra-vayu'])
_c['pal'] = {**_c['pal'], 'hood_in': (92, 58, 40, 255)}
_c['front'] = _c['front'][:2] + [
    L(outline([(-2, 44), (8, 26), (20, 40), (18, 70), (16, 98), (4, 100), (-4, 76)]), 'hood_in', 'b', False),
    L(outline([(102, 44), (92, 26), (80, 40), (82, 70), (84, 98), (96, 100), (104, 76)]), 'hood_in', 'b', False)] + _c['front'][2:]
CHARS[f'{_T}:indra-vayu'] = _c
