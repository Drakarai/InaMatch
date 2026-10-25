"""Regenera src/assets/pack/README.md con los nombres de archivo de todos los jugadores y escudos.

Uso (desde la raíz del repo): python3 -I tools/pack_readme.py
"""
import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'src', 'data', 'teams', '*.json'))):
    t = json.load(open(f, encoding='utf-8'))
    rows.append(f"\n### {t['name']}\n\nEscudo: `emblems/{t['id']}.png`\n\n| Jugador | Archivo |\n|---|---|")
    for p in sorted(t['players'], key=lambda p: p['number']):
        rows.append(f"| {p['number']} · {p['name']} ({p['position']}) | `{p['id']}.png` |")

doc = f"""# Sprites originales

Deja aquí las imágenes **con el nombre exacto de la lista de abajo** y el juego las usará en lugar
de los dibujos provisionales. No hay que tocar código ni ningún archivo de configuración.

```
src/assets/pack/
  sprites/     muñeco en el campo        → sprites/mark-evans.png
  portraits/   retrato (ficha y duelos)  → portraits/mark-evans.png
  emblems/     escudo del equipo         → emblems/inazuma-japan.png
```

- Formatos: `.png` (recomendado), `.webp`, `.gif` o `.jpg`.
- **Sprite de campo**: un solo fotograma del jugador de frente, parado, con fondo transparente.
  Se escala a 46 px de alto con escalado nítido, así que vale el tamaño original de la DS.
- **Retrato**: cuadrado, con o sin fondo.
- **Escudo**: cuadrado con fondo transparente.
- Lo que no pongas se sigue dibujando con el gráfico provisional; puedes ir poco a poco.
- Un jugador que está en varios equipos usa el mismo archivo en todos.

Esta lista se regenera con `python3 -I tools/pack_readme.py`.

## Nombres de archivo
{chr(10).join(rows)}
"""
open(os.path.join(ROOT, 'src', 'assets', 'pack', 'README.md'), 'w', encoding='utf-8').write(doc)
print('equipos:', sum(1 for r in rows if r.startswith('\n###')))
