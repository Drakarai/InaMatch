"""Correcciones de la revisión de diseños (grupo sc_ie2a): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de IE2 (primera mitad de la lista): casi todo coincidía con su retrato de Victory Road; lo que se corrige aquí
son sobre todo ojos y bocas que en el retrato son muy característicos (ojos grandes, sonrisas enormes, gafas opacas...)."""
import copy  # noqa: F401
from chars import CHARS, L, OUTC, blob, ell  # noqa: F401
from heads import quad

K = 'scouts-ie2:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
TW, TB = (248, 248, 248, 255), (30, 26, 30, 255)  # blanco y negro de los módulos de ojeadores de IE2


def _c(h):
    h = h.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


def flat(view_layers):
    return [l for item in view_layers for l in (item if isinstance(item, list) else [item])]


def take(pid):
    """Copia del dibujo actual del ojeador, con las capas de cada vista aplanadas."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = flat(c[v])
    return c


def put(pid, c):
    CHARS[K + pid] = c


def eye(cx, ey, rx, ry, s=1, pup=(0.0, 0.0, 3.0), lid=None, tilt=0.0, iris=None, hi=True, lw=1.4, lidw=2.4):
    """Ojo de dibujos animados como capas: blanco ovalado con contorno, pupila (dx, dy, r) y, si se da lid (0..1), el
    párpado de arriba lo corta en recto (tilt lo inclina: >0 baja hacia la nariz = ceño). s = 1 ojo izquierdo, -1 derecho."""
    pts = ell(cx, ey, rx, ry, 40)
    if lid is not None:
        ly = lambda x: ey - ry * (1 - 2 * lid) + tilt * (x - cx) * s
        pts = [(x, max(y, ly(x))) for x, y in pts]
    out = [L(pts, WHITE, 'f', False), L(pts + [pts[0]], OUTC, 'f', False, False, lw)]
    dx, dy, r = pup
    px, py = cx + dx * s, ey + dy
    if iris:
        ip = [(x, y) for x, y in ell(px, py, r * 1.6, r * 1.75, 30)]
        if lid is not None:
            ip = [(x, max(y, ly(x))) for x, y in ip]
        out.append(L(ip, iris, 'f', False))
    pp = ell(px, py, r, r * 1.1, 24)
    if lid is not None:
        pp = [(x, max(y, ly(x) + 0.3)) for x, y in pp]
    out.append(L(pp, BLACK, 'f', False))
    if hi:
        out.append(L(ell(px - r * 0.35, py - r * 0.4, r * 0.32, r * 0.32, 12), WHITE, 'f', False))
    if lid is not None:
        out.append(L([(cx - rx - 1, ly(cx - rx - 1)), (cx + rx + 1, ly(cx + rx + 1))], OUTC, 'f', False, False, lidw))
    return out


def eyes2(ey=76, sep=14, **k):
    return eye(50 - sep, ey, s=1, **k) + eye(50 + sep, ey, s=-1, **k)


def side_eye(ey=76, rx=4.2, ry=None, pup=(1.6, 0.0, 2.4), lid=None, tilt=0.0, iris=None, x=80.5):
    return eye(x, ey, rx, ry or rx * 1.25, s=1, pup=pup, lid=lid, tilt=-tilt, iris=iris, hi=False, lw=1.2, lidw=2.0)


def big_grin(y=96, w=17, h=11, lip=(110, 40, 40, 255)):
    """Sonrisa enorme en D con la fila de dientes de arriba."""
    outer = blob([(50 - w, y - 2), (50, y), (50 + w, y - 2), (50 + w * 0.72, y + h * 0.7), (50, y + h), (50 - w * 0.72, y + h * 0.7)], 6)
    teeth = blob([(50 - w + 2.4, y - 0.8), (50, y + 1), (50 + w - 2.4, y - 0.8), (50 + w * 0.62, y + h * 0.5), (50, y + h * 0.62), (50 - w * 0.62, y + h * 0.5)], 6)
    return [L(outer, lip, 'f', True), L(teeth, WHITE, 'f', False),
            L(quad((50 - w + 3, y + 2.4), (50, y + 4.6), (50 + w - 3, y + 2.4)), OUTC, 'f', False, False, 0.8)]


def side_grin(y=96, h=9):
    return [L(blob([(74, y - 1), (88, y - 3), (87, y + h * 0.6), (78, y + h * 0.8)], 4), (110, 40, 40, 255), 'f', True),
            L(blob([(76, y), (87, y - 1.6), (86.4, y + 3.4), (77, y + 3.6)], 3), WHITE, 'f', False)]


# ------------------------------------------------------------------------------------------------------- correcciones

# Lou Fauntleroy: la peluca rubia de rizos no deja calva la coronilla: el pelo dorado le rodea la cabeza por arriba
# (un reborde de rizos sobre la frente alta) y baja en tirabuzones por los lados
c = take('lou-fauntleroy')
rim_out = [(14, 54), (14, 30), (24, 12), (38, 2), (50, 0), (62, 2), (76, 12), (86, 30), (86, 54)]
rim_in = [(78, 52), (76, 32), (68, 18), (58, 12), (50, 11), (42, 12), (32, 18), (24, 32), (22, 52)]
c['front'].insert(1, L(blob(rim_out + rim_in, 4), 'mid', 'b'))
c['front'].insert(2, L(quad((30, 14), (50, 4), (70, 14)), 'deep', 'b', False, False, 1.2))
c['side'].insert(1, L(blob([(22, 46), (24, 22), (40, 6), (58, 2), (76, 8), (88, 22), (80, 26), (66, 14), (52, 12), (38, 18), (32, 30), (32, 46)], 4), 'mid', 'b'))
put('lou-fauntleroy', c)

# Fred Punch: ojos grandes y blancos con iris gris verdoso unidos por un antifaz negro, cejas castañas muy gruesas (la
# izquierda en arco alto, la derecha en ceño) y una sonrisa enorme de dientes de oreja a oreja
c = take('fred-punch')
nose = c['front'][-7]
c['front'] = c['front'][:-9]
BROW = _c('#5a3018')
c['front'] += [L(blob([(16, 72), (30, 56), (40, 58), (48, 68), (44, 70), (36, 64), (28, 64), (20, 74)], 4), BROW, 'f', False),
               L(blob([(52, 70), (62, 62), (82, 66), (82, 70), (64, 68), (56, 74)], 4), BROW, 'f', False),
               L(blob([(24, 74), (36, 70), (50, 76), (64, 70), (76, 74), (76, 84), (64, 82), (50, 80), (36, 82), (24, 84)], 4), BLACK, 'f', False)]
c['front'] += eye(35, 77, 7.6, 6.2, s=1, pup=(0.6, 0.4, 2.4), iris=_c('#3c5552')) + eye(65, 77, 7.6, 6.2, s=-1, pup=(0.6, 0.4, 2.4), iris=_c('#3c5552'))
nose['s'] = ell(50, 86, 3.4, 3.0)
c['front'] += [nose] + big_grin(94, 19, 12)
c['side'] += [L(blob([(70, 72), (86, 70), (86, 82), (70, 82)], 4), BLACK, 'f', False)] + side_eye(77, 5.2, 4.6, pup=(2.0, 0.4, 2.0), iris=_c('#3c5552'))
c['side'] += side_grin(94, 10) + [L(ell(86, 86, 2.6, 2.4), _c('#e86a4a'), 'f', True)]
c['face']['eyes'] = 'none'
put('fred-punch', c)

# Sherlock Sagers: la sonrisa es enorme, de dientes, casi de lado a lado de la cara (no una boquita)
c = take('sherlock-sagers')
c['face']['mouth'] = 'none'
c['front'] += big_grin(95, 17, 11) + [L([(50, 80), (52, 89), (48, 90)], _c('#8a5a30'), 'f', False, False, 1.4)]
c['side'] += side_grin(97, 10)
put('sherlock-sagers', c)

# Neil Seating: bajo el flequillo de tazón asoman unos ojos grandes y blancos de pupila negra, con el párpado recto de ceño
c = take('neil-seating')
c['face']['eyes'] = 'none'
c['front'] += eyes2(77, 15, rx=7.6, ry=6.6, pup=(2.2, 1.4, 2.6), lid=0.18, tilt=0.18)
c['side'] += side_eye(77, 5.0, 5.4, pup=(2.0, 1.2, 2.2), lid=0.18)
put('neil-seating', c)

# Ollie Tuckney: ojos entornados (rendijas blancas con la pupila oscura), con una marca morada cuadrada en el lagrimal y
# una raya morada en diagonal en cada mejilla; sin cejas moradas
c = take('ollie-tuckney')
PM = c['front'][-1]['c']
c['front'] = [l for l in c['front'] if l['c'] != PM]
c['face']['eyes'] = 'none'
c['front'] += eyes2(76, 15, rx=8.0, ry=4.2, pup=(1.4, 0.6, 2.2), lid=0.3, tilt=-0.06, hi=False)
c['front'] += [L(blob([(42, 72), (46, 72), (46, 79), (42, 79)], 2), PM, 'f', False), L(blob([(54, 72), (58, 72), (58, 79), (54, 79)], 2), PM, 'f', False),
               L(blob([(22, 84), (26, 83), (32, 94), (28, 95)], 2), PM, 'f', False), L(blob([(78, 84), (74, 83), (68, 94), (72, 95)], 2), PM, 'f', False)]
c['side'] += side_eye(76, 5.0, 3.0, pup=(1.6, 0.4, 1.8), lid=0.3) + [L(blob([(78, 86), (83, 85), (88, 95), (84, 97)], 2), PM, 'f', False)]
put('ollie-tuckney', c)

# Serena Besse: ojos grandes de anime con el iris granate, no unos puntitos
c = take('serena-besse')
c['face']['eyes'] = 'big'
put('serena-besse', c)

# Andy Fudge: colmillos grandes que salen de la mandíbula hacia arriba en las comisuras, boca ancha en ceño y ojos blancos
# pequeños metidos en un contorno negro muy grueso
c = take('andy-fudge')
c['front'] = [l for l in c['front'] if l['c'] != TW and not (l['w'] and l['c'] != OUTC and l['s'][0] == (30, 104))]
c['face']['mouth'] = 'none'
c['face']['eyes'] = 'none'
c['front'] += [L(blob([(22, 74), (36, 68), (48, 76), (40, 82), (26, 82)], 4), BLACK, 'f', False),
               L(blob([(78, 74), (64, 68), (52, 76), (60, 82), (74, 82)], 4), BLACK, 'f', False)]
c['front'] += eye(36, 76, 4.6, 3.6, s=1, pup=(0.4, 0.2, 1.8)) + eye(64, 76, 4.6, 3.6, s=-1, pup=(0.4, 0.2, 1.8))
c['front'] += [L(quad((32, 100), (50, 93), (68, 100)), OUTC, 'f', False, False, 2.2),
               L([(27, 104), (30, 88), (40, 100)], WHITE, 'f', True), L([(73, 104), (70, 88), (60, 100)], WHITE, 'f', True)]
c['side'] = [l for l in c['side'] if l['c'] != TW] + [L([(76, 104), (80, 88), (87, 100)], WHITE, 'f', True)]
put('andy-fudge', c)

# Travis Borer: los ojos no se ven: las gafas redondas son cristales claros y brillantes; encima, cejas de preocupación
c = take('travis-borer')
c['face']['eyes'] = 'none'
c['face']['brows'] = False
LENS = _c('#e4d4bc')
for cx, s in ((36, 1), (64, -1)):
    c['front'].append(L(ell(cx, 76, 8.0, 7.0), LENS, 'f', False))
    c['front'].append(L([(cx - 4, 79), (cx + 1, 72)], WHITE, 'f', False, False, 1.4))
    c['front'].append(L([(cx + 1, 80), (cx + 4, 76)], WHITE, 'f', False, False, 1.2))
    c['front'].append(L(quad((cx - 7 * s, 64), (cx - 1 * s, 63), (cx + 6 * s, 60)), OUTC, 'f', False, False, 1.8))
c['side'] += [L(ell(80, 76, 5.4, 6.4), LENS, 'f', False), L(quad((74, 64), (79, 62), (85, 60)), OUTC, 'f', False, False, 1.8)]
put('travis-borer', c)

# Tim Pression: ojos blancos y redondos con la pupila abajo y el párpado recto de ceño
c = take('tim-pression')
c['face']['eyes'] = 'none'
c['front'] += eyes2(78, 14, rx=6.4, ry=6.0, pup=(0.6, 1.8, 2.6), lid=0.22, tilt=0.16)
c['side'] += side_eye(78, 4.6, 5.0, pup=(1.6, 1.6, 2.2), lid=0.22)
put('tim-pression', c)

# Reg Strimmer: nariz en rombo y boca abierta enorme de sonrisa con los dientes de arriba
c = take('reg-strimmer')
c['face']['mouth'] = 'none'
for l in c['front']:
    if l['s'] and tuple(l['s'][0]) == (44, 80):
        l['s'] = blob([(43, 81), (50, 74), (57, 81), (50, 89)], 2)
c['front'] += big_grin(93, 19, 12)
c['side'] += side_grin(94, 10)
put('reg-strimmer', c)

# Elias Lens: la sonrisa de dientes es enorme, de lado a lado
c = take('elias-lens')
c['front'] = c['front'][:-6] + big_grin(94, 18, 11)
c['side'] += side_grin(95, 9)
put('elias-lens', c)

# Chip Spacek: boca grande abierta en ceño (granate por fuera y naranja dentro), no un bigotito
c = take('chip-spacek')
c['front'][-1] = L(blob([(30, 98), (38, 88), (50, 85), (62, 88), (70, 98), (64, 99), (50, 93), (36, 99)], 5), _c('#7a3a20'), 'f', True)
c['front'].append(L(blob([(36, 96), (42, 91), (50, 89), (58, 91), (64, 96), (50, 94)], 4), _c('#d8702c'), 'f', False))
put('chip-spacek', c)

# Blake Nailor: la boca son unos labios gruesos rosados en ceño, no una fila de dientes
c = take('blake-nailor')
c['front'] = c['front'][:-2] + [L(blob([(36, 101), (42, 96), (50, 95), (58, 96), (64, 101), (60, 106), (50, 107), (40, 106)], 5), _c('#e8a294'), 'f', True),
                                L(quad((38, 101), (50, 98), (62, 101)), OUTC, 'f', False, False, 1.2)]
put('blake-nailor', c)

# Lou Daguerre: ojos altos y ovalados con la pupila arriba hacia la nariz y el párpado naranja; coloretes naranjas dentro
# de las mejillas
c = take('lou-daguerre')
OC = (240, 150, 90, 255)
c['front'] = [l for l in c['front'] if not (l['z'] == 'f' and l['c'] in (TW, 'skin', OC) or l['c'] == OUTC and l['w'] == 2.2
                                           or l['c'] == (28, 22, 26, 255))]
LIDC = _c('#e8904a')
for cx, s in ((36, 1), (64, -1)):
    o = ell(cx, 77, 6.6, 9.0, 40)
    c['front'] += [L(o, WHITE, 'f', False), L(ell(cx + 2.2 * s, 73.5, 2.6, 2.8), BLACK, 'f', False),
                   L([(x, y) for x, y in o if y <= 72] + [(cx + 6.6, 72)], LIDC, 'f', False), L(o + [o[0]], OUTC, 'f', False, False, 1.4),
                   L(quad((cx - 6.4, 72), (cx, 73.4), (cx + 6.4, 72)), OUTC, 'f', False, False, 1.2)]
c['front'] += [L(ell(32, 88, 3.4, 4.4), OC, 'f', False), L(ell(68, 88, 3.4, 4.4), OC, 'f', False)]
put('lou-daguerre', c)

# Ojos grandes, blancos y redondos con la pupila negra (en el retrato se les ven así, no como puntitos)
for pid, ey, sep, rx, ry, pup, lid, tilt in (('gem-shorn', 76, 15, 6.4, 6.6, (0.2, 0.6, 3.0), None, 0.0),
                                             ('beau-hammock', 76, 15, 7.0, 7.4, (0.0, 0.4, 2.6), None, 0.0),
                                             ('claire-taker', 76, 15, 7.0, 6.6, (0.4, 1.0, 3.0), None, 0.0),
                                             ('beat-scatton', 77, 15, 6.8, 6.6, (1.0, 0.6, 2.4), 0.12, 0.14),
                                             ('carey-filling', 77, 14, 6.6, 5.4, (0.6, 0.8, 2.4), 0.32, -0.04),
                                             ('john-bleach', 77, 15, 7.0, 6.0, (1.2, 0.8, 2.4), 0.16, 0.2)):
    c = take(pid)
    ey = c['face'].get('eye_y', ey)
    c['face']['eyes'] = 'none'
    c['front'] += eyes2(ey, sep, rx=rx, ry=ry, pup=pup, lid=lid, tilt=tilt)
    c['side'] += side_eye(ey, rx * 0.7, ry * 0.8, pup=(1.6, pup[1], pup[2] * 0.8), lid=lid)
    if pid == 'carey-filling':  # sus cejas de ceño quedan encima del párpado recto
        c['front'] = [l for l in c['front'] if not (l['w'] == 3.0 and l['c'] == OUTC)]
        c['front'] += [L([(24, 67), (42, 69)], OUTC, 'f', False, False, 2.6), L([(58, 69), (76, 67)], OUTC, 'f', False, False, 2.6)]
    put(pid, c)

# Odessa Ryder y Remy Diggun: ojos grandes de anime (Odessa casi negros, Remy azules), no puntitos
for pid in ('odessa-ryder', 'remy-diggun'):
    c = take(pid)
    c['face']['eyes'] = 'big'
    put(pid, c)


# ------------------------------------------------------------------ tono de piel (revisión con el retrato)
# Piel medida en el retrato de Victory Road (mejillas y barbilla, tono iluminado más frecuente): varios dibujos tenían la
# piel rosada/pálida donde el retrato es anaranjado/tostado (o al revés). Se cambia skin (skin_d = 0,86) y las capas de
# color fijo que repetían la piel antigua. Se dejan sin tocar máscaras, cascos y caras pintadas. El tono del pelo ya
# coincidía con el retrato en todos.
from chars import hexc as _sk_hex, tone as _sk_tone  # noqa: E402


def _sk_near(a, b, tol=6):
    return isinstance(a, tuple) and len(a) >= 3 and all(isinstance(x, int) for x in a[:3]) and \
        sum(abs(a[i] - b[i]) for i in range(3)) <= tol


def _sk_reskin(key, h):
    c = copy.deepcopy(CHARS[key])
    p = c['pal']
    old, old_d = p['skin'], p['skin_d']
    p['skin'] = _sk_hex(h)
    p['skin_d'] = _sk_tone(p['skin'], 0.86)
    subs = [(old, p['skin']), (old_d, p['skin_d'])]

    def fix(v):
        for o, n in subs:
            if _sk_near(v, o):
                return n
        return v
    for view in ('front', 'side', 'back'):
        for item in c.get(view, []):
            for l in (item if isinstance(item, list) else [item]):
                if isinstance(l, dict) and 'c' in l:
                    l['c'] = fix(l['c'])
    for k, v in list(c.get('face', {}).items()):
        if isinstance(v, tuple) and len(v) == 4 and all(isinstance(x, int) for x in v):
            c['face'][k] = fix(v)
    CHARS[key] = c


_SKIN2 = {
    'yve-dunbar': '#b7723a',
    'jess-winkles': '#f8be93',
    'tom-skipper': '#eda45f',
    'robyn-weaver': '#fecf9e',
    'kate-later': '#b08c73',
    'in-chikita': '#fec270',
    'bob-daruma': '#f6bf92',
    'jon-izumo': '#fdeab8',
    'junior-gambit': '#e3ccad',
    'katy-punter': '#fec270',
    'vanity-percy': '#e4ccad',
    'sherlock-sagers': '#dda356',
    'hide-king': '#f6b57c',
    'ed-hartsell': '#dfa259',
    'sonny-cinders': '#fbbc7b',
    'elata-mighty': '#fbbc7a',
    'tim-pression': '#af8c72',
    'floyd-spades': '#fec270',
    'john-bleach': '#fbbc7c',
    'clay-turnor': '#fbbc7b',
    'justin-cush': '#cf986a',
    'ethan-swallow': '#fabd7c',
    'clark-tappen': '#fdc370',
    'harry-keenan': '#e4ccad',
    'simeon-squareyes': '#f5be92',
    'stuart-leafe': '#fec26f',
    'edward-baron': '#fbbc7b',
    'stu-hoofer': '#fbbc7b',
    'griff-hardcasel': '#e4ccac',
    'joe-divide': '#fec270',
    'verity-soliz': '#b7733b',
    'erica-hogland': '#fabc7a',
    'tim-opener': '#fdc372',
    'kath-leaflin': '#fbbc7a',
    'jay-asher': '#fec270',
    'james-hearson': '#ce966a',
    'fen-skates': '#f7be93',
    'guy-pinnay': '#fbbc7a',
    'garry-planer': '#fec270',
    'herbie-garnet': '#fed09f',
    'fawn-blossom': '#fcbc7b',
    'elinor-maven': '#fbbb7b',
    'ant-anomy': '#fcbc7c',
    'harry-angue': '#fbbc7a',
    'terry-dryden': '#cf9567',
    'jerry-bateman': '#fdc270',
}
for _p, _h in _SKIN2.items():
    _sk_reskin('scouts-ie2:' + _p, _h)
