"""Correcciones de la revisión de diseños (grupo csa): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, outline, pal, strand  # noqa: E402,F401


def _fix(key, src=None, **kw):
    """Copia el dibujo actual (src, o la propia clave) a la clave del equipo y le cambia los campos de kw."""
    c = copy.deepcopy(CHARS[src or key])
    c.update(kw)
    CHARS[key] = c
    return c


def _fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# ============================================================== Garu (cs-garu)
# Kazach y Fumh no son corpulentos: en su modelo 3D tienen el cuerpo normal
_fix('cs-garu:kazach', 'kazach', body='normal')
_fix('cs-garu:fumh', 'fumh', body='normal')

# Pinoh: un único cono altísimo (no dos cuernos), que sale de lo alto de la cabeza un poco a la izquierda, con anillos
# marcados; mechones cortos en punta junto a las orejas
_c = _fix('cs-garu:pinoh', 'pinoh')
_c['front'] = [L(outline([(14, 70), (6, 44), (10, 20), (22, 4), (26, -30), (32, -86, 1), (48, -36), (60, -4), (82, 6), (96, 26), (94, 50), (88, 70), (82, 50), (18, 50)])),
               L(outline([(36, -60), (48, -36), (60, -4), (82, 6), (96, 26), (92, 50), (70, 30), (44, 4)]), 'shade', 'b', False),
               strand([(24, -10), (36, -4), (52, -12)], 'deep', 'b', 1.4), strand([(27, -34), (36, -30), (46, -38)], 'deep', 'b', 1.2),
               strand([(29, -56), (35, -54), (41, -60)], 'deep', 'b', 1.0),
               _fringe([(12, 62), (14, 42), (28, 30), (50, 26), (72, 30), (86, 42), (88, 62), (78, 52), (70, 62, 1), (62, 50), (54, 60, 1), (48, 48), (40, 60, 1),
                        (32, 50), (24, 62, 1)]),
               L(outline([(8, 66), (16, 64), (14, 80), (2, 84, 1)]), 'mid', 'f', ln=True), L(outline([(92, 66), (84, 64), (86, 80), (98, 84, 1)]), 'mid', 'f', ln=True),
               L([(30, 90), (31, 91)], OUTC, 'f', False, False, 1.2), L([(70, 90), (71, 91)], OUTC, 'f', False, False, 1.2)]
_c['side'] = [L(outline([(54, 62), (60, 48), (82, 46), (92, 30), (84, 10), (76, -20), (84, -84, 1), (56, -40), (36, -20), (14, 0), (2, 30), (2, 60), (-8, 76, 1), (14, 72),
                         (34, 70), (46, 66)])),
              L(outline([(60, -36), (80, -70), (74, -20), (70, 0)]), 'shade', 'b', False),
              L(outline([(4, 34), (24, 40), (26, 66), (8, 60)]), 'shade', 'b', False),
              strand([(40, -14), (60, -8), (78, -14)], 'deep', 'b', 1.4), strand([(56, -40), (66, -36), (78, -42)], 'deep', 'b', 1.2),
              _fringe([(70, 6), (92, 18), (96, 40), (92, 56, 1), (86, 44), (78, 32)])]
_c['back'] = [L(outline([(16, 80), (6, 44), (10, 20), (30, 2), (40, -36), (68, -86, 1), (74, -30), (78, 4), (90, 20), (94, 44), (88, 80), (50, 88)])),
              L(outline([(66, -60), (74, -30), (78, 4), (90, 20), (92, 50), (86, 76), (62, 84), (60, 10)]), 'shade', 'b', False),
              strand([(48, -10), (64, -4), (76, -12)], 'deep', 'b', 1.4), strand([(54, -34), (64, -30), (73, -38)], 'deep', 'b', 1.2),
              L(outline([(6, 70), (14, 68), (12, 82), (0, 86, 1)]), 'mid', 'f', ln=True), L(outline([(94, 70), (86, 68), (88, 82), (100, 86, 1)]), 'mid', 'f', ln=True)]

# Chikka: el remolino de pelo crema no le tapa la cara: una melena rizada y ahuecada que le enmarca la cara hasta la
# barbilla y acaba arriba en una punta curva inclinada a un lado; nariz y mejillas rosadas
_c = _fix('cs-garu:chikka', 'chikka')
_c['face'] = dict(_c['face'], nose=(50, 86, 3.2))
_c['pal'] = dict(_c['pal'], nose=(240, 150, 150, 255))
_c['front'] = [L(outline([(16, 100), (0, 96), (-12, 76), (-8, 54), (-14, 34), (0, 14), (14, 4), (24, -12), (42, -18), (40, -40, 1), (60, -22), (80, -12), (92, 4), (110, 22),
                          (112, 44), (106, 62), (112, 80), (98, 98), (84, 100), (84, 64), (16, 64)])),
               L(outline([(60, -16), (84, -6), (104, 22), (106, 60), (102, 90), (86, 92), (86, 40)]), 'shade', 'b', False),
               strand([(0, 40), (12, 34), (24, 40)], 'deep', 'b', 1.2), strand([(76, 40), (88, 34), (102, 40)], 'deep', 'b', 1.2),
               strand([(30, 4), (50, -2), (70, 4)], 'shade', 'b', 1.6),
               _fringe([(10, 74), (10, 46), (24, 28), (50, 22), (76, 28), (90, 46), (90, 74), (84, 60), (78, 54, 1), (70, 48), (62, 56, 1), (54, 46), (46, 56, 1), (38, 48),
                        (30, 56, 1), (20, 56), (16, 62)]),
               L(outline([(4, 76), (14, 70), (18, 92), (10, 104, 1), (2, 92)]), 'mid', 'f', ln=True),
               L(outline([(96, 76), (86, 70), (82, 92), (90, 104, 1), (98, 92)]), 'mid', 'f', ln=True)]
_c['side'] = [L(outline([(54, 62), (60, 48), (82, 44), (94, 30), (96, 10), (84, -6), (66, -14), (56, -38, 1), (40, -16), (16, -8), (-6, 10), (-14, 36), (-10, 62), (-2, 86),
                         (16, 98), (36, 94), (48, 78)])),
              L(outline([(-8, 14), (20, 20), (34, 60), (30, 90), (6, 90), (-6, 60)]), 'shade', 'b', False),
              strand([(4, 30), (20, 26), (36, 32)], 'deep', 'b', 1.2), strand([(-2, 60), (14, 56), (28, 62)], 'deep', 'b', 1.2),
              _fringe([(70, 6), (92, 18), (96, 40), (92, 56, 1), (86, 44), (78, 32)])]
_c['back'] = [L(outline([(16, 100), (0, 96), (-12, 76), (-8, 54), (-14, 34), (0, 14), (20, -10), (40, -20), (60, -40, 1), (58, -18), (80, -10), (100, 14), (112, 34),
                         (106, 56), (112, 76), (100, 96), (84, 102), (50, 106)])),
              L(outline([(56, -14), (84, -6), (104, 22), (106, 60), (102, 92), (60, 104)]), 'shade', 'b', False),
              strand([(10, 40), (30, 34), (50, 40)], 'deep', 'b', 1.2), strand([(50, 60), (70, 54), (92, 60)], 'deep', 'b', 1.2),
              strand([(14, 80), (34, 74), (54, 80)], 'deep', 'b', 1.2)]

# ============================================================== Dominio de Zanark (cs-zanark-domain)
# Zanark no es corpulento: alto y fibroso, con hombreras (como en su ficha de Chrono Storm)
_fix('cs-zanark-domain:zanark-avalonic', 'zanark-avalonic', body='normal')

# ============================================================== Protocolo Omega 3.0 (cs-protocol-omega-3-0)
# Quebec (Bahamus Mixi Max): no es un sombrero de ala ancha: la melena revuelta sube en dos cuernos curvos altos y los
# mechones de los lados caen abiertos y ondulados hasta los hombros
_c = _fix('cs-protocol-omega-3-0:quebec')
_c['front'] = [L(outline([(14, 74), (-6, 84), (-22, 104, 1), (-14, 80), (-20, 66, 1), (-4, 56), (-2, 34), (6, 12), (12, -6), (2, -30), (8, -46, 1), (20, -18), (36, -10),
                          (50, -12), (64, -10), (80, -18), (92, -46, 1), (98, -30), (88, -6), (96, 14), (102, 34), (104, 56), (120, 66, 1), (114, 80), (122, 104, 1),
                          (106, 84), (86, 74), (84, 60), (16, 60)])),
               L(outline([(60, -8), (86, 0), (100, 40), (110, 76), (88, 72), (80, 40)]), 'shade', 'b', False),
               strand([(-2, 60), (-10, 80), (-16, 96)], 'shade', 'b', 1.2), strand([(102, 60), (110, 80), (116, 96)], 'shade', 'b', 1.2),
               _fringe([(12, 70), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (88, 70), (80, 56), (74, 64, 1), (68, 48), (60, 58, 1), (56, 44), (42, 84, 1),
                        (34, 64), (28, 76, 1), (20, 60)])]
_c['side'] = [L(outline([(54, 62), (60, 48), (80, 48), (92, 34), (90, 14), (80, 0), (78, -26), (84, -44, 1), (66, -24), (60, -6), (40, -6), (20, 4), (6, 26), (-12, 48),
                         (-30, 60, 1), (-14, 66), (-6, 88), (-14, 104, 1), (8, 92), (24, 84), (40, 78), (46, 70)])),
              L(outline([(-12, 50), (8, 40), (26, 70), (4, 86)]), 'shade', 'b', False),
              _fringe([(66, 4), (90, 18), (96, 42), (94, 70, 1), (86, 54), (80, 66, 1), (76, 44), (66, 30)])]
_c['back'] = [L(outline([(14, 80), (-6, 86), (-22, 104, 1), (-14, 80), (-20, 66, 1), (-4, 56), (-2, 34), (6, 12), (12, -6), (2, -30), (8, -46, 1), (20, -18), (36, -10),
                         (50, -12), (64, -10), (80, -18), (92, -46, 1), (98, -30), (88, -6), (96, 14), (102, 34), (104, 56), (120, 66, 1), (114, 80), (122, 104, 1),
                         (106, 86), (86, 80), (50, 88)]), 'shade'),
              L(outline([(12, -6), (2, -30), (8, -46, 1), (20, -18), (36, -10), (50, -12), (64, -10), (80, -18), (92, -46, 1), (98, -30), (88, -6), (96, 30),
                         (50, 46), (4, 30)]), 'mid', 'b', False)]

# ============================================================== Shiroshika Gumi (cs-shiroshika-gumi)
# Kaburo Hayama: de espaldas, la coleta alta cae como una cortina larga y ancha por el centro de la espalda (no de lado)
_c = _fix('cs-shiroshika-gumi:kaburo-hayama', 'kaburo-hayama')
_c['back'] = [L(outline([(16, 84), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 84), (50, 92)])),
              L(outline([(56, 6), (84, 18), (92, 50), (84, 80), (62, 88)]), 'shade', 'b', False),
              L(outline([(40, 4), (42, -26), (56, -38), (72, -26), (66, 0), (74, 40), (80, 100), (76, 132, 1), (64, 118), (54, 136, 1), (44, 116), (32, 130, 1),
                         (26, 96), (32, 40)]), 'mid', 'f', ln=True),
              L(outline([(58, 0), (70, 40), (76, 100), (74, 128), (64, 114), (56, 60)]), 'shade', 'f', False)]

# ============================================================== The Lagoon (cs-the-lagoon)
# Hippos Kohlt: de espaldas no hay una placa blanca en la nuca: el pelo gris le baja hasta el cuello
_c = _fix('cs-the-lagoon:hippos-kohlt', 'hippos-kohlt')
_c['back'] = [dict(_c['back'][0], c='shade')] + _c['back'][1:]

# ============================================================== Tsukigami no Ichizoku (cs-tsukigami-no-ichizoku)
# Gerald Fuss y Wolfram Vulpeen: de espaldas la mancha oscura en mitad del pelo parecía un agujero; en el modelo la nuca es
# toda pelo
for _k in ('gerald-fuss', 'wolfram-vulpeen'):
    _c = _fix(f'cs-tsukigami-no-ichizoku:{_k}', _k)
    _c['back'] = [l for l in _c['back'] if isinstance(l, list) or l.get('c') != 'deep']
