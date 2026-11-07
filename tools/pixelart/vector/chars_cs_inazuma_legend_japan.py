"""Inazuma Legend Japan (cs-inazuma-legend-japan): los héroes de Inazuma Japón que viajan a Chrono Stone. Sus modelos 3D de
Chrono Stone son los de Inazuma Japón (IE3), así que llevan el mismo dibujo que en ie3-inazuma-japan: la versión 'ie3:<id>'
si la hay (Xavier ya humano, Caleb sin la marca roja) y si no, la de siempre."""
from chars import CHARS

for _pid in ('mark-evans', 'nathan-swift', 'jack-wallside', 'hurley-kane', 'xavier-foster', 'caleb-stonewall', 'jude-sharp', 'kevin-dragonfly',
             'shawn-froste', 'axel-blaze', 'david-samford'):
    if f'ie3:{_pid}' in CHARS:
        CHARS[f'cs-inazuma-legend-japan:{_pid}'] = CHARS[f'ie3:{_pid}']
