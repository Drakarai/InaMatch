"""Colores reales de cada supertécnica, sacados de los fotogramas de su vídeo en la enciclopedia oficial.

Lee las capturas <id>_<n>.png de una carpeta (las hace tools/zukan/frames.cjs) y, para cada técnica,
busca los colores más llamativos: descarta el verde del césped, los grises y las siluetas oscuras de
los jugadores y se queda con los tres más vivos y abundantes.

Uso: python3 -I tools/zukan/palette.py <carpeta de capturas> <salida.json>
"""
import colorsys
import glob
import json
import os
import sys
from collections import Counter, defaultdict

from PIL import Image


def is_background(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    if v < 0.22 or s < 0.28:
        return True  # siluetas, sombras, blancos y grises
    if 0.25 < h < 0.40 and 0.3 < s < 0.8 and 0.3 < v < 0.75:
        return True  # césped
    return False


def palette(paths, n=3):
    n_search = 8
    counts = Counter()
    for p in paths:
        im = Image.open(p).convert('RGB').resize((160, 90))
        q = im.quantize(colors=24, method=Image.Quantize.MEDIANCUT)
        pal = q.getpalette()
        for count, idx in q.getcolors():
            r, g, b = pal[idx * 3 : idx * 3 + 3]
            if is_background(r, g, b):
                continue
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            # agrupa tonos parecidos y premia los vivos
            key = (round(h * 18) % 18, round(s * 3), round(v * 3))
            counts[key] += count * (0.4 + s) * (0.4 + v)
    picked = []
    for (hk, sk, vk), _ in counts.most_common():
        if any(min(abs(hk - p[0]), 18 - abs(hk - p[0])) < 2 and abs(vk - p[2]) < 1 for p in picked):
            continue
        picked.append((hk, sk, vk))
        if len(picked) == n_search:
            break
    # fuera los tonos apagados (gradas, sombras del estadio) si hay de sobra vivos
    vivid = [c for c in picked if c[1] >= 2 and c[2] >= 2]
    picked = vivid if len(vivid) >= 2 else picked
    out = []
    for hk, sk, vk in picked:
        r, g, b = colorsys.hsv_to_rgb(hk / 18, min(1, sk / 3 + 0.1), min(1, vk / 3 + 0.08))
        out.append('#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)))
    return out[:n]


def main():
    folder, dest = sys.argv[1], sys.argv[2]
    frames = defaultdict(list)
    for f in glob.glob(os.path.join(folder, '*_*.png')):
        frames[os.path.basename(f).rsplit('_', 1)[0]].append(f)
    result = {mid: palette(sorted(fs)[1:-1] or sorted(fs)) for mid, fs in sorted(frames.items())}
    json.dump(result, open(dest, 'w'), indent=1)
    print(len(result), 'técnicas', file=sys.stderr)


if __name__ == '__main__':
    main()
