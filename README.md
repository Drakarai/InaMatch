# InaMatch

Juego de navegador para PC que recrea los partidos de **Inazuma Eleven 3** (DS): duelos por comandos,
supertécnicas, FP/TP, elementos y la pantalla de formación. Trae **55 equipos** de IE1, IE2 e IE3. Gratis y sin servidor: es una web estática
que se puede publicar gratis en Cloudflare Pages (ver abajo).

> Proyecto de fans sin ánimo de lucro. Inazuma Eleven es una marca de LEVEL-5.

## Jugar en local

Hace falta [Node.js](https://nodejs.org/) 20 o superior.

```bash
npm install
npm run dev      # abre http://localhost:5173
```

Otros comandos: `npm test` (tests de las reglas y los datos), `npm run build` (genera `dist/`) y `npm run typecheck`.

## Menú

Pantalla de "versus": cada mitad lleva los colores de su equipo (**TÚ** a la izquierda, **RIVAL** a la derecha),
partidas por un rayo.
- Cada lado muestra el escudo, la **media** del equipo y barras de **Ataque**, **Medio** y **Defensa** de los titulares
  (delanteros: tiro, control y velocidad; medios: control, físico, velocidad y tiro; defensas y portero: defensa,
  físico y agallas).
- Abajo, la **estantería**: pestañas de temporada (IE1, IE2, IE3) con todos sus escudos. Pulsa una mitad para elegir
  ese lado y luego un escudo. Las flechas o la rueda del ratón también cambian de equipo dentro de su temporada.
- Teclado: izquierda/derecha cambian de equipo, arriba/abajo de temporada, **Tab** de lado y **Enter** sigue.
- En el centro: **Cambiar lados** y **Rival aleatorio** (de cualquier temporada). Se pueden mezclar temporadas.
- La elección se recuerda al volver al menú.

## Controles

El ratón hace de lápiz de la DS.

| Situación | Acción |
|---|---|
| Con balón | **Arrastra desde tu jugador** para dibujar el recorrido: lo va siguiendo mientras dibujas. Sin línea, al recibir espera un momento y luego avanza despacio hacia la portería rival |
| | **Pulsa a un compañero** para pasarle; el bocadillo "¡Aquí!" marca al mejor libre y "¡Tira!" avisa de una buena ocasión |
| | **Pulsa en un hueco** para un pase al espacio |
| | **Pulsa la portería**, el botón **Tirar** o la tecla **T** para tirar. Solo desde cerca del área; desde más lejos, únicamente con una supertécnica de **tiro largo** (el botón pasa a "Tiro largo") |
| Sin balón | **Arrastra a cualquier jugador** para moverlo, o **pulsa en el campo** para mandar al jugador activo (el del aro blanco) |
| Tiro rival en el aire | **Arrastra a un defensa** hasta la línea turquesa para bloquearlo (va a cámara lenta) |
| Duelos y tiros | Botones en pantalla o teclas **1**/**2** (comandos básicos) y **3**, **4**… (supertécnicas) |
| | Si no eliges a tiempo se usa el primer comando |
| En cualquier momento | **Espacio** / **Esc** o el botón **II**: pausa (reanudar, controles, reiniciar, abandonar y la estamina y técnica de tu equipo) |

Comandos básicos:
- **Atacando**: Regate o Finta.
- **Defendiendo**: Entrada o Entrada en plancha. La plancha gana al regate, pero la finta la deja en ridículo
  y, si roba el balón, puede ser **falta** (tiro libre para el rival).
- **Tirando**: Tiro o Vaselina, y después **¡Regula la potencia!** (Normal, Fuerte +10 FP, Máxima +20 FP).
  Las supertécnicas tiran con su potencia, sin regular. Los **tiros largos** (Remate del águila, Excalibur, Remate tsunami…,
  marcados en la wiki) se pueden lanzar desde cualquier sitio del campo. Pierden un 7 % de fuerza por cada segundo
  en el aire (`LONG_SHOT_DECAY` en `src/engine/rules.ts`), así que desde campo propio llegan bastante más flojos.
- **Bloqueando**: el tiro vuela en tiempo real con su trayectoria marcada.
  - Cuando tira la CPU, el juego va a **cámara lenta**: arrastra a un defensa hasta la línea para cruzarte.
  - El defensa que se cruza elige Bloquear o Dejar pasar. Si no lo para, el tiro llega más flojo.
  - Cuando tiras tú, los defensas rivales corren a cortarte.
  - Los tiros potentes vuelan más rápido, y la vaselina pasa por encima de todos.
- **Portero**: Atrapar o Despejar.

En cada duelo se ve el **Poder** de los dos jugadores y, al resolverse, el choque de potencias.
- **Apoyo**: cada compañero cerca del duelo suma un 10 % (máximo dos; sale el doble aro rojo). Si además es de la
  misma afinidad que el jugador del duelo, suma otro 10 % (**¡Bonus de afinidad!**).
- **FIRED UP**: ganar duelos, bloquear, parar o encajar un gol llena la barra de tensión del equipo.
  Al llenarse, el equipo juega 25 segundos con un +15 %.

Las supertécnicas gastan TP y suelen ganar a los comandos básicos. Además, **afinidades**:
- Ciclo: **Bosque > Aire > Montaña > Fuego > Bosque** (+20 % al que gana). **Neutro** (morado) va aparte:
  ni gana ni pierde y no tiene STAB.
- Se evalúan en **dos capas por separado**:
  - **Jugadores:** cuenta siempre, aunque nadie use técnica.
  - **Técnicas:** solo cuando los dos usan supertécnica.
  - Ejemplo: Aire con técnica de Bosque contra Montaña con técnica de Fuego. El de Aire gana por jugadores y pierde por
    técnicas, así que las ventajas se anulan.
- **STAB**: técnica de la misma afinidad que el jugador, +25 %.
- En el panel de duelo, el punto de color es la afinidad del jugador y la flechita marca quién tiene ventaja.
- Los porcentajes no son oficiales; están juntos en `src/data/elements.ts` y `src/engine/rules.ts` para ajustarlos.
- **Estamina (FP, naranja):** se gasta al moverse, al tirar (más cuanto más fuerte) y al parar. Con la estamina
  agotada, el jugador corre más despacio y rinde algo menos en duelos, tiros y paradas.
- **Técnica (TP, verde):** solo la gastan las supertécnicas.
- **Descanso:** todos recuperan un 33 % de cada barra. Se abre la formación para hacer cambios (cada jugador
  conserva su estamina) o cambiar de formación antes de la 2ª parte.
- En un **duelo** con supertécnica, las dos elecciones aparecen frente a frente, chocan y queda la ganadora, que
  hace su efecto. En tiros, bloqueos y paradas se ve la técnica como antes.

El ritmo general del partido se ajusta con `GAME_SPEED` en `src/config.ts` (ahora 0,75; 1 = más rápido).

## Estructura

```
src/
  data/            equipos (teams/*.json), supertécnicas (moves.json), formaciones y elementos
  engine/          reglas puras (duelos, tiros, IA de comandos) + tests
  match/           entidad jugador del partido
  scenes/          Boot, Menú, Formación, Partido y HUD (marcador, duelos, radar, animaciones)
  ui/              botones, barras y el tema visual (theme.ts: colores, formas inclinadas, fondos)
  gfx/             gráficos provisionales generados por código
  assets/pack/     sprites originales: se usan con solo ponerles el nombre del jugador
docs/              notas de referencia del juego original
```

## Equipos

Los equipos se generan con `python3 -I tools/wiki/teams.py` a partir de la
[wiki inglesa](https://inazuma-eleven.fandom.com/), separados por temporada (cada id empieza por `ie1-`, `ie2-` o `ie3-`):
- **IE1 (14):** Raimon, Royal Academy, Zeus, Occult, Wild, Brain, Otaku, Shuriken, Farm, Kirkwood, Inazuma Eleven…
- **IE2 (20):** Raimon II, Jóvenes Inazuma, la Academia Alius (Génesis, Caos, Épsilon, Prominence, Polvo de Diamantes, Tormenta de
  Géminis…), los Emperadores Oscuros, Royal Academy Redux, los institutos del viaje (Alpino, Mar de Árboles, Fauxshore…).
- **IE3 (21):** las selecciones del Fútbol Frontier Internacional, Neo Japón, Ogro, el Equipo D, el Zoolan Team (equipo de Garshield), los
  equipos del cielo y del infierno, y el Mega Inazuma Eleven.

De dónde sale cada cosa:
- **Plantilla, dorsales y formación:** la tabla de miembros de ese juego en la página de cada equipo.
- **Posición, afinidad y técnicas:** `Module:PlayerData/IE`, `IE2` e `IE3`, las del juego de cada temporada.
- **Nombre europeo, atributos a nivel 99 y descripción:** la página de cada jugador, en la pestaña del juego de la
  temporada (si falta, la del juego más cercano; 4 jugadores sin datos llevan atributos estimados por su posición).
- **Técnicas:** potencia y coste de IE3 de `Module:WazaData` (o de IE2 si no salen en IE3), con el nombre en español del catálogo.
- **Formaciones:** nombre y distribución (F-D Lion 4-4-2, F-Kingdom 4-3-3…); el juego coloca a los jugadores a partir de la distribución.
- **Nombre del equipo en español:** el enlace con la [wiki española](https://inazuma.fandom.com/es/). Los que no lo
  tienen, o se llaman distinto en los juegos (Polvo de Diamantes, Servicio Secreto, Equipo D, Os Reis…), están en
  `NAME_ES` dentro del script.
- **Titulares:** portero y las líneas de la formación por orden de dorsal. Si faltan jugadores de una posición, entra el que mejor encaja por atributos.

**Escudos:** `python3 -I tools/wiki/emblems.py` baja el de cada equipo de la wiki (el rehecho para Victory Road si lo hay;
si no, el de los juegos de DS) a `src/assets/pack/emblems/`. Ya están los 55. Las imágenes de la wiki están en `static.wikia.nocookie.net`; sin escudo, el juego dibuja
uno provisional con las siglas.

Lo que no viene en la wiki se pone a mano en el script: los colores de los equipos más conocidos (el resto lleva colores
sacados de su nombre) y las siglas.
En el campo se ve el nombre de pila en los equipos japoneses y el apellido en el resto.

Para añadir un equipo a mano, crea un `.json` en `src/data/teams/` copiando uno de los existentes y aparecerá solo en el menú,
en la temporada que diga su campo `season` (sin él, en "Otros equipos").
- Los 11 primeros jugadores son los titulares, en el orden de los huecos de la formación, empezando por el portero.
- `npm test` avisa de técnicas inexistentes, ids repetidos o plantillas incompletas.
- Después, `python3 -I tools/pack_readme.py` actualiza la lista de nombres de los sprites.

## Catálogo de supertécnicas

`data/tecnicas.json` tiene **883 supertécnicas** sacadas de la
[wiki inglesa](https://inazuma-eleven.fandom.com/) y la [wiki española](https://inazuma.fandom.com/es/) de Inazuma Eleven.
De cada una guarda:
- Nombre en español (814 lo tienen), nombre de la wiki inglesa y nombre del doblaje.
- Tipo y afinidad. Las técnicas con versiones de distinta afinidad guardan todas en `elements`, con la principal
  primero. Por ejemplo, Mano mágica es de Montaña en la versión de Mark y de Bosque en la de Darren; en el juego
  son dos técnicas distintas.
- Potencia y coste en Victory Road, y TP en IE3.

Las técnicas del juego (`src/data/moves.json`) las genera `tools/wiki/teams.py`. Cada una lleva:
- **Nombre:** en español, del catálogo.
- **Potencia y coste:** los de IE3 (`Module:WazaData`).
- **Afinidad:** la de cada versión. Por ejemplo, la Mano mágica de Darren es de Bosque.

Para actualizar el catálogo cuando cambien las wikis: `tools/wiki/build.sh` (hace unas 50 peticiones, con pausas).

Los textos y datos de las wikis de Fandom están bajo licencia [CC BY-SA](https://creativecommons.org/licenses/by-sa/3.0/).

## Efectos de las supertécnicas

Cada supertécnica tiene su propio efecto especial, hecho a partir de su vídeo en la
[enciclopedia oficial de Victory Road](https://zukan.inazuma.jp/en/skill/). Algunos ejemplos:
- **Manos:** la Mano celestial es amarilla, con rayos y relámpagos. La Mano mágica sale con el Majin detrás y la
  Mano diabólica con un demonio morado. El Millón de manos son muchas manos pequeñas.
- **Criaturas:** pingüinos rojos, morados o con casco espacial; guiverno con alas; rey dragón; fénix, águila,
  cóndor y pegaso; tigre y lobo; ballena, tiburón, unicornio y serpiente.
- **Muros:** de roca, de hierro, de piedra, una montaña o pilares.
- **Fuego:** espiral de llamas (Tornado de fuego), bola de fuego, sol (Llamarada atómica), tormenta, géiseres y
  explosiones.
- **Hielo, rayos y oscuridad:** ventisca con un copo gigante (Ventisca eterna), bloque de hielo, rayo enorme del
  cielo, orbe eléctrico, agujero negro, espiral blanca y negra (Carga negativa) y portales.
- **Objetos y lugares:** Excalibur, las siete espadas del Círculo de espadas, el Coliseo, la Torre Eiffel, un torii,
  un reloj, un tren, un misil, llaves, un abanico, una tabla de surf, la telaraña…

Cómo se ven en el partido:
- La animación con el retrato toma los colores reales del vídeo y las partículas del efecto.
- Después, el efecto aparece sobre el campo, orientado hacia el rival, la portería o el balón.
- En los tiros, el balón deja una estela del mismo tipo.
- En un duelo de supertécnicas (regate contra defensa, tiro contra bloqueo o contra el portero) solo se ve la
  animación de la que gana. Si solo uno usa supertécnica, se ve la suya y, si pierde, salta en pedazos.

Cómo está hecho:
- **Receta:** cada técnica tiene una forma con su variante (`dragon:wyvern`, `hand:majin`…), capas que la
  acompañan y sus colores. Está en `src/data/movefx.json`, que genera `python3 -I tools/zukan/recipes.py` a partir de:
  - `tools/zukan/recipes.txt`: la forma de cada técnica, anotada viendo su vídeo fotograma a fotograma.
  - `tools/zukan/palette.json`: los colores de cada vídeo (`tools/zukan/palette.py` los saca de los fotogramas).
  - Las técnicas que no están en la enciclopedia van a mano en el propio script.
- **Dibujo:** las formas son unas 130, dibujadas por código (`src/gfx/fxshapes.ts`, con utilidades en
  `src/gfx/fxkit.ts` y los efectos básicos en `src/gfx/fx.ts`).
- **Cambiar el efecto de una técnica:** edita su línea en `tools/zukan/recipes.txt` y vuelve a ejecutar el script.

## Jugadores: sprites, retratos y descripciones

- **Retrato:** el de Victory Road, con la equipación del equipo en el que juega cada uno (732 de 810). Sale en la ficha
  de la formación, en el panel del partido y en la animación de las supertécnicas. Los baja
  `python3 -I tools/wiki/sprites.py` de la wiki inglesa a `src/assets/pack/portraits/<equipo>/<jugador>.webp`, y se
  cargan al elegir equipos.
- **Sprite del campo:** un muñeco en pixel art, al estilo de los partidos de IE3, parecido a cada jugador:
  - El mismo script saca de su retrato el color del pelo, de la piel y de los ojos, la silueta del peinado y algún
    accesorio, como la cinta de Mark (`src/data/looks.json`).
  - El juego lo dibuja con la equipación de su equipo, y en otro color si es portero.
  - Quien no tiene retrato lleva una cabeza genérica.
- **Descripción:** la oficial de los juegos en español, de la [wiki española](https://inazuma.fandom.com/es/), la de la
  temporada de su equipo (la saca `tools/wiki/teams.py`). Unas 70 no tienen versión española y van en inglés.

### Sprites originales

Si tienes los sprites de verdad, mételos en `src/assets/pack/sprites/` con el nombre del jugador
(`sprites/axel-blaze.png`…) y sustituyen al muñeco dibujado.
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

### Probar ramas en GitHub Pages

Las ramas `claude/...` se publican en `https://drakarai.github.io/InaMatch/` con
`.github/workflows/pages.yml`, sin gastar despliegues de Cloudflare. Hay que activarlo una vez:
1. **Settings → Pages → Source: GitHub Actions**.
2. **Settings → Environments → github-pages → Deployment branches and tags**: añade la regla `claude/*`.
3. En Cloudflare, **Settings → Builds & deployments → Branch control → Preview deployments: None**, para que solo publique `main`.

