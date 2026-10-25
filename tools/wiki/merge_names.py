"""Une las técnicas de la wiki inglesa (datos de Victory Road) con su nombre en español.

Emparejado, por orden de fiabilidad:
1. enlace entre idiomas (en cualquiera de las dos direcciones),
2. nombre japonés en katakana,
3. nombre del doblaje inglés que aparece en la ficha española.

Uso: python3 -I merge_names.py <hissatsu.json> <supertecnicas_raw.json> <redir_en.json> <redir_es.json> <salida.json>
"""
import json
import re
import sys
import unicodedata

en_moves = json.load(open(sys.argv[1], encoding='utf-8'))
es_raw = json.load(open(sys.argv[2], encoding='utf-8'))
redir_en = json.load(open(sys.argv[3], encoding='utf-8'))
redir_es = json.load(open(sys.argv[4], encoding='utf-8'))
OUT = sys.argv[5]


def norm(s):
    s = unicodedata.normalize('NFKC', s or '').lower()
    s = re.sub(r'\(.*?\)', '', s)
    return re.sub(r'[^\w]+', '', s)


def es_infobox(text):
    m = re.search(r'\{\{Supertécnica\s*\n(.*?)\n\}\}', text or '', re.S)
    if not m:
        return {}
    fields, key, depth = {}, None, 0
    for line in m.group(1).split('\n'):
        mm = re.match(r'\|\s*([^=|]+?)\s*=(.*)', line)
        if mm and depth == 0:
            key = mm.group(1).strip()
            fields[key] = mm.group(2).strip()
        elif key:
            fields[key] += '\n' + line
        depth += line.count('{{') - line.count('}}')
    return fields


TYPE_ES = {'Tiro': 'Shoot', 'Regate': 'Dribble', 'Bloqueo': 'Block', 'Atajo': 'Catch', 'Parada': 'Catch', 'Portero': 'Catch'}
ELEM_ES = {'Fuego': 'Fire', 'Aire': 'Wind', 'Bosque': 'Forest', 'Montaña': 'Mountain', 'Neutro': 'Void', 'Vacío': 'Void'}

by_link, by_kata, by_dub, es_info = {}, {}, {}, {}
for p in es_raw:
    title = p['title']
    if not p.get('wikitext') or p['wikitext'].lstrip().upper().startswith('#REDIREC'):
        continue
    # el enlace a la wiki inglesa vale aunque la ficha use otra plantilla
    if p.get('link'):
        by_link[norm(redir_en.get(p['link'], p['link']))] = title
    f = es_infobox(p['wikitext'])
    if not f:
        continue
    info = {'title': title}
    t = re.search(r'ST/Tipo/(\w+)', f.get('Tipo', ''))
    e = re.search(r'ST/Elemento/(\w+)', f.get('Elemento', ''))
    info['type'] = TYPE_ES.get(t.group(1)) if t else None
    info['element'] = ELEM_ES.get(e.group(1)) if e else None
    n = re.search(r'(\d+)', f.get('PT IE 3', ''))
    info['tp_ie3'] = int(n.group(1)) if n else None
    es_info[title] = info
    k = re.search(r'K\s*=\s*([^|}]+)', f.get('Nombre Japonés', ''))
    if k:
        by_kata.setdefault(norm(k.group(1)), title)
    for line in f.get('Nombre DOB', '').split('\n') + [f.get('Nombre Japonés', '')]:
        if '{{EN}}' in line or '<br>' in line:
            name = re.sub(r'\{\{.*?\}\}', '', line.split('<br>')[-1]).strip(' *,')
            for part in name.split(','):
                if part.strip():
                    by_dub.setdefault(norm(part), title)

stats = {'enlace': 0, 'katakana': 0, 'doblaje': 0, 'sin nombre': 0}
merged = []
for m in en_moves:
    es = redir_es.get(m['es'], m['es']) if m.get('es') else None
    how = 'enlace' if es else None
    if not es and norm(m['en']) in by_link:
        es, how = by_link[norm(m['en'])], 'enlace'
    if not es and m.get('jp'):
        kata = norm(re.split(r'[\s(（]', m['jp'])[0])
        if kata in by_kata:
            es, how = by_kata[kata], 'katakana'
    if not es:
        for cand in (m['en'], m.get('dub')):
            if cand and norm(cand) in by_dub:
                es, how = by_dub[norm(cand)], 'doblaje'
                break
    stats[how or 'sin nombre'] += 1
    info = es_info.get(es, {})
    # la ficha inglesa a veces trae plantillas en lugar del elemento; la española lo completa
    element = m['element'] if m['element'] in ('Fire', 'Wind', 'Forest', 'Mountain', 'Void') else info.get('element')
    merged.append({**m, 'es': es, 'match': how, 'element': element, 'tp_ie3': m['tp_ie3'] or info.get('tp_ie3')})

json.dump(merged, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('técnicas:', len(merged), stats)
vr = [x for x in merged if x['vr']]
print('de Victory Road:', len(vr), '| con nombre en español:', sum(1 for x in vr if x['es']))
print('sin afinidad válida:', sum(1 for x in merged if not x['element']))
