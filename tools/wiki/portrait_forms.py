"""Retrato de Victory Road de la FORMA con la que juega cada jugador en cada equipo (después de sprites.py).

sprites.py elige el retrato por el prefijo de equipo más repetido, y falla con los que en un equipo juegan con otra forma
(adultos del Inazuma Japón Legendario, Mixi Max del Chrono Storm, Épsilon Plus...). Aquí, para cada equipo: la tabla de
miembros de su página de la wiki da la clave de la forma de cada jugador (Desarm_EK, Endou_ILJ...), Module:PlayerData/<juego>
da el archivo VR de esa forma, y si el retrato guardado no es ese, se sustituye (con sus rasgos de looks.json).

Uso (desde la raíz del repo): python3 -I tools/wiki/portrait_forms.py [--dry-run]
"""

import glob, json, os, re, sys, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sprites as SP
S = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.cache', 'forms')
os.makedirs(S, exist_ok=True)
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = {'User-Agent': 'InaMatch-fan-project/0.1'}
def api(params):
    return json.loads(urllib.request.urlopen(urllib.request.Request(API + '?' + urllib.parse.urlencode({**params, 'format': 'json'}), headers=UA), timeout=90).read())
def wikitext(titles):
    out = {}
    for i in range(0, len(titles), 40):
        d = api({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': 1, 'titles': '|'.join(titles[i:i + 40])})
        back = {r['to']: r['from'] for r in d['query'].get('redirects', []) + d['query'].get('normalized', [])}
        for p in d['query']['pages'].values():
            t = back.get(p['title'], p['title']); t = back.get(t, t)
            out[t] = p['revisions'][0]['slots']['main']['*'] if 'revisions' in p else ''
    return out
cache = f'{S}/modules.json'
if os.path.exists(cache):
    MOD = json.load(open(cache))
else:
    MOD = wikitext([f'Module:PlayerData/{g}' for g in ('IE', 'IE2', 'IE3', 'GO', 'CS', 'GX', 'AT', 'OK', 'VR', 'AC', 'X')])
    json.dump(MOD, open(cache, 'w'))
ENTRY = {}  # clave -> (page, vrfile)
for mod, t in MOD.items():
    for m in re.finditer(r'\n\t([A-Za-z0-9_]+)\s*=\s*\{(.*?)\n\t\},?', t, re.S):
        k, b = m.group(1), m.group(2)
        pg = re.search(r'\bpage\s*=\s*"([^"]*)"', b)
        f = re.search(r'\bfile\s*=\s*(\{.*?\}|"[^"]*")', b, re.S)
        vr = None
        if f:
            fv = f.group(1)
            mv = re.search(r'\bVR\s*=\s*"([^"]*)"', fv)
            vr = mv.group(1) if mv else None
        if k not in ENTRY or (vr and not ENTRY[k][1]):
            ENTRY[k] = (pg.group(1) if pg else None, vr)
GAME = {'ie1': 'IE', 'ie2': 'IE2', 'ie3': 'IE3', 'go': 'GO', 'cs': 'CS', 'gx': 'GX', 'ares': 'AT', 'orion': 'OK', 'vr': 'VR'}
teams = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(SP.ROOT, 'src', 'data', 'teams', '*.json'))) if not f.endswith('club.json')]
pcache = f'{S}/teampages.json'
PAGES = json.load(open(pcache)) if os.path.exists(pcache) else {}
need = sorted({t['wiki'] for t in teams if t.get('wiki') and t['wiki'] not in PAGES})
if need:
    PAGES.update(wikitext(need)); json.dump(PAGES, open(pcache, 'w'))
audit = {}
nokeys = []
for t in teams:
    txt = PAGES.get(t.get('wiki'), '')
    tables = re.findall(r'\{\{#invoke:MemberTable\|main(.*?)\}\}', txt, re.S)
    if not tables:
        nokeys.append(t['id']); continue
    game = GAME.get(t['id'].split('-')[0])
    pick = next((tb for tb in tables if re.search(r'\|\s*game\s*=\s*' + str(game) + r'\s*[|\n]', tb)), tables[0])
    keys = [m.group(1).strip() for m in re.finditer(r'\|\s*p\d+\s*=\s*([^|\n}]+)', pick)]
    bypage = {}
    for k in keys:
        e = ENTRY.get(k)
        if e and e[0]:
            bypage.setdefault(e[0], []).append(k)
    res = {}
    used = {}
    for p in t['players']:
        w = p.get('wiki')
        ks = bypage.get(w, [])
        i = used.get(w, 0); used[w] = i + 1
        if not ks: continue
        k = ks[min(i, len(ks) - 1)]
        res[p['id']] = [k, ENTRY[k][1]]
    audit[t['id']] = res
json.dump({'audit': audit, 'nokeys': nokeys}, open(f'{S}/audit.json', 'w'), indent=0)
print('equipos con tabla', len(audit), 'sin tabla', len(nokeys), nokeys[:20])
print('jugadores con forma', sum(len(v) for v in audit.values()), 'con VR', sum(1 for v in audit.values() for x in v.values() if x[1]))

from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageChops, ImageStat
apply_ = '--dry-run' not in sys.argv
A = audit
files = sorted({v[1] + '.png' for t in A.values() for v in t.values() if v[1]})
urls = {}
for i in range(0, len(files), 45):
    q = urllib.parse.urlencode({'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'format': 'json', 'titles': '|'.join('File:' + f for f in files[i:i + 45])})
    d = json.loads(urllib.request.urlopen(urllib.request.Request(SP.API + '?' + q, headers={'User-Agent': SP.UA}), timeout=90).read())
    norm = {n['to']: n['from'] for n in d['query'].get('normalized', [])}
    for p in d['query']['pages'].values():
        if 'imageinfo' in p:
            urls[norm.get(p['title'], p['title'])[5:]] = p['imageinfo'][0]['url']
print('urls', len(urls), 'de', len(files))
os.makedirs(SP.CACHE, exist_ok=True)
def load(fn):
    try:
        return fn, SP.fetch(urls[fn], os.path.join(SP.CACHE, re.sub(r'[^A-Za-z0-9]+', '_', fn)))
    except Exception as e:
        return fn, None
imgs = {}
with ThreadPoolExecutor(8) as ex:
    for fn, im in ex.map(load, [f for f in files if f in urls]):
        if im is not None: imgs[fn] = im
print('bajadas', len(imgs))
looks_path = os.path.join(SP.ROOT, 'src', 'data', 'looks.json')
LOOKS = json.load(open(looks_path))
diff = []
for tid, ps in A.items():
    for pid, (k, vr) in ps.items():
        if not vr or vr + '.png' not in imgs: continue
        new = SP.portrait(imgs[vr + '.png'])
        dest = os.path.join(SP.ROOT, 'src', 'assets', 'pack', 'portraits', tid, pid + '.webp')
        changed = True
        if os.path.exists(dest):
            cur = Image.open(dest).convert('RGBA').resize((64, 64))
            nn = new.convert('RGBA').resize((64, 64))
            changed = sum(ImageStat.Stat(ImageChops.difference(cur, nn)).mean[:3]) / 3 > 6
        if changed:
            diff.append((tid, pid, k, vr))
            if apply_:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                new.save(dest, 'WEBP', quality=86, method=6)
                LOOKS[f'{tid}:{pid}'] = SP.looks(imgs[vr + '.png'])
if apply_:
    with open(looks_path, 'w', encoding='utf-8') as f:
        f.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v)}' for k, v in sorted(LOOKS.items())) + '\n}\n')
json.dump(diff, open(f'{S}/diff.json', 'w'), indent=0)
from collections import Counter
print('distintos', len(diff)); print(Counter(d[0] for d in diff).most_common(40))
