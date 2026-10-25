"""Extrae de la ficha {{Hissatsu}} de cada técnica los datos útiles para InaMatch.

Uso: python3 -I parse_hissatsu.py <hissatsu_raw.json> <salida.json>
"""
import json
import re
import sys
from collections import Counter

raw = json.load(open(sys.argv[1], encoding='utf-8'))


def infobox(text):
    m = re.search(r'\{\{Hissatsu\s*\n(.*?)\n\}\}', text or '', re.S)
    if not m:
        return None
    body = m.group(1)
    fields = {}
    key = None
    depth = 0
    for line in body.split('\n'):
        mm = re.match(r'\|\s*([\w]+)\s*=(.*)', line)
        if mm and depth == 0:
            key = mm.group(1)
            fields[key] = mm.group(2).strip()
        elif key:
            fields[key] += '\n' + line
        depth += line.count('{{') - line.count('}}')
    return fields


def clean(v):
    v = re.sub(r'<br\s*/?>', ' / ', v or '')
    v = re.sub(r"'''?", '', v)
    v = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', v)
    return v.strip()


def per_game(v, game):
    """Número de la línea '*60 (''Victory Road'')' de un campo con varios juegos."""
    for line in (v or '').split('\n'):
        if game in line:
            n = re.search(r'(\d+)', line)
            if n:
                return int(n.group(1))
    return None


def first_int(v):
    n = re.search(r'(\d+)', v or '')
    return int(n.group(1)) if n else None


out = []
for p in raw:
    f = infobox(p.get('wikitext'))
    if not f:
        continue
    power = f.get('power', '')
    out.append(
        {
            'en': p['title'],
            'es': p.get('link'),
            'dub': clean(f.get('name_dub')) or None,
            'jp': clean(f.get('name_jp')) or None,
            'type': clean(f.get('type')).split('/')[0].strip() or None,
            'element': clean(f.get('element')).split('/')[0].strip() or None,
            'characteristic': clean(f.get('characteristic')) or None,
            'power_vr': per_game(power, 'Victory Road'),
            'power_go': per_game(power, "''GO''"),
            'power_cs': per_game(power, 'Chrono Stone'),
            'power_gx': per_game(power, 'Galaxy'),
            'tp_ie3': first_int(f.get('tp_ie3')),
            'tp_ie2': first_int(f.get('tp_ie2')),
            'tp_ie': first_int(f.get('tp_ie')),
            'cost_vr': first_int(f.get('t_vr')),
            'vr': 'Victory Road' in power or 't_vr' in f,
        }
    )

json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('fichas leídas:', len(out), 'de', len(raw))
print('tipos:', Counter(o['type'] for o in out).most_common(8))
print('afinidades:', Counter(o['element'] for o in out).most_common(8))
for k in ['es', 'power_vr', 'cost_vr', 'tp_ie3', 'power_go', 'power_cs']:
    print(f'con {k}:', sum(1 for o in out if o[k]))
print('de VR:', sum(1 for o in out if o['vr']), '| de VR con nombre es:', sum(1 for o in out if o['vr'] and o['es']))
