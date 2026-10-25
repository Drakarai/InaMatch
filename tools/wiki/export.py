"""Último paso: completa afinidades y tipos con las categorías de la wiki y escribe
el catálogo compacto que usa el juego.

Uso: python3 -I export.py <tecnicas.json> <hissatsu_raw.json> <salida.json>
"""
import json
import re
import sys

moves = json.load(open(sys.argv[1], encoding='utf-8'))
raw = {p['title']: p for p in json.load(open(sys.argv[2], encoding='utf-8'))}

ELEMENT = {'Fire': 'fire', 'Wind': 'wind', 'Forest': 'wood', 'Mountain': 'earth', 'Void': 'neutral'}
KIND = {'Shoot': 'shoot', 'Dribble': 'dribble', 'Block': 'block', 'Catch': 'catch'}
CAT_KIND = {'Shoot hissatsu': 'Shoot', 'Dribble hissatsu': 'Dribble', 'Block hissatsu': 'Block', 'Catch hissatsu': 'Catch', 'Keeper hissatsu': 'Catch'}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


out = []
for m in moves:
    cat_list = [c.replace('Category:', '').replace('_', ' ') for c in raw.get(m['en'], {}).get('categories', [])]
    cats = set(cat_list)
    # algunas técnicas tienen versiones de distinta afinidad (Mano mágica: Montaña la de Mark, Bosque la de Darren);
    # la wiki las mete en varias categorías, en el orden de sus versiones
    cat_elements = [c.removesuffix(' hissatsu') for c in cat_list if c.removesuffix(' hissatsu') in ELEMENT and c.endswith(' hissatsu')]
    element = m['element'] if m['element'] in ELEMENT else (cat_elements[0] if cat_elements else None)
    # si la ficha inglesa no da la afinidad (usa una plantilla), manda el orden de versiones de la página:
    # la descripción las lista como "{{Mountain}} version", "{{Forest}} version"... (las categorías van por orden alfabético)
    text = raw.get(m['en'], {}).get('wikitext') or ''
    versions = list(dict.fromkeys(re.findall(r'\{\{(Fire|Wind|Forest|Mountain|Void)\}\} version', text)))
    if versions:
        cat_elements = versions + [e for e in cat_elements if e not in versions]
        if re.search(r'\|\s*element\s*=\s*\{\{', text):
            element = versions[0]
    kind = m['type'] if m['type'] in KIND else next((v for k, v in CAT_KIND.items() if k in cats), None)
    if not element or not kind:
        continue
    dub = re.sub(r'\{\{PAGENAME\}\}', m['en'], m.get('dub') or '').split('\n')[0].lstrip('*').strip()
    out.append(
        {
            'id': slug(m['en']),
            'es': m['es'],
            'en': m['en'],
            'dub': re.sub(r'\s*\(.*?\)', '', dub) or m['en'],
            'kind': KIND[kind],
            'element': ELEMENT[element],
            'elements': list(dict.fromkeys(ELEMENT[e] for e in [element, *cat_elements])),
            'powerVr': m['power_vr'],
            'costVr': m['cost_vr'],
            'tpIe3': m['tp_ie3'],
            'victoryRoad': m['vr'],
        }
    )
out.sort(key=lambda x: x['id'])
json.dump(out, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('catálogo:', len(out), 'técnicas | con nombre en español:', sum(1 for x in out if x['es']))
