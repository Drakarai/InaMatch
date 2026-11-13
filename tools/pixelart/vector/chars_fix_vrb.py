"""Correcciones de la revisión de diseños (grupo vrb): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, outline, strand  # noqa: E402,F401
from heads import quad  # noqa: E402,F401


def _fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


# ---------------------------------------------------------------- vr-batten-yokato

# Ebiss Marlowe: la melena naranja no lleva dos cuernos grandes: es una mata redonda con la raya en medio, un pincho en la
# coronilla con dos cuernecillos a los lados, y por los lados le salen mechones en punta hacia fuera a la altura de las
# mejillas; ojos redondos muy abiertos y sonrisa de dientes de tiburón
c = copy.deepcopy(CHARS['vr:ebiss-marlowe'])
c['face'].update({'eyes': 'round', 'mouth': 'grin', 'mouth_y': 95})
c['front'] = [
    L(outline([(18, 90), (8, 84, 1), (12, 76), (-6, 72, 1), (8, 64), (-6, 54, 1), (8, 48), (4, 32, 1), (14, 24), (16, 14), (30, 6), (26, -6, 1), (40, 2), (50, -18, 1),
               (60, 2), (74, -6, 1), (70, 6), (84, 14), (86, 24), (96, 32, 1), (92, 48), (106, 54, 1), (92, 64), (106, 72, 1), (88, 76), (92, 84, 1), (82, 90), (80, 62),
               (20, 62)])),
    L(outline([(60, 4), (74, -4), (70, 8), (86, 18), (94, 32), (90, 48), (104, 56), (90, 62), (102, 72), (86, 76), (80, 50), (70, 24)]), 'shade', 'b', False),
    L(outline([(46, 0), (50, -14), (54, 0)]), 'deep', 'b', False),
    _fr([(14, 70), (14, 44), (24, 24), (40, 14), (50, 16), (60, 14), (76, 24), (86, 44), (86, 70), (80, 56), (72, 48), (62, 46), (52, 60, 1), (50, 46), (48, 60, 1),
         (38, 46), (28, 48), (20, 56)]),
    L([(52, 60), (50, 46), (48, 60)], OUTC, 'f', False, False, 1.1),
    strand([(50, 16), (50, 44)], 'deep', 'f', 1.0),
    L(outline([(14, 56), (22, 58), (22, 88), (14, 96, 1), (12, 76)]), 'mid', 'f', ln=True),
    L(outline([(86, 56), (78, 58), (78, 88), (86, 96, 1), (88, 76)]), 'mid', 'f', ln=True)]
c['back'] = [
    L(outline([(18, 92), (6, 86, 1), (10, 76), (-6, 72, 1), (8, 64), (-6, 54, 1), (8, 48), (4, 32, 1), (14, 24), (16, 14), (30, 6), (26, -6, 1), (40, 2), (50, -18, 1),
               (60, 2), (74, -6, 1), (70, 6), (84, 14), (86, 24), (96, 32, 1), (92, 48), (106, 54, 1), (92, 64), (106, 72, 1), (90, 76), (94, 86, 1), (82, 92), (50, 96)])),
    L(outline([(56, 4), (74, -4), (70, 8), (86, 18), (94, 32), (90, 48), (104, 56), (90, 62), (102, 72), (88, 80), (66, 92), (64, 40)]), 'shade', 'b', False),
    L(outline([(46, 0), (50, -14), (54, 0)]), 'deep', 'b', False),
    strand([(50, 10), (48, 50), (50, 90)], 'deep', 'b', 1.0)]
CHARS['vr-batten-yokato:ebiss-marlowe'] = c


# ---------------------------------------------------------------- vr-nishinomiya

# Laymark Starwyn: el pelo rubio melocotón era casi del color de la piel y en el partido parecía calvo: rubio más dorado
# y con la sombra más tostada, como en el modelo
c = copy.deepcopy(CHARS['laymark-starwyn'])
c['pal'].update({'mid': (238, 204, 150, 255), 'shade': (212, 166, 118, 255), 'deep': (178, 130, 92, 255), 'light': (248, 228, 190, 255)})
CHARS['vr-nishinomiya:laymark-starwyn'] = c
