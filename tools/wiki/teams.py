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
import unicodedata
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
    'Asia Daihyou': 'Ases Asiáticos',
    'Ura Raimon': 'Ultra Raimon',
    'NEW Genesis': 'Génesis NEW',
    'NEW Zeus': 'Zeus NEW',
    'NEW Teikoku Gakuen': 'Royal Academy NEW',
}
# Equipos extra que visten como otro (versiones del mismo equipo) o con colores puestos aquí
STYLE_OF = {
    'Ura Zeus': 'Zeus', 'Neo Teikoku': 'Teikoku Gakuen', 'Kageyama All Star': 'Shin Teikoku Gakuen',
    'Aliea A': 'The Genesis', 'Aliea B': 'Chaos', 'Super Shuuyou Meito': 'Shuuyou Meito Gakuen',
    'Super Oosaka CCC': 'Osaka Gals CCC', 'Inazuma KFC Kai': 'Inazuma KFC', 'NEW Genesis': 'The Genesis',
    'NEW Zeus': 'Zeus', 'NEW Teikoku Gakuen': 'Teikoku Gakuen', 'First Raimon': 'Raimon', 'Neo Raimon': 'Raimon',
    'Ura Raimon': 'Raimon', 'Neo Japan Kai': 'Neo Japan', 'Another Chaos': 'Chaos', 'Real Aliea': 'The Genesis',
    'Inazuma Legend': 'Inazuma Eleven', 'Nippon Daihyou Kouho A': 'Inazuma Japan',
}
STYLE.update({
    'Kami to Uchuu': ('#f2f2f2', '#5a3a8a', '#c8a020', '#7a5aa8'),
    'Zenkoku Team Senbatsu A': ('#2a5fc0', '#f2f2f2', '#e8892b', '#1d4596'),
    'Zenkoku Team Senbatsu B': ('#c8202f', '#f2f2f2', '#2a8a3a', '#a01a26'),
    'Nippon Daihyou Kouho B': ('#f2f2f2', '#2a6fd6', '#e8892b', '#2d5fb8'),
    'Dark Angel': ('#1a1a1a', '#3a1a4a', '#8a1a2a', '#5a2a6a'),
    'Chaos Angels': ('#7a2a5a', '#f2f2f2', '#3a8ac0', '#8a3a6a'),
    'God Angel': ('#f2f2f2', '#c8a020', '#7ab8e8', '#b89020'),
    'Sekai Daihyou': ('#1d2f6b', '#f2f2f2', '#c8a020', '#c8a020'),
    'Asia Daihyou': ('#c8202f', '#f2f2f2', '#2a5fc0', '#a01a26'),
    'Europe Daihyou': ('#2457b8', '#f2f2f2', '#c8a020', '#1d4596'),
    'Africa Daihyou': ('#2a8a5a', '#f2c230', '#c8202f', '#1f6a44'),
    'Nanbei Daihyou': ('#f2d230', '#2a8a3a', '#2a5fc0', '#2a8a3a'),
    'Joshi Senbatsu Team': ('#e98aa8', '#f2f2f2', '#5a3a8a', '#c86a8a'),
})

MIN_PLAYERS = 11

# Equipos que no son grupos del módulo de jugadores: se montan con la tabla de miembros de su página.
EXTRA = {
    'ie1': ['Ura Zeus'],
    'ie2': [
        'Kami to Uchuu', 'Neo Teikoku', 'Kageyama All Star', 'Aliea A', 'Aliea B', 'Super Shuuyou Meito',
        'Super Oosaka CCC', 'Inazuma KFC Kai', 'Zenkoku Team Senbatsu A', 'Zenkoku Team Senbatsu B',
        'NEW Genesis', 'NEW Zeus', 'NEW Teikoku Gakuen',
    ],
    'ie3': [
        'First Raimon', 'Neo Raimon', 'Ura Raimon', 'Nippon Daihyou Kouho A', 'Nippon Daihyou Kouho B',
        'Neo Japan Kai', 'Dark Angel', 'Chaos Angels', 'God Angel', 'Inazuma Legend', 'Sekai Daihyou',
        'Asia Daihyou', 'Europe Daihyou', 'Africa Daihyou', 'Nanbei Daihyou', 'Joshi Senbatsu Team',
        'Real Aliea', 'Another Chaos',
    ],
}

# Descripciones en español puestas a mano (por página del jugador en la wiki inglesa) para los que no
# tienen la oficial en la wiki española: traducidas de la inglesa o escritas a partir de su historia.
# También nombres que la wiki no trae bien.
OVERRIDES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.json'), encoding='utf-8'))


ES_API = 'https://inazuma.fandom.com/es/api.php'


def api(params, url=API):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(url + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # reintento con espera creciente
            if attempt == 3:
                raise
            print('reintento', e, file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


def fetch_pages(titles, extra=None, url=API):
    """Wikitexto (y lo que pida `extra`) de una lista de páginas, en lotes de 50."""
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i : i + 50]
        data = api({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': '1', **(extra or {})}, url)
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
    # equipos extra (versiones mejoradas, selecciones, equipos secretos): solo con la tabla de su página
    extra = fetch_pages(EXTRA.get(season, []), {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})
    for name in EXTRA.get(season, []):
        page = extra.get(name)
        text = content(page) if page else ''
        rows = [r for r in member_table(text, game) if r[0] in PLAYERS]
        rosters.append((season, game, order, name, rows, formation_of(text, game), page))

player_pages = sorted({PLAYERS[r[0]]['page'] for t in rosters for r in t[4] if PLAYERS[r[0]].get('page')})
print('jugadores distintos:', len(player_pages), file=sys.stderr)
char_pages = fetch_pages(player_pages, {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})

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


def dub_name(text, title=''):
    m = re.search(r'\|name_dub=\s*([^\n|]+)', text)
    if not m:
        return None
    name = m.group(1).replace('{{PAGENAME}}', title)
    name = re.sub(r"\{\{.*?\}\}|'''?|\[\[|\]\]|<[^>]+>", '', name).lstrip('*').strip()
    # lo que va entre paréntesis son aclaraciones ("(IE NL)"); a veces la plantilla corta el cierre
    name = re.sub(r'\s*\(.*$', '', name).strip()
    return name or None


# las páginas de la wiki española tienen las descripciones oficiales de los juegos en español
es_titles = {p: page['langlinks'][0]['title'] for p, page in char_pages.items() if page.get('langlinks')}
# muchas páginas no tienen el enlace, pero en la wiki española se llaman como en el doblaje europeo
for p, page in char_pages.items():
    if p not in es_titles and (dub := dub_name(content(page), p)):
        es_titles[p] = dub
es_pages = fetch_pages(sorted(set(es_titles.values())), url=ES_API)
print('jugadores con página en la wiki española:', sum(1 for t in es_titles.values() if content(es_pages.get(t, {}))), file=sys.stderr)

# Los que siguen sin página: en el juego español algunos se llaman distinto (Umi Hwang es Umi Wang; los de
# Los Rojos tienen nombres españoles). Se buscan en la tabla de miembros de su equipo en la wiki española:
# por una parte del nombre en común o, si no, por dorsal y posición.
ES_POS = {'GK': 'PR', 'DF': 'DF', 'MF': 'MD', 'FW': 'DL'}


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return re.sub(r'[^a-z0-9 ]', ' ', ''.join(c for c in s if not unicodedata.combining(c)))


def es_members(text):
    """[(dorsal, página, posición, dorsal dudoso)] de las tablas de miembros de un equipo en la wiki española."""
    out = []
    for body in re.findall(r'\{\{Tabla \(Miembros\)\s*\n(.*?)\n\}\}', text, re.S):
        dor = re.search(r'\|\s*Dor\s*=\s*([^\n]*)', body)
        nom = re.search(r'\|\s*Nom\s*=\s*\[\[([^\]|]+)', body)
        pos = re.search(r'\{\{M\|P\|(\w+)', body)
        n = re.match(r'\s*(\d+)', dor.group(1)) if dor else None
        if n and nom:
            out.append((int(n.group(1)), nom.group(1).strip(), pos.group(1) if pos else '', '/' in dor.group(1)))
    return out


team_es = {}
for _s, _g, _o, name, _rows, _f, page in rosters:
    ll = (page or {}).get('langlinks', [])
    team_es[name] = ll[0]['title'] if ll else NAME_ES.get(name)
es_team_pages = fetch_pages(sorted({t for t in team_es.values() if t}), url=ES_API)
es_by_player = {}  # (equipo, clave del jugador) -> página en la wiki española
for _s, _g, order, name, rows, _f, _p in rosters:
    members = es_members(content(es_team_pages.get(team_es.get(name) or '', {})))
    for i, (key, no, _c) in enumerate(rows):
        pg = PLAYERS[key].get('page', '')
        if content(es_pages.get(es_titles.get(pg, ''), {})):
            continue
        no = no or i + 1  # el mismo dorsal que se le pone en build_player
        en_names = [pg, dub_name(content(char_pages.get(pg, {})), pg) or '']
        tokens = {w for n in en_names for w in norm(n).split() if len(w) >= 3}
        by_name = {m[1] for m in members if tokens & set(norm(m[1]).split())}
        pos = ES_POS.get(per_game(PLAYERS[key].get('position'), order))
        same_no = [m for m in members if m[0] == no]
        by_no = {m[1] for m in same_no if m[2] == pos and not m[3]} if len(same_no) == 1 else set()
        # si el nombre y el dorsal no coinciden, manda el dorsal (un apellido en común puede ser casualidad)
        match = by_name if len(by_name) == 1 and (not by_no or by_no == by_name) else by_no
        if len(match) == 1:
            es_by_player[(name, key)] = match.pop()
# el mismo jugador en otro equipo (selecciones, versiones mejoradas) usa la página encontrada
by_key = {key: title for (_n, key), title in es_by_player.items()}
for _s, _g, _o, name, rows, _f, _p in rosters:
    for key, _no, _c in rows:
        if (name, key) not in es_by_player and key in by_key:
            es_by_player[(name, key)] = by_key[key]
es_pages.update(fetch_pages(sorted(set(es_by_player.values()) - set(es_pages)), url=ES_API))
print('encontrados en las tablas de equipo de la wiki española:', len(es_by_player), file=sys.stderr)


ES_DESC = {'IE': ('IE', 'Descripción IE'), 'IE2': ('IE 2', 'Descripción IE2'), 'IE3': ('IE 3', 'Descripción IE3')}


def clean_wiki(t):
    t = re.sub(r'<nowiki>\s*</nowiki>|<[^>]+>', ' ', t)
    t = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    return re.sub(r"'''?|\s+", ' ', t).strip()


GAME_NO = {'IE': 1, 'IE2': 2, 'IE3': 3}
END = r'(?=\n\s*\||\}\}\s*(?:\n|$))'  # fin de un parámetro: el siguiente o el cierre de la plantilla


def es_text_of(body):
    """Texto de una descripción. Si trae la traducción literal del japonés y la del juego español
    (líneas *{{JP}}: ... y *{{ES}}: ...), la española; si trae varias (antes/después...), la primera."""
    bullets = re.findall(r"\*\s*(?:'''([^']*)'''\s*:\s*)?([^\n*]+)", body)
    if bullets:
        es = [b for label, b in bullets if '{{ES}}' in (label or '')]
        jp = [b for label, b in bullets if '{{JP}}' in (label or '')]
        body = es[0] if es else None if jp else bullets[0][1]
    elif body and '----' in body:  # variantes sin viñetas ('''Normal''': ... ---- '''Otra''': ...)
        body = re.sub(r"^\s*'''[^']*'''\s*:?", '', body.split('----')[0].strip())
    return clean_wiki(body) if body else None


def description_es(text, game):
    """Descripción oficial en español del juego, de las plantillas de la sección de descripción:
    - el parámetro "Descripción IE3 = ..." (o IE2, o IE) de {{Descripción/IE 3 | ...}} o {{Descripción | ...}};
    - {{Descripción/IE | Descripción = ...}} (IE1);
    - {{Descripción/Varios | IE = {{IE|J|IE 2-3}} | Descripción = ...}}, la misma para varios juegos."""
    _tpl, param = ES_DESC[game]
    bodies = [m.group(1) for m in re.finditer(r'\|\s*%s\s*=(.*?)%s' % (re.escape(param), END), text, re.S)]
    if game == 'IE':
        bodies += re.findall(r'\{\{Descripci[oó]n/IE\s*\|(?:[^{}]|\{\{[^{}]*\}\})*?\|\s*Descripci[oó]n\s*=(.*?)%s' % END, text, re.S)
    for m in re.finditer(r'\{\{Descripci[oó]n/Varios\s*\|\s*IE\s*=\s*\{\{IE\|[^|}]*\|([^}]*)\}\}\s*\|\s*Descripci[oó]n\s*=(.*?)%s' % END, text, re.S):
        r = re.search(r'IE (\d)(?:-(\d))?$', m.group(1).strip())
        games = range(int(r.group(1)), int(r.group(2) or r.group(1)) + 1) if r else range(1, 4) if 'Mark' in m.group(1) else ()
        if GAME_NO[game] in games:
            bodies.append(m.group(2))
    for body in bodies:
        if 'Aviso' in body:
            continue
        if out := es_text_of(body):
            return out
    return None


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
es_matches = []  # jugadores emparejados por la tabla de su equipo (para revisarlos)
no_spanish = []  # jugadores sin descripción en español: hay que añadirla a overrides.json


def build_player(key, number, team_name, season, order, used_ids):
    d = PLAYERS[key]
    page = char_pages.get(d.get('page', ''))
    text = content(page) if page else ''
    name = OVERRIDES['names'].get(d.get('page', '')) or dub_name(text, d.get('page', '')) or d.get('page') or key
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
    es_text = content(es_pages.get(es_titles.get(d.get('page', ''), ''), {}))
    if not es_text and (team_name, key) in es_by_player:
        es_text = content(es_pages.get(es_by_player[(team_name, key)], {}))
        es_matches.append(f"{team_name} | {name} -> {es_by_player[(team_name, key)]} | {next((x for g in order if (x := description_es(es_text, g))), '')} | {next((x for g in order if (x := description(text, g))), '')}")
    desc = OVERRIDES['descriptions'].get(d.get('page', ''))
    desc = desc or next((x for g in order if (x := description_es(es_text, g))), None)
    if not desc:
        english = next((x for g in order if (x := description(text, g))), None)
        no_spanish.append(f"{d.get('page') or key} | {name} | {team_name} | {english or ''}")
    if desc:
        desc = desc.replace('\ufeff', '').strip()
        for wrong, right in OVERRIDES['fixes']:
            desc = desc.replace(wrong, right)
        if desc[-1].isalnum():
            desc += '.'
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
    look_as = STYLE_OF.get(name, name)
    style = STYLE.get(look_as) or (
        pick(look_as, SHIRTS),
        pick(look_as + 's', ['#f2f2f2', '#1a1a1a', '#2a3a5a']),
        pick(look_as + 'g', ['#e8892b', '#3a8a3a', '#5a5a5a']),
        pick(look_as, SHIRTS),
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
no_spanish = sorted(set(no_spanish))
print('jugadores sin descripción en español (añádela en tools/wiki/overrides.json):', len(no_spanish))
os.makedirs(os.path.join(ROOT, 'tools', 'wiki', '.cache'), exist_ok=True)
with open(os.path.join(ROOT, 'tools', 'wiki', '.cache', 'sin_descripcion.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(no_spanish) + '\n')
with open(os.path.join(ROOT, 'tools', 'wiki', '.cache', 'emparejados_es.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(set(es_matches))) + '\n')
