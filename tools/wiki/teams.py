"""Monta los equipos de IE1, IE2 e IE3 con datos de la wiki inglesa de Inazuma Eleven.

Por cada temporada (juego):
- Equipos: los grupos del módulo de jugadores de ese juego (Module:PlayerData/IE, IE2, IE3).
- Plantilla, dorsales y formación: la tabla de miembros de ese juego en la página de cada equipo
  (si no la hay, el grupo del módulo).
- Posición, afinidad y técnicas: Module:PlayerData (las de ese juego; si faltan, las del más cercano).
- Nombre europeo, atributos a nivel 99 y descripción: la página de cada jugador.
- Técnicas: Module:WazaData (potencia y coste de IE3, o de IE2 si no salen en IE3)
  + nombre en español de data/tecnicas.json.
- Formaciones: Module:FormationData (nombre y distribución, p. ej. 4-4-2).
- Nombre del equipo en español: enlace entre wikis.

Uso (desde la raíz del repo): python3 -I tools/wiki/teams.py
Escribe src/data/teams/*.json, src/data/moves.json y src/data/formations.json.
"""
import bisect
import glob
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lua_table import parse_module  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
API = 'https://inazuma-eleven.fandom.com/api.php'
UA = 'InaMatch-fan-project/0.1 (descarga puntual de datos de equipos)'

# temporada del juego: (id, clave del juego en la wiki, pestaña de atributos, orden de respaldo)
SEASONS = [
    ('ie1', 'IE', 'Inazuma Eleven', ['IE', 'IE2', 'IE3']),
    ('ie2', 'IE2', 'Inazuma Eleven 2', ['IE2', 'IE', 'IE3']),
    ('ie3', 'IE3', 'Inazuma Eleven 3', ['IE3', 'IE2', 'IE']),
    ('go', 'GO', 'Inazuma Eleven GO', ['GO', 'CS', 'GX', 'VR']),
    ('cs', 'CS', 'Inazuma Eleven GO 2: Chrono Stone', ['CS', 'GO', 'GX', 'VR']),
    ('gx', 'GX', 'Inazuma Eleven GO Galaxy', ['GX', 'CS', 'GO', 'VR']),
    # Ares y Orión no tienen juego: sus equipos son los de sus módulos (AT y OK) y las técnicas, las de Victory Road
    ('ares', 'AT', None, ['VR', 'AT', 'OK', 'GX', 'CS', 'GO']),
    ('orion', 'OK', None, ['VR', 'OK', 'AT', 'GX', 'CS', 'GO']),
    ('vr', 'VR', None, ['VR', 'GX', 'CS', 'GO', 'IE3', 'IE2', 'IE']),
]
GAME_TAB = {g: tab for _, g, tab, _ in SEASONS if tab}
GO_GAMES = ('GO', 'CS', 'GX', 'VR', 'AT', 'OK')
# Juego de cada ficha de Inazugle (zukan.inazuma.jp), para los atributos de Victory Road
ZUKAN_GAME = {
    'IE': 'Inazuma Eleven', 'IE2': 'Inazuma Eleven 2', 'IE3': 'Inazuma Eleven 3', 'GO': 'Inazuma Eleven GO:',
    'CS': 'Chrono Stones', 'GX': 'Galaxy', 'ares': 'Ares', 'orion': 'Orion', 'VR': 'Victory Road',
}

ELEMENT = {'Fire': 'fire', 'Wind': 'wind', 'Forest': 'wood', 'Mountain': 'earth', 'Void': 'neutral'}
KIND = {'SH': 'shoot', 'OF': 'dribble', 'DF': 'block', 'GK': 'catch'}

# Colores de cada equipo (la wiki no los tiene en datos): camiseta, pantalón, portero y acento.
# Los que no estén aquí se generan a partir del nombre.
STYLE = {
    # IE1
    'Raimon': ('#f2c230', '#2a5fc0', '#e8892b', '#d9a400'),
    # Teikoku: camiseta verde con detalles rojos (mangas del mismo verde), pantalón caqui; portero en naranja
    # Nose (Wild): camiseta verde con detalles blancos, pantalón gris oscuro; portero de granate
    'Nose': ('#3f8a54', '#2e3c44', '#8a1e66', '#e8ece4', '#3f8a54'),
    # Shuuyou Meito (Otaku): camiseta azul petróleo con mangas rosas, pantalón malva; portero de verde
    'Shuuyou Meito Gakuen': ('#1e5a78', '#b8949a', '#6a9a70', '#e4b0b4', '#e4b0b4'),
    # Sally's: camiseta mostaza con detalles verdes, pantalón verde; portero de rosa
    "Ichibangai Sally's": ('#e0a020', '#2e6a3a', '#ee7a7a', '#2e6a3a', '#e0a020'),
    # Sengoku Igajima (Instituto Shuriken): todo morado con ribetes azul grisáceo y medias grises; portero verde azulado
    # Hakuren (Instituto Alpino): camiseta crema con ribetes azul marino, pantalón azul marino y medias blancas; portero verde oliva
    'Hakuren': ('#f4f0dc', '#2e4466', '#4a5226', '#2e4466', '#f4f0dc', '#f4f0dc', '#d8d0b0', '#4a5226'),
    # Mar de Árboles: mono verde claro con franjas negras; el portero de verde oliva oscuro
    'Jukai Team': ('#a8d888', '#a8d888', '#4a5a3a', '#1e2a1e', '#a8d888', '#a8d888', '#4a5a3a', '#4a5a3a'),
    # Robots Guardias: camiseta azul petróleo con mangas rosas, pantalón azul oscuro; portero rojo
    'Keibi Machines': ('#1e5a7a', '#1a2e44', '#a83a3a', '#e8b0b0', '#e8b0b0', '#1e5a7a', '#1a2e44', '#e8b0b0'),
    'Sengoku Igajima': ('#4e3a5c', '#4e3a5c', '#6a9a96', '#9ab4bc', '#4e3a5c', '#a8a49c', '#5e8a86'),
    # Kidokawa Seishuu (Kirkwood): camiseta roja (con laterales negros), pantalón beige y medias rojas; portero verde claro
    'Kidokawa Seishuu': ('#c00c0c', '#d8c8b4', '#b8c87e', '#2a2a2e', '#c00c0c', '#c00c0c', '#4a5a68'),
    # Mikage Sennou (Brain): camiseta crema con mangas gris pardo, pantalón y medias grises; portero gris con pantalón oliva
    'Mikage Sennou': ('#e8dcc0', '#8a8076', '#9a9488', '#6a4a3a', '#8a7e74', '#a09888', '#5a5238'),
    # Zeus: todo blanco con ribetes azul petróleo y medias moradas grisáceas; portero marrón oscuro con pantalón malva
    'Zeus': ('#f2f2f2', '#f2f2f2', '#3a2c18', '#1e5a6a', '#f2f2f2', '#6a6078', '#8a7e94', '#1e2a4a'),
    # Senbayama (Farm): camiseta mostaza de cuadros con cuello crema, pantalón marrón oscuro y medias mostaza; portero azul grisáceo
    'Senbayama': ('#9a8010', '#3a2c20', '#4e6e80', '#f0e8cc', '#9a8010', '#9a8010'),
    # Kasamino (Umbrella): camiseta azul claro con mangas crema, pantalón azul y medias blancas; portero verde con mangas crema
    'Kasamino': ('#94bccc', '#2e5a80', '#5a7a34', '#2e4a6a', '#e8dcc0', '#f2f2f2', '#3a4a40', '#e8dcc0'),
    # Inazuma KFC: camiseta roja con mangas amarillas, pantalón gris pardo y medias rojas; portero azul petróleo con mangas amarillas
    'Inazuma KFC': ('#d01010', '#4e4a40', '#1e5a7a', '#f0c010', '#f0c010', '#c01010', '#3a3a3e', '#e0a020'),
    'Teikoku Gakuen': ('#36584a', '#7a6438', '#f08a2a', '#b0202a', '#36584a'),
    # Occult: camiseta morada (mangas iguales), pantalón gris, medias oscuras; portero de rojo
    'Occult': ('#4a4a7e', '#a2a2aa', '#a81c1c', '#3a3a68', '#4a4a7e', '#4a4a52'),
    # Inazuma Eleven (los veteranos): camiseta morada oscura con mangas negras y cremallera dorada, pantalón negro y medias crema;
    # portero con un abrigo morado largo
    'Inazuma Eleven': ('#382a4a', '#141218', '#2e2240', '#c8a030', '#141218', '#e0d4b8', '#2e2240', '#2e2240'),
    # IE2
    'Second Raimon': ('#f2c230', '#2a5fc0', '#e8892b', '#d9a400'),
    # Tormenta de Géminis: traje gris pardo con tirantes naranjas y un orbe azul, mangas crema; portero azul marino
    'Gemini Storm': ('#6e6460', '#4a4240', '#2a3450', '#e07020', '#e8e0d0', '#6e6460', '#2a3450', '#2a3450'),
    # Épsilon (y Épsilon Plus): traje rojo con mangas y pantalón gris oscuro, medias rojas; el portero (Dvalin / Zel) de negro
    'Epsilon': ('#b81e3a', '#3a3a44', '#28262c', '#2a8aa0', '#3a3a44', '#b81e3a', '#28262c', '#28262c'),
    'Epsilon Kai': ('#b81e3a', '#3a3a44', '#28262c', '#2a8aa0', '#3a3a44', '#b81e3a', '#28262c', '#28262c'),
    # Génesis: traje blanco con mangas y medias negras grises; portero morado
    'The Genesis': ('#f0eef0', '#f0eef0', '#5a3a9a', '#4a4a54', '#3a3a44', '#f0eef0', '#3a2a5a', '#3a3a44'),
    # Polvo de Diamantes: camiseta blanca con el pecho azul, pantalón y medias azul marino; portero negro
    'Diamond Dust': ('#f0ece4', '#1e2e5a', '#2a2a30', '#2a7ac0', '#2a7ac0', '#2a4a8a', '#2a2a30', '#2a2a30'),
    # Prominence: camiseta roja con el pecho blanco, pantalón negro y medias rojas; portero rojo oscuro
    'Prominence': ('#d82a20', '#26222a', '#7a1a1a', '#f0ece4', '#d82a20', '#d82a20', '#26222a', '#7a1a1a'),
    # Caos: camiseta roja y azul petróleo, pantalón negro y medias azul marino; portero negro
    'Chaos': ('#d02a2a', '#22202a', '#2a2a30', '#2a9aa8', '#d02a2a', '#1e2e5a', '#2a2a30', '#2a2a30'),
    # Emperadores Oscuros: mono azul marino con una V azul, medias blancas; portero gris con la V amarilla
    'Dark Emperors': ('#1e2440', '#1e2440', '#7a7a80', '#1e8ac8', '#1e2440', '#e8e4e4', '#7a7a80', '#7a7a80'),
    # Jóvenes Inazuma: camiseta negra con mangas blancas, pantalón blanco y medias negras; portero rojo oscuro con mangas negras
    'Young Inazuma': ('#1a1a1e', '#e8e4e4', '#8a1e14', '#e8e4e4', '#e8e4e4', '#1a1a1e', '#1a1a1e', '#1a1a1e'),
    'Shin Teikoku Gakuen': ('#2a2a4a', '#1a1a1a', '#c8a020', '#3a3a6a'),
    # IE3
    'Inazuma Japan': ('#2a6fd6', '#f4f4f4', '#e8892b', '#2d5fb8'),
    'Big Waves': ('#f2c230', '#1f5f3a', '#3a7bd5', '#2f8a4a'),
    'Desert Lion': ('#8e1f2f', '#f2ede4', '#3b3b48', '#a8283a'),
    'Neo Japan': ('#1b1b2f', '#e8e8e8', '#c9a227', '#3a3a6a'),
    'Fire Dragon': ('#d6342a', '#1a1a1a', '#f2c230', '#b82a22'),
    'Knights of Queen': ('#f2f2f2', '#1d2f6b', '#c8202f', '#1d2f6b'),
    'Orpheus': ('#2457b8', '#f2f2f2', '#2e2e2e', '#1d4596'),
    'Team K': ('#3a2a5a', '#1a1a1a', '#8a8a8a', '#5a3a8a'),
    'The Empire': ('#8fc6ea', '#1a1a1a', '#f2c230', '#4a8fc0'),
    'Unicorn': ('#f2f2f2', '#1d3b8a', '#c8202f', '#1d3b8a'),
    'The Kingdom': ('#f2d230', '#2a5fc0', '#2a8a3a', '#2a8a3a'),
    'Team Garshield': ('#2e2e2e', '#5a5a5a', '#8a2a2a', '#4a4a4a'),
    'Little Gigant': ('#f28a1d', '#1a1a1a', '#2a8a8a', '#d06a10'),
    'Brockenborg': ('#1a1a1a', '#f2f2f2', '#c8a020', '#3a3a3a'),
    'Red Matador': ('#c8202f', '#1d2f6b', '#f2c230', '#a01a26'),
    'Rose Griffon': ('#1d3b8a', '#f2f2f2', '#c8202f', '#2a4fa8'),
    'The Great Horn': ('#2a8a5a', '#f2f2f2', '#c87a20', '#1f6a44'),
    'Tenkuu no Shito': ('#f2f2f2', '#d8c070', '#7ab8e8', '#b8a050'),
    'Makai Gundan Z': ('#3a1a4a', '#1a1a1a', '#8a1a2a', '#5a2a6a'),
    'Ogre': ('#1a1a1a', '#8a1a1a', '#5a5a5a', '#8a1a1a'),
    'Real Inazuma': ('#f2c230', '#2a5fc0', '#e8892b', '#c89a10'),
}
SHORT = {
    'Inazuma Japan': 'INA', 'Big Waves': 'BWA', 'Desert Lion': 'DLI', 'Neo Japan': 'NEO', 'Fire Dragon': 'FDR',
    'Knights of Queen': 'KOQ', 'Orpheus': 'ORP', 'Team K': 'TMK', 'The Empire': 'EMP', 'Unicorn': 'UNI',
    'The Kingdom': 'KNG', 'Team Garshield': 'GAR', 'Little Gigant': 'LGI', 'Brockenborg': 'BRO', 'Red Matador': 'RMA',
    'Rose Griffon': 'RGR', 'The Great Horn': 'TGH', 'Tenkuu no Shito': 'TNS', 'Makai Gundan Z': 'MGZ', 'Ogre': 'OGR',
    'Real Inazuma': 'RIN', 'Raimon': 'RAI', 'Second Raimon': 'RAI', 'Teikoku Gakuen': 'TEI', 'Zeus': 'ZEU',
}
# Selecciones del Fútbol Frontier Internacional: en el campo se ve el apellido. En el resto (equipos
# japoneses y alienígenas), el nombre de pila, como Mark o Axel.
SURNAME_TEAMS = {
    'Big Waves', 'Desert Lion', 'Fire Dragon', 'Knights of Queen', 'Orpheus', 'The Empire', 'Unicorn', 'The Kingdom',
    'Little Gigant', 'Brockenborg', 'Red Matador', 'Rose Griffon', 'The Great Horn', 'Team Garshield',
}
# Equipos sin página propia en la wiki (variantes): nombre en español puesto a mano
# Nombre en España de los equipos sin enlace entre wikis, o cuyo nombre en los juegos no es el del
# título de la página de la wiki española (inazuma.fandom.com/es, campo "Nombre" de cada equipo).
NAME_ES = {
    'Dark Emperors (cloaked)': 'Emperadores Oscuros (con capa)',
    'Diamond Dust': 'Polvo de Diamantes',
    'Epsilon': 'Épsilon',
    'Epsilon Kai': 'Épsilon Plus',
    'Inazuma Eleven': 'Inazuma Eleven',
    'Kasamino': 'Instituto Umbrella',
    'Little Gigant': 'Los Pequeños Gigantes',
    'Manyuuji': 'Instituto Claustro Sagrado',
    'Osaka Gals CCC': 'Triple C de Osaka',
    'SP Fixers': 'Servicio Secreto',
    'Team Garshield': 'Zoolan Team',
    'Team K': 'Equipo D',
    'The Great Horn': 'Caimanes del Cabo',
    'The Kingdom': 'Os Reis',
    'Asia Daihyou': 'Ases Asiáticos',
    'Ura Raimon': 'Ultra Raimon',
    'NEW Genesis': 'Génesis NEW',
    'NEW Zeus': 'Zeus NEW',
    'NEW Teikoku Gakuen': 'Royal Academy NEW',
    # GO, Ares, Orion y Victory Road: nombre oficial en España según la wiki española (título de la página del equipo)
    'Eisei Gakuen': 'Academia Alia',
    'Hakuren (Ares)': 'Instituto Alpino (Ares)',
    'Inakuni Raimon': 'Raimon Isla Remota',
    'Kidokawa Seishuu (Ares)': 'Instituto Kirkwood (Ares)',
    'Midorigaoka': 'Instituto Colina Verde',
    'Mikage Sennou (Ares)': 'Instituto Brain (Ares)',
    'Minodouzan': 'Instituto Bastión',
    'Outei Tsukinomiya': 'Academia Plenilunio',

    'Seishou Gakuen': 'Academia Polaris',
    'Tonegawa Tousen': 'Instituto Ribera',
    'Destructchers': 'Desesperdidos',
    'Garu': 'Gar',
    'Giru': 'Gir',
    'Karakuri Bingmayong': 'Ejército de Terracota',
    'Perfect Cascade': 'Cascada Perfecta',
    'Shiroshika Gumi': 'Banda del Ciervo Blanco',
    'Team Raimon': 'Instituto Raimon (Chrono Stones)',
    'Tenmas': 'Los Arions',
    'The Lagoon': 'Ragnah',
    'Akizora Challengers': 'Edad Dorada',
    'Ancient Dark': 'Oscuridad Ancestral',
    'Aoba Gakuen': 'Colegio Ultramegahiedra',
    'Arakumo Gakuen': 'Instituto Universal',
    "Demon's Horn": 'Cuerno Demoníaco',
    'Dragonlink': 'Dragon Link',
    'Genei Gakuen': 'Instituto Espejismo',
    'Kuro no Kishidan': 'Orden de los Caballeros Templarios',
    'Mannouzaka': 'Colegio Poderosa Fe',
    'Seidouzan': 'Colegio Monte Olimpo',
    'Tengawara': 'Colegio Concertado Vía Láctea',
    'Faram Dite': 'Falam Medius',
    'Fire Dragon (GO)': 'Dragones de Fuego (GO)',
    'Gurdon Eleven': 'Los Magmavís',
    'Ixal Fleet': 'Flota Ixar',
    'Mach Tiger': 'Muay Tigers',
    'Ratoniik Eleven': 'Los Fertilia',
    'Sandorius Eleven': 'Los Sílice',
    'Shamshir': 'Los Cimitarras',
    'Storm Wolf': 'Storm Wolves',
    'Arab no Hi no Tori Gundan': 'Ejército del Fénix Árabe',
    'Eternal Dancers': 'Bailarines Eternos',
    'Guardians of Queen': 'Guardianes de la Reina',
    'Inazuma Japan (Orion)': 'Inazuma Japón (Orion)',
    'Muteki no Giant': 'Gigantes Invencibles',
    'Perfect Spark': 'Chispas Perfectas',
    'Red Bison': 'Bisonte Rojo',
    'Shadow of Orion': 'Eclipse de Orión',
    'Shining Satans': 'Demonios Brillantes',
    'Soccer Zatsugidan': 'Tropa Acrobática del Fútbol',
    'AI Gakuen': 'Academia IA',
    'Batten-Yokato': 'Secundaria Crosswind-Fauxshore',
    'Destroyers': 'Destructores',
    'Gatekeepers': 'Guardianas',
    'Hakuren (Victory Road)': 'Instituto Alpino (Victory Road)',
    'Houreikan': 'Instituto Lawcrest',
    'Ijinmei Bundou': 'Instituto Visión Noble',
    'Keizen Arashiyama': 'Secundaria Stormridge',
    'Meiran Gakuin': 'Academia Orchid',
    'Nagumohara Shopkeepers': 'Vendedores de South Cirrus',
    'Nikogawa': 'Instituto Twinford',
    'Ouja Raimon': 'Instituto Raimon (Victory Road)',
    'Platos': 'Plathos',
    'Rojiura Backkicks': 'Goleadores del Callejón',
    'Senjutsu no Teikoku': 'Royal Academy (Victory Road)',
    'Tenshou-Zeus': 'Secundaria Solaria-Zeus',
    'Toufuu Ikokukan': 'Secundaria Internacional Eastwind',
    'Umi Kamome Soccer Club': 'Gaviotas FC',
    'Zanark Strangers': 'Zanark Outsiders',
}
# Equipos que no se incluyen: versiones repetidas o especiales de otros equipos que no se quieren en el juego
REMOVED = {
    'Ura Zeus', 'Aliea A', 'Aliea B', 'Kami to Uchuu', 'Dark Emperors (cloaked)', 'NEW Genesis', 'Inazuma KFC Kai', 'Kageyama All Star',
    'Neo Teikoku', 'Zenkoku Team Senbatsu A', 'Zenkoku Team Senbatsu B', 'Super Shuuyou Meito', 'Super Oosaka CCC', 'NEW Zeus',
    'Chaos Angels', 'Real Aliea', 'Real Inazuma', 'Inazuma Legend', 'Joshi Senbatsu Team', 'God Angel', 'Neo Japan Kai', 'Neo Raimon',
    'Another Chaos', 'Ura Raimon', 'First Raimon', 'Raimon (Ares)', 'Auras', 'Galaxy Eleven',
}
# Equipos extra que visten como otro (versiones del mismo equipo) o con colores puestos aquí
STYLE_OF = {
    'Ura Zeus': 'Zeus', 'Neo Teikoku': 'Teikoku Gakuen', 'Kageyama All Star': 'Shin Teikoku Gakuen',
    'Aliea A': 'The Genesis', 'Aliea B': 'Chaos', 'Super Shuuyou Meito': 'Shuuyou Meito Gakuen',
    'Super Oosaka CCC': 'Osaka Gals CCC', 'Inazuma KFC Kai': 'Inazuma KFC', 'NEW Genesis': 'The Genesis',
    'NEW Zeus': 'Zeus', 'NEW Teikoku Gakuen': 'Teikoku Gakuen', 'First Raimon': 'Raimon', 'Neo Raimon': 'Raimon',
    'Ura Raimon': 'Raimon', 'Neo Japan Kai': 'Neo Japan', 'Another Chaos': 'Chaos', 'Real Aliea': 'The Genesis',
    'Inazuma Legend': 'Inazuma Eleven', 'Nippon Daihyou Kouho A': 'Inazuma Japan',
}
STYLE.update({
    'Kami to Uchuu': ('#f2f2f2', '#5a3a8a', '#c8a020', '#7a5aa8'),
    'Zenkoku Team Senbatsu A': ('#2a5fc0', '#f2f2f2', '#e8892b', '#1d4596'),
    'Zenkoku Team Senbatsu B': ('#c8202f', '#f2f2f2', '#2a8a3a', '#a01a26'),
    'Nippon Daihyou Kouho B': ('#f2f2f2', '#2a6fd6', '#e8892b', '#2d5fb8'),
    'Dark Angel': ('#1a1a1a', '#3a1a4a', '#8a1a2a', '#5a2a6a'),
    'Chaos Angels': ('#7a2a5a', '#f2f2f2', '#3a8ac0', '#8a3a6a'),
    'God Angel': ('#f2f2f2', '#c8a020', '#7ab8e8', '#b89020'),
    'Sekai Daihyou': ('#1d2f6b', '#f2f2f2', '#c8a020', '#c8a020'),
    'Asia Daihyou': ('#c8202f', '#f2f2f2', '#2a5fc0', '#a01a26'),
    'Europe Daihyou': ('#2457b8', '#f2f2f2', '#c8a020', '#1d4596'),
    'Africa Daihyou': ('#2a8a5a', '#f2c230', '#c8202f', '#1f6a44'),
    'Nanbei Daihyou': ('#f2d230', '#2a8a3a', '#2a5fc0', '#2a8a3a'),
    'Joshi Senbatsu Team': ('#e98aa8', '#f2f2f2', '#5a3a8a', '#c86a8a'),
})

MIN_PLAYERS = 11

# Equipos que no son grupos del módulo de jugadores: se montan con la tabla de miembros de su página.
EXTRA = {
    'ie1': ['Ura Zeus'],
    'ie2': [
        'Kami to Uchuu', 'Neo Teikoku', 'Kageyama All Star', 'Aliea A', 'Aliea B', 'Super Shuuyou Meito',
        'Super Oosaka CCC', 'Inazuma KFC Kai', 'Zenkoku Team Senbatsu A', 'Zenkoku Team Senbatsu B',
        'NEW Genesis', 'NEW Zeus', 'NEW Teikoku Gakuen',
    ],
    'ie3': [
        'First Raimon', 'Neo Raimon', 'Ura Raimon', 'Nippon Daihyou Kouho A', 'Nippon Daihyou Kouho B',
        'Neo Japan Kai', 'Dark Angel', 'Chaos Angels', 'God Angel', 'Inazuma Legend', 'Sekai Daihyou',
        'Asia Daihyou', 'Europe Daihyou', 'Africa Daihyou', 'Nanbei Daihyou', 'Joshi Senbatsu Team',
        'Real Aliea', 'Another Chaos',
    ],
}

# Descripciones en español puestas a mano (por página del jugador en la wiki inglesa) para los que no
# tienen la oficial en la wiki española: traducidas de la inglesa o escritas a partir de su historia.
# También nombres que la wiki no trae bien.
# Descripciones traducidas del inglés (de la wiki inglesa o de Inazugle) para los jugadores que no tienen la
# oficial en español en la wiki española, por la página del jugador en la wiki inglesa.
TRANSLATED = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'descripciones_traducidas.json'), encoding='utf-8'))
OVERRIDES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.json'), encoding='utf-8'))


ES_API = 'https://inazuma.fandom.com/es/api.php'


CACHE_DIR = os.path.join(ROOT, 'tools', 'wiki', '.cache', 'api')


def api(params, url=API):
    """Petición a la wiki. Las respuestas se guardan en tools/wiki/.cache/api: bórrala para bajarlo todo de nuevo."""
    params = {**params, 'format': 'json', 'formatversion': '2'}
    os.makedirs(CACHE_DIR, exist_ok=True)
    cached = os.path.join(CACHE_DIR, hashlib.md5((url + json.dumps(params, sort_keys=True)).encode()).hexdigest() + '.json')
    if os.path.exists(cached):
        with open(cached, encoding='utf-8') as f:
            return json.load(f)
    data = _api(params, url)
    with open(cached, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return data


def _api(params, url):
    req = urllib.request.Request(url + '?' + urllib.parse.urlencode(params), headers={'User-Agent': UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:  # reintento con espera creciente
            if attempt == 3:
                raise
            print('reintento', e, file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


def fetch_pages(titles, extra=None, url=API):
    """Wikitexto (y lo que pida `extra`) de una lista de páginas, en lotes de 50."""
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i : i + 50]
        data = api({'action': 'query', 'titles': '|'.join(chunk), 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': '1', **(extra or {})}, url)
        q = data['query']
        alias = {r['from']: r['to'] for r in q.get('normalized', []) + q.get('redirects', [])}
        by_title = {p['title']: p for p in q['pages']}
        for t in chunk:
            final = t
            for _ in range(3):
                final = alias.get(final, final)
            if final in by_title and 'missing' not in by_title[final]:
                out[t] = by_title[final]
        time.sleep(0.5)
    return out


def content(page):
    return page.get('revisions', [{}])[0].get('slots', {}).get('main', {}).get('content', '')


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def pick(h, palette):
    return palette[int(hashlib.md5(h.encode()).hexdigest(), 16) % len(palette)]


def per_game(v, order):
    """Valor de un dato que puede ir por juego ({IE2='FW', IE3='MF'}), en el orden de preferencia dado."""
    if not isinstance(v, dict):
        return v
    for g in order:
        if v.get(g) is not None:
            return v[g]
    return list(v.values())[-1] if v else None


# ------------------------------------------------------------------ módulos
print('descargando módulos...', file=sys.stderr)
ALL_GAMES = ('IE', 'IE2', 'IE3') + GO_GAMES
mods = fetch_pages([f'Module:PlayerData/{g}' for g in ALL_GAMES] + ['Module:WazaData', 'Module:FormationData'])
BY_GAME = {g: parse_module(content(mods[f'Module:PlayerData/{g}']), 'PLAYERS') for g in ALL_GAMES}
PLAYERS = {}
for g in ('IE', 'IE2', 'IE3'):
    PLAYERS.update(BY_GAME[g])
# los módulos de la era GO repiten claves (cada juego tiene su ficha del personaje): van con prefijo
for g in GO_GAMES:
    for k, v in BY_GAME[g].items():
        PLAYERS[f'{g}:{k}'] = v


def rkey(k, game):
    """Clave en PLAYERS de un jugador de la tabla de miembros (o del grupo) de un juego."""
    if game in GO_GAMES:
        for g in (game,) + GO_GAMES:
            if f'{g}:{k}' in PLAYERS:
                return f'{g}:{k}'
    if k in PLAYERS:
        return k
    return next((f'{g}:{k}' for g in GO_GAMES if f'{g}:{k}' in PLAYERS), None)


ZUKAN = {}
ZUKAN_ALL = {}
for c in json.load(open(os.path.join(ROOT, 'tools', 'zukan', 'charas.json'), encoding='utf-8')):
    if len(c['stats']) == 7:
        ZUKAN.setdefault(c['name'].lower(), []).append(c)
WAZA = parse_module(content(mods['Module:WazaData']), 'WAZAS')
FORMATION = parse_module(content(mods['Module:FormationData']), 'FORMATION')


def member_table(text, game):
    """Primera tabla de miembros del juego: [(clave, dorsal, capitán)]."""
    for head, body in re.findall(r'\{\{#invoke:MemberTable\|main([^\n]*)\n(.*?)\}\}\s*(?:\n|$)', text, re.S):
        if not re.search(r'\|game=%s\s*(?:\n|\||$)' % game, head + '\n' + body):
            continue
        fields = dict(re.findall(r'\|(\w+)=([^|\n]*)', body))
        rows = []
        n = 1
        while f'p{n}' in fields:
            no = re.match(r'\s*(\d+)', fields.get(f'no{n}', '')) if fields.get(f'no{n}') else None
            rows.append((fields[f'p{n}'].strip(), int(no.group(1)) if no else None, fields.get(f'captain{n}') == 'true'))
            n += 1
        return rows
    return []


def formation_of(text, game):
    m = re.search(r'#invoke:FormationTable\|main\s*\n\|game=%s\s*\n\|f1=(\w+)' % game, text)
    return m.group(1) if m else None


# --------------------------------------------------------- equipos por temporada
rosters = []  # (season, game, order, nombre del grupo, filas, formación, página)
for season, game, _tab, order in SEASONS:
    groups = {}
    for k, v in BY_GAME[game].items():
        groups.setdefault(v.get('__group__'), []).append(k)
    names = [g for g in groups if g and g != 'Scouts']
    pages = fetch_pages([re.sub(r'\s*\(WIP[^)]*\)', '', n).split('/')[-1] for n in names], {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})
    for gname in names:
        name = re.sub(r'\s*\(WIP[^)]*\)', '', gname).split('/')[-1]
        page = pages.get(name)
        text = content(page) if page else ''
        rows = member_table(text, 'VR' if game in ('AT', 'OK') else game)
        keys = [r[0] for r in rows]
        for k in groups[gname]:  # si la tabla está incompleta, se completa con el grupo del módulo
            if len(rows) >= 16:
                break
            if k not in keys:
                rows.append((k, None, False))
                keys.append(k)
        rows = [(rkey(k, game), no, c) for k, no, c in rows]
        rows = [r for r in rows if r[0]]
        rosters.append((season, game, order, name, rows, formation_of(text, game), page))
    print(f'{season}: {len(names)} grupos', file=sys.stderr)
    # equipos extra (versiones mejoradas, selecciones, equipos secretos): solo con la tabla de su página
    extra = fetch_pages(EXTRA.get(season, []), {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})
    for name in EXTRA.get(season, []):
        page = extra.get(name)
        text = content(page) if page else ''
        rows = [(rkey(k, game), no, c) for k, no, c in member_table(text, game)]
        rows = [r for r in rows if r[0]]
        rosters.append((season, game, order, name, rows, formation_of(text, game), page))

# Ojeadores (los jugadores que se fichan en los juegos y no son de ningún equipo): el grupo "Scouts" de cada
# módulo. Si uno sale en varios juegos, se queda la ficha del más reciente.
SCOUT_SEASON = {'IE': 'ie1', 'IE2': 'ie2', 'IE3': 'ie3', 'GO': 'go', 'CS': 'cs', 'GX': 'gx', 'VR': 'vr', 'AT': 'ares', 'OK': 'orion'}
in_teams = {PLAYERS[r[0]].get('page') for t in rosters for r in t[4]}
scout_rows = {}
for g in ALL_GAMES:
    for k, v in BY_GAME[g].items():
        if v.get('__group__') == 'Scouts' and v.get('page') and v['page'] not in in_teams:
            key = rkey(k, g)
            season = SCOUT_SEASON[g]
            scout_rows[v['page']] = (season, g, next(x[3] for x in SEASONS if x[0] == season), key)
print('ojeadores:', len(scout_rows), file=sys.stderr)

player_pages = sorted({PLAYERS[r[0]]['page'] for t in rosters for r in t[4] if PLAYERS[r[0]].get('page')} | set(scout_rows))
print('jugadores distintos:', len(player_pages), file=sys.stderr)
char_pages = fetch_pages(player_pages, {'prop': 'revisions|langlinks', 'lllang': 'es', 'lllimit': 'max'})

STAT_KEYS = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Body': 'body', 'Control': 'control', 'Guard': 'guard', 'Speed': 'speed', 'Stamina': 'stamina', 'Guts': 'guts'}
# los juegos GO tienen otros atributos: se pasan a la escala de IE3 al final (normalize_stats)
STAT_KEYS_GO = {'GP': 'fp', 'TP': 'tp', 'Kick': 'kick', 'Dribbling': 'dribbling', 'Technique': 'technique', 'Block': 'block',
                'Speed': 'speed', 'Stamina': 'stamina', 'Catch': 'catch', 'Lucky': 'lucky'}


def params_for(text, game):
    """Atributos (nivel 99) de la pestaña de ese juego en la sección ==Parameters==.
    En IE1 hay versión japonesa y europea: se usa la europea, que es la que se jugó aquí."""
    sec = re.search(r'==\s*Parameters\s*==(.*?)(?:\n==[^=]|$)', text, re.S)
    if not sec or game not in GAME_TAB:
        return None
    m = re.search(r'\|\s*%s\s*\|(.*?)(?:\n\|[^|\n]+\||\n\}\})' % re.escape(GAME_TAB[game]), sec.group(1), re.S)
    if not m:
        return None
    block = m.group(1)
    eu = re.search(r';\s*European version(.*?)(?:\n;|$)', block, re.S)
    block = (eu.group(1) if eu else block).split('----')[0]
    vals = dict(re.findall(r"\*'''(\w+)''':\s*(\d+)", block))
    keys = STAT_KEYS_GO if game in GO_GAMES else STAT_KEYS
    out = {keys[k]: int(v) for k, v in vals.items() if k in keys}
    if len(out) != len(keys):
        return None
    out['_src'] = 'go' if game in GO_GAMES else 'ie'
    return out


def zukan_for(name, games):
    """Parámetros de Victory Road de Inazugle (por el nombre del doblaje), de la ficha del juego más parecido."""
    cands = ZUKAN.get((name or '').lower())
    if not cands:
        return None
    for g in games:
        for c in cands:
            if ZUKAN_GAME.get(g, '~') in c['game']:
                return {**c['stats'], '_src': 'vr'}
    return {**cands[0]['stats'], '_src': 'vr'}


def dub_name(text, title=''):
    m = re.search(r'\|name_dub=\s*([^\n|]+)', text)
    if not m:
        return None
    name = m.group(1).replace('{{PAGENAME}}', title)
    name = re.sub(r"\{\{.*?\}\}|'''?|\[\[|\]\]|<[^>]+>", '', name).lstrip('*').strip()
    # lo que va entre paréntesis son aclaraciones ("(IE NL)"); a veces la plantilla corta el cierre
    name = re.sub(r'\s*\(.*$', '', name).strip()
    return name or None


# las páginas de la wiki española tienen las descripciones oficiales de los juegos en español
es_titles = {p: page['langlinks'][0]['title'] for p, page in char_pages.items() if page.get('langlinks')}
# muchas páginas no tienen el enlace, pero en la wiki española se llaman como en el doblaje europeo
for p, page in char_pages.items():
    if p not in es_titles and (dub := dub_name(content(page), p)):
        es_titles[p] = dub


def es_category(title, seen=None):
    """Páginas de una categoría de la wiki española y de sus subcategorías."""
    seen = seen if seen is not None else set()
    out, cont = [], {}
    while True:
        q = api({'action': 'query', 'list': 'categorymembers', 'cmtitle': title, 'cmlimit': 'max', **cont}, ES_API)
        for m in q['query']['categorymembers']:
            if m['ns'] == 14 and m['title'] not in seen:
                seen.add(m['title'])
                out += es_category(m['title'], seen)
            elif m['ns'] == 0:
                out.append(m['title'])
        if 'continue' not in q:
            return out
        cont = q['continue']


def romaji(s):
    """Nombre japonés comparable entre wikis: sin macrones ni vocales dobles, sin orden de nombre y apellido."""
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z ]', ' ', s).replace('ou', 'o').replace('uu', 'u').replace('oo', 'o').replace('ei', 'e')
    return ' '.join(sorted(s.split()))


# Fichas de personajes de la wiki española: muchas no tienen enlace desde la inglesa ni se llaman como en el
# doblaje inglés. Se emparejan por su enlace a la wiki inglesa y por el nombre japonés de la ficha.
es_char_titles = sorted(set(es_category('Categoría:Personajes')))
es_char_pages = fetch_pages(es_char_titles, {'prop': 'revisions|langlinks', 'lllang': 'en', 'lllimit': 'max'}, url=ES_API)
by_en_link, by_romaji = {}, {}
for t, pg in es_char_pages.items():
    for ll in pg.get('langlinks', []):
        by_en_link.setdefault(ll['title'], pg['title'])
    jp = re.search(r'\|\s*Nombre JP\s*=([^\n]*)', content(pg))
    if jp:
        for r in re.findall(r'R\s*=\s*([^|}]+)', jp.group(1)) + re.split(r'<br\s*/?>', re.sub(r'\{\{.*?\}\}', '', jp.group(1))):
            if r.strip():
                by_romaji.setdefault(romaji(r), pg['title'])
es_pages = fetch_pages(sorted(set(es_titles.values())), url=ES_API)
es_pages.update({pg['title']: pg for pg in es_char_pages.values()})
found = 0
for p in char_pages:
    if content(es_pages.get(es_titles.get(p, ''), {})):
        continue
    t = by_en_link.get(p) or by_romaji.get(romaji(p))
    if t and t in es_pages:
        es_titles[p] = t
        found += 1
print('fichas de la wiki española:', len(es_char_pages), '| emparejadas por enlace o nombre japonés:', found, file=sys.stderr)
print('jugadores con página en la wiki española:', sum(1 for t in es_titles.values() if content(es_pages.get(t, {}))), file=sys.stderr)

# Los que siguen sin página: en el juego español algunos se llaman distinto (Umi Hwang es Umi Wang; los de
# Los Rojos tienen nombres españoles). Se buscan en la tabla de miembros de su equipo en la wiki española:
# por una parte del nombre en común o, si no, por dorsal y posición.
ES_POS = {'GK': 'PR', 'DF': 'DF', 'MF': 'MD', 'FW': 'DL'}


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return re.sub(r'[^a-z0-9 ]', ' ', ''.join(c for c in s if not unicodedata.combining(c)))


def es_members(text):
    """[(dorsal, página, posición, dorsal dudoso)] de las tablas de miembros de un equipo en la wiki española."""
    out = []
    for body in re.findall(r'\{\{Tabla \(Miembros\)\s*\n(.*?)\n\}\}', text, re.S):
        dor = re.search(r'\|\s*Dor\s*=\s*([^\n]*)', body)
        nom = re.search(r'\|\s*Nom\s*=\s*\[\[([^\]|]+)', body)
        pos = re.search(r'\{\{M\|P\|(\w+)', body)
        n = re.match(r'\s*(\d+)', dor.group(1)) if dor else None
        if n and nom:
            out.append((int(n.group(1)), nom.group(1).strip(), pos.group(1) if pos else '', '/' in dor.group(1)))
    return out


team_es = {}
for _s, _g, _o, name, _rows, _f, page in rosters:
    ll = (page or {}).get('langlinks', [])
    team_es[name] = ll[0]['title'] if ll else NAME_ES.get(name)
es_team_pages = fetch_pages(sorted({t for t in team_es.values() if t}), url=ES_API)
es_by_player = {}  # (equipo, clave del jugador) -> página en la wiki española
for _s, _g, order, name, rows, _f, _p in rosters:
    members = es_members(content(es_team_pages.get(team_es.get(name) or '', {})))
    for i, (key, no, _c) in enumerate(rows):
        pg = PLAYERS[key].get('page', '')
        if content(es_pages.get(es_titles.get(pg, ''), {})):
            continue
        no = no or i + 1  # el mismo dorsal que se le pone en build_player
        en_names = [pg, dub_name(content(char_pages.get(pg, {})), pg) or '']
        tokens = {w for n in en_names for w in norm(n).split() if len(w) >= 3}
        by_name = {m[1] for m in members if tokens & set(norm(m[1]).split())}
        pos = ES_POS.get(per_game(PLAYERS[key].get('position'), order))
        same_no = [m for m in members if m[0] == no]
        by_no = {m[1] for m in same_no if m[2] == pos and not m[3]} if len(same_no) == 1 else set()
        # si el nombre y el dorsal no coinciden, manda el dorsal (un apellido en común puede ser casualidad)
        match = by_name if len(by_name) == 1 and (not by_no or by_no == by_name) else by_no
        if len(match) == 1:
            es_by_player[(name, key)] = match.pop()
# el mismo jugador en otro equipo (selecciones, versiones mejoradas) usa la página encontrada
by_key = {key: title for (_n, key), title in es_by_player.items()}
for _s, _g, _o, name, rows, _f, _p in rosters:
    for key, _no, _c in rows:
        if (name, key) not in es_by_player and key in by_key:
            es_by_player[(name, key)] = by_key[key]
es_pages.update(fetch_pages(sorted(set(es_by_player.values()) - set(es_pages)), url=ES_API))
print('encontrados en las tablas de equipo de la wiki española:', len(es_by_player), file=sys.stderr)


ES_DESC = {'IE': ('IE', 'Descripción IE'), 'IE2': ('IE 2', 'Descripción IE2'), 'IE3': ('IE 3', 'Descripción IE3'),
           'GO': ('IE GO', 'Descripción IEGO'), 'CS': ('IE GO 2', 'Descripción IEGO2'), 'GX': ('IE GO 3', 'Descripción IEGO3'),
           'VR': ('IE HVR', 'Descripción IEHVR'), 'AT': ('IE HVR', 'Descripción IEHVR'), 'OK': ('IE HVR', 'Descripción IEHVR')}


def clean_wiki(t):
    t = re.sub(r'<nowiki>\s*</nowiki>|<[^>]+>', ' ', t)
    t = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', t)
    t = re.sub(r'\{\{[^{}]*\}\}', '', t)
    return re.sub(r"'''?|\s+", ' ', t).strip()


GAME_NO = {'IE': ('IE', 1), 'IE2': ('IE', 2), 'IE3': ('IE', 3), 'GO': ('GO', 1), 'CS': ('GO', 2), 'GX': ('GO', 3), 'VR': ('HVR', 1), 'AT': ('HVR', 1), 'OK': ('HVR', 1)}
END = r'(?=\n\s*\||\}\}\s*(?:\n|$))'  # fin de un parámetro: el siguiente o el cierre de la plantilla


def es_text_of(body):
    """Texto de una descripción. Si trae la traducción literal del japonés y la del juego español
    (líneas *{{JP}}: ... y *{{ES}}: ...), la española; si trae varias (antes/después...), la primera."""
    bullets = re.findall(r"\*\s*(?:'''([^']*)'''\s*:\s*)?([^\n*]+)", body)
    if bullets:
        es = [b for label, b in bullets if '{{ES}}' in (label or '')]
        jp = [b for label, b in bullets if '{{JP}}' in (label or '')]
        body = es[0] if es else None if jp else bullets[0][1]
    elif body and '----' in body:  # variantes sin viñetas ('''Normal''': ... ---- '''Otra''': ...)
        body = re.sub(r"^\s*'''[^']*'''\s*:?", '', body.split('----')[0].strip())
    return clean_wiki(body) if body else None


def param_values(text, param):
    """Valores de "|<param> = ..." en las plantillas, contando llaves: el valor acaba en el siguiente parámetro
    de la misma plantilla o en su cierre, aunque dentro haya otras plantillas ({{Aviso...}}, {{ES}}...)."""
    out = []
    for m in re.finditer(r'\|\s*%s\s*=' % re.escape(param), text):
        i, depth = m.end(), 0
        while i < len(text):
            if text.startswith('{{', i):
                depth += 1
                i += 2
                continue
            if text.startswith('}}', i):
                if depth == 0:
                    break
                depth -= 1
                i += 2
                continue
            if depth == 0 and text[i] == '\n' and re.match(r'\n\s*\|', text[i:]):
                break
            i += 1
        out.append(text[m.end():i])
    return out


def description_es(text, game):
    """Descripción oficial en español del juego, de las plantillas de la sección de descripción:
    - el parámetro "Descripción IE3 = ..." (o IE2, o IE) de {{Descripción/IE 3 | ...}} o {{Descripción | ...}};
    - {{Descripción/IE | Descripción = ...}} (IE1);
    - {{Descripción/Varios | IE = {{IE|J|IE 2-3}} | Descripción = ...}}, la misma para varios juegos."""
    _tpl, param = ES_DESC[game]
    bodies = param_values(text, param)
    if game == 'IE':
        bodies += re.findall(r'\{\{Descripci[oó]n/IE\s*\|(?:[^{}]|\{\{[^{}]*\}\})*?\|\s*Descripci[oó]n\s*=(.*?)%s' % END, text, re.S)
    for m in re.finditer(r'\{\{Descripci[oó]n/Varios\s*\|\s*IE\s*=\s*\{\{IE\|[^|}]*\|([^}]*)\}\}\s*\|\s*Descripci[oó]n\s*=(.*?)%s' % END, text, re.S):
        label = m.group(1).strip()
        series = 'GO' if ' GO' in label else 'HVR' if 'HVR' in label else 'IE'
        r = re.search(r'(\d)(?:-(\d))?$', label)
        games = range(int(r.group(1)), int(r.group(2) or r.group(1)) + 1) if r else range(1, 4) if 'Mark' in label or series == 'HVR' else ()
        if GAME_NO[game][0] == series and GAME_NO[game][1] in games:
            bodies.append(m.group(2))
    for body in bodies:
        if 'Aviso' in body:
            # Galaxy no salió en España: la wiki pone su propia traducción, después del aviso
            if game != 'GX' or '----' not in body:
                continue
            body = body.split('----', 1)[1]
        if out := es_text_of(body):
            return out
    return None


def description_es_any(text):
    """Último recurso: cualquier descripción oficial en español de la ficha ({{Descripción | Descripción = ...}})."""
    for body in param_values(text, 'Descripción'):
        if 'Aviso' not in body and (out := es_text_of(body)):
            return out
    return None


def description(text, game):
    m = re.search(r'\{\{Profile/Entry\|g1=%s(?:\|[^}]*?)?\|entry_dub=([^}|]*)' % game, text)
    return re.sub(r"<br\s*/?>|'''?|\[\[|\]\]", ' ', m.group(1)).strip() if m else None


CATALOG = {m['en']: m for m in json.load(open(os.path.join(ROOT, 'data', 'tecnicas.json'), encoding='utf-8'))}
moves_used = {}


def gv(field, game):
    """Valor numérico de un dato de WazaData en un juego (los de solo Victory Road vienen sin juego)."""
    v = field.get(game) if isinstance(field, dict) else field if game == 'VR' else None
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


QMAP = {}


def to_ie_scale(field, w):
    """Potencia o coste en la escala de IE3. Las técnicas de la era GO no tienen dato de IE3: se pasa su valor
    del juego más cercano por percentiles (la misma posición entre las técnicas de su tipo en ese juego que
    entre las de IE3)."""
    ie_games = ('IE3', 'IE2') if field == 'power' else ('IE3', 'IE2', 'IEEU', 'IE')
    v = next((x for g in ie_games if (x := gv(w.get(field), g)) is not None), None)
    if v is not None:
        return v
    for g in ('GX', 'CS', 'GO', 'VR'):
        v = gv(w.get(field), g)
        if v is None:
            continue
        key = (field, g, w['wType'])
        if key not in QMAP:
            same = [x for x in WAZA.values() if x.get('wType') == w['wType']]
            src = sorted(x for o in same if (x := gv(o.get(field), g)) is not None)
            dst = sorted(x for o in same if (x := next((y for gg in ie_games if (y := gv(o.get(field), gg)) is not None), None)) is not None)
            QMAP[key] = (src, dst)
        src, dst = QMAP[key]
        if not src or not dst:
            return None
        frac = (bisect.bisect_left(src, v) + bisect.bisect_right(src, v)) / 2 / len(src)
        return dst[min(len(dst) - 1, int(frac * len(dst)))]
    return None


def move_from_key(key):
    """Técnica de WazaData. Potencia y coste de IE3 (o de IE2): los de IE1 van en otra escala.
    Las de la era GO y Victory Road, pasadas a la escala de IE3 (to_ie_scale)."""
    w = WAZA.get(key)
    if not w or w.get('wType') not in KIND or w.get('__group__') == 'Real Skills':
        return None
    power = to_ie_scale('power', w)
    cost = to_ie_scale('cost', w)
    element = per_game(w.get('element'), ['IE3', 'IE2', 'IE', 'GO', 'CS', 'GX', 'VR'])
    if power is None or cost is None or element not in ELEMENT:
        return None
    cat = CATALOG.get(w['page'], {})
    mid = slug(w['page'])
    # versiones de una misma técnica con otra afinidad (Mano mágica de Montaña / de Bosque)
    if mid in moves_used and moves_used[mid]['element'] != ELEMENT[element]:
        mid = f'{mid}-{ELEMENT[element]}'
    moves_used[mid] = {
        'id': mid,
        'name': OVERRIDES['moves'].get(w['page']) or cat.get('es') or cat.get('dub') or w['page'],
        'kind': KIND[w['wType']],
        'element': ELEMENT[element],
        'power': int(power),
        'tp': int(cost),
        'wiki': w['page'],
    }
    if w.get('chr') == 'L':  # tiro largo: se puede usar desde cualquier distancia
        moves_used[mid]['long'] = True
    # bloqueo de tiros: las técnicas defensivas de bloqueo (B) y los tiros que sirven para cortar o devolver un tiro
    # rival (B en IE2/GO, CN "Counter" en Victory Road). Sin una de estas, solo el portero puede parar un tiro.
    chr_all = set(w['chr'].values()) if isinstance(w.get('chr'), dict) else {w.get('chr')}
    if (KIND[w['wType']] == 'block' and 'B' in chr_all) or (KIND[w['wType']] == 'shoot' and chr_all & {'B', 'CN'}):
        moves_used[mid]['shotBlock'] = True
    return mid


HAIR = ['#3a2a1a', '#6b3e1f', '#8b5a2b', '#c0302a', '#efe6c4', '#4c8a3c', '#3a6fb5', '#c9ccd6', '#1d1410', '#e98aa8', '#5a3a7a', '#d9822b']
SKIN = ['#f1c79b', '#f1c79b', '#e8b888', '#c08a5e', '#b5835a', '#9a6a44']
SHIRTS = ['#c8202f', '#2a5fc0', '#2a8a3a', '#f2c230', '#5a3a8a', '#e86a1a', '#1a1a1a', '#f2f2f2', '#3a8ac0', '#8a1a3a', '#4a6a2a', '#c87aa8']
missing_stats = []
es_matches = []  # jugadores emparejados por la tabla de su equipo (para revisarlos)
no_spanish = []  # jugadores sin descripción en español: hay que añadirla a overrides.json


def build_player(key, number, team_name, season, order, used_ids):
    d = PLAYERS[key]
    page = char_pages.get(d.get('page', ''))
    text = content(page) if page else ''
    name = OVERRIDES['names'].get(d.get('page', '')) or dub_name(text, d.get('page', '')) or d.get('page') or key
    pid = slug(name)
    if pid in used_ids:  # mismo jugador en otra forma dentro del equipo
        pid = slug(f'{name} {key}')
    used_ids.add(pid)
    element = per_game(d.get('element'), order)
    position = per_game(d.get('position'), order) or 'MF'
    if position not in ('GK', 'DF', 'MF', 'FW'):
        position = 'MF'
    stats = next((s for g in order if (s := params_for(text, g))), None)
    if not stats or stats['_src'] != 'ie':
        # era GO: los atributos de su juego o, si no, los de Victory Road de Inazugle; se pasan a la escala de
        # IE3 cuando están todos los jugadores (normalize_stats)
        raw = stats or zukan_for(name, [season] + order)
        stats = None
    else:
        raw = None
    if not stats and not raw:
        missing_stats.append(f'{season} {team_name}: {name}')
        base = {'GK': (45, 60, 40, 80, 45), 'DF': (50, 70, 50, 70, 55), 'MF': (60, 55, 65, 50, 65), 'FW': (75, 55, 60, 40, 65)}[position]
        stats = {'fp': 120, 'tp': 120, 'kick': base[0], 'body': base[1], 'control': base[2], 'guard': base[3], 'speed': base[4], 'stamina': 60, 'guts': 60}
    movesets = d.get('moveset', {})
    mgame = next((g for g in order if movesets.get(g)), None)
    moveset = movesets.get(mgame, []) if mgame else []
    moves = []
    for entry in moveset:
        if isinstance(entry, dict):  # {"X", 30, a=true}: las alternativas (a) no son las suyas
            if entry.get('a'):
                continue
            entry = entry.get('__list__', [])
        mk = entry[0] if isinstance(entry, list) and entry else None
        mid = move_from_key(mk) if isinstance(mk, str) else None
        if mid and mid not in moves:
            moves.append(mid)
    if mgame == 'VR' and len(moves) > 4:  # en Victory Road aprenden seis: las cuatro últimas son las suyas
        moves = moves[-4:]
    parts = name.split()
    player = {
        'id': pid,
        'name': name,
        'short': parts[-1] if team_name in SURNAME_TEAMS else parts[0],
        'number': number,
        'position': position,
        'element': ELEMENT.get(element, 'neutral'),
        'level': 99,
        'fp': stats['fp'] if stats else 0,
        'tp': stats['tp'] if stats else 0,
        'stats': {k: stats[k] for k in ['kick', 'body', 'control', 'guard', 'speed', 'stamina', 'guts']} if stats else {},
        'moves': moves,
        'look': {'hair': pick(name, HAIR), 'skin': pick(name[::-1], SKIN)},
        'wiki': d.get('page') or key,
    }
    if raw:
        player['_raw'] = raw
    es_text = content(es_pages.get(es_titles.get(d.get('page', ''), ''), {}))
    if not es_text and (team_name, key) in es_by_player:
        es_text = content(es_pages.get(es_by_player[(team_name, key)], {}))
        es_matches.append(f"{team_name} | {name} -> {es_by_player[(team_name, key)]} | {next((x for g in order if (x := description_es(es_text, g))), '')} | {next((x for g in order if (x := description(text, g))), '')}")
    desc = OVERRIDES['descriptions'].get(d.get('page', ''))
    desc = desc or next((x for g in order if (x := description_es(es_text, g))), None) or description_es_any(es_text)
    # sin versión oficial en español: la traducción de la inglesa (tools/wiki/descripciones_traducidas.json)
    desc = desc or TRANSLATED.get(d.get('page', ''))
    if not desc:
        english = next((x for g in order if (x := description(text, g))), None)
        if not english and (z := ZUKAN.get(name.lower())):
            english = z[0]['desc']
        no_spanish.append(f"{d.get('page') or key} | {name} | {team_name} | {english or ''}")
    if desc:
        desc = desc.replace('\ufeff', '').strip()
        for wrong, right in OVERRIDES['fixes']:
            desc = desc.replace(wrong, right)
        if desc[-1].isalnum():
            desc += '.'
        player['description'] = desc
    return player


# --------------------------------------------------------------- formaciones
formations = {}


def formation_id(fkey, game, players):
    f = FORMATION.get(fkey) if fkey else None
    layout = per_game(f.get('layout'), [game, 'IE3', 'IE2', 'IE']) if f else None
    valid = isinstance(layout, str) and re.fullmatch(r'\d-\d-\d', layout) and sum(map(int, layout.split('-'))) == 10
    if not valid:
        # sin datos: la distribución de los titulares por posición
        c = {p: sum(1 for x in players[1:11] if x['position'] == p) for p in ('DF', 'MF', 'FW')}
        layout = f"{c['DF']}-{c['MF']}-{c['FW']}"
        if sum(c.values()) != 10:
            layout = '4-4-2'
        name = f'F-{layout}'
    else:
        name = f.get('page') or fkey
    fid = slug(name)
    formations[fid] = {'id': fid, 'name': name, 'layout': layout}
    return fid, [int(x) for x in layout.split('-')]


FIT = {
    'DF': lambda s: s['guard'] + s['body'],
    'MF': lambda s: s['control'] + s['speed'] + s['kick'] / 2,
    'FW': lambda s: s['kick'] * 1.5 + s['control'] / 2,
}


def pick_starters(players, counts):
    """Portero + DF/MF/FW según la distribución, por orden de dorsal; el resto al banquillo.
    Si faltan jugadores de una posición, entra el que mejor encaje por atributos."""
    pool = list(players)
    gk = next((p for p in pool if p['position'] == 'GK'), pool[0])
    pool.remove(gk)
    lines = {}
    for pos, n in zip(('DF', 'MF', 'FW'), counts):
        chosen = [p for p in pool if p['position'] == pos][:n]
        for p in chosen:
            pool.remove(p)
        lines[pos] = (chosen, n)
    for pos, (chosen, n) in lines.items():
        while len(chosen) < n and pool:
            outfield = [p for p in pool if p['position'] != 'GK'] or pool
            filler = max(outfield, key=lambda p: FIT[pos](p['stats']))
            pool.remove(filler)
            chosen.append(filler)
    return [gk] + lines['DF'][0] + lines['MF'][0] + lines['FW'][0] + pool


def unique_shorts(players):
    """Si dos jugadores comparten nombre corto, se usa la otra parte de su nombre."""
    seen = {}
    for p in players:
        seen.setdefault(p['short'], []).append(p)
    for group in seen.values():
        if len(group) > 1:
            for p in group:
                parts = p['name'].split()
                p['short'] = parts[0] if p['short'] != parts[0] else parts[-1]


def team_short(name, taken):
    if name in SHORT and SHORT[name] not in taken:
        return SHORT[name]
    words = [w for w in re.split(r'\W+', name) if w and w.lower() not in ('the', 'of', 'no')]
    cands = [''.join(w[0] for w in words)[:3].upper() if len(words) >= 3 else '', re.sub(r'\W', '', name)[:3].upper()]
    cands += [(words[0][:2] + words[-1][0]).upper() if len(words) > 1 else '', (words[0][0] + words[0][2:4]).upper()]
    for c in cands:
        if len(c) == 3 and c not in taken:
            return c
    return name[:2].upper() + str(len(taken))


# ------------------------------------------------------------- atributos
STAT_NAMES = ['kick', 'body', 'control', 'guard', 'speed', 'stamina', 'guts']
MAP_RAW = {
    # era GO: Tiro, Regate, Técnica, Bloqueo, Velocidad, Aguante, Parada y Suerte
    'go': lambda r, pos: {'kick': r['kick'], 'control': r['dribbling'], 'guard': r['catch'] if pos == 'GK' else r['block'],
                          'body': r['technique'], 'speed': r['speed'], 'stamina': r['stamina'], 'guts': r['lucky'],
                          'fp': r['fp'], 'tp': r['tp']},
    # Victory Road (Inazugle): Tiro, Control, Técnica, Presión, Físico, Agilidad, Inteligencia
    'vr': lambda r, pos: {'kick': r['kick'], 'control': r['control'], 'guard': r['pressure'], 'body': r['physical'],
                          'speed': r['agility'], 'stamina': (r['physical'] + r['intelligence']) / 2, 'guts': r['technique'],
                          'fp': r['physical'] + r['intelligence'], 'tp': r['technique'] + r['intelligence']},
}


def normalize_stats(players):
    """Pasa los atributos de la era GO y de Victory Road a la escala de IE3: cada valor queda a la misma
    distancia de la media (en desviaciones) entre los de su juego y su posición que entre los jugadores de IE."""
    def spread(vals):
        m = sum(vals) / len(vals)
        sd = (sum((v - m) ** 2 for v in vals) / len(vals)) ** 0.5 or 1
        return m, sd
    target = {}
    for pos in ('GK', 'DF', 'MF', 'FW'):
        ie = [p for p in players if '_raw' not in p and p['position'] == pos and p['stats']]
        for k in STAT_NAMES:
            target[(pos, k)] = spread([p['stats'][k] for p in ie])
        for k in ('fp', 'tp'):
            target[(pos, k)] = spread([p[k] for p in ie])
    for src, fn in MAP_RAW.items():
        for pos in ('GK', 'DF', 'MF', 'FW'):
            group = [p for p in players if p.get('_raw', {}).get('_src') == src and p['position'] == pos]
            if not group:
                continue
            mapped = [fn(p['_raw'], pos) for p in group]
            for k in STAT_NAMES + ['fp', 'tp']:
                m, sd = spread([x[k] for x in mapped])
                tm, tsd = target[(pos, k)]
                for p, x in zip(group, mapped):
                    v = round(tm + (x[k] - m) / sd * tsd)
                    if k in ('fp', 'tp'):
                        p[k] = max(60, min(250, v))
                    else:
                        p['stats'][k] = max(15, min(99, v))
    for p in players:
        p.pop('_raw', None)


# ------------------------------------------------------------------ salida
teams_dir = os.path.join(ROOT, 'src', 'data', 'teams')
for f in glob.glob(os.path.join(teams_dir, '*.json')):
    os.remove(f)
written = {s[0]: [] for s in SEASONS}
shorts = {s[0]: set() for s in SEASONS}
skipped = []
built = []
raw_teams = []
for season, game, order, name, rows, fkey, page in rosters:
    if name in REMOVED:
        continue
    used = set()
    rows = rows[:18]
    players = [build_player(key, no or i + 1, name, season, order, used) for i, (key, no, _c) in enumerate(rows)]
    if len(players) < MIN_PLAYERS or not any(p['position'] == 'GK' for p in players):
        skipped.append(f'{season} {name} ({len(players)} jugadores)')
        continue
    raw_teams.append((season, game, name, fkey, page, players))

# ojeadores: un "equipo" por temporada (scouts-ie1...), sin formación
scouts = {}
for page_title, (season, game, order, key) in sorted(scout_rows.items()):
    p = build_player(key, 0, 'Scouts', season, order, set())
    if p['position'] and (p['stats'] or p.get('_raw')):
        scouts.setdefault(season, []).append(p)
for season, ps in scouts.items():
    seen = set()
    for p in ps:  # ids únicos dentro de cada temporada
        while p['id'] in seen:
            p['id'] += '-b'
        seen.add(p['id'])

normalize_stats([p for t in raw_teams for p in t[5]] + [p for ps in scouts.values() for p in ps])

for season, game, name, fkey, page, players in raw_teams:
    players.sort(key=lambda p: p['number'])
    fid, counts = formation_id(fkey, game, players)
    players = pick_starters(players, counts)
    unique_shorts(players)
    es = (page or {}).get('langlinks', [])
    look_as = STYLE_OF.get(name, name)
    style = STYLE.get(look_as) or (
        pick(look_as, SHIRTS),
        pick(look_as + 's', ['#f2f2f2', '#1a1a1a', '#2a3a5a']),
        pick(look_as + 'g', ['#e8892b', '#3a8a3a', '#5a5a5a']),
        pick(look_as, SHIRTS),
    )
    short = team_short(name, shorts[season])
    shorts[season].add(short)
    tid = f'{season}-{slug(name)}'
    if any(t['id'] == tid for t in built):
        continue
    built.append({
        'id': tid,
        'season': season,
        'wiki': name,
        'name': NAME_ES.get(name) or (es[0]['title'] if es else name),
        'short': short,
        'colors': {'shirt': style[0], 'shorts': style[1], 'gkShirt': style[2], 'accent': style[3], **({'sleeve': style[4]} if len(style) > 4 else {}), **({'socks': style[5]} if len(style) > 5 else {}), **({'gkShorts': style[6]} if len(style) > 6 else {}), **({'gkSleeve': style[7]} if len(style) > 7 else {})},
        'formation': fid,
        'players': players,
    })

for team in built:
    with open(os.path.join(teams_dir, team['id'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(team, f, ensure_ascii=False, indent=1)
        f.write('\n')
    written[team['season']].append(team['name'])
with open(os.path.join(ROOT, 'src', 'data', 'scouts.json'), 'w', encoding='utf-8') as f:
    f.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v, ensure_ascii=False, separators=(",", ":"))}' for k, v in scouts.items()) + '\n}\n')
print('ojeadores por temporada:', {k: len(v) for k, v in scouts.items()})

# todas las supertécnicas de la wiki, también las que no lleva ningún jugador: son los cuadernos del gacha de Mi club
used_by_players = set(moves_used)
for key in sorted(WAZA):
    move_from_key(key)
print('técnicas que no lleva nadie (solo en cuadernos):', len(set(moves_used) - used_by_players))

with open(os.path.join(ROOT, 'src', 'data', 'moves.json'), 'w', encoding='utf-8') as f:
    kinds = ['shoot', 'dribble', 'block', 'catch']
    moves = sorted(moves_used.values(), key=lambda m: (kinds.index(m['kind']), -m['power'], m['name']))
    f.write('[\n' + ',\n'.join('  ' + json.dumps(m, ensure_ascii=False) for m in moves) + '\n]\n')
with open(os.path.join(ROOT, 'src', 'data', 'formations.json'), 'w', encoding='utf-8') as f:
    json.dump(sorted(formations.values(), key=lambda x: x['name']), f, ensure_ascii=False, indent=1)
    f.write('\n')

for s, names in written.items():
    print(f'{s}: {len(names)} equipos -> {", ".join(names)}')
print('omitidos:', skipped)
print('técnicas:', len(moves_used), '| sin nombre en español:', sum(1 for m in moves_used.values() if not CATALOG.get(m['wiki'], {}).get('es') and m['wiki'] not in OVERRIDES['moves']))
print('formaciones:', len(formations))
print('jugadores sin atributos en la wiki (estimados por posición):', len(missing_stats))
for m in missing_stats[:30]:
    print('  ', m)
no_spanish = sorted(set(no_spanish))
print('jugadores sin descripción en español (añádela en tools/wiki/overrides.json):', len(no_spanish))
os.makedirs(os.path.join(ROOT, 'tools', 'wiki', '.cache'), exist_ok=True)
with open(os.path.join(ROOT, 'tools', 'wiki', '.cache', 'sin_descripcion.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(no_spanish) + '\n')
with open(os.path.join(ROOT, 'tools', 'wiki', '.cache', 'emparejados_es.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(set(es_matches))) + '\n')
