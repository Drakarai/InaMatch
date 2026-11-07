"""Baja las referencias 3D (enciclopedia oficial) de los jugadores de un equipo para dibujarlos.

Para cada jugador: nombre japonés de su ficha de la wiki -> ficha de la enciclopedia en japonés (tools/wiki/.cache/
zukan_ja, de tools/zukan/charas_ja.py) -> visor 3D -> busto de frente (b0), perfil (b6), espalda (b4) y cuerpo (f0).

Uso: python3 -I tools/pixelart/vector/refs.py <equipo | scouts-<temporada>> <carpeta de salida> [ids,separados,por,comas]
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
# juegos de la enciclopedia, del más parecido al menos, para cada temporada: el modelo 3D es el de ese juego
G = {'ie1': 'イナズマイレブン', 'ie2': 'イナズマイレブン2 ', 'ie3': 'イナズマイレブン3 ', 'go': 'イナズマイレブンGO シャイン', 'cs': 'イナズマイレブンGO2 ',
     'gx': 'イナズマイレブンGO ギャラクシー', 'ares': 'イナズマイレブン アレス', 'orion': 'イナズマイレブン オリオン', 'vr': 'イナズマイレブン 英雄'}
ORDER = {'ie1': ['ie1', 'ie2', 'ie3', 'vr'], 'ie2': ['ie2', 'ie1', 'ie3', 'vr'], 'ie3': ['ie3', 'ie2', 'ie1', 'vr'],
         'go': ['go', 'cs', 'gx', 'vr'], 'cs': ['cs', 'go', 'gx', 'vr'], 'gx': ['gx', 'cs', 'go', 'vr'],
         'ares': ['ares', 'orion', 'vr'], 'orion': ['orion', 'ares', 'vr'], 'vr': ['vr']}
# equipos en los que los personajes juegan con otra identidad (los alienígenas de la Academia Alius): se busca el
# modelo por su alias (nickname_jp: レーゼ, no 緑川リュウジ)
ALIAS_TEAMS = {'ie2-gemini-storm', 'ie2-epsilon', 'ie2-epsilon-kai', 'ie2-diamond-dust', 'ie2-prominence', 'ie2-chaos', 'ie2-the-genesis'}


# nombres japoneses que la wiki escribe con otro kanji que la enciclopedia (o que en la wiki no salen): nombre de la wiki
# (sin espacios) -> nombre en la enciclopedia
ZUKAN_NAME = {
    '小庭利徳': '木庭利徳', 'コバ': '木庭利徳', '飛豆祟利': '飛豆崇利', '蒼月望観': '蒼月希観', '真住火郎志': '真住火朗志', '伊理虹七郎': '伊里虹七郎',
    '御殿場亨': '御殿場享', '正宗五郎': '正宗五朗', '新木明': '新木朗', '佐々鬼巌': '佐々鬼厳', '村上軍紀': '村上軍記', '山崎虎太郎': '山裂虎太郎',
    '遊海端': '遊海瑞', '天野帙司': '天野快司', '長久童子': '永久童子', '伊矢部聡志': '伊矢部敏志', '加納一括': '加納一活', '夜須天恵': '夜須天慧',
    '早矢馬齧郎': '早矢馬鏑郎', 'サタン': 'ザタン',
}
# fichas de la wiki sin nombre japonés: título de la ficha -> nombre en la enciclopedia
ZUKAN_PAGE = {'Guanyu': '関羽', 'Zhangfei': '張飛'}


def pick(cands, season):
    """El modelo del juego de la temporada; si no sale en él, el del juego más parecido."""
    for s in ORDER.get(season, []):
        for g, q in cands:
            if (g == G[s]) if s == 'ie1' else g.startswith(G[s]):
                return q
    return cands[0][1]


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
            n = re.search(r'\|\s*nickname_jp\s*=\s*([^\n|]*)', text)
            out[t] = (m.group(1).strip().lstrip('*') if m else '', n.group(1).strip().lstrip('*') if n else '')
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
    ids = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else None  # solo esos jugadores
    os.makedirs(out, exist_ok=True)
    if tid.startswith('scouts-'):  # ojeadores de una temporada (src/data/scouts.json)
        season = tid.split('-', 1)[1]
        team = {'players': json.load(open(os.path.join(ROOT, 'src', 'data', 'scouts.json'), encoding='utf-8'))[season]}
    else:
        season = tid.split('-')[0]
        team = json.load(open(os.path.join(ROOT, 'src', 'data', 'teams', tid + '.json'), encoding='utf-8'))
    if ids:
        team['players'] = [p for p in team['players'] if p['id'] in ids]
    jp = wiki_jp([p['wiki'] for p in team['players'] if p.get('wiki')])
    links = zukan_links()
    for p in team['players']:
        name, alias = (re.sub(r'\s', '', x) for x in jp.get(p.get('wiki', ''), ('', '')))
        names = [alias, name] if tid in ALIAS_TEAMS else [name, alias]
        names = [ZUKAN_NAME.get(n, n) for n in names] + ([ZUKAN_PAGE[p['wiki']]] if p.get('wiki') in ZUKAN_PAGE else [])
        cands = next((links[n] for n in names if n and n in links), [])
        if not cands:
            print(p['id'], 'sin modelo 3D', name, alias)
            continue
        q = pick(cands, season)
        h = get('https://zukan.inazuma.jp/chara_model_view/?q=' + q).decode()
        base = re.search(r'return `(https://[^`]+)` \+ `_r', h).group(1)
        for tag, suf in (('b0', '_r0'), ('b6', '_r6'), ('b4', '_r4'), ('f0', '_r0_fullbody')):
            Image.open(io.BytesIO(get(base + suf + '.webp'))).convert('RGBA').save(os.path.join(out, f"{p['id']}_{tag}.png"))
        print(p['id'], 'ok')


if __name__ == '__main__':
    main()
