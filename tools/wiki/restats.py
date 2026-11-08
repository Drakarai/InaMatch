"""Rehace los atributos de la era GO y de Victory Road (y marca los capitanes) sin regenerar el resto de los datos.

teams.py pasaba los atributos de los juegos de la era GO (y los de Victory Road de Inazugle) a la escala de IE3 comparando
cada valor con los de su misma demarcación. Así un delantero solo se medía con los delanteros de su juego (y uno bueno
podía quedar flojo si los demás eran muy buenos), y un portero con los porteros: las medias de equipos de esa época
salían incoherentes (en el Raimon de Victory Road, el portero con 83 de media y Harper Evans muy por debajo).
Aquí cada atributo se compara con el de TODOS los jugadores de su juego (salvo la parada del portero, que va aparte) y
se lleva a la escala de IE3 de su demarcación. Si un personaje tiene varias fichas en Inazugle, se queda la más fuerte.
Los jugadores de IE1-IE3 no cambian: sus atributos son los de sus juegos.

Capitanes: la tabla de miembros de cada equipo en la wiki los marca (captainN=true); se guardan como "captain": true.

Uso (desde la raíz del repo): python3 -I tools/wiki/restats.py
Cambia src/data/teams/*.json y src/data/scouts.json (solo fp, tp, stats y captain).
"""
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (atributos)'
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.cache', 'restats_pages.json')

# los mismos datos que tools/wiki/teams.py
ORDER = {'ie1': ['IE', 'IE2', 'IE3'], 'ie2': ['IE2', 'IE', 'IE3'], 'ie3': ['IE3', 'IE2', 'IE'], 'go': ['GO', 'CS', 'GX', 'VR'],
         'cs': ['CS', 'GO', 'GX', 'VR'], 'gx': ['GX', 'CS', 'GO', 'VR'], 'ares': ['VR', 'AT', 'OK', 'GX', 'CS', 'GO'],
         'orion': ['VR', 'OK', 'AT', 'GX', 'CS', 'GO'], 'vr': ['VR', 'GX', 'CS', 'GO', 'IE3', 'IE2', 'IE']}
GAME = {'ie1': 'IE', 'ie2': 'IE2', 'ie3': 'IE3', 'go': 'GO', 'cs': 'CS', 'gx': 'GX', 'ares': 'AT', 'orion': 'OK', 'vr': 'VR'}
GAME_TAB = {'IE': 'Inazuma Eleven', 'IE2': 'Inazuma Eleven 2', 'IE3': 'Inazuma Eleven 3', 'GO': 'Inazuma Eleven GO',
            'CS': 'Inazuma Eleven GO 2: Chrono Stone', 'GX': 'Inazuma Eleven GO Galaxy'}
GO_GAMES = ('GO', 'CS', 'GX', 'VR', 'AT', 'OK')
ZUKAN_GAME = {'IE': 'Inazuma Eleven', 'IE2': 'Inazuma Eleven 2', 'IE3': 'Inazuma Eleven 3', 'GO': 'Inazuma Eleven GO:',
              'CS': 'Chrono Stones', 'GX': 'Galaxy', 'ares': 'Ares', 'orion': 'Orion', 'VR': 'Victory Road'}
STAT_KEYS = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Body': 'body', 'Control': 'control', 'Guard': 'guard', 'Speed': 'speed', 'Stamina': 'stamina', 'Guts': 'guts'}
STAT_KEYS_GO = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Dribbling': 'dribbling', 'Technique': 'technique', 'Block': 'block',
                'Speed': 'speed', 'Stamina': 'stamina', 'Catch': 'catch', 'Lucky': 'lucky'}
STAT_NAMES = ['kick', 'body', 'control', 'guard', 'speed', 'stamina', 'guts']
MAP_RAW = {
    'go': lambda r, pos: {'kick': r['kick'], 'control': r['dribbling'], 'guard': r['catch'] if pos == 'GK' else r['block'],
                          'body': r['technique'], 'speed': r['speed'], 'stamina': r['stamina'], 'guts': r['lucky'],
                          'fp': r['fp'], 'tp': r['tp']},
    'vr': lambda r, pos: {'kick': r['kick'], 'control': r['control'], 'guard': r['pressure'], 'body': r['physical'],
                          'speed': r['agility'], 'stamina': (r['physical'] + r['intelligence']) / 2, 'guts': r['technique'],
                          'fp': r['physical'] + r['intelligence'], 'tp': r['technique'] + r['intelligence']},
}


def api(params):
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode({**params, 'format': 'json'}), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=90).read())
        except Exception:  # noqa: BLE001
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))


def pages(titles):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    need = [t for t in titles if t not in cache]
    for i in range(0, len(need), 50):
        chunk = need[i:i + 50]
        d = api({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': 1, 'titles': '|'.join(chunk)})
        q = d['query']
        alias = {r['from']: r['to'] for r in q.get('normalized', []) + q.get('redirects', [])}
        by = {p['title']: p for p in q['pages'].values()}
        for t in chunk:
            f = t
            for _ in range(3):
                f = alias.get(f, f)
            p = by.get(f, {})
            cache[t] = p['revisions'][0]['slots']['main']['*'] if 'revisions' in p else ''
        time.sleep(0.3)
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(cache, open(CACHE, 'w'))
    return cache


def params_for(text, game):
    sec = re.search(r'==\s*Parameters\s*==(.*?)(?:\n==[^=]|$)', text, re.S)
    if not sec or game not in GAME_TAB:
        return None
    m = re.search(r'\|\s*%s\s*\|(.*?)(?:\n\|[^|\n]+\||\n\}\})' % re.escape(GAME_TAB[game]), sec.group(1), re.S)
    if not m:
        return None
    block = m.group(1)
    eu = re.search(r';\s*European version(.*?)(?:\n;|$)', block, re.S)
    block = (eu.group(1) if eu else block).split('----')[0]
    vals = dict(re.findall(r"\*'''(\w+)''':\s*(\d+)", block))
    keys = STAT_KEYS_GO if game in GO_GAMES else STAT_KEYS
    out = {keys[k]: int(v) for k, v in vals.items() if k in keys}
    if len(out) != len(keys):
        return None
    out['_src'] = 'go' if game in GO_GAMES else 'ie'
    return out


ZUKAN = {}
for c in json.load(open(os.path.join(ROOT, 'tools', 'zukan', 'charas.json'), encoding='utf-8')):
    if len(c['stats']) == 7:
        ZUKAN.setdefault(c['name'].lower(), []).append(c)


def zukan_for(name, games):
    cands = ZUKAN.get((name or '').lower())
    if not cands:
        return None
    for g in games:
        same = [c for c in cands if ZUKAN_GAME.get(g, '~') in c['game']]
        if same:  # de las fichas de ese juego, la más fuerte (Harper Evans tiene dos)
            return {**max(same, key=lambda c: sum(c['stats'].values()))['stats'], '_src': 'vr'}
    return {**cands[0]['stats'], '_src': 'vr'}


def spread(vals):
    m = sum(vals) / len(vals)
    sd = (sum((v - m) ** 2 for v in vals) / len(vals)) ** 0.5 or 1
    return m, sd


def main():
    team_files = sorted(f for f in glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json')) if not f.endswith('club.json'))
    teams = [(f, json.load(open(f, encoding='utf-8'))) for f in team_files]
    scouts_path = os.path.join(ROOT, 'src', 'data', 'scouts.json')
    scouts = json.load(open(scouts_path, encoding='utf-8'))
    everyone = []  # (season, player)
    for _, t in teams:
        season = t['id'].split('-')[0]
        everyone += [(season, p) for p in t['players']]
    for season, ps in scouts.items():
        everyone += [(season, p) for p in ps]
    texts = pages(sorted({p['wiki'] for _, p in everyone if p.get('wiki')} | {t['wiki'] for _, t in teams if t.get('wiki')}))

    # de dónde salen los atributos de cada uno (lo mismo que teams.py)
    native, raw, missing = [], [], []
    for season, p in everyone:
        text = texts.get(p.get('wiki', ''), '')
        order = ORDER.get(season, ['VR'])
        st = next((s for g in order if (s := params_for(text, g))), None)
        if st and st['_src'] == 'ie':
            native.append(p)
            continue
        r = st or zukan_for(p['name'], [season] + order)
        if r:
            raw.append((p, r))
        else:
            missing.append((season, p))
    # escala de IE3 de cada demarcación (con los jugadores de IE1-IE3)
    target = {}
    for pos in ('GK', 'DF', 'MF', 'FW'):
        ie = [p for p in native if p['position'] == pos and p['stats']]
        for k in STAT_NAMES:
            target[(pos, k)] = spread([p['stats'][k] for p in ie])
        for k in ('fp', 'tp'):
            target[(pos, k)] = spread([p[k] for p in ie])
    for src, fn in MAP_RAW.items():
        group = [(p, fn(r, p['position'])) for p, r in raw if r['_src'] == src]
        for k in STAT_NAMES + ['fp', 'tp']:
            # la referencia del juego: todos sus jugadores; la parada del portero se compara solo entre porteros
            if k == 'guard':
                ref = {g: spread([x[k] for p, x in group if (p['position'] == 'GK') == (g == 'GK')]) for g in ('GK', 'F')}
            else:
                ref = spread([x[k] for _, x in group])
            for p, x in group:
                m, sd = (ref['GK' if p['position'] == 'GK' else 'F'] if k == 'guard' else ref)
                tm, tsd = target[(p['position'], k)]
                v = round(tm + (x[k] - m) / sd * tsd)
                if k in ('fp', 'tp'):
                    p[k] = max(60, min(250, v))
                else:
                    p['stats'][k] = max(15, min(99, v))
    # los que no tienen atributos en ningún sitio (algunos de Orion y Victory Road): la mediana de su demarcación en su
    # temporada, en vez de unos valores de relleno iguales para todos
    known = {id(p) for p in native} | {id(p) for p, _ in raw}
    for season, p in missing:
        peers = [q for s2, q in everyone if s2 == season and q['position'] == p['position'] and id(q) in known]
        if not peers:
            continue
        med = lambda vals: sorted(vals)[len(vals) // 2]  # noqa: E731
        p['stats'] = {k: med([q['stats'][k] for q in peers]) for k in STAT_NAMES}
        p['fp'], p['tp'] = med([q['fp'] for q in peers]), med([q['tp'] for q in peers])
    print(f'atributos: {len(native)} de IE1-IE3 (sin cambios), {len(raw)} rehechos, {len(missing)} sin datos (mediana)', file=sys.stderr)

    # capitanes: la tabla de miembros del juego del equipo
    n_cap = 0
    for f, t in teams:
        for p in t['players']:
            p.pop('captain', None)
        text = texts.get(t.get('wiki', ''), '')
        game = GAME.get(t['id'].split('-')[0])
        tables = re.findall(r'\{\{#invoke:MemberTable\|main(.*?)\}\}', text, re.S)
        tb = next((x for x in tables if re.search(r'\|\s*game\s*=\s*' + str(game) + r'\s*[|\n]', x)), tables[0] if tables else '')
        fields = dict(re.findall(r'\|\s*(\w+)\s*=\s*([^|\n}]*)', tb))
        caps = [fields.get(f'p{k[7:]}', '').strip() for k in fields if re.fullmatch(r'captain\d+', k) and fields[k].strip() == 'true']
        cap_pages = set()
        mods = MODULES()
        for key in caps:
            page = mods.get(key)
            if page:
                cap_pages.add(page)
        # si la tabla no lo marca, el campo captain del cuadro del equipo (el primero de los suyos que salga)
        ordered = [p.get('wiki') for p in t['players'] if p.get('wiki') in cap_pages]
        if not ordered:
            box = re.search(r'\|\s*captain\s*=(.*?)\n\|', text, re.S)
            lines = [ln for ln in (box.group(1).split('\n') if box else []) if not re.search(r'formerly|temporary|former', ln, re.I)]
            links = [x.split('|')[0].strip() for ln in lines for x in re.findall(r'\[\[([^\]]+)\]\]', ln)]
            roster = {p.get('wiki') for p in t['players']}
            ordered = [x for x in links if x in roster][:1]
        for p in t['players']:
            if ordered and p.get('wiki') == ordered[0]:
                p['captain'] = True
                n_cap += 1
                break  # uno por equipo (si sale dos veces, la primera)
        open(f, 'w', encoding='utf-8').write(json.dumps(t, ensure_ascii=False, indent=1) + '\n')
    print(f'capitanes: {n_cap} de {len(teams)} equipos', file=sys.stderr)
    with open(scouts_path, 'w', encoding='utf-8') as fh:
        fh.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v, ensure_ascii=False, separators=(",", ":"))}' for k, v in scouts.items()) + '\n}\n')


_MODS = {}


def MODULES():
    """clave de la tabla de miembros -> página del personaje (Module:PlayerData/*)."""
    if _MODS:
        return _MODS
    titles = [f'Module:PlayerData/{g}' for g in ('IE', 'IE2', 'IE3', 'GO', 'CS', 'GX', 'AT', 'OK', 'VR')]
    for t, txt in pages(titles).items():
        for m in re.finditer(r'\n\t([A-Za-z0-9_]+)\s*=\s*\{(.*?)\n\t\},?', txt, re.S):
            pg = re.search(r'\bpage\s*=\s*"([^"]*)"', m.group(2))
            if pg and m.group(1) not in _MODS:
                _MODS[m.group(1)] = pg.group(1)
    return _MODS


if __name__ == '__main__':
    main()
