"""Correcciones de la revisión de diseños (grupo vra): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS, L, outline  # noqa: F401

# ------------------------------------------------------------------ tipo de cuerpo
# Los modelos 3D de cuerpo entero de estos son tan bajitos como los 'bajito' (de 368 a 424 px frente a los 443-630 de los
# normales y delgados): eran 'normal'/'delgado' y en el partido salían tan altos como el resto.
for _t, _k in (('vr-destroyers', 'declan-jaxor'), ('vr-ai-gakuen', 'vr:eugenio-provost'), ('vr-ai-gakuen', 'vr:chayce-golana'),
               ('vr-houreikan', 'alzen-wasruff'), ('vr-keizen-arashiyama', 'elijah-singleton')):
    _c = copy.deepcopy(CHARS[_k])
    _c['body'] = 'bajito'
    CHARS[f"{_t}:{_k.split(':')[-1]}"] = _c

# ------------------------------------------------------------------ Umi Kamome
# Kata Caballo: la piel del modelo es morena clara (tostada, con rubor), no marrón oscura
_c = copy.deepcopy(CHARS['vr:kata-caballo'])
_c['pal']['skin'] = (226, 160, 124, 255)
_c['pal']['skin_d'] = tuple(int(v * 0.86) for v in _c['pal']['skin'][:3]) + (255,)
CHARS['vr-umi-kamome-soccer-club:kata-caballo'] = _c

# Summers Laughlin: el pelo es un casco redondeado (de frente y de espaldas no acaba en punta como una gota)
_c = copy.deepcopy(CHARS['vr:summers-laughlin'])
_c['front'][0] = L(outline([(16, 80), (12, 56), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (88, 56), (84, 80), (78, 60), (22, 60)]))
_c['front'][1] = L(outline([(58, 4), (74, 12), (86, 36), (84, 74), (74, 40)]), 'shade', 'b', False)
_c['side'][0] = L(outline([(58, 62), (60, 52), (78, 48), (86, 34), (78, 12), (56, 2), (34, 4), (14, 20), (6, 46), (10, 70), (24, 80), (40, 74), (48, 62)]))
_c['back'][0] = L(outline([(16, 80), (12, 56), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (88, 56), (84, 80), (50, 88)]))
CHARS['vr-umi-kamome-soccer-club:summers-laughlin'] = _c
