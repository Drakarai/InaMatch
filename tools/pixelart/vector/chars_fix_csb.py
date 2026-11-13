"""Correcciones de la revisión de diseños (grupo csb): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS, L, OUTC, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401


def _fix(key, base, **changes):
    """Copia del dibujo actual (base) con cambios en la ficha, guardada con la clave del equipo."""
    c = copy.deepcopy(CHARS[base])
    c.update(changes)
    CHARS[key] = c
    return c


# ---------------------------------------------------------------- Gir (cs-giru)
# Bhufa: en su modelo es un portero ancho y fornido (hombros y brazos grandes), no de cuerpo normal
_fix('cs-giru:bhufa', 'bhufa', body='corpulento')

# ---------------------------------------------------------------- Zan (cs-zan)
# Mhadoor: alto y delgado en su modelo (la melena rubia hasta los hombros abulta, pero el cuerpo es normal)
_fix('cs-zan:mhadoor', 'mhadoor', body='normal')


def _flat(items):
    return [l for it in items for l in (it if isinstance(it, list) else [it])]


def _mirror(layers):
    """Las mismas capas con la imagen volteada (izquierda <-> derecha)."""
    out = []
    for l in _flat(layers):
        m = dict(l)
        m['s'] = [(100 - x, y) for x, y in l['s']]
        out.append(m)
    return out


# ---------------------------------------------------------------- Destructchers (cs-destructchers)
# Chamomile: el flequillo le tapa el ojo derecho de la imagen (no el izquierdo) y la melena cae por el lado izquierdo de la
# imagen en una gran masa que se abre hacia fuera a la altura del pecho; de espaldas, esa masa queda a la derecha
_c = _fix('cs-destructchers:chamomile', 'chamomile')
_c['front'] = _mirror(_c['front'])
_c['front'].insert(0, L(outline([(10, 40), (-8, 70), (-30, 100), (-38, 128, 1), (-14, 126), (8, 120), (20, 100), (22, 64)])))
_c['front'].insert(1, L(outline([(-6, 84), (-30, 120), (-12, 122), (8, 112)]), 'shade', 'b', False))
_c['back'].insert(0, L(outline([(90, 40), (108, 70), (130, 100), (138, 128, 1), (114, 126), (92, 120), (80, 100), (78, 64)])))
_c['back'].insert(1, L(outline([(106, 84), (130, 120), (112, 122), (92, 112)]), 'shade', 'b', False))


def _fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Ludeau: la melena rubia no es una bola de pinchos: son rizos gruesos y redondeados que le caen hasta los hombros, y
# arriba se abren dos grandes mechones en abanico, como alas o cuernos de alce, más anchos que la cabeza
_c = _fix('cs-zan:ludeau', 'ludeau')
_c['pal']['shade'] = (226, 190, 120, 255)
_LU = [(18, 72), (4, 110), (-12, 104), (-6, 92), (-20, 82), (-10, 68), (-22, 52), (-8, 40), (-14, 24), (0, 14), (-14, 0), (-28, -24, 1), (-6, -14),
       (-12, -34, 1), (8, -16), (8, -40, 1), (24, -12), (36, 0), (50, -6), (64, 0), (76, -12), (92, -40, 1), (92, -16), (112, -34, 1), (106, -14),
       (128, -24, 1), (114, 0), (100, 14), (114, 24), (108, 40), (122, 52), (110, 68), (120, 82), (106, 92), (112, 104), (96, 110), (82, 72)]
_c['front'] = [L(outline(_LU)),
               L(outline([(64, 0), (76, -12), (92, -40, 1), (92, -16), (112, -34, 1), (106, -14), (128, -24, 1), (114, 0), (100, 14), (114, 24), (108, 40),
                          (122, 52), (110, 68), (120, 82), (106, 92), (112, 104), (96, 110), (88, 70), (86, 30)]), 'shade', 'b', False),
               strand([(4, -10), (16, 4)], 'shade', 'b', 1.2), strand([(96, -10), (84, 4)], 'deep', 'b', 1.2),
               _c['front'][2], _c['front'][3]]
_c['side'] = [L(outline([(52, 70), (60, 50), (80, 44), (92, 30), (86, 6), (80, -10), (64, -36, 1), (56, -12), (40, -6), (22, -36, 1), (16, -4), (-2, 4), (-18, 14),
                         (-10, 30), (-26, 44), (-14, 58), (-28, 74), (-12, 84), (-24, 100), (-4, 104), (2, 120), (20, 108), (34, 116), (42, 96), (48, 84)])),
              L(outline([(-4, 40), (22, 50), (28, 100), (0, 104), (-14, 80)]), 'shade', 'b', False),
              _c['side'][2]]
_c['back'] = [L(outline(_LU[1:-1] + [(98, 118), (70, 126), (50, 118), (30, 126), (2, 118)])),
              L(outline([(58, 0), (76, -12), (92, -40, 1), (92, -16), (112, -34, 1), (106, -14), (128, -24, 1), (114, 0), (100, 14), (114, 24), (108, 40),
                         (122, 52), (110, 68), (120, 82), (106, 92), (112, 104), (98, 118), (70, 124), (78, 60)]), 'shade', 'b', False),
              strand([(30, 30), (24, 60), (32, 100)], 'shade', 'b', 1.2), strand([(56, 20), (48, 70), (54, 110)], 'shade', 'b', 1.2)]

# Zatang: melena blanca crema despeinada que cae por delante de la cara hasta la barbilla (un mechón largo entre los ojos)
# y un pincho alto en lo alto; las sombras del pelo son rosadas (de espaldas casi todo se ve rosa)
_c = _fix('cs-zan:zatang', 'zatang')
_c['pal'].update(shade=(232, 186, 180, 255), deep=(200, 144, 140, 255))
_c['front'] = [L(outline([(16, 92), (4, 100, 1), (4, 80), (-8, 74, 1), (2, 60), (-8, 44, 1), (4, 34), (2, 14), (16, 0), (30, -8), (42, -4), (56, -32, 1), (62, -6),
                          (78, -2), (92, 10), (106, 4, 1), (98, 28), (110, 46, 1), (96, 56), (106, 80, 1), (94, 82), (96, 102, 1), (84, 88), (84, 60), (16, 60)])),
               L(outline([(62, -4), (92, 10), (106, 4, 1), (98, 28), (110, 46, 1), (96, 56), (106, 80, 1), (94, 82), (96, 102, 1), (86, 86), (84, 40)]), 'shade', 'b', False),
               _fringe([(12, 76), (12, 44), (26, 24), (50, 16), (72, 22), (88, 40), (90, 74), (82, 62), (80, 86, 1), (72, 60), (64, 70, 1), (58, 52), (52, 88, 1),
                        (46, 54), (38, 72, 1), (32, 56), (22, 82, 1), (18, 64)]),
               strand([(66, 26), (74, 46), (78, 66)], 'shade', 'f', 1.0), strand([(48, 24), (50, 50), (52, 76)], 'shade', 'f', 1.0)]
_c['side'] = [L(outline([(56, 60), (64, 48), (84, 46), (94, 32), (90, 12), (98, -6, 1), (76, -2), (66, -28, 1), (50, -4), (30, -12, 1), (24, 4), (4, 8, 1), (8, 24),
                         (-8, 38, 1), (4, 48), (-6, 66, 1), (6, 70), (0, 92, 1), (16, 84), (20, 102, 1), (32, 84), (46, 74)])),
              L(outline([(-6, 40), (24, 40), (30, 80), (18, 96, 1), (6, 76)]), 'shade', 'b', False),
              _fringe([(64, 2), (90, 16), (96, 40), (94, 70, 1), (86, 52), (82, 66, 1), (76, 42), (66, 30)])]
_c['back'] = [L(outline([(14, 92), (-4, 94, 1), (2, 74), (-10, 56, 1), (2, 44), (-4, 20, 1), (14, 14), (20, -6, 1), (36, 2), (50, -26, 1), (60, 0), (78, -4, 1),
                         (84, 12), (104, 10, 1), (96, 32), (110, 50, 1), (96, 62), (104, 90, 1), (84, 86), (74, 102, 1), (62, 88), (50, 104, 1), (40, 88), (28, 102, 1)]),
                 'shade'),
              L(outline([(22, 30), (32, 8), (50, 0), (68, 8), (78, 30), (60, 24), (50, 44), (40, 24)]), 'mid', 'b', False),
              strand([(30, 50), (26, 80)], 'deep', 'b', 1.0), strand([(70, 50), (74, 80)], 'deep', 'b', 1.0)]

# Torhm: la parte de atrás del pelo es gris malva, no gris neutro
_c = _fix('cs-zan:torhm', 'torhm')
_c['pal'].update(shade=(170, 152, 146, 255), deep=(138, 122, 116, 255))


# ---------------------------------------------------------------- Protocolo Omega (cs-protocol-omega y 2.0, El Dorado 02)
def _po_mic(view):
    import chars_cs_protocol_omega as _P
    return _P.mic(view)


# Oscar (Medam): los dos mechones granates de los lados le llegan hasta el pecho, y por detrás lleva una coleta granate
# enorme, recogida arriba en un moño de nudos, que le tapa toda la nuca y cae hasta la espalda
_c = copy.deepcopy(CHARS['oscar'])
_c['front'] = [_c['front'][0], _c['front'][1], _c['front'][2],
               L(outline([(16, 52), (8, 90), (6, 136), (12, 148, 1), (22, 128), (24, 64)]), 'red', 'f', ln=True),
               L(outline([(84, 52), (92, 90), (94, 136), (88, 148, 1), (78, 128), (76, 64)]), 'red', 'f', ln=True),
               strand([(14, 70), (12, 130)], 'red_d', 'f', 0.9), strand([(86, 70), (88, 130)], 'red_d', 'f', 0.9),
               _c['front'][5]] + _po_mic('front')
_c['side'] = [L(outline([(28, 4), (6, 10), (-10, 40), (-16, 100), (-12, 146, 1), (0, 130), (8, 150, 1), (16, 120), (22, 60), (30, 30)]), 'red', 'b', ln=True),
              strand([(-4, 50), (-6, 130)], 'red_d', 'b', 1.0),
              L(ell(14, 14, 10, 9), 'red_d', 'b', ln=True),
              L(outline([(54, 56), (62, 46), (80, 46), (92, 30), (84, 10), (62, 0), (34, 2), (14, 16), (8, 40), (14, 66), (32, 72), (46, 66)])),
              L(outline([(30, 4), (58, 0), (76, 8), (62, 18), (40, 30), (22, 26)]), 'red', 'b', ln=True),
              L(outline([(54, 56), (58, 90), (56, 136), (52, 148, 1), (46, 120), (46, 60)]), 'red', 'f', ln=True)] + _po_mic('side')
_c['back'] = [L(outline([(16, 74), (12, 34), (24, 10), (50, 0), (76, 10), (88, 34), (84, 74), (50, 82)])),
              L(outline([(14, 56), (8, 92), (8, 136), (14, 148, 1), (22, 120), (22, 64)]), 'red', 'f', ln=True),
              L(outline([(86, 56), (92, 92), (92, 136), (86, 148, 1), (78, 120), (78, 64)]), 'red', 'f', ln=True),
              L(outline([(30, 4), (70, 4), (80, 40), (82, 100), (78, 146), (66, 136), (58, 150, 1), (50, 138), (42, 150, 1), (34, 136), (22, 146), (18, 100), (20, 40)]),
                'red', 'f', ln=True),
              L(outline([(70, 8), (80, 40), (82, 100), (78, 146), (66, 136), (68, 60)]), 'red_d', 'f', False),
              L(ell(50, 22, 11, 10), 'red_d', 'f', ln=True), L(ell(50, 44, 8, 8), 'red_d', 'f', ln=True),
              strand([(40, 60), (38, 130)], 'red_d', 'f', 1.0), strand([(56, 60), (58, 130)], 'red_d', 'f', 1.0)]
for _t in ('cs-protocol-omega', 'cs-protocol-omega-2-0'):
    CHARS[f'{_t}:oscar'] = _c

# Lima (Quorth): melena morada muy oscura más larga y ondulada: mechones gruesos que caen por delante de los hombros, uno
# que le cruza la cara por la izquierda y otro rizado a la derecha; por detrás le llega a media espalda en ondas
_c = copy.deepcopy(CHARS['lima'])
_c['pal'].update(shade=(30, 26, 52, 255), deep=(18, 16, 34, 255), light=(84, 76, 120, 255))
_c['front'] = [L(outline([(12, 70), (-6, 92), (-2, 120), (-10, 146, 1), (8, 136), (16, 150, 1), (22, 120), (20, 90),
                          (16, 64), (-6, 40), (6, 10), (30, -6), (62, -8), (90, 6), (106, 36), (84, 64), (80, 90), (78, 120), (84, 150, 1), (92, 136), (110, 146, 1),
                          (102, 120), (106, 92), (88, 70)])),
               L(outline([(62, -4), (90, 8), (104, 40), (90, 66), (100, 110), (106, 140, 1), (90, 130), (82, 70)]), 'shade', 'b', False),
               _fringe([(10, 76), (8, 44), (22, 20), (48, 10), (74, 16), (90, 40), (92, 72), (84, 60), (76, 70, 1), (68, 48), (56, 54), (44, 70), (36, 100), (30, 112, 1),
                        (30, 84), (34, 56), (24, 58), (16, 72)]),
               L(outline([(80, 70), (88, 84), (82, 96), (74, 92), (80, 86)]), 'mid', 'f', ln=True),
               strand([(40, 22), (30, 60), (34, 100)], 'light', 'f', 1.0), strand([(70, 20), (78, 46)], 'light', 'f', 1.0)] + _po_mic('front')
_c['side'] = [L(outline([(54, 62), (60, 50), (82, 48), (94, 32), (86, 6), (60, -6), (28, -4), (6, 14), (-8, 44), (-20, 80), (-34, 110), (-30, 130, 1), (-12, 116),
                         (-8, 140, 1), (6, 120), (14, 146, 1), (24, 116), (36, 96), (44, 80)])),
              L(outline([(-6, 46), (24, 50), (30, 100), (8, 120), (-16, 112)]), 'shade', 'b', False),
              strand([(30, 10), (6, 50), (-14, 100)], 'light', 'b', 1.0),
              _fringe([(64, 2), (88, 16), (96, 40), (94, 70, 1), (84, 52), (78, 64, 1), (70, 40)])] + _po_mic('side')
_c['back'] = [L(outline([(4, 130), (-10, 140, 1), (-6, 100), (-10, 60), (4, 18), (30, -4), (70, -4), (96, 18), (110, 60), (106, 100), (110, 140, 1), (94, 130),
                         (82, 146, 1), (70, 128), (58, 148, 1), (48, 128), (36, 146, 1), (24, 126), (14, 144, 1)])),
              L(outline([(56, 0), (92, 18), (108, 62), (104, 120), (82, 140), (66, 120), (70, 60)]), 'shade', 'b', False),
              strand([(30, 20), (20, 70), (28, 120)], 'deep', 'b', 1.2), strand([(52, 20), (46, 80), (52, 130)], 'deep', 'b', 1.2),
              strand([(76, 24), (84, 70), (80, 120)], 'deep', 'b', 1.2), strand([(40, 10), (30, 50)], 'light', 'b', 1.0)]
for _t in ('cs-protocol-omega', 'cs-protocol-omega-2-0'):
    CHARS[f'{_t}:lima'] = _c


def _mx(pts):
    """Puntos en espejo (x -> 100 - x), conservando las puntas afiladas."""
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


# ---------------------------------------------------------------- Raimon de Chrono Stone (y Shinsei Inazuma Japan, El Dorado 02)
# Riccardo (Shindou) en Chrono Stone: pelo castaño rojizo ondulado, con una coleta corta de mechones que sale de lo alto
# atada con una goma blanca, y mechones finos que se abren a los lados a la altura de las sienes y acaban rizados; ojos
# rojos
_WH = (246, 246, 246, 255)
_TOP = [(42, 4), (36, -20), (26, -38, 1), (42, -28), (48, -48, 1), (56, -30), (72, -42, 1), (64, -18), (58, 4)]
_RIC = [(16, 92), (8, 100, 1), (6, 86), (-8, 76), (-24, 82, 1), (-6, 68), (0, 56), (-14, 44, 1), (4, 40), (4, 20), (18, 4), (40, -4), (60, -4), (82, 4), (96, 20),
        (96, 40), (114, 44, 1), (100, 56), (106, 68), (124, 82, 1), (108, 76), (94, 86), (92, 100, 1), (84, 92)]
_c = copy.deepcopy(CHARS['riccardo-di-rigo'])
_c['pal'] = pal('#94585a', '#fcdcc0', iris='#c81e1e', shade='#6e3c3e', deep='#502a2c', light='#b88080')
_c['front'] = [L(outline(_TOP)), L(outline(_TOP[4:] + [(52, 0)]), 'shade', 'b', False),
               L(outline(_RIC + [(84, 62), (16, 62)])),
               L(outline([(62, -2), (82, 4), (96, 20), (96, 40), (114, 44, 1), (100, 56), (106, 68), (124, 82, 1), (108, 76), (94, 86), (92, 100, 1), (86, 90), (84, 40)]),
                 'shade', 'b', False),
               L(outline([(44, -6), (56, -6), (57, 2), (43, 2)]), _WH, 'f', ln=True),
               _fringe([(12, 70), (12, 42), (26, 20), (50, 12), (74, 20), (88, 42), (88, 70), (80, 58), (76, 72, 1), (68, 50), (60, 62, 1), (54, 46), (48, 64, 1),
                        (42, 46), (34, 62, 1), (28, 50), (20, 68, 1)]),
               strand([(30, 22), (24, 40)], 'light', 'f', 1.0)]
_STOP = [(30, 4), (22, -20), (6, -40, 1), (26, -30), (30, -52, 1), (40, -28), (54, -44, 1), (50, -16), (44, 6)]
_c['side'] = [L(outline(_STOP)),
              L(outline([(54, 62), (60, 50), (82, 46), (92, 32), (86, 10), (64, -2), (36, 0), (14, 12), (2, 36), (-14, 40, 1), (0, 50), (-4, 70), (-22, 78, 1),
                         (-2, 82), (4, 100, 1), (16, 88), (24, 104, 1), (34, 86), (46, 74)])),
              L(outline([(0, 40), (24, 44), (30, 84), (8, 90), (-2, 70)]), 'shade', 'b', False),
              L(outline([(30, -4), (42, -2), (42, 6), (30, 6)]), _WH, 'f', ln=True),
              _fringe([(64, 2), (88, 14), (96, 38), (92, 64, 1), (84, 48), (78, 60, 1), (72, 38)])]
_c['back'] = [L(outline(_RIC[:-1] + [(96, 100, 1), (80, 92), (70, 104, 1), (60, 90), (50, 106, 1), (40, 90), (30, 104, 1), (20, 92)])),
              L(outline([(56, -4), (82, 4), (96, 20), (96, 40), (114, 44, 1), (100, 56), (106, 68), (124, 82, 1), (108, 76), (96, 100, 1), (80, 92), (70, 104, 1),
                         (64, 60)]), 'shade', 'b', False),
              L(outline(_TOP), 'mid', 'f', ln=True), L(outline(_TOP[4:] + [(52, 0)]), 'shade', 'f', False),
              L(outline([(43, -6), (57, -6), (58, 2), (42, 2)]), _WH, 'f', ln=True),
              strand([(30, 30), (24, 70), (30, 96)], 'deep', 'b', 1.0), strand([(70, 30), (76, 70), (70, 96)], 'deep', 'b', 1.0)]
for _t in ('cs-team-raimon', 'cs-shinsei-inazuma-japan', 'cs-el-dorado-team-02'):
    CHARS[f'{_t}:riccardo-di-rigo'] = _c

# Ryoma (Nishiki) en Chrono Stone: pelo azul marino, todo hacia arriba en un moño alto, y largos mechones ondulados como
# tentáculos que se abren en horizontal a los dos lados de la cabeza (de perfil, hacia atrás); dos mechones le caen junto
# a las mejillas; piel tostada y ojos verde azulado
_LT = [(14, 48), (-4, 42), (-30, 46), (-58, 36, 1), (-34, 56), (-12, 56), (-30, 66), (-56, 76, 1), (-26, 74), (-8, 72), (-20, 86), (-40, 98, 1), (-10, 90), (14, 72)]
_c = copy.deepcopy(CHARS['ryoma-nishiki'])
_c['pal'] = pal('#1e3e78', '#dc9c5c', iris='#2a8a7a', shade='#142c5a', deep='#0c1c3e', light='#3a64a8', ring=(42, 154, 168, 255))
_c['front'] = [L(outline([(38, 10), (36, -20), (44, -40), (54, -44), (62, -36), (64, -14), (62, 10)])),
               L(outline([(55, -43), (62, -36), (64, -14), (62, 10), (56, 4)]), 'shade', 'b', False),
               L(outline(_LT)), L(outline(_mx(_LT))),
               L(outline([(16, 72), (10, 40), (20, 12), (50, 2), (80, 12), (90, 40), (84, 72), (80, 56), (20, 56)])),
               L(outline([(62, 4), (82, 14), (90, 40), (84, 66), (78, 40)]), 'shade', 'b', False),
               _fringe([(14, 60), (16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (86, 60), (78, 48), (66, 40), (56, 46, 1), (50, 36), (44, 46, 1), (34, 40), (22, 48)]),
               L(outline([(16, 56), (10, 80), (14, 106, 1), (22, 84), (22, 60)]), 'mid', 'f', ln=True),
               L(outline([(84, 56), (90, 80), (86, 106, 1), (78, 84), (78, 60)]), 'mid', 'f', ln=True),
               strand([(40, 0), (44, -36)], 'light', 'b', 1.2), strand([(30, 22), (50, 22), (70, 22)], 'light', 'f', 0.8)]
_c['side'] = [L(outline([(12, 30), (-20, 18), (-52, 8, 1), (-24, 30), (-52, 40, 1), (-20, 44), (-48, 62, 1), (-14, 58), (-32, 82, 1), (8, 62)])),
              L(outline([(40, 6), (30, -24), (36, -44), (54, -46), (62, -30), (56, 4)])),
              L(outline([(54, 60), (60, 48), (82, 46), (92, 32), (86, 10), (64, -2), (36, 0), (14, 12), (6, 34), (8, 58), (20, 72), (36, 72), (46, 64)])),
              L(outline([(8, 30), (26, 36), (28, 64), (12, 60)]), 'shade', 'b', False),
              L(outline([(56, 56), (60, 82), (56, 104, 1), (50, 82), (50, 60)]), 'mid', 'f', ln=True),
              _fringe([(66, 2), (88, 14), (94, 38), (90, 54, 1), (84, 40), (76, 30)])]
_c['back'] = [L(outline([(14, 40), (-10, 30), (-42, 24, 1), (-16, 44), (-46, 54, 1), (-14, 58), (-36, 78, 1), (12, 66)])),
              L(outline(_mx([(14, 40), (-10, 30), (-42, 24, 1), (-16, 44), (-46, 54, 1), (-14, 58), (-36, 78, 1), (12, 66)]))),
              L(outline([(16, 80), (12, 40), (22, 12), (50, 2), (78, 12), (88, 40), (84, 80), (50, 88)])),
              L(outline([(56, 4), (82, 16), (90, 46), (84, 76), (62, 84)]), 'shade', 'b', False),
              L(outline([(38, 14), (36, -20), (44, -40), (54, -44), (62, -36), (64, -14), (62, 14)]), 'mid', 'f', ln=True),
              strand([(36, 20), (40, 70)], 'deep', 'b', 1.0), strand([(64, 20), (60, 70)], 'deep', 'b', 1.0)]
for _t in ('cs-team-raimon', 'cs-shinsei-inazuma-japan'):
    CHARS[f'{_t}:ryoma-nishiki'] = _c


# ---------------------------------------------------------------- Vamptym (cs-vamptym)
# Dave Walker: melena blanco azulada enorme que se arremolina como humo: mechones ondulados que salen a los dos lados en
# horizontal, un flequillo que le tapa la cara hasta la nariz dejando ver solo el ojo rojo, y por detrás casi todo en gris
# malva (la sombra)
_c = _fix('cs-vamptym:dave-walker', 'dave-walker')
_c['pal'].update(shade=(168, 152, 164, 255), deep=(138, 122, 136, 255), light=(236, 248, 250, 255))
_c['front'] = [L(outline([(16, 84), (2, 80), (-20, 98, 1), (-10, 74), (-28, 64, 1), (-6, 58), (-4, 40), (-22, 30, 1), (2, 24), (14, 4), (36, -10), (46, -30, 1),
                          (56, -10), (76, -6), (96, 10), (120, 2, 1), (104, 26), (110, 44), (130, 56, 1), (106, 60), (112, 76), (126, 94, 1), (100, 84), (86, 86),
                          (84, 62), (16, 62)])),
               L(outline([(70, -6), (96, 10), (120, 2, 1), (104, 26), (110, 44), (130, 56, 1), (106, 60), (112, 76), (126, 94, 1), (100, 84), (88, 80), (90, 30)]),
                 'shade', 'b', False),
               strand([(-14, 64), (6, 56)], 'shade', 'b', 1.0), strand([(110, 70), (96, 62)], 'deep', 'b', 1.0),
               _fringe([(10, 74), (12, 40), (30, 16), (56, 10), (78, 18), (90, 40), (90, 64), (82, 58), (72, 66), (66, 60), (58, 68), (50, 98, 1), (44, 74),
                        (34, 92, 1), (30, 70), (20, 88, 1), (16, 70)]),
               strand([(30, 22), (40, 50), (38, 80)], 'shade', 'f', 1.0), strand([(56, 16), (70, 34)], 'light', 'f', 1.2),
               L(ell(70, 76, 3, 2.4), 'iris', 'f', False)]
_c['side'] = [L(outline([(56, 60), (62, 48), (80, 44), (92, 28), (88, 8), (70, -6), (60, -28, 1), (42, -6), (20, 0), (0, 12), (-24, 8, 1), (-6, 28), (-30, 40, 1),
                         (-8, 48), (-26, 66, 1), (-4, 64), (-12, 86, 1), (10, 76), (14, 96, 1), (28, 78), (44, 72)]), 'shade'),
              L(outline([(60, -2), (84, 8), (94, 30), (80, 30), (60, 20), (40, 26), (20, 14), (40, 2)]), 'mid', 'b', False),
              strand([(10, 30), (-16, 46)], 'deep', 'b', 1.0), strand([(20, 50), (0, 74)], 'deep', 'b', 1.0),
              _fringe([(66, 0), (90, 14), (98, 40), (98, 74, 1), (88, 56), (86, 78, 1), (78, 50), (66, 34)])]
_c['back'] = [L(outline([(16, 88), (-2, 84), (-22, 98, 1), (-10, 74), (-30, 64, 1), (-6, 56), (-4, 40), (-24, 28, 1), (2, 22), (14, 2), (36, -10), (46, -30, 1),
                         (56, -10), (76, -6), (96, 10), (120, 4, 1), (104, 26), (110, 44), (130, 56, 1), (106, 62), (112, 78), (126, 96, 1), (100, 88), (84, 92),
                         (50, 96)]), 'shade'),
              L(outline([(30, -4), (56, -8), (80, 0), (70, 14), (50, 10), (30, 18), (16, 10)]), 'mid', 'b', False),
              strand([(30, 30), (10, 60), (-14, 70)], 'deep', 'b', 1.2), strand([(70, 30), (92, 56), (116, 60)], 'deep', 'b', 1.2),
              strand([(50, 30), (50, 80)], 'deep', 'b', 1.0)]

# Turner Fogg: los ojos son dos almendras enormes inclinadas (la punta de fuera sube hacia la sien), negro morado con un
# borde morado más claro y una pupila pequeña granate; la cabeza calva tiene las sombras rosadas, no beige
_c = _fix('cs-vamptym:turner-fogg', 'turner-fogg')
_c['pal'].update(shade=(226, 180, 160, 255), socket=(36, 22, 40, 255), socket_l=(110, 70, 110, 255), iris=(150, 30, 40, 255))
_EL = [(10, 50, 1), (24, 58), (40, 66), (47, 76), (42, 86), (28, 86), (18, 76)]
_c['front'] = [_c['front'][0], _c['front'][1],
               L(outline([(p[0] - 1.5, p[1] - 1.5) + tuple(p[2:]) for p in _EL]), 'socket_l', 'f', ln=True),
               L(outline(_mx([(p[0] - 1.5, p[1] - 1.5) + tuple(p[2:]) for p in _EL])), 'socket_l', 'f', ln=True),
               L(outline(_EL), 'socket', 'f', False), L(outline(_mx(_EL)), 'socket', 'f', False),
               L(ell(34, 78, 4, 2.4), 'iris', 'f', False), L(ell(66, 78, 4, 2.4), 'iris', 'f', False),
               L([(14, 46), (22, 40)], 'socket', 'f', False, False, 1.4), L([(86, 46), (78, 40)], 'socket', 'f', False, False, 1.4)]
_c['face']['mouth_y'] = 97
_c['side'] = [_c['side'][0], _c['side'][1],
              L(outline([(70, 70), (78, 58), (90, 54, 1), (94, 70), (88, 86), (76, 84)]), 'socket_l', 'f', ln=True),
              L(outline([(72, 70), (79, 60), (88, 57), (92, 70), (87, 83), (77, 81)]), 'socket', 'f', False),
              L(ell(86, 74, 2.6, 2.2), 'iris', 'f', False)]


def _shorten(spec, k, y0=100):
    """Acorta lo que cuelga por debajo de y0 (la melena de Lima y los mechones de Oscar llegan al pecho, no a la cintura)."""
    for v in ('front', 'side', 'back'):
        for l in _flat(spec[v]):
            l['s'] = [(x, y0 + (y - y0) * k if y > y0 else y) for x, y in l['s']]


_shorten(CHARS['cs-protocol-omega:lima'], 0.45)
_shorten(CHARS['cs-protocol-omega:oscar'], 0.6)
