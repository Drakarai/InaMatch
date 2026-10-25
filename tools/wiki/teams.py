"""Monta los equipos de IE3 con datos de la wiki inglesa de Inazuma Eleven.

- Plantillas, dorsales, capitán y formación: tabla de miembros de IE3 de la página de cada equipo.
- Posición, afinidad y técnicas de IE3: Module:PlayerData/IE, IE2 e IE3.
- Nombre europeo, atributos de IE3 (nivel 99) y descripción: página de cada jugador.
- Técnicas: Module:WazaData (potencia y coste de IE3) + nombre en español de data/tecnicas.json.
- Formaciones: Module:FormationData (nombre y distribución, p. ej. 4-4-2).
- Nombre del equipo en español: enlace entre wikis.

Uso (desde la raíz del repo): python3 -I tools/wiki/teams.py
Escribe src/data/teams/*.json, src/data/moves.json y src/data/formations.json.
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lua_table import parse_module  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de datos de equipos)'

ELEMENT = {'Fire': 'fire', 'Wind': 'wind', 'Forest': 'wood', 'Mountain': 'earth', 'Void': 'neutral'}
KIND = {'SH': 'shoot', 'OF': 'dribble', 'DF': 'block', 'GK': 'catch'}

# Colores de cada equipo (la wiki no los tiene en datos): camiseta, pantalón, portero y acento.
STYLE = {
    'Inazuma Japan': ('#2a6fd6', '#f4f4f4', '#e8892b', '#2d5fb8'),
    'Big Waves': ('#f2c230', '#1f5f3a', '#3a7bd5', '#2f8a4a'),
    'Desert Lion': ('#8e1f2f', '#f2ede4', '#3b3b48', '#a8283a'),
    'Neo Japan': ('#1b1b2f', '#e8e8e8', '#c9a227', '#3a3a6a'),
    'Fire Dragon': ('#d6342a', '#1a1a1a', '#f2c230', '#b82a22'),
    'Knights of Queen': ('#f2f2f2', '#1d2f6b', '#c8202f', '#1d2f6b'),
    'Orpheus': ('#2457b8', '#f2f2f2', '#2e2e2e', '#1d4596'),
    'Team K': ('#3a2a5a', '#1a1a1a', '#8a8a8a', '#5a3a8a'),
    'The Empire': ('#8fc6ea', '#1a1a1a', '#f2c230', '#4a8fc0'),
    'Unicorn': ('#f2f2f2', '#1d3b8a', '#c8202f', '#1d3b8a'),
    'The Kingdom': ('#f2d230', '#2a5fc0', '#2a8a3a', '#2a8a3a'),
    'Team Garshield': ('#2e2e2e', '#5a5a5a', '#8a2a2a', '#4a4a4a'),
    'Little Gigant': ('#f28a1d', '#1a1a1a', '#2a8a8a', '#d06a10'),
    'Brockenborg': ('#1a1a1a', '#f2f2f2', '#c8a020', '#3a3a3a'),
    'Red Matador': ('#c8202f', '#1d2f6b', '#f2c230', '#a01a26'),
    'Rose Griffon': ('#1d3b8a', '#f2f2f2', '#c8202f', '#2a4fa8'),
    'The Great Horn': ('#2a8a5a', '#f2f2f2', '#c87a20', '#1f6a44'),
    'Tenkuu no Shito': ('#f2f2f2', '#d8c070', '#7ab8e8', '#b8a050'),
    'Makai Gundan Z': ('#3a1a4a', '#1a1a1a', '#8a1a2a', '#5a2a6a'),
    'Ogre': ('#1a1a1a', '#8a1a1a', '#5a5a5a', '#8a1a1a'),
    'Real Inazuma': ('#f2c230', '#2a5fc0', '#e8892b', '#c89a10'),
}
SHORT = {
    'Inazuma Japan': 'INA', 'Big Waves': 'BWA', 'Desert Lion': 'DLI', 'Neo Japan': 'NEO', 'Fire Dragon': 'FDR',
    'Knights of Queen': 'KOQ', 'Orpheus': 'ORP', 'Team K': 'TMK', 'The Empire': 'EMP', 'Unicorn': 'UNI',
    'The Kingdom': 'KNG', 'Team Garshield': 'GAR', 'Little Gigant': 'LGI', 'Brockenborg': 'BRO', 'Red Matador': 'RMA',
    'Rose Griffon': 'RGR', 'The Great Horn': 'TGH', 'Tenkuu no Shito': 'TNS', 'Makai Gundan Z': 'MGZ', 'Ogre': 'OGR',
    'Real Inazuma': 'RIN',
}
# Equipos de origen japonés: en el campo se ve el nombre de pila (Mark, Axel...); en el resto, el apellido.
GIVEN_NAME_TEAMS = {'Inazuma Japan', 'Neo Japan', 'Real Inazuma', 'Team K', 'Ogre'}


def api(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # reintento con espera creciente
            if attempt == 3:
                raise
            print('reintento', e, file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


def fetch_pages(titles, extra=None):
    """Wikitexto (y lo que pida `extra`) de una lista de páginas, en lotes de 50."""
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i : i + 50]
        data = api({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': '1', **(extra or {})})
        q = data['query']
        alias = {r['from']: r['to'] for r in q.get('normalized', []) + q.get('redirects', [])}
        by_title = {p['title']: p for p in q['pages']}
        for t in chunk:
            final = t
            for _ in range(3):
                final = alias.get(final, final)
            if final in by_title:
                out[t] = by_title[final]
        time.sleep(0.5)
    return out


def content(page):
    return page.get('revisions', [{}])[0].get('slots', {}).get('main', {}).get('content', '')


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def color_for(text, palette):
    h = int(hashlib.md5(text.encode()).hexdigest(), 16)
    return palette[h % len(palette)]


# ------------------------------------------------------------------ módulos
print('descargando módulos...', file=sys.stderr)
mods = fetch_pages(['Module:PlayerData/IE', 'Module:PlayerData/IE2', 'Module:PlayerData/IE3', 'Module:WazaData', 'Module:FormationData'])
PLAYERS = {}
for m in ['Module:PlayerData/IE', 'Module:PlayerData/IE2', 'Module:PlayerData/IE3']:
    PLAYERS.update(parse_module(content(mods[m]), 'PLAYERS'))
WAZA = parse_module(content(mods['Module:WazaData']), 'WAZAS')
FORMATION = parse_module(content(mods['Module:FormationData']), 'FORMATION')
ie3 = parse_module(content(mods['Module:PlayerData/IE3']), 'PLAYERS')
groups = {}
for k, v in ie3.items():
    groups.setdefault(v.get('__group__'), []).append(k)
team_names = [g for g in groups if g and g != 'Scouts']
print('equipos de IE3:', len(team_names), file=sys.stderr)

# ------------------------------------------------------------- equipos
team_pages = fetch_pages(team_names, {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})


def member_table(text, game='IE3'):
    """Primera tabla de miembros del juego: [(clave, dorsal, capitán)]."""
    for body in re.findall(r'\{\{#invoke:MemberTable\|main\s*\n(.*?)\}\}\s*(?:\n|$)', text, re.S):
        if not re.search(r'\|game=%s\b' % game, body):
            continue
        fields = dict(re.findall(r'\|(\w+)=([^|\n]*)', body))
        rows = []
        n = 1
        while f'p{n}' in fields:
            no = re.match(r'\s*(\d+)', fields.get(f'no{n}', '')) if fields.get(f'no{n}') else None
            rows.append((fields[f'p{n}'].strip(), int(no.group(1)) if no else None, fields.get(f'captain{n}') == 'true'))
            n += 1
        return rows
    return []


def formation_of(text, game='IE3'):
    m = re.search(r'#invoke:FormationTable\|main\s*\n\|game=%s\s*\n\|f1=(\w+)' % game, text)
    return m.group(1) if m else None


# -------------------------------------------------------------- jugadores
rosters = {}
for name in team_names:
    page = team_pages.get(name)
    text = content(page) if page else ''
    rows = member_table(text)
    keys = [r[0] for r in rows]
    # si la tabla de la página está incompleta, se completa con el grupo del módulo
    for k in groups[name]:
        if len(rows) >= 16:
            break
        if k not in keys:
            rows.append((k, None, False))
            keys.append(k)
    rosters[name] = {'rows': [r for r in rows if r[0] in PLAYERS], 'formation': formation_of(text), 'page': page}

player_pages = sorted({PLAYERS[r[0]]['page'] for t in rosters.values() for r in t['rows']})
print('jugadores distintos:', len(player_pages), file=sys.stderr)
char_pages = fetch_pages(player_pages)

STAT_KEYS = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Body': 'body', 'Control': 'control', 'Guard': 'guard', 'Speed': 'speed', 'Stamina': 'stamina', 'Guts': 'guts'}


def ie3_params(text):
    """Primer bloque de atributos de IE3 de la pestaña 'Inazuma Eleven 3' (nivel 99).
    Se busca solo en la sección ==Parameters==: otras secciones (fichaje...) también tienen esa pestaña."""
    sec = re.search(r'==\s*Parameters\s*==(.*?)(?:\n==[^=]|$)', text, re.S)
    if not sec:
        return None
    m = re.search(r'\|\s*Inazuma Eleven 3\s*\|(.*?)(?:\n\|[^|\n]+\||\n\}\})', sec.group(1), re.S)
    if not m:
        return None
    block = m.group(1).split('----')[0]
    vals = dict(re.findall(r"\*'''(\w+)''':\s*(\d+)", block))
    out = {STAT_KEYS[k]: int(v) for k, v in vals.items() if k in STAT_KEYS}
    return out if len(out) == len(STAT_KEYS) else None


def dub_name(text):
    m = re.search(r'\|name_dub=\s*([^\n|]+)', text)
    if not m:
        return None
    name = re.sub(r"\{\{.*?\}\}|'''?|\[\[|\]\]|<[^>]+>", '', m.group(1)).lstrip('*').strip()
    return re.sub(r'\s*\(.*?\)', '', name) or None


def ie3_description(text):
    m = re.search(r'\{\{Profile/Entry\|g1=IE3[^}]*?entry_dub=([^}]*)\}\}', text)
    return re.sub(r"<br\s*/?>|'''?|\[\[|\]\]", ' ', m.group(1)).strip() if m else None


CATALOG = {m['en']: m for m in json.load(open(os.path.join(ROOT, 'data', 'tecnicas.json'), encoding='utf-8'))}
moves_used = {}


def move_from_key(key):
    w = WAZA.get(key)
    if not w or w.get('wType') not in KIND:
        return None
    power = w.get('power', {})
    cost = w.get('cost', {})
    power = power.get('IE3') if isinstance(power, dict) else power
    cost = cost.get('IE3') if isinstance(cost, dict) else cost
    element = w.get('element')
    element = element.get('IE3') if isinstance(element, dict) else element
    if power is None or cost is None or element not in ELEMENT:
        return None
    cat = CATALOG.get(w['page'], {})
    mid = slug(w['page'])
    # versiones de una misma técnica con otra afinidad (Mano mágica de Montaña / de Bosque)
    if mid in moves_used and moves_used[mid]['element'] != ELEMENT[element]:
        mid = f'{mid}-{ELEMENT[element]}'
    moves_used[mid] = {
        'id': mid,
        'name': cat.get('es') or cat.get('dub') or w['page'],
        'kind': KIND[w['wType']],
        'element': ELEMENT[element],
        'power': int(power),
        'tp': int(cost),
        'wiki': w['page'],
    }
    return mid


HAIR = ['#3a2a1a', '#6b3e1f', '#8b5a2b', '#c0302a', '#efe6c4', '#4c8a3c', '#3a6fb5', '#c9ccd6', '#1d1410', '#e98aa8', '#5a3a7a', '#d9822b']
SKIN = ['#f1c79b', '#f1c79b', '#e8b888', '#c08a5e', '#b5835a', '#9a6a44']
missing_stats = []


def build_player(key, number, team_name, used_ids):
    d = PLAYERS[key]
    page = char_pages.get(d['page'])
    text = content(page) if page else ''
    name = dub_name(text) or d['page']
    pid = slug(name)
    if pid in used_ids:  # mismo jugador en otra forma dentro del equipo
        pid = slug(f'{name} {key}')
    used_ids.add(pid)
    def for_ie3(v):
        # algunos datos van por juego: {IE2='FW', IE3='MF'}
        return (v.get('IE3') or list(v.values())[-1]) if isinstance(v, dict) else v

    element = for_ie3(d.get('element'))
    position = for_ie3(d.get('position')) or 'MF'
    stats = ie3_params(text)
    if not stats:
        missing_stats.append(f'{team_name}: {name}')
        base = {'GK': (45, 60, 40, 80, 45), 'DF': (50, 70, 50, 70, 55), 'MF': (60, 55, 65, 50, 65), 'FW': (75, 55, 60, 40, 65)}[position]
        stats = {'fp': 120, 'tp': 120, 'kick': base[0], 'body': base[1], 'control': base[2], 'guard': base[3], 'speed': base[4], 'stamina': 60, 'guts': 60}
    moveset = d.get('moveset', {}).get('IE3', [])
    moves = []
    for entry in moveset:
        mk = entry[0] if isinstance(entry, list) else None
        mid = move_from_key(mk) if mk else None
        if mid and mid not in moves:
            moves.append(mid)
    parts = name.split()
    short = parts[0] if team_name in GIVEN_NAME_TEAMS else parts[-1]
    player = {
        'id': pid,
        'name': name,
        'short': short,
        'number': number,
        'position': position,
        'element': ELEMENT.get(element, 'neutral'),
        'level': 99,
        'fp': stats['fp'],
        'tp': stats['tp'],
        'stats': {k: stats[k] for k in ['kick', 'body', 'control', 'guard', 'speed', 'stamina', 'guts']},
        'moves': moves,
        'look': {'hair': color_for(name, HAIR), 'skin': color_for(name[::-1], SKIN)},
        'wiki': d['page'],
    }
    desc = ie3_description(text)
    if desc:
        player['description'] = desc
    return player


# --------------------------------------------------------------- formaciones
formations = {}


def formation_id(fkey, players):
    f = FORMATION.get(fkey) if fkey else None
    layout = f.get('layout') if f else None
    if isinstance(layout, dict):
        layout = layout.get('IE3') or next(iter(layout.values()))
    if not layout or not re.fullmatch(r'\d-\d-\d', layout):
        # sin datos: la distribución de los titulares por posición
        c = {p: sum(1 for x in players[1:11] if x['position'] == p) for p in ('DF', 'MF', 'FW')}
        layout = f"{c['DF']}-{c['MF']}-{c['FW']}"
        name = f'F-{layout}'
    else:
        name = f.get('page') or fkey
    fid = slug(name)
    formations[fid] = {'id': fid, 'name': name, 'layout': layout}
    return fid, [int(x) for x in layout.split('-')]


FIT = {
    'DF': lambda s: s['guard'] + s['body'],
    'MF': lambda s: s['control'] + s['speed'] + s['kick'] / 2,
    'FW': lambda s: s['kick'] * 1.5 + s['control'] / 2,
}


def pick_starters(players, counts):
    """Portero + DF/MF/FW según la distribución, por orden de dorsal; el resto al banquillo.
    Si faltan jugadores de una posición, entra el que mejor encaje por atributos."""
    pool = list(players)
    starters = []
    gk = next((p for p in pool if p['position'] == 'GK'), pool[0])
    starters.append(gk)
    pool.remove(gk)
    lines = {}
    for pos, n in zip(('DF', 'MF', 'FW'), counts):
        chosen = [p for p in pool if p['position'] == pos][:n]
        for p in chosen:
            pool.remove(p)
        lines[pos] = (chosen, n)
    for pos, (chosen, n) in lines.items():
        while len(chosen) < n and pool:
            outfield = [p for p in pool if p['position'] != 'GK'] or pool
            filler = max(outfield, key=lambda p: FIT[pos](p['stats']))
            pool.remove(filler)
            chosen.append(filler)
    for pos in ('DF', 'MF', 'FW'):
        starters += lines[pos][0]
    return starters + pool


def unique_shorts(players):
    """Si dos jugadores comparten nombre corto (Majdi y Rajab Ismail), se usa el nombre de pila."""
    seen = {}
    for p in players:
        seen.setdefault(p['short'], []).append(p)
    for group in seen.values():
        if len(group) > 1:
            for p in group:
                p['short'] = p['name'].split()[0]


# ------------------------------------------------------------------ salida
teams_dir = os.path.join(ROOT, 'src', 'data', 'teams')
written = []
for name in team_names:
    r = rosters[name]
    used = set()
    players = []
    for i, (key, no, captain) in enumerate(r['rows']):
        players.append(build_player(key, no or i + 1, name, used))
    if len(players) < 11 or not any(p['position'] == 'GK' for p in players):
        print('se omite (plantilla incompleta):', name, len(players), file=sys.stderr)
        continue
    players.sort(key=lambda p: p['number'])
    fid, counts = formation_id(r['formation'], players)
    players = pick_starters(players, counts)
    unique_shorts(players)
    es = (r['page'] or {}).get('langlinks', [])
    shirt, shorts, gk, accent = STYLE.get(name, ('#5a6a7a', '#f2f2f2', '#c87a20', '#4a5a6a'))
    team = {
        'id': slug(name),
        'name': es[0]['title'] if es else name,
        'short': SHORT.get(name, name[:3].upper()),
        'colors': {'shirt': shirt, 'shorts': shorts, 'gkShirt': gk, 'accent': accent},
        'formation': fid,
        'players': players,
    }
    with open(os.path.join(teams_dir, team['id'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(team, f, ensure_ascii=False, indent=1)
        f.write('\n')
    written.append(team['id'])

with open(os.path.join(ROOT, 'src', 'data', 'moves.json'), 'w', encoding='utf-8') as f:
    order = ['shoot', 'dribble', 'block', 'catch']
    moves = sorted(moves_used.values(), key=lambda m: (order.index(m['kind']), -m['power'], m['name']))
    f.write('[\n' + ',\n'.join('  ' + json.dumps(m, ensure_ascii=False) for m in moves) + '\n]\n')
with open(os.path.join(ROOT, 'src', 'data', 'formations.json'), 'w', encoding='utf-8') as f:
    json.dump(sorted(formations.values(), key=lambda x: x['name']), f, ensure_ascii=False, indent=1)
    f.write('\n')

print('equipos:', len(written), written)
print('técnicas:', len(moves_used), '| sin nombre en español:', sum(1 for m in moves_used.values() if m['name'] == m['wiki'] and not CATALOG.get(m['wiki'], {}).get('es')))
print('formaciones:', len(formations))
print('jugadores sin atributos de IE3 en la wiki (estimados por posición):', len(missing_stats))
for m in missing_stats[:40]:
    print('  ', m)
