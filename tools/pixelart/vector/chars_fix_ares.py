"""Correcciones de la revisión de diseños (grupo ares): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, ell, hexc, outline, pal, strand, tone, mix  # noqa: E402,F401
from heads import blob, quad, spk  # noqa: E402,F401


def hair(c, shade=None, deep=None, light=None):
    """Tonos del pelo (mid, shade, deep, light) a partir del color medio, como pal()."""
    h = hexc(c)
    out = {'mid': h, 'shade': hexc(shade) if shade else tone(h, 0.78), 'deep': hexc(deep) if deep else tone(h, 0.6),
           'light': hexc(light) if light else mix(h, (255, 255, 255), 0.38)}
    return out


def _fix(team, pid, base=None, **kw):
    """Copia el dibujo actual del jugador (o el de 'base') a la clave del equipo y le cambia lo que se pase."""
    if base is None:  # el dibujo que usa ahora export.key_for: el del equipo, el de la temporada o el suyo
        base = next(k for k in (f'{team}:{pid}', f"{team.split('-')[0]}:{pid}", pid) if k in CHARS)
    c = copy.deepcopy(CHARS[base])
    for k, v in kw.items():
        if k == 'pal_upd':
            c['pal'].update(v)
        elif k == 'face_upd':
            c.setdefault('face', {}).update(v)
        else:
            c[k] = v
    CHARS[f'{team}:{pid}'] = c
    return c


def _cloud(cx, cy, rx, ry, n=8, a0=0.0, k=0.8):
    """Nube de rizos: bultos redondos alrededor de un centro."""
    import math
    pts = [(cx + rx * (1.0 if i % 2 == 0 else k) * math.cos(a0 + math.pi * i / n), cy + ry * (1.0 if i % 2 == 0 else k) * math.sin(a0 + math.pi * i / n))
           for i in range(n * 2)]
    return blob(pts, 6)


def guarded(fn):
    """Cada bloque de correcciones va protegido: si falla, avisa y no rompe la carga de chars para nadie."""
    try:
        fn()
    except Exception as e:  # noqa: BLE001
        import sys
        print(f'chars_fix_ares: {fn.__name__} falló: {e!r}', file=sys.stderr)
    return fn


# ---------------------------------------------------------------- Outei Tsukinomiya
@guarded
def outei():
    # Lucas Star (Ichihoshi Hikaru): el pelo es azul marino oscuro, no azul eléctrico
    _fix('ares-outei-tsukinomiya', 'lucas-star', pal_upd=hair('#24357e', '#162252'))


# ---------------------------------------------------------------- Hakuren (Ares)
@guarded
def hakuren():
    # Robert Skipolson: el flequillo le tapa entero el ojo izquierdo (el de la izquierda de la imagen) y el otro ojo es gris
    _c = _fix('ares-hakuren-ares', 'robert-skipolson', pal_upd={'iris': hexc('#6e7a8c')})
    _i = next(i for i, l in enumerate(_c['front']) if isinstance(l, dict) and l['z'] == 'f' and l['c'] == 'mid' and l['sil'] and not l.get('spk'))
    _c['front'][_i] = L(blob([(8, 40), (40, 26), (60, 32), (56, 58), (50, 88), (36, 92), (24, 80), (12, 64)]), 'mid', 'f')
    _c['front'].insert(_i + 1, strand([(56, 36), (50, 62), (42, 90)], 'shade', 'f', 1.6))
    for _l in _c['front']:
        if isinstance(_l, dict) and _l.get('w') and _l['c'] == OUTC:  # la raya negra del flequillo, ahora por el borde del mechón
            _l['s'] = strand([(58, 34), (54, 60), (48, 88)], OUTC, 'f', 1.0)['s']

    # Aiden Froste (Fubuki Atsuya): el pelo es naranja asalmonado, no naranja
    _fix('ares-hakuren-ares', 'aiden-froste', pal_upd=hair('#d88a62', '#b0623e', '#8a4630'))


# ---------------------------------------------------------------- Raimon de la isla (Inakuni Raimon)
@guarded
def inakuni():
    # Aurelia Dingle: cejas finas y suaves, no fruncidas como un chico
    _fix('ares-inakuni-raimon', 'aurelia-dingle', face_upd={'brows': True})


# ---------------------------------------------------------------- Kidokawa Seishuu (Ares)
def _murdock_lips(c, lens=None):
    """Los trillizos Murdock: labios gruesos marrones que sobresalen (un óvalo grande con la raya de la boca)."""
    c['face'] = dict(c['face'], mouth='none')
    c['pal']['lip'] = hexc('#9a5a36')
    c['pal']['lip_d'] = hexc('#6e3a20')
    if lens:
        c['pal']['lens'] = hexc(lens)
    for v in ('front', 'side'):  # montura más gruesa: con la fina las gafas no se veían en el sprite
        for l in c[v]:
            if isinstance(l, dict) and l['c'] == 'frame' and l['w']:
                l['w'] = 3.0
    c['front'] = c['front'] + [L(ell(50, 93, 9, 5), 'lip', 'f', ln=True), L(quad((42, 93), (50, 95.5), (58, 93)), 'lip_d', 'f', False, False, 1.3)]
    c['side'] = c['side'] + [L(ell(88, 92, 4.5, 5), 'lip', 'f', ln=True), L([(85, 92), (92, 92)], 'lip_d', 'f', False, False, 1.1)]


@guarded
def kidokawa():
    T = 'ares-kidokawa-seishuu-ares'
    # Alfred Meenan: ojos granates (rojizos), no grises
    _fix(T, 'alfred-meenan', pal_upd={'iris': hexc('#8a2e30')})
    _murdock_lips(_fix(T, 'marvin-murdock'), '#b8601a')  # cristales naranjas tintados
    _murdock_lips(_fix(T, 'thomas-murdock'), '#6e4a34')  # cristales marrones
    _murdock_lips(_fix(T, 'tyler-murdock'), '#8a4e2c')  # cristales ámbar con montura rosa
    # Axel Blaze en Ares: rubio pajizo más amarillo (sombras anaranjadas), no beige rosado
    _fix(T, 'axel-blaze', pal_upd=hair('#f4d898', '#d8a46a', '#a8703e', '#fff4d8'))


# ---------------------------------------------------------------- Minodouzan
@guarded
def minodouzan():
    # Björn Brocken: melena azul marino muy oscura, casi negra (no violeta)
    _fix('ares-minodouzan', 'bj-rn-brocken', pal_upd=hair('#2e2656', '#211a40', '#160f2c'))


# ---------------------------------------------------------------- Tonegawa Tousen
@guarded
def tonegawa():
    # Luke Blank: ojos grandes y oscuros de anime (no dos puntitos con el blanco alrededor)
    _fix('ares-tonegawa-tousen', 'luke-blank', face_upd={'eyes': 'big'}, pal_upd={'iris': hexc('#22222c')})


# ---------------------------------------------------------------- Eisei Gakuen
@guarded
def eisei():
    T = 'ares-eisei-gakuen'
    # Claire Lesnow: el pelo es azul marino, no azul rey
    _fix(T, 'claire-lesnow', pal_upd=hair('#2a4a80', '#1e365e', '#142640'))
    # Xavier Schiller: castaño grisáceo con las mechas de arriba casi blancas (no gris apagado)
    _fix(T, 'xavier-schiller', pal_upd=hair('#6a5a5a', '#45363a', '#32262a', '#dcdadc'))


# ---------------------------------------------------------------- Teikoku (Ares)
@guarded
def teikoku():
    # David Samford en Ares: el parche del ojo es una placa metálica gris, no negra
    _fix('ares-teikoku-gakuen-ares', 'david-samford', pal_upd={'patch': hexc('#9a9ca4')})


# ---------------------------------------------------------------- Mikage Sennou (Ares)
@guarded
def mikage():
    # Jonathan Seller: el pelo es beige rosado muy claro con sombras malva, no gris rosado apagado
    c = _fix('ares-mikage-sennou-ares', 'jonathan-seller', pal_upd=hair('#e6d4ca', '#b48e88', '#8a6660', '#faf2ee'))
    # y el pelo ondulado abulta mucho a los lados (sobre todo a la derecha de la imagen), por encima de las orejas
    c['front'] = [L(_cloud(96, 44, 18, 26, 5, 0.4)), L(_cloud(96, 50, 10, 16, 4, 0.2), 'shade', 'b', False), L(_cloud(6, 48, 12, 20, 4, 0.3)),
                  strand([(84, 30), (104, 44), (96, 66)], 'deep', 'b', 1.0)] + c['front']
    c['back'] = [L(_cloud(98, 44, 18, 26, 5, 0.4)), L(_cloud(4, 44, 18, 26, 5, 0.4))] + c['back']


# ---------------------------------------------------------------- Peinados con volumen (segunda pasada)
@guarded
def mickey_way():
    # Mickey Way (Amano Masamichi): melena salvaje enorme, el doble de ancha que la cara, de pinchos que salen hacia los lados y
    # caen por encima de los hombros; de perfil, los pinchos van hacia atrás y abajo hasta la espalda
    c = _fix('ares-seishou-gakuen', 'mickey-way')
    top = [(-4, 106), (-14, 124, 1), (-8, 104), (-26, 100, 1), (-12, 86), (-32, 74, 1), (-14, 62), (-34, 46, 1), (-14, 36), (-26, 16, 1), (-6, 14), (-10, -8, 1),
           (10, 0), (12, -20, 1), (28, -8), (34, -28, 1), (46, -12), (56, -32, 1), (64, -12), (78, -26, 1), (84, -6), (104, -12, 1), (102, 8), (124, 10, 1), (110, 26),
           (134, 38, 1), (114, 48), (134, 64, 1), (114, 74), (130, 90, 1), (110, 96), (124, 114, 1), (106, 108), (114, 126, 1)]
    front = top + [(96, 110), (86, 98), (70, 92), (30, 92), (14, 98), (4, 110)]
    back = top + [(98, 112), (88, 126, 1), (78, 112), (70, 128, 1), (60, 114), (50, 130, 1), (40, 114), (30, 128, 1), (22, 112), (12, 126, 1), (6, 110)]
    shade_f = L(outline([(74, -8), (104, 2), (120, 40), (118, 90), (104, 104), (90, 92), (92, 50)]), 'shade', 'b', False)
    tex = lambda: [strand([(20, 6), (6, 40), (-10, 70)], 'deep', 'b', 1.0), strand([(36, -6), (26, 20)], 'deep', 'b', 1.0),
                   strand([(64, -6), (76, 22)], 'deep', 'b', 1.0), strand([(84, 10), (100, 48), (112, 84)], 'deep', 'b', 1.0)]
    fr = [l for l in c['front'] if l['z'] == 'f']
    c['front'] = [L(outline(front)), shade_f] + tex() + fr
    side = [(62, 48), (78, 42), (90, 30), (92, 12), (104, 0, 1), (86, -6), (88, -24, 1), (68, -16), (62, -34, 1), (46, -18), (32, -30, 1), (24, -12), (2, -20, 1),
            (2, 0), (-22, -2, 1), (-8, 14), (-32, 24, 1), (-12, 36), (-36, 52, 1), (-14, 58), (-32, 78, 1), (-10, 80), (-26, 104, 1), (-4, 100), (-14, 126, 1), (6, 112),
            (8, 132, 1), (20, 114), (32, 124, 1), (36, 104), (46, 88), (50, 66)]
    c['side'] = [L(outline(side)), L(outline([(-10, 30), (20, 40), (34, 80), (30, 110), (8, 112), (-12, 90)]), 'shade', 'b', False),
                 strand([(60, -20), (30, 0), (0, 30)], 'deep', 'b', 1.0), strand([(70, 10), (30, 30), (-10, 70)], 'deep', 'b', 1.0),
                 strand([(40, 40), (10, 80), (0, 110)], 'deep', 'b', 1.0)] + [l for l in c['side'] if l['z'] == 'f']
    c['back'] = [L(outline(back)), L(outline([(60, -12), (104, 2), (122, 44), (118, 96), (100, 116), (78, 112), (74, 50)]), 'shade', 'b', False)] + \
        [strand([(30, 0), (20, 50), (10, 100)], 'deep', 'b', 1.0), strand([(50, -10), (50, 60), (46, 110)], 'deep', 'b', 1.0),
         strand([(70, 0), (80, 50), (90, 100)], 'deep', 'b', 1.0)]


@guarded
def salvador_castell():
    # Salvador Castell (Alonso Fibiano): un gorro de rizos crema pegado a la cabeza, con dos bultos de lana a los lados a la
    # altura de los ojos; la cara redonda queda entera a la vista (no una nube grande que le tapa media cara)
    c = _fix('ares-barcelona-orb', 'salvador-castell')
    keep = [l for l in c['front'] if l['c'] in ((248, 248, 248, 255), OUTC) or (isinstance(l['c'], tuple) and l['c'][:3] == (248, 248, 248))]
    c['front'] = [L(_cloud(50, 30, 46, 32, 9, 0.2)), L(_cloud(8, 68, 15, 20, 6, 0.3)), L(_cloud(92, 68, 15, 20, 6, 0.6)),
                  L(outline([(78, 6), (92, 20), (98, 40), (96, 60), (92, 44), (84, 22)]), 'shade', 'b', False),
                  L(_cloud(50, 40, 36, 13, 8, 0.2), 'mid', 'f'), L(_cloud(38, 14, 12, 8, 4), 'light', 'f', False),
                  strand([(24, 36), (30, 46)], 'deep', 'f', 1.0), strand([(76, 36), (70, 46)], 'deep', 'f', 1.0),
                  strand([(44, 6), (40, 16), (48, 22)], 'deep', 'f', 1.0), strand([(60, 12), (66, 22)], 'deep', 'f', 1.0)] + keep
    c['side'] = [L(_cloud(40, 34, 46, 34, 9)), L(_cloud(24, 72, 20, 22, 6)),
                 
                 L(_cloud(70, 28, 18, 14, 5, 0.4), 'mid', 'f'), L(_cloud(52, 8, 12, 8, 4), 'light', 'f', False)] + \
        [l for l in c['side'] if l['z'] == 'f' and l['c'] not in ('mid', 'light')]
    c['back'] = [L(_cloud(50, 36, 48, 36, 10)), L(_cloud(8, 68, 15, 20, 6, 0.3)), L(_cloud(92, 68, 15, 20, 6, 0.6)), L(_cloud(50, 78, 38, 16, 7)),
                 L(outline([(78, 8), (92, 22), (98, 44), (94, 64), (90, 46), (84, 24)]), 'shade', 'b', False),
                 strand([(30, 20), (26, 50)], 'deep', 'b', 1.0), strand([(70, 20), (74, 50)], 'deep', 'b', 1.0), strand([(50, 50), (50, 80)], 'deep', 'b', 1.0)]


@guarded
def gideon_poe():
    # Gideon Poe (Oma Nao) es un chico (la wiki: gender M): cuerpo delgado, no de chica
    _fix('ares-mikage-sennou-ares', 'gideon-poe', body='delgado')


@guarded
def neville_merchant():
    # Neville Merchant (Mizuho Kaname): rizos esponjosos en dos capas, la de arriba gris ceniza y la de abajo (que asoma por los
    # lados de la cara y la nuca) pardo grisácea más oscura; contorno de bultos redondos, no liso
    c = _fix('ares-tonegawa-tousen', 'neville-merchant', pal_upd={'deep': hexc('#5e4c4e')})
    fr = [l for l in c['front'] if l['z'] == 'f']
    c['front'] = [L(_cloud(50, 80, 56, 24, 8, 0.2), 'deep'), L(_cloud(50, 30, 52, 38, 9, 0.2)),
                  L(outline([(70, 0), (92, 18), (100, 46), (92, 62), (84, 34)]), 'shade', 'b', False)] + fr
    c['side'] = [L(_cloud(26, 72, 30, 30, 7, 0.3), 'deep'), L(_cloud(44, 30, 50, 36, 9, 0.2)),
                 L(outline([(4, 30), (24, 34), (30, 58), (6, 60)]), 'shade', 'b', False)] + [l for l in c['side'] if l['z'] == 'f']
    c['back'] = [L(_cloud(50, 76, 56, 28, 8, 0.2), 'deep'), L(_cloud(50, 32, 52, 38, 9, 0.2)),
                 L(outline([(66, 2), (92, 20), (100, 46), (90, 64), (78, 40)]), 'shade', 'b', False)]


def _glasses(y=76, c=(24, 22, 26, 255), w=3.0):
    """Gafas rectangulares de montura gruesa (que se vean también en el sprite pequeño)."""
    return [L([(21, y - 6), (46, y - 6), (46, y + 5), (22, y + 5), (21, y - 6)], c, 'f', False, False, w),
            L([(79, y - 6), (54, y - 6), (54, y + 5), (78, y + 5), (79, y - 6)], c, 'f', False, False, w),
            L([(46, y - 4), (54, y - 4)], c, 'f', False, False, w * 0.8), L([(21, y - 5), (14, y - 7)], c, 'f', False, False, w * 0.8),
            L([(79, y - 5), (86, y - 7)], c, 'f', False, False, w * 0.8)]


@guarded
def gerard_carbonell():
    # Gerard Carbonell (Gregorio Jaballo): pelo corto rubio blanquecino con sombras rosadas, peinado hacia los lados con unas
    # pocas puntas cortas (no una mata de pinchos grande), y gafas negras rectangulares bien visibles
    c = _fix('ares-barcelona-orb', 'gerard-carbonell', pal_upd=hair('#f0dcc6', '#d2a89a', '#a87e74', '#fff4ea'))
    c['face'] = dict(c['face'], eye_y=76)
    c['front'] = [L(outline([(14, 66), (8, 52), (2, 44, 1), (10, 34), (8, 16, 1), (22, 12), (28, -4, 1), (40, 4), (54, -8, 1), (62, 4), (78, -2, 1), (82, 12),
                             (98, 20, 1), (92, 32), (100, 48, 1), (90, 52), (86, 66), (84, 58), (16, 58)])),
                  L(outline([(62, 4), (80, 6), (92, 32), (90, 52), (82, 40)]), 'shade', 'b', False),
                  L(outline([(30, 6), (40, 4), (38, 18)]), 'light', 'b', False),
                  L(outline([(14, 62), (16, 40), (30, 24), (50, 18), (72, 24), (86, 40), (86, 60), (78, 48), (72, 58, 1), (64, 44), (56, 54, 1), (50, 40), (42, 52, 1),
                             (36, 40), (26, 56, 1), (20, 46)]), 'mid', 'f'),
                  strand([(30, 26), (24, 46)], 'shade', 'f', 1.2), strand([(66, 26), (74, 44)], 'shade', 'f', 1.2)] + _glasses(76)
    c['side'] = [L(outline([(56, 60), (60, 48), (78, 44), (90, 32), (90, 14), (100, 6, 1), (80, 2), (74, -10, 1), (58, 0), (42, -12, 1), (32, 2), (12, -2, 1),
                            (14, 14), (-4, 24, 1), (6, 34), (-6, 48, 1), (6, 54), (2, 70, 1), (16, 66), (24, 80, 1), (34, 68), (46, 66)])),
                 L(outline([(4, 34), (24, 40), (26, 64), (10, 62)]), 'shade', 'b', False),
                 L(outline([(66, 2), (90, 16), (94, 40), (92, 58, 1), (84, 44), (78, 52, 1), (74, 38), (66, 28)]), 'mid', 'f'),
                 L([(76, 70), (89, 70), (89, 81), (77, 81), (76, 70)], (24, 22, 26, 255), 'f', False, False, 2.6),
                 L([(76, 72), (50, 68)], (24, 22, 26, 255), 'f', False, False, 2.2)]
    c['back'] = [L(outline([(14, 78), (4, 70, 1), (8, 56), (-2, 44, 1), (8, 34), (6, 14, 1), (22, 12), (28, -4, 1), (40, 4), (54, -8, 1), (62, 4), (78, -2, 1),
                            (82, 12), (98, 20, 1), (94, 34), (104, 46, 1), (94, 56), (98, 72, 1), (86, 78), (74, 90, 1), (64, 82), (52, 92, 1), (40, 82), (28, 90, 1)])),
                 L(outline([(58, 4), (80, 8), (94, 40), (90, 72), (66, 82)]), 'shade', 'b', False),
                 strand([(30, 20), (36, 50), (30, 74)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50), (70, 74)], 'deep', 'b', 1.0),
                 L([(8, 70), (2, 68)], (24, 22, 26, 255), 'f', False, False, 2.2), L([(92, 70), (98, 68)], (24, 22, 26, 255), 'f', False, False, 2.2)]


@guarded
def ross_siddon():
    # Ross Siddon (Posei Donji «DJ», portero): cabeza enorme más ancha que alta, con papada y mofletes caídos; el cráneo rapado
    # gris hasta las cejas con una placa dorada plana arriba y dos bolitas doradas a cada lado; orejas grandes a media altura
    # y rastas doradas cortas que asoman por detrás de los mofletes; cejas de enfado, ojos pequeños y dientes apretados
    from chars import rope
    c = _fix('ares-zeus-ares', 'ross-siddon')
    face = outline([(10, 46), (24, 28), (50, 22), (76, 28), (90, 46), (96, 64), (106, 84), (100, 100), (84, 110), (50, 114), (16, 110), (0, 100), (-6, 84), (4, 64)])
    c['face'] = dict(c['face'], face_front=face, ear_out=14, big_ears=3, mouth='none', nose=(50, 86, 4.4), eye_y=72, eye_sep=15)
    knobs = lambda pts: [L(ell(x, y, 3.6, 3.6), 'gold', 'f', ln=True) for x, y in pts]
    c['front'] = [L(rope((10, 84), (-6, 92), (-18, 106), 7), 'gold', 'b'), L(rope((90, 84), (106, 92), (118, 106), 7), 'gold', 'b'),
                  L(rope((14, 88), (2, 100), (-8, 114), 6), 'gold_d', 'b'), L(rope((86, 88), (98, 100), (108, 114), 6), 'gold_d', 'b'),
                  L(outline([(10, 48), (24, 28), (50, 22), (76, 28), (90, 48), (72, 42), (50, 40), (28, 42)]), 'mid', 'f', ln=True),
                  L(outline([(60, 26), (76, 30), (88, 46), (74, 40)]), 'shade', 'f', False),
                  L(outline([(30, 24), (34, 12), (66, 12), (70, 24), (50, 27)]), 'gold', 'f', ln=True),
                  L(outline([(34, 14), (66, 14), (64, 18), (36, 18)]), 'gold_d', 'f', False),
                  L([(39, 93), (61, 93), (59, 102), (41, 102)], (250, 250, 250, 255), 'f', ln=True),  # dientes apretados
                  L([(40, 97.5), (60, 97.5)], OUTC, 'f', False, False, 1.0), L([(46, 93), (46, 102)], OUTC, 'f', False, False, 0.8),
                  L([(54, 93), (54, 102)], OUTC, 'f', False, False, 0.8)] + knobs([(19, 34), (13, 44), (81, 34), (87, 44)])
    c['side'] = [L(rope((32, 22), (8, 30), (-14, 52), 8), 'gold', 'b'), L(rope((34, 26), (14, 46), (0, 70), 8), 'gold_d', 'b'),
                 L(rope((30, 30), (4, 50), (-16, 72), 7), 'gold', 'b'),
                 L(outline([(18, 34), (36, 18), (66, 18), (86, 36), (88, 46), (60, 42), (30, 52)]), 'mid', 'f', ln=True),
                 L(outline([(38, 18), (42, 6), (66, 6), (70, 18)]), 'gold', 'f', ln=True)] + knobs([(36, 34), (28, 44)])
    c['back'] = [L(outline([(8, 70), (10, 36), (30, 18), (50, 14), (70, 18), (90, 36), (92, 70), (50, 78)])),
                 L(outline([(56, 16), (78, 22), (92, 46), (90, 70), (70, 74)]), 'shade', 'b', False),
                 L(outline([(32, 16), (36, 4), (64, 4), (68, 16)]), 'gold', 'f', ln=True)] + \
        [L(rope((50, 14), (x0, 44), (x1, y1), 9), k, 'f') for x0, x1, y1, k in ((26, -2, 60, 'gold'), (74, 102, 60, 'gold'), (36, 16, 80, 'gold_d'),
                                                                                 (64, 84, 80, 'gold_d'), (50, 50, 90, 'gold'))] + knobs([(10, 46), (90, 46)])
    # la bufanda gris alrededor del cuello, que le asoma bajo la papada
    c['pal']['scarf'], c['pal']['scarf_d'] = hexc('#b4b4b8'), hexc('#8a8a90')
    c['front'] = [L(blob([(-4, 104), (50, 112), (104, 104), (110, 120), (50, 128), (-10, 120)], 6), 'scarf', 'b', ln=True),
                  L(blob([(60, 112), (104, 106), (108, 118), (62, 124)], 5), 'scarf_d', 'b', False)] + c['front']
    c['side'] = [L(blob([(10, 96), (70, 100), (84, 112), (60, 122), (6, 116)], 6), 'scarf', 'b', ln=True)] + c['side']
    c['back'] = c['back'] + [L(blob([(-6, 100), (50, 106), (106, 100), (110, 118), (50, 124), (-10, 118)], 6), 'scarf', 'f', ln=True)]


@guarded
def hakuren_extra():
    # Maddox Rock: los cascos de las orejas son gris oscuro (no crema)
    _fix('ares-hakuren-ares', 'maddox-rock', pal_upd={'muff': hexc('#7a7a82'), 'muff_d': hexc('#4a4a52')})


@guarded
def minodouzan_extra():
    # Jack Wallside (Ares): piel tostada anaranjada como en su modelo, no marrón grisácea (en el sprite la cara se perdía bajo
    # el casco)
    _fix('ares-minodouzan', 'jack-wallside', pal_upd={'skin': hexc('#e2a46a'), 'skin_d': hexc('#c08452'), 'nose': hexc('#e0703a')})


def _white_glasses(y=75, side=False):
    """Gafas de montura blanca con su contorno oscuro (si no, sobre la piel clara no se ven)."""
    W = (246, 246, 246, 255)
    if side:
        g = [(76, y - 6), (90, y - 6), (90, y + 6), (77, y + 6), (76, y - 6)]
        return [L(g, OUTC, 'f', False, False, 3.6), L(g, W, 'f', False, False, 1.8), L([(76, y - 3), (50, y - 6)], OUTC, 'f', False, False, 3.0),
                L([(76, y - 3), (50, y - 6)], W, 'f', False, False, 1.4)]
    out = []
    for g in ([(26, y - 7), (46, y - 7), (45, y + 7), (27, y + 7), (26, y - 7)], [(74, y - 7), (54, y - 7), (55, y + 7), (73, y + 7), (74, y - 7)]):
        out += [L(g, OUTC, 'f', False, False, 3.6), L(g, W, 'f', False, False, 1.8)]
    return out + [L([(46, y - 4), (54, y - 4)], OUTC, 'f', False, False, 3.0), L([(46, y - 4), (54, y - 4)], W, 'f', False, False, 1.4)]


@guarded
def seishou_extra():
    # Ari Zimmerman: sus gafas blancas grandes no se veían (montura fina blanca sobre piel clara): ahora con contorno
    c = _fix('ares-seishou-gakuen', 'ari-zimmerman')
    c['face'] = {k: v for k, v in c['face'].items() if k not in ('glasses', 'glasses_rect')}
    c['front'] = c['front'] + _white_glasses(c['face'].get('eye_y', 75))
    c['side'] = c['side'] + _white_glasses(c['face'].get('eye_y', 75), True)


@guarded
def tonegawa_extra():
    # Eamond Everwing: el pañuelo rojo anudado al cuello
    c = _fix('ares-tonegawa-tousen', 'eamond-everwing', pal_upd={'scarf': hexc('#d0403a'), 'scarf_d': hexc('#9a2a26')})
    c['front'] = c['front'] + [L(blob([(30, 104), (70, 104), (66, 112), (50, 122), (34, 112)], 5), 'scarf', 'f', ln=True),
                               L(blob([(52, 106), (68, 105), (64, 112), (54, 118)], 4), 'scarf_d', 'f', False)]
    c['side'] = c['side'] + [L(blob([(48, 102), (82, 104), (86, 116), (60, 116)], 5), 'scarf', 'f', ln=True)]
    c['back'] = c['back'] + [L(blob([(30, 104), (70, 104), (66, 112), (34, 112)], 5), 'scarf', 'f', ln=True)]


@guarded
def bonnie_sparks():
    # Bonnie Sparks (Barazono Hana): el pelo morado va peinado hacia atrás (sin flequillo, se ve la frente) y recogido en una
    # coleta ancha y aplastada que se abre a los dos lados por detrás de los hombros como una cola de sirena; lazo turquesa
    # enorme arriba y gafas de nadador
    c = _fix('ares-eisei-gakuen', 'bonnie-sparks')
    keep = [l for l in c['front'] if l['c'] in ('bow', 'bow_d', 'gog', 'lens')]
    tail_l = L(outline([(14, 58), (2, 78), (-14, 100), (-22, 124, 1), (-6, 116), (10, 100), (18, 80)]), 'mid', 'b')
    tail_r = L(outline([(86, 58), (98, 78), (114, 100), (122, 124, 1), (106, 116), (90, 100), (82, 80)]), 'mid', 'b')
    c['face'] = dict(c['face'], ears=True, hairline=False)
    c['front'] = [tail_l, tail_r, L(outline([(-6, 104), (10, 96), (-14, 118)]), 'shade', 'b', False), L(outline([(106, 104), (90, 96), (114, 118)]), 'shade', 'b', False),
                  L(outline([(16, 52), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (84, 52), (72, 42), (50, 38), (28, 42)]), 'mid', 'f', ln=True),
                  L(outline([(60, 10), (80, 20), (86, 40), (78, 40), (70, 22)]), 'shade', 'f', False),
                  strand([(30, 30), (50, 18), (70, 30)], 'shade', 'f', 1.2)] + keep
    c['back'] = [L(outline([(16, 70), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 70), (96, 86), (118, 108), (126, 126, 1), (86, 120), (50, 116), (14, 120),
                            (-26, 126, 1), (-18, 108), (4, 86)])),
                 L(outline([(56, 8), (82, 18), (90, 46), (90, 80), (112, 104), (120, 120), (90, 114), (70, 60)]), 'shade', 'b', False),
                 strand([(40, 30), (30, 80), (0, 116)], 'shade', 'b', 1.2), strand([(60, 30), (70, 80), (100, 116)], 'shade', 'b', 1.2)] + \
        [l for l in c['back'] if l['c'] in ('bow', 'bow_d')]


@guarded
def jude_sharp_seishou():
    # Jude Sharp en Seishou: las rastas gruesas en filas (de frente hacia arriba y atrás, de perfil el mazo recogido detrás)
    # como en su modelo, no una mata esponjosa; mismas gafas de natación y la capa roja de Seishou
    c = copy.deepcopy(CHARS['jude-sharp'])
    c['cape'] = '#d81e24'
    c['pal'].update(hair('#9a7a3e', '#7a5c2a', '#5a4220', '#c8a464'))
    CHARS['ares-seishou-gakuen:jude-sharp'] = c
