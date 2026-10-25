"""Descarga todas las páginas de una categoría de una wiki MediaWiki (Fandom) con su
wikitexto, sus categorías y el enlace a otro idioma.

Uso: python3 -I fetch_category.py <api_url> <categoría> <idioma_enlace> <salida.json>
  inglés:  https://inazuma-eleven.fandom.com/api.php  Category:Hissatsu      es
  español: https://inazuma.fandom.com/es/api.php      Categoría:Supertécnicas en
"""
import json
import sys
import time
import urllib.parse
import urllib.request

API, CATEGORY, LINK_LANG, OUT = sys.argv[1:5]
UA = 'InaMatch-fan-project/0.1 (descarga puntual de datos de supertécnicas)'


def get(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # reintento con espera creciente
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))
            print('reintento', e, file=sys.stderr)


pages = {}
cont = {}
batches = 0
while True:
    data = get(
        {
            'action': 'query',
            'generator': 'categorymembers',
            'gcmtitle': CATEGORY,
            'gcmnamespace': '0',
            'gcmlimit': '50',
            'prop': 'revisions|langlinks|categories',
            'rvprop': 'content',
            'rvslots': 'main',
            'lllang': LINK_LANG,
            'lllimit': 'max',
            'cllimit': 'max',
            **cont,
        }
    )
    batches += 1
    for p in data.get('query', {}).get('pages', []):
        entry = pages.setdefault(p['title'], {'title': p['title']})
        revs = p.get('revisions')
        if revs:
            entry['wikitext'] = revs[0]['slots']['main']['content']
        for ll in p.get('langlinks', []):
            entry['link'] = ll['title']
        for c in p.get('categories', []):
            entry.setdefault('categories', []).append(c['title'])
    if 'continue' not in data:
        break
    cont = data['continue']
    time.sleep(0.5)
    if batches % 10 == 0:
        print('lotes', batches, 'páginas', len(pages), file=sys.stderr)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(list(pages.values()), f, ensure_ascii=False)
print('lotes', batches, 'páginas', len(pages), 'con enlace de idioma', sum(1 for p in pages.values() if 'link' in p))
