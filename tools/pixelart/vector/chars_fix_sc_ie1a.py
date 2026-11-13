"""Correcciones de la revisión de diseños (grupo sc_ie1a): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, blob, ell, outline, hexc, tone, mix  # noqa: E402,F401
from heads import quad  # noqa: E402,F401

K = 'scouts-ie1:'


def _fx(pid):
    """Copia del dibujo actual del ojeador para corregirla (con su misma clave)."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):  # capas en una lista plana, para poder quitar y cambiar
        c[v] = [x for it in c[v] for x in (it if isinstance(it, list) else [it])]
    CHARS[K + pid] = c
    return c


def _hair(c, mid, shade=None, deep=None, light=None):
    """Color del pelo sacado del retrato (y sus sombras: las del retrato o las de pal())."""
    h = hexc(mid)
    p = c['pal']
    p['mid'] = h
    p['shade'] = hexc(shade) if shade else tone(h, 0.78)
    p['deep'] = hexc(deep) if deep else tone(h, 0.6)
    p['light'] = hexc(light) if light else mix(h, (255, 255, 255), 0.38)


# ------------------------------------------------------------------ colores del pelo medidos en el retrato
# (el dibujo tenía bien la forma, pero el tono se iba: más gris, más saturado, más claro o de otro matiz)
for _pid, _cols in {
    'tim-toppel': ('#a88382', '#845654', '#5e3a38', '#c8a8a4'),        # castaño rosado, no gris lila
    'paul-downs': ('#6e454c', '#55323a', '#3a2224'),                   # granate apagado, no vino
    'herb-ivore': ('#7d7081', '#5e5262', '#463a44'),                   # gris malva, no azul marino
    'manny-steele': ('#bb776a', '#8f5a50', '#6e443c'),                 # rapado castaño rojizo, no rosa
    'ike-flinger-doerflinger': ('#d1cca9', '#b0aa88', '#8f7d65', '#eae7d3'),  # crema caqui, no blanco grisáceo
    'chops-denton': ('#b63208', '#882406', '#6d220a'),
    'harley-trotter': ('#52955e', '#3f6440', '#2f4a30'),
    'griff-strummer': ('#7e480b', '#603213', '#43240f'),
    'florian-selles': ('#713c05', '#5a300a', '#49230b'),
    'boe-tyer': ('#a94109', '#7e300a', '#61260d'),
    'rocky-rollans': ('#a94009', '#8a340c', '#552411'),
    'samuel-peeps': ('#9b4214', '#873712', '#532613'),
    'troy-glodight': ('#9c2609', '#7a1e0a', '#4e190e'),
    'rory-polisher': ('#c66e68', '#a85a52', '#7e4038'),
    'cash-barganier': ('#c16959', '#9a4f44', '#733627'),
    'bob-whittle': ('#a8380c', '#7c2407', '#5a1c06'),
    'chris-hypogee': ('#6f6e2e', '#555324', '#4c401c'),
    'hiroshi-dot': ('#466e69', '#355550', '#2b3d38'),
    'jen-quibble': ('#d0ccaa', '#b4ae8e', '#8e6b48'),
    'nathin-gaunt': ('#938a6b', '#7e745c', '#5e5644'),
    'mark-tinney': ('#948a6c', '#796c54', '#5a5040'),
    'percy-wrench': ('#485a6a', '#364452', '#2a3038'),
    'garland-gathers': ('#485a6a', '#3c4a58', '#2b2c30'),
    'rob-ottley': ('#689399', '#50666a', '#3c4446'),
    'pete-grimes': ('#5d887f', '#4f7069', '#3a4a44'),
    'saul-dowd': ('#769344', '#585c2d', '#47371d'),
    'biff-beeston': ('#cb7e37', '#a8682c', '#794b23'),
    'knight-reader': ('#364f66', '#283a4c', '#1e2023'),
    'luke-raffles': ('#6e4650', '#573638', '#462623'),
    'charlie-krelborn': ('#9e7a6c', '#7d5a50', '#54362a'),
    'grover-bearing': ('#da7815', '#b06010', '#814e22'),
}.items():
    _hair(_fx(_pid), *_cols)

CHARS[K + 'herb-ivore']['pal']['brow'] = hexc('#6e6072')            # cejas del mismo gris malva que el pelo
CHARS[K + 'bob-whittle']['pal'].update(helm=hexc('#766d47'), helm_d=hexc('#524734'))  # casco caqui, no verde
CHARS[K + 'cash-barganier']['pal']['mask_o'] = hexc('#cb6743')

# Andy Roff: cejas gruesas casi negras (verde oliva muy oscuro), no del color claro del pelo
_c = CHARS[K + 'andy-roff'] = _fx('andy-roff')
_c['pal']['brow'] = hexc('#46441c')
for _v in ('front', 'side'):
    for _l in _c[_v]:
        if _l['z'] == 'f' and _l['c'] == 'mid':
            _l['c'] = 'brow'
_c['front'] = [l for l in _c['front'] if l['c'] != 'brow'] + [
    L(blob([(25, 66), (29, 60.5), (44, 60.5), (47, 64.5), (44, 68), (28, 69)], 6), 'brow', 'f', ln=True),
    L(blob([(75, 66), (71, 60.5), (56, 60.5), (53, 64.5), (56, 68), (72, 69)], 6), 'brow', 'f', ln=True)]
# y la cresta más oscura que le baja por el centro de la cabeza hasta la frente
_c['front'].insert(1, L(blob([(44, 4), (50, 0), (56, 4), (57, 30), (54, 46), (46, 46), (43, 30)], 6), 'deep', 'b', False))
_c['back'].insert(1, L(blob([(44, 4), (50, 0), (56, 4), (57, 40), (54, 70), (46, 70), (43, 40)], 6), 'deep', 'b', False))

# Knight Reader: arriba azul marino peinado hacia atrás, pero las ondas largas de los lados son casi negras
_c = CHARS[K + 'knight-reader']
_c['pal']['curl'] = hexc('#262628')
_c['front'][1:1] = [L(outline([(14, 120), (4, 104, 1), (10, 90), (2, 76, 1), (12, 62), (20, 60), (20, 100)]), 'curl', 'b', False),
                    L(outline([(86, 120), (96, 104, 1), (90, 90), (98, 76, 1), (88, 62), (80, 60), (80, 100)]), 'curl', 'b', False)]
_c['side'][1:1] = [L(outline([(2, 62), (-6, 80, 1), (4, 88), (-4, 104, 1), (8, 108), (6, 124, 1), (22, 112), (34, 104, 1), (36, 84), (38, 64), (20, 58)]),
                     'curl', 'b', False)]
_c['back'].append(L(outline([(12, 116), (2, 100, 1), (10, 88), (2, 72, 1), (10, 58), (90, 58), (98, 72, 1), (90, 88), (98, 100, 1), (88, 116), (70, 110),
                             (60, 122, 1), (50, 110), (40, 122, 1), (30, 110)]), 'curl', 'b', False))

# Cal O'Rees: la cicatriz de la frente es una marca parda (de la piel), no una estrella amarilla
CHARS[K + 'cal-o-rees'] = _fx('cal-o-rees')
CHARS[K + 'cal-o-rees']['pal']['scar'] = hexc('#c47c46')

# Frank Meyer: la cinta lleva rayas diagonales anchas morado oscuro sobre crema (no rayitas rojas)
_c = _fx('frank-meyer')
_c['pal']['band2'] = hexc('#5a3a4c')
_c['front'] = [l for l in _c['front'] if l['c'] != 'band2']
_i = next(n for n, l in enumerate(_c['front']) if l['c'] == 'band')
for _x in (18, 30, 42, 54, 66, 78):
    _y = lambda x: 47 - (1 - ((x - 50) / 36) ** 2) * 13 if abs(x - 50) < 36 else 47  # borde de arriba de la cinta (aprox.)
    _c['front'].insert(_i + 1, L([(_x, _y(_x) + 1), (_x + 5, _y(_x + 5) + 1), (_x + 1, _y(_x) + 15), (_x - 4, _y(_x - 4) + 15)], 'band2', 'f', False))
_c['side'] = [l for l in _c['side'] if l['c'] != 'band2'] + [L([(x, 33), (x + 5, 32), (x + 1, 44), (x - 4, 45)], 'band2', 'f', False) for x in (62, 76)]

# Cash Barganier: la máscara crema es más alta (le tapa la frente hasta el pelo) y el borde naranja más fino arriba
_c = _fx('cash-barganier')
_m = [n for n, l in enumerate(_c['front']) if l['c'] in ('mask_o', 'mask') and not l['w']]
_c['front'][_m[0]]['s'] = blob([(12, 62), (15, 47), (34, 43), (50, 45), (66, 43), (85, 47), (88, 62), (86, 82), (74, 90), (50, 94), (26, 90), (14, 82)], 6)
_c['front'][_m[1]]['s'] = blob([(16, 63), (18, 50), (34, 47), (50, 49), (66, 47), (82, 50), (84, 63), (80, 76), (64, 77), (50, 84), (36, 77), (20, 76)], 6)
for _l in _c['front']:
    if _l['c'] == 'mask_o' and len(_l['s']) == 36 and abs(_l['s'][0][1] - 64) < 1:
        _l['s'] = ell(_l['s'][0][0] - 2, 57, 2, 2)

# Walter Poseur: por su derecha (izquierda de la imagen) y por detrás el pelo es oliva casi negro; el mechón ondulado
# grande que cae por el otro lado es verde
_c = _fx('walter-poseur')
_c['pal']['dark'] = hexc('#3c4224')
_c['pal']['deep'] = hexc('#3c4224')
_c['front'].insert(1, L(outline([(14, 70), (6, 56), (8, 36), (16, 14), (34, 4), (40, 18), (30, 40), (22, 52), (20, 60)]), 'dark', 'b', False))
_c['side'][0]['c'] = 'dark'
_c['side'][1]['c'] = tone(hexc('#3c4224'), 0.8)
_c['side'].insert(2, L(outline([(66, 50), (84, 42), (90, 26), (82, 8), (60, -6), (50, 6), (64, 22)]), 'mid', 'b', False))
_c['back'][0]['c'] = 'dark'
for _l in _c['back'][1:]:  # el mechón verde de su izquierda, de espaldas, a la izquierda de la imagen
    if _l['c'] == 'shade':
        _l['s'] = [(100 - x, y) for x, y in _l['s']][::-1]
        _l['c'] = 'mid'

# Tabor Drummond: lo de arriba (las dos orejas de búho) es pardo topo y debajo el pelo es crema, que baja en pico por el
# centro de la frente y por las sienes; estaba al revés
_c = _fx('tabor-drummond')
_c['pal'].update(mid=hexc('#b89c7c'), shade=hexc('#9a8064'), deep=hexc('#7a6450'), side=hexc('#ece0b0'))
_c['face']['hairline'] = [(14, 64), (17, 46), (34, 42), (50, 54), (66, 42), (83, 46), (86, 64)]

# Gus Potter: casi calvo; solo una franja fina de pelo rapado verde grisáceo con dientes oscuros en lo alto de la cabeza
_c = _fx('gus-potter')
_c['pal'].update(mid=hexc('#8a9a5a'), shade=hexc('#6e7c48'), deep=hexc('#4e5a40'))
_c['face']['face_front'] = blob([(10, 60), (12, 36), (24, 16), (50, 8), (76, 16), (88, 36), (90, 60), (92, 80), (86, 98), (66, 108), (50, 110), (34, 108),
                                 (14, 98), (8, 80)])
_c['face']['hairline'] = [(10, 44), (14, 34), (24, 20), (36, 14), (50, 12), (64, 14), (76, 20), (86, 34), (90, 44)]
_c['front'] = [L(blob([(8, 48), (10, 30), (22, 10), (50, 2), (78, 10), (90, 30), (92, 48), (50, 40)], 8))] + [
    L([(x - 4, y), (x + 4, y), (x, y + 6)], 'deep', 'b', False) for x, y in ((24, 15), (37, 8), (50, 5), (63, 8), (76, 15))] + [
    l for l in _c['front'] if l['z'] == 'f']
_c['side'] = [L(outline([(80, 34), (72, 20), (50, 14), (26, 18), (12, 32), (8, 48), (20, 38), (32, 28), (50, 24), (68, 28)]))] + [
    l for l in _c['side'] if l['z'] == 'f']
_c['back'] = [L(blob([(14, 46), (17, 28), (32, 16), (50, 12), (68, 16), (83, 28), (86, 46), (76, 36), (50, 28), (24, 36)], 8))]

# Hershel Layton: la sombra de la chistera tenía un bulto redondo encima (contorno suavizado); recta como la chistera
_c = _fx('hershel-layton')
for _v in ('front', 'side', 'back'):
    for _l in _c[_v]:
        if _l['c'] == 'hat_d':
            _l['s'] = [(62, -35), (79.5, -35), (81.5, 44), (64, 44)]

# Reid Scarlet: las franjas naranjas de la cara van por dentro de la cara, pegadas a sus bordes, desde las sienes hasta la
# mandíbula (no salidas por fuera como patillas)
_c = _fx('reid-scarlet')
_ff = _c['face']['face_front']
_orp = next(l['c'] for l in _c['front'] if not isinstance(l['c'], str) and l['c'][:3] == (0xd8, 0x70, 0x2a))
_c['front'] = [l for l in _c['front'] if l['c'] != _orp and not (l['w'] and len(l['s']) == 2 and l['s'][0][0] in (30, 70))]
for _sg in (1, -1):
    _edge = sorted([p for p in _ff if (p[0] < 50) == (_sg == 1) and 58 <= p[1] <= 100], key=lambda p: p[1])
    _xi = 31 if _sg == 1 else 69
    _shape = _edge + [(_xi, _edge[-1][1] - 2), (_xi, 58)]
    _c['front'].insert(len(_c['front']) - 1, L(_shape, _orp, 'f', False))
    _c['front'].insert(len(_c['front']) - 1, L([(_xi, 58), (_xi, _edge[-1][1] - 2)], OUTC, 'f', False, False, 1.2))
# y el flequillo rosa crema le cae en mechones de punta sobre la frente, tapando las esquinas de arriba de la cara
_c['front'] += [L(blob([(10, 46), (50, 44), (90, 46), (90, 56), (50, 56), (10, 56)], 4), 'mid', 'f', False),
                L(outline([(8, 50), (24, 50), (20, 66, 1), (12, 60)]), 'mid', 'f'), L(outline([(92, 50), (76, 50), (80, 66, 1), (88, 60)]), 'mid', 'f'),
                L(outline([(30, 52), (42, 52), (34, 66, 1)]), 'mid', 'f'), L(outline([(46, 52), (60, 52), (56, 68, 1)]), 'shade', 'f'),
                L(outline([(62, 52), (74, 52), (70, 64, 1)]), 'mid', 'f')]

# ------------------------------------------------------------------ lado bien puesto de perfil y de espaldas
# De perfil (mira a la derecha) se ve su lado DERECHO, que de frente está a la izquierda de la imagen; de espaldas, lo
# que de frente está a la izquierda queda a la derecha.

# Tyche Winham: su mitad derecha (izquierda de la imagen de frente) es azul marino, así que de perfil se ve azul
_c = _fx('tyche-winham')
_navy = next(l['c'] for l in _c['front'] if not isinstance(l['c'], str))
_c['side'][0]['c'] = _navy
_c['side'][1]['c'] = tone(_navy, 0.78)

# Jacob Grimley: el monóculo está en su ojo derecho (se ve de perfil) y el mechón rosa en su lado izquierdo (no se ve de
# perfil; de espaldas queda a la izquierda de la imagen)
_c = _fx('jacob-grimley')
_c['side'] = [l for l in _c['side'] if l['c'] != 'pink'] + [
    L(ell(81, 76, 6, 8) + [ell(81, 76, 6, 8)[0]], 'rim', 'f', False, False, 2.0), L(quad((76, 82), (70, 92), (70, 104)), 'rim', 'f', False, False, 0.9)]
for _l in _c['back']:
    if _l['c'] == 'pink':
        _l['s'] = [(100 - x, y) for x, y in _l['s']][::-1]

# Paisley Onepiece: el mechón naranja cae por su izquierda (derecha de la imagen): de perfil no se ve
_c = _fx('paisley-onepiece')
_c['side'] = [l for l in _c['side'] if l['c'] != 'lock']

# Ropert Chapp: el monóculo está en su ojo izquierdo (derecha de la imagen): de perfil no se ve
_c = _fx('ropert-chapp')
_c['side'] = [l for l in _c['side'] if l['c'] != 'gold']

# ------------------------------------------------------------------ detalles (segunda pasada)
from chars_vr_keizen_arashiyama import cloud  # noqa: E402

# Steve Pinner: la marca naranja de rayo le cruza el ojo derecho (izquierda de la imagen): de perfil también se ve
_c = _fx('steve-pinner')
_c['side'].append(L([(74, 60), (80, 70), (76, 76), (82, 90)], (220, 120, 40, 255), 'f', False, False, 2.0))

# Jonah Troutman: el mechón verde oliva que le tapa el ojo derecho cae por el lado que se ve de perfil
_c = _fx('jonah-troutman')
_c['side'].append(L(outline([(68, 22), (84, 26), (90, 44), (88, 64), (84, 86, 1), (79, 64), (72, 44)]), 'olive', 'f'))

# Frank Meyer: la mata de pelo es ahuecada en mechones redondeados, no en pinchos de punta
_c = _fx('frank-meyer')
_c['front'][0:1] = [L(cloud(50, 32, 54, 40, 8, 0.3, 0.84)), L(outline([(10, 82), (-2, 66), (0, 44), (100, 44), (102, 66), (90, 82), (84, 60), (16, 60)]))]
_c['side'][0:1] = [L(cloud(42, 30, 52, 42, 8, 0.3, 0.84)), L(outline([(74, 50), (88, 40), (0, 36), (-10, 60), (2, 78), (16, 86), (32, 84), (40, 70), (50, 58), (62, 54)]))]
_c['back'][0:1] = [L(cloud(50, 32, 54, 40, 8, 0.3, 0.84)), L(outline([(10, 86), (-4, 66), (0, 44), (100, 44), (104, 66), (90, 86), (70, 92), (50, 94), (30, 92)]))]

# Cash Barganier: pelo corto y compacto en rizos redondeados (no una bola de pinchos)
_c = _fx('cash-barganier')
_c['front'][0:2] = [L(cloud(50, 32, 42, 26, 9, 0.2, 0.88)), L(outline([(12, 64), (9, 40), (91, 40), (88, 64), (80, 50), (20, 50)])),
                    L(blob([(62, 10), (88, 26), (90, 48), (76, 40)], 6), 'shade', 'b', False)]
_c['side'][0:2] = [L(cloud(46, 32, 42, 28, 9, 0.2, 0.88)), L(outline([(70, 48), (84, 38), (10, 32), (4, 56), (14, 74), (30, 74), (40, 60), (54, 52)])),
                   L(blob([(10, 44), (16, 70), (32, 72), (26, 52)], 6), 'shade', 'b', False)]
_c['back'][0:2] = [L(cloud(50, 34, 44, 28, 9, 0.2, 0.88)), L(outline([(10, 40), (90, 40), (86, 70), (66, 80), (50, 82), (34, 80), (14, 70)])),
                   L(blob([(62, 12), (90, 30), (88, 66), (66, 76)], 6), 'shade', 'b', False)]

# ------------------------------------------------------------------ piel medida en la cara del retrato
# (la media del tono de la piel iluminada de las mejillas y la barbilla; solo donde se iba más de 30 en la suma de R+G+B).
# Sin tocar: Vinny O'Gaines, Crispin Shooter y Dan Vega (difieren poco: gafas, máscara) ni Vince Bull (vendado).
_SKIN = {
    'berty-adman': '#f1b46b', 'biff-beeston': '#f1b46c', 'bill-wordsy-wordsworthy': '#f0b46d', 'bob-whittle': '#c69859',
    'boe-tyer': '#f1b46e', 'bos-horne': '#cd9149', 'bramley-cox': '#e4d4bc', 'bryce-bergman': '#f3b36b',
    'bud-hunter': '#f0b46c', 'buddy-goodman': '#f1b46c', 'cal-o-rees': '#f0b56c', 'carl-sacks': '#f0b16c',
    'chelmey': '#d89850', 'chops-denton': '#eeb66a', 'claude-snap': '#e4ae7c', 'colin-salts': '#f1b269',
    'dan-dandy': '#c69858', 'don-paolo': '#c09878', 'don-ringo': '#f6b779', 'finn-attick': '#f0b266',
    'finn-sawyer': '#f1b56c', 'flora-reinhold': '#e8c091', 'florian-hutter': '#f1b46d', 'florian-selles': '#f1b46c',
    'fran-zimmer': '#f1b46d', 'frank-meyer': '#cd914a', 'fred-makepeace': '#f0b36f', 'garland-gathers': '#f1b46c',
    'gene-bottle': '#f0b46d', 'griff-strummer': '#f9b46b', 'grover-bearing': '#f0b46c', 'guile-crocket': '#f1b56a',
    'gus-potter': '#f1b56c', 'harley-trotter': '#cd9149', 'harold-derry': '#f1b56c', 'harry-overton': '#f0b46d',
    'harry-redcastle': '#efb067', 'herb-ivore': '#f1b46d', 'herc-bigsby': '#cd914a', 'hershel-layton': '#ec9b68',
    'hollis-ticure': '#f0b370', 'hugh-dyer': '#f0b46c', 'hunter-glory': '#c59859', 'ike-flinger-doerflinger': '#ce9149',
    'jack-mate': '#f1b46c', 'jacob-grimley': '#f1b46d', 'jem-paste': '#f0b46d', 'jess-uplement': '#f0b46b',
    'joe-straiter': '#f0b46d', 'john-baird': '#c69858', 'jonah-troutman': '#f1b46c', 'jonny-strutt': '#f0b46b',
    'kevin-doors': '#c69859', 'knight-reader': '#f1b56d', 'larry-oldman': '#ce9249', 'lincoln-hawking': '#cd9149',
    'luke-raffles': '#c69858', 'lyle-o-day': '#ce924a', 'manny-steele': '#f1b56c', 'mario-nette': '#f1b56c',
    'marty-gras': '#cd914a', 'matthew-pencil': '#f1b46d', 'max-bright': '#f1b46c', 'mo-eisner': '#f1b56c',
    'mo-hawkes': '#a88565', 'nester-damus': '#cd9149', 'nick-knack': '#cd9149', 'nick-yergrub': '#c59859',
    'olef-tennant': '#f1b56c', 'pascal-richter': '#f1b46e', 'patch-upright': '#f1b46c', 'percy-wrench': '#a88564',
    'pete-grimes': '#a88565', 'pete-nokeyo': '#f0b56c', 'peyton-pope': '#f1b46c', 'phil-biblist-o-biblist': '#fdcf95',
    'pippin-flowers': '#f1b46c', 'rainier-welkin': '#7b5840', 'rayburn-lightly': '#f0b56d', 'reese-ickle': '#f1b46b',
    'reid-scarlet': '#c69858', 'rocky-rollans': '#f1b56c', 'ropert-chapp': '#f1b56c', 'rory-polisher': '#f0b46c',
    'sam-firman': '#cd9149', 'sam-fitspire': '#f1b46c', 'sam-o-reilly': '#e4ad65', 'samuel-peeps': '#f0b46c',
    'sascha-powder': '#f1b46d', 'saul-dowd': '#f0b46c', 'scamp-shrimplin': '#cd9149', 'sean-lavender': '#f8aa7d',
    'shaun-imago': '#d5984e', 'shirley-ladyman': '#f0b46d', 'shylock-watson': '#f7d697', 'silas-scrooge': '#f9d59e',
    'silver-platt': '#f1b46c', 'simon-stryker': '#f1b46b', 'sol-crater': '#f2b36b', 'stan-trum': '#f1b46c',
    'steve-pinner': '#f1b46d', 'stu-born': '#f1b46c', 'tabor-drummond': '#f4b76f', 'tad-trinket': '#f1b46c',
    'teagen-brewer': '#d2984c', 'tex-tingle': '#f1b46c', 'thomas-cott': '#f0b46d', 'tim-toppel': '#f9ab7d',
    'tyson-moodey': '#f1b46d', 'walter-poseur': '#fbbc7b', 'will-racer': '#f4b86e',
}
for _pid, _sk in _SKIN.items():
    _c = _fx(_pid)
    _c["pal"]["skin"] = hexc(_sk)
    _c["pal"]["skin_d"] = tone(hexc(_sk), 0.86)
