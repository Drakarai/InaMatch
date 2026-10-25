"""Resuelve redirecciones de títulos en una wiki (MediaWiki), en lotes de 50.

Uso: python3 -I resolve_redirects.py <api_url> <titulos.json> <salida.json>
Salida: {titulo_original: titulo_final}
"""
import json
import sys
import time
import urllib.parse
import urllib.request

API, SRC, OUT = sys.argv[1:4]
titles = json.load(open(SRC, encoding='utf-8'))
UA = 'InaMatch-fan-project/0.1 (descarga puntual de datos de supertécnicas)'
result = {}
for i in range(0, len(titles), 50):
    chunk = titles[i : i + 50]
    params = {'action': 'query', 'titles': '|'.join(chunk), 'redirects': '1', 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        q = json.load(r)['query']
    norm = {n['from']: n['to'] for n in q.get('normalized', [])}
    redir = {n['from']: n['to'] for n in q.get('redirects', [])}
    for t in chunk:
        cur = norm.get(t, t)
        for _ in range(3):
            cur = redir.get(cur, cur)
        result[t] = cur
    time.sleep(0.4)
json.dump(result, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
print('resueltos', len(result), 'cambiados', sum(1 for k, v in result.items() if k != v))
