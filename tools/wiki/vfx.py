"""Decide el efecto visual de cada supertécnica del juego a partir de su descripción en la wiki.

Lee src/data/moves.json, baja la página de cada técnica de la wiki inglesa de Inazuma Eleven y busca
en su nombre y sus descripciones (las de los juegos y la del anime) palabras que digan qué se ve:
una mano gigante, un muro, un tornado, fuego, hielo, un dragón... Las técnicas más conocidas, y las
que se revisaron mirando su imagen en la wiki, llevan su efecto puesto a mano en OVERRIDES.

Escribe tools/wiki/movefx_wiki.json: { "<id de la técnica>": "<efecto>" }. Solo se usa para las técnicas que no
salen en la enciclopedia oficial (las demás tienen receta en tools/zukan/recipes.txt).
Los efectos se dibujan en src/gfx/fx.ts.

Uso (desde la raíz del repo): python3 -I tools/wiki/vfx.py [--verbose]
"""
import collections
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de descripciones de técnicas)'

# Efecto -> palabras que lo delatan. El orden importa en los empates: primero lo más concreto
# (criaturas y objetos), luego los elementos y al final lo genérico.
KEYWORDS = [
    ('penguin', ['penguin']),
    ('dragon', ['dragon', 'hydra', 'serpent', 'wyvern', 'orochi']),
    ('bird', ['phoenix', 'eagle', 'bird', 'wing', 'feather', 'hawk', 'falcon', 'crow', 'swan', 'pegasus', 'condor', 'griffin', 'gryphon']),
    ('beast', ['lion', 'tiger', 'wolf', 'beast', 'fang', 'claw', 'bear', 'shark', 'cerberus', 'bull', 'horn', 'gorilla', 'panther', 'snake']),
    ('hand', ['hand', 'palm', 'majin', 'grip', 'catch it']),
    ('punch', ['punch', 'fist', 'knuckle', 'rocket']),
    ('wall', ['wall', 'pillar', 'tower', 'fortress', 'rampart', 'bulwark']),
    ('shield', ['shield', 'barrier', 'dome', 'net', 'web', 'curtain', 'mirror', 'cage', 'guard']),
    ('sword', ['sword', 'blade', 'slash', 'excalibur', 'spear', 'lance', 'gungnir', 'katana', 'cut', 'scythe', 'axe', 'arrow']),
    ('meteor', ['meteor', 'comet', 'star', 'galaxy', 'cosmic', 'space', 'planet', 'universe', 'big bang', 'gravity', 'astro', 'moon']),
    ('tornado', ['tornado', 'whirlwind', 'cyclone', 'spiral', 'vortex', 'hurricane', 'typhoon', 'twister', 'spin', 'screw', 'drill', 'rotat']),
    ('ice', ['ice', 'freez', 'frozen', 'snow', 'blizzard', 'frost', 'glacier', 'cold', 'icicle', 'aurora']),
    ('fire', ['fire', 'flame', 'blaze', 'burn', 'inferno', 'heat', 'scorch', 'magma', 'lava', 'volcano', 'explo']),
    ('lightning', ['lightning', 'thunder', 'electric', 'spark', 'bolt', 'inazuma', 'plasma', 'voltage', 'shock']),
    ('water', ['water', 'wave', 'tsunami', 'sea', 'aqua', 'ocean', 'splash', 'bubble', 'tide', 'rain', 'flood']),
    ('flower', ['flower', 'petal', 'rose', 'sakura', 'cherry', 'leaf', 'leaves', 'forest', 'tree', 'vine', 'bloom', 'wood']),
    ('earth', ['earth', 'rock', 'ground', 'quake', 'mountain', 'boulder', 'stone', 'sand', 'crush', 'land', 'boom']),
    ('dark', ['dark', 'shadow', 'death', 'demon', 'devil', 'evil', 'hell', 'curse', 'black', 'abyss', 'void', 'nightmare']),
    ('light', ['light', 'heaven', 'angel', 'holy', 'divine', 'god', 'shine', 'sun', 'rainbow', 'radian', 'glow', 'celestial']),
    ('clone', ['illusion', 'clone', 'afterimage', 'mirage', 'copies', 'phantom', 'ghost', 'invisible', 'split', 'many', 'trick']),
    ('wind', ['wind', 'gust', 'air', 'storm', 'breeze', 'sonic', 'speed', 'dash', 'fast', 'flash', 'accelerat', 'sprint']),
]
FX = [k for k, _ in KEYWORDS] + ['impact']

# Las más conocidas, a mano (por el título de la wiki inglesa).
OVERRIDES = {
    'God Hand': 'hand', 'Majin The Hand': 'hand', 'God Hand Kai': 'hand', 'Mugen The Hand': 'hand',
    'Fist of Justice': 'punch', 'Burning Catch': 'fire', 'Explosion Punch': 'punch',
    'Fire Tornado': 'fire', 'Fire Tornado DD': 'fire', 'Bakunetsu Screw': 'fire', 'Grand Fire': 'fire', 'Atomic Flare': 'fire',
    'Dragon Crash': 'dragon', 'Dragon Tornado': 'dragon', 'Twin Boost': 'impact', 'Inazuma Break': 'lightning',
    'Inazuma Drop': 'lightning', 'Inazuma 1gou': 'lightning', 'Inazuma 1gou Otoshi': 'lightning',
    'The Wall': 'wall', 'Killer Slide': 'wind', 'Spinning Cut': 'sword', 'Gravitation': 'meteor',
    'Eternal Blizzard': 'ice', 'Snow Angel': 'ice', 'Northern Impact': 'ice', 'Ice Ground': 'ice',
    'Illusion Ball': 'clone', 'Heaven Drive': 'light', 'Heaven\'s Time': 'light', 'Angel Ball': 'light',
    'Death Zone': 'dark', 'Death Zone 2': 'dark', 'Death Spear': 'dark', 'Dark Phoenix': 'bird',
    'Phoenix': 'bird', 'Fire Bird': 'bird', 'Pegasus Shot': 'bird',
    'Big Bang': 'meteor', 'Gungnir': 'sword', 'Excalibur': 'sword', 'Eagle Buster': 'bird',
    'Tsunami Boost': 'water', 'Great The Tsunami': 'water', 'X Blast': 'impact',
    'Prima Donna': 'flower', 'Rose Spear': 'flower', 'Cosmic Blaster': 'meteor', 'Space Penguin': 'bird',
    'Koutei Penguin 1gou': 'penguin', 'Koutei Penguin 2gou': 'penguin', 'Koutei Penguin 3gou': 'penguin',
    'Koutei Penguin X': 'penguin', 'Space Penguin': 'penguin',
    'The Birth': 'light', 'Unicorn Boost': 'light', 'Triangle Z': 'light', 'Rainbow Loop': 'light', 'Flash Upper': 'light',
    'Photon Flash': 'light', 'Butterfly Dream': 'flower', 'Ganymede Proton': 'meteor', 'Astro Break': 'meteor',
    'Double Grenade': 'fire', 'Grenade Shot': 'fire', 'Dynamite Shoot': 'fire', 'Dual Storm': 'fire', 'Jibashiri Kaen': 'fire',
    'Kamikakushi': 'dark', 'Wormhole': 'dark', 'Onryou': 'dark', 'Naraku Otoshi': 'dark', 'The End': 'dark',
    'Megaton Head': 'impact', 'Kangaroo Kick': 'impact', 'Southern Crosscut': 'sword', 'Echo Ball': 'wind', 'Oouchiwa': 'wind',
    'Mogura Shuffle': 'earth', 'Mogura Feint': 'earth', 'Dog Run': 'beast', 'Kagome Kagome': 'shield', 'Shoot Pocket': 'shield',
    'Jikuu no Kabe': 'wall', 'Tsumuji': 'tornado', 'Zanzou': 'clone', 'Doppelganger': 'clone',
    # revisadas con la imagen de cada técnica en la wiki
    'Gunshot': 'impact', 'Rolling Kick': 'impact', 'Twin Boost F': 'impact', 'Slingshot': 'impact', 'Chaos Break': 'fire',
    'Good Smell': 'flower', 'Sigma Zone': 'shield', 'Stinger': 'lightning', 'Gorimuchuu': 'wind', 'U-Boat': 'water',
    'Death Rain': 'dark', 'Slash Nail': 'beast', 'Eiffel Drive': 'light', 'Reppuu Dash': 'fire', 'Warp Drive': 'dark',
    'Revolution V': 'light',
}


def get(params):
    params = {**params, 'format': 'json', 'formatversion': '2'}
    req = urllib.request.Request(API + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except OSError:
            time.sleep(2 ** attempt)
    raise RuntimeError('la wiki no responde')


def fetch(titles):
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i : i + 50]
        q = get({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': '1'})['query']
        alias = {r['from']: r['to'] for r in q.get('normalized', []) + q.get('redirects', [])}
        pages = {p['title']: p for p in q['pages']}
        for t in chunk:
            final = alias.get(alias.get(t, t), alias.get(t, t))
            page = pages.get(final, {})
            out[t] = page.get('revisions', [{}])[0].get('slots', {}).get('main', {}).get('content', '')
        time.sleep(0.5)
    return out


def description(wikitext):
    """Textos de las descripciones de los juegos y la prosa del anime, sin plantillas."""
    entries = re.findall(r'\|entry(?:_dub)?=([^|}]*)', wikitext)
    anime = ''
    m = re.search(r'==\s*Anime\s*==(.*?)(?:\n==[^=]|$)', wikitext, re.S)
    if m:
        anime = re.sub(r'\{\{[^{}]*\}\}|\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', m.group(1))[:1500]
    return ' '.join(entries) + ' ' + anime


def classify(title, text):
    if title in OVERRIDES:
        return OVERRIDES[title], collections.Counter()
    name = title.lower()
    body = text.lower()
    scores = collections.Counter()
    for fx, words in KEYWORDS:
        for w in words:
            scores[fx] += 4 * len(re.findall(r'\b' + re.escape(w), name))
            scores[fx] += len(re.findall(r'\b' + re.escape(w), body))
    if not scores or max(scores.values()) == 0:
        return 'impact', scores
    best = max(scores.values())
    # empate: gana el primero de la lista (lo más concreto)
    return next(fx for fx, _ in KEYWORDS if scores[fx] == best), scores


def main():
    verbose = '--verbose' in sys.argv
    moves = json.load(open(os.path.join(ROOT, 'src', 'data', 'moves.json'), encoding='utf-8'))
    pages = fetch(sorted({m['wiki'] for m in moves if m.get('wiki')}))
    out = {}
    for m in moves:
        title = m.get('wiki', '')
        fx, scores = classify(title, description(pages.get(title, '')))
        out[m['id']] = fx
        if verbose:
            top = ', '.join(f'{k}:{v}' for k, v in scores.most_common(3) if v)
            print(f"{m['kind']:8} {fx:9} {m['name']} ({title})  [{top}]")
    with open(os.path.join(ROOT, 'tools', 'wiki', 'movefx_wiki.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    counts = collections.Counter(out.values())
    print('efectos:', ', '.join(f'{k} {v}' for k, v in counts.most_common()), file=sys.stderr)


if __name__ == '__main__':
    main()
