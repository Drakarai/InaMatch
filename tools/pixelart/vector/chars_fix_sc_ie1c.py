"""Correcciones de la revisión de diseños (grupo sc_ie1c): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401

from heads import L, ell, blob  # noqa: E402

K = 'scouts-ie1:'
OUTC = (60, 24, 16, 255)


def _tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def _recolor(obj, old, new):
    """Cambia en las capas los colores literales iguales a la piel antigua."""
    if isinstance(obj, list):
        return [_recolor(o, old, new) for o in obj]
    if isinstance(obj, dict):
        return {k: (new.get(v, v) if k == 'c' and isinstance(v, tuple) else _recolor(v, old, new)) for k, v in obj.items()}
    return obj


# Piel: los retratos de Victory Road salen del modelo 3D (mismos colores planos), así que el tono de piel de cada
# ojeador es el de su retrato (muchos estaban dibujados con una piel clara rosada o con otro tono que no era el suyo).
SKIN = {
    'ben-delimms': (169, 133, 101),
    'bennett-byers': (245, 186, 114),
    'bill-looney': (242, 181, 108),
    'bill-mumm': (241, 179, 108),
    'bill-tardy': (206, 145, 73),
    'bo-ling': (242, 180, 108),
    'bob-baggum': (242, 180, 108),
    'bob-shishker': (242, 180, 108),
    'bob-stretcher': (242, 180, 108),
    'bobby-constable': (169, 134, 100),
    'bobby-peel': (241, 180, 108),
    'brendan-branch': (198, 153, 90),
    'brian-presser': (242, 180, 107),
    'brock-twigg': (250, 213, 157),
    'buck-teachey': (242, 180, 108),
    'cal-emarry': (242, 180, 108),
    'callan-trens': (242, 180, 108),
    'cam-vass': (243, 179, 108),
    'cameron-hameha': (238, 180, 110),
    'casey-novak': (242, 180, 107),
    'cass-crocker': (198, 153, 89),
    'ches-gnashers-nutcracker': (204, 146, 75),
    'creed-wrighter': (242, 180, 107),
    'dan-castella': (197, 150, 91),
    'fontaine-tapper': (251, 177, 105),
    'frank-drake': (242, 180, 108),
    'frank-koshar': (242, 180, 108),
    'fred-ferrel': (242, 180, 108),
    'gary-salmon': (242, 180, 108),
    'gil-rivers': (241, 180, 108),
    'glen-garry': (242, 180, 107),
    'grew-driver': (241, 180, 108),
    'gwyn-penn': (242, 180, 108),
    'haden-seek': (170, 134, 98),
    'hale-quinn': (242, 180, 108),
    'hans-bigger': (251, 177, 102),
    'heath-rower': (241, 180, 108),
    'hike-basher': (250, 175, 101),
    'isaac-goss': (242, 180, 108),
    'isaiah-shutt': (245, 177, 109),
    'jack-nimble': (238, 180, 114),
    'jack-trades-tradesman': (241, 180, 108),
    'jay-archer': (211, 153, 76),
    'jay-pan': (250, 213, 157),
    'jebb-ettow': (197, 153, 89),
    'joe-nalist': (241, 179, 107),
    'joe-stick': (243, 181, 107),
    'john-demi': (241, 180, 108),
    'kurt-o-graphy': (242, 180, 107),
    'kurt-price': (242, 180, 108),
    'lance-lotts': (205, 146, 74),
    'lee-figreene': (250, 214, 157),
    'leon-lawn': (206, 146, 73),
    'les-tarrant': (242, 180, 108),
    'lon-grainger': (198, 153, 89),
    'lou-beigh': (252, 187, 123),
    'loughrey-mose': (205, 146, 74),
    'luke-o-cyte': (206, 146, 73),
    'luther-rio': (205, 146, 74),
    'marc-o-lepsy': (203, 147, 76),
    'nathan-weyton': (205, 146, 74),
    'nev-erin': (242, 180, 108),
    'neville-list': (242, 180, 108),
    'page-helper': (205, 146, 74),
    'pascal-blaise': (250, 213, 155),
    'paul-chucker': (242, 180, 107),
    'paul-sapp': (253, 213, 154),
    'perry-pincher': (242, 180, 114),
    'pete-legume': (251, 177, 105),
    'phil-dippedes': (242, 180, 108),
    'pip-goodweather': (206, 146, 73),
    'quentin-quartz': (242, 180, 108),
    'rich-cave': (238, 180, 108),
    'ron-away': (242, 180, 108),
    'ronny-o-mania': (205, 146, 74),
    'sagaminator-saggy': (252, 188, 123),
    'sam-aritan': (205, 146, 74),
    'sayer-lemon': (241, 179, 110),
    'scout-messenger': (230, 184, 122),
    'shep-shank': (250, 213, 157),
    'sly-o-hands': (242, 180, 108),
    'sly-winker': (205, 146, 74),
    'sol-stiss': (205, 146, 74),
    'solomon-justice': (242, 180, 109),
    'solomon-osaka': (242, 180, 108),
    'sonny-rentman': (204, 147, 69),
    'spike-pitt': (250, 178, 106),
    'spike-thorne': (241, 179, 110),
    'stu-helmsley': (205, 146, 74),
    'ted-fast': (206, 146, 73),
    'tex-curvator': (242, 180, 108),
    'thor-toise': (241, 179, 105),
    'tim-mittus': (242, 180, 107),
    'tony-hacker': (242, 179, 114),
    'travis-mcclean': (242, 180, 108),
    'victor-grand': (222, 210, 189),
    'vinny-trioquist': (242, 181, 108),
    'walter-walken': (205, 146, 73),
}
SKIN['mark-sudor'] = (205, 148, 74)  # cara de gorila: la piel del hocico, no el pelo verde oliva

for _id, _s in SKIN.items():
    _c = copy.deepcopy(CHARS[K + _id])
    _p = _c['pal']
    _old_s, _old_d = _p['skin'], _p['skin_d']
    _p['skin'] = tuple(_s) + (255,)
    _p['skin_d'] = _tone(_s, 0.86)
    _m = {_old_s: _p['skin'], _old_d: _p['skin_d']}
    for _v in ('front', 'side', 'back'):
        _c[_v] = _recolor(_c[_v], None, _m)
    CHARS[K + _id] = _c


def _fix(pid, **face):
    c = copy.deepcopy(CHARS[K + pid])
    c['face'].update(face)
    CHARS[K + pid] = c
    return c


# Ojos: en el retrato tienen ojos con blanco y pupila (afilados, con mala cara), no dos puntitos que se pierden
_fix('tom-stevenson', eyes='sharp', brows='angry')
_fix('albert-wister', eyes='sharp')
_fix('adam-nesiac', eyes='sharp')
_fix('clark-watcher', eyes='sharp', brows='angry')
_fix('tiny-forester', eyes='sharp')
# Bill Looney: sonrisa torcida de medio lado (no estaba dibujada la boca)
_fix('bill-looney', mouth='smile', mouth_y=97)
# Marc O'Lepsy: bocaza de labios gruesos marrones de lado a lado de la cara
_c = _fix('marc-o-lepsy', mouth='none')
_c['front'] = _c['front'] + [L(ell(50, 96, 17, 6), (150, 92, 58, 255), 'f', False, True),
                             L([(36, 96), (50, 97), (64, 96)], OUTC, 'f', False, False, 1.4)]
# Doug Walker: muy despejado; el pelo lila rapado solo queda en lo alto de la coronilla y en las sienes
_c = _fix('doug-walker', hairline=[(14, 56), (17, 40), (24, 26), (32, 22), (40, 16), (50, 14), (60, 16), (68, 22), (76, 26), (83, 40), (86, 56)],
          face_front=blob([(16, 50), (22, 26), (50, 12), (78, 26), (84, 50), (90, 78), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (10, 78)]))
