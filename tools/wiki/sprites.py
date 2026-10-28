"""Cabezas en pixel art y retratos de cada jugador, sacados de la wiki inglesa de Inazuma Eleven.

Por cada jugador de src/data/teams/*.json busca en la página de su personaje:
- El retrato de los juegos de DS, "(equipo) Nombre sprite.png" (64x64, pixel art). De él se recorta la
  cabeza, se reduce a la escala de los sprites de campo de IE3 y se guarda en
  src/assets/pack/heads/<id>.png. El juego le pone debajo el cuerpo con la equipación de cada equipo.
- El retrato de Victory Road, "Nombre sprite (VR).png", que se guarda en src/assets/pack/portraits/<id>.png
  para la ficha del jugador y la animación de las supertécnicas.

Lo que ya esté en src/assets/pack/sprites/ (sprites completos puestos a mano) tiene prioridad en el juego.

Uso (desde la raíz del repo): python3 -I tools/wiki/sprites.py [--force]
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
UA = 'InaMatch-fan-project/0.1 (descarga puntual de retratos)'
PACK = os.path.join(ROOT, 'src', 'assets', 'pack')
HEAD_W = 22
PORTRAIT = 128


def get(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError('la wiki no responde')


def download(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return Image.open(io.BytesIO(r.read())).convert('RGBA')
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError(f'no se pudo bajar {url}')


def page_images(pages):
    """Imágenes que usa cada página (con las redirecciones resueltas)."""
    out = {}
    for i in range(0, len(pages), 50):
        chunk = pages[i : i + 50]
        cont = {}
        while True:
            q = get({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'images', 'imlimit': 'max', 'redirects': '1', **cont})
            alias = {r['from']: r['to'] for r in q['query'].get('normalized', []) + q['query'].get('redirects', [])}
            by = {p['title']: p for p in q['query']['pages']}
            for t in chunk:
                f = alias.get(alias.get(t, t), alias.get(t, t))
                out.setdefault(t, []).extend(im['title'][5:] for im in by.get(f, {}).get('images', []))
            if 'continue' not in q:
                break
            cont = q['continue']
        time.sleep(0.4)
    return out


def file_urls(files):
    out = {}
    for i in range(0, len(files), 50):
        q = get({'action': 'query', 'titles': '|'.join('File:' + f for f in files[i : i + 50]), 'prop': 'imageinfo', 'iiprop': 'url'})['query']
        back = {n['to']: n['from'] for n in q.get('normalized', [])}
        for p in q['pages']:
            if p.get('imageinfo'):
                out[back.get(p['title'], p['title'])[5:]] = p['imageinfo'][0]['url']
        time.sleep(0.3)
    return out


def pick(images, name):
    """El retrato de DS ("(R) Endou Mamoru sprite.png") y el de Victory Road del personaje."""
    base = re.escape(name)
    ds = [f for f in images if re.fullmatch(r'\([^)]+\) ' + base + r' sprite\.png', f)]
    vr = [f for f in images if re.fullmatch(r'(?:\([^)]+\) )?' + base + r' sprite \(VR\)\.png', f)]
    # sin prefijo de equipo antes que con prefijo (el de VR "genérico")
    vr.sort(key=lambda f: f.startswith('('))
    return (ds[0] if ds else None), (vr[0] if vr else None)


def head(img):
    """Cabeza del retrato de DS a la escala de los sprites de campo: paleta corta y bordes nítidos."""
    bbox = img.getbbox()
    img = img.crop((bbox[0], bbox[1], bbox[2], bbox[1] + int((bbox[3] - bbox[1]) * 0.78)))
    h = round(img.height * HEAD_W / img.width)
    small = img.resize((HEAD_W, h), Image.BOX)
    alpha = small.getchannel('A').point(lambda a: 255 if a > 110 else 0)
    rgb = small.convert('RGB').quantize(colors=14, method=Image.Quantize.MEDIANCUT).convert('RGBA')
    rgb.putalpha(alpha)
    return rgb


def portrait(img):
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    img.thumbnail((PORTRAIT, PORTRAIT), Image.LANCZOS)
    canvas = Image.new('RGBA', (PORTRAIT, PORTRAIT))
    canvas.paste(img, ((PORTRAIT - img.width) // 2, PORTRAIT - img.height))
    return canvas


def main():
    force = '--force' in sys.argv
    players = {}
    for path in sorted(glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json'))):
        for p in json.load(open(path, encoding='utf-8'))['players']:
            if p.get('wiki'):
                players.setdefault(p['id'], p['wiki'])
    os.makedirs(os.path.join(PACK, 'heads'), exist_ok=True)
    os.makedirs(os.path.join(PACK, 'portraits'), exist_ok=True)
    todo = {pid: w for pid, w in players.items() if force or not os.path.exists(os.path.join(PACK, 'heads', pid + '.png'))}
    images = page_images(sorted(set(todo.values())))
    chosen = {pid: pick(images.get(w, []), w) for pid, w in todo.items()}
    urls = file_urls(sorted({f for pair in chosen.values() for f in pair if f}))
    no_head, no_portrait = [], []
    for n, (pid, (ds, vr)) in enumerate(sorted(chosen.items())):
        if ds and ds in urls:
            head(download(urls[ds])).save(os.path.join(PACK, 'heads', pid + '.png'), optimize=True)
        else:
            no_head.append(pid)
        if vr and vr in urls:
            portrait(download(urls[vr])).save(os.path.join(PACK, 'portraits', pid + '.png'), optimize=True)
        else:
            no_portrait.append(pid)
        if n % 50 == 0:
            print(f'{n}/{len(chosen)}', file=sys.stderr)
        time.sleep(0.1)
    print(f'{len(players)} jugadores; sin cabeza de DS: {len(no_head)}, sin retrato de VR: {len(no_portrait)}', file=sys.stderr)
    if no_head:
        print('sin cabeza:', ', '.join(no_head), file=sys.stderr)


if __name__ == '__main__':
    main()
