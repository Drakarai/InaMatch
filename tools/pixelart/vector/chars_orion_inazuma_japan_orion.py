"""Inazuma Japón (Orion) (orion-inazuma-japan-orion): la selección japonesa de Orion no Kokuin. La wiki la lista con las
versiones de Ares (Endou_AT, Kidou_AT, Gouenji_AT...) y la enciclopedia solo tiene sus modelos 3D de Ares (アレスの天秤),
salvo Ichihoshi (オリオンの刻印). Todos van como 'orion:<id>': los que ya estaban dibujados de Ares con el mismo modelo se
reutilizan; Endou, Kazemaru y Gouenji de Ares no estaban dibujados (sus equipos de Ares cogían los de IE).
El 15 de la plantilla (xavier-foster) es Kiyama Tatsuya (el Hiroto de IE en Ares), no Hiroto Kiyama de IE2.
El 13 es Ichihoshi: lucas-star es Mitsuru (antes de darse cuenta, ceño fruncido) y lucas-star-ok-hikaru es Hikaru."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

O = 'orion'
# mismo modelo 3D que en Ares
for _pid, _src in {'caleb-stonewall': 'ares:caleb-stonewall', 'jude-sharp': 'ares-seishou-gakuen:jude-sharp', 'xavier-schiller': 'ares:xavier-schiller',
                   'shawn-froste': 'ares:shawn-froste', 'byron-love': 'ares:byron-love', 'xavier-foster': 'ares:xavier-foster',
                   'billy-miller': 'billy-miller', 'valentin-eisner': 'valentin-eisner', 'sonny-wright': 'sonny-wright',
                   'adriano-donati': 'adriano-donati', 'heath-moore': 'heath-moore', 'cliff-parker': 'cliff-parker',
                   'lucas-star-ok-hikaru': 'lucas-star',
                   # Endou, Kazemaru y Gouenji de Ares tienen el mismo diseño que los de IE (cinta y mechones, coleta, pinchos)
                   'mark-evans': 'mark-evans', 'axel-blaze': 'axel-blaze'}.items():
    CHARS[f'{O}:{_pid}'] = CHARS[_src]

# Ichihoshi Mitsuru (lucas-star, antes de darse cuenta): el mismo pelo azul marino en seta que Hikaru (modelo オリオンの刻印
# con la camiseta de Japón), pero con la mirada afilada de párpados caídos, el ceño fruncido y la boca recta
CHARS[f'{O}:lucas-star'] = copy.deepcopy(CHARS['lucas-star'])
CHARS[f'{O}:lucas-star']['face'].update({'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97})

# Kazemaru de Ares: el mismo peinado que en IE (coleta alta, flequillo que tapa un ojo), pero la goma de la coleta es oscura
CHARS[f'{O}:nathan-swift'] = copy.deepcopy(CHARS['nathan-swift'])
CHARS[f'{O}:nathan-swift']['pal']['tie'] = (52, 60, 64, 255)

# Haizaki: el mismo modelo que en Ares, pero el modelo 3D y el sprite de la wiki no tienen ningún mechón rojo en el flequillo
# (es gris entero); se quita esa capa
CHARS[f'{O}:elliot-ember'] = copy.deepcopy(CHARS['elliot-ember'])
CHARS[f'{O}:elliot-ember']['front'] = [l for l in CHARS[f'{O}:elliot-ember']['front'] if l['c'] != 'red']
