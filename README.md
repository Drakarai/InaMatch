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

Como el "Partido clásico" de FIFA: una columna para tu equipo (**LOCAL**) y otra para la CPU (**VISITANTE**).
- Arriba, las **temporadas** (IE1, IE2, IE3) hacen de ligas. Abajo sale el logo de la temporada.
- En la ficha: escudo, estrellas y medias **ATA / MED / DEF** de los titulares (delanteros: tiro, control y velocidad;
  medios: control, físico, velocidad y tiro; defensas y portero: defensa, físico y agallas).
- **◀ ▶** (o la rueda del ratón sobre la ficha) cambian de equipo. Con teclado: flechas izquierda/derecha para el equipo,
  arriba/abajo para la temporada, **Tab** para pasar a la otra columna y **Enter** para seguir.
- En el centro: **Cambiar lados** y **Rival aleatorio** (de cualquier temporada). Se pueden mezclar temporadas.
- La elección se recuerda al volver al menú.

## Controles

El ratón hace de lápiz de la DS.

| Situación | Acción |
|---|---|
| Con balón | **Arrastra desde tu jugador** para dibujar el recorrido: lo va siguiendo mientras dibujas |
| | **Pulsa a un compañero** para pasarle; el bocadillo "¡Aquí!" marca al mejor libre y "¡Tira!" avisa de una buena ocasión |
| | **Pulsa en un hueco** para un pase al espacio |
| | **Pulsa la portería**, el botón **Tirar** o la tecla **T** para tirar |
| Sin balón | **Arrastra a cualquier jugador** para moverlo, o **pulsa en el campo** para mandar al jugador activo (el del aro blanco) |
| Tiro rival en el aire | **Arrastra a un defensa** hasta la línea turquesa para bloquearlo (va a cámara lenta) |
| Duelos y tiros | Botones en pantalla o teclas **1**/**2** (comandos básicos) y **3**, **4**… (supertécnicas) |
| | Si no eliges a tiempo se usa el primer comando |
| En cualquier momento | **Espacio** / **Esc** o el botón **II**: pausa |

Comandos básicos:
- **Atacando**: Regate o Finta.
- **Defendiendo**: Entrada o Entrada en plancha. La plancha gana al regate, pero la finta la deja en ridículo
  y, si roba el balón, puede ser **falta** (tiro libre para el rival).
- **Tirando**: Tiro o Vaselina, y después **¡Regula la potencia!** (Normal, Fuerte +10 TP, Máxima +20 TP).
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
- Con poca **FP** el jugador rinde menos.

El ritmo general del partido se ajusta con `GAME_SPEED` en `src/config.ts` (ahora 0,75; 1 = más rápido).

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

### Probar ramas en GitHub Pages

Las ramas `claude/...` se publican en `https://drakarai.github.io/InaMatch/` con
`.github/workflows/pages.yml`, sin gastar despliegues de Cloudflare. Hay que activarlo una vez:
1. **Settings → Pages → Source: GitHub Actions**.
2. **Settings → Environments → github-pages → Deployment branches and tags**: añade la regla `claude/*`.
3. En Cloudflare, **Settings → Builds & deployments → Branch control → Preview deployments: None**, para que solo publique `main`.

