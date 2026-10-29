"""Retratos de Victory Road de cada jugador y sus rasgos para dibujar el sprite de campo.

- Retrato: "(equipo) Nombre sprite (VR).png" de la categoría "Victory Road sprites" de la wiki inglesa de
  Inazuma Eleven, con la equipación del equipo en el que juega. Se guarda en
  src/assets/pack/portraits/<equipo>/<jugador>.webp para la ficha y la animación de las supertécnicas.
- Rasgos: del retrato se sacan el color del pelo, de la piel y de los ojos, la silueta del peinado a la
  escala del sprite de campo y, si lo hay, un accesorio (cinta, gafas...). Van a src/data/looks.json
  ("<equipo>:<jugador>"); el juego dibuja con ellos un muñeco en pixel art
  parecido a cada jugador (src/gfx/placeholders.ts).

Uso (desde la raíz del repo): python3 -I tools/wiki/sprites.py [--force]
"""
import colorsys
import glob
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de retratos)'
OUT = os.path.join(ROOT, 'src', 'assets', 'pack', 'portraits')
CACHE = os.path.join(ROOT, 'tools', 'wiki', '.cache', 'vr')
PORTRAIT = 192
# silueta del pelo: rejilla de la cabeza del sprite (ancho x alto, en píxeles del sprite)
HAIR_W, HAIR_H = 22, 20


def get(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError('la wiki no responde')


def vr_files():
    files, cont = [], {}
    while True:
        q = get({'action': 'query', 'list': 'categorymembers', 'cmtitle': 'Category:Victory Road sprites', 'cmlimit': 'max', 'cmtype': 'file', **cont})
        files += [m['title'][5:] for m in q['query']['categorymembers']]
        if 'continue' not in q:
            return files
        cont = q['continue']
        time.sleep(0.3)


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


def fetch(url, dest):
    if not os.path.exists(dest):
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    open(dest, 'wb').write(r.read())
                break
            except OSError:
                time.sleep(2 ** attempt)
        time.sleep(0.05)
    return Image.open(dest).convert('RGBA')


# ------------------------------------------------------------------ rasgos

def hsv(c):
    return colorsys.rgb_to_hsv(c[0] / 255, c[1] / 255, c[2] / 255)


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a[:3], b[:3])) ** 0.5


def hexc(c):
    return '#%02x%02x%02x' % tuple(int(x) for x in c[:3])


def dominant(img, box, keep, step=6):
    """Color más frecuente (agrupado) de una zona del retrato entre los píxeles que cumplen `keep`."""
    px = img.load()
    count = Counter()
    x0, y0, x1, y1 = box
    for y in range(y0, y1):
        for x in range(x0, x1):
            c = px[x, y]
            if c[3] > 200 and keep(c):
                count[(c[0] // step * step, c[1] // step * step, c[2] // step * step)] += 1
    return count.most_common(1)[0][0] if count else None


def looks(img):
    """Pelo, piel, ojos y silueta del peinado. El retrato de VR es un busto de frente sobre transparente:
    la cara ocupa el centro y el pelo la parte de arriba y los lados."""
    W, H = img.size
    bright = lambda c: hsv(c)[2] > 0.3
    # piel: mejillas
    skin = dominant(img, (int(W * 0.38), int(H * 0.54), int(W * 0.62), int(H * 0.66)), bright) or (241, 199, 155)
    # pelo: parte de arriba, sin bordes oscuros ni nada parecido a la piel
    hair = dominant(img, (int(W * 0.15), int(H * 0.02), int(W * 0.85), int(H * 0.3)), lambda c: hsv(c)[2] > 0.18 and dist(c, skin) > 45, 10)
    hair = hair or (60, 40, 26)
    # silueta del pelo: la cabeza (sin hombros), píxel a píxel "¿se parece más al pelo que a la piel?"
    head = img.crop((0, 0, W, int(H * 0.74)))
    hb = head.getbbox() or (0, 0, W, H)
    bbox_top = hb[1]
    head = head.crop(hb)
    hp = head.load()

    def classify(factor):
        mask = Image.new('L', head.size)
        smask = Image.new('L', head.size)
        mp, sp = mask.load(), smask.load()
        for y in range(head.height):
            for x in range(head.width):
                c = hp[x, y]
                if c[3] > 128:
                    dh, ds = dist(c, hair), dist(c, skin)
                    if dh < 120 * max(1, factor) and dh < ds * factor:
                        mp[x, y] = 255
                    elif ds < 110 or (hsv(c)[2] < 0.3 and ds < 200):
                        sp[x, y] = 255  # piel (y las líneas oscuras de la cara, que se quedan dentro)
        return mask, smask

    mask, smask = classify(0.9)
    # pelo muy claro (blanco, rosa pálido...) que se confunde con la piel: más margen para el pelo
    if sum(1 for v in mask.resize((HAIR_W, HAIR_H), Image.BOX).getdata() if v > 90) < 40:
        mask, smask = classify(1.35)
    # accesorio (cinta, gafas...): color vivo en la frente que no es ni pelo ni piel
    acc = dominant(img, (int(W * 0.2), int(H * 0.22), int(W * 0.8), int(H * 0.44)),
                   lambda c: hsv(c)[1] > 0.6 and hsv(c)[2] > 0.45 and dist(c, hair) > 90 and dist(c, skin) > 90, 16)
    amask = Image.new('L', head.size)
    if acc:
        ap = amask.load()
        for y in range(head.height):
            for x in range(head.width):
                c = hp[x, y]
                if c[3] > 128 and dist(c, acc) < 60:
                    ap[x, y] = 255
    # ojos: lo más oscuro y distinto de piel y pelo en la franja de los ojos
    eyes = dominant(img, (int(W * 0.3), int(H * 0.42), int(W * 0.7), int(H * 0.53)), lambda c: dist(c, skin) > 90 and dist(c, hair) > 70 and sum(c[:3]) < 560 and (not acc or dist(c, acc) > 80), 16)
    eyes = eyes or (40, 30, 30)
    # pupilas: lo muy oscuro de la franja de los ojos
    emask = Image.new('L', head.size)
    ep = emask.load()
    top = (H * 0.44 - bbox_top) / head.height
    bot = (H * 0.55 - bbox_top) / head.height
    for y in range(int(head.height * top), int(head.height * bot)):
        for x in range(int(head.width * 0.22), int(head.width * 0.78)):
            c = hp[x, y]
            if c[3] > 128 and hsv(c)[2] < 0.35 and dist(c, skin) > 120:
                ep[x, y] = 255
    small = mask.resize((HAIR_W, HAIR_H), Image.BOX)
    esmall = emask.resize((HAIR_W, HAIR_H), Image.BOX)
    ssmall = smask.resize((HAIR_W, HAIR_H), Image.BOX)
    asmall = amask.resize((HAIR_W, HAIR_H), Image.BOX)
    rows = []
    n_acc = 0
    for y in range(HAIR_H):
        row = ''
        for x in range(HAIR_W):
            if esmall.getpixel((x, y)) > 50:
                row += 'e'
            elif asmall.getpixel((x, y)) > 110 and y < HAIR_H * 0.7:
                row += 'a'
                n_acc += 1
            else:
                row += '#' if small.getpixel((x, y)) > 90 else 's' if ssmall.getpixel((x, y)) > 110 else '.'
        rows.append(row)
    out = {'hair': hexc(hair), 'skin': hexc(skin), 'eyes': hexc(eyes), 'head': rows}
    if n_acc >= 10:
        out['accessory'] = hexc(acc)
    else:
        out['head'] = [r.replace('a', '#') for r in rows]
    return out


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
    teams = {}
    for path in sorted(glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json'))):
        t = json.load(open(path, encoding='utf-8'))
        teams[t['id']] = [(p['id'], p['wiki']) for p in t['players'] if p.get('wiki')]
    # archivos de cada personaje, por prefijo de equipo ('' = sin prefijo)
    by_name = {}
    for fn in vr_files():
        m = re.fullmatch(r'(?:\(([^)]+)\) )?(.+?) sprite \(VR\)\.png', fn)
        if m:
            by_name.setdefault(m.group(2), {})[m.group(1) or ''] = fn
    # código de cada equipo en la wiki: el prefijo más repetido entre sus jugadores
    codes = {}
    for tid, players in teams.items():
        c = Counter(code for _, w in players for code in by_name.get(w, {}) if code)
        if c and c.most_common(1)[0][1] >= 3:
            codes[tid] = c.most_common(1)[0][0]
    # retrato de cada jugador en cada equipo: el de su equipo; si no, el de otro equipo suyo; si no, el genérico
    chosen = {}
    for tid, players in teams.items():
        for pid, w in players:
            files = by_name.get(w)
            if not files:
                continue
            own = files.get(codes.get(tid, '\0'))
            other = next((files[codes[t]] for t in teams if codes.get(t) in files and any(p == pid for p, _ in teams[t])), None)
            pref = next((f for code, f in sorted(files.items()) if code), None)
            chosen[(tid, pid)] = own or other or pref or files['']
    urls = file_urls(sorted(set(chosen.values())))
    os.makedirs(CACHE, exist_ok=True)
    looks_path = os.path.join(ROOT, 'src', 'data', 'looks.json')
    all_looks = {} if force else (json.load(open(looks_path)) if os.path.exists(looks_path) else {})
    for n, ((tid, pid), fn) in enumerate(sorted(chosen.items())):
        if fn not in urls:
            continue
        img = fetch(urls[fn], os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]+', '_', fn)))
        os.makedirs(os.path.join(OUT, tid), exist_ok=True)
        dest = os.path.join(OUT, tid, pid + '.webp')
        if force or not os.path.exists(dest):
            portrait(img).save(dest, 'WEBP', quality=86, method=6)
        key = f'{tid}:{pid}'
        if force or key not in all_looks:
            all_looks[key] = looks(img)
        if n % 100 == 0:
            print(f'{n}/{len(chosen)}', file=sys.stderr)
    with open(looks_path, 'w', encoding='utf-8') as f:
        f.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v)}' for k, v in sorted(all_looks.items())) + '\n}\n')
    total = sum(len(v) for v in teams.values())
    print(f'{total} jugadores en equipos; con retrato de Victory Road: {len(chosen)}; códigos de equipo: {len(codes)}/{len(teams)}', file=sys.stderr)


if __name__ == '__main__':
    main()
