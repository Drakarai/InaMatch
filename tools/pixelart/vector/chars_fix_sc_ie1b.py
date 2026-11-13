"""Correcciones de la revisión de diseños (grupo sc_ie1b): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
import math
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad

K = 'scouts-ie1:'
# cara alargada de adulto (mandíbula larga)
LONG = blob([(18, 50), (50, 28), (82, 50), (84, 80), (76, 100), (62, 110), (50, 112), (38, 110), (24, 100), (16, 80)])


def spiral(cx, cy, r, turns=1.4, c='deep', w=1.1, z='f', a0=0.0):
    """Rizo en espiral (los rizos de los peinados de caracolillos)."""
    pts = [(cx + r * (1 - t) * math.cos(a0 + t * turns * 2 * math.pi), cy + r * 0.8 * (1 - t) * math.sin(a0 + t * turns * 2 * math.pi))
           for t in (i / 24 for i in range(22))]
    return L(pts, c, z, False, False, w)


# Rip Airman: el pelo es castaño grisáceo (no malva) y sube en un pico alto sobre la coronilla; los lados bajan lisos
# hasta las orejas como patillas y dejan la frente despejada; cara larga y narizota
c = copy.deepcopy(CHARS[K + 'rip-airman'])
c['pal'] = pal('#8e7a70', '#fad6a8', iris='#4a4a66', shade='#6e5c54', deep='#4e3e38')
c['face']['hairline'] = [(10, 74), (18, 60), (26, 46), (38, 38), (50, 36), (62, 38), (74, 46), (82, 60), (90, 74)]
c['front'] = [L(outline([(17, 76), (12, 46), (18, 20), (34, 4), (50, -14, 1), (66, 4), (82, 20), (88, 46), (83, 76), (78, 60), (70, 44), (50, 38), (30, 44), (22, 60)])),
              L(outline([(56, 0), (80, 18), (88, 46), (83, 72), (76, 44), (66, 22)]), 'shade', 'b', False),
              strand([(50, -10), (48, 36)], 'deep', 'b', 1.0), strand([(38, 6), (30, 40)], 'deep', 'b', 1.0), strand([(62, 6), (70, 40)], 'deep', 'b', 1.0)] \
    + [l for l in CHARS[K + 'rip-airman']['front'][5:]]
c['side'] = [L(outline([(72, 46), (82, 36), (80, 18), (64, 2), (44, -14, 1), (28, -2), (12, 12), (4, 36), (6, 62), (18, 80), (32, 76), (38, 62), (50, 50)])),
             L(outline([(5, 40), (30, 42), (38, 62), (32, 76), (18, 80), (6, 62)]), 'shade', 'b', False),
             strand([(40, -8), (60, 30)], 'deep', 'b', 1.0)] + [l for l in CHARS[K + 'rip-airman']['side'][2:]]
c['back'] = [L(outline([(16, 78), (12, 44), (18, 20), (34, 4), (50, -14, 1), (66, 4), (82, 20), (88, 44), (84, 78), (50, 84)])),
             L(outline([(56, 0), (80, 18), (88, 46), (84, 76), (62, 82)]), 'shade', 'b', False), strand([(50, -10), (50, 60)], 'deep', 'b', 1.0)]
CHARS[K + 'rip-airman'] = c

# Shemmy Ramis: los rizos pequeños de la nube parecían rombos (como otro par de ojos) en la frente: son caracolillos en
# espiral; las cejas son verde pálido
c = copy.deepcopy(CHARS[K + 'shemmy-ramis'])
fr_ = [l for l in c['front'] if not (l.get('ln') and l['c'] == 'shade')]
c['front'] = fr_ + [spiral(36, 30, 7, a0=0.5), spiral(64, 26, 8, a0=3.0), spiral(50, 12, 6, a0=1.6), spiral(22, 44, 5, a0=0.2), spiral(78, 44, 5, a0=2.6)]
for l in c['front']:
    if l['c'] == (230, 226, 170, 255):
        l['c'] = (196, 206, 130, 255)
c['side'] = c['side'] + [spiral(40, 24, 7, z='b'), spiral(20, 40, 6, z='b'), spiral(56, 8, 5, z='b')]
c['back'] = c['back'] + [spiral(36, 30, 7, z='b'), spiral(64, 30, 7, z='b', a0=2), spiral(50, 56, 7, z='b', a0=1), spiral(26, 60, 6, z='b'),
                         spiral(74, 60, 6, z='b', a0=3)]
CHARS[K + 'shemmy-ramis'] = c

# Ant Hophila (Otake): la franja de pelo verde oscuro le rodea la coronilla de oreja a oreja (de frente se ve el arco por
# encima de la cara), con el mechón blanco encima
c = copy.deepcopy(CHARS[K + 'ant-hophila'])
c['front'] = [L(outline([(6, 64), (4, 40), (14, 18), (50, 6), (86, 18), (96, 40), (94, 64), (80, 56), (20, 56)])),
              L(outline([(60, 8), (86, 18), (96, 42), (94, 62), (84, 36)]), 'shade', 'b', False)] + c['front'][2:]
c['side'] = [L(outline([(14, 74), (4, 50), (8, 28), (24, 10), (50, 4), (72, 10), (84, 24), (80, 32), (62, 26), (44, 28), (32, 40), (32, 62)])),
             L(outline([(5, 46), (24, 44), (32, 60), (14, 72)]), 'shade', 'b', False)] + c['side'][1:]
CHARS[K + 'ant-hophila'] = c

# Carey Ginu: labios rojos gruesos y bien visibles (en el retrato son de lo que más destaca)
c = copy.deepcopy(CHARS[K + 'carey-ginu'])
LIP = (204, 84, 84, 255)
c['front'] = [l for l in c['front'] if l['c'] != (200, 96, 90, 255)] + [
    L(blob([(40, 96), (46, 93), (50, 95), (54, 93), (60, 96), (56, 101), (50, 103), (44, 101)], 6), LIP, 'f', False, True),
    L(quad((41, 97), (50, 98.5), (59, 97)), OUTC, 'f', False, False, 0.9)]
CHARS[K + 'carey-ginu'] = c

# Carl Gnu: cabeza calva alargada, con la mandíbula larga
c = copy.deepcopy(CHARS[K + 'carl-gnu'])
c['face']['face_front'] = LONG
c['face']['mouth_y'] = 98
CHARS[K + 'carl-gnu'] = c

# Braden Bakewell: adulto de cara alargada
c = copy.deepcopy(CHARS[K + 'braden-bakewell'])
c['face']['face_front'] = LONG
c['face']['mouth_y'] = 98
CHARS[K + 'braden-bakewell'] = c
c['front'][2]['ln'] = False  # el tupé sin la línea interior, que hacía de visera de casco

# Shemmy Ramis: la boca naranja es enorme (casi de mejilla a mejilla), no un bulto en la barbilla
c = CHARS[K + 'shemmy-ramis']
ORANGE_MOUTH = (226, 126, 60, 255)
c['front'] = [l for l in c['front'] if l['c'] != ORANGE_MOUTH and not (l['w'] and l['c'] == OUTC and len(l['s']) == 21)] + [
    L(blob([(34, 90), (50, 88), (66, 90), (64, 98), (50, 102), (36, 98)], 6), ORANGE_MOUTH, 'f', False, True),
    L(quad((36, 94), (50, 97), (64, 94)), OUTC, 'f', False, False, 1.0)]

# Harry Caine: piel clara anaranjada como la del retrato (estaba muy morena)
c = copy.deepcopy(CHARS[K + 'harry-caine'])
c['pal']['skin'] = (242, 180, 122, 255)
c['pal']['skin_d'] = (214, 152, 100, 255)
CHARS[K + 'harry-caine'] = c

# Manny Kinsland: los dos tirabuzones en espiral de los lados de la melena quedaban tapados por la cara: van por fuera, a
# la altura de las mejillas
c = copy.deepcopy(CHARS[K + 'manny-kinsland'])
for l in c['front'][1:5]:
    l['z'] = 'f'
c['front'][1] = L(ell(8, 86, 10, 12), 'mid', 'f', ln=True)
c['front'][2] = L(ell(92, 86, 10, 12), 'mid', 'f', ln=True)
c['front'][3] = spiral(8, 86, 7, a0=0.0, c='deep', w=1.3)
c['front'][4] = spiral(92, 86, 7, a0=math.pi, c='deep', w=1.3)
CHARS[K + 'manny-kinsland'] = c
c = CHARS[K + 'shemmy-ramis']
c['front'] = c['front'][:-2] + [L(blob([(35, 86), (50, 84.5), (65, 86), (63, 92), (50, 95.5), (37, 92)], 6), ORANGE_MOUTH, 'f', False, True),
                                L(quad((37, 89), (50, 91.5), (63, 89)), OUTC, 'f', False, False, 1.0)]
c['face']['mouth_y'] = 90
c = CHARS[K + 'manny-kinsland']
c['side'] = c['side'] + [L(ell(30, 90, 9, 11), 'mid', 'f', ln=True), spiral(30, 90, 6, c='deep', w=1.3)]

# Braden Bakewell: raya a la izquierda de la imagen; a ese lado el pelo es corto y deja la frente despejada, y desde la raya
# un tupé grande cae en curva hacia la derecha hasta la ceja; las puntas salen hacia fuera por encima de las orejas
c = CHARS[K + 'braden-bakewell']
c['face']['hairline'] = [(8, 72), (14, 60), (20, 48), (30, 40), (40, 38), (52, 44), (66, 52), (80, 60), (92, 72)]
c['front'] = [L(outline([(4, 76, 1), (12, 64), (10, 40), (18, 16), (38, 2), (60, 0), (80, 10), (92, 32), (92, 58), (100, 76, 1), (86, 70), (82, 62), (66, 50),
                         (40, 38), (28, 42), (18, 54), (14, 68)])),
              L(outline([(60, 2), (80, 10), (92, 34), (92, 58), (98, 74), (86, 66), (80, 32)]), 'shade', 'b', False),
              L(outline([(36, 36), (40, 20), (58, 12), (78, 20), (90, 40), (92, 64, 1), (82, 54), (68, 44), (50, 38)]), 'mid', 'f', sil=False),
              L(outline([(60, 16), (78, 22), (90, 42), (92, 62, 1), (82, 46), (70, 32)]), 'shade', 'f', False),
              strand([(30, 40), (34, 12)], 'deep', 'b', 1.0), strand([(46, 34), (66, 24), (84, 44)], 'deep', 'f', 1.0)]

# ------------------------------------------------------------------ segunda pasada

from chars import messy  # noqa: E402


def edge(pts, w=1.2):
    """Contorno solo por el borde de abajo de un flequillo (las puntas que caen sobre la cara)."""
    return L(list(pts), OUTC, 'f', False, False, w)


# Jacky Lantern: no es una mata de pinchos sino una greña gris parda abundante, con las puntas desflecadas a los lados y un
# flequillo grueso que le cae en diagonal por la frente hasta el ojo izquierdo (de la imagen); ojos negros ovalados
# grandes con brillo y una sola ceja negra gruesa visible (la otra la tapa el flequillo)
c = copy.deepcopy(CHARS[K + 'jacky-lantern'])
c['pal'] = pal('#968c70', '#dc9a5e', shade='#776f58', deep='#58523f', light='#b8b098', nose='#e8aa72')
c['face']['eyes'] = 'none'
BANG = [(10, 66), (12, 40), (30, 20), (56, 16), (78, 24), (90, 42), (88, 60, 1), (78, 50), (68, 54, 1), (60, 46), (50, 58, 1), (44, 48), (36, 68, 1), (28, 56), (20, 72, 1)]
EYES = []
for x in (36, 64):
    EYES += [L(ell(x, 77, 4.2, 5.6), OUTC, 'f', False), L(ell(x - 1.2, 74.6, 1.4, 1.8), (255, 255, 255, 255), 'f', False)]
c['front'] = [L(outline([(10, 84, 1), (14, 68), (0, 62, 1), (8, 48), (-4, 36, 1), (10, 28), (12, 12), (28, -2), (50, -6), (74, -2), (90, 10), (102, 22, 1), (94, 32),
                         (104, 46, 1), (94, 52), (100, 68, 1), (88, 70), (86, 58), (14, 58)])),
              L(outline([(60, -2), (90, 10), (100, 24), (94, 34), (100, 46), (92, 54), (96, 66), (86, 60), (80, 30)]), 'shade', 'b', False),
              L(blob([(20, 14), (36, 2), (52, 0), (40, 12), (26, 22)], 6), 'light', 'b', False),
              L(outline(BANG), 'mid', 'f', False),
              L(outline([(58, 18), (78, 24), (90, 42), (88, 58, 1), (80, 40), (68, 28)]), 'shade', 'f', False),
              edge([(90, 42), (88, 60), (78, 50), (68, 54), (60, 46), (50, 58), (44, 48), (36, 68), (28, 56), (20, 72), (10, 66)]),
              strand([(30, 22), (40, 40), (44, 48)], 'deep', 'f', 1.0), strand([(56, 18), (64, 34), (68, 52)], 'deep', 'f', 1.0),
              L([(56, 67), (74, 63)], OUTC, 'f', False, False, 3.8),
              L(ell(48, 86, 0.8, 1.2), OUTC, 'f', False), L(ell(52, 86, 0.8, 1.2), OUTC, 'f', False)] + EYES
c['side'] = messy('side', amp=9, n=13, seed=21, rx=50) + [
    L(outline([(66, 12), (86, 22), (96, 40), (96, 62, 1), (88, 52), (84, 66, 1), (78, 48), (70, 32)]), 'mid', 'f', False),
    edge([(96, 40), (96, 62), (88, 52), (84, 66), (78, 48)]),
    L([(76, 64), (88, 63)], OUTC, 'f', False, False, 3.6),
    L(ell(83, 77, 2.8, 5.0), OUTC, 'f', False), L(ell(82.4, 74.8, 1.0, 1.5), (255, 255, 255, 255), 'f', False)]
c['back'] = messy('back', amp=9, n=13, seed=21, rx=52, nape=94)
CHARS[K + 'jacky-lantern'] = c

# Jack Pott: de perfil, el moño de su lado va a la altura de la oreja (encima de ella), no en lo alto de la cabeza
c = copy.deepcopy(CHARS[K + 'jack-pott'])
c['side'] = c['side'][:2] + [L(ell(38, 58, 11, 11), 'mid', 'f', ln=True), L(blob([(42, 50), (48, 56), (46, 66), (40, 62)], 5), 'shade', 'f', False),
                             spiral(37, 58, 6, c='deep', w=1.1)] + c['side'][4:]
CHARS[K + 'jack-pott'] = c

# Horace Nelson: de espaldas la sombra iba en una franja horizontal (parecía una cinta); el tupé y la nuca corta son una
# sola masa con la sombra en su lado
c = copy.deepcopy(CHARS[K + 'horace-nelson'])
c['back'] = [c['back'][0], L(outline([(60, -6), (74, -20), (80, -2), (84, 20), (84, 40), (82, 72), (66, 80), (62, 40)]), 'shade', 'b', False),
             strand([(34, 10), (56, -2), (72, -14)], 'deep', 'b', 1.0), strand([(30, 30), (30, 70)], 'shade', 'b', 1.0)]
CHARS[K + 'horace-nelson'] = c

# Drew Crenshaw: de espaldas es calvo por arriba (la coronilla en piel, sin bulto encima) y el pelo hace herradura por los
# lados y la nuca, con su mancha en zigzag en la coronilla
c = copy.deepcopy(CHARS[K + 'drew-crenshaw'])
c['back'] = [L(outline([(16, 80), (12, 52), (14, 36), (24, 28), (34, 40), (50, 46), (66, 40), (76, 28), (86, 36), (88, 52), (84, 80), (50, 86)])),
             L(outline([(62, 44), (76, 30), (86, 38), (88, 54), (84, 78), (62, 84)]), 'shade', 'b', False),
             L(outline([(42, 16), (52, 20), (48, 26), (58, 28), (60, 33), (51, 33), (49, 27), (40, 22)]), 'mid', 'b', False, True)]
CHARS[K + 'drew-crenshaw'] = c

# Odo Cologne: el nacimiento del pelo (pelo peinado hacia atrás, frente despejada) es una curva suave; con puntos sueltos
# salía un polígono anguloso que parecía el borde de una capucha
c = copy.deepcopy(CHARS[K + 'odo-cologne'])
c['face']['hairline'] = [(12, 70)] + quad((15, 56), (50, 16), (85, 56)) + [(88, 70)]
CHARS[K + 'odo-cologne'] = c

# Harry Caine: el flequillo (de frente) y el mechón (de perfil) llevaban el contorno entero, que dibujaba un arco dentro del
# pelo; ahora solo el borde de las puntas
c = CHARS[K + 'harry-caine']
c['front'][2]['ln'] = False
c['front'].append(edge([(86, 66), (80, 52), (72, 62), (66, 48), (58, 60), (52, 46), (44, 60), (40, 46), (30, 60), (24, 50), (14, 66)]))
c['side'][2]['ln'] = False
c['side'].append(edge([(92, 46), (88, 58), (80, 40)]))
# Jack Pott: el flequillo de perfil sin el contorno entero (parecía una aleta), solo el borde de las puntas
c = CHARS[K + 'jack-pott']
c['side'][-1]['ln'] = False
c['side'].append(edge([(92, 36), (92, 56), (84, 56)]))


# ------------------------------------------------------------------ tercera pasada: tono de piel y de pelo
# Piel medida en el retrato de Victory Road (mejillas y barbilla, tono iluminado más frecuente): muchos dibujos tenían la
# piel rosada/pálida donde el retrato es anaranjado/tostado. Se cambia skin (skin_d = 0,86) y las capas de color fijo que
# repetían la piel antigua; el pelo, donde el tono se alejaba claramente del retrato (mid/shade/deep/light y capas fijas).


def _rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def _mix(c, d, t):
    return tuple(int(c[i] + (d[i] - c[i]) * t) for i in range(3)) + (255,)


def _near(a, b, tol=6):
    return isinstance(a, tuple) and len(a) >= 3 and sum(abs(a[i] - b[i]) for i in range(3)) <= tol


def _recolor(c, subs):
    """Cambia en las capas (y valores sueltos de la cara) los colores fijos que repiten uno antiguo."""
    def fix(v):
        for old, new in subs:
            if _near(v, old):
                return new
        return v
    for view in ('front', 'side', 'back'):
        for item in c.get(view, []):
            for l in (item if isinstance(item, list) else [item]):
                if isinstance(l, dict) and 'c' in l:
                    l['c'] = fix(l['c'])
    for k, v in list(c.get('face', {}).items()):
        if isinstance(v, tuple) and len(v) == 4 and all(isinstance(x, int) for x in v):
            c['face'][k] = fix(v)


def _reskin(pid, h):
    c = copy.deepcopy(CHARS[_KS + pid])
    p = c['pal']
    s = _rgb(h)
    old, old_d = p['skin'], p['skin_d']
    p['skin'], p['skin_d'] = s, _tone(s, 0.86)
    _recolor(c, [(old, p['skin']), (old_d, p['skin_d'])])
    CHARS[_KS + pid] = c


def _rehair(pid, h):
    c = copy.deepcopy(CHARS[_KS + pid])
    p = c['pal']
    m = _rgb(h)
    olds = {k: p[k] for k in ('mid', 'shade', 'deep', 'light') if k in p}
    std = {'mid': m, 'shade': _tone(m, 0.78), 'deep': _tone(m, 0.6), 'light': _mix(m, (255, 255, 255), 0.38)}
    om = olds['mid']
    for k, v in olds.items():  # mantiene la relación de cada tono con el principal
        p[k] = std[k] if k == 'mid' else tuple(max(0, min(255, int(v[i] * m[i] / max(om[i], 1)))) for i in range(3)) + (255,)
    _recolor(c, [(olds[k], p[k]) for k in olds])
    CHARS[_KS + pid] = c


_KS = 'scouts-ie1:'
_SKIN = {
    'spike-coiffs': '#f1b46d',
    'braden-bakewell': '#f1b56d',
    'spike-needle': '#f1b56d',
    'bob-dingy-dingnagian': '#f1b46d',
    'bully-thrower': '#f1b46e',
    'troy-trucker': '#fab16a',
    'pica-vellosum': '#f2b56f',
    'rich-eden': '#f1b46d',
    'theo-riser': '#f1b46c',
    'spike-clutcher': '#f1b46d',
    'ryder-waverly': '#f0b56e',
    'hank-o-buff': '#cd924b',
    'toby-patient': '#ce924a',
    'robin-cruise': '#ce924a',
    'gene-bates': '#f1b56d',
    'hal-lebutt': '#f1b46d',
    'ifan-tassy': '#f1b46c',
    'bones-size': '#c6985a',
    'marv-errick': '#c69859',
    'buster-chopps': '#f1b46d',
    'rush-tooset': '#f1b56d',
    'ricky-charmers': '#f0b46d',
    'stu-lucky-perstitious': '#cd924c',
    'char-shumaker': '#f1b56d',
    'powers-squatts': '#f2b371',
    'rod-entwhistle': '#f2b46d',
    'mark-skidfree': '#cd924b',
    'jim-reed': '#cc924c',
    'homer-pidgeon': '#f1b56e',
    'glen-adeer': '#f1b56e',
    'jacky-lantern': '#f0b46c',
    'bear-turnbull': '#c6995a',
    'sid-parting': '#f1b46e',
    'bill-phee': '#f0b56d',
    'jack-pott': '#f1b56d',
    'gabriel-shekinah': '#f0b46d',
    'bert-neptune': '#fde9ba',
    'ivor-parrot': '#f0b46c',
    'martin-sheller': '#f2b36d',
    'hal-mullet': '#f1b56c',
    'bill-moony': '#fece95',
    'per-hockside': '#f1b56c',
    'healey-proctor': '#cd924a',
    'lee-gleagle': '#c59959',
    'macky-valley': '#f1b46c',
    'carl-gnu': '#ce9149',
    'raven-crowe': '#f1b46d',
    'cruz-ligner': '#f0b665',
    'colin-lection': '#ce924b',
    'pres-cripton': '#f2b177',
    'shemmy-ramis': '#f1b56d',
    'sharkey-gobble': '#f1b56d',
    'shaun-staid': '#f9d79d',
    'matt-matickal': '#f1b46d',
    'chick-adiddy': '#f1b46d',
    'stu-shiner': '#f0b46d',
    'heath-freke': '#f1b56d',
    'beau-fort': '#f1b46d',
    'cam-agent-broadsheet': '#f1b46f',
    'virgil-lantis': '#ce914a',
    'ray-deo': '#f2b46d',
    'patch-borgnine': '#f9b16a',
    'john-corder': '#f1b36b',
    'teddy-kodiak': '#f1b56d',
    'mal-inger': '#fab46b',
    'lucky-winn': '#fee7b3',
    'paul-rush': '#f7b365',
    'sim-cope': '#fad69f',
    'sylver-stone': '#cd924a',
    'paddy-popper': '#f1b46d',
    'troy-carr': '#cd924a',
    'tim-crochett': '#c8965a',
    'finn-carper': '#f1b56d',
    'harvey-sweats': '#ce924a',
    'percy-verence': '#f7c797',
    'billy-nomates': '#f1b26a',
    'jim-makegood': '#f0b46d',
    'jools-iceberg': '#f0b56d',
    'monty-burrows': '#f1b56e',
    'sal-curie': '#eeb176',
    'pauly-ontology': '#f1b46d',
    'gore-lyath': '#f1b46e',
    'ray-dioset': '#f0b66a',
    'gerry-attrick': '#f1b56d',
    'carson-haynes': '#ce924b',
    'carey-ginu': '#f1b36d',
    'conor-abley': '#c6985a',
    'skip-rooter': '#f1b56d',
    'crane-clawson': '#c69859',
    'manny-kinsland': '#fac778',
    'creed-craving': '#c6995a',
    'john-maggie': '#f1b56d',
    'cam-o-miles': '#f1b46e',
    'iggy-loyaller': '#f2b56e',
    'ringo-stagg': '#dda35c',
    'terrence-anthem': '#f9d79d',
    'jody-macgough': '#f1b46d',
    'luke-triton': '#f3af86',
    'jimmy-mach': '#be854d',
    'buster-locke': '#f1b370',
    'carey-bean': '#b07957',
    'taka-tanaka': '#f1b56e',
    'john-coralli': '#f1b46d',
    'joe-lamkin': '#f2b56e',
    'ben-curd': '#f1b46c',
    'jim-cook': '#f1b46d',
    'manny-atom': '#cf924a',
    'seymour-senary': '#ce924b',
    'ramsey-faroe': '#f3b470',
    'kim-ono': '#f1b46d',
    'beau-painton': '#f1b56d',
    'mitch-hett': '#f1b46e',
    'dai-hart': '#ce924b',
}
_HAIR = {
    'rod-entwhistle': '#699398',
    'tosh-coach': '#6d9195',
    'troy-trucker': '#b77a69',
    'sam-murray': '#495969',
}
for _p, _h in _SKIN.items():
    _reskin(_p, _h)
for _p, _h in _HAIR.items():
    _rehair(_p, _h)
