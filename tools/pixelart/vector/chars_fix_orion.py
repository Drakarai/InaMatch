"""Correcciones de la revisión de diseños (grupo orion): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401

from chars import L, OUTC, ell, outline  # noqa: E402

# ---------------------------------------------------------------- Guardianes de la Reina
# Zerbino Savelli: el flequillo de la izquierda le tapa entero el ojo izquierdo (con la lente de las gafas) hasta la mejilla
# y por debajo asoma un mechón rosa; de las gafas moradas solo se ve la lente derecha
_LILAC = (176, 130, 210, 255)
_PINK = (226, 128, 176, 255)
c = copy.deepcopy(CHARS['zerbino-savelli'])
c['face'].pop('glasses', None)
c['face'].pop('glasses_rect', None)
c['front'] = [l for l in c['front'] if not (l['z'] == 'f' and l['s'][0][0] < 30)]
c['front'] += [L([(54, 69), (74, 69), (73, 81), (55, 81), (54, 69)], _LILAC, 'f', False, False, 2.0),
               L([(74, 71), (82, 70)], _LILAC, 'f', False, False, 1.6),
               L(outline([(44, 40), (52, 46), (52, 66), (48, 84), (42, 92, 1), (44, 70), (46, 52)]), _PINK, 'f', False),
               L(outline([(10, 66), (12, 44), (24, 30), (40, 28), (50, 36), (48, 56), (44, 76), (38, 92), (28, 100, 1), (24, 88), (16, 80)]), 'mid', 'f', ln=True),
               L(outline([(30, 34), (44, 32), (46, 52), (40, 76), (34, 90), (36, 66), (34, 46)]), 'shade', 'f', False)]
c['side'] += [L(ell(80, 75, 6, 6.5) + [ell(80, 75, 6, 6.5)[0]], _LILAC, 'f', False, False, 1.6), L([(74, 74), (50, 69)], _LILAC, 'f', False, False, 1.4)]
CHARS['orion-guardians-of-queen:zerbino-savelli'] = c

# ---------------------------------------------------------------- Chispas Perfectas
# Boris Kaprichyov: el pelo negro es corto y rizado, de contorno abultado en rizos (no un casco liso con un pico arriba)
from chars import strand  # noqa: E402
c = copy.deepcopy(CHARS['boris-kaprichyov'])
_curls_f = [(12, 72), (8, 60), (3, 50), (9, 42), (6, 30), (16, 24), (18, 13), (31, 13), (37, 4), (50, 8), (61, 1), (69, 10), (82, 10), (85, 22), (95, 28),
            (91, 40), (97, 51), (89, 60), (88, 72), (82, 60), (66, 58), (50, 62), (34, 58), (18, 60)]
c['front'] = [L(outline(_curls_f)), L(outline([(61, 1), (69, 10), (82, 10), (85, 22), (95, 28), (91, 40), (97, 51), (89, 60), (84, 50), (76, 30), (64, 14)]), 'shade', 'b', False),
              strand([(24, 30), (30, 24), (36, 28)], 'deep', 'b', 1.0), strand([(44, 22), (52, 16), (58, 22)], 'deep', 'b', 1.0),
              strand([(66, 30), (72, 26), (78, 32)], 'deep', 'b', 1.0), strand([(30, 46), (38, 42), (42, 50)], 'deep', 'b', 1.0),
              strand([(56, 46), (62, 40), (68, 46)], 'deep', 'b', 1.0)] + [l for l in c['front'] if l['z'] == 'f']
c['face']['hairline'] = [(12, 70), (18, 58), (34, 58), (50, 62), (66, 58), (82, 58), (88, 70)]
c['side'] = [L(outline([(62, 56), (70, 46), (82, 46), (90, 36), (86, 24), (80, 12), (68, 8), (58, 0), (44, 4), (32, 0), (22, 10), (10, 12), (8, 26), (0, 36), (4, 48),
                        (0, 60), (8, 70), (20, 74), (32, 66), (44, 60), (54, 58)])),
             L(outline([(4, 36), (14, 22), (26, 32), (32, 64), (20, 74), (8, 70), (0, 60), (4, 48)]), 'shade', 'b', False),
             strand([(30, 16), (38, 12), (44, 18)], 'deep', 'b', 1.0), strand([(54, 18), (62, 14), (68, 22)], 'deep', 'b', 1.0),
             strand([(16, 40), (22, 34), (28, 40)], 'deep', 'b', 1.0)] + [l for l in c['side'] if l['z'] == 'f']
c['back'] = [L(outline([(14, 76), (8, 64), (4, 52), (10, 42), (6, 30), (16, 22), (20, 12), (32, 12), (38, 4), (50, 8), (62, 2), (70, 10), (82, 12), (86, 24), (96, 30),
                        (90, 42), (96, 54), (90, 64), (86, 76), (70, 80), (60, 74), (50, 80), (40, 74), (30, 80)])),
             L(outline([(62, 2), (70, 10), (82, 12), (86, 24), (96, 30), (90, 42), (96, 54), (90, 64), (86, 76), (72, 74), (66, 40), (60, 14)]), 'shade', 'b', False),
             strand([(26, 30), (32, 24), (38, 30)], 'deep', 'b', 1.0), strand([(46, 46), (52, 40), (58, 46)], 'deep', 'b', 1.0),
             strand([(30, 58), (36, 52), (42, 58)], 'deep', 'b', 1.0)] + [l for l in c['back'] if l['z'] == 'f']
CHARS['orion-perfect-spark:boris-kaprichyov'] = c

# Marfisa Corsi: las dos trenzas le caen por delante de los hombros hasta el pecho (no dos bultos a la altura de la barbilla)
def _braid(x0, y0, x1, y1, z='b', n=5, r=6.4):
    out = []
    for i in range(n):
        t = i / (n - 1)
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        rr = r * (1 - 0.25 * t)
        out.append(L(ell(x, y, rr, rr * 1.05), 'mid', z, True, True))
        out.append(L(ell(x + rr * 0.35, y + rr * 0.15, rr * 0.5, rr * 0.6), 'shade', z, False))
    out.append(L(outline([(x1 - 3, y1 + 4), (x1 + 3, y1 + 4), (x1 + 2, y1 + 14, 1), (x1 - 2, y1 + 14, 1)]), 'deep', z, True))
    return out


c = copy.deepcopy(CHARS['marfisa-corsi'])
c['front'] = _braid(13, 80, 10, 128) + _braid(87, 80, 90, 128) + c['front']
c['side'] = _braid(30, 80, 38, 128) + c['side']
c['back'] = _braid(14, 76, 12, 126, 'f') + _braid(86, 76, 88, 126, 'f') + c['back']
CHARS['orion-guardians-of-queen:marfisa-corsi'] = c
