"""Correcciones de la revisión de diseños (grupo ie3b): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401


def _fix(team, pid, **kw):
    """Copia el dibujo que usa ahora el jugador en ese equipo y le cambia lo que se pase (body, pal, face...)."""

    base = _key(team, pid)
    c = copy.deepcopy(CHARS[base])
    for k, v in kw.items():
        if k in ('pal', 'face') and isinstance(v, dict):
            c.setdefault(k, {}).update(v)
        else:
            c[k] = v
    CHARS[f'{team}:{pid}'] = c
    return c


def _key(team, pid):
    for k in (f'{team}:{pid}', f"{team.split('-')[0]}:{pid}"):
        if k in CHARS:
            return k
    for base in sorted(CHARS, key=len, reverse=True):
        if pid == base or pid.startswith(base + '-'):
            return base
    raise KeyError(pid)


# Brockenborg: Heinrich Farber es alto y de complexión normal, no corpulento
_fix('ie3-brockenborg', 'heinrich-farber', body='normal')
# Fire Dragon: Bryce juega con la camiseta sin mangas
_fix('ie3-fire-dragon', 'bryce-whitingale', sleeveless=True)
# Makai Gundan Z: Arachne y Jezebeth son chicas (cuerpo de chica, como en su modelo)
_fix('ie3-makai-gundan-z', 'arachne', body='chica')
_fix('ie3-makai-gundan-z', 'jezebeth', body='chica')
# Tenkuu no Shito: Gaiel es una chica
_fix('ie3-tenkuu-no-shito', 'gaiel', body='chica')


# ------------------------------------------------------------------ peinados rehechos para que coincidan con su modelo
from chars import L, outline, strand  # noqa: E402
from heads import spk  # noqa: E402

# Destra: melena castaño rojiza de pinchos grandes que suben en la coronilla y se abren hacia los lados y hacia abajo hasta
# los hombros, con la cara entera a la vista bajo un flequillo de puntas hasta las cejas
_c = _fix('ie3-makai-gundan-z', 'destra')
_c['face'] = dict(_c['face'], hairline=False)
_c['front'] = [
    L(outline([(-12, 134, 1), (6, 114), (-22, 102, 1), (4, 88), (-26, 68, 1), (4, 58), (-16, 34, 1), (12, 30), (0, 4, 1), (22, 10), (22, -22, 1), (38, 0),
               (50, -32, 1), (60, -2), (76, -22, 1), (78, 8), (100, 4, 1), (88, 30), (116, 34, 1), (96, 58), (126, 68, 1), (96, 88), (122, 102, 1), (94, 114),
               (112, 134, 1), (86, 122), (50, 116), (14, 122)])),
    L(outline([(60, -2), (76, -18, 1), (78, 8), (98, 6, 1), (88, 30), (114, 36, 1), (96, 58), (124, 70, 1), (96, 88), (120, 104, 1), (92, 116), (108, 132, 1),
               (86, 118), (84, 70), (76, 30)]), 'shade', 'b', False),
    L(outline([(10, 72, 1), (14, 44), (30, 26), (50, 20), (70, 26), (86, 44), (90, 72, 1), (80, 56), (72, 64, 1), (64, 48), (56, 62, 1), (50, 48), (44, 62, 1),
               (36, 48), (28, 64, 1), (20, 56)]), 'mid', 'f'),
    L(outline([(56, 24), (72, 28), (84, 42), (88, 66, 1), (78, 50), (66, 40)]), 'shade', 'f', False),
]
_c['side'] = [
    L(outline([(86, 40), (96, 30, 1), (80, 22), (86, 0, 1), (66, 4), (62, -28, 1), (48, -2), (30, -22, 1), (24, 4), (-2, -8, 1), (10, 20), (-20, 22, 1), (2, 40),
               (-24, 58, 1), (0, 68), (-20, 92, 1), (2, 98), (-12, 126, 1), (12, 114), (12, 138, 1), (28, 116), (38, 128, 1), (44, 102), (50, 88), (52, 70),
               (58, 54), (72, 46)])),
    L(outline([(30, 30), (-2, 42), (-18, 60, 1), (0, 70), (-16, 92, 1), (4, 100), (-8, 122, 1), (14, 112), (14, 134, 1), (28, 112), (36, 124, 1), (42, 100),
               (46, 70), (40, 44)]), 'shade', 'b', False),
    spk((60, 34), (88, 40), (92, 62), 4, z='f', light_left=False),
]
_c['back'] = [
    L(outline([(-12, 132, 1), (6, 114), (-22, 102, 1), (4, 88), (-26, 68, 1), (4, 58), (-16, 34, 1), (12, 30), (0, 4, 1), (22, 10), (22, -22, 1), (38, 0),
               (50, -32, 1), (60, -2), (76, -22, 1), (78, 8), (100, 4, 1), (88, 30), (116, 34, 1), (96, 58), (126, 68, 1), (96, 88), (122, 102, 1), (94, 114),
               (112, 132, 1), (88, 124), (78, 140, 1), (66, 126), (50, 142, 1), (34, 126), (22, 140, 1), (12, 124)])),
    L(outline([(56, 0), (76, -18, 1), (78, 8), (98, 6, 1), (88, 30), (114, 36, 1), (96, 58), (124, 70, 1), (96, 88), (120, 104, 1), (92, 116), (108, 130, 1),
               (86, 122), (76, 136, 1), (64, 124), (66, 60)]), 'shade', 'b', False),
]

# la melena de Destra, algo más recogida: de los hombros no pasa (escalada hacia el centro de la cabeza, sin tocar el flequillo)
for _v in ('front', 'side', 'back'):
    for _i, _l in enumerate(_c[_v]):
        if isinstance(_l, dict) and _l['z'] == 'b':
            _c[_v][_i] = dict(_l, s=[(50 + (x - 50) * 0.8, 40 + (y - 40) * 0.8) for x, y in _l['s']])

# Leone Badigo: melena rubia ondulada de largo medio (hasta la mandíbula), pegada a la cabeza por arriba y con puntas
# cortas que se abren a los lados; la frente despejada con unos mechones que caen
_c = _fix('ie3-the-empire', 'leone-badigo')
_c['front'] = [
    L(outline([(6, 96, 1), (8, 80), (-6, 72, 1), (6, 62), (-6, 46, 1), (8, 40), (4, 20, 1), (18, 16), (26, 2, 1), (40, 6), (50, -2), (62, 4), (76, 0, 1),
               (80, 14), (96, 16, 1), (92, 32), (106, 44, 1), (94, 52), (106, 66, 1), (92, 72), (96, 88, 1), (88, 82), (84, 98, 1), (82, 62), (18, 62),
               (16, 98, 1), (12, 82)])),
    L(outline([(60, 4), (76, 2, 1), (80, 14), (94, 18, 1), (92, 32), (104, 44, 1), (94, 52), (104, 66, 1), (92, 72), (94, 86, 1), (86, 80), (84, 94, 1), (82, 52),
               (74, 24)]), 'shade', 'b', False),
    L(outline([(12, 66, 1), (14, 40), (30, 22), (50, 16), (70, 22), (86, 40), (88, 66, 1), (80, 48), (68, 40), (60, 52, 1), (56, 36), (44, 34), (38, 50, 1),
               (32, 38), (20, 46)]), 'mid', 'f'),
    L(outline([(28, 26), (50, 18), (44, 28)]), 'light', 'f', False),
    L(outline([(58, 22), (76, 28), (86, 42), (86, 60, 1), (78, 46), (66, 36)]), 'shade', 'f', False),
]
_c['side'] = [
    L(outline([(56, 58), (62, 46), (78, 42), (90, 32), (86, 16), (70, 4), (54, -2), (48, -14, 1), (40, 0), (20, 4), (-10, 8, 1), (10, 22), (-16, 34, 1), (6, 42),
               (-14, 56, 1), (8, 62), (-8, 78, 1), (12, 80), (2, 96, 1), (22, 90), (26, 106, 1), (36, 92), (44, 96), (50, 84), (52, 70)])),
    L(outline([(30, 30), (6, 44), (-12, 58, 1), (8, 64), (-6, 80, 1), (14, 82), (4, 94, 1), (24, 90), (28, 102, 1), (36, 90), (44, 72), (42, 44)]), 'shade', 'b', False),
    spk((62, 32), (88, 38), (92, 58), 4, z='f', light_left=False),
]
_c['back'] = [
    L(outline([(8, 100, 1), (4, 82), (-8, 74, 1), (4, 62), (-8, 48, 1), (6, 40), (4, 20, 1), (18, 14), (28, 0, 1), (40, 4), (50, -4), (62, 4), (76, 0, 1), (82, 14),
               (96, 20, 1), (94, 40), (108, 48, 1), (96, 62), (108, 74, 1), (96, 82), (92, 100, 1), (80, 92), (70, 106, 1), (60, 94), (50, 108, 1), (40, 94),
               (30, 106, 1), (20, 92)])),
    L(outline([(56, 2), (76, 2, 1), (82, 14), (94, 22, 1), (94, 40), (106, 50, 1), (96, 62), (106, 74, 1), (96, 82), (90, 98, 1), (80, 90), (70, 102, 1), (62, 92),
               (60, 40)]), 'shade', 'b', False),
    L(outline([(30, 50), (40, 64, 1), (36, 50)]), 'shade', 'b', False), L(outline([(62, 54), (70, 70, 1), (68, 52)]), 'shade', 'b', False),
]

# Phillip Owen: pelo gris verdoso de pinchos largos que suben (más alto que ancho), corto y pegado en los lados con las
# orejas a la vista, y puntas cortas de flequillo sobre la frente
_c = _fix('ie3-knights-of-queen', 'phillip-owen')
_c['front'] = [
    L(outline([(16, 62), (12, 50), (2, 40, 1), (12, 32), (4, 14, 1), (18, 12), (16, -10, 1), (30, 2), (36, -24, 1), (44, -2), (54, -28, 1), (58, -4), (70, -18, 1),
               (72, 4), (88, -2, 1), (84, 16), (98, 22, 1), (88, 34), (96, 44, 1), (88, 50), (84, 62)])),
    L(outline([(58, -4), (70, -16, 1), (72, 4), (86, 0, 1), (84, 16), (96, 24, 1), (88, 34), (94, 44, 1), (86, 52), (78, 30), (62, 16)]), 'shade', 'b', False),
    L(outline([(30, -2), (36, -20, 1), (40, 0)]), 'light', 'b', False),
    L(outline([(14, 62, 1), (16, 42), (28, 28), (50, 22), (72, 28), (84, 42), (86, 62, 1), (78, 50), (70, 58, 1), (64, 44), (56, 58, 1), (50, 44), (42, 58, 1),
               (36, 44), (28, 58, 1), (22, 48)]), 'mid', 'f'),
    L(outline([(58, 26), (74, 30), (84, 44), (86, 60, 1), (78, 48), (68, 38)]), 'shade', 'f', False),
]
_c['side'] = [
    L(outline([(86, 40), (94, 28, 1), (80, 24), (84, 2, 1), (68, 8), (68, -18, 1), (54, 2), (44, -26, 1), (38, 0), (20, -14, 1), (24, 10), (-2, 4, 1), (12, 24),
               (-10, 34, 1), (10, 42), (-8, 56, 1), (12, 60), (2, 76, 1), (20, 74), (24, 90), (40, 92), (48, 84), (52, 70), (58, 52), (72, 46)])),
    L(outline([(28, 24), (-6, 36, 1), (10, 44), (-6, 56, 1), (12, 62), (2, 74, 1), (20, 74), (24, 88), (40, 90), (46, 70), (42, 40)]), 'shade', 'b', False),
    spk((60, 34), (88, 40), (92, 60), 4, z='f', light_left=False),
]
_c['back'] = [
    L(outline([(16, 84), (14, 70), (6, 60, 1), (12, 50), (2, 38, 1), (14, 30), (8, 12, 1), (22, 12), (22, -10, 1), (34, 4), (42, -22, 1), (50, 0), (60, -24, 1),
               (64, 2), (78, -8, 1), (78, 12), (94, 14, 1), (86, 30), (98, 40, 1), (88, 50), (94, 60, 1), (86, 70), (84, 84), (66, 88), (50, 90), (34, 88)])),
    L(outline([(56, 4), (60, -20, 1), (64, 2), (78, -6, 1), (78, 12), (92, 16, 1), (86, 30), (96, 40, 1), (88, 50), (92, 60, 1), (86, 70), (82, 84), (64, 88),
               (62, 40)]), 'shade', 'b', False),
]

# Carlos Lagarto: las trenzas pegadas abultan más (suben por encima de la cabeza) y le tapan la frente hasta las cejas por
# un lado; antes la cara le tapaba la frente y parecía calvo por delante
_c = _fix('ie3-the-kingdom', 'carlos-lagarto')
_lips = [l for l in _c['front'] if l.get('c') == 'lip']
_lock = _c['front'][-len(_lips) - 4:-len(_lips)]  # el mechón que cae sobre el ojo y sus surcos
_c['front'] = [
    L(outline([(12, 66), (10, 36), (20, 10), (38, -4), (56, -6), (74, 2), (88, 24), (90, 50), (86, 64), (80, 52), (64, 46), (50, 46), (34, 48), (20, 56)]), 'mid', 'f', ln=True),
    L(outline([(60, -2), (78, 8), (88, 28), (88, 50), (76, 30)]), 'shade', 'f', False),
] + [strand([(x, 50 - abs(x - 50) * 0.1), (x + 1, 24), (x + 4, 0 + abs(x - 50) * 0.2)], 'shade', 'f', 1.4) for x in (20, 32, 44, 56)] + _lock + _lips
_c['side'] = [
    L(outline([(44, 88), (22, 84), (10, 62), (8, 30), (22, 6), (48, -6), (74, -2), (90, 14), (92, 34), (78, 38), (62, 44), (52, 60), (48, 78)]), 'mid', 'f', ln=True),
    L(outline([(10, 40), (34, 40), (42, 78), (22, 84), (10, 62)]), 'shade', 'f', False),
] + [strand([(88 - k * 3, 8 + k * 7), (52, 2 + k * 12), (16, 22 + k * 13)], 'shade', 'f', 1.4) for k in range(5)] + [l for l in _c['side'] if l.get('c') == 'lip']
_c['back'] = [
    L(outline([(14, 80), (10, 30), (22, 6), (50, -6), (78, 6), (90, 30), (86, 80), (50, 88)]), 'mid', 'f', ln=True),
    L(outline([(56, -2), (80, 10), (90, 32), (86, 78), (62, 84)]), 'shade', 'f', False),
] + [strand([(50, -2), (50 + (x - 50) * 0.5, 40), (x, 84)], 'shade', 'f', 1.4) for x in (18, 34, 50, 66, 82)]
