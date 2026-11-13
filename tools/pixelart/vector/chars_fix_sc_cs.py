"""Correcciones de la revisión de diseños (grupo sc_cs): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de CS (scouts-cs), Orión (scouts-orion) y Ares (scouts-ares), comparados con su retrato de Victory Road y,
cuando lo hay, con su modelo 3D."""
import copy  # noqa: F401

from chars import CHARS, L, OUTC, blob, ell, outline, strand  # noqa: F401
from heads import lerp, quad  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl  # noqa: F401
from chars_scouts_ie1_03 import side_brow, thick_brows  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def _get(key):
    return copy.deepcopy(CHARS[key])


def _set(key, c):
    CHARS[key] = c


def M(pts, c='mid', z='b', sil=True, ln=False):
    return L(outline(pts), c, z, sil, ln)


def mx(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def W(pts, c, w, z='f'):
    """Raya de grosor w."""
    return L(pts, c, z, False, False, w)


def _recolor(c, old, new, views=('front', 'side', 'back')):
    for v in views:
        for l in c[v]:
            if l['c'] == old:
                l['c'] = new


CS = 'scouts-cs:'


# --------------------------------------------------------------------------------------------------------------------
# Keenan Mustard: el sombrero vaquero es de copa marrón muy oscura (granate) y ala NEGRA, con la cinta negra tachonada
# de puntos blancos (antes todo marrón claro).
HAT_CROWN, HAT_BRIM, HAT_BAND = _c('#5a3430'), _c('#221c20'), _c('#141012')


def _keenan():
    c = _get(CS + 'keenan-mustard')
    for v, (brim, crown, band) in (('front', (4, 5, 6)), ('side', (3, 4, 5)), ('back', (3, 4, 5))):
        c[v][brim]['c'] = HAT_BRIM
        c[v][crown]['c'] = HAT_CROWN
        c[v][band]['c'] = HAT_BAND
    c['front'] += [L(ell(x, 34, 1.3, 1.3), WHITE, 'f', False) for x in (30, 40, 50, 60, 70)]
    c['side'] += [L(ell(x, 32, 1.3, 1.3), WHITE, 'f', False) for x in (30, 44, 58, 72)]
    c['back'] += [L(ell(x, 36, 1.3, 1.3), WHITE, 'f', False) for x in (32, 50, 68)]
    _set(CS + 'keenan-mustard', c)


_keenan()


# Jinpei Ashiga: el pelo es casi blanco (sombra rosada) peinado hacia atrás en mechones, no un gorro rosa; el parche es
# un aro rojo con el centro negro cruzado por dos barritas rojas (antes un disco rojo con una X negra).
def _jinpei():
    c = _get(CS + 'jinpei-ashiga')
    c['pal'].update(mid=_c('#f4ecea'), shade=_c('#dcbcc0'), deep=_c('#c49aa2'), light=_c('#ffffff'))
    fr = c['front']
    del fr[6:8]  # la X negra
    red = fr[5]['c']
    fr[5:6] = [L(ell(36, 76, 9, 8), red, 'f'), L(ell(36, 76, 5.8, 5), BLACK, 'f', False),
               W([(30.5, 74.4), (41.5, 74.4)], red, 1.4), W([(30.5, 77.8), (41.5, 77.8)], red, 1.4)]
    sw = [strand([(36, 42), (40, 24), (50, 12)], 'shade', 'b', 1.2), strand([(64, 42), (62, 24), (58, 10)], 'shade', 'b', 1.2)]
    c['front'][2:2] = sw
    c['side'][2:2] = [strand([(80, 40), (60, 22), (36, 18), (20, 30)], 'shade', 'b', 1.4), strand([(70, 52), (50, 36), (24, 40), (12, 56)], 'shade', 'b', 1.4),
                      strand([(56, 60), (36, 56), (18, 72)], 'shade', 'b', 1.2)]
    c['back'][2:2] = [strand([(50, 16), (48, 50), (50, 80)], 'shade', 'b', 1.4), strand([(30, 22), (24, 50), (28, 78)], 'shade', 'b', 1.3),
                      strand([(70, 22), (76, 50), (72, 78)], 'shade', 'b', 1.3)]
    _set(CS + 'jinpei-ashiga', c)


_jinpei()


# Kippoji Ani: el pelo NO es una bola enorme: va peinado hacia atrás desde una frente alta, con unas pocas puntas arriba
# y detrás, y baja por las sienes en patillas largas que llegan a la perilla.
def _kippoji():
    c = _get(CS + 'kippoji-ani')
    kw = dict(top=8, w=42, cy=50, n=7, amp=7, seed=18, sweep=0.15)
    c['front'][0:2] = dome('front', sb=70, **kw) + [M([(14, 56), (24, 58), (24, 74), (21, 86, 1), (15, 74)], 'mid', 'b'),
                                                    M([(86, 56), (76, 58), (76, 74), (79, 86, 1), (85, 74)], 'mid', 'b')]
    c['face']['hairline'] = [(17.6, 104), (14, 60), (22, 50), (34, 44), (50, 42), (66, 44), (78, 50), (86, 60), (82.4, 104)]
    c['side'][0:2] = dome('side', nape=88, fr=46, **kw)
    c['back'][0:2] = dome('back', nape=88, **kw)
    _set(CS + 'kippoji-ani', c)


_kippoji()


# Chomo Ba: la X de la frente está sobre la ceja de SU izquierda (a la derecha de la imagen); el pelo es una melena ondulada
# peinada hacia atrás que baja hasta la mandíbula con mechones más claros, no un afro redondo.
def _chomo():
    c = _get(CS + 'chomo-ba')
    c['pal']['light'] = _c('#b07870')
    kw = dict(top=2, w=48, cy=46, n=10, amp=8, soft=True, seed=51)
    fr = c['front']
    crown, x1, x2, goatee = fr[2:4], fr[4], fr[5], fr[6]
    x1['s'] = [(58, 54), (67, 62)]
    x2['s'] = [(67, 54), (58, 62)]
    streaks = [strand([(30, 44), (36, 24), (50, 10)], 'light', 'b', 1.6), strand([(64, 42), (62, 22), (56, 10)], 'light', 'b', 1.6),
               strand([(12, 70), (10, 50), (20, 30)], 'light', 'b', 1.4), strand([(88, 70), (90, 50), (80, 30)], 'light', 'b', 1.4)]
    c['front'] = dome('front', long=96, flare=6, **kw) + streaks + crown + [x1, x2, goatee]
    c['side'] = dome('side', long=96, flare=6, fr=48, **kw) + [strand([(70, 40), (50, 20), (24, 26), (10, 50)], 'light', 'b', 1.6)] + c['side'][2:]
    c['back'] = dome('back', long=96, flare=6, ends=5, **kw) + [strand([(50, 10), (46, 40), (40, 80)], 'light', 'b', 1.6),
                                                               strand([(30, 20), (20, 50), (18, 84)], 'light', 'b', 1.4)] + c['back'][2:]
    _set(CS + 'chomo-ba', c)


_chomo()


# Emosuke Rokudo: le faltaban las patillas largas y finas que bajan por las mejillas hasta la mandíbula.
def _emosuke():
    c = _get(CS + 'emosuke-rokudo')
    c['front'] += [M([(17, 60), (24, 62), (25, 78), (24, 94, 1), (18, 78)], 'mid', 'f'), M(mx([(17, 60), (24, 62), (25, 78), (24, 94, 1), (18, 78)]), 'mid', 'f')]
    c['side'] += [M([(52, 58), (60, 60), (60, 78), (62, 94, 1), (54, 78)], 'mid', 'f')]
    _set(CS + 'emosuke-rokudo', c)


_emosuke()


# Ruff LeGrand: el pelo rubio va peinado hacia ATRÁS y deja la frente al aire (antes el pelo, del color de la piel, bajaba
# hasta las cejas y parecía una frente enorme); la piel es más clara y rosada.
def _ruff():
    c = _get(CS + 'ruff-legrand')
    c['pal'].update(skin=_c('#f2c49c'), skin_d=_c('#dca884'))
    c['face']['hairline'] = [(17.6, 104), (10, 60), (16, 42), (30, 32), (50, 30), (70, 32), (84, 42), (90, 60), (82.4, 104)]
    sw = [strand([(28, 36), (34, 18), (46, 2)], 'shade', 'b', 1.4), strand([(50, 32), (50, 14), (54, -2)], 'shade', 'b', 1.4),
          strand([(72, 36), (68, 18), (58, 2)], 'shade', 'b', 1.4)]
    c['front'][2:2] = sw
    _set(CS + 'ruff-legrand', c)


_ruff()


# Konano Futsuno: el moño grande va arriba y atrás; de perfil y de espaldas quedaba escondido dentro del pelo.
def _konano():
    c = _get(CS + 'konano-futsuno')
    c['side'][2] = L(ell(16, 10, 19, 18))
    c['side'].append(strand([(4, 6), (16, -2), (28, 8)], 'shade', 'b', 1.2))
    c['back'][2] = L(ell(50, 6, 22, 19), 'mid', 'f')
    c['back'] += [strand([(34, 4), (50, -6), (66, 4)], 'shade', 'f', 1.4), strand([(36, 14), (50, 22), (64, 14)], 'shade', 'f', 1.2)]
    _set(CS + 'konano-futsuno', c)


_konano()


# Lave Hato: tres pinchos arriba (el del centro alto y recto, los de los lados abiertos) y un mechón de punta hacia fuera
# en cada sien; antes era una gorra lisa de pelo.
def _lave():
    c = _get(CS + 'lave-hato')
    spikes = [M([(38, 24), (50, -16, 1), (62, 24)]), M([(24, 30), (22, 0, 1), (42, 22)]), M([(76, 30), (78, 0, 1), (58, 22)]),
              M([(10, 44), (-4, 40, 1), (14, 32)]), M([(90, 44), (104, 40, 1), (86, 32)])]
    sh = [L(outline([(50, 22), (50, -12, 1), (60, 22)]), 'shade', 'b', False), L(outline([(66, 26), (77, 2, 1), (60, 22)]), 'shade', 'b', False)]
    c['front'] = spikes + c['front'] + sh
    c['side'] = [M([(40, 20), (40, -14, 1), (56, 18)]), M([(22, 24), (8, 0, 1), (36, 18)]), M([(10, 40), (-6, 30, 1), (16, 30)])] + c['side']
    c['back'] = [M([(38, 24), (50, -16, 1), (62, 24)]), M([(24, 30), (22, 0, 1), (42, 22)]), M([(76, 30), (78, 0, 1), (58, 22)]),
                 M([(10, 44), (-4, 40, 1), (14, 32)]), M([(90, 44), (104, 40, 1), (86, 32)])] + c['back']
    _set(CS + 'lave-hato', c)


_lave()


# Gilles de Rais: la barba es una franja negra gruesa por toda la mandíbula (el modelo 3D de perfil la enseña ancha), y
# tiene una raya curva en cada pómulo bajo las ojeras.
def _gilles():
    c = _get(CS + 'gilles-de-rais')
    c['front'][1]['w'] = c['front'][2]['w'] = 4.2
    c['front'] += [W(quad((22, 82), (26, 90), (34, 92)), BLACK, 1.6), W(quad((78, 82), (74, 90), (66, 92)), BLACK, 1.6)]
    c['side'][1:2] = [M([(50, 70), (58, 70), (64, 88), (76, 100), (84, 104), (78, 109), (64, 104), (54, 90)], BLACK, 'f')]
    _set(CS + 'gilles-de-rais', c)


_gilles()


# Percival Travis: el flequillo largo le TAPA el ojo derecho (a la izquierda de la imagen) hasta la mejilla; el pelo es
# castaño grisáceo tirando a malva.
def _percival():
    c = _get(CS + 'percival-travis')
    c['pal'].update(mid=_c('#5a4a50'), shade=_c('#3e3238'), deep=_c('#30262c'), light=_c('#7a6a70'))
    c['front'].insert(3, M([(58, 36), (44, 44), (30, 56), (22, 70), (21, 92, 1), (30, 78), (40, 64), (50, 54), (60, 46)], 'mid', 'f'))
    c['front'].insert(4, strand([(50, 46), (34, 60), (25, 82)], 'shade', 'f', 1.2))
    _set(CS + 'percival-travis', c)


_percival()


# Hachinoshin Nitta: nariz grande, redonda y marrón (antes un botoncito del color de la piel).
def _hachinoshin():
    c = _get(CS + 'hachinoshin-nitta')
    c['face']['nose'] = (50, 86, 7)
    c['pal']['nose'] = _c('#c07a4a')
    _set(CS + 'hachinoshin-nitta', c)


_hachinoshin()


# Isami Kondo: la coleta corta sale de la coronilla hacia atrás y abajo, atada con una cinta rosa clara (modelo 3D); antes
# era un pincho horizontal con un punto oscuro.
def _isami():
    c = _get(CS + 'isami-kondo')
    c['side'][2:4] = [M([(12, 30), (-6, 32), (-24, 46), (-42, 74, 1), (-26, 64), (-34, 90, 1), (-14, 68), (6, 58)]),
                      strand([(0, 44), (-20, 56), (-32, 74)], 'shade', 'b', 1.3), L(ell(6, 44, 3.6, 7.4), _c('#e8c8d0'), 'f')]
    _set(CS + 'isami-kondo', c)


_isami()


# Nagahide Niwa: la coleta alta es larga y gruesa y cae por la espalda (modelo 3D); de perfil quedaba escondida.
def _nagahide():
    c = _get(CS + 'nagahide-niwa')
    from chars import rope
    c['side'][3] = L(rope((24, 2), (-30, 30), (-14, 128), 18), 'mid')
    c['side'].insert(4, strand([(14, 8), (-14, 40), (-12, 110)], 'shade', 'b', 1.4))
    c['back'][2] = M([(36, 10), (64, 10), (68, 60), (66, 112), (57, 136, 1), (50, 126), (43, 136, 1), (34, 112), (32, 60)], 'mid', 'f', True, True)
    c['back'].insert(3, strand([(50, 20), (52, 70), (48, 120)], 'shade', 'f', 1.4))
    _set(CS + 'nagahide-niwa', c)


_nagahide()


# Yoshinobu Tokugawa: del eboshi sale por detrás una cinta negra larguísima que se arquea y cae por la espalda (modelo 3D).
def _yoshinobu():
    c = _get(CS + 'yoshinobu-tokugawa')
    eb = c['side'][2]['c']
    c['side'].insert(0, W(quad((40, -34), (6, -50), (-6, -10)) + [(-8, 40), (-8, 150)], eb, 3.0, 'b'))
    c['back'].append(W([(50, -30), (50, 150)], eb, 3.4, 'f'))
    _set(CS + 'yoshinobu-tokugawa', c)


_yoshinobu()


# Chester Horse Sr.: solo la parte de arriba (el pico) es pelo; de los lados para atrás va rapado: piel con rayas de pelo
# castaño (modelo 3D), no pelo con rayas de piel.
def _chester_sr():
    c = _get(CS + 'chester-horse-sr')
    st = _c('#5a4636')  # no es un color del pelo: así fill_back_gaps no rellena la piel entre las rayas
    c['side'][0:3] = [M([(70, 42), (84, 34), (64, 8, 1), (40, 12), (16, 26), (10, 42), (40, 40)])] + \
        [W(quad((12, y), (26, y + 3), (40, y + 2)), st, 2.6) for y in (48, 56, 64)]
    c['back'] = [M([(12, 46), (14, 36), (30, 22), (50, 8, 1), (70, 22), (86, 36), (88, 46), (50, 42)])] + \
        [W(quad((13, y), (50, y + 6), (87, y)), st, 2.6) for y in (52, 60, 68)]
    _set(CS + 'chester-horse-sr', c)


_chester_sr()


# Ai Machina: los ojos son negros (no rojos) y la melena rizada acaba a la altura de la barbilla.
def _ai():
    c = _get(CS + 'ai-machina')
    c['pal']['iris'] = _c('#2a1820')
    kw = dict(top=0, w=48, cy=46, n=8, amp=8, soft=True, flare=12, seed=3)
    c['front'][1:3] = dome('front', long=98, **kw)
    c['side'][1:3] = dome('side', long=98, fr=50, **kw)
    c['back'][1:3] = dome('back', long=98, ends=5, **kw)
    _set(CS + 'ai-machina', c)


_ai()


# Choen Ryo: el pelo rojo baja por los lados en mechones de punta hasta la mandíbula.
def _choen():
    c = _get(CS + 'choen-ryo')
    lock = [(8, 56), (2, 76), (10, 98, 1), (14, 82), (20, 100, 1), (22, 64)]
    c['front'][0:0] = [M(lock), M(mx(lock))]
    c['back'][0:0] = [M([(6, 70), (4, 92), (14, 104, 1), (24, 90)]), M(mx([(6, 70), (4, 92), (14, 104, 1), (24, 90)]))]
    c['side'][0:0] = [M([(46, 56), (44, 80), (50, 100, 1), (56, 80), (58, 60)])]
    _set(CS + 'choen-ryo', c)


_choen()


# Scott Chegwin: el pelo baja en pico hasta el entrecejo (cara de mono en forma de corazón) y tiene un remolino de puntas
# arriba.
def _scott():
    c = _get(CS + 'scott-chegwin')
    c['face']['hairline'] = [(10, 80), (16, 56), (28, 50), (40, 54), (50, 66), (60, 54), (72, 50), (84, 56), (90, 80)]
    tuft = M([(36, 2), (40, -14, 1), (48, -6), (56, -18, 1), (60, -4), (68, -10, 1), (66, 4)])
    c['front'].insert(0, tuft)
    ears = c['front'][1:5]  # las orejas de mono quedaban tapadas por el pelo: van delante
    del c['front'][1:5]
    for e in ears:
        e['z'] = 'f'
    c['front'] += ears
    c['back'].insert(0, copy.deepcopy(tuft))
    c['side'].insert(0, M([(26, 4), (22, -14, 1), (34, -6), (40, -18, 1), (46, -2)]))
    _set(CS + 'scott-chegwin', c)


_scott()


# Suzy Stamp: las dos coletas son ENORMES (más grandes que media cabeza), abombadas, con el lazo amarillo largo cayendo
# por su lado de dentro.
def _suzy():
    c = _get(CS + 'suzy-stamp')
    from chars_scouts_ie2_03 import curls
    yb = _c('#f4c840')

    def puff(cx, s):
        return [L(curls(cx, 14, (26, 28), 6, 0.3)), L(blob([(cx - 4 * s, -2), (cx + 12 * s, 18), (cx + 8 * s, 30)], 4), 'shade', 'b', False),
                M([(cx + 6 * s, -12), (cx + 16 * s, 4), (cx + 22 * s, 34, 1), (cx + 8 * s, 20), (cx - 2 * s, 2)], yb, 'f')]
    c['front'] = puff(2, 1) + puff(98, -1) + c['front'][4:]
    c['back'] = puff(2, 1) + puff(98, -1) + c['back'][4:]
    c['side'][0:2] = [L(curls(18, 12, (24, 26), 6, 0.3)), M([(26, -10), (34, 6), (36, 32, 1), (24, 18)], yb, 'f')]
    _set(CS + 'suzy-stamp', c)


_suzy()


# Liana Moonicorn: melena rubia de tirabuzones: los lados caen en rizos gordos, no lisos.
def _liana():
    c = _get(CS + 'liana-moonicorn')
    from chars_scouts_ie2_03 import curls
    cl = [L(curls(x, y, (9, 9), 5, 0.4), 'mid', 'f', True, True) for y in (80, 98, 114) for x in (2, 98)]
    c['front'][2:2] = cl
    c['front'] += [strand([(6, 74), (10, 82)], 'shade', 'b', 1.0)]
    c['back'] += [L(curls(x, 116, (9, 9), 5, 0.4), 'mid', 'f', True, True) for x in (2, 22, 42, 62, 82, 100)]
    c['side'] += [L(curls(x, 116, (9, 9), 5, 0.4), 'mid', 'f', True, True) for x in (0, 18, 36)]
    _set(CS + 'liana-moonicorn', c)


_liana()


# Ryuun Cho: la coleta alta sube recta desde la coronilla y se dobla hacia un lado, atada con una cinta roja.
def _ryuun():
    c = _get(CS + 'ryuun-cho')
    c['front'][2] = M([(42, 6), (40, -14), (48, -34), (66, -36, 1), (56, -22), (58, 4)])
    c['front'][3] = W([(42, 2), (58, 1)], _c('#c82a2a'), 3)
    c['front'].insert(3, strand([(50, 0), (48, -16), (54, -30)], 'shade', 'b', 1.2))
    c['back'][-2] = M([(42, 4), (58, 4), (60, -16), (54, -34), (36, -36, 1), (44, -22), (42, -8)], 'mid', 'f')
    _set(CS + 'ryuun-cho', c)


_ryuun()


# Stan Proud: orejas de punta (le asoman a los lados de la melena roja).
def _stan():
    c = _get(CS + 'stan-proud')
    from chars_scouts_ie2_03 import ears_pointy
    c['face']['ears'] = False
    c['front'] += [dict(e, z='f') for e in ears_pointy('front', h=10)]
    c['back'] += [dict(e, z='f') for e in ears_pointy('back', h=10)]
    c['side'] += ears_pointy('side', h=10)
    _set(CS + 'stan-proud', c)


_stan()


# Van Yamano: de espaldas y de perfil el pelo acaba en pinchos que bajan por la nuca (modelo 3D).
def _van():
    c = _get(CS + 'van-yamano')
    c['back'] += [M([(x - 9, 80), (x + dx, 104, 1), (x + 9, 80)], 'mid', 'b') for x, dx in ((24, -6), (38, -2), (50, 0), (62, 2), (76, 6))]
    c['side'] += [M([(10, 70), (-4, 96, 1), (20, 84)], 'mid', 'b'), M([(20, 80), (16, 104, 1), (34, 88)], 'mid', 'b')]
    _set(CS + 'van-yamano', c)


_van()


# Nirasane Nebuka: la coleta alta sale del moño y vuela hacia atrás (de perfil apenas asomaba).
def _nirasane():
    c = _get(CS + 'nirasane-nebuka')
    c['side'][-1] = M([(32, 0), (12, 2), (-12, 16), (-26, 34, 1), (-8, 26), (4, 44, 1), (18, 18), (36, 10)])
    _set(CS + 'nirasane-nebuka', c)


_nirasane()


# Genko Ka: el parche es NEGRO (con una placa roja y blanca en medio), no rojo con una raya blanca.
def _genko():
    c = _get(CS + 'genko-ka')
    pk = _c('#241c22')
    c['front'][2]['c'] = pk
    c['front'][3:4] = [M([(60, 72), (67, 72), (67, 79), (60, 79)], _c('#c42a2a'), 'f', False), M([(67, 72), (72, 72), (72, 79), (67, 79)], WHITE, 'f', False)]
    c['side'][2]['c'] = pk
    c['side'].append(M([(80, 72), (86, 72), (86, 79), (80, 79)], _c('#c42a2a'), 'f', False))
    _set(CS + 'genko-ka', c)


_genko()


def _stubble(key, front_pts, side_pts):
    """Sombra de barba de pocos días: la piel un poco más oscura en la barbilla y la mandíbula."""
    c = _get(key)
    s = c['pal']['skin']
    st = tuple(int(v * 0.8) for v in s[:3]) + (255,)
    c['front'].append(L(blob(front_pts, 6), st, 'f', False))
    c['side'].append(L(blob(side_pts, 6), st, 'f', False))
    _set(key, c)
    return c


# Senjiro Kohama y Massimo Donati: tienen sombra de barba en la barbilla y la mandíbula (retrato).
_stubble(CS + 'senjiro-kohama', [(24, 88), (34, 98), (50, 104), (66, 98), (76, 88), (70, 100), (50, 108), (30, 100)],
         [(62, 92), (74, 100), (86, 98), (80, 106), (66, 104)])
_stubble('scouts-ares:massimo-donati', [(34, 96), (50, 100), (66, 96), (62, 104), (50, 108), (38, 104)], [(70, 98), (84, 98), (80, 106), (70, 104)])


# Yekaterina: los rizos son blancos azulados con la sombra MALVA abajo, en las volutas de los lados (modelo 3D); antes
# tenía manchas grises sueltas en la coronilla.
def _yekaterina():
    k = 'scouts-orion:yekaterina'
    c = _get(k)
    from chars_scouts_ie2_03 import curls
    c['pal'].update(shade=_c('#b4a2bc'), deep=_c('#8e7c98'))
    fr = c['front']
    del fr[4:6]
    fr[4:4] = [L(curls(11, 92, (9, 10), 5, 0.2), 'shade', 'b', True, True), L(curls(89, 92, (9, 10), 5, 0.7), 'shade', 'b', True, True)]
    sd = c['side']
    sd[3] = L(curls(20, 82, (20, 14), 6, 0.1), 'shade', 'b', True, True)
    bk = c['back']
    bk[2] = L(curls(50, 82, (44, 14), 8, 0.2), 'shade', 'f', True, True)
    _set(k, c)


_yekaterina()


# Truman Newton: la coleta baja cae por la nuca hasta el cuello, atada con una goma (modelo 3D); de perfil apenas asomaba.
def _truman():
    k = 'scouts-orion:truman-newton'
    c = _get(k)
    c['side'][1] = M([(16, 50), (2, 58), (-4, 80), (0, 106, 1), (8, 88), (12, 102, 1), (18, 74), (26, 60)])
    c['side'].insert(2, L(ell(12, 58, 3.4, 4.6), _c('#4a4446'), 'f'))
    _set(k, c)


_truman()


# Kim Canter (Terberry): las orejas de punta le asoman entre los mechones a la altura de los ojos.
def _kim():
    c = _get(CS + 'kim-canter-terberry')
    from chars_scouts_ie2_03 import ears_pointy
    c['face']['ears'] = False
    c['front'] += [dict(e, z='f') for e in ears_pointy('front', h=8)]
    c['side'] += ears_pointy('side', h=8)
    _set(CS + 'kim-canter-terberry', c)


_kim()


# Brick Deville: del flequillo le caen unos mechones de punta por encima de las gafas, hasta media cara.
def _brick():
    c = _get(CS + 'brick-deville')
    c['front'] += [M([(31, 50), (37, 50), (34, 72, 1)], 'mid', 'f'), M([(47, 50), (54, 50), (50, 76, 1)], 'mid', 'f'),
                   M([(63, 50), (69, 50), (67, 70, 1)], 'mid', 'f')]
    _set(CS + 'brick-deville', c)


_brick()


# Jinpei Ashiga (2.ª pasada): el pelo va pegado a la cabeza, liso y peinado hacia atrás; la masa abultada de bultos
# parecía un turbante.
def _jinpei2():
    c = _get(CS + 'jinpei-ashiga')
    kw = dict(top=12, w=41, cy=46, n=9, amp=3, soft=True, seed=12)
    c['front'][0:2] = dome('front', sb=62, **kw)
    c['side'][0:2] = dome('side', nape=84, fr=40, **kw)
    c['back'][0:2] = dome('back', nape=84, **kw)
    _set(CS + 'jinpei-ashiga', c)


_jinpei2()


# Liana Moonicorn (2.ª pasada): el contorno de la melena es ondulado, de rizos gordos (antes, liso con piquitos).
def _liana2():
    c = _get(CS + 'liana-moonicorn')
    kw = dict(top=2, w=50, cy=44, n=13, amp=7, soft=True, seed=28, long=116, flare=10)
    c['front'][0:2] = dome('front', **kw)
    c['side'][0:2] = dome('side', fr=52, **kw)
    c['back'][0:2] = dome('back', ends=6, **kw)
    _set(CS + 'liana-moonicorn', c)


_liana2()


# Brick Deville: menos volumen: pinchos más cortos y la masa más estrecha.
def _brick2():
    c = _get(CS + 'brick-deville')
    kw = dict(top=-2, w=46, cy=44, n=9, amp=11, sweep=0.2, seed=31)
    c['front'][0:2] = dome('front', sb=72, **kw)
    c['side'][0:2] = dome('side', nape=88, fr=50, **kw)
    c['back'][0:2] = dome('back', nape=88, **kw)
    _set(CS + 'brick-deville', c)


_brick2()


# Prince Charles: el pelo es blanco con la sombra malva rosada del modelo 3D (antes rosa pálido uniforme).
def _prince():
    c = _get(CS + 'prince-charles')
    c['pal'].update(mid=_c('#ece0e2'), shade=_c('#c8a0a6'), deep=_c('#a07c84'), light=_c('#fbf6f6'))
    _set(CS + 'prince-charles', c)


_prince()


# Redd Hazzard: la máscara roja acaba en pico sobre la nariz y deja ver las mejillas (antes, un bloque hasta la boca);
# le caen dos mechones del flequillo por encima.
def _redd():
    c = _get(CS + 'redd-hazzard')
    fr = c['front']
    fr[2]['s'] = outline([(16, 54), (24, 42), (50, 38), (76, 42), (84, 54), (84, 72), (70, 82), (58, 80), (50, 90, 1), (42, 80), (30, 82), (16, 72)])
    fr += [M([(36, 38), (44, 40), (38, 56, 1)], 'mid', 'f'), M([(62, 38), (70, 40), (66, 54, 1)], 'mid', 'f')]
    _set(CS + 'redd-hazzard', c)


_redd()


# ---------------------------------------------------------------------------------------------- piel y pelo medidos
# Color medido en el retrato (mediana de las mejillas y la barbilla, sin pelo ni máscaras; y del pelo, sin brillos
# blancos) cuando la suma de diferencias RGB pasaba de 30 y, revisado a ojo, el retrato lo confirmaba. La sombra de la
# piel es el 86 %; las sombras del pelo se escalan en la misma proporción que el tono medio.
MEASURED = {
    'scouts-cs:neville-foodcake': ((251, 216, 180), (212, 203, 112)),
    'scouts-cs:jinpei-ashiga': (None, (239, 224, 216)),
    'scouts-cs:keenan-mustard': ((255, 210, 137), (253, 159, 5)),
    'scouts-cs:kim-canter-terberry': ((254, 245, 217), None),
    'scouts-cs:leila-sway': ((238, 166, 98), None),
    'scouts-cs:mai-assam-assamu': ((250, 216, 181), None),
    'scouts-cs:konano-futsuno': ((251, 216, 180), None),
    'scouts-cs:kyoko-hanabayashi': ((238, 166, 96), (59, 53, 60)),
    'scouts-cs:souta-hayari': ((236, 172, 111), None),
    'scouts-cs:sloan-henge-hinge': ((252, 209, 163), None),
    'scouts-cs:tey-liadika': ((191, 133, 77), None),
    'scouts-cs:jetaime-horitara': ((251, 188, 124), None),
    'scouts-cs:mei-gongzhu': (None, (157, 62, 22)),
    'scouts-cs:johnny-kato': ((190, 133, 77), None),
    'scouts-cs:konomi-kodawara': ((206, 151, 105), None),
    'scouts-cs:samey-kondo': ((246, 191, 138), None),
    'scouts-cs:kocho-kyo': ((203, 113, 79), None),
    'scouts-cs:mmor-pegg': ((251, 216, 181), (140, 6, 6)),
    'scouts-cs:macha-green': ((255, 240, 212), (79, 69, 126)),
    'scouts-cs:meg-meggi-imai': (None, (18, 77, 119)),
    'scouts-cs:munetsugu-niseya': ((252, 188, 124), (74, 97, 86)),
    'scouts-cs:nirasane-nebuka': ((251, 216, 181), (63, 71, 104)),
    'scouts-cs:nagahide-niwa': (None, (67, 68, 115)),
    'scouts-cs:nizo-koda': ((206, 151, 104), None),
    'scouts-cs:lise-la-transe': ((206, 151, 103), None),
    'scouts-cs:pyon-pyon': (None, (44, 44, 48)),
    'scouts-cs:liana-moonicorn': ((255, 241, 211), (249, 243, 168)),
    'scouts-cs:senkuro-hajime': ((255, 208, 159), None),
    'scouts-cs:marc-mystique': (None, (160, 96, 63)),
    'scouts-cs:will-reynard': ((253, 234, 184), None),
    'scouts-cs:kyohi-sho': ((255, 240, 212), (208, 138, 166)),
    'scouts-cs:lunete-taliesin': (None, (61, 49, 112)),
    'scouts-cs:sting-xiang': ((250, 217, 182), None),
    'scouts-cs:kakui-ten': (None, (84, 57, 35)),
    'scouts-cs:vic-longboat': ((238, 166, 97), None),
    'scouts-cs:lupin-wolfe': ((255, 240, 211), None),
    'scouts-cs:ori-gami': ((250, 188, 122), None),
    'scouts-cs:van-yamano': ((251, 216, 182), None),
    'scouts-orion:philip-star': (None, (18, 44, 117)),
    'scouts-orion:yekaterina': (None, (220, 236, 253)),
    'scouts-ares:massimo-donati': ((177, 117, 84), (61, 58, 57)),
    'scouts-ares:faith-winter': (None, (66, 59, 71)),
}


def _measured():
    for key, (skin, hair) in MEASURED.items():
        c = _get(key)
        p = c['pal']
        if skin:
            old = p['skin']
            p['skin'] = tuple(skin) + (255,)
            p['skin_d'] = tuple(int(v * 0.86) for v in skin) + (255,)
            if p.get('nose') == old:
                p['nose'] = p['skin_d']
        if hair:
            old = p['mid']
            k = [(n + 1) / (o + 1) for n, o in zip(hair, old[:3])]
            for name in ('shade', 'deep', 'light'):
                if name in p:
                    p[name] = tuple(max(0, min(255, int(v * k[i]))) for i, v in enumerate(p[name][:3])) + (255,)
            p['mid'] = tuple(hair) + (255,)
        _set(key, c)


_measured()
