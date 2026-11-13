"""Correcciones de la revisión de diseños (grupo sc_ie3b): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de IE3 (scouts-ie3), segunda mitad: comparados con su retrato de Victory Road."""
import copy  # noqa: F401
from chars import CHARS, L, blob, ell, outline, strand  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, hl
from chars_scouts_ie2_04 import lashes, lash_side
from chars_scouts_ie3_05 import TUR, TURD
from chars_scouts_ie3_06 import band as band6
from heads import quad

K = 'scouts-ie3:'
WHITE = (250, 250, 250, 255)


def _get(pid):
    return copy.deepcopy(CHARS[K + pid])


def _flat(layers):
    return [l for it in layers for l in (it if isinstance(it, list) else [it])]


def _drop(layers, col):
    return [l for l in _flat(layers) if l['c'] != col]


# Olivia Palme: el pañuelo amarillo no es una cinta fina: le tapa la cabeza desde la frente hasta media coronilla y se ata
# arriba en un lazo grande de dos orejas
c = _get('olivia-palme')
YB_OLD = _c('#e9c157')
SC, SCD = _c('#ecb22e'), _c('#c98a1c')
c['front'] = _drop(c['front'], YB_OLD) + [
    L(outline([(12, 54), (12, 34), (26, 18), (50, 12), (74, 18), (88, 34), (88, 54), (70, 48), (50, 46), (30, 48)]), SC, 'f', True, True),
    L(quad((16, 40), (50, 26), (84, 40)), SCD, 'f', False, False, 1.4),
    L(outline([(48, 16), (34, 2), (18, -8, 1), (26, 8), (40, 20)]), SC, 'f', True, True),
    L(outline([(52, 16), (66, 0), (86, -10, 1), (78, 8), (60, 20)]), SC, 'f', True, True),
    L(ell(50, 16, 6, 5), SCD, 'f', True, True)]
c['side'] = _drop(c['side'], YB_OLD) + [
    L(outline([(8, 50), (10, 28), (30, 10), (56, 6), (80, 16), (90, 36), (86, 50), (60, 42), (30, 44)]), SC, 'f', True, True),
    L(outline([(52, 8), (44, -6), (36, -14, 1), (44, 0)]), SC, 'f', True, True), L(ell(52, 8, 5, 4), SCD, 'f', True, True)]
c['back'] = _drop(c['back'], YB_OLD) + [
    L(outline([(10, 52), (12, 30), (28, 14), (50, 10), (72, 14), (88, 30), (90, 52), (50, 58)]), SC, 'f', True, True),
    L(quad((14, 40), (50, 30), (86, 40)), SCD, 'f', False, False, 1.4)]
CHARS[K + 'olivia-palme'] = c

# Riku Ryu (retrato de DS): pelo castaño liso, no en bultos: raya en medio, flequillo de mechones que llega a las cejas y
# los lados lisos tapando las orejas
c = _get('riku-ryu')
c['face']['hairline'] = hl(5, 66, 55, 63, lean=-1.5, jit=2.5, seed=12)
c['front'] = dome('front', top=4, w=48, cy=46, sb=86) + [L(outline([(18, 44), (50, 36), (82, 44), (82, 68), (18, 68)]), 'mid', 'b', False),
                                                        strand([(50, 6), (48, 34)], 'deep', 'b', 1.2)]
c['side'] = dome('side', top=4, w=48, cy=46, nape=92, fr=58)
c['back'] = dome('back', top=4, w=48, cy=46, nape=92) + [strand([(50, 8), (50, 80)], 'deep', 'b', 1.2)]
CHARS[K + 'riku-ryu'] = c

# Risako Sugaya (retrato de DS): el flequillo recto le llega hasta las cejas
c = _get('risako-rishako-sugaya')
c['face']['hairline'] = [(6, 70), (14, 66), (30, 66), (50, 67), (70, 66), (86, 66), (94, 70)]
c['front'] = _flat(c['front']) + [L(outline([(16, 44), (24, 26), (50, 18), (76, 26), (84, 44), (82, 66), (50, 67), (18, 66)]), 'mid', 'b', False),
                                  strand([(34, 40), (32, 66)], 'shade', 'b', 1.0), strand([(50, 38), (50, 66)], 'shade', 'b', 1.0),
                                  strand([(66, 40), (68, 66)], 'shade', 'b', 1.0)]
CHARS[K + 'risako-rishako-sugaya'] = c

# Yurina Kumai: flequillo ladeado que le cae por la frente hasta los ojos (raya un poco a su izquierda)
c = _get('yurina-kumai')
c['front'] = _flat(c['front']) + [
    L(outline([(60, 36), (44, 40), (30, 50), (22, 70, 1), (34, 60), (44, 58), (50, 66, 1), (54, 54), (62, 60, 1), (64, 46)]), 'mid', 'f', True, True),
    strand([(56, 40), (40, 50), (30, 64)], 'shade', 'f', 1.0)]
CHARS[K + 'yurina-kumai'] = c

# Yuta Kitajima (retrato de DS): pelo corto y pegado, no un afro: masa casi lisa con ondas suaves y patillas cortas
c = _get('yuta-kitajima')
c['face']['hairline'] = hl(5, 62, 53, 57, lean=-1, jit=1.5, seed=71)
c['front'] = dome('front', top=8, w=47, cy=46, n=9, amp=2.5, soft=True, seed=72, sb=64) + [L(outline([(20, 46), (50, 40), (80, 46), (80, 60), (20, 60)]), 'mid', 'b', False)]
c['side'] = dome('side', top=8, w=47, cy=46, n=9, amp=2.5, soft=True, seed=72, nape=82, fr=52)
c['back'] = dome('back', top=8, w=47, cy=46, n=9, amp=2.5, soft=True, seed=72, nape=82)
CHARS[K + 'yuta-kitajima'] = c

# Stu Stewpot Potter: la cinta azul marino es mucho más ancha (de las cejas a casi la coronilla) y el óvalo rojo, más alto
NAV, RD = _c('#2c2840'), _c('#c8302a')
c = _get('stu-stewpot-potter')
keep = lambda ls: [l for l in _flat(ls) if l['c'] not in (NAV, RD)]  # noqa: E731
c['front'] = keep(c['front']) + [band6('front', NAV, 20, 34, w=46, dip=6), L(ell(50, 36, 6.5, 7), RD, 'f', True, True),
                                 L([(44, 34), (56, 34)], NAV, 'f', False, False, 1.4), L([(44.5, 38.5), (55.5, 38.5)], NAV, 'f', False, False, 1.4)]
c['side'] = keep(c['side']) + [band6('side', NAV, 18, 32)]
c['back'] = keep(c['back']) + [band6('back', NAV, 18, 32, dip=6)]
CHARS[K + 'stu-stewpot-potter'] = c

# Demerara Kane: frente muy alta (el pelo oliva solo asoma por los lados de la coronilla) y ojos azules de pestañas, no
# puntitos
c = _get('demerara-kane')
f = c['face']
f['face_front'] = face(w=8, chin=104, jaw=6, top=-4)
f['hairline'] = [(6, 62), (14, 44), (26, 30), (40, 24), (50, 26), (60, 24), (74, 30), (86, 44), (94, 62)]
f['eyes'] = 'normal'
c['pal']['iris'] = _c('#4a6a8a')
c['front'] = _flat(c['front']) + lashes(75)
c['side'] = _flat(c['side']) + lash_side(75)
CHARS[K + 'demerara-kane'] = c

# Sahara Kalahari: el turbante le baja por la izquierda (lado del espectador) tapándole ese ojo; se le ve el otro, con el
# mechón oscuro por fuera, junto a la sien
c = _get('sahara-kalahari')
fr_ = _flat(c['front'])
strand_layer = [l for l in fr_ if l['c'] == 'mid' and l['z'] == 'f']
rest = [l for l in fr_ if l not in strand_layer]
c['front'] = rest + [L(outline([(74, 60), (82, 72), (82, 96), (76, 110, 1), (74, 88), (72, 70)]), 'mid', 'f'),
                     L(outline([(12, 48), (36, 42), (56, 50), (56, 66), (48, 82), (30, 88), (14, 84), (10, 66)]), TUR, 'f'),
                     L(quad((14, 68), (34, 60), (54, 62)), TURD, 'f', False, False, 1.2)]
CHARS[K + 'sahara-kalahari'] = c

# Miyabi Natsuyaki: la diadema es ancha, a rayas azul marino y blancas
c = _get('miyabi-miiya-natsuyaki')
STRB = _c('#2a2a4a')
def _stripes(p0, cc, p1, w=8.0):
    off = w * 0.22
    return [L(quad(p0, cc, p1), STRB, 'f', False, False, w),
            L(quad((p0[0], p0[1] - off), (cc[0], cc[1] - off), (p1[0], p1[1] - off)), WHITE, 'f', False, False, w * 0.2),
            L(quad((p0[0], p0[1] + off), (cc[0], cc[1] + off), (p1[0], p1[1] + off)), WHITE, 'f', False, False, w * 0.2)]
c['front'] = [l for l in _flat(c['front']) if l['c'] not in (STRB, WHITE)] + _stripes((12, 34), (50, 6), (88, 34))
c['side'] = [l for l in _flat(c['side']) if l['c'] != STRB] + _stripes((10, 26), (50, 2), (90, 30))
c['back'] = [l for l in _flat(c['back']) if l['c'] != STRB] + _stripes((8, 32), (50, 6), (92, 32))
CHARS[K + 'miyabi-miiya-natsuyaki'] = c

# Onslow Mastick: el pelo rosa es una nube de bultos redondos (dos grandes a los lados, altos, y un copete abultado en medio
# que baja a la frente), no una forma de esquinas en punta
c = _get('onslow-mastick')
c['front'] = [L(outline([(6, 66), (4, 40), (20, 30), (80, 30), (96, 40), (94, 66), (80, 56), (20, 56)])),
              L(ell(22, 20, 21, 22)), L(ell(78, 20, 21, 22)), L(ell(50, 12, 18, 14)),
              L(ell(18, 12, 5, 3.5), 'light', 'b', False), L(ell(72, 10, 5, 3.5), 'light', 'b', False),
              L(blob([(32, 42), (36, 26), (50, 20), (64, 26), (68, 42), (60, 54), (50, 58), (40, 54)], 8), 'mid', 'f', True, True),
              L(ell(44, 30, 5, 3.5), 'light', 'f', False)]
c['face']['hairline'] = [(6, 62), (14, 54), (30, 56), (40, 50), (50, 58), (60, 50), (70, 56), (86, 54), (94, 62)]
c['side'] = [L(outline([(54, 60), (62, 48), (80, 46), (90, 34), (80, 26), (20, 24), (4, 40), (6, 60), (22, 74), (40, 72), (48, 64)])),
             L(ell(30, 18, 26, 22)), L(ell(62, 12, 20, 15)), L(ell(26, 12, 5, 3.5), 'light', 'b', False),
             L(blob([(64, 46), (66, 30), (78, 24), (90, 32), (90, 44), (80, 52)], 8), 'mid', 'f', True, True), L(ell(76, 32, 4, 3), 'light', 'f', False)]
c['back'] = [L(outline([(6, 76), (4, 40), (20, 30), (80, 30), (96, 40), (94, 76), (50, 84)])),
             L(ell(22, 20, 21, 22)), L(ell(78, 20, 21, 22)), L(ell(50, 12, 18, 14)),
             L(ell(24, 12, 5, 3.5), 'light', 'b', False)]
CHARS[K + 'onslow-mastick'] = c

# Mark Brand: de perfil y de espaldas también se ve la cresta morada con sus rayas oscuras, y de perfil la frente pintada
# de rayas negras tribales y la visera verde que le envuelve la cabeza
BLK = (24, 18, 20, 255)
VIS2 = _c('#2d4d37')
c = _get('mark-brand')
c['side'] = _flat(c['side']) + [
    strand([(34, 4), (16, 30), (8, 70), (18, 100)], 'shade', 'f', 1.4), strand([(46, 8), (30, 34), (24, 72), (30, 96)], 'shade', 'f', 1.4),
    L(outline([(62, 26), (70, 18), (76, 30), (70, 52), (64, 56)]), BLK, 'f', False),
    L(outline([(78, 34), (84, 36), (82, 54), (78, 56)]), BLK, 'f', False),
    L(outline([(30, 60), (62, 58), (62, 70), (30, 72)]), VIS2, 'f')]
c['back'] = _flat(c['back']) + [
    strand([(50, 6), (50, 104)], 'deep', 'f', 1.4), strand([(40, 8), (32, 50), (30, 102)], 'shade', 'f', 1.3),
    strand([(60, 8), (68, 50), (70, 102)], 'shade', 'f', 1.3),
    L(outline([(10, 60), (90, 60), (90, 70), (10, 70)]), VIS2, 'b')]
CHARS[K + 'mark-brand'] = c

# Roy Ellway: la gorra granate puesta del revés asoma más (la copa le cubre el lado izquierdo de la cabeza) y la cinta
# amarilla de detrás se ve en arco por arriba, a su derecha
CAPR, CAPY = _c('#7a2414'), _c('#e0b040')
c = _get('roy-ellway')
fr_ = _flat(c['front'])
c['front'] = [
    L(blob([(4, 36), (14, 8), (40, -4), (70, -6), (92, 6), (98, 26), (90, 40), (10, 44)], 5), CAPR),
    L(blob([(44, -6), (70, -8), (92, 4), (100, 22), (90, 26), (66, 8)], 4), CAPY, 'b')] + \
    [l for l in fr_ if l['c'] not in (CAPR, CAPY)] + [
    L(blob([(-4, 36), (0, 10), (18, -6), (40, -8), (38, 6), (22, 18), (8, 38)], 5), CAPR, 'f'),
    L(quad((-2, 34), (8, 10), (30, -6)), _c('#a03a24'), 'f', False, False, 1.4)]
CHARS[K + 'roy-ellway'] = c

# Lucien Brightside: tupé alto peinado hacia arriba y atrás que forma una ola que se riza hacia su izquierda, con los lados
# más cortos y pegados; frente despejada
c = _get('lucien-brightside')
c['face']['hairline'] = [(6, 66), (14, 54), (26, 48), (44, 46), (60, 45), (76, 48), (86, 54), (94, 66)]
c['front'] = [
    L(outline([(12, 72), (9, 50), (10, 28), (18, 10), (30, -2), (46, -8), (62, -10), (78, -4), (90, 10), (93, 30), (91, 50), (88, 72), (82, 56), (18, 56)])),
    L(outline([(62, -8), (78, -2), (89, 12), (91, 32), (89, 56), (82, 46), (78, 24), (68, 6)]), 'shade', 'b', False),
    L(outline([(14, 56), (12, 40), (16, 30), (22, 48), (22, 60)]), 'shade', 'b', False),
    strand([(24, 42), (26, 20), (40, 4), (60, -4)], 'shade', 'b', 1.4), strand([(38, 44), (42, 22), (56, 8), (76, 4)], 'shade', 'b', 1.4),
    strand([(54, 44), (60, 26), (74, 16), (86, 18)], 'shade', 'b', 1.3),
    L(quad((56, 24), (46, -2), (70, 8)), 'deep', 'b', False, False, 1.6),
    strand([(16, 52), (18, 36)], 'shade', 'b', 1.0), strand([(84, 52), (82, 36)], 'shade', 'b', 1.0)]
c['side'] = [
    L(outline([(56, 62), (64, 48), (80, 44), (92, 30), (94, 10), (82, -6), (60, -14), (34, -8), (14, 6), (4, 26), (4, 54), (16, 78), (34, 78), (46, 64)])),
    strand([(40, -2), (66, 0), (90, 14)], 'shade', 'b', 1.4), strand([(18, 18), (48, 14), (84, 30)], 'shade', 'b', 1.4),
    strand([(10, 40), (40, 34), (62, 46)], 'shade', 'b', 1.2)]
CHARS[K + 'lucien-brightside'] = c


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
    'miyabi-miiya-natsuyaki': '#fedfc0',
    'laititia-cheeseman': '#f6be92',
    'titania-wraps-khamun': '#c99970',
    'lacy-cagney': '#f7be92',
    'pomponius-fanfair': '#fbbc7b',
    'sunil-ra-rahman': '#cf9768',
    'leighton-bolt': '#b7743a',
    'grover-noggin': '#fed189',
    'justice-gavel': '#fcbc79',
    'judge-justice-jury': '#dda357',
    'stackem-skyhigh': '#fbbc7b',
    'michael-wacko-shako': '#fbbc7d',
    'indira-patil': '#dea255',
    'al-opino': '#ae8b72',
    'keshia-readingplace': '#fccf9e',
    'gail-ellement': '#feeab8',
    'aaron-dainty-gossamer': '#feebb8',
    'theron-shuriken-starr': '#fbbc7a',
    'chucky-discard-cardaway': '#fbbc7b',
    'bella-baker': '#fad8b7',
    'susan-taylor': '#fcbc7b',
    'jeanie-tajine-tanner': '#b87238',
    'snowy-bergman': '#dea256',
    'noel-taurius': '#b08c73',
    'walt-whittler': '#af8c73',
    'colin-commando-mando': '#f5be93',
    'nifty-trials-throttler': '#ce966b',
    'kev-keffiyeh-fiyah': '#b8733a',
    'tia-t-quoise-cruz': '#fcbc7d',
    'virginia-virgo-goldstein': '#fed09f',
    'chauncey-slinka': '#e6cdad',
}
for _p, _h in _SKIN2.items():
    _sk_reskin('scouts-ie3:' + _p, _h)
