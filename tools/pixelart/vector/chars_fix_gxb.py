"""Correcciones de la revisión de diseños (grupo gxb): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import hexc, outline, pal  # noqa: E402,F401
from heads import L  # noqa: E402


def _recolor(c, **cols):
    """Cambia colores de la paleta (hex) de una ficha ya copiada."""
    for k, v in cols.items():
        c['pal'][k] = hexc(v)
    return c


def _swap_shape(layers, old_first, new_pts):
    """Sustituye la forma de la capa (de una lista de capas) cuyo contorno se hizo con outline() a partir de old_first."""
    ref = outline(old_first)
    for i, l in enumerate(layers):
        if isinstance(l, dict) and l['s'] == ref:
            layers[i] = dict(l, s=outline(new_pts))
            return True
    raise KeyError('capa no encontrada')


# --- Big Waves (GO Galaxy) ---------------------------------------------------------------------------------------------
# Jude Gordon: la melena es azul grisácea apagada (el modelo 3D: gris azulado, casi gris de perfil), no azul vivo
c = copy.deepcopy(CHARS['jude-gordon'])
CHARS['gx-big-waves-go:jude-gordon'] = _recolor(c, mid='#6a8cac', shade='#56677e', deep='#424e60', light='#9ab4ca')

# --- Faram Dite ----------------------------------------------------------------------------------------------------------
# Selenia: las dos coletas, atadas arriba a los lados, le caen largas hasta el pecho (antes acababan a la altura de la cara)
_sel_old = [(18, 16), (4, 18), (-8, 34), (-14, 60), (-8, 82), (-14, 114, 1), (2, 104), (8, 118, 1), (18, 92), (22, 62), (26, 34)]
_sel_new = [(18, 16), (4, 18), (-8, 36), (-12, 66), (-8, 100), (-14, 142, 1), (0, 128), (8, 144, 1), (16, 112), (22, 72), (26, 34)]
_sel_mir = lambda pts: [(100 - t[0],) + tuple(t[1:]) for t in pts]
c = copy.deepcopy(CHARS['selenia'])
for _v in ('front', 'back'):
    _swap_shape(c[_v], _sel_old, _sel_new)
    _swap_shape(c[_v], _sel_mir(_sel_old), _sel_mir(_sel_new))
_swap_shape(c['side'], [(16, 20), (-6, 30), (-14, 60), (-10, 112, 1), (4, 100), (8, 114, 1), (14, 80), (10, 56), (22, 36)],
            [(16, 20), (-6, 32), (-12, 66), (-10, 140, 1), (4, 126), (10, 142, 1), (14, 96), (10, 56), (22, 36)])
CHARS['gx-faram-dite:selenia'] = c

# --- Big Bang (y Space Rankers, que copia el dibujo de Big Bang en chars_combined) -------------------------------------
# Zartan Walder: la melena lacia le cae recta hasta los hombros por los dos lados (antes se abría en pinchos hacia fuera
# a la altura del cuello)
c = copy.deepcopy(CHARS['zartan-walder'])
_swap_shape(c['front'], [(18, 112), (-2, 118, 1), (2, 106), (-18, 110, 1), (-8, 96), (-20, 88, 1), (-4, 78), (0, 52), (4, 28), (18, 6), (50, -4), (82, 6), (96, 28),
                         (100, 52), (104, 78), (120, 88, 1), (108, 96), (118, 110, 1), (98, 106), (102, 118, 1), (82, 112), (82, 70), (18, 70)],
            [(18, 114), (6, 124, 1), (6, 110), (-6, 120, 1), (-4, 98), (-8, 78), (-4, 52), (2, 28), (18, 6), (50, -4), (82, 6), (98, 28),
             (104, 52), (108, 78), (104, 98), (106, 120, 1), (94, 110), (94, 124, 1), (82, 114), (82, 70), (18, 70)])
CHARS['gx-big-bang:zartan-walder'] = c

# Circulus: rubio muy claro arriba y melocotón en las capas de abajo (no naranja dorado)
c = copy.deepcopy(CHARS['circulus'])
CHARS['gx-big-bang:circulus'] = _recolor(c, mid='#f6dc94', shade='#e0a676', light='#fcf0c8', deep='#c08a5e')
