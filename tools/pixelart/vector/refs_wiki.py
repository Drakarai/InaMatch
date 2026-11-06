"""Referencias 3D de la wiki inglesa para los personajes cuya versión no está en la enciclopedia oficial (por ejemplo los
alienígenas de la Academia Alius): archivos "(<equipo>) <nombre> 3D (1..4).png" (o "(VR) (1..4)").

Uso: python3 -I tools/pixelart/vector/refs_wiki.py <carpeta> <id>=<prefijo> ...
     p. ej. refs_wiki.py ref/ie2-epsilon dave-quagmire="(E) Desarm" zeke-valanche="(E) Zel"
Escribe <id>_v1.png ... <id>_v4.png (las cuatro vistas tal cual) para elegir cuál es cada una.
"""
import io
import json
import os
import sys
import urllib.parse
import urllib.request

from PIL import Image

API = 'https://inazuma-eleven.fandom.com/api.php'
UA = {'User-Agent': 'InaMatch (proyecto de fans)'}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for arg in sys.argv[2:]:
        pid, prefix = arg.split('=', 1)
        q = urllib.parse.urlencode({'action': 'query', 'list': 'allimages', 'aiprefix': prefix.replace(' ', '_') + '_3D', 'ailimit': 50, 'aiprop': 'url', 'format': 'json'})
        files = {i['name']: i['url'] for i in json.loads(get(API + '?' + q))['query']['allimages']}
        for v in ('_(VR)', '', '_(GO)', '_(SD)'):
            names = [f"{prefix.replace(' ', '_')}_3D{v}_({k}).png" for k in range(1, 5)]
            if all(n in files for n in names):
                for k, n in enumerate(names, 1):
                    Image.open(io.BytesIO(get(files[n]))).convert('RGBA').save(os.path.join(out, f'{pid}_v{k}.png'))
                print(pid, 'ok', v or '(DS)')
                break
        else:
            print(pid, 'sin 3D en la wiki:', sorted(files)[:6])


if __name__ == '__main__':
    main()
