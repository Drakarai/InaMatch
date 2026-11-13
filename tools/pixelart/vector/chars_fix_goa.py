"""Correcciones de la revisión de diseños (grupo goa): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, blob, ell, outline, pal, strand  # noqa: E402,F401
from heads import quad  # noqa: E402,F401

WHITE = (250, 250, 250, 255)


def _fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


def _scale(layer, kx, ky, cx=50, cy=40):
    """Encoge (o agranda) una capa respecto a un punto: para pelos que se habían dibujado demasiado grandes."""
    layer = dict(layer)
    layer['s'] = [(cx + (x - cx) * kx, cy + (y - cy) * ky) for x, y in layer['s']]
    return layer


# ================================================================ go-aoba-gakuen

# Clem Attish: la piel es tostada (no naranja) y el pelo es una columna alta y estrecha encima de la frente: los lados de la
# cabeza van rapados (se ven la piel y las orejas), no un casco rojo hasta las sienes
c = copy.deepcopy(CHARS['clem-attish'])
c['pal']['skin'], c['pal']['skin_d'] = (207, 150, 103, 255), (176, 124, 84, 255)
c['front'][0] = L(outline([(30, 52), (28, 20), (32, -10), (40, -30), (56, -34), (64, -20), (66, 0), (76, -14), (96, -6), (110, 10), (104, 30, 1), (96, 12),
                           (80, 8), (72, 24), (70, 52), (50, 48)]))
c['front'][2] = L(outline([(56, -30), (64, -20), (66, 0), (60, 20), (56, 48), (70, 50), (70, 20), (68, -6)]), 'shade', 'b', False)
c['back'][0] = L(outline([(28, 90), (26, 52), (28, 20), (32, -10), (40, -30), (56, -34), (64, -20), (66, 0), (76, -14), (96, -6), (110, 10), (104, 30, 1),
                          (96, 12), (80, 8), (74, 52), (72, 90), (50, 96)]))
c['back'][2] = L(outline([(54, 20), (74, 20), (72, 88), (60, 94)]), 'shade', 'b', False)
CHARS['go-aoba-gakuen:clem-attish'] = c

# Joshua Bleak: la melena en campana cae por los dos lados de la cara hasta la barbilla y se abre en puntas (antes asomaba
# a cada lado como dos coletitas)
c = copy.deepcopy(CHARS['joshua-bleak'])
c['front'][0] = L(outline([(10, 50), (12, 26), (26, 4), (50, -4), (74, 4), (88, 26), (92, 46), (102, 62), (112, 84), (120, 104, 1), (106, 98), (102, 110, 1),
                           (92, 100), (86, 108, 1), (80, 92), (84, 62), (16, 62), (20, 92), (14, 108, 1), (8, 100), (-2, 110, 1), (-6, 98), (-20, 104, 1),
                           (-12, 84), (-2, 62), (8, 46)]))
c['front'][1] = L(outline([(60, 2), (86, 18), (94, 48), (108, 80), (112, 96), (96, 96), (86, 86), (84, 40)]), 'shade', 'b', False)
CHARS['go-aoba-gakuen:joshua-bleak'] = c

# Martin Blando: los pinchos son cortos y la mata, compacta (en el sprite salía una melena enorme que doblaba la cabeza)
c = copy.deepcopy(CHARS['martin-blando'])
for v, idx in (('front', (0, 1)), ('side', (0, 1)), ('back', (0, 1))):
    for i in idx:
        c[v][i] = _scale(c[v][i], 0.84, 0.86, 50 if v != 'side' else 46, 50)
CHARS['go-aoba-gakuen:martin-blando'] = c

# ================================================================ go-raimon-2gun

# Bucky Woodchuck: entre el pelo y la cara (más ancha y baja) quedaba una franja vacía que se veía como una cinta blanca en
# la frente; el pelo baja hasta la cara y cae en un flequillo corto de mechones, como en su modelo
c = copy.deepcopy(CHARS['bucky-woodchuck'])
c['front'][0] = L(outline([(14, 64), (12, 40), (20, 16), (38, 4), (56, 2), (78, 10), (90, 32), (88, 64), (82, 60), (66, 56), (50, 56), (34, 56), (18, 60)]))
c['front'].insert(2, _fr([(16, 60), (20, 36), (36, 22), (56, 20), (76, 28), (86, 44), (86, 60), (78, 52), (72, 60, 1), (64, 50), (56, 58, 1), (48, 48), (40, 58, 1),
                          (32, 50), (24, 60, 1)]))
c['pal'].update(pal('#3e4e7a', '#fcd0a0', iris='#1e1414', blush='#f49a8a'))
CHARS['go-raimon-2gun:bucky-woodchuck'] = c

# Hayden Whyrl: la mata de pinchos rosa es más recogida (no le dobla la cabeza a lo ancho)
c = copy.deepcopy(CHARS['hayden-whyrl'])
for v, idx, cx in (('front', (0, 1), 50), ('side', (0, 1), 40), ('back', (0, 1), 50)):
    for i in idx:
        c[v][i] = _scale(c[v][i], 0.86, 0.9, cx, 50)
CHARS['go-aoba-gakuen:hayden-whyrl'] = c

# Matt Durer: el mechón rubio es una puntita en la nuca: de frente no se ve (salían dos bolas amarillas junto a la mandíbula)
# y de espaldas es un pico corto bajo el pelo rapado, no una franja ancha de oreja a oreja
c = copy.deepcopy(CHARS['matt-durer'])
c['front'] = c['front'][:-2]
c['back'][-1] = L(outline([(38, 84), (50, 88), (62, 84), (60, 98), (54, 96), (50, 106, 1), (46, 96), (40, 98)]), 'blond', 'f', ln=True)
CHARS['go-aoba-gakuen:matt-durer'] = c


def E_key(tid, pid):
    """La clave del dibujo que usa ahora export.key_for (sin importar export, que importa chars)."""
    for k in (f'{tid}:{pid}', f"{tid.split('-')[0]}:{pid}"):
        if k in CHARS:
            return k
    return max((b for b in CHARS if pid == b or pid.startswith(b + '-')), key=len)


def _shrink(c, kx, ky, n=2, cy=50):
    """Encoge las n primeras capas (la masa del pelo y su sombra) de las tres vistas."""
    for v, cx in (('front', 50), ('side', 42), ('back', 50)):
        for i in range(min(n, len(c[v]))):
            if isinstance(c[v][i], dict):
                c[v][i] = _scale(c[v][i], kx, ky, cx, cy)
    return c


# ================================================================ go-eito-gakuen

# Ian Stein: la melena rizada azul marino es abultada pero no tanto (salía casi el doble de ancha que la cabeza)
CHARS['go-eito-gakuen:ian-stein'] = _shrink(copy.deepcopy(CHARS['ian-stein']), 0.84, 0.92)

# Dar Wynne: es ancho y fornido, de hombros caídos y brazos separados (cuerpo de gorila), no de complexión normal
c = copy.deepcopy(CHARS['dar-wynne'])
c['body'] = 'corpulento'
CHARS['go-eito-gakuen:dar-wynne'] = c

# ================================================================ go-genei-gakuen

# Hocus Sesame y Harrold Houdini: el pelo (los mechones en punta de Hocus, los cuernos de pelo de Harrold) es más corto y
# pegado a la cabeza; en el sprite les salía casi el doble de ancho
CHARS['go-genei-gakuen:hocus-sesame'] = _shrink(copy.deepcopy(CHARS['hocus-sesame']), 0.84, 0.9)
CHARS['go-genei-gakuen:harrold-houdini'] = _shrink(copy.deepcopy(CHARS['harrold-houdini']), 0.82, 0.9)

# ================================================================ go-henkaku-no-teikoku

# Earl Eton: los pinchos suben casi rectos en una cresta estrecha (salían abiertos a los lados, el doble de anchos); Colby
# Columbia: la mata de pinchos rojos es más pequeña
CHARS['go-henkaku-no-teikoku:earl-eton'] = _shrink(copy.deepcopy(CHARS['earl-eton']), 0.74, 1.0)
CHARS['go-henkaku-no-teikoku:colby-columbia'] = _shrink(copy.deepcopy(CHARS['colby-columbia']), 0.86, 0.92)

# Fred Featherstonhaugh (portero suplente): ancho y cargado de hombros, no de complexión normal; Arthur Ascot: la mata de
# pinchos blancos es recogida, con los mechones largos hacia arriba (salía como un sol el doble de ancho que la cabeza)
c = copy.deepcopy(CHARS['fred-featherstonhaugh'])
c['body'] = 'corpulento'
CHARS['go-henkaku-no-teikoku:fred-featherstonhaugh'] = c
CHARS['go-henkaku-no-teikoku:arthur-ascot'] = _shrink(copy.deepcopy(CHARS['arthur-ascot']), 0.8, 0.9)

# ================================================================ go-kaiou-gakuen

# Cheung Po: la cabeza de huevo es corta y redonda (salía alargada hacia arriba, casi tan alta como el cuerpo) y el rizo
# negro sale de lo alto, más pequeño
c = copy.deepcopy(CHARS['cheung-po'])
for v, idx in (('front', (0, 1, 2)), ('side', (0, 1, 2)), ('back', (0, 1, 2))):
    for i in idx:
        c[v][i] = _scale(c[v][i], 1.0, 0.7, 50, 64)
CHARS['go-kaiou-gakuen:cheung-po'] = c

# ================================================================ go-kuro-no-kishidan

# Nun Chuck: los dos moños rosas son bollos cortos junto a las sienes (le llegaban hasta la mandíbula); Clay Moor: la melena
# ondulada negra es menos ancha
c = copy.deepcopy(CHARS['nun-chuck'])
for v, idx in (('front', (0, 1, 2, 3)), ('side', (1,)), ('back', (0, 1))):
    for i in idx:
        c[v][i] = _scale(c[v][i], 1.12, 0.62, 50, 30)
for i in (2, 3):  # de espaldas la mata rizada es corta: se ve la nuca
    c['back'][i] = _scale(c['back'][i], 1.0, 0.7, 50, -8)
CHARS['go-kuro-no-kishidan:nun-chuck'] = c
CHARS['go-kuro-no-kishidan:clay-moor'] = _shrink(copy.deepcopy(CHARS['clay-moor']), 0.88, 0.95)
# Flam Berger: la melena naranja rizada cae hasta los hombros pero no es tan ancha
CHARS['go-kuro-no-kishidan:flam-berger'] = _shrink(copy.deepcopy(CHARS['flam-berger']), 0.86, 0.95)

# ================================================================ go-seidouzan

# Atlas Carrier: los pinchos rubios son más cortos y recogidos (en el sprite le hacían un sol alrededor de la cabeza)
CHARS['go-seidouzan:atlas-carrier'] = _shrink(copy.deepcopy(CHARS['atlas-carrier']), 0.86, 0.9)

# ================================================================ go-tengawara

# Starbuck Rogers: la cinta negra le ciñe la frente justo encima de los ojos (no le tapa media cara): debajo se le ven los ojos
# afilados y la sonrisa de dientes
c = copy.deepcopy(CHARS['starbuck-rogers'])
for v, idx in (('front', (4, 5)), ('side', (3,)), ('back', (3,))):
    for i in idx:
        c[v][i] = _scale(c[v][i], 1.0, 0.66, 50, 30)
c['face'].update({'eyes': 'sharp', 'eye_y': 74})
for v, idx in (('front', (2, 3)), ('back', (1, 2))):  # el moño crema es más estrecho que la cinta
    for i in idx:
        c[v][i] = _scale(c[v][i], 0.8, 1.0, 50, 40)
c['pal']['iris'] = (30, 20, 20, 255)
CHARS['go-tengawara:starbuck-rogers'] = c
# Jimmy Kyrk: los pinchos naranjas son cortos y salen hacia arriba (no un sol el doble de ancho que la cabeza)
CHARS['go-tengawara:jimmy-kyrk'] = _shrink(copy.deepcopy(CHARS['jimmy-kyrk']), 0.82, 0.9)
# Sithri Peon: el moño de lo alto es pequeño (salía un penacho casi tan alto como la cara); Isaac Binks: la mata blanca de
# pinchos es más recogida
c = copy.deepcopy(CHARS['sithri-peon'])
for v in ('front', 'side', 'back'):
    c[v][0] = _scale(c[v][0], 0.7, 0.6, 50 if v != 'side' else 44, 8)
CHARS['go-tengawara:sithri-peon'] = c
CHARS['go-tengawara:isaac-binks'] = _shrink(copy.deepcopy(CHARS['isaac-binks']), 0.85, 0.92)

# Joaquín Coronado, Friedrich Schiller, Ota Shape y Adarn Shame: su pelo (pinchos o mata) es más recogido que el que salía en
# el sprite, que les ensanchaba la cabeza mucho más que en su modelo
CHARS['go-raimon-2gun:joaqu-n-coronado'] = _shrink(copy.deepcopy(CHARS[E_key('go-raimon-2gun', 'joaqu-n-coronado')]), 0.85, 0.92)
CHARS['go-raimon-2gun:friedrich-schiller'] = _shrink(copy.deepcopy(CHARS[E_key('go-raimon-2gun', 'friedrich-schiller')]), 0.86, 0.92)
CHARS['go-raimon-2gun:ota-shape'] = _shrink(copy.deepcopy(CHARS[E_key('go-raimon-2gun', 'ota-shape')]), 0.86, 0.92)
CHARS['go-raimon-2gun:adarn-shame'] = _shrink(copy.deepcopy(CHARS[E_key('go-raimon-2gun', 'adarn-shame')]), 0.86, 0.92)

# ================================================================ go-unlimited-shining

# Dwight Whittaker y Bailong: sus pinchos son más cortos y pegados (salían como un sol alrededor de la cabeza)
CHARS['go-unlimited-shining:dwight-whittaker'] = _shrink(copy.deepcopy(CHARS[E_key('go-unlimited-shining', 'dwight-whittaker')]), 0.86, 0.92)
CHARS['go-unlimited-shining:bailong'] = _shrink(copy.deepcopy(CHARS[E_key('go-unlimited-shining', 'bailong')]), 0.86, 0.92)

# ================================================================ go-demon-s-horn

# Keith Wellington: el casco de pelo en forma de seta es más pequeño (salía casi tan ancho como los hombros y le tapaba la cara)
CHARS['go-demon-s-horn:keith-wellington'] = _shrink(copy.deepcopy(CHARS[E_key('go-demon-s-horn', 'keith-wellington')]), 0.84, 0.9)

# Xavier Shotwell (portero de Cuerno Demoníaco): la melena es rubia con mechas finas rosas y blancas que siguen el
# peinado hacia un lado; antes la mecha rosa ocupaba media cabeza
c = copy.deepcopy(CHARS['xavier-shotwell'])
c['pal']['streak'] = (250, 246, 240, 255)
c['front'][1] = strand([(60, 4), (36, 12), (20, 32), (12, 70), (8, 110)], 'pink', 'b', 9.0)
c['front'][2] = strand([(48, 2), (26, 16), (14, 40), (6, 80)], 'streak', 'b', 4.5)
c['front'][4] = strand([(68, 12), (50, 20), (34, 30)], 'pink', 'f', 6.0)
c['side'][1] = strand([(50, 4), (32, 30), (22, 80), (16, 120)], 'pink', 'b', 9.0)
c['side'][2] = strand([(70, 14), (50, 26), (38, 60), (32, 96)], 'streak', 'b', 4.5)
c['back'][1] = strand([(46, 2), (48, 60), (50, 122)], 'pink', 'b', 9.0)
c['back'][2] = strand([(62, 6), (60, 60), (56, 110)], 'streak', 'b', 4.5)
CHARS['go-demon-s-horn:xavier-shotwell'] = c

# Spike Stiletto: de espaldas, encima del aro verde oscuro asoman los pinchos azul claro del pelo, y del aro baja un pico
# corto verde oscuro por el centro de la nuca (antes solo se veía una barra plana sobre la cabeza calva)
c = copy.deepcopy(CHARS['spike-stiletto'])
c['back'].insert(1, L(outline([(-10, 14), (10, 4), (12, -10, 1), (26, 2), (34, -18, 1), (44, 0), (52, -24, 1), (60, 0), (70, -16, 1), (76, 2), (90, -8, 1),
                               (92, 6), (110, 14), (50, 22)])))
c['back'].insert(2, L(outline([(52, -20), (60, 0), (70, -14), (76, 4), (92, 8), (108, 14), (60, 16)]), 'shade', 'b', False))
c['back'].append(L(outline([(42, 26), (58, 26), (50, 44, 1)]), 'wing', 'b'))
CHARS['go-kuro-no-kishidan:spike-stiletto'] = c
