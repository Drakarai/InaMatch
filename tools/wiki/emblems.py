"""Descarga el escudo de cada equipo de la wiki inglesa de Inazuma Eleven.

Busca los archivos "<equipo> emblem*.png" y prefiere el rehecho para Victory Road ("X emblem (VR).png");
si no lo hay, el de los juegos de DS ("X emblem.png"), el de Strikers (S) o el de las cartas (SD). Los guarda en
src/assets/pack/emblems/<id del equipo>.png a 160 px (los de pixel art se amplían sin suavizar),
que el juego carga solo.

Uso (desde la raíz del repo, después de tools/wiki/teams.py): python3 -I tools/wiki/emblems.py
"""
import glob
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de escudos)'
SIZE = 160
OUT = os.path.join(ROOT, 'src', 'assets', 'pack', 'emblems')

# equipos cuyo escudo está con otro nombre en la wiki
ALIAS = {
    'Dark Emperors (cloaked)': ['Dark Emperors'],
    'Inazuma Eleven': ['Inazuma Eleven (team)', 'Raimon OB'],
    "Ichibangai Sally's": ['Sallys', "Sally's"],
    'Inazuma KFC': ['Inazuma Kids FC', 'Inazuma KFC'],
    'Real Inazuma': ['Real Inazuma', 'Inazuma Japan'],
}
# escudos que solo están en la wiki española
ES_API = 'https://inazuma.fandom.com/es/api.php'
ES_FILES = {'Osaka Gals CCC': 'Escudo - Triple C de Osaka (SD).png'}
# orden de preferencia de las variantes del archivo
VARIANTS = [' (VR)', '', ' (S)', ' (SD)', ' (X)']


def get(params, api=API):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(api + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError('la wiki no responde')


def candidates(name):
    """Archivos "<name> emblem..." que existen en la wiki."""
    found = []
    for prefix in (f'{name} emblem', f'{name}_emblem'):
        data = get({'action': 'query', 'list': 'allimages', 'aiprefix': prefix, 'ailimit': '50', 'aiprop': 'url|size'})
        found += [i for i in data['query']['allimages'] if i not in found]
    return found


def best(files, name):
    by_name = {f['name'].replace('_', ' ').rsplit('.', 1)[0]: f for f in files}
    for v in VARIANTS:
        if f'{name} emblem{v}' in by_name:
            return by_name[f'{name} emblem{v}']
    return None


def download(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        img = Image.open(io.BytesIO(r.read())).convert('RGBA')
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    if max(img.size) * 2 <= SIZE:
        # los de DS son pixel art pequeño: se amplían a un múltiplo entero, sin suavizar
        k = SIZE // max(img.size)
        img = img.resize((img.width * k, img.height * k), Image.NEAREST)
    img.thumbnail((SIZE, SIZE), Image.LANCZOS)
    canvas = Image.new('RGBA', (SIZE, SIZE))
    canvas.paste(img, ((SIZE - img.width) // 2, (SIZE - img.height) // 2))
    return canvas


def main():
    os.makedirs(OUT, exist_ok=True)
    missing = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json'))):
        team = json.load(open(path, encoding='utf-8'))
        wiki = team.get('wiki')
        if not wiki:
            continue
        chosen = None
        for name in ALIAS.get(wiki, []) + [wiki]:
            chosen = best(candidates(name), name)
            time.sleep(0.3)
            if chosen:
                break
        if not chosen and wiki in ES_FILES:
            data = get({'action': 'query', 'titles': 'File:' + ES_FILES[wiki], 'prop': 'imageinfo', 'iiprop': 'url'}, ES_API)
            info = data['query']['pages'][0].get('imageinfo')
            chosen = info and {'name': ES_FILES[wiki], 'url': info[0]['url']}
        if not chosen:
            missing.append(f"{team['id']} ({wiki})")
            continue
        try:
            image = download(chosen['url'])
        except OSError as err:
            sys.exit(f'no se pudo bajar {chosen["url"]}: {err}\n'
                     '(las imágenes de la wiki están en static.wikia.nocookie.net: tiene que estar permitido en la red)')
        image.save(os.path.join(OUT, team['id'] + '.png'), optimize=True)
        print(f"{team['id']}: {chosen['name']}", file=sys.stderr)
        time.sleep(0.3)
    if missing:
        print('sin escudo:', ', '.join(missing), file=sys.stderr)


if __name__ == '__main__':
    main()
