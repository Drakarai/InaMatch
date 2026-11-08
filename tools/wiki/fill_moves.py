"""Deja a todos los jugadores (equipos y ojeadores) con 4 supertécnicas, sin regenerar el resto de los datos.

- Si le faltan: primero las que ese mismo personaje lleva en sus otros equipos o formas (misma ficha de la wiki), y si
  no llegan, las más usadas en su temporada por los de su demarcación, mejor de su afinidad y de una potencia parecida a
  las suyas. Se eligen por el tipo que le falta para su puesto: portero, paradas; defensa, bloqueos; medio, regates;
  delantero, tiros (y luego del resto).
- Si le sobran (5 o 6): se quedan las 4 que mejor cubren su puesto, las más fuertes de cada tipo.
Siempre igual para el mismo jugador (no hay azar).

Uso (desde la raíz del repo): python3 -I tools/wiki/fill_moves.py
"""
import glob
import json
import os
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# tipos de técnica que quiere cada puesto, por orden
WANT = {'GK': ['catch', 'catch', 'block', 'dribble'], 'DF': ['block', 'block', 'dribble', 'shoot'],
        'MF': ['dribble', 'shoot', 'block', 'dribble'], 'FW': ['shoot', 'shoot', 'dribble', 'block']}


def main():
    moves = {m['id']: m for m in json.load(open(os.path.join(ROOT, 'src', 'data', 'moves.json'), encoding='utf-8'))}
    team_files = sorted(f for f in glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json')) if not f.endswith('club.json'))
    teams = [(f, json.load(open(f, encoding='utf-8'))) for f in team_files]
    scouts_path = os.path.join(ROOT, 'src', 'data', 'scouts.json')
    scouts = json.load(open(scouts_path, encoding='utf-8'))
    everyone = [(t['id'].split('-')[0], p) for _, t in teams for p in t['players']] + [(s, p) for s, ps in scouts.items() for p in ps]
    # técnicas de cada personaje en todas sus versiones, y las más usadas por temporada y puesto
    by_char = defaultdict(list)
    usage = defaultdict(Counter)
    for season, p in everyone:
        for m in p['moves']:
            if m in moves:
                if p.get('wiki'):
                    by_char[p['wiki']].append(m)
                usage[(season, p['position'])][m] += 1
                usage[(season, '*')][m] += 1

    def kinds(ms):
        return Counter(moves[m]['kind'] for m in ms if m in moves)

    def next_kind(p, ms):
        have = kinds(ms)
        need = Counter()
        for k in WANT[p['position']][:len(ms) + 1]:
            need[k] += 1
        for k in WANT[p['position']]:
            if have[k] < need[k] or have[k] < WANT[p['position']].count(k):
                return k
        return WANT[p['position']][0]

    def pick(season, p, ms):
        kind = next_kind(p, ms)
        target = sum(moves[m]['power'] for m in ms if m in moves) / max(1, len([m for m in ms if m in moves])) if ms else None
        # 1) del mismo personaje
        own = [m for m in dict.fromkeys(by_char.get(p.get('wiki'), [])) if m not in ms]
        for pool in ([m for m in own if moves[m]['kind'] == kind], own):
            if pool:
                return pool[0]
        # 2) de su temporada y puesto: las del tipo que le falta, por afinidad, uso y potencia parecida
        for scope in ((season, p['position']), (season, '*')):
            cands = [m for m, n in usage[scope].items() if m not in ms and moves[m]['kind'] == kind]
            if not cands:
                continue
            if target is None:
                pw = sorted(moves[m]['power'] for m in cands)
                target = pw[len(pw) // 2]

            def score(m):
                mv = moves[m]
                return (mv['element'] != p['element'], abs(mv['power'] - target) // 10, -usage[scope][m], m)
            return min(cands, key=score)
        return None

    changed = 0
    for season, p in everyone:
        ms = [m for m in dict.fromkeys(p['moves']) if m in moves]
        before = list(p['moves'])
        if len(ms) > 4:  # sobran: las más fuertes de cada tipo que pide su puesto
            keep = []
            for k in WANT[p['position']]:
                best = sorted((m for m in ms if moves[m]['kind'] == k and m not in keep), key=lambda m: -moves[m]['power'])
                if best:
                    keep.append(best[0])
            keep += sorted((m for m in ms if m not in keep), key=lambda m: -moves[m]['power'])
            ms = [m for m in ms if m in keep[:4]]
        while len(ms) < 4:
            m = pick(season, p, ms)
            if not m:
                break
            ms.append(m)
        if ms != before:
            p['moves'] = ms
            changed += 1
    for f, t in teams:
        open(f, 'w', encoding='utf-8').write(json.dumps(t, ensure_ascii=False, indent=1) + '\n')
    with open(scouts_path, 'w', encoding='utf-8') as fh:
        fh.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v, ensure_ascii=False, separators=(",", ":"))}' for k, v in scouts.items()) + '\n}\n')
    print(f'{changed} jugadores cambiados; con 4 técnicas: {sum(len(p["moves"]) == 4 for _, p in everyone)} de {len(everyone)}')


if __name__ == '__main__':
    main()
