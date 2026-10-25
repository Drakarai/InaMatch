# InaMatch

Juego de navegador para PC que recrea los partidos de **Inazuma Eleven 3** (DS): duelos por comandos,
supertécnicas, FP/TP, elementos y la pantalla de formación. Gratis y sin servidor: es una web estática
que se puede publicar gratis en Cloudflare Pages (ver abajo).

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
| Con balón | **Arrastra desde tu jugador** para dibujar el recorrido: lo va siguiendo mientras dibujas |
| | **Pulsa a un compañero** para pasarle; el bocadillo "¡Pase!" marca al mejor libre |
| | **Pulsa en un hueco** para un pase al espacio |
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
  assets/pack/     sprites originales: se usan con solo ponerles el nombre del jugador
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
mete las imágenes en `src/assets/pack/` con el nombre del jugador (`sprites/axel-blaze.png`…).
[Instrucciones y lista de nombres](src/assets/pack/README.md). Se incluyen también en `npm run build:single`.

## Publicarlo gratis (Cloudflare Pages, con el repo privado)

Se hace una sola vez desde la web, sin terminal:

1. Crea una cuenta gratuita en [dash.cloudflare.com](https://dash.cloudflare.com).
2. Ve a **Workers & Pages → Create application → Pages → Import an existing Git repository**
   (o "Connect to Git").
3. Conecta tu cuenta de GitHub. Cuando GitHub pregunte a qué repositorios dar acceso, elige
   **Only select repositories → InaMatch**.
4. Configuración de compilación:
   - **Production branch**: `main`
   - **Framework preset**: `Vite` (o ninguno)
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
5. **Save and Deploy**. En un par de minutos estará en `https://<nombre-del-proyecto>.pages.dev`.

A partir de ahí, cada cambio que llegue a `main` se publica solo. La versión de Node la fija `.node-version`.
