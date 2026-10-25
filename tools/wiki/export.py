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
    cats = {c.replace('Category:', '').replace('_', ' ') for c in raw.get(m['en'], {}).get('categories', [])}
    element = m['element'] if m['element'] in ELEMENT else next((e for e in ELEMENT if f'{e} hissatsu' in cats), None)
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
            'powerVr': m['power_vr'],
            'costVr': m['cost_vr'],
            'tpIe3': m['tp_ie3'],
            'victoryRoad': m['vr'],
        }
    )
out.sort(key=lambda x: x['id'])
json.dump(out, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('catálogo:', len(out), 'técnicas | con nombre en español:', sum(1 for x in out if x['es']))
