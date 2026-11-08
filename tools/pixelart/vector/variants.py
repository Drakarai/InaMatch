"""Versiones distintas de cada personaje para los fichajes de Mi club: src/data/variants.json, "<equipo>:<jugador>" -> huella de
su dibujo de partido. El gacha (src/club/pool.ts) saca una carta por personaje y dibujo: Mark Evans sale una vez (su
dibujo es el mismo en todos sus equipos aunque cambien sus técnicas), pero Fubuki normal y Fubuki con Atsuya, o los
adultos del Inazuma Japón Legendario, salen aparte porque su sprite de partido es otro.

Uso (desde la raíz del repo, después de exportar los sprites): python3 -I tools/pixelart/vector/variants.py
"""
import glob
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chars as C  # noqa: E402
import export as E  # noqa: E402


def main():
    out = {}
    for f in sorted(glob.glob(os.path.join(E.ROOT, 'src', 'data', 'teams', '*.json'))):
        t = json.load(open(f, encoding='utf-8'))
        if t['id'] == 'club':
            continue
        for p in t['players']:
            key = E.key_for(t['id'], p['id'])
            if not key:
                continue
            spec = json.dumps(C.CHARS[key], sort_keys=True, default=repr)
            out[f"{t['id']}:{p['id']}"] = hashlib.md5(spec.encode()).hexdigest()[:8]
    path = os.path.join(E.ROOT, 'src', 'data', 'variants.json')
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, separators=(',', ':'), sort_keys=True)
    print(len(out), 'jugadores;', len(set(out.values())), 'dibujos distintos')


if __name__ == '__main__':
    main()
