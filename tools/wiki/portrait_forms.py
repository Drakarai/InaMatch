"""Foto de perfil de la FORMA con la que juega cada jugador en cada equipo (después de sprites.py).

sprites.py elige el retrato por el prefijo de equipo más repetido, y falla con los que en un equipo juegan con otra forma
(adultos del Inazuma Japón Legendario, Mixi Max, Épsilon Plus, Chaos, las versiones de Ares y Orion...). Aquí, para cada
jugador de cada equipo:
- su forma: si su id lleva la clave de la forma (los que salen dos veces, como 'sol-daystar-cs-amemiya-mm'), esa; si no,
  la de la tabla de miembros de la página del equipo en la wiki (Desarm_EK, Endou_ILJ...);
- su imagen: el archivo de esa forma en Module:PlayerData/<juego> (el de Victory Road, o el único que tenga si es una
  forma propia como _AT, _OK, _MM, _C);
y si la foto guardada no es esa, se sustituye (con sus rasgos de looks.json).

Uso (desde la raíz del repo): python3 -I tools/wiki/portrait_forms.py [--dry-run]
"""
import glob
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from PIL import Image, ImageChops, ImageStat

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sprites as SP  # noqa: E402

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.cache', 'forms')
GAMES = ('IE', 'IE2', 'IE3', 'GO', 'CS', 'GX', 'AT', 'OK', 'VR')
SEASON_GAME = {'ie1': 'IE', 'ie2': 'IE2', 'ie3': 'IE3', 'go': 'GO', 'cs': 'CS', 'gx': 'GX', 'ares': 'AT', 'orion': 'OK', 'vr': 'VR'}


def api(params):
    url = SP.API + '?' + urllib.parse.urlencode({**params, 'format': 'json'})
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': SP.UA}), timeout=90).read())


def wikitext(titles):
    out = {}
    for i in range(0, len(titles), 40):
        d = api({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': 1, 'titles': '|'.join(titles[i:i + 40])})
        back = {r['to']: r['from'] for r in d['query'].get('redirects', []) + d['query'].get('normalized', [])}
        for p in d['query']['pages'].values():
            t = back.get(p['title'], p['title'])
            t = back.get(t, t)
            out[t] = p['revisions'][0]['slots']['main']['*'] if 'revisions' in p else ''
    return out


def cached(name, fetch):
    path = os.path.join(CACHE, name)
    if os.path.exists(path):
        return json.load(open(path))
    data = fetch()
    json.dump(data, open(path, 'w'))
    return data


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def entries():
    """(juego, clave) -> {page, files}: las fichas de Module:PlayerData/<juego>."""
    mods = cached('modules.json', lambda: wikitext([f'Module:PlayerData/{g}' for g in GAMES]))
    ent = {}
    for mod, txt in mods.items():
        g = mod.split('/')[-1]
        for m in re.finditer(r'\n\t([A-Za-z0-9_]+)\s*=\s*\{(.*?)\n\t\},?', txt, re.S):
            body = m.group(2)
            pg = re.search(r'\bpage\s*=\s*"([^"]*)"', body)
            f = re.search(r'\bfile\s*=\s*(\{.*?\}|"[^"]*")', body, re.S)
            files = {}
            if f:
                files = {'*': f.group(1).strip('"')} if f.group(1).startswith('"') else dict(re.findall(r'\b(\w+)\s*=\s*"([^"]*)"', f.group(1)))
            ent[(g, m.group(1))] = {'page': pg.group(1) if pg else None, 'files': files}
    return ent


def forms(ent, teams):
    """{equipo: {jugador: (juego, clave, archivo)}}"""
    pages = cached('teampages.json', lambda: wikitext(sorted({t['wiki'] for t in teams if t.get('wiki')})))

    def find(k, prefer):
        return next(((g, k) for g in (prefer,) + GAMES if (g, k) in ent), None)

    out = {}
    for t in teams:
        game = SEASON_GAME[t['id'].split('-')[0]]
        txt = pages.get(t.get('wiki'), '')
        tables = re.findall(r'\{\{#invoke:MemberTable\|main(.*?)\}\}', txt, re.S)
        table = next((tb for tb in tables if re.search(r'\|\s*game\s*=\s*' + game + r'\s*[|\n]', tb)), tables[0] if tables else '')
        bypage = {}
        for k in (m.group(1).strip() for m in re.finditer(r'\|\s*p\d+\s*=\s*([^|\n}]+)', table)):
            e = find(k, game)
            if e and ent[e]['page']:
                bypage.setdefault(ent[e]['page'], []).append(e)
        used, res = {}, {}
        for p in t['players']:
            w, base = p.get('wiki'), slug(p['name'])
            e = None
            suffix = p['id'][len(base) + 1:] if p['id'].startswith(base + '-') else ''
            m = re.match(r'(ie|ie2|ie3|go|cs|gx|vr|at|ok)-(.+)$', suffix)
            if m:  # el id lleva su forma (el mismo jugador sale dos veces en el equipo)
                cands = sorted((key for key in ent if slug(key[1]) == m.group(2) and ent[key]['page'] == w), key=lambda key: key[0] != m.group(1).upper())
                e = cands[0] if cands else None
            if not e:
                ks = bypage.get(w, [])
                i = used.get(w, 0)
                used[w] = i + 1
                e = ks[min(i, len(ks) - 1)] if ks else None
            if not e:
                continue
            files = ent[e]['files']
            # la imagen de Victory Road; si es una forma propia sin ella (_AT, _OK, _MM...), su único archivo
            f = files.get('VR') or (files.get('*') or files.get(game) if '_' in e[1] else None)
            if f:
                res[p['id']] = (e[0], e[1], f)
        out[t['id']] = res
    return out


def main():
    dry = '--dry-run' in sys.argv
    os.makedirs(CACHE, exist_ok=True)
    teams = [json.load(open(f, encoding='utf-8')) for f in sorted(glob.glob(os.path.join(SP.ROOT, 'src', 'data', 'teams', '*.json'))) if not f.endswith('club.json')]
    plan = forms(entries(), teams)
    files = sorted({v[2] + '.png' for r in plan.values() for v in r.values()})
    urls = {}
    for i in range(0, len(files), 45):
        d = api({'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': '|'.join('File:' + f for f in files[i:i + 45])})
        norm = {n['to']: n['from'] for n in d['query'].get('normalized', [])}
        for p in d['query']['pages'].values():
            if 'imageinfo' in p:
                urls[norm.get(p['title'], p['title'])[5:]] = p['imageinfo'][0]['url']
    os.makedirs(SP.CACHE, exist_ok=True)

    def load(fn):
        try:
            return fn, SP.fetch(urls[fn], os.path.join(SP.CACHE, re.sub(r'[^A-Za-z0-9]+', '_', fn)))
        except Exception:  # noqa: BLE001
            return fn, None

    with ThreadPoolExecutor(8) as ex:
        imgs = {fn: im for fn, im in ex.map(load, [f for f in files if f in urls]) if im is not None}
    print(f'{sum(len(r) for r in plan.values())} jugadores con su forma; imágenes: {len(imgs)} de {len(files)}', file=sys.stderr)
    looks_path = os.path.join(SP.ROOT, 'src', 'data', 'looks.json')
    looks = json.load(open(looks_path))
    changed = []
    for tid, r in plan.items():
        for pid, (g, k, f) in r.items():
            img = imgs.get(f + '.png')
            if img is None:
                continue
            if max(img.size) < 120:  # sprites de DS de cuerpo entero (Chaos, Fire Dragon...): peor que la foto que haya
                continue
            if max(img.size) < SP.PORTRAIT:  # retratos pequeños: se amplían
                s = SP.PORTRAIT / max(img.size)
                img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
            new = SP.portrait(img)
            dest = os.path.join(SP.ROOT, 'src', 'assets', 'pack', 'portraits', tid, pid + '.webp')
            if os.path.exists(dest):
                cur = Image.open(dest).convert('RGBA').resize((64, 64))
                if sum(ImageStat.Stat(ImageChops.difference(cur, new.convert('RGBA').resize((64, 64)))).mean[:3]) / 3 <= 6:
                    continue
            changed.append((tid, pid, k, f))
            if not dry:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                new.save(dest, 'WEBP', quality=86, method=6)
                looks[f'{tid}:{pid}'] = SP.looks(img)
    if not dry:
        with open(looks_path, 'w', encoding='utf-8') as fh:
            fh.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v)}' for k, v in sorted(looks.items())) + '\n}\n')
    json.dump(changed, open(os.path.join(CACHE, 'changed.json'), 'w'), indent=0)
    print(f'{"distintas" if dry else "cambiadas"}: {len(changed)}', file=sys.stderr)


if __name__ == '__main__':
    main()
