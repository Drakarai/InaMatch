"""Correcciones de la revisión de diseños (grupo ie1): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, blob, spk, strand, outline, pal, hexc, tone, mix, BACK_SKULL, sheen  # noqa: E402,F401


def _fix(key, base=None):
    """Copia del dibujo actual (base, o el que se usa ahora con esa clave) para corregirlo con la clave del equipo."""
    c = copy.deepcopy(CHARS[base or key.split(':', 1)[1]])
    CHARS[key] = c
    return c


# ================================================================== Raimon
# Bobby Shearer: pelo gris verdoso corto de punta arriba, con los lados y la nuca rapados más oscuros (no una bola)
_c = _fix('ie1-raimon:bobby-shearer')
_c['pal']['cut'] = hexc('#6c665c')
_c['face']['hairline'] = [(8, 60), (18, 58), (24, 50), (36, 48), (50, 46), (64, 48), (76, 50), (82, 58), (92, 60)]
_c['front'] = [
    L(blob([(14, 72), (13, 48), (30, 40), (70, 40), (87, 48), (86, 72), (80, 62), (20, 62)]), 'cut'),
    L(outline([(18, 52), (14, 40), (4, 32, 1), (18, 28), (16, 14, 1), (30, 20), (32, 6, 1), (44, 14), (50, 4, 1), (60, 14), (70, 8, 1),
               (72, 20), (88, 16, 1), (84, 30), (96, 34, 1), (86, 44), (82, 52), (66, 48), (50, 46), (34, 48)])),
    L(outline([(60, 16), (72, 4), (72, 20), (88, 14), (84, 30), (96, 33), (84, 46), (80, 50), (70, 46)]), 'shade', 'b', False),
    sheen(26, 50, 22, 3),
    spk((36, 42), (50, 42), (40, 56), 2, z='f'), spk((52, 42), (64, 44), (62, 55), 2, z='f', light_left=False),
]
_c['side'] = [
    L(blob([(44, 92), (22, 88), (14, 64), (16, 44), (40, 40), (60, 46), (54, 62), (50, 80)]), 'cut'),
    L(outline([(16, 50), (4, 40, 1), (16, 32), (8, 18, 1), (26, 20), (24, 6, 1), (40, 12), (46, 2, 1), (56, 12), (66, 6, 1), (70, 18),
               (84, 20, 1), (80, 30), (90, 40, 1), (76, 44), (60, 46), (36, 44)])),
    L(outline([(16, 48), (6, 40), (16, 32), (8, 18), (26, 22), (32, 42)]), 'shade', 'b', False),
]
_c['back'] = [
    L(BACK_SKULL, 'cut'),
    L(blob([(56, 40), (84, 44), (82, 70), (66, 86)], 6), tone(hexc('#6c665c'), 0.85), 'b', False),
    L(outline([(14, 54), (6, 34, 1), (18, 28), (18, 14, 1), (32, 20), (34, 6, 1), (46, 14), (52, 4, 1), (60, 14), (72, 8, 1), (72, 22),
               (88, 16, 1), (84, 30), (96, 34, 1), (86, 54), (50, 48)])),
    L(outline([(58, 16), (74, 4), (72, 22), (88, 14), (84, 30), (94, 35), (86, 52), (64, 48)]), 'shade', 'b', False),
]

# ================================================================== Teikoku
# Alan Master: la gema azul de la frente y los dos mechones largos como cuernos que salen de arriba
from chars import ell  # noqa: E402
_c = _fix('ie1-teikoku-gakuen:alan-master', 'alan-master')
_c['pal']['gem'] = hexc('#24406e')
_c['front'] = [spk((34, 22), (50, 18), (30, -34), 7), spk((56, 20), (72, 26), (80, -22), 7, light_left=False)] + _c['front'] + [
    L(ell(46, 57, 2.8, 3.2), 'gem', 'f', False)]
_c['side'] = [spk((40, 18), (56, 16), (36, -34), 7), spk((56, 18), (70, 22), (72, -24), 6, light_left=False)] + _c['side']
_c['back'] = [spk((50, 18), (66, 22), (70, -32), 7, light_left=False), spk((30, 26), (46, 18), (22, -22), 7)] + _c['back']

# ================================================================== Nose (Wild)
# Philip Anders: los dos moños redondos arriba a los lados
_c = _fix('ie1-nose:philip-anders', 'philip-anders')
_bun = lambda cx, cy, r: [L(ell(cx, cy, r, r * 0.95)), L(ell(cx + r * 0.3, cy + r * 0.2, r * 0.6, r * 0.55), 'shade', 'b', False)]
_c['front'] = _bun(9, 12, 13) + _bun(91, 12, 13) + _c['front']
_c['back'] = _bun(9, 12, 13) + _bun(91, 12, 13) + _c['back']
_c['side'] = _bun(34, 2, 13) + _c['side']
# Rocky Rackham: dos bultos redondos de pelo arriba (orejas de mapache)
_c = _fix('ie1-nose:rocky-rackham', 'rocky-rackham')
_c['front'] = _bun(18, 12, 10) + _bun(82, 12, 10) + _c['front'] + [
    L(blob([(26, 70), (50, 72), (74, 70), (74, 79), (50, 78), (26, 79)], 6), 'patch', 'f', False),
    L(ell(36, 75, 2.4, 2.8), (30, 20, 16, 255), 'f', False), L(ell(64, 75, 2.4, 2.8), (30, 20, 16, 255), 'f', False),
    L(ell(35.2, 74, 0.8, 0.8), (255, 255, 255, 255), 'f', False), L(ell(63.2, 74, 0.8, 0.8), (255, 255, 255, 255), 'f', False)]  # antifaz y ojillos
_c['back'] = _bun(18, 12, 10) + _bun(82, 12, 10) + _c['back']
_c['side'] = _bun(40, 4, 10) + _c['side']
# Gary Lancaster: orejas de oso redondas (de piel) arriba a los lados y el monóculo blanco
_c = _fix('ie1-nose:gary-lancaster', 'gary-lancaster')
_ear = lambda cx, cy: [L(ell(cx, cy, 11, 10), 'skin'), L(ell(cx, cy + 1, 6, 5.5), 'skin_d', 'b', False)]
_c['front'] = _ear(14, 34) + _ear(86, 34) + _c['front']
_c['back'] = _ear(14, 34) + _ear(86, 34) + _c['back']
_c['side'] = _ear(30, 26) + _c['side']

# ================================================================== Ichibangai Sally's
# Ness Sheldon: el pelo sube recto muy alto, en bloque con la parte de arriba plana (no un casquete)
_c = _fix('ie1-ichibangai-sally-s:ness-sheldon', 'ness-sheldon')
_top = blob([(18, 34), (19, -16), (50, -22), (81, -16), (82, 34), (50, 24)])
_c['front'][1] = L(_top)
_c['front'].insert(2, L(blob([(58, -18), (80, -14), (82, 30), (64, 22)], 6), 'shade', 'b', False))
_c['back'][1] = L(_top)
_c['side'][1] = L(blob([(18, 30), (22, -18), (72, -20), (80, 24), (50, 14)]))
