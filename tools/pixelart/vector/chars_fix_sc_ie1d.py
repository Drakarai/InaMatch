"""Correcciones de la revisión de diseños (grupo sc_ie1d): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS, L, OUTC, blob, ell, hexc, messy, outline, strand, tone  # noqa: F401
from heads import FACE_FRONT, OUT, quad  # noqa: F401


def K(pid):
    return f'scouts-ie1:{pid}'


def get(pid):
    return copy.deepcopy(CHARS[K(pid)])


def put(pid, c):
    CHARS[K(pid)] = c


def skin(c, h):
    """Cambia la piel (y su sombra) de una ficha."""
    s = hexc(h)
    c['pal']['skin'], c['pal']['skin_d'] = s, tone(s, 0.86)


def lids(view, ey=75, sep=14, drop=1.5):
    """Párpados caídos (ojos entornados, de sueño o de cansancio): tapa con piel la mitad de arriba del ojo y traza el
    borde del párpado. drop = hasta dónde baja el párpado respecto al centro del ojo."""
    out = []
    xs = ((50 - sep, 7.2), (50 + sep, 7.2)) if view == 'front' else ((81.5, 5.6),) if view == 'side' else ()
    for cx, hw in xs:
        out.append(L([(cx - hw, ey - 8.2), (cx + hw, ey - 8.2), (cx + hw, ey + drop - 1.6), (cx - hw, ey + drop)], 'skin', 'f', False))
        out.append(L(quad((cx - hw + 0.6, ey + drop + 0.6), (cx, ey + drop - 1.4), (cx + hw - 0.6, ey + drop + 0.4)), OUT, 'f', False, False, 2.2))
    return out


# ------------------------------------------------------------------ Shawn Broker: ojos entornados de sueño con ojeras,
# pelo morado con las puntas de los lados vueltas hacia fuera
c = get('shawn-broker')
c['face']['eyes'] = 'round'
c['face']['brows'] = 'angry'
c['front'] += lids('front', drop=0.5) + [L(quad((33, 82), (36, 84.5), (41, 82)), tone(c['pal']['skin'], 0.7), 'f', False, False, 1.2),
                                      L(quad((59, 82), (64, 84.5), (67, 82)), tone(c['pal']['skin'], 0.7), 'f', False, False, 1.2)]
c['front'] = [L(outline([(16, 74), (4, 80), (-8, 74, 1), (4, 68), (12, 56)])), L(outline([(84, 74), (96, 80), (106, 72, 1), (94, 66), (88, 56)])),
              L(outline([(16, 46), (2, 50), (-4, 62, 1), (4, 46), (18, 30)]))] + c['front']
put('shawn-broker', c)

# Brook Atwater: frente despejada y alta con el pico del pelo bajando en V hasta el entrecejo (no un flequillo)
c = get('brook-atwater')
c['face']['face_front'] = quad((19, 52), (17, 92), (50, 100)) + quad((50, 100), (83, 92), (81, 52))[1:] + quad((81, 52), (50, 4), (19, 52))[1:-1]
c['face']['hairline'] = [(12, 112), (20, 112), (20, 40), (28, 30), (40, 28), (47, 40), (50, 54), (53, 40), (60, 28), (72, 30), (80, 40), (80, 112), (88, 112)]
c['front'] = [l for l in c['front'] if l.get('w', 0) == 0 or l['c'] != 'deep']
c['front'] += [strand([(44, 30), (36, 10)], 'deep', 'b', 1.0), strand([(56, 30), (64, 10)], 'deep', 'b', 1.0)]
put('brook-atwater', c)

# Dick Turbin: raya en medio con la frente a la vista y el pelo apartado a los lados
c = get('dick-turbin')
c['face']['hairline'] = [(16, 70), (18, 52), (28, 42), (42, 36), (50, 42), (58, 36), (72, 42), (82, 52), (84, 70)]
c['front'] = [l for l in c['front'] if not l.get('w')] + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.2), strand([(48, 10), (34, 22), (22, 46)], 'deep', 'b', 1.0),
                                                         strand([(52, 10), (66, 22), (78, 46)], 'deep', 'b', 1.0)]
put('dick-turbin', c)

# Paddy Prunus: piel clara (no morena) y ojos entornados
c = get('paddy-prunus')
skin(c, '#f8cca2')
c['face']['eyes'] = 'round'
c['front'] += lids('front', drop=0)
put('paddy-prunus', c)

# Sonny Welkin: de perfil también se le ve el cuerno de pelo del lado que da a la cámara
c = get('sonny-welkin')
c['side'] += [L(outline([(34, 46), (24, 30), (22, 8), (30, -14, 1), (34, 8), (44, 24), (52, 36)])),
              L(outline([(30, -10), (34, 8), (44, 24), (48, 34), (38, 26)]), 'shade', 'b', False)]
put('sonny-welkin', c)

# Reagan Boneman: el pelo es gris lavanda, no azul
c = get('reagan-boneman')
for k, f in (('mid', 1.0), ('shade', 0.8), ('deep', 0.62)):
    c['pal'][k] = tone(hexc('#8e86a6'), f)
c['pal']['light'] = (190, 184, 206, 255)
put('reagan-boneman', c)

# Gary Osoto: ojos con el iris azul claro
c = get('gary-osoto')
c['face']['eyes'] = 'normal'
c['pal']['iris'] = hexc('#8cb4d4')
put('gary-osoto', c)

# Den Taligene: nariz grande y redonda
c = get('den-taligene')
c['face']['nose'] = (50, 84, 5.4)
c['pal']['nose'] = tone(c['pal']['skin'], 1.04)
put('den-taligene', c)

# Bill Yards, Cal Cooler: piel tostada
for pid, h in (('bill-yards', '#eeb27a'), ('cal-cooler', '#e8ae76')):
    c = get(pid)
    skin(c, h)
    put(pid, c)

# Bamber Shoot, Mat Char: ojos caídos entornados
for pid, drop in (('bamber-shoot', 0.5), ('mat-char', 0.5)):
    c = get(pid)
    if c['face'].get('eyes') == 'dot':
        c['face']['eyes'] = 'round'
    ey = c['face'].get('eye_y', 75)
    c['front'] += lids('front', ey=ey, drop=drop)
    put(pid, c)

# Les Knightley: es pelo (no un gorro): flequillo de puntas sobre la frente y moño de mechones en punta en lo alto
c = get('les-knightley')
TUFT = [(44, 12), (40, -2), (44, -14, 1), (50, -6), (56, -18, 1), (60, -4), (64, 2, 1), (58, 12)]
c['front'] = [l for l in c['front'] if not (len(l['s']) == 36 and abs(l['s'][0][1] - 4) < 10)]
c['front'] += [L(outline(TUFT)), strand([(50, 10), (52, -6)], 'shade', 'b', 1.0),
               L(outline([(14, 64), (16, 40), (28, 24), (50, 18), (72, 24), (84, 40), (86, 64), (78, 52), (72, 60, 1), (66, 48), (58, 58, 1), (52, 46),
                          (44, 58, 1), (38, 46), (30, 58, 1), (24, 50)]), 'mid', 'f'),
               strand([(36, 26), (32, 46)], 'shade', 'f', 1.0), strand([(64, 26), (68, 46)], 'shade', 'f', 1.0)]
c['side'] = [l for l in c['side'] if not (len(l['s']) == 36)] + [L(outline([(t[0] - 4, t[1]) + t[2:] for t in TUFT])),
                                                               L(outline([(62, 40), (76, 26), (88, 34), (90, 56, 1), (82, 48), (76, 58, 1), (70, 46)]), 'mid', 'f')]
c['back'] = [l for l in c['back'] if not (len(l['s']) == 36)] + [L(outline(TUFT), 'mid', 'f'),
                                                               L(outline([(16, 76), (24, 86, 1), (34, 80), (42, 90, 1), (50, 82), (58, 90, 1), (66, 80), (76, 86, 1), (84, 76), (50, 70)]))]
c['face']['hairline'] = False
put('les-knightley', c)

# Ashley Fay: el ojo que se ve lleva una cruz blanca en la pupila
c = get('ashley-fay')
W = (250, 250, 250, 255)
c['front'] += [L([(64, 71.5), (64, 79)], W, 'f', False, False, 1.1), L([(60.6, 75.5), (67.4, 75.5)], W, 'f', False, False, 1.1)]
put('ashley-fay', c)

# Arthur Dox: cejas muy gruesas azul marino
c = get('arthur-dox')
NAVY = (36, 52, 84, 255)
c['front'] += [L(outline([(26, 66), (34, 61), (44, 63), (44, 68), (34, 67), (27, 70)]), NAVY, 'f', False, True),
               L(outline([(74, 66), (66, 61), (56, 63), (56, 68), (66, 67), (73, 70)]), NAVY, 'f', False, True)]
c['side'] += [L(outline([(70, 64), (78, 61), (86, 63), (86, 68), (78, 67), (71, 69)]), NAVY, 'f', False, True)]
put('arthur-dox', c)

# Irv Washinton: el pelo naranja muy corto le bordea toda la bóveda de la cabeza (hasta las sienes), con la cresta en lo alto
c = get('irv-washinton')
c['front'] += [L(outline([(4, 54), (8, 34), (26, 16), (50, 10), (74, 16), (92, 34), (96, 54), (90, 50), (76, 32), (50, 24), (24, 32), (10, 50)]), 'mid', 'f', ln=True)]
c['side'] += [L(outline([(14, 60), (16, 32), (34, 12), (54, 8), (72, 16), (74, 24), (56, 18), (36, 22), (24, 38), (22, 60)]), 'mid', 'f', ln=True)]
c['back'] += [L(outline([(10, 62), (12, 34), (28, 14), (50, 6), (72, 14), (88, 34), (90, 62), (80, 46), (66, 30), (50, 26), (34, 30), (20, 46)]), 'mid', 'f', ln=True)]
put('irv-washinton', c)

# Caz Yewell: la franja de pelo azul grisáceo es más ancha (ocupa casi toda la coronilla) y baja en punta hacia la frente
c = get('caz-yewell')
c['front'] = [c['front'][0], L(outline([(24, 26), (34, 10), (50, 4), (66, 8), (78, 22), (80, 34), (70, 36), (60, 40), (54, 54, 1), (46, 40), (34, 34)]), 'mid', 'b'),
              L(outline([(56, 6), (68, 10), (78, 22), (80, 34), (66, 30), (60, 18)]), 'shade', 'b', False)] + c['front'][3:]
c['side'] = [L(outline([(86, 48), (88, 30), (78, 12), (58, 4), (36, 8), (20, 20), (18, 34), (40, 26), (62, 28), (78, 38)]), 'mid', 'b')] + c['side'][1:]
c['back'] = [L(outline([(28, 30), (32, 12), (50, 6), (68, 12), (72, 30), (60, 46), (40, 46)]), 'mid', 'b')] + c['back'][1:]
put('caz-yewell', c)

# Madison Cabinet: casco de balón: hexágonos blancos (uno grande en el centro de la frente y otros a los lados, arriba) entre
# pentágonos rojos, con las costuras marcadas
c = get('madison-cabinet')
c['pal']['patch'] = (246, 242, 232, 255)
SEAM = (120, 26, 22, 255)


def hexa(pts):
    return L(outline([p + (1,) for p in pts]), 'patch', 'f', False, True)


def seams(segs):
    return [L(list(s), SEAM, 'f', False, False, 1.3) for s in segs]


helm = [l for l in c['front'] if l['c'] == 'helm']
rim = [l for l in c['front'] if l['c'] == 'rim']
c['front'] = helm + [hexa([(36, 28), (64, 28), (72, 42), (64, 55), (36, 55), (28, 42)]),
                     hexa([(10, 22), (22, 12), (30, 18), (28, 34), (16, 40), (8, 34)]),
                     hexa([(90, 22), (78, 12), (70, 18), (72, 34), (84, 40), (92, 34)])] + seams(
    [((36, 28), (30, 18)), ((64, 28), (70, 18)), ((30, 18), (40, 4)), ((70, 18), (60, 4)), ((28, 42), (16, 40)), ((72, 42), (84, 40)),
     ((22, 12), (30, 4))]) + rim
helm = [l for l in c['side'] if l['c'] == 'helm']
rim = [l for l in c['side'] if l['c'] == 'rim']
c['side'] = helm + [hexa([(64, 26), (84, 24), (92, 38), (86, 52), (66, 54), (58, 40)]),
                    hexa([(30, 8), (50, 6), (58, 20), (50, 32), (32, 32), (24, 20)]),
                    hexa([(4, 36), (14, 34), (22, 46), (16, 58), (4, 58)])] + seams(
    [((58, 40), (50, 32)), ((64, 26), (58, 20)), ((24, 20), (14, 34)), ((22, 46), (40, 46)), ((40, 46), (58, 40)), ((40, 46), (32, 32))]) + rim
helm = [l for l in c['back'] if l['c'] == 'helm']
rim = [l for l in c['back'] if l['c'] == 'rim']
c['back'] = helm + [hexa([(38, 6), (62, 6), (68, 20), (60, 32), (40, 32), (32, 20)]),
                    hexa([(8, 40), (20, 34), (30, 46), (26, 62), (10, 62)]), hexa([(92, 40), (80, 34), (70, 46), (74, 62), (90, 62)])] + seams(
    [((40, 32), (30, 46)), ((60, 32), (70, 46)), ((30, 46), (50, 58)), ((70, 46), (50, 58)), ((50, 58), (50, 70)), ((32, 20), (20, 34)),
     ((68, 20), (80, 34))]) + rim
put('madison-cabinet', c)

# Derek Longhand, Kevin Boardman: nariz larga (tabique marcado desde el entrecejo)
for pid, nz, top in (('derek-longhand', (50, 89, 6.6), 70), ('kevin-boardman', (50, 87, 4.2), 74)):
    c = get(pid)
    c['face']['nose'] = nz
    nx, ny, nr = nz
    c['front'] += [L(quad((nx - 2, top), (nx - 3.5, ny - 8), (nx - nr * 0.9, ny - 1)), OUTC, 'f', False, False, 1.3),
                   L(quad((nx + 2, top + 2), (nx + 3, ny - 8), (nx + nr * 0.7, ny - 3)), tone(c['pal']['skin'], 0.8), 'f', False, False, 1.0)]
    c['face']['nose_side'] = (88, ny - 1, nr * 0.7)
    put(pid, c)

# Derek Longhand: la nariz es enorme y larga, desde el entrecejo hasta casi la boca
c = get('derek-longhand')
c['face'].pop('nose', None)
c['front'] = [l for l in c['front'] if not (l['w'] and l['c'] in (OUTC,) and len(l['s']) == 21 and l['s'][0][1] == 70)]
c['front'] += [L(blob([(48.6, 73), (51.4, 73), (54, 80), (57, 85), (54.5, 89), (50, 90), (45.5, 89), (43, 85), (46, 80)], 8), tone(c['pal']['skin'], 0.93), 'f', False, True),
               L(ell(47, 87.6, 1.0, 0.8), OUTC, 'f', False), L(ell(53, 87.6, 1.0, 0.8), OUTC, 'f', False),
               L(quad((39, 94), (50, 97.5), (61, 94)), OUTC, 'f', False, False, 1.4)]
c['face']['mouth'] = 'none'
c['face']['nose_side'] = (89, 87, 4.4)
put('derek-longhand', c)


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
    'shawn-broker': '#f3b46e',
    'brook-atwater': '#f0b56d',
    'gaston-berry': '#f0b46d',
    'jack-frosty': '#f1b36a',
    'reagan-boneman': '#f1b56d',
    'conan-fox': '#c69858',
    'paddy-streehan': '#ce924b',
    'fingus-inky': '#f9b46c',
    'thomas-ediston': '#ce924b',
    'cam-lensman': '#f1b46d',
    'harry-harper': '#f1b46e',
    'vin-fleetwood': '#f1b46d',
    'billy-blanc': '#f1b56d',
    'chris-massey': '#f9b169',
    'mat-char': '#a88666',
    'willow-withers': '#fab16b',
    'chris-talise': '#f1b46d',
    'phil-rosey': '#c6995a',
    'max-scara': '#e4d4ba',
    'les-belisha': '#f1b46f',
    'philip-prince': '#f3b46d',
    'randolf-finn': '#f1b56d',
    'chuck-hardy': '#f1b46d',
    'nat-picker': '#f1b46e',
    'pat-maclean': '#f1b56e',
    'sim-pathy': '#f1b46d',
    'teller-scoap': '#f1b56e',
    'benedict-eggers': '#f1b56e',
    'patsy-cornish': '#f1b56d',
    'stu-venier': '#f1b56d',
    'rab-acus': '#f1b46d',
    'jon-quill': '#f1b46d',
    'butch-pythons': '#f1b46d',
    'bud-dahman': '#cd914a',
    'manuel-gere': '#fad69f',
    'rolly-kerr': '#ce914a',
    'buster-clout': '#f1b46d',
    'tim-eisback': '#f1b46e',
    'horty-courture': '#c7995b',
    'monty-hillary': '#f1b46d',
    'jak-hammer-hammerslam': '#f1b46c',
    'biron-pendexter': '#f1b56e',
    'christian-dear': '#f1b36a',
    'sage-wisdom': '#f3b472',
    'grant-slammer': '#ce914b',
    'harvey-lifter': '#c6985a',
    'onslow-ball': '#f9d69d',
    'theo-bernoulli': '#ce9149',
    'nigel-bramel': '#f1b46c',
    'bo-luger': '#ca965c',
    'larry-helps': '#f1b46d',
    'oscar-petty': '#fad69c',
    'scot-enguard': '#f1b46d',
    'bill-dozer': '#f1b46c',
    'ollie-twister': '#f1b46d',
    'mark-perfect': '#f0b46d',
    'jack-trumper': '#fee7b2',
    'tel-egram': '#f1b569',
    'paul-pitcher': '#f0b46b',
    'grant-mardy': '#f1b56e',
    'manny-carbs': '#f1b46d',
    'todd-tempole': '#d0914b',
    'nick-templeton': '#f1b46d',
    'joe-rassock': '#f0b46d',
    'patrick-edie': '#f1b56d',
    'carl-penter': '#cd924b',
    'gill-o-mend': '#f1b76d',
    'julius-vernon': '#f5b36c',
    'tim-piece': '#f1b46e',
    'waite-forrit': '#f1b46d',
    'telly-fonbocks': '#f1b46c',
    'caz-yewell': '#f1b46d',
    'nobby-shinn': '#f0b46d',
    'vance-bookings': '#f1b56e',
    'ben-evolent': '#c5995b',
    'nick-savers': '#f1b46c',
    'theo-broma': '#cd924a',
    'ty-priter': '#f0b46d',
    'jig-charley-charleston': '#f1b56d',
    'butler-chambers': '#f0b56e',
    'ronny-knowles': '#f0b46d',
    'hank-shortman': '#ca944c',
    'sean-trawler': '#ce914a',
    'fry-vollity': '#efb472',
    'horace-coop': '#f1b56d',
    'ike-banner': '#f1b471',
    'gauge-diven': '#cd924b',
    'ken-sewer': '#f9d79f',
    'phil-fog': '#a88564',
    'madison-cabinet': '#f9d69d',
    'jon-driedon': '#f1b46c',
    'paddy-prunus': '#f1b774',
    'innes-caving': '#f2b974',
    'ray-whitehead': '#a88666',
    'josh-rogan': '#ce924b',
    'rod-opsin': '#a88566',
    'rupert-spiers': '#f0b46c',
    'reg-thrift': '#f0b56e',
    'gary-osoto': '#f2b56e',
    'kit-chapman': '#ce924b',
    'bill-teller': '#f1b46d',
    'francis-paine': '#f3b46e',
    'bob-lioteck': '#ce924a',
    'bill-aegis': '#f0b46d',
    'lee-dorr': '#fcd59c',
    'sul-tarner': '#f0b566',
    'jim-nastick': '#f1b46e',
    'brent-cross': '#f1b471',
    'hal-leeward': '#f1b56e',
    'miles-seaford': '#f0b56e',
    'ray-menn': '#ca904b',
    'carter-nightly': '#f1b46d',
    'bobby-yeller-yellow': '#f1b46d',
    'les-knightley': '#ce924b',
}
_HAIR = {
    'vin-fleetwood': '#7aa6ab',
    'caz-yewell': '#68939a',
    'fingus-inky': '#48596a',
    'guy-dance': '#bf6a67',
    'grant-slammer': '#a2767e',
}
for _p, _h in _SKIN.items():
    _reskin(_p, _h)
for _p, _h in _HAIR.items():
    _rehair(_p, _h)
