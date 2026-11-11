"""Equipos formados con jugadores de otros (Nuevo Inazuma Japón, Resistencia Japón, Dinastía Galáctica): cada uno
lleva el dibujo de la versión de su equipo de origen ('<equipo>:<jugador>' o '<temporada>:<jugador>'), si la tiene;
si no, el suyo de siempre (export.py lo busca por el id)."""
from chars import CHARS

# '<equipo nuevo>:<jugador>' -> equipo del que viene
FROM = {
    'cs-shinsei-inazuma-japan:aitor-cazador': 'go-shinsei-raimon',
    'cs-shinsei-inazuma-japan:arion-sherwind': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:bailong': 'cs-chrono-storm',
    'cs-shinsei-inazuma-japan:fei-rune': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:gabriel-garcia': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:goldie-lemmon': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:jean-pierre-lapin': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:njord-snio': 'go-hakuren-go',
    'cs-shinsei-inazuma-japan:riccardo-di-rigo': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:ryoma-nishiki': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:sol-daystar': 'cs-team-raimon',
    'cs-shinsei-inazuma-japan:victor-blade': 'cs-team-raimon',
    'gx-resistance-japan:aim-quintet': 'go-dragonlink',
    'gx-resistance-japan:bailong': 'go-zero',
    'gx-resistance-japan:bay-laurel': 'go-kidokawa-seishuu-go',
    'gx-resistance-japan:cronus-fourseasons': 'go-seidouzan',
    'gx-resistance-japan:davy-jones': 'go-kaiou-gakuen',
    'gx-resistance-japan:doug-mcarthur': 'go-gassan-kunimitsu',
    'gx-resistance-japan:harrold-houdini': 'go-genei-gakuen',
    'gx-resistance-japan:iggie-loo': 'go-hakuren-go',
    'gx-resistance-japan:jimmy-kyrk': 'go-tengawara',
    'gx-resistance-japan:njord-snio': 'go-hakuren-go',
    'gx-resistance-japan:quentin-cinquedea': 'go-dragonlink',
    'gx-space-rankers:apas-mulan': 'gx-supernova',
    'gx-space-rankers:arculus-orbes': 'gx-supernova',
    'gx-space-rankers:ashley-sarpala': 'gx-supernova',
    'gx-space-rankers:ashvina-bharani': 'gx-supernova',
    'gx-space-rankers:bambaros-tower': 'gx-big-bang',
    'gx-space-rankers:bhaga-guni': 'gx-supernova',
    'gx-space-rankers:bindal-hermit': 'gx-big-bang',
    'gx-space-rankers:circulus': 'gx-big-bang',
    'gx-space-rankers:fow-tudas': 'gx-big-bang',
    'gx-space-rankers:indra-vayu': 'gx-supernova',
    'gx-space-rankers:joss-fool': 'gx-big-bang',
    'gx-space-rankers:madison-barada': 'gx-big-bang',
    'gx-space-rankers:mitra-jeshu': 'gx-supernova',
    'gx-space-rankers:soma-lobi': 'gx-supernova',
    'gx-space-rankers:strem-goozer': 'gx-big-bang',
    'gx-space-rankers:zartan-walder': 'gx-big-bang',
}

for key, src in FROM.items():
    pid = key.split(':', 1)[1]
    for k in (f'{src}:{pid}', f"{src.split('-')[0]}:{pid}"):
        if k in CHARS:
            CHARS[key] = CHARS[k]
            break
