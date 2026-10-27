"""Monta los equipos de IE1, IE2 e IE3 con datos de la wiki inglesa de Inazuma Eleven.

Por cada temporada (juego):
- Equipos: los grupos del módulo de jugadores de ese juego (Module:PlayerData/IE, IE2, IE3).
- Plantilla, dorsales y formación: la tabla de miembros de ese juego en la página de cada equipo
  (si no la hay, el grupo del módulo).
- Posición, afinidad y técnicas: Module:PlayerData (las de ese juego; si faltan, las del más cercano).
- Nombre europeo, atributos a nivel 99 y descripción: la página de cada jugador.
- Técnicas: Module:WazaData (potencia y coste de IE3, o de IE2 si no salen en IE3)
  + nombre en español de data/tecnicas.json.
- Formaciones: Module:FormationData (nombre y distribución, p. ej. 4-4-2).
- Nombre del equipo en español: enlace entre wikis.

Uso (desde la raíz del repo): python3 -I tools/wiki/teams.py
Escribe src/data/teams/*.json, src/data/moves.json y src/data/formations.json.
"""
import glob
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

# temporada del juego: (id, clave del juego en la wiki, pestaña de atributos, orden de respaldo)
SEASONS = [
    ('ie1', 'IE', 'Inazuma Eleven', ['IE', 'IE2', 'IE3']),
    ('ie2', 'IE2', 'Inazuma Eleven 2', ['IE2', 'IE', 'IE3']),
    ('ie3', 'IE3', 'Inazuma Eleven 3', ['IE3', 'IE2', 'IE']),
]
GAME_TAB = {g: tab for _, g, tab, _ in SEASONS}

ELEMENT = {'Fire': 'fire', 'Wind': 'wind', 'Forest': 'wood', 'Mountain': 'earth', 'Void': 'neutral'}
KIND = {'SH': 'shoot', 'OF': 'dribble', 'DF': 'block', 'GK': 'catch'}

# Colores de cada equipo (la wiki no los tiene en datos): camiseta, pantalón, portero y acento.
# Los que no estén aquí se generan a partir del nombre.
STYLE = {
    # IE1
    'Raimon': ('#f2c230', '#2a5fc0', '#e8892b', '#d9a400'),
    'Teikoku Gakuen': ('#5a4a8a', '#3a3a4a', '#c8a020', '#4a3a7a'),
    'Occult': ('#3a1a4a', '#1a1a1a', '#6a8a2a', '#5a2a6a'),
    'Zeus': ('#f2f2f2', '#c8a020', '#5a8ac8', '#b89020'),
    'Inazuma Eleven': ('#f2c230', '#2a5fc0', '#e8892b', '#c89a10'),
    # IE2
    'Second Raimon': ('#f2c230', '#2a5fc0', '#e8892b', '#d9a400'),
    'Gemini Storm': ('#4a7a3a', '#1a2a1a', '#c8c020', '#3a6a2a'),
    'Epsilon': ('#3a2a6a', '#1a1a2a', '#c83a3a', '#4a3a8a'),
    'Epsilon Kai': ('#3a2a6a', '#1a1a2a', '#c83a3a', '#4a3a8a'),
    'The Genesis': ('#e8e8e8', '#5a3a8a', '#c8a020', '#7a5aa8'),
    'Diamond Dust': ('#a8d8f2', '#2a4a6a', '#f2f2f2', '#4a8ac0'),
    'Prominence': ('#d8342a', '#2a1a1a', '#f2a020', '#b82a22'),
    'Chaos': ('#7a2a5a', '#1a1a2a', '#3a8ac0', '#8a3a6a'),
    'Dark Emperors': ('#1a1a1a', '#5a1a1a', '#8a8a8a', '#6a1a2a'),
    'Shin Teikoku Gakuen': ('#2a2a4a', '#1a1a1a', '#c8a020', '#3a3a6a'),
    # IE3
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
    'Real Inazuma': 'RIN', 'Raimon': 'RAI', 'Second Raimon': 'RAI', 'Teikoku Gakuen': 'TEI', 'Zeus': 'ZEU',
}
# Selecciones del Fútbol Frontier Internacional: en el campo se ve el apellido. En el resto (equipos
# japoneses y alienígenas), el nombre de pila, como Mark o Axel.
SURNAME_TEAMS = {
    'Big Waves', 'Desert Lion', 'Fire Dragon', 'Knights of Queen', 'Orpheus', 'The Empire', 'Unicorn', 'The Kingdom',
    'Little Gigant', 'Brockenborg', 'Red Matador', 'Rose Griffon', 'The Great Horn', 'Team Garshield',
}
# Equipos sin página propia en la wiki (variantes): nombre en español puesto a mano
# Nombre en España de los equipos sin enlace entre wikis, o cuyo nombre en los juegos no es el del
# título de la página de la wiki española (inazuma.fandom.com/es, campo "Nombre" de cada equipo).
NAME_ES = {
    'Dark Emperors (cloaked)': 'Emperadores Oscuros (con capa)',
    'Diamond Dust': 'Polvo de Diamantes',
    'Epsilon': 'Épsilon',
    'Epsilon Kai': 'Épsilon Plus',
    'Inazuma Eleven': 'Inazuma Eleven',
    'Kasamino': 'Instituto Umbrella',
    'Little Gigant': 'Los Pequeños Gigantes',
    'Manyuuji': 'Instituto Claustro Sagrado',
    'Osaka Gals CCC': 'Triple C de Osaka',
    'SP Fixers': 'Servicio Secreto',
    'Team Garshield': 'Zoolan Team',
    'Team K': 'Equipo D',
    'The Great Horn': 'Caimanes del Cabo',
    'The Kingdom': 'Os Reis',
}
MIN_PLAYERS = 11


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
            if final in by_title and 'missing' not in by_title[final]:
                out[t] = by_title[final]
        time.sleep(0.5)
    return out


def content(page):
    return page.get('revisions', [{}])[0].get('slots', {}).get('main', {}).get('content', '')


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def pick(h, palette):
    return palette[int(hashlib.md5(h.encode()).hexdigest(), 16) % len(palette)]


def per_game(v, order):
    """Valor de un dato que puede ir por juego ({IE2='FW', IE3='MF'}), en el orden de preferencia dado."""
    if not isinstance(v, dict):
        return v
    for g in order:
        if v.get(g) is not None:
            return v[g]
    return list(v.values())[-1] if v else None


# ------------------------------------------------------------------ módulos
print('descargando módulos...', file=sys.stderr)
mods = fetch_pages(['Module:PlayerData/IE', 'Module:PlayerData/IE2', 'Module:PlayerData/IE3', 'Module:WazaData', 'Module:FormationData'])
BY_GAME = {g: parse_module(content(mods[f'Module:PlayerData/{g}']), 'PLAYERS') for g in ('IE', 'IE2', 'IE3')}
PLAYERS = {}
for g in ('IE', 'IE2', 'IE3'):
    PLAYERS.update(BY_GAME[g])
WAZA = parse_module(content(mods['Module:WazaData']), 'WAZAS')
FORMATION = parse_module(content(mods['Module:FormationData']), 'FORMATION')


def member_table(text, game):
    """Primera tabla de miembros del juego: [(clave, dorsal, capitán)]."""
    for body in re.findall(r'\{\{#invoke:MemberTable\|main\s*\n(.*?)\}\}\s*(?:\n|$)', text, re.S):
        if not re.search(r'\|game=%s\s*(?:\n|\|)' % game, body):
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


def formation_of(text, game):
    m = re.search(r'#invoke:FormationTable\|main\s*\n\|game=%s\s*\n\|f1=(\w+)' % game, text)
    return m.group(1) if m else None


# --------------------------------------------------------- equipos por temporada
rosters = []  # (season, game, order, nombre del grupo, filas, formación, página)
for season, game, _tab, order in SEASONS:
    groups = {}
    for k, v in BY_GAME[game].items():
        groups.setdefault(v.get('__group__'), []).append(k)
    names = [g for g in groups if g and g != 'Scouts']
    pages = fetch_pages(names, {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})
    for name in names:
        page = pages.get(name)
        text = content(page) if page else ''
        rows = member_table(text, game)
        keys = [r[0] for r in rows]
        for k in groups[name]:  # si la tabla está incompleta, se completa con el grupo del módulo
            if len(rows) >= 16:
                break
            if k not in keys:
                rows.append((k, None, False))
                keys.append(k)
        rows = [r for r in rows if r[0] in PLAYERS]
        rosters.append((season, game, order, name, rows, formation_of(text, game), page))
    print(f'{season}: {len(names)} grupos', file=sys.stderr)

player_pages = sorted({PLAYERS[r[0]]['page'] for t in rosters for r in t[4] if PLAYERS[r[0]].get('page')})
print('jugadores distintos:', len(player_pages), file=sys.stderr)
char_pages = fetch_pages(player_pages)

STAT_KEYS = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Body': 'body', 'Control': 'control', 'Guard': 'guard', 'Speed': 'speed', 'Stamina': 'stamina', 'Guts': 'guts'}


def params_for(text, game):
    """Atributos (nivel 99) de la pestaña de ese juego en la sección ==Parameters==.
    En IE1 hay versión japonesa y europea: se usa la europea, que es la que se jugó aquí."""
    sec = re.search(r'==\s*Parameters\s*==(.*?)(?:\n==[^=]|$)', text, re.S)
    if not sec:
        return None
    m = re.search(r'\|\s*%s\s*\|(.*?)(?:\n\|[^|\n]+\||\n\}\})' % re.escape(GAME_TAB[game]), sec.group(1), re.S)
    if not m:
        return None
    block = m.group(1)
    eu = re.search(r';\s*European version(.*?)(?:\n;|$)', block, re.S)
    block = (eu.group(1) if eu else block).split('----')[0]
    vals = dict(re.findall(r"\*'''(\w+)''':\s*(\d+)", block))
    out = {STAT_KEYS[k]: int(v) for k, v in vals.items() if k in STAT_KEYS}
    return out if len(out) == len(STAT_KEYS) else None


def dub_name(text):
    m = re.search(r'\|name_dub=\s*([^\n|]+)', text)
    if not m:
        return None
    name = re.sub(r"\{\{.*?\}\}|'''?|\[\[|\]\]|<[^>]+>", '', m.group(1)).lstrip('*').strip()
    return re.sub(r'\s*\(.*?\)', '', name) or None


def description(text, game):
    m = re.search(r'\{\{Profile/Entry\|g1=%s(?:\|[^}]*?)?\|entry_dub=([^}|]*)' % game, text)
    return re.sub(r"<br\s*/?>|'''?|\[\[|\]\]", ' ', m.group(1)).strip() if m else None


CATALOG = {m['en']: m for m in json.load(open(os.path.join(ROOT, 'data', 'tecnicas.json'), encoding='utf-8'))}
moves_used = {}


def move_from_key(key):
    """Técnica de WazaData. Potencia y coste de IE3 (o de IE2): los de IE1 van en otra escala."""
    w = WAZA.get(key)
    if not w or w.get('wType') not in KIND:
        return None
    raw_power = w.get('power', {})
    if isinstance(raw_power, dict) and not any(raw_power.get(g) is not None for g in ('IE3', 'IE2')):
        return None
    power = per_game(raw_power, ['IE3', 'IE2'])
    cost = per_game(w.get('cost', {}), ['IE3', 'IE2', 'IEEU', 'IE'])
    element = per_game(w.get('element'), ['IE3', 'IE2', 'IE'])
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
    if w.get('chr') == 'L':  # tiro largo: se puede usar desde cualquier distancia
        moves_used[mid]['long'] = True
    return mid


HAIR = ['#3a2a1a', '#6b3e1f', '#8b5a2b', '#c0302a', '#efe6c4', '#4c8a3c', '#3a6fb5', '#c9ccd6', '#1d1410', '#e98aa8', '#5a3a7a', '#d9822b']
SKIN = ['#f1c79b', '#f1c79b', '#e8b888', '#c08a5e', '#b5835a', '#9a6a44']
SHIRTS = ['#c8202f', '#2a5fc0', '#2a8a3a', '#f2c230', '#5a3a8a', '#e86a1a', '#1a1a1a', '#f2f2f2', '#3a8ac0', '#8a1a3a', '#4a6a2a', '#c87aa8']
missing_stats = []


def build_player(key, number, team_name, season, order, used_ids):
    d = PLAYERS[key]
    page = char_pages.get(d.get('page', ''))
    text = content(page) if page else ''
    name = dub_name(text) or d.get('page') or key
    pid = slug(name)
    if pid in used_ids:  # mismo jugador en otra forma dentro del equipo
        pid = slug(f'{name} {key}')
    used_ids.add(pid)
    element = per_game(d.get('element'), order)
    position = per_game(d.get('position'), order) or 'MF'
    if position not in ('GK', 'DF', 'MF', 'FW'):
        position = 'MF'
    stats = next((s for g in order if (s := params_for(text, g))), None)
    if not stats:
        missing_stats.append(f'{season} {team_name}: {name}')
        base = {'GK': (45, 60, 40, 80, 45), 'DF': (50, 70, 50, 70, 55), 'MF': (60, 55, 65, 50, 65), 'FW': (75, 55, 60, 40, 65)}[position]
        stats = {'fp': 120, 'tp': 120, 'kick': base[0], 'body': base[1], 'control': base[2], 'guard': base[3], 'speed': base[4], 'stamina': 60, 'guts': 60}
    movesets = d.get('moveset', {})
    moveset = next((movesets[g] for g in order if movesets.get(g)), [])
    moves = []
    for entry in moveset:
        mk = entry[0] if isinstance(entry, list) and entry else None
        mid = move_from_key(mk) if isinstance(mk, str) else None
        if mid and mid not in moves:
            moves.append(mid)
    parts = name.split()
    player = {
        'id': pid,
        'name': name,
        'short': parts[-1] if team_name in SURNAME_TEAMS else parts[0],
        'number': number,
        'position': position,
        'element': ELEMENT.get(element, 'neutral'),
        'level': 99,
        'fp': stats['fp'],
        'tp': stats['tp'],
        'stats': {k: stats[k] for k in ['kick', 'body', 'control', 'guard', 'speed', 'stamina', 'guts']},
        'moves': moves,
        'look': {'hair': pick(name, HAIR), 'skin': pick(name[::-1], SKIN)},
        'wiki': d.get('page') or key,
    }
    desc = next((x for g in order if (x := description(text, g))), None)
    if desc:
        player['description'] = desc
    return player


# --------------------------------------------------------------- formaciones
formations = {}


def formation_id(fkey, game, players):
    f = FORMATION.get(fkey) if fkey else None
    layout = per_game(f.get('layout'), [game, 'IE3', 'IE2', 'IE']) if f else None
    valid = isinstance(layout, str) and re.fullmatch(r'\d-\d-\d', layout) and sum(map(int, layout.split('-'))) == 10
    if not valid:
        # sin datos: la distribución de los titulares por posición
        c = {p: sum(1 for x in players[1:11] if x['position'] == p) for p in ('DF', 'MF', 'FW')}
        layout = f"{c['DF']}-{c['MF']}-{c['FW']}"
        if sum(c.values()) != 10:
            layout = '4-4-2'
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
    gk = next((p for p in pool if p['position'] == 'GK'), pool[0])
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
    return [gk] + lines['DF'][0] + lines['MF'][0] + lines['FW'][0] + pool


def unique_shorts(players):
    """Si dos jugadores comparten nombre corto, se usa la otra parte de su nombre."""
    seen = {}
    for p in players:
        seen.setdefault(p['short'], []).append(p)
    for group in seen.values():
        if len(group) > 1:
            for p in group:
                parts = p['name'].split()
                p['short'] = parts[0] if p['short'] != parts[0] else parts[-1]


def team_short(name, taken):
    if name in SHORT and SHORT[name] not in taken:
        return SHORT[name]
    words = [w for w in re.split(r'\W+', name) if w and w.lower() not in ('the', 'of', 'no')]
    cands = [''.join(w[0] for w in words)[:3].upper() if len(words) >= 3 else '', re.sub(r'\W', '', name)[:3].upper()]
    cands += [(words[0][:2] + words[-1][0]).upper() if len(words) > 1 else '', (words[0][0] + words[0][2:4]).upper()]
    for c in cands:
        if len(c) == 3 and c not in taken:
            return c
    return name[:2].upper() + str(len(taken))


# ------------------------------------------------------------------ salida
teams_dir = os.path.join(ROOT, 'src', 'data', 'teams')
for f in glob.glob(os.path.join(teams_dir, '*.json')):
    os.remove(f)
written = {s[0]: [] for s in SEASONS}
shorts = {s[0]: set() for s in SEASONS}
skipped = []
for season, game, order, name, rows, fkey, page in rosters:
    used = set()
    players = [build_player(key, no or i + 1, name, season, order, used) for i, (key, no, _c) in enumerate(rows)]
    if len(players) < MIN_PLAYERS or not any(p['position'] == 'GK' for p in players):
        skipped.append(f'{season} {name} ({len(players)} jugadores)')
        continue
    players.sort(key=lambda p: p['number'])
    fid, counts = formation_id(fkey, game, players)
    players = pick_starters(players, counts)
    unique_shorts(players)
    es = (page or {}).get('langlinks', [])
    style = STYLE.get(name) or (
        pick(name, SHIRTS),
        pick(name + 's', ['#f2f2f2', '#1a1a1a', '#2a3a5a']),
        pick(name + 'g', ['#e8892b', '#3a8a3a', '#5a5a5a']),
        pick(name, SHIRTS),
    )
    short = team_short(name, shorts[season])
    shorts[season].add(short)
    team = {
        'id': f'{season}-{slug(name)}',
        'season': season,
        'wiki': name,
        'name': NAME_ES.get(name) or (es[0]['title'] if es else name),
        'short': short,
        'colors': {'shirt': style[0], 'shorts': style[1], 'gkShirt': style[2], 'accent': style[3]},
        'formation': fid,
        'players': players,
    }
    with open(os.path.join(teams_dir, team['id'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(team, f, ensure_ascii=False, indent=1)
        f.write('\n')
    written[season].append(team['name'])

with open(os.path.join(ROOT, 'src', 'data', 'moves.json'), 'w', encoding='utf-8') as f:
    kinds = ['shoot', 'dribble', 'block', 'catch']
    moves = sorted(moves_used.values(), key=lambda m: (kinds.index(m['kind']), -m['power'], m['name']))
    f.write('[\n' + ',\n'.join('  ' + json.dumps(m, ensure_ascii=False) for m in moves) + '\n]\n')
with open(os.path.join(ROOT, 'src', 'data', 'formations.json'), 'w', encoding='utf-8') as f:
    json.dump(sorted(formations.values(), key=lambda x: x['name']), f, ensure_ascii=False, indent=1)
    f.write('\n')

for s, names in written.items():
    print(f'{s}: {len(names)} equipos -> {", ".join(names)}')
print('omitidos:', skipped)
print('técnicas:', len(moves_used), '| sin nombre en español:', sum(1 for m in moves_used.values() if not CATALOG.get(m['wiki'], {}).get('es')))
print('formaciones:', len(formations))
print('jugadores sin atributos en la wiki (estimados por posición):', len(missing_stats))
for m in missing_stats[:30]:
    print('  ', m)
