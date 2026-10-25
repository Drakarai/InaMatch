# InaMatch

Juego de navegador para PC que recrea los partidos de **Inazuma Eleven 3** (DS): duelos por comandos,
supertécnicas, FP/TP, elementos y la pantalla de formación. Gratis y sin servidor: es una web estática
que se puede publicar en GitHub Pages.

> Proyecto de fans sin ánimo de lucro. Inazuma Eleven es una marca de LEVEL-5.

## Jugar en local

Hace falta [Node.js](https://nodejs.org/) 20 o superior.

```bash
npm install
npm run dev      # abre http://localhost:5173
```

Otros comandos: `npm test` (tests de las reglas y los datos), `npm run build` (genera `dist/`) y `npm run typecheck`.

## Controles

El ratón hace de lápiz de la DS.

| Situación | Acción |
|---|---|
| Con balón | **Arrastra desde tu jugador** para dibujar el recorrido (regate) |
| | **Pulsa a un compañero** para pasarle; el bocadillo "¡Pase!" marca al mejor libre |
| | **Pulsa en el campo** para que corra hacia ahí (nunca suelta el balón) |
| | **Clic derecho** en un hueco: pase al espacio |
| | **Pulsa la portería**, el botón **Tirar** o la tecla **T** para tirar |
| Sin balón | **Arrastra a cualquier jugador** para moverlo, o **pulsa en el campo** para mandar al jugador activo (el del aro blanco) |
| Duelos y tiros | Botones en pantalla o teclas **1**/**2** (comandos básicos) y **3**, **4**… (supertécnicas) |
| | Si no eliges a tiempo se usa el primer comando |
| En cualquier momento | **Espacio** / **Esc** o el botón **II**: pausa |

Comandos básicos:
- **Atacando**: Regate o Finta.
- **Defendiendo**: Entrada o Entrada en plancha. La plancha gana al regate, pero la finta la deja en ridículo.
- **Tirando**: Tiro o Vaselina.
- **Portero**: Atrapar o Despejar.

Las supertécnicas gastan TP y suelen ganar a los comandos básicos. Además:
- **Elementos**: Fuego > Bosque > Aire > Montaña > Fuego (+20 %).
- Si el elemento de la técnica coincide con el del jugador, gana un +10 %.
- Con poca **FP** el jugador rinde menos.

## Estructura

```
src/
  data/            equipos (teams/*.json), supertécnicas (moves.json), formaciones y elementos
  engine/          reglas puras (duelos, tiros, IA de comandos) + tests
  match/           entidad jugador del partido
  scenes/          Boot, Menú, Formación, Partido y HUD (marcador, duelos, radar, animaciones)
  gfx/             gráficos provisionales generados por código
public/assets/pack carpeta para los sprites originales (ver su README)
docs/              notas de referencia del juego original
```

## Añadir equipos

Crea un `.json` en `src/data/teams/` copiando uno de los existentes y aparecerá solo en el menú.
- Los 11 primeros jugadores son los titulares, en el orden de los huecos de la formación, empezando por el portero.
- El resto va al banquillo.
- Las supertécnicas se referencian por `id` (`src/data/moves.json`).
- `npm test` avisa de técnicas inexistentes, ids repetidos o plantillas incompletas.

Las estadísticas de Inazuma National y Desert Lions salen del vídeo de referencia cuando se ven en pantalla.
El resto son estimaciones que hay que ir corrigiendo con los datos de los juegos.

## Sprites originales

El juego funciona con gráficos provisionales dibujados por código. Para usar los originales,
mete las imágenes en `public/assets/pack/` y añádelas a `manifest.json`
([instrucciones](public/assets/pack/README.md)). No hace falta tocar código.

## Publicarlo gratis (GitHub Pages)

1. En GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Cada push a `main` ejecuta `.github/workflows/deploy.yml`: pasa los tests, compila y publica en
   `https://<usuario>.github.io/<repo>/`.
