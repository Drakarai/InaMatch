"""Correcciones de la revisión de diseños (grupo gob): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, outline, strand  # noqa: E402,F401

FIXES = {}  # '<equipo>:<id>' -> dibujo corregido


def fix(teams, pid, base=None):
    """Copia el dibujo actual de pid (o de base) para corregirlo y lo registra con la clave de cada equipo."""
    c = copy.deepcopy(CHARS[base or pid])
    for t in teams.split():
        CHARS[f'{t}:{pid}'] = c
    return c


# ------------------------------------------------------------------ Arakumo Gakuen

# Deimos Mars: además de las puntas, mechones largos que le bajan por los lados de la cara hasta la barbilla y una melena
# de puntas que le cae por la nuca hasta los hombros
c = fix('go-arakumo-gakuen', 'deimos-mars')
c['front'][0:0] = [L(outline([(20, 60), (6, 74), (2, 100), (8, 118, 1), (14, 104), (18, 122, 1), (24, 100), (24, 72)])),
                   L(outline([(80, 60), (94, 74), (98, 100), (92, 118, 1), (86, 104), (82, 122, 1), (76, 100), (76, 72)])),
                   L(outline([(6, 80), (4, 104), (8, 118, 1), (14, 100)]), 'shade', 'b', False),
                   L(outline([(94, 80), (96, 104), (92, 118, 1), (86, 100)]), 'shade', 'b', False)]
c['side'][0:0] = [L(outline([(40, 70), (30, 90), (14, 112), (2, 132, 1), (22, 120), (24, 136, 1), (36, 112), (46, 96), (48, 76)])),
                  L(outline([(30, 92), (16, 114), (4, 130, 1), (24, 116)]), 'shade', 'b', False)]
c['back'][0:0] = [L(outline([(14, 70), (8, 104), (14, 128, 1), (26, 110), (34, 134, 1), (42, 112), (50, 138, 1), (58, 112), (66, 134, 1), (74, 110),
                             (86, 128, 1), (92, 104), (86, 70)])),
                  L(outline([(54, 80), (86, 76), (92, 104), (86, 128, 1), (74, 110), (66, 134, 1), (58, 112)]), 'shade', 'b', False)]


# ------------------------------------------------------------------ Dragonlink

# Fivier Saviola: gafas de pasta negra gruesas y rectangulares (antes, un alambre fino)
c = fix('go-dragonlink', 'fivier-saviola')
_gy = c['face'].get('eye_y', 75)
for _cx in (36, 64):
    c['front'].append(L([(_cx - 11, _gy - 7), (_cx + 11, _gy - 7), (_cx + 10, _gy + 7), (_cx - 10, _gy + 7), (_cx - 11, _gy - 7)], (24, 20, 22, 255), 'f', False, False, 3.2))
c['front'].append(L([(47, _gy - 4), (53, _gy - 4)], (24, 20, 22, 255), 'f', False, False, 2.6))

# Quinque Flores: el pelo no es blanco grisáceo sino rosa muy pálido con la sombra malva
c = fix('go-dragonlink', 'quinque-flores')
c['pal'].update({'mid': (236, 220, 230, 255), 'shade': (190, 160, 178, 255), 'deep': (150, 116, 136, 255), 'light': (250, 242, 246, 255)})


# ------------------------------------------------------------------ Inazuma KFC (GO)

# Reed Maind: el azul claro solo es la parte de arriba; las puntas de la melena larga (por detrás y por los lados) son azul
# marino muy oscuro
c = fix('go-inazuma-kfc-go', 'reed-maind')
c['pal']['tip'] = (40, 46, 78, 255)
c['back'].insert(2, L(outline([(2, 72), (98, 72), (97, 120), (3, 120)], 2), 'tip', 'b', False))
c['side'].insert(2, L(outline([(0, 70), (40, 76), (46, 118), (-20, 118)], 2), 'tip', 'b', False))
c['front'].insert(2, L(outline([(2, 96), (16, 96), (16, 120), (4, 120)], 2), 'tip', 'b', False))
c['front'].insert(3, L(outline([(84, 96), (98, 96), (96, 120), (84, 120)], 2), 'tip', 'b', False))


# ------------------------------------------------------------------ Kidokawa Seishuu (GO)

# Calder Elm: el pelo es gris marengo con brillos grises, no negro
c = fix('go-kidokawa-seishuu-go', 'calder-elm')
c['pal'].update({'mid': (72, 72, 78, 255), 'shade': (50, 50, 56, 255), 'deep': (34, 34, 38, 255), 'light': (120, 120, 126, 255)})

# Bay Laurel: azul marino apagado (índigo grisáceo), no azul vivo
c = fix('go-kidokawa-seishuu-go', 'bay-laurel')
c['pal'].update({'mid': (64, 62, 108, 255), 'shade': (46, 44, 82, 255), 'deep': (32, 30, 60, 255), 'light': (110, 108, 150, 255)})

# Strom Boojum (portero): un grandullón de brazos enormes, no de complexión normal
c = fix('go-kidokawa-seishuu-go', 'strom-boojum')
c['body'] = 'corpulento'


# ------------------------------------------------------------------ Equipo Zero

# Pinkus Mountbatten: tupé plano y ancho que sale hacia delante y se echa a la derecha en una sola punta (antes, dos
# puntas a los lados que parecían orejas de gato)
c = fix('go-zero', 'pinkus-mountbatten')
c['front'][1] = L(outline([(14, 40), (8, 18), (18, 2), (44, -8), (74, -8), (96, -4), (120, -10, 1), (104, 8), (92, 22), (86, 40), (50, 32)]), 'mid', 'f')
c['front'][2] = L(outline([(60, -6), (94, -2), (100, 6), (90, 20), (70, 20)]), 'shade', 'f', False)
c['back'][2] = L(outline([(12, 34), (8, 12), (24, -4), (50, -8), (76, -6), (98, -2), (120, -10, 1), (104, 8), (90, 34), (50, 30)]), 'mid', 'f')


# ------------------------------------------------------------------ Akizora Challengers

# Bobine Apples: señora rechoncha (cuerpo corpulento, no normal)
c = fix('go-akizora-challengers', 'bobine-apples')
c['body'] = 'corpulento'


# ------------------------------------------------------------------ Southern Claw

# Xavier Shotwell: de frente la melena es rubia y solo lleva una mecha rosa estrecha (antes el rosa tapaba casi todo el
# flequillo)
c = fix('go-southern-claw', 'xavier-shotwell')
c['front'][1] = L(outline([(26, 8), (40, 3), (30, 22), (18, 50), (12, 74), (12, 44)]), 'pink', 'b', False)
c['front'][4] = L(outline([(40, 24), (56, 14), (66, 12), (52, 22)]), 'pink', 'f', False)
