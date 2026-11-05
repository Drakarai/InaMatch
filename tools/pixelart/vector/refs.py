"""Baja las referencias 3D (enciclopedia oficial) de los jugadores de un equipo para dibujarlos.

Para cada jugador: nombre japonés de su ficha de la wiki -> ficha de la enciclopedia en japonés (tools/wiki/.cache/
zukan_ja, de tools/zukan/charas_ja.py) -> visor 3D -> busto de frente (b0), perfil (b6), espalda (b4) y cuerpo (f0).

Uso: python3 -I tools/pixelart/vector/refs.py <equipo> <carpeta de salida>
"""
import glob
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
UA = {'User-Agent': 'InaMatch (proyecto de fans)'}
GAME = {'ie1': 'イナズマイレブン', 'ie2': 'イナズマイレブン2', 'ie3': 'イナズマイレブン3'}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()


def wiki_jp(titles):
    out = {}
    for i in range(0, len(titles), 40):
        q = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'format': 'json',
                                    'redirects': 1, 'titles': '|'.join(titles[i:i + 40])})
        d = json.loads(get('https://inazuma-eleven.fandom.com/api.php?' + q))
        back = {r['to']: r['from'] for r in d['query'].get('redirects', []) + d['query'].get('normalized', [])}
        for p in d['query']['pages'].values():
            t = back.get(p['title'], p['title'])
            t = back.get(t, t)
            text = p['revisions'][0]['slots']['main']['*'] if 'revisions' in p else ''
            m = re.search(r'\|\s*name_jp\s*=\s*([^\n|]*)', text)
            out[t] = m.group(1).strip().lstrip('*') if m else ''
    return out


def zukan_links():
    """nombre japonés -> [(juego, q del visor 3D)]"""
    links = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'wiki', '.cache', 'zukan_ja', '*.html')), key=lambda x: int(re.findall(r'\d+', x)[-1])):
        h = open(f, encoding='utf-8').read()
        for blk in h.split('<div class="nameBox">')[1:]:
            name = re.search(r'alt="([^"]+)"', blk)
            q = re.search(r'chara_model_view/\?q=([^"]+)"', blk)
            game = re.search(r'class="appearedWorks">.*?<dd>(.*?)</dd>', blk, re.S)
            if name and q:
                links.setdefault(re.sub(r'\s', '', name.group(1)), []).append((re.sub(r'\s+', ' ', game.group(1)).strip() if game else '', q.group(1)))
    return links


def main():
    tid, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    team = json.load(open(os.path.join(ROOT, 'src', 'data', 'teams', tid + '.json'), encoding='utf-8'))
    jp = wiki_jp([p['wiki'] for p in team['players'] if p.get('wiki')])
    links = zukan_links()
    game = GAME.get(tid.split('-')[0], '')
    for p in team['players']:
        name = re.sub(r'\s', '', jp.get(p.get('wiki', ''), ''))
        cands = links.get(name, [])
        if not cands:
            print(p['id'], 'sin modelo 3D', jp.get(p.get('wiki', '')))
            continue
        q = next((c for g, c in cands if g.startswith(game) and not g.startswith(game + '2') and not g.startswith(game + '3')), cands[0][1])
        h = get('https://zukan.inazuma.jp/chara_model_view/?q=' + q).decode()
        base = re.search(r'return `(https://[^`]+)` \+ `_r', h).group(1)
        for tag, suf in (('b0', '_r0'), ('b6', '_r6'), ('b4', '_r4'), ('f0', '_r0_fullbody')):
            Image.open(io.BytesIO(get(base + suf + '.webp'))).convert('RGBA').save(os.path.join(out, f"{p['id']}_{tag}.png"))
        print(p['id'], 'ok')


if __name__ == '__main__':
    main()
