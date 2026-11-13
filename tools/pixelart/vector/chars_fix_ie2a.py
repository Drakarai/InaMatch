"""Correcciones de la revisión de diseños (grupo ie2a): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from heads import L, blob, fat, spk


def _base(team, pid):
    """Dibujo que usa ahora el jugador en ese equipo (su versión del equipo o la de siempre)."""
    k = f'{team}:{pid}'
    return copy.deepcopy(CHARS[k] if k in CHARS else CHARS[pid])


# ------------------------------------------------------------------ Shawn Froste (Raimon de IE2 y Hakuren): en el modelo la mitad
# de abajo del pelo (nuca y puntas de los lados) es malva oscuro; el dibujo solo lo tenía en dos puntitas de delante
def _froste_tips(c):
    c['pal']['tips'] = (138, 104, 120, 255)
    back_tips = [((10, 76), (28, 84), (6, 96)), ((28, 84), (50, 88), (36, 102)), ((50, 88), (72, 84), (66, 102)),
                 ((72, 84), (90, 76), (94, 96)), ((2, 58), (10, 74), (-14, 76)), ((90, 74), (98, 58), (114, 76))]
    c['back'] = c['back'] + [L(blob([(4, 62), (96, 62), (94, 78), (72, 84), (50, 88), (28, 84), (6, 78)], 6), 'tips', 'b', False)] + \
        [L(fat(a, b, t, 3), 'tips', 'b', False) for a, b, t in back_tips]
    side_tips = [((4, 54), (8, 70), (-16, 66)), ((8, 70), (16, 82), (-12, 92)), ((18, 84), (32, 90), (8, 102))]
    c['side'] = c['side'] + [L(blob([(6, 58), (28, 62), (46, 78), (44, 90), (14, 90), (4, 72)], 6), 'tips', 'b', False)] + \
        [L(fat(a, b, t, 3), 'tips', 'b', False) for a, b, t in side_tips]
    front_tips = [((2, 58), (10, 74), (-14, 76)), ((90, 74), (98, 58), (114, 76)), ((8, 72), (18, 80), (-2, 90)), ((82, 80), (92, 72), (102, 90))]
    c['front'] = c['front'] + [L(fat(a, b, t, 3), 'tips', 'b', False) for a, b, t in front_tips]
    return c


for _team, _pid in (('ie2-second-raimon', 'shawn-froste'), ('ie2-second-raimon', 'shawn-froste-fubuki'),
                    ('ie2-second-raimon', 'shawn-froste-fubuki-cc'), ('ie2-hakuren', 'shawn-froste')):
    _src = f'{_team}:{_pid}' if f'{_team}:{_pid}' in CHARS else 'shawn-froste'
    CHARS[f'{_team}:{_pid}'] = _froste_tips(copy.deepcopy(CHARS[_src]))


# ------------------------------------------------------------------ Bobby Shearer (Raimon de IE2): en el modelo, mechones de punta
# hacia arriba y los lados cortos; el pelo revuelto en bola que tenía no se le parecía. Se recuperan sus pinchos de arriba.
def _bobby():
    import chars as _C
    c = copy.deepcopy(CHARS['bobby-shearer'])
    top = copy.deepcopy(_C.BOBBY_TOP)
    c['front'] = top + c['front'][1:]
    c['back'] = copy.deepcopy(top) + c['back'][1:]
    c['side'] = [spk((16, 50), (28, 34), (2, 30), 5), spk((24, 36), (40, 24), (12, 8), 5), spk((38, 26), (54, 20), (34, 0), 5),
                 spk((52, 20), (66, 22), (58, 0), 4, light_left=False), spk((64, 24), (78, 32), (78, 10), 4, light_left=False)] + c['side'][1:]
    return c


CHARS['ie2-second-raimon:bobby-shearer'] = _bobby()


# ------------------------------------------------------------------ Martin Ursus (Hakuren): el tupé plano es mucho más alto en el modelo
def _martin():
    c = copy.deepcopy(CHARS['martin-ursus'])
    c['front'][0] = L(blob([(14, 62), (12, 10), (10, -24), (50, -32), (90, -24), (88, 10), (86, 62)]))
    c['front'][1] = L(blob([(62, -28), (86, 8), (84, 60), (72, 56)], 6), 'shade', 'b', False)
    c['side'][0] = L(blob([(44, 70), (20, 68), (10, 40), (12, -6), (30, -30), (66, -30), (88, -18), (92, 18), (78, 32), (60, 36), (52, 50)]))
    c['back'][0] = L(blob([(14, 74), (12, 10), (10, -24), (50, -32), (90, -24), (88, 10), (86, 74), (66, 86), (34, 86)]))
    c['back'][1] = L(blob([(58, -28), (86, 8), (84, 72), (66, 84)], 6), 'shade', 'b', False)
    return c


CHARS['ie2-hakuren:martin-ursus'] = _martin()

# ------------------------------------------------------------------ Oumihara
_c = _base('ie2-oumihara', 'coral-talent')  # ojos dorados, no oscuros
_c['pal']['iris'] = (206, 168, 52, 255)
CHARS['ie2-oumihara:coral-talent'] = _c
_c = _base('ie2-oumihara', 'victor-hills')  # cuerpo delgado y fibroso en el modelo, no gordo
_c['body'] = 'normal'
CHARS['ie2-oumihara:victor-hills'] = _c
_c = _base('ie2-oumihara', 'stan-andagi')  # bajo y ancho de hombros
_c['body'] = 'corpulento'
CHARS['ie2-oumihara:stan-andagi'] = _c

# ------------------------------------------------------------------ SP Fixers: Ian Smith es alto y flaco en el modelo
_c = _base('ie2-sp-fixers', 'ian-smith')
_c['body'] = 'delgado'
CHARS['ie2-sp-fixers:ian-smith'] = _c

# ------------------------------------------------------------------ Jóvenes Inazuma: Garret sonríe con la boca cerrada (sin dientes)
_c = _base('ie2-young-inazuma', 'garret-hairtown')
_c['face'] = {**_c['face'], 'mouth': 'smile'}
CHARS['ie2-young-inazuma:garret-hairtown'] = _c


# ================================================================== segunda pasada (detalles)
from chars import outline, rope  # noqa: E402
from heads import ell, quad, strand  # noqa: E402


# ------------------------------------------------------------------ Dora Delight (Oumihara): el gorro es una caracola en espiral de
# pisos que se estrechan hacia arriba (ancha abajo, más que la cabeza), azul celeste con surcos grises y pinchos grises en los
# bordes de cada piso; debajo, melena naranja corta con flequillo
def _dora():
    c = copy.deepcopy(CHARS['dora-delight'])
    c['pal'].update(shell=(184, 228, 230, 255), shell_d=(138, 180, 190, 255), groove=(118, 128, 134, 255), spike=(150, 156, 162, 255))
    tiers = [(-6, 58, 106), (2, 42, 98), (12, 26, 88), (24, 12, 76), (36, 0, 64)]  # (x izq, y del borde de abajo, x der)

    def shell(view):
        dx = 4 if view == 'side' else 0
        pts = [(-8 + dx, 62)]
        for k, (x0, y, x1) in enumerate(tiers):
            pts += [(x0 - 2 + dx, y - 2), (x0 + 6 + dx, y - 10)]
        pts += [(50 + dx, -10)]
        for k, (x0, y, x1) in reversed(list(enumerate(tiers))):
            pts += [(x1 - 6 + dx, y - 10), (x1 + 2 + dx, y - 2)]
        pts += [(108 + dx, 62), (50 + dx, 68)]
        out = [L(blob(pts, 6), 'shell', 'f', ln=True),
               L(blob([(60 + dx, -4), (100 + dx, 34), (106 + dx, 60), (70 + dx, 64)], 6), 'shell_d', 'f', False)]
        for k, (x0, y, x1) in enumerate(tiers[1:]):  # surcos entre pisos
            out.append(L(quad((x0 - 4 + dx, y + 2), (50 + dx, y + 12), (x1 + 4 + dx, y + 2)), 'groove', 'f', False, False, 2.4))
        out.append(L(quad((-6 + dx, 62), (50 + dx, 72), (106 + dx, 62)), 'groove', 'f', False, False, 2.6))
        for k, (x0, y, x1) in enumerate(tiers[:4]):  # pinchos en los bordes de los pisos
            for x, s in ((x0 + dx, -1), (x1 + dx, 1)):
                out.append(L([(x, y - 8), (x + s * 9, y - 4), (x, y)], 'spike', 'f', ln=True))
            if view != 'side' and k < 3:
                xm = 50 + (k - 1) * 18
                out.append(L([(xm - 3, y + 6), (xm, y - 2), (xm + 3, y + 6)], 'spike', 'f', ln=True))
        out.append(L([(47 + dx, -8), (50 + dx, -20), (53 + dx, -8)], 'spike', 'f', ln=True))
        return out

    from chars_umbrella import BOB_B, BOB_F, BOB_S, fringe
    c['front'] = [L(blob(BOB_F))] + fringe(4, 54, 70) + shell('front')
    c['side'] = [L(blob(BOB_S))] + shell('side')
    c['back'] = [L(blob(BOB_B))] + shell('back')
    c['face'] = {**c['face'], 'hairline': (66, 60)}
    return c


CHARS['ie2-oumihara:dora-delight'] = _dora()


# ------------------------------------------------------------------ Mackenzie Fordline (Oumihara): la cabeza rapada (castaño rojizo
# oscuro con surcos) en un lado y, encima, un montón de mechones rojos gruesos y planos que caen hacia el lado izquierdo de la
# imagen hasta la oreja; gafas de sol pequeñas con montura dorada
def _mackenzie():
    c = copy.deepcopy(CHARS['mackenzie-fordline'])
    c['pal'].update(shave=(122, 52, 32, 255), shave_d=(92, 36, 22, 255), frame=(214, 190, 80, 255))
    SK_F = [(16, 66), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 66)]
    locks_f = [((72, 4), (40, -10), (2, 6)), ((80, 14), (44, 2), (-2, 30)), ((76, 24), (36, 14), (4, 52)), ((60, 30), (26, 26), (8, 70)),
               ((84, 6), (66, -8), (30, -16)), ((88, 24), (70, 18), (56, 40)), ((56, 14), (30, 0), (14, -10))]
    front = [L(blob(SK_F), 'shave'), L(blob([(62, 14), (86, 36), (84, 64), (74, 60)], 6), 'shave_d', 'b', False)]
    front += [strand([(66 + k * 6, 30), (70 + k * 6, 58)], 'shave_d', 'b', 1.4) for k in range(3)]
    for k, (a, m, b) in enumerate(locks_f):
        front.append(L(rope(a, m, b, 16), 'mid' if k % 2 == 0 else 'shade', 'b'))
    front += [L(blob([(22, 70), (44, 70), (42, 78), (24, 78)], 4), 'lens', 'f', ln=True), L(blob([(78, 70), (56, 70), (58, 78), (76, 78)], 4), 'lens', 'f', ln=True),
              L([(44, 72), (56, 72)], 'frame', 'f', False, False, 1.6), L([(20, 70), (80, 70)], 'frame', 'f', False, False, 1.0)]
    side = [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]), 'shave'),
            strand([(20, 50), (34, 70)], 'shave_d', 'b', 1.4), strand([(26, 42), (42, 64)], 'shave_d', 'b', 1.4)]
    locks_s = [((80, 18), (56, -12), (24, -8)), ((70, 10), (36, -4), (4, 14)), ((60, 22), (24, 16), (-4, 40)), ((86, 30), (88, 12), (96, 2)),
               ((44, 34), (14, 40), (2, 66)), ((74, 26), (60, 0), (40, -16)), ((40, 12), (14, 2), (-6, 18))]
    for k, (a, m, b) in enumerate(locks_s):
        side.append(L(rope(a, m, b, 16), 'mid' if k % 2 == 0 else 'shade', 'b'))
    side.append(L(blob([(76, 70), (94, 70), (92, 78), (78, 78)], 4), 'lens', 'f', ln=True))
    side.append(L([(76, 72), (52, 68)], 'frame', 'f', False, False, 1.2))
    back = [L(blob([(16, 72), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 72), (66, 88), (34, 88)]), 'shave'),
            L(blob([(56, 30), (84, 40), (84, 70), (62, 86)], 6), 'shave_d', 'b', False)]
    back += [strand([(20 + k * 7, 40 + k * 2), (24 + k * 7, 76)], 'shave_d', 'b', 1.4) for k in range(3)]
    locks_b = [((30, 4), (60, -10), (98, 8)), ((22, 16), (60, 4), (102, 30)), ((28, 26), (66, 16), (96, 52)), ((40, 34), (74, 30), (92, 68)),
               ((16, 8), (34, -8), (70, -16)), ((14, 26), (30, 18), (44, 40))]
    for k, (a, m, b) in enumerate(locks_b):
        back.append(L(rope(a, m, b, 16), 'mid' if k % 2 == 0 else 'shade', 'b'))
    c['front'], c['side'], c['back'] = front, side, back
    c['face'] = {**c['face'], 'hairline': (58, 48)}
    return c


CHARS['ie2-oumihara:mackenzie-fordline'] = _mackenzie()


# ------------------------------------------------------------------ Jack Griddle (Oumihara): pelo morado peinado hacia atrás y hacia
# arriba (no un erizo), pegado a los lados, con mechones que bajan por delante de las orejas; pinchos hacia atrás de perfil y
# hacia abajo en la nuca
def _jack():
    c = copy.deepcopy(CHARS['jack-griddle'])
    lens = c['front'][-1]
    SK = [(14, 66), (12, 36), (22, 14), (50, 4), (78, 14), (88, 36), (86, 66), (76, 52), (50, 46), (24, 52)]
    c['front'] = [spk((22, 20), (40, 10), (24, -14), 5), spk((38, 10), (56, 6), (46, -18), 5), spk((54, 6), (72, 10), (70, -14), 5, light_left=False),
                  spk((70, 12), (84, 26), (90, -2), 5, light_left=False), spk((12, 40), (22, 20), (4, 8), 4),
                  L(blob(SK)), L(blob([(62, 10), (88, 36), (86, 64), (74, 54)], 6), 'shade', 'b', False),
                  strand([(30, 46), (34, 20), (40, 8)], 'deep', 'b', 1.2), strand([(50, 44), (50, 16), (52, 4)], 'deep', 'b', 1.2),
                  strand([(70, 46), (66, 20), (62, 8)], 'deep', 'b', 1.2),
                  spk((12, 52), (22, 52), (16, 84), 2, z='f'), spk((78, 52), (88, 52), (84, 84), 2, z='f', light_left=False), lens]
    c['face'] = {**c['face'], 'hairline': (54, 44)}
    c['side'] = [spk((40, 10), (62, 6), (20, -10), 6), spk((22, 22), (42, 10), (-2, 4), 6), spk((14, 40), (24, 22), (-8, 26), 6),
                 spk((14, 60), (16, 42), (-8, 52), 5), spk((22, 80), (16, 62), (-2, 80), 4),
                 L(blob([(44, 90), (22, 88), (12, 64), (14, 36), (30, 14), (56, 6), (78, 14), (88, 30), (76, 38), (62, 44), (54, 60), (50, 80)])),
                 L(blob([(16, 48), (18, 76), (36, 86), (28, 60)], 6), 'shade', 'b', False),
                 strand([(78, 22), (50, 16), (24, 30)], 'deep', 'b', 1.2), strand([(70, 34), (44, 30), (20, 50)], 'deep', 'b', 1.2),
                 spk((60, 50), (68, 50), (64, 80), 2, z='f'), c['side'][-1]]
    c['back'] = [spk((22, 20), (40, 10), (24, -14), 5), spk((38, 10), (56, 6), (46, -18), 5), spk((54, 6), (72, 10), (70, -14), 5, light_left=False),
                 spk((70, 12), (84, 26), (90, -2), 5, light_left=False),
                 L(blob([(14, 72), (12, 36), (22, 14), (50, 4), (78, 14), (88, 36), (86, 72), (64, 84), (36, 84)])),
                 L(blob([(58, 10), (88, 36), (86, 70), (64, 82)], 6), 'shade', 'b', False),
                 spk((22, 76), (38, 82), (28, 98), 3), spk((38, 82), (52, 84), (46, 100), 3), spk((52, 84), (66, 82), (58, 100), 3, light_left=False),
                 spk((66, 80), (80, 74), (76, 96), 3, light_left=False),
                 strand([(30, 70), (34, 30), (40, 10)], 'deep', 'b', 1.2), strand([(70, 70), (66, 30), (60, 10)], 'deep', 'b', 1.2)]
    return c


CHARS['ie2-oumihara:jack-griddle'] = _jack()


# ------------------------------------------------------------------ Kim Powell (Génesis): melena granate larga y abultada con raya en
# medio, que cae por los lados en grandes tirabuzones hasta por debajo de los hombros
def _kim():
    c = copy.deepcopy(CHARS['kim-powell'])
    # contorno: raya en medio, volumen a los lados que se ensancha hacia abajo y acaba en tirabuzones a la altura de los hombros
    mane = [(50, 2), (70, -2), (90, 12), (102, 40), (108, 70), (114, 93.6), (110, 106.8, 1), (100, 100.8), (96, 110.4, 1), (86, 102), (80, 91.2),
            (80, 60), (20, 60), (20, 91.2), (14, 102), (4, 110.4, 1), (0, 100.8), (-10, 106.8, 1), (-14, 93.6), (-8, 70), (-2, 40), (10, 12), (30, -2)]
    curl = lambda x, y, s: strand([(x, y), (x + s * 6, y + 10), (x + s * 4, y + 24)], 'deep', 'b', 1.2)
    c['front'] = [L(outline(mane)), L(outline([(64, 4), (92, 18), (104, 60), (110, 96), (96, 103.2), (84, 88), (82, 50)]), 'shade', 'b', False),
                  curl(-2, 74, 1), curl(6, 90, 1), curl(102, 74, -1), curl(94, 90, -1),
                  strand([(50, 4), (50, 26)], 'deep', 'b', 1.4), L(ell(30, 14, 9, 3.5), 'light', 'b', False), L(ell(70, 14, 9, 3.5), 'light', 'b', False),
                  spk((44, 8), (54, 10), (16, 62), 7, z='f'), spk((46, 10), (56, 8), (84, 62), 7, z='f', light_left=False)]
    side_mane = [(56, 0), (80, 8), (92, 30), (80, 44), (62, 50), (54, 62), (56, 91.2), (50, 103.2), (40, 109.2, 1), (32, 100.8), (18, 110.4, 1), (8, 102), (-6, 106.8, 1),
                 (-8, 90), (-6, 50), (6, 20), (28, 2)]
    c['side'] = [L(outline(side_mane)), L(outline([(2, 40), (30, 50), (44, 93.6), (30, 103.2), (4, 98.4)]), 'shade', 'b', False),
                 curl(4, 80, 1), curl(24, 88, 1), curl(42, 84, 1), L(ell(36, 12, 10, 3.5), 'light', 'b', False),
                 spk((56, 30), (88, 40), (92, 64), 5, z='f', light_left=False)]
    back_mane = [(50, 2), (70, -2), (90, 12), (102, 40), (108, 70), (114, 93.6), (110, 106.8, 1), (96, 102), (88, 111.6, 1), (74, 103.2), (62, 112.8, 1),
                 (50, 104.4), (38, 112.8, 1), (26, 103.2), (12, 111.6, 1), (4, 102), (-10, 106.8, 1), (-14, 93.6), (-8, 70), (-2, 40), (10, 12), (30, -2)]
    c['back'] = [L(outline(back_mane)), L(outline([(60, 4), (92, 18), (104, 60), (108, 98.4), (84, 105.6), (66, 90)]), 'shade', 'b', False),
                 curl(4, 84, 1), curl(26, 91.2, 1), curl(50, 91.2, 1), curl(74, 91.2, -1), curl(98, 84, -1),
                 strand([(50, 4), (50, 70)], 'deep', 'b', 1.2), L(ell(30, 14, 9, 3.5), 'light', 'b', False)]
    c['face'] = {**c['face'], 'hairline': (60, 46)}
    return c


CHARS['ie2-the-genesis:kim-powell'] = _kim()
