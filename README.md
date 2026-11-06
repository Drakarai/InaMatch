# InaMatch

Juego de navegador para PC que recrea los partidos de **Inazuma Eleven 3** (DS): duelos por comandos,
supertécnicas, FP/TP, elementos y la pantalla de formación. Trae **198 equipos**, de IE1 a Victory Road (GO, Chrono Stone, Galaxy, Ares y Orión incluidos), más de 3000 ojeadores y 887 supertécnicas. Gratis y sin servidor: es una web estática
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

Pantalla de "versus": una tarjeta por equipo (**TÚ** a la izquierda, **RIVAL** a la derecha) con el color de su camiseta.
- Cada tarjeta muestra el escudo, la **media** con estrellas, la formación, el jugador **estrella** y barras de
  **Ataque**, **Medio** y **Defensa** de los titulares (delanteros: tiro, control y velocidad; medios: control,
  físico, velocidad y tiro; defensas y portero: defensa, físico y agallas).
- Abajo, la **estantería**: pestañas con el logo de cada juego (Mi club, IE1, IE2, IE3, GO, Chrono Stone, Galaxy, Ares,
  Orión y Victory Road; los logos son los de la [enciclopedia oficial](https://zukan.inazuma.jp/), en
  `src/assets/pack/series/`) y, debajo, todos los escudos del juego elegido. Pulsa una tarjeta (o el segmento
  "eligiendo para") para elegir ese lado y luego un escudo. Las flechas o la rueda del ratón también cambian de
  equipo dentro de su temporada. Nunca pueden estar los dos lados con el mismo equipo: si eliges el del otro lado,
  se intercambian.
- Teclado: izquierda/derecha cambian de equipo, arriba/abajo de temporada, **Tab** de lado, **R** rival al azar y
  **Enter** sigue.
- En el centro: **Cambiar lados** y **Rival al azar** (de cualquier temporada). Se pueden mezclar temporadas.
- La elección se recuerda al volver al menú.
- La barra de arriba es igual en todas las pantallas: volver (o **Esc**) a la izquierda, monedas, **Mi club**,
  **Fichajes** y el botón **♪** del sonido a la derecha.

El rediseño de la interfaz (y la comparativa de antes y después de cada pantalla) está documentado en
`docs/rediseno/`.

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
| En cualquier momento | **Espacio** / **Esc** o el botón **II**: pausa (reanudar, controles, reiniciar, sonido, abandonar y la estamina y técnica de tu equipo) |

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
- En un **duelo** con supertécnica, la pantalla se parte en diagonal con el color de cada técnica. Los dos jugadores
  lanzan su energía, los rayos chocan y forcejean en el centro, y la ganadora empuja, barre la pantalla y hace
  su efecto. La perdedora se rompe. En tiros, bloqueos y paradas se ve la técnica como antes.

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
  audio/           música y efectos de sonido, generados con Web Audio (sin archivos)
  assets/pack/     sprites originales: se usan con solo ponerles el nombre del jugador
docs/              notas de referencia del juego original
```

## Equipos

Los equipos se generan con `python3 -I tools/wiki/teams.py` a partir de la
[wiki inglesa](https://inazuma-eleven.fandom.com/), separados por temporada (cada id empieza por `ie1-`, `ie2-`, `ie3-`, `go-`,
`cs-`, `gx-`, `ares-`, `orion-` o `vr-`). Son 198:
- **IE1 (15):** Raimon, Royal Academy, Zeus, Occult, Wild, Brain, Otaku, Shuriken, Farm, Kirkwood, Inazuma Eleven…
  y el Ultra Zeus.
- **IE2 (33):** Raimon II, Jóvenes Inazuma, la Academia Alius (Génesis, Caos, Épsilon, Prominence, Polvo de Diamantes, Tormenta de
  Géminis…), los Emperadores Oscuros, Royal Academy Redux, los institutos del viaje (Alpino, Mar de Árboles, Fauxshore…).
  Extras: Divinidades y Alienígenas, Neo Royal Academy, Ray Dark All Stars, Alius A y B, Súper Otaku, Súper Triple C,
  Inazuma Kids FC Plus, las Selecciones Nacionales A y B, y las versiones NEW de Génesis, Zeus y Royal Academy.
- **IE3 (39):** las selecciones del Fútbol Frontier Internacional, Neo Japón, Ogro, el Equipo D, el Zoolan Team (equipo de Garshield), los
  equipos del cielo y del infierno, y el Mega Inazuma Eleven. Extras: Raimon I, Neo Raimon, Ultra Raimon, las Pruebas de
  Selección A y B, Neo Japón Plus, Ángel Oscuro, Ángeles del Caos, Equipo Celestial, Leyendas de Antaño, Ases
  Internacionales, los Ases de Asia, Europa, África y Sudamérica, Estrellas Femeninas, Atlético Alius y Nuevo Caos.

- **GO (24), Chrono Stone (21) y Galaxy (17):** los grupos de `Module:PlayerData/GO`, `CS` y `GX`: Raimon, Sector Quinto,
  Protocolo Omega, Chrono Storm, Earth Eleven, los equipos de Galaxy…
- **Ares (14) y Orión (13):** los de `Module:PlayerData/AT` y `OK` (Inakuni Raimon, Seishou, la Inazuma Japón de Orión,
  Unicorn Estelar, la Sombra de Orión…). No tienen juego propio: sus técnicas son las de Victory Road.
- **Victory Road (22):** los de `Module:PlayerData/VR`.

Los extras (versiones mejoradas, selecciones y equipos secretos) no son grupos del módulo de jugadores: están en la lista
`EXTRA` del script, que monta cada uno con la tabla de miembros de su página. Para añadir otro, pon el título de su página
de la wiki inglesa en la temporada que toque.

**Ojeadores:** los jugadores que se fichan en los juegos y no son de ningún equipo (el grupo "Scouts" de cada módulo, unos
3000). Van en `src/data/scouts.json`, que solo se carga para Mi club.

**Atributos de la era GO y de Victory Road:** los juegos GO tienen otros atributos (Regate, Técnica, Bloqueo, Parada,
Suerte…) y los de Victory Road y Ares/Orión no salen en la wiki: se toman de la enciclopedia oficial
[Inazugle](https://zukan.inazuma.jp/en/chara_param/) (`tools/zukan/charas.py` guarda sus 5459 fichas en
`tools/zukan/charas.json`). El script los pasa a la escala de IE3 (cada valor a la misma distancia de la media, por
posición, que entre los jugadores de IE), y la potencia y el coste de las técnicas nuevas igual, por percentiles. Así
todas las temporadas quedan con medias parecidas.

Las respuestas de la wiki se guardan en `tools/wiki/.cache/api` (bórrala para bajarlo todo de nuevo).

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
si no, el de los juegos de DS) a `src/assets/pack/emblems/`. Ya están 193 de 198 (las versiones NEW llevan el del equipo original). Las imágenes de la wiki están en `static.wikia.nocookie.net`; sin escudo, el juego dibuja
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

Las técnicas del juego (`src/data/moves.json`, 887: todas las de la wiki, de IE1 a Victory Road; unas 160 no las lleva nadie y solo salen en los cuadernos) las genera `tools/wiki/teams.py`.
Las de la era GO, Victory Road y Ares/Orión que no tienen datos de IE3 se pasan a su escala por percentiles. Cada una lleva:
- **Nombre:** el de los juegos de DS en España. Sale del catálogo (el título de su página en la wiki española), salvo
  las que están en `moves` de `tools/wiki/overrides.json` (99):
  - La wiki española titula muchas con el nombre del anime y pone aparte el de los juegos ("también conocida como
    … en los videojuegos"): Carrera relámpago es Acelerrelámpago, Trama trama es Trama, Terremoto es Sismo…
  - Las que no tenían nombre en español o lo tenían mal: Vuelo de Ícaro, Regate aurora, Inmersión, Coz 2 y 3,
    Escáner ataque y Escáner defensa.
  - Las de la era GO y Victory Road que la wiki española no trae, traducidas del nombre inglés o japonés
    (Planeo del águila calva, Tiro radiocontrol, ¡Hala! ¡Un ovni!…).
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
- **Era GO, Ares, Orión y Victory Road:** los espíritus guerreros (Keshin) salen gigantes detrás del jugador, y hay
  niebla, lluvia de cartas, dados, un moái, un ancla, pinzas de cangrejo y ojos que brillan en la oscuridad.

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
  - Las técnicas que no están en la enciclopedia (unas 30) van a mano en el propio script.
- Las 887 técnicas tienen receta: 854 sacadas de su vídeo y el resto a mano.
- **Dibujo:** las formas son unas 140, dibujadas por código (`src/gfx/fxshapes.ts`, con utilidades en
  `src/gfx/fxkit.ts` y los efectos básicos en `src/gfx/fx.ts`).
- **Cambiar el efecto de una técnica:** edita su línea en `tools/zukan/recipes.txt` y vuelve a ejecutar el script.

## Sonido

Toda la música y los efectos se generan en el navegador con Web Audio. No hay archivos de audio.
- **Música:** composiciones originales para InaMatch, inspiradas en el estilo de la saga (metales, guitarra
  eléctrica y batería rápida, en tono heroico). No copian melodías de la banda sonora oficial. Hay un tema
  para el menú y la formación, otro para los partidos y una fanfarria para los goles.
- **Efectos:** cada tipo de supertécnica tiene su sonido (fuego, hielo, viento, rayo, tierra, sombras, luz,
  espíritus guardianes, muros, manos gigantes...). También suenan el silbato, los chutes, el gol, el choque de
  técnicas en los duelos y los botones. Mientras suena una técnica, la música baja un momento.
- **Quitarlo:** el botón **♪** del menú o **Sonido** en la pausa. La música y los efectos se activan por
  separado y cada uno tiene su volumen. La elección se guarda en el navegador.
- **Cambiar sonidos:** `src/audio/sfx.ts` (tabla `TECH`, una receta por tipo de efecto) y
  `src/audio/music.ts` (las canciones son listas de acordes y notas por compás).

## Mi club y fichajes

- **Mi club:** tu equipo propio. La primera vez que abres el juego se reparte una plantilla de 16 al azar, distinta para cada
  uno: casi todo ojeadores y jugadores poco conocidos, y uno o dos conocidos. Sale como un equipo más en el menú (pestaña
  "Mi club") y se juega igual que los demás; la formación y la alineación que elijas se guardan.
- **Pantalla del club** (botón **⚡ Mi club** del menú): la plantilla y la colección de jugadores conseguidos. Pulsa un
  hueco de la plantilla y luego un jugador para ponerlo; dos huecos, para cambiarlos.
- **Fichajes** (gacha): tirada a 100 monedas o diez a 900, que traen al menos un ★★★. Probabilidades: ★★★★ Estrella 2 %,
  ★★★ Conocido 10 %, ★★ Poco conocido 28 %, ★ Ojeador 60 %. Los repetidos devuelven monedas.
- **Rareza:** según lo conocido que es cada personaje: en cuántos equipos sale (ojeadores, uno, dos o tres, cuatro o más,
  como Mark o Axel). De cada personaje se puede conseguir su mejor versión, con sus técnicas de la wiki.
- **Monedas:** se empieza con 500. Cada partido con Mi club da 300 ganando, 140 empatando y 70 perdiendo, más 20 por gol;
  con otros equipos, 120, 70 o 40, más 10 por gol.
- **Escudos** (botón **Escudo** del club): los 340 de Victory Road de la wiki (`Category:Victory Road emblem images`,
  en `src/assets/crests/` a 192 px y su lista en `src/data/crests.json`). Se empieza con tres al azar y cada victoria da
  uno nuevo (con todos, 100 monedas); el elegido es el escudo de Mi club en el menú y en los partidos.
- **Rango S:** ganar 5-0 o más sin encajar da 500 monedas extra y un cuaderno de supertécnica ★★★ o ★★★★.
- La partida se guarda en el navegador (`localStorage`); si se borran los datos del sitio, se empieza de cero.
- **Cuadernos de supertécnicas** (botón **Cuadernos** del club): tirada a 80 monedas o diez a 700, que traen al menos un
  ★★★. Cada cuaderno es una supertécnica; su rareza depende de lo potente que es entre las de su tipo (el 7 % más potente
  es ★★★★). Los repetidos se acumulan: con dos cuadernos de la misma técnica se le puede poner a dos jugadores.
- **Editar técnicas** (botón **Editar ✎** de la ficha de un jugador del club): como en los juegos, cada jugador tiene sus
  **4 técnicas de base**, que se pueden cambiar, y **2 huecos extra**. Sus técnicas propias son gratis; las demás gastan un
  cuaderno mientras estén puestas (al quitarlas, el cuaderno vuelve). En el partido salen todas en los comandos (teclas 3–8).
- Código: `src/club/` (plantilla, gacha, cuadernos y guardado) y las escenas `ClubScene` y `GachaScene`.

## Aspecto

- Letras: **Bebas Neue** en títulos y marcadores, como en las retransmisiones deportivas, y **Barlow Semi Condensed**
  en la interfaz. Van dentro del juego (`@fontsource`), y el juego espera a tenerlas antes de arrancar.
- Pantalla de carga con el logo, fondo de estadio de noche y botones y paneles inclinados, como los rótulos del anime.

## Formación

- Pulsa dos jugadores para cambiarlos (titular por suplente o de sitio).
- Pulsa el nombre de la formación para ver la lista de todas. Al pasar el ratón por una, se ve cómo quedaría tu
  equipo en el campo; solo se elige si la pulsas. Las flechas ◀ ▶ pasan de una en una.

## Jugadores: sprites, retratos y descripciones

- **Retrato:** el de Victory Road, con la equipación del equipo en el que juega cada uno (5907 de 5908, ojeadores incluidos: 1970
  de la wiki inglesa y el resto de la [enciclopedia oficial](https://zukan.inazuma.jp/en/chara_param/) o de su ficha
  de la wiki). Solo falta Avatar, el personaje que se crea el jugador en Victory Road, que no tiene cara fija. Sale en la ficha
  de la formación, en el panel del partido y en la animación de las supertécnicas. Los baja
  `python3 -I tools/wiki/sprites.py` (de la wiki inglesa y, si no está, de la enciclopedia) a
  `src/assets/pack/portraits/<equipo>/<jugador>.webp`, y se
  cargan al elegir equipos. Quien no está con el mismo nombre se busca así:
  - En la enciclopedia en inglés, por el nombre del doblaje.
  - En la enciclopedia en japonés (`tools/zukan/charas_ja.json`, de `python3 -I tools/zukan/charas_ja.py`), por el
    nombre japonés de su ficha de la wiki, su apodo o su lectura en kana. Así salen los que allí tienen otro nombre de
    doblaje, como los de la Academia Alius con su alias alienígena (Gordon Star es ゴルレオ, Ashton Malone es アーク).
  - Los que no están en la enciclopedia (cameos de famosos, fusiones Mixi Max de Galaxy, los robots SR y las sombras
    de Osoroshii Kage) llevan el retrato de su ficha de la wiki, ampliado o recortado según
    `tools/wiki/portraits_extra.json`.
- **Sprite del campo:** un muñeco en pixel art, al estilo de los partidos de IE3, parecido a cada jugador:
  - El mismo script saca de su retrato el color del pelo, de la piel y de los ojos, la silueta del peinado y algún
    accesorio, como la cinta de Mark (`src/data/looks.json`).
  - El juego lo dibuja con la equipación de su equipo, y en otro color si es portero.
  - Quien no tiene retrato lleva una cabeza genérica.
- **Descripción:** la oficial de los juegos en español, de la [wiki española](https://inazuma.fandom.com/es/), la de la
  temporada de su equipo (la saca `tools/wiki/teams.py`).
  - Si en la wiki española la página del jugador tiene otro nombre (en el juego español algunos se llaman distinto:
    Umi Wang, los de Los Rojos…), se encuentra por la tabla de miembros de su equipo.
  - Cuando la página trae la traducción literal del japonés y el texto del juego español, se usa el del juego.
  - `tools/wiki/overrides.json`: descripciones escritas a mano para los pocos que no tienen versión española o la
    tienen mal copiada, nombres que la wiki no trae bien y erratas de las descripciones oficiales.
  - Muchas fichas de la wiki española no tienen enlace desde la inglesa ni se llaman como en el doblaje inglés: se
    emparejan por su enlace a la wiki inglesa y por el nombre japonés de la ficha.
  - Los que no tienen descripción oficial en español en ninguna parte (casi todos ojeadores de la era GO y de Victory
    Road) llevan la inglesa traducida: `tools/wiki/descripciones_traducidas.json`.
  - El script deja en `tools/wiki/.cache/sin_descripcion.txt` los que se quedan sin descripción en español.

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

