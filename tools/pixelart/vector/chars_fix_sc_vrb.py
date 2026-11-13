"""Correcciones de la revisión de diseños (grupo sc_vrb): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de Victory Road (scouts-vr), segunda tanda: colores de pelo y piel medidos en su retrato (agrupando los
colores de la cabeza del retrato) y retoques de forma y rasgos donde el dibujo se apartaba del retrato."""
import copy

from chars import CHARS
from heads import L, blob, ell, fat, lerp, quad, strand  # noqa: F401

K = 'scouts-vr:'
OUT = (60, 24, 16, 255)


def hx(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _scale(old_ref, new_ref, c):
    """Lleva el color c (sombra o brillo de old_ref) al nuevo tono: las sombras con la misma proporción de luz y los
    brillos con la misma mezcla hacia el blanco que tenían."""
    so, sc = sum(old_ref[:3]), sum(c[:3])
    if sc <= so:  # sombra: el nuevo color oscurecido en la misma proporción
        f = sc / so if so else 1.0
        return tuple(max(0, min(255, int(round(v * f)))) for v in new_ref[:3]) + (255,)
    t = (sc - so) / max(1, 765 - so)  # brillo: mezcla hacia el blanco
    return tuple(int(round(v + (255 - v) * t)) for v in new_ref[:3]) + (255,)


def _fx(pid):
    """Copia del dibujo actual del ojeador para corregirla (con su misma clave), con las capas en listas planas."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = [x for it in c[v] for x in (it if isinstance(it, list) else [it])]
    CHARS[K + pid] = c
    return c


def _swap(c, old, new):
    """Cambia en todas las vistas las capas pintadas con el color literal old (#hex) por new (#hex o clave de paleta)."""
    o = hx(old)[:3]
    n = hx(new) if isinstance(new, str) and new.startswith('#') else new
    for v in ('front', 'side', 'back'):
        for l in c[v]:
            if isinstance(l['c'], tuple) and tuple(l['c'][:3]) == o:
                l['c'] = n


def col(pid, mid=None, skin=None, **kw):
    """Colores medidos en el retrato. mid / skin arrastran sus sombras (shade, deep, light / skin_d) en la misma
    proporción que tenían; el resto de claves (#hex) se ponen tal cual en la paleta."""
    c = CHARS[K + pid] if isinstance(CHARS[K + pid]['front'][0], dict) else _fx(pid)
    p = c['pal']
    if mid:
        new = hx(mid)
        for k in ('shade', 'deep', 'light'):
            if k in p and k not in kw:
                p[k] = _scale(p['mid'], new, p[k])
        p['mid'] = new
    if skin:
        new = hx(skin)
        if 'skin_d' not in kw:
            p['skin_d'] = _scale(p['skin'], new, p['skin_d'])
        p['skin'] = new
    for k, v in kw.items():
        p[k] = hx(v)
    return c


# ------------------------------------------------------------------ colores de pelo y piel medidos en el retrato
# (mid = tono medio del pelo; skin = piel de la cara). Muchos tenían la piel mucho más oscura que el retrato.
for _pid, _kw in {
    'karina-rosenqueen': dict(mid='#907a7a', skin='#fdeae1'),
    'torric-brawnstone': dict(mid='#f67439', skin='#c88b76'),
    'talken-bigby': dict(mid='#b19c59', skin='#fbcaa9'),
    'alonzo-readdie': dict(skin='#fce1c8'),
    'bastian-brineford': dict(mid='#b7b796', skin='#c28464'),
    'puerita-cakeley': dict(mid='#b76454', shade='#88463c', deep='#592f28'),
    'damion-duform': dict(mid='#507378', skin='#d8ac9c', brow='#2c4a4c'),
    'joyce-deckard': dict(mid='#f18f1b'),
    'gloria-somdenn': dict(mid='#5a699b', shade='#414d7c', deep='#2b3256'),
    'barnaby-livergain': dict(mid='#93b7da', skin='#c58b77'),
    'erina-haberdash': dict(mid='#464d91'),
    'tally-mcintosh': dict(mid='#788ab3'),
    'pristin-florynce': dict(mid='#edd65b'),
    'miriam-masheene': dict(mid='#37373c', skin='#fce9df'),
    'dina-faith-kingston': dict(mid='#d0c99f', skin='#fbd7c3'),
    'harris-gridley': dict(mid='#333333', skin='#dbb2a4'),
    'verdy-golnuts': dict(mid='#779ea2'),
    'blendon-frugel': dict(mid='#544344', skin='#f9e5d2'),
    'judeau-garb': dict(mid='#a09889'),
    'cassia-bladecroft': dict(mid='#716f6b', skin='#c78c73'),
    'edith-endenwald': dict(mid='#fbefdc', shade='#dcc4b0', deep='#9e7368', skin='#fbe1cf', iris='#e0a830'),
    'helen-deavor': dict(mid='#31344a', shade='#262a3c', deep='#1c1d2a'),
    'macy-drapeley': dict(mid='#a5362f', shade='#86352d', deep='#531f1c'),
    'diana-whispervelt': dict(mid='#e6ca85'),
    'serina-shelby': dict(mid='#1c485f', skin='#f7cbaf'),
    'praiseton-strongshout': dict(mid='#dd6861', skin='#fce6d3'),
    'whitney-blackrock': dict(mid='#c07fcb'),
    'hildy-tattleswell': dict(mid='#855091'),
    'aria-fondue': dict(mid='#e7a18f'),
    'laurence-stumbleton': dict(mid='#368a8a', deep='#273d3a', skin='#fbe0b5'),
    'finnes-grapplefeld': dict(mid='#4b1c1e', shade='#3b1a1a', deep='#2a1012'),
    'adele-lettante': dict(mid='#bfb6c5', skin='#fde0af'),
    'ouijane-boarden': dict(mid='#2d2c2c'),
    'cosmo-starward': dict(mid='#5c4e45', skin='#cb7d5a'),
    'norah-noshawn': dict(mid='#382d57'),
    'jeremy-yung': dict(mid='#989596'),
    'britson-farago': dict(mid='#dfb34a', skin='#fcd2be'),
    'minerva-elderbright': dict(mid='#41647b'),
    'raymond-galak': dict(mid='#0a2434'),
    'flynn-duval': dict(mid='#351713', skin='#d38460'),
    'brenae-ackermann': dict(mid='#4a596d', iris='#7ab4c8'),
    'frey-granzburn': dict(skin='#674f54'),
    'dizzy-fumbleton': dict(mid='#524845', skin='#daab9a'),
    'nivea-etoile': dict(mid='#c5c3c1'),
    'gilbert-kraft': dict(mid='#8b6d84', skin='#c28666'),
    'niro-vannaburg': dict(mid='#867b78', skin='#fcc6a2'),
    'iza-improvelli': dict(mid='#8b5541'),
    'curven-rallye': dict(mid='#5b6c62', skin='#daafa0'),
    'jella-fisker': dict(mid='#467bba'),
    'cleara-sounds': dict(mid='#66344e', shade='#532737', deep='#441e28'),
    'tempest-liebkind': dict(mid='#95b4ce', skin='#f6c7a8'),
    'castor-fatica': dict(mid='#7c5273'),
    'inga-calmari': dict(mid='#75c0c8'),
    'wily-wimpinberg': dict(mid='#414141', skin='#fcdeb1'),
    'callista-norton': dict(mid='#e4e1ef'),
    'slater-verbenbaum': dict(mid='#946c5d', skin='#fdebe0'),
    'lumina': dict(mid='#f0e794'),
    'chiana-fielder': dict(mid='#33d29c'),
    'caelum-wade': dict(skin='#f6d0b3'),
    'trad-askenburg': dict(mid='#91172c', shade='#741524', deep='#4b1a1d', skin='#dbafa0'),
    'regis-tunesmith': dict(mid='#af9c6d'),
    'mora-grimmoir': dict(mid='#c85022'),
    'isanna-countenford': dict(mid='#684e3b', skin='#fbc5a3'),
    'wentworth-wiggins': dict(mid='#fded7d', skin='#fbd8ca'),
    'olive-mapleton': dict(mid='#fa9386', skin='#f9cdaf'),
    'fang-arzola': dict(mid='#4f5875', skin='#fcdfb2'),
    'galina-chilvers': dict(mid='#bdc5ec', skin='#ddaa8d'),
    'verica-nyman': dict(mid='#5d6048', skin='#fdeadf'),
    'emil-tait': dict(mid='#e95645', shade='#b84034', deep='#852d25'),
    'rhianna-wardholdt': dict(mid='#1c2024'),
    'trace-combe': dict(mid='#c17763', shade='#a0604f', deep='#68342d', skin='#facaab'),
    'zayn-pinegrove': dict(mid='#3c484f', skin='#fddbb4'),
    'machaela-thevert': dict(mid='#69614b', skin='#fad0b4'),
    'adelaide-plainhart': dict(mid='#7f4e3c', skin='#fbe1cf'),
    'focas-quayle': dict(mid='#9ee1bb', skin='#f1a97b'),
    'emi-blanchett': dict(mid='#b7987f'),
    'livia-marsquall': dict(mid='#ad6f83'),
    'megal-o-donn': dict(mid='#df7038', skin='#f9c5a3'),
    'colleen-evenholm': dict(mid='#2d2a3e', skin='#f9d7c6'),
    'murray-hollowpot': dict(mid='#355449', skin='#fad4c2'),
    'krome-tallic': dict(mid='#2f474a'),
    'evander-greenvale': dict(mid='#707641', shade='#5c6034', deep='#4a3a21', skin='#c69074', brow='#646a36'),
    'curia-caldwell': dict(mid='#75426d'),
    'ivo-woodward': dict(mid='#5b7f6d'),
    'ava-ehrenreich': dict(mid='#e0cfac', skin='#fde4d2'),
    'cheery-allende': dict(mid='#a9c7ce'),
    'annie-glenvale': dict(mid='#152841', skin='#c29070'),
    'zackory-wart': dict(mid='#631e11', skin='#f7a979'),
    'louise-basson': dict(mid='#e26e26'),
    'wendy-stitchilton': dict(mid='#55619b', shade='#433f5b', deep='#2d2a3e', skin='#face99'),
    'ripley-swaydon': dict(mid='#e8dcc1', skin='#c08b78'),
    'lisa-lovetluke': dict(mid='#f3726e', skin='#fdcca7'),
    'cyrus-veil': dict(mid='#b7c235', skin='#d7ab9a'),
    'heather-lovella': dict(mid='#281c32'),
    'lior-morrissey': dict(mid='#dcaa18', skin='#af6955'),
    'kipper-marino': dict(mid='#3c4158'),
    'cristensen-blance': dict(mid='#281f15', skin='#fcd6bc'),
    'puffet-vearn': dict(mid='#581e2b', shade='#431d23', deep='#371b1e', skin='#daad9c'),
    'aila-pavey': dict(mid='#231f33', skin='#f7e3d5'),
    'mika-upton': dict(mid='#d65b8b'),
    'stratos-merrill': dict(mid='#486182', skin='#fac7a6'),
    'eli-hoopsen': dict(mid='#3d3833', skin='#fbdfb4'),
    'coco-lajoie': dict(mid='#3c2c3f', skin='#fcd3be'),
    'lysander-trimore': dict(mid='#c79573', shade='#a8775c', deep='#8e6252', front='#e9d8bc', skin='#efbea5'),
    'morrigan-shutterly': dict(mid='#47203b', shade='#361d29', deep='#2e1b22'),
    'pierce-castleton': dict(mid='#5a4d46', skin='#fbbd89'),
    'starry-durant': dict(mid='#3a2848'),
    'godfrey-shahmann': dict(mid='#867350', skin='#d6a476'),
    'ricemond-chowen': dict(mid='#af6057', skin='#fccbaa'),
    'vicente-olsean': dict(mid='#333333', skin='#fbc7a5'),
    'hardan-kempton': dict(mid='#685458', shade='#503f41', deep='#382b2d', skin='#fce5d1'),
    'niles-gawkerson': dict(mid='#185c92', shade='#183e5e', skin='#c78147'),
    'margo-versier': dict(mid='#c54159', shade='#97323f', deep='#66262d', skin='#fcd0bf'),
    'naya-prism': dict(mid='#4e7d6d', skin='#c28564'),
    'eamon-cattrall': dict(mid='#515b4e', skin='#eecba0'),
    'donovan-brasswagon': dict(mid='#e5b348', skin='#faebe0'),
    'brianna-summing': dict(mid='#4d4322', skin='#f7a97a'),
    'allegra-langton': dict(mid='#ad79ad', skin='#fde9df'),
    'credence-throwe': dict(mid='#dd3b7e', skin='#c18568'),
    'leston-thoreau': dict(mid='#b9c5c2', skin='#fde9df'),
    'colm-dawdlin': dict(mid='#64586a', skin='#f2c8b6'),
    'abbie-sentridge': dict(mid='#3d563f', skin='#fae5d7'),
    'vane-nishmont': dict(mid='#39383e', skin='#facfad'),
    'ruy-roosalot': dict(mid='#3b4778', shade='#2f3a62', deep='#2a2b3f', light='#6480a9'),
    'lester-bawlund': dict(mid='#331219', shade='#2a0f15', deep='#1e0a0e', skin='#fad5c3'),
    'ezra-bachmann': dict(mid='#e4c698', skin='#fcd6bb'),
    'tessa-rapperton': dict(mid='#3d4748', skin='#fae2d3'),
    'stran-linemont': dict(mid='#74d4e5'),
    'serene-goldwell': dict(mid='#d9c481'),
    'lyra-nazar': dict(mid='#312b1e', skin='#daad9b'),
    'caddy-chamomile': dict(mid='#fab8d1'),
    'felicia-felton': dict(mid='#765840', shade='#5c4533'),
    'calina-breezer': dict(mid='#b18a9b', skin='#fee3d1'),
    'soria-bordeau': dict(mid='#8f515e', shade='#6e424a', deep='#4e292d', skin='#fbe9e0'),
    'hernan-rippett': dict(mid='#e0cfba', skin='#fcbda0'),
    'trane-levitt': dict(mid='#779391', skin='#facdae'),
    'claudette-clackenoff': dict(mid='#d8a998', shade='#b8867a', deep='#754741', skin='#fbe5d6'),
    'margot-napier': dict(mid='#ddbf80', shade='#b8985c', deep='#866245', light='#fdfce6', skin='#fbd7c8'),
    'duarte-wilde': dict(mid='#494572', skin='#b66c59'),
    'yarden-forsman': dict(mid='#c1cda7', skin='#673e32'),
    'nerida-neuland': dict(mid='#2f2e36', skin='#fde4d3'),
    'winifred-wardrow': dict(mid='#fdd89e', shade='#e2b077', deep='#b8805a'),
    'faris-creed': dict(mid='#242429', skin='#f7d3b2'),
    'hiatt-heddon': dict(skin='#b26a5a'),
    'nico-kensee': dict(mid='#b3676d', shade='#975558', deep='#733a3b', skin='#fde8d6'),
    'ravyn-grooves': dict(mid='#7de182', shade='#5cb862', deep='#3f7a48', skin='#ad6f55'),
    'lawton-dappermann': dict(mid='#746962', skin='#fbe0bc'),
    'sami-wampovich': dict(mid='#503437', shade='#3e2728', deep='#321f1f', skin='#fccfb9'),
    'kurtis-loafinn': dict(mid='#42477d', skin='#f9c4a9'),
    'grayson-tiltwood': dict(mid='#558a99', skin='#fceae0'),
    'nasser-pryce': dict(mid='#e56f40', shade='#bf5530', deep='#7d3421', skin='#fbcbaa'),
    'sten-fanborough': dict(mid='#711907', shade='#5a1709', deep='#412015', skin='#f6ae81'),
    'alara-belmont': dict(mid='#804429', shade='#6b3c26', deep='#5d2e18', skin='#f7ceb2'),
    'feodor-wayte': dict(mid='#b83f3d', shade='#9d3430', deep='#772520', skin='#f6ac81'),
    'liam-tossarawn': dict(mid='#cc3355', shade='#982e3d', deep='#662426', skin='#f9bc8b'),
    'didar-valmont': dict(mid='#b2a690', skin='#683933', skin_d='#512e2a'),
    'pennie-pound': dict(mid='#2e2d32', skin='#fbe5d2'),
    'cuthbert-obelidge': dict(mid='#cdc8b4', skin='#fee4d2'),
    'ignacio-gerhardt': dict(mid='#db4f54', skin='#c38769'),
    'maeve-smith': dict(mid='#5a482f', shade='#4a3a26', deep='#3f3122', skin='#faccac'),
    'biijiro-onoda': dict(mid='#62161f', skin='#fac7a7'),
    'montgomery-marchand': dict(mid='#373f3d', shade='#292c2a', deep='#1e2120', skin='#d7ae9e'),
    'shawl-creedstern': dict(mid='#1a1533', skin='#d9a08e'),
    'manon-matopia': dict(mid='#ea9a35'),
    'watt-ownes': dict(mid='#744123', shade='#5c2f1d', deep='#3f231c', skin='#b17359'),
    'tenison-onsera': dict(mid='#777778', skin='#fcd3be'),
    'jester-biggs': dict(mid='#a34e57', skin='#f9ceba'),
    'fenric-wulfgang': dict(mid='#bed9d8', skin='#faece4'),
    'chaunce-gambell': dict(mid='#c5a5af', skin='#fcc6a2'),
    'patrice-kampanee': dict(mid='#e4bbbc', shade='#c99a9d', deep='#865556'),
    'carole-meine': dict(mid='#cbcaca', skin='#fce9e0'),
    'foster-bracewell': dict(mid='#2c2e51', skin='#fae5d6'),
    'charlet-namora': dict(mid='#435a54', shade='#364540', deep='#292d2b', skin='#fae4d1'),
    'sona-sondheim': dict(mid='#c5bdaf', shade='#a89c8c', deep='#8d7975', skin='#fcd9cc'),
    'smiles-thrussell': dict(mid='#625651', shade='#4d403b', deep='#382a26', skin='#fde5d0'),
    'willem-durrmore': dict(mid='#fdf8d7', skin='#bf8975'),
}.items():
    col(_pid, **_kw)

# colores literales de mechones y adornos, medidos en el retrato
for _pid, _old, _new in (
    ('puerita-cakeley', '#f0d080', '#e8c29c'),        # mechón rubio pálido, no amarillo
    ('miriam-masheene', '#c02a2a', '#a84a48'),        # mechón rojo apagado
    ('cassia-bladecroft', '#f0c040', '#f9d273'),
    ('slater-verbenbaum', '#f0e4a0', '#f2e8c8'),      # puntas y cejas crema pálido
    ('olive-mapleton', '#6ae0a0', '#72eeaa'),
    ('megal-o-donn', '#7ac8a8', '#83ab90'),           # mechón verde grisáceo
    ('curia-caldwell', '#f0a8d0', '#e8b6bc'),         # puntas rosa palo
    ('lester-bawlund', '#b02030', '#901120'),
    ('cristensen-blance', '#80d0b0', '#8cc6b1'),
    ('praiseton-strongshout', '#5a3428', '#4e2916'),
):
    _swap(CHARS[K + _pid], _old, _new)


# ------------------------------------------------------------------ ayudas para los retoques de forma
def brows(c, key, thick=4.0, angry=False, side=True, dy=0.0, w=8.0):
    """Cejas gruesas rellenas del color key (del pelo, por ejemplo) en lugar de la raya fina de contorno."""
    f = c['face']
    ey, sep = f.get('eye_y', 75), f.get('eye_sep', 14)
    by = ey - 11 + dy
    f['brows'] = False
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        if angry:  # baja hacia la nariz
            pts = [(cx - w * s, by - 3), (cx + (w - 1) * s, by + 1.5), (cx + (w - 1) * s, by + 1.5 + thick * 0.8), (cx - w * s, by - 3 + thick)]
        else:
            pts = [(cx - w * s, by + 1.5), (cx - 2 * s, by - 2.5), (cx + w * s, by - 0.5), (cx + w * s, by - 0.5 + thick * 0.7),
                   (cx - 2 * s, by - 2.5 + thick), (cx - w * s, by + 1.5 + thick * 0.6)]
        c['front'].append(L(blob(pts, 5), key, 'f', ln=True))
    if side:
        if angry:
            pts = [(71, by - 2), (85, by + 2), (85, by + 2 + thick * 0.8), (71, by - 2 + thick)]
        else:
            pts = [(71, by + 1), (78, by - 2.5), (86, by - 0.5), (86, by + thick * 0.6), (78, by - 2.5 + thick), (71, by + 1 + thick * 0.6)]
        c['side'].append(L(blob(pts, 5), key, 'f', ln=True))


def top_tip(c, key, view, h=14, w=7, idx=0):
    """Pinta la punta más alta de la capa idx (pincho, tupé) con otro color."""
    l = c[view][idx]
    tx, ty = min(l['s'], key=lambda p: p[1])
    tri = [(tx, ty), (tx + w, ty + h), (tx + w * 0.4, ty + h * 0.7), (tx, ty + h * 0.95), (tx - w * 0.4, ty + h * 0.7), (tx - w, ty + h)]
    c[view].insert(idx + 1, L(tri, key, l['z'], False))


def beads(pts, r=5.2, c='mid', z='b', end=None, n=None):
    """Trenza: cuentas redondas a lo largo de la curva por pts (y una punta de otro color al final)."""
    path = []
    for i in range(len(pts) - 1):
        path += [lerp(pts[i], pts[i + 1], t / 8) for t in range(8)]
    path.append(pts[-1])
    out = []
    step = max(1, len(path) // (n or max(3, len(path) // 3)))
    for i in range(0, len(path), step):
        x, y = path[i]
        out.append(L(ell(x, y, r, r * 0.95, 16), c, z, ln=(z == 'f')))
    if end:
        x, y = path[-1]
        out.append(L(ell(x, y + r * 0.6, r * 1.05, r * 1.1, 16), end, z, ln=(z == 'f')))
    return out


def mirror_layers(ls):
    return [dict(l, s=[(100 - x, y) for x, y in l['s']][::-1]) for l in ls]


# ------------------------------------------------------------------ retoques de forma y rasgos
# Torric Brawnstone: cejas naranjas gruesas (del color del pelo) y los lados rapados azul marino
_c = CHARS[K + 'torric-brawnstone']
_c['pal']['low'] = hx('#2f3550')
brows(_c, 'mid', thick=5.0)

# Marjorie Piperplume: dos tonos: casquete castaño con raya en medio y las nubes de los lados y el flequillo melocotón
_c = col('marjorie-piperplume', mid='#eebfa9', shade='#d49e8a', deep='#b07c6c', top='#a57765', top_d='#835a50')
_c['front'].insert(3, L(blob([(8, 44), (14, 18), (50, 2), (86, 18), (92, 44), (74, 36), (56, 40), (50, 34), (44, 40), (26, 36)], 8), 'top', 'b', False))
_c['front'].insert(4, L(blob([(60, 6), (86, 18), (92, 42), (76, 34)], 6), 'top_d', 'b', False))
_c['front'].insert(5, strand([(50, 4), (50, 34)], 'top_d', 'b', 1.2))
_c['side'].insert(2, L(blob([(4, 50), (8, 18), (44, 0), (80, 12), (90, 34), (70, 34), (50, 42), (24, 56)], 8), 'top', 'b', False))
_c['back'].insert(3, L(blob([(6, 50), (14, 16), (50, 0), (86, 16), (94, 50), (70, 60), (50, 56), (30, 60)], 8), 'top', 'b', False))
_c['back'].insert(4, strand([(50, 2), (50, 54)], 'top_d', 'b', 1.2))

# Damion Duform: cejas gruesas azul marino oscuro
_swap(CHARS[K + 'damion-duform'], '#2a4a8a', '#2a3f6a')

# Whitney Blackrock: trenzas largas que salen de dos lazos altos, suben en arco hacia fuera y bajan hasta los hombros
# con las puntas oscuras (antes eran dos mechones cortos de lado)
_c = _fx('whitney-blackrock')
_c['pal']['tip'] = hx('#6a3e72')
_c['pal']['tie'] = hx('#3b2b41')
_L = [(10, 30), (-2, 14), (-16, 12), (-24, 28), (-22, 54), (-14, 76), (-12, 94)]
_bl = beads(_L, 6.4, 'mid', 'b', end='tip')
_tie = [L(ell(8, 32, 5.5, 5, 16), 'tie', 'f')]
_c['front'] = _c['front'][:2] + _bl + mirror_layers(_bl) + _tie + mirror_layers(_tie)
_S = [(8, 26), (-6, 12), (-20, 14), (-26, 34), (-22, 60), (-14, 82), (-12, 98)]
_c['side'] = _c['side'][:2] + beads(_S, 6.4, 'mid', 'b', end='tip') + [L(ell(8, 28, 5.5, 5, 16), 'tie', 'f')]
_bb = beads([(12, 30), (0, 14), (-14, 12), (-22, 28), (-20, 54), (-12, 76), (-10, 94)], 6.4, 'mid', 'b', end='tip')
_c['back'] = _c['back'][:2] + _bb + mirror_layers(_bb) + [L(ell(10, 32, 5.5, 5, 16), 'tie', 'f'), L(ell(90, 32, 5.5, 5, 16), 'tie', 'f')]
brows(_c, 'tie', thick=4.0, angry=True)

# Helen Deavor: las horquillas blancas van a los dos lados de la raya, no solo en uno
_c = _fx('helen-deavor')
_c['front'] += mirror_layers([l for l in _c['front'] if l['c'] == (248, 248, 248, 255)])

# Verdy Golnuts: la punta del tupé es blanca (como nevada) y las cejas gruesas gris azulado
_c = _fx('verdy-golnuts')
_c['pal']['snow'] = hx('#eef6f4')
for _v in ('front', 'side', 'back'):
    top_tip(_c, 'snow', _v, h=13, w=6.5)
brows(_c, 'shade', thick=4.5, dy=1)


def sharp(pts, n=6):
    """Contorno cerrado suave por los puntos; los que llevan un tercer valor, (x, y, 1), quedan en punta."""
    out, k = [], len(pts)
    for i in range(k):
        p1, p2 = pts[i], pts[(i + 1) % k]
        p0 = p1 if len(p1) > 2 else pts[i - 1]
        p3 = p2 if len(p2) > 2 else pts[(i + 2) % k]
        for j in range(n):
            t = j / n
            out.append(tuple(0.5 * (2 * p1[c] + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t * t
                                    + (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t ** 3) for c in (0, 1)))
    return out


def flower(x, y, r=3.2, c=(250, 250, 248, 255), mid=(240, 200, 90, 255)):
    import math
    out = [L(ell(x + r * 0.9 * math.cos(a), y + r * 0.9 * math.sin(a), r * 0.62, r * 0.62, 12), c, 'f') for a in [i * 2 * math.pi / 5 - math.pi / 2 for i in range(5)]]
    return out + [L(ell(x, y, r * 0.35, r * 0.35, 10), mid, 'f', False)]


# Harris Gridley: franja rojiza (colorete) sobre el puente de la nariz, entre los ojos
_c = _fx('harris-gridley')
_c['front'].append(L(blob([(44, 62), (50, 61), (56, 62), (54, 74), (50, 76), (46, 74)], 6), hx('#e0aaa2'), 'f', False))

# Trace Combe: el flequillo baja en mechones de punta desde lo alto de la cabeza y le tapa los ojos (antes era una
# visera plana con dientes pegada a la frente)
_c = _fx('trace-combe')
_c['front'] = [l for i, l in enumerate(_c['front']) if i not in (2, 3, 4)]
_c['front'] += [
    L(sharp([(5, 58), (8, 32), (28, 12), (50, 8), (72, 12), (92, 32), (95, 58), (90, 72, 1), (83, 64), (77, 82, 1), (70, 70),
             (62, 86, 1), (56, 74), (49, 88, 1), (43, 74), (35, 84, 1), (29, 68), (21, 78, 1), (15, 64), (9, 72, 1)]), 'mid', 'f'),
    L(blob([(62, 14), (86, 28), (92, 56), (82, 64), (72, 40)], 6), 'shade', 'f', False),
    strand([(48, 10), (44, 40), (46, 80)], 'shade', 'f', 1.2), strand([(30, 20), (26, 46), (30, 74)], 'shade', 'f', 1.1),
    strand([(66, 18), (66, 50), (62, 78)], 'deep', 'f', 1.1)]

# Ava Ehrenreich: pelo recogido (frente despejada, mechones cortos delante de las orejas hasta la mandíbula) con dos
# moños grandes a los lados de la cabeza y una flor blanca en cada uno (antes melena hasta el cuello y moños diminutos)
from chars_scouts_ie1_09 import dome  # noqa: E402
_c = _fx('ava-ehrenreich')
_bun = lambda x, y, r, z='b': L(ell(x, y, r, r * 0.95, 30), 'mid', z)  # noqa: E731
_c['front'] = [_bun(6, 34, 14), _bun(94, 34, 14), L(ell(10, 38, 9, 8, 20), 'shade', 'b', False)] + dome('front', top=4, w=45, cy=46, sb=92) + \
    [strand([(30, 14), (38, 40)], 'shade', 'b', 1.0), strand([(70, 14), (62, 40)], 'shade', 'b', 1.0)] + flower(14, 24) + flower(86, 24)
_c['side'] = dome('side', top=4, w=45, cy=46, nape=80, fr=46) + [dict(_bun(32, 20, 14, 'f'), ln=True), L(ell(34, 26, 8, 7, 20), 'shade', 'b', False)] + flower(40, 14)
_c['back'] = dome('back', top=4, w=45, cy=46, nape=80) + [_bun(6, 34, 14, 'f'), _bun(94, 34, 14, 'f'), strand([(50, 8), (50, 74)], 'shade', 'b', 1.0)]

# Wentworth Wiggins: melena en forma de seta, mucho más ancha que la cabeza, con el borde ondulado, el rizo en corazón en
# medio del flequillo y la cara de abajo más oscura
_c = _fx('wentworth-wiggins')
_c['pal']['under'] = hx('#d9a640')
_W = [(-20, 62, 1), (-10, 40), (12, 16), (50, 4), (88, 16), (110, 40), (120, 62, 1), (104, 52), (90, 68, 1), (78, 50), (66, 64, 1),
      (58, 50), (50, 60, 1), (42, 50), (34, 64, 1), (22, 50), (10, 68, 1), (-4, 52)]
_c['front'] = [L(blob([(-16, 60), (10, 50), (50, 50), (90, 50), (116, 60), (90, 66), (50, 62), (10, 66)], 6), 'under', 'b'),
               L(sharp(_W), 'mid', 'f'), L(blob([(64, 10), (104, 36), (112, 54), (92, 50), (76, 30)], 6), 'shade', 'f', False),
               strand([(50, 54), (45, 48), (50, 45), (55, 48), (50, 54)], 'deep', 'f', 1.2)] + _c['front'][1:]
_c['side'] = [L(sharp([(-14, 66, 1), (-8, 40), (14, 12), (50, 2), (80, 12), (94, 34), (96, 52, 1), (78, 48), (62, 54), (48, 50),
                       (34, 60), (16, 58), (2, 70, 1), (-2, 58)]), 'mid', 'b'),
              L(blob([(-10, 50), (10, 40), (30, 52), (10, 62)], 6), 'shade', 'b', False)]
_c['back'] = [L(sharp([(-20, 62, 1), (-10, 40), (12, 16), (50, 4), (88, 16), (110, 40), (120, 62, 1), (100, 66), (80, 74, 1),
                       (66, 72), (50, 78, 1), (34, 72), (20, 74, 1), (0, 66)]), 'mid', 'b'),
              L(blob([(62, 10), (104, 36), (112, 60), (86, 66), (74, 32)], 6), 'shade', 'b', False)]
_c['face']['hairline'] = (58, 54)
_c['face']['eyes'] = 'normal'
_c['pal']['iris'] = hx('#d4c040')

# Trace Combe de perfil: el flequillo cae en punta por delante de la cara (no una solapa cuadrada)
_c = CHARS[K + 'trace-combe']
_c['side'][2] = L(sharp([(52, 26), (84, 30), (93, 48), (90, 66, 1), (84, 58), (80, 78, 1), (72, 62), (64, 72, 1), (56, 56)]), 'mid', 'f')
# Ava: sin la mancha de sombra encima del moño de perfil
CHARS[K + 'ava-ehrenreich']['side'] = [l for l in CHARS[K + 'ava-ehrenreich']['side'] if not (l['c'] == 'shade' and len(l['s']) == 20)]

# Yarden Forsman: triángulo verde oscuro en lo alto del flequillo y cejas verdes en uve por encima de las gafas
_c = _fx('yarden-forsman')
_c['pal']['gb'] = hx('#4f6e44')
_c['front'].insert(2, L(blob([(34, 30), (50, 15), (66, 30), (58, 32), (50, 28), (42, 32)], 5), 'gb', 'b', False))
_c['side'].insert(2, L(blob([(62, 26), (74, 14), (84, 24), (78, 28), (70, 28)], 5), 'gb', 'b', False))
brows(_c, 'gb', thick=3.4, angry=True, dy=-5)

# Ouijane Boarden: un gran lazo negro en lo alto (no dos orejas de ratón redondas) y un mechón rosa por el lado izquierdo
_c = _fx('ouijane-boarden')
_c['pal'].update(bow=hx('#1f1e20'), bow_d=hx('#111012'), pk=hx('#d6a6b2'))
_lb = [L(blob([(48, 2), (34, -12), (16, -20), (8, -8), (14, 6), (30, 8)], 8), 'bow', 'b'),
       L(blob([(44, 2), (30, -6), (16, -12), (14, -4), (28, 4)], 6), 'bow_d', 'b', False)]
_knot = [L(ell(50, 0, 6.5, 6, 18), 'bow', 'f')]
_c['front'] = _lb + mirror_layers(_lb) + [l for i, l in enumerate(_c['front']) if i not in (0, 1, 6)] + _knot
_c['front'].insert(6, strand([(14, 34), (8, 56), (14, 78), (6, 100), (10, 120)], 'pk', 'b', 4.5))
_c['back'] = _lb + mirror_layers(_lb) + [l for i, l in enumerate(_c['back']) if i not in (0, 1, 4)] + _knot
_c['back'].append(strand([(86, 34), (92, 56), (86, 78), (94, 100), (90, 124)], 'pk', 'b', 4.5))
_c['side'] = [L(blob([(44, 2), (34, -14), (18, -18), (14, -4), (24, 6)], 8), 'bow', 'b'),
              L(blob([(44, 2), (52, -14), (66, -16), (66, -2), (54, 6)], 8), 'bow', 'b')] + _c['side'][1:] + [L(ell(44, 0, 5.5, 5.5, 16), 'bow', 'f')]

# Miriam Masheene: melena negra de mechones largos en punta que caen hasta los hombros enmarcando la cara (con raya al
# medio y un pico de flequillo entre los ojos), no una masa de pinchos alrededor de la cabeza
_c = _fx('miriam-masheene')
_c['front'][0] = L(sharp([(0, 114, 1), (6, 80), (4, 48), (12, 22), (28, 6), (44, 0), (56, 0), (72, 6), (88, 22), (96, 48), (94, 80),
                          (100, 114, 1), (88, 98), (84, 112, 1), (80, 82), (80, 60), (70, 48), (56, 54), (50, 76, 1), (44, 54), (30, 48),
                          (20, 60), (20, 82), (16, 112, 1), (12, 98)]), 'mid', 'b')
_c['front'] += [L(sharp([(16, 54), (26, 60), (24, 86), (16, 108, 1), (14, 80)]), 'mid', 'f'),
                L(sharp([(84, 54), (86, 80), (84, 108, 1), (76, 86), (74, 60)]), 'mid', 'f'),
                strand([(50, 4), (50, 40)], 'deep', 'b', 1.2)]

# Wendy Stitchilton: trenza larga que cae por delante del hombro izquierdo de la imagen y mechas moradas a los dos lados
_c = _fx('wendy-stitchilton')
_pur = [l for l in _c['front'] if l['c'] == 'pur']
_c['front'] = [l for i, l in enumerate(_c['front']) if i != 3] + mirror_layers(_pur) + beads([(4, 70), (-2, 92), (1, 112), (3, 126)], 5.6, 'mid', 'f', end='deep')
_c['back'] += beads([(92, 66), (96, 88), (93, 110), (91, 126)], 5.6, 'mid', 'b', end='deep')

# Cleara Sounds: dos rizos del flequillo que suben como cuernecillos sobre la frente
_c = _fx('cleara-sounds')
_horn = [L(sharp([(34, 60), (35, 48), (41, 36, 1), (44, 47), (43, 60)]), 'mid', 'f', ln=True),
         L(sharp([(38, 58), (39, 49), (41, 41, 1), (42, 50), (41, 58)]), 'deep', 'f', False)]
_c['front'] += _horn + mirror_layers(_horn)

# Inga Calmari: el pelo de debajo (patillas y nuca) es gris oscuro; el turquesa es solo la masa de arriba
_c = _fx('inga-calmari')
_c['pal']['low'] = hx('#484b4d')
_lo = [L(blob([(10, 52), (22, 52), (24, 78), (16, 84), (10, 74)], 6), 'low', 'b')]
_c['front'] = _lo + mirror_layers(_lo) + _c['front']
_c['side'].insert(2, L(blob([(4, 62), (34, 60), (48, 82), (28, 90), (6, 82)], 6), 'low', 'b'))
_c['back'].insert(2, L(blob([(8, 62), (50, 60), (92, 62), (88, 86), (50, 92), (12, 86)], 6), 'low', 'b'))


def flips(c, pts, views=('front', 'back'), z='b'):
    """Puntas de la melena vueltas hacia fuera (a los dos lados): pts es la de la izquierda de la imagen."""
    lf = [L(sharp(pts), 'mid', z)]
    for v in views:
        c[v][0:0] = lf + mirror_layers(lf)


# Puerita, Tally e Iza: la melena corta acaba con las puntas vueltas hacia fuera a la altura de la mandíbula
flips(_fx('puerita-cakeley'), [(6, 70), (-2, 86), (-16, 96, 1), (-2, 102), (14, 98), (20, 84)])
flips(_fx('tally-mcintosh'), [(6, 70), (-2, 88), (-16, 100, 1), (0, 104), (16, 99), (20, 82)])
flips(_fx('iza-improvelli'), [(0, 62), (-10, 82), (-22, 94, 1), (-6, 101), (10, 97), (16, 80)])

# Shawl Creedstern: las mechas doradas son medias lunas curvas, no rayas rectas
_c = _fx('shawl-creedstern')
_c['pal']['gold'] = hx('#9a8636')
_gl = L(blob([(36, 4), (27, 16), (29, 34), (32, 22), (39, 11)], 6), 'gold', 'b', False)
_gr = L(blob([(62, 6), (72, 14), (73, 30), (69, 20), (60, 12)], 6), 'gold', 'b', False)
_c['front'] = [l for l in _c['front'] if l['w'] == 0] [:2] + [_gl, _gr] + [l for l in _c['front'] if l['w'] == 0][2:]
_c['side'] = [l for l in _c['side'] if l['w'] == 0] + [L(blob([(40, 2), (32, 14), (34, 30), (37, 18), (44, 9)], 6), 'gold', 'b', False)]
_c['back'] = [l for l in _c['back'] if l['w'] == 0] + [dict(_gr, s=[(100 - x, y) for x, y in _gr['s']]), dict(_gl, s=[(100 - x, y) for x, y in _gl['s']])]

# Lysander Trimore: tirita sobre la ceja derecha de la imagen y ojos castaños con iris (no puntos negros)
_c = _fx('lysander-trimore')
_c['face']['eyes'] = 'normal'
_c['pal']['iris'] = hx('#9a6e3e')
_c['front'].append(L(blob([(58, 63), (75, 57), (78, 61), (61, 67)], 4), hx('#f2dcb8'), 'f', ln=True))
_c['side'].append(L(blob([(72, 61), (84, 58), (86, 62), (74, 65)], 4), hx('#f2dcb8'), 'f', ln=True))
CHARS[K + 'iza-improvelli']['face']['eyes'] = 'sharp'  # ojos grises entornados, no puntos
CHARS[K + 'iza-improvelli']['pal']['iris'] = hx('#6e7480')

# Miriam de perfil: melena lisa de mechones en punta hasta los hombros (no una bola de pinchos)
_c = CHARS[K + 'miriam-masheene']
_c['side'][0] = L(sharp([(52, 70), (54, 100, 1), (42, 92), (34, 110, 1), (26, 94), (14, 112, 1), (8, 92), (-2, 104, 1), (0, 70), (-2, 40),
                         (8, 16), (28, 0), (46, -4), (54, -16, 1), (60, -2), (76, 6), (90, 24), (94, 46, 1), (82, 40), (72, 52), (64, 46), (58, 56)]),
                  'mid', 'b')

# Blendon Frugel: cejas negras muy gruesas y pobladas
_c = _fx('blendon-frugel')
_c['front'] = [l for l in _c['front'] if not (l['w'] and l['c'] == OUT)]
_c['pal']['brow'] = hx('#3a2e30')
for _s in (1, -1):
    _cx = 50 - 15 * _s
    _c['front'].append(L(blob([(_cx - 11 * _s, 66), (_cx - 9 * _s, 60), (_cx + 2 * _s, 57), (_cx + 9 * _s, 60), (_cx + 10 * _s, 66), (_cx + 2 * _s, 63)], 5), 'brow', 'f', ln=True))
_c['face']['brows'] = False
_c['side'].append(L(blob([(70, 64), (74, 59), (84, 58), (88, 63), (80, 62)], 5), 'brow', 'f', ln=True))

# Pristin Florynce: coloretes melocotón (no rosas) y cejas rubias
_swap(_fx('pristin-florynce'), '#ee8c8c', '#f8c090')
brows(CHARS[K + 'pristin-florynce'], 'mid', thick=3.0, dy=-1)

# Hildy Tattleswell: ojos grandes y redondos violeta (no puntos negros) y la pinza marrón del lado izquierdo de la imagen
_c = _fx('hildy-tattleswell')
_c['face']['eyes'] = 'big'
_c['pal']['iris'] = hx('#6a4a8e')
_c['front'].insert(1, L(ell(6, 50, 6, 10, 20), hx('#8a7068'), 'b'))

# Minerva Elderbright: el flequillo recto se abre en medio (raya) y deja ver una rendija de frente
_c = _fx('minerva-elderbright')
_c['front'].append(L([(48, 42), (52, 42), (51.2, 55), (48.8, 55)], 'skin', 'f', False))
_c['front'].append(strand([(48, 42), (48.8, 55)], 'deep', 'f', 0.9))
_c['front'].append(strand([(52, 42), (51.2, 55)], 'deep', 'f', 0.9))

# Brenae Ackermann: ojos grandes azul claro (en espiral en el retrato), no puntos
_c = _fx('brenae-ackermann')
_c['face']['eyes'] = 'big'

# Frey Granzburn: la melena blanca tiene las sombras rosadas
col('frey-granzburn', shade='#d8bcc6', deep='#a88a96')

# Jeremy Yung y Niro Vannaburg: cejas grises gruesas
brows(_fx('jeremy-yung'), 'shade', thick=4.2, angry=True)
brows(_fx('niro-vannaburg'), 'mid', thick=4.0, dy=-1)

# Lumina: por debajo de la melena asoma la capa castaña (medida en el retrato y en el modelo 3D)
_swap(_fx('lumina'), '#a07a40', '#9c7a58')

# Jella Fisker: la media melena acaba en una franja morada ancha (de la mejilla para abajo), también de perfil
_c = _fx('jella-fisker')
_pb = [L(blob([(4, 66), (17, 63), (18, 92), (9, 95), (4, 88)], 6), hx('#8a6ac8'), 'b', False)]
_c['front'][2:2] = _pb + mirror_layers(_pb)
_c['side'].insert(2, L(blob([(-4, 66), (30, 64), (48, 70), (50, 92), (20, 96), (-2, 92)], 6), hx('#8a6ac8'), 'b', False))
_c['back'].insert(2, L(blob([(1, 66), (50, 64), (99, 66), (100, 98), (50, 102), (0, 98)], 6), hx('#8a6ac8'), 'b', False))
# (las franjas de color de debajo forman parte de la silueta del pelo: con contorno, sin salirse sueltas)
for _pid in ('lumina', 'jella-fisker'):
    for _v in ('side', 'back'):
        for _l in CHARS[K + _pid][_v]:
            if _l['c'] in (hx('#9c7a58'), hx('#8a6ac8')) and not _l['w']:
                _l['sil'] = True

# Mora Grimmoir: la melena larga acaba en las puntas vueltas hacia fuera a la altura de los hombros
flips(_fx('mora-grimmoir'), [(-4, 96), (-14, 112), (-28, 118, 1), (-12, 124), (4, 120), (8, 104)])

# Emil Tait y Galina Chilvers: cejas gruesas (azul marino oscuro / lavanda)
_c = _fx('emil-tait')
_c['pal']['brow'] = hx('#283850')
brows(_c, 'brow', thick=4.0, dy=-1)
brows(_fx('galina-chilvers'), 'shade', thick=4.6, dy=-1)

# Regis Tunesmith: cejas caqui mucho más grandes (gruesas y anchas)
_c = _fx('regis-tunesmith')
_c['front'] = [l for i, l in enumerate(_c['front']) if i not in (2, 3)]
for _s in (1, -1):
    _cx = 50 - 15 * _s
    _c['front'].append(L(blob([(_cx - 10 * _s, 66), (_cx - 8 * _s, 59), (_cx + 3 * _s, 57), (_cx + 9 * _s, 61), (_cx + 7 * _s, 66), (_cx - 1 * _s, 63)], 5), 'mid', 'f', ln=True))

# Krome Tallic: cejas en zigzag verde oscuro por encima de las gafas de sol
_c = _fx('krome-tallic')
_c['pal']['brow'] = hx('#1e3434')
for _s in (1, -1):
    _c['front'].append(strand([(50 - 5 * _s, 64), (50 - 11 * _s, 56), (50 - 17 * _s, 60), (50 - 25 * _s, 53)], 'brow', 'f', 2.6))
_c['side'].append(strand([(72, 60), (78, 54), (82, 57), (88, 52)], 'brow', 'f', 2.6))

# Livia Marsquall y Curia Caldwell: cejas gruesas del color del pelo
brows(_fx('livia-marsquall'), 'shade', thick=4.6, dy=-1)
brows(_fx('curia-caldwell'), 'shade', thick=5.0, dy=-1)
brows(CHARS[K + 'evander-greenvale'], 'brow', thick=4.4, angry=True)  # cejas verde oliva gruesas, como el pelo

# Zackory Wart: cejas castañas muy gruesas y fruncidas
brows(_fx('zackory-wart'), 'mid', thick=5.4, angry=True)

# Stratos Merrill: gafas de montura gruesa gris oscuro (no solo los cristales) y cejas azules arqueadas
_c = _fx('stratos-merrill')
_swap(_c, '#1e1a1e', 'mid')
for _v in ('front', 'side'):
    for _l in [l for l in _c[_v] if l['c'] == hx('#a8c0d0')]:
        _c[_v].append(L(_l['s'] + [_l['s'][0]], hx('#3a4048'), 'f', False, w=3.6))
_c['front'].append(strand([(48, 74), (52, 74)], hx('#3a4048'), 'f', 2.4))

# Mika Upton: sombra de ojos morada (no amarilla) y cejas rosas
_swap(_fx('mika-upton'), '#e0c040', '#a070b8')
brows(CHARS[K + 'mika-upton'], 'shade', thick=2.8, dy=-3)

# Cyrus Veil y Eli Hoopsen: cejas gruesas (verde lima / casi negras)
brows(_fx('cyrus-veil'), 'mid', thick=4.4, dy=-1)
brows(_fx('eli-hoopsen'), 'deep', thick=4.6, angry=True)

# Godfrey Shahmann: los lados y la nuca casi negros (verde oliva muy oscuro); el caqui es solo el tupé de arriba
_c = _fx('godfrey-shahmann')
_c['pal'].update(side=hx('#33352a'), side_d=hx('#25271f'))
_c['front'][0]['c'] = 'side'
_c['front'][1]['c'] = 'side_d'
_c['front'].insert(2, L(blob([(30, 46), (24, 20), (36, 4), (50, 0), (64, 4), (76, 20), (70, 46), (58, 30), (50, 40), (42, 30)], 8), 'mid', 'b', False, ln=True))
_c['front'].insert(3, L(blob([(52, 6), (66, 10), (72, 26), (66, 38), (60, 22)], 6), 'shade', 'b', False))
_c['side'][0]['c'] = 'side'
_c['side'][1]['c'] = 'side_d'
_c['side'].insert(2, L(blob([(30, 10), (52, -2), (76, 6), (90, 26), (76, 30), (56, 24), (36, 28)], 8), 'mid', 'b', False, ln=True))
for _l in _c['back'][:2]:  # (la coleta, que va al final, es caqui como el tupé)
    if _l['c'] in ('mid', 'shade'):
        _l['c'] = 'side' if _l['c'] == 'mid' else 'side_d'
_c['back'].insert(2, L(blob([(30, 34), (24, 12), (50, 0), (76, 12), (70, 34), (50, 28)], 8), 'mid', 'b', False, ln=True))

# Niles Gawkerson: los rizos de los lados bajo la melena son dorados, no azul claro
CHARS[K + 'niles-gawkerson']['pal']['light'] = hx('#e8a62c')

# Ricemond Chowen: cejas gruesas castaño rojizo como el pelo (no rayas negras)
_c = _fx('ricemond-chowen')
for _v in ('front', 'side'):
    for _l in _c[_v]:
        if _l['w'] == 3.0:
            _l['c'] = 'shade'
            _l['w'] = 4.2

# Naya Prism y Eamon Cattrall: cejas gruesas verdes (del color del pelo)
brows(_fx('naya-prism'), 'shade', thick=4.0, angry=True)
brows(_fx('eamon-cattrall'), 'mid', thick=3.6, dy=-1)
# Margo Versier: mechones rojos claros en el flequillo y los pasadores verde azulado junto a las sienes
_c = _fx('margo-versier')
for _x in (40, 48, 56):
    _c['front'].append(strand([(_x + 2, 34), (_x - 2, 56)], 'light', 'f', 2.8))
_c['front'] += [L(blob([(14, 74), (19, 72), (19, 80), (14, 80)], 4), hx('#2e7880'), 'f', ln=True),
                L(blob([(86, 74), (81, 72), (81, 80), (86, 80)], 4), hx('#2e7880'), 'f', ln=True)]

# Colm Dawdlin: gafas rectangulares con la montura negra gruesa por arriba
_c = _fx('colm-dawdlin')
for _l in [l for l in _c['front'] if l['c'] == hx('#f4f4f6')]:
    _xs = [p[0] for p in _l['s']]; _ys = [p[1] for p in _l['s']]
    _c['front'].insert(_c['front'].index(_l) + 1, strand([(min(_xs), min(_ys) + 0.5), (max(_xs), min(_ys) + 0.5)], hx('#1e1a1e'), 'f', 2.8))
_c['side'].append(strand([(70, 69.5), (90, 69.5)], hx('#1e1a1e'), 'f', 2.8))

# Leston Thoreau: cejas grises gruesas fruncidas y patillas grises que bajan hasta la mandíbula
_c = _fx('leston-thoreau')
brows(_c, 'shade', thick=4.4, angry=True)
_sb = [L(blob([(15, 74), (21, 74), (24, 94), (32, 102), (22, 100), (15, 90)], 6), 'mid', 'f', ln=True)]
_c['front'] += _sb + mirror_layers(_sb)
_c['side'].append(L(blob([(44, 74), (52, 74), (58, 94), (66, 102), (54, 100), (46, 90)], 6), 'mid', 'f', ln=True))

# Tessa Rapperton: cejas oscuras gruesas
brows(_fx('tessa-rapperton'), 'deep', thick=3.8, angry=True)

# Calina Breezer y Hernan Rippett: cejas gruesas del color del pelo; Hernan con ojos grises entornados, no puntos
brows(_fx('calina-breezer'), 'shade', thick=4.6, dy=-1)
_c = _fx('hernan-rippett')
_c['face']['eyes'] = 'sharp'
_c['pal']['iris'] = hx('#8a8e98')
brows(_c, 'shade', thick=4.4, angry=True)
# Yarden: el pelo baja hasta las cejas (el nacimiento del pelo quedaba muy alto y se veía una caja de frente)
CHARS[K + 'yarden-forsman']['face']['hairline'] = [(19.55, 104), (16, 54), (50, 50), (84, 54), (80.45, 104)]

# Sten Fanborough, Ignacio Gerhardt y Montgomery Marchand: cejas gruesas (castaño / pardo oscuro / casi negras)
brows(_fx('sten-fanborough'), 'shade', thick=5.0, angry=True)
_c = _fx('ignacio-gerhardt')
_c['pal']['brow'] = hx('#3d342e')
brows(_c, 'brow', thick=5.0, angry=True)
brows(_fx('montgomery-marchand'), 'deep', thick=5.0, angry=True)
# Montgomery: la cinta blanca de la frente es ancha (de las sienes a las cejas) y el pelo negro cae por encima en dos mechones
_c = CHARS[K + 'montgomery-marchand']
_c['front'][2] = L(blob([(4, 40), (50, 28), (96, 40), (95, 58), (50, 50), (5, 58)], 8), hx('#f8f8f8'), 'f', True)
_c['front'].insert(3, strand([(50, 30), (38, 32), (34, 44)], 'mid', 'f', 3.2))
_c['front'].insert(4, strand([(50, 30), (62, 32), (66, 44)], 'mid', 'f', 3.2))
_c['face']['hairline'] = [(19.55, 104), (16, 58), (50, 52), (84, 58), (80.45, 104)]

# Tenison Onsera: ojos azul claro grandes tras las gafas (no puntos negros)
_c = _fx('tenison-onsera')
_c['face']['eyes'] = 'normal'
_c['pal']['iris'] = hx('#5a98c0')
# Chaunce Gambell y Smiles Thrussell: cejas gruesas oscuras fruncidas
_c = _fx('chaunce-gambell')
_c['pal']['brow'] = hx('#4a3a3a')
brows(_c, 'brow', thick=4.4, angry=True)
brows(_fx('smiles-thrussell'), 'deep', thick=4.4, angry=True)

# Willem Durrmore: sombra del pelo crema cálida (no gris) y cejas blancas gruesas
col('willem-durrmore', shade='#e2d4a6', deep='#b8a478')
brows(CHARS[K + 'willem-durrmore'], 'light', thick=5.0)
# Miriam de espaldas: la misma melena de mechones en punta hasta los hombros
_c = CHARS[K + 'miriam-masheene']
_c['back'][0] = L(sharp([(0, 114, 1), (6, 80), (2, 46), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (98, 46), (94, 80), (100, 114, 1),
                         (86, 100), (78, 116, 1), (68, 100), (58, 118, 1), (50, 102), (42, 118, 1), (32, 100), (22, 116, 1), (14, 100)]), 'mid', 'b')
