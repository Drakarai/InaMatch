"""Fichas de todos los personajes de la enciclopedia oficial (Inazugle, zukan.inazuma.jp/en/chara_param/).

De cada ficha guarda el nombre (el del doblaje inglés), el apodo, el juego en el que sale, la descripción en
inglés, la posición, la afinidad, el retrato y los parámetros de Victory Road a nivel 50 (Tiro, Control,
Técnica, Presión, Físico, Agilidad e Inteligencia). tools/wiki/teams.py los usa para los jugadores que no
tienen atributos en la wiki (los de Victory Road y los de Ares/Orión) y para emparejar personajes.

Uso (desde la raíz del repo): python3 -I tools/zukan/charas.py   -> tools/zukan/charas.json
"""
import html
import json
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
URL = 'https://zukan.inazuma.jp/en/chara_param/?page={}'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de fichas)'
STATS = {'Kick': 'kick', 'Control': 'control', 'Technique': 'technique', 'Pressure': 'pressure',
         'Physical': 'physical', 'Agility': 'agility', 'Intelligence': 'intelligence'}


def get(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode('utf-8')
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError('Inazugle no responde: ' + url)


def text(s):
    return html.unescape(re.sub(r'<br\s*/?>', ' ', re.sub(r'\s+', ' ', s or ''))).strip()


def parse(page):
    out = []
    for blk in re.split(r'<div class="nameBox">\s*<span class="name">', page)[1:]:
        name = re.search(r'<ruby>(.*?)</ruby>', blk, re.S)
        nick = re.search(r'class="nickname">\s*<ruby>(.*?)</ruby>', blk, re.S)
        img = re.search(r'<img src="(https://[^"]+)"', blk)
        game = re.search(r'class="appearedWorks">.*?<dd>(.*?)</dd>', blk, re.S)
        desc = re.search(r'class="description">(.*?)</p>', blk, re.S)
        pos = re.search(r'<dt>Position</dt>\s*<dd><p>(.*?)</p>', blk)
        elem = re.search(r'<dt>Element</dt>\s*<dd><p>(.*?)</p>', blk)
        role = re.search(r'<dt>Character Role</dt>\s*<dd>(.*?)</dd>', blk)
        gender = re.search(r'<dt>Gender</dt>\s*<dd>(.*?)</dd>', blk)
        stats = {}
        for k, v in re.findall(r'<dt>(\w+)</dt>\s*<dd>\s*<table>.*?<td>(\d+)</td>', blk, re.S):
            if k in STATS:
                stats[STATS[k]] = int(v)
        out.append({
            'name': text(name.group(1)) if name else '',
            'nick': text(nick.group(1)) if nick else '',
            'game': text(game.group(1)) if game else '',
            'position': text(pos.group(1)) if pos else '',
            'element': text(elem.group(1)) if elem else '',
            'role': text(role.group(1)) if role else '',
            'gender': text(gender.group(1)) if gender else '',
            'desc': text(desc.group(1)) if desc else '',
            'img': img.group(1) if img and 'secret' not in img.group(1) else None,
            'stats': stats,
        })
    return out


def main():
    first = get(URL.format(1))
    last = max(int(n) for n in re.findall(r'chara_param/\?page=(\d+)', first))
    charas = parse(first)
    for n in range(2, last + 1):
        charas += parse(get(URL.format(n)))
        if n % 10 == 0:
            print(f'{n}/{last}', file=sys.stderr)
        time.sleep(0.4)
    with open(os.path.join(HERE, 'charas.json'), 'w', encoding='utf-8') as f:
        f.write('[\n' + ',\n'.join(json.dumps(c, ensure_ascii=False) for c in charas) + '\n]\n')
    print(len(charas), 'fichas', file=sys.stderr)


if __name__ == '__main__':
    main()
