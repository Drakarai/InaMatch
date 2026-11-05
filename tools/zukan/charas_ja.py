"""Nombres japoneses de los personajes de la enciclopedia oficial (zukan.inazuma.jp/chara_param/).

Sirve para encontrar el retrato de los que en la enciclopedia tienen otro nombre de doblaje que en la wiki
(Aliea, Osoroshii Kage, robots...): se emparejan por el nombre japonés, en kanji o en kana.
Guarda tools/zukan/charas_ja.json: [{name (kanji), kana, nick, game, img}].

Uso (desde la raíz del repo): python3 -I tools/zukan/charas_ja.py
"""
import html
import json
import os
import re
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
URL = 'https://zukan.inazuma.jp/chara_param/?per_page=200&page={}'


def ruby(fragment):
    """('円堂 守', 'えんどう まもる') a partir de las etiquetas <ruby>."""
    base, kana = [], []
    for body in re.findall(r'<ruby>(.*?)</ruby>', fragment, re.S):
        rt = re.search(r'<rt>(.*?)</rt>', body, re.S)
        text = html.unescape(re.sub(r'<rt>.*?</rt>', '', body, flags=re.S)).strip()
        base.append(text if text else (' ' if body.strip() == '' and body else ''))
        kana.append(html.unescape(rt.group(1)).strip() if rt else text)
    clean = lambda parts: re.sub(r'\s+', ' ', ''.join(parts)).strip()
    return clean(base), clean(kana)


CACHE = os.path.join(HERE, '..', 'wiki', '.cache', 'zukan_ja')


def page(n):
    path = os.path.join(CACHE, f'{n}.html')
    if os.path.exists(path):
        return open(path, encoding='utf-8').read()
    req = urllib.request.Request(URL.format(n), headers={'User-Agent': 'InaMatch (proyecto de fans)'})
    h = urllib.request.urlopen(req, timeout=120).read().decode('utf-8')
    os.makedirs(CACHE, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(h)
    return h


def main():
    out = []
    n = 1
    while True:
        h = page(n)
        # además de las fichas hay un bloque de plantilla sin imagen: si no hay ninguna ficha, se acabó
        items = [b for b in h.split('<div class="nameBox">')[1:] if 'class="appearedWorks"' in b]
        if not items:
            break
        for blk in items:
            name_html = re.search(r'<span class="name">(.*?)</span>', blk, re.S)
            nick_html = re.search(r'<span class="nickname">(.*?)</span>', blk, re.S)
            img = re.search(r'<img src="([^"]+\.png)"', blk)
            game = re.search(r'class="appearedWorks">.*?<dd>(.*?)</dd>', blk, re.S)
            name, kana = ruby(name_html.group(1)) if name_html else ('', '')
            nick, nick_kana = ruby(nick_html.group(1)) if nick_html else ('', '')
            out.append({
                'name': name,
                'kana': kana,
                'nick': nick,
                'nick_kana': nick_kana,
                'game': re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', game.group(1)))).strip() if game else '',
                'img': img.group(1) if img else '',
            })
        print('página', n, len(out), flush=True)
        n += 1
        time.sleep(0.5)
    with open(os.path.join(HERE, 'charas_ja.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
