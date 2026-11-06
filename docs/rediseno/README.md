# Rediseño "estadio" (rama `claude/determined-archimedes-9t98ga`)

Esta rama guarda el rediseño completo de la interfaz sin tocar `main`. Las imágenes de esta carpeta comparan
cada pantalla **antes** (izquierda) y **después** (derecha), a 1920x1080.

| Pantalla | Comparativa |
|---|---|
| Menú | `menu-antes-despues.png` |
| Mi club | `club-antes-despues.png` |
| Fichajes | `gacha-antes-despues.png` |
| Formación | `formation-antes-despues.png` |
| Pausa | `pause-antes-despues.png` |
| Final del partido | `result-antes-despues.png` |
| Nitidez al redimensionar | `nitidez-antes-despues.png` |

## Por qué se veía borroso (y qué se ha arreglado)

1. **El lienzo se creaba una sola vez, al tamaño de la ventana inicial.** Si la pestaña se abría pequeña y luego
   se maximizaba (o se pasaba a otra pantalla, o se cambiaba el zoom del navegador), el navegador estiraba un
   lienzo de 1280x720 hasta 1920x1080 y todo salía difuminado. Ahora `main.ts` vigila el tamaño de la ventana,
   vuelve a crear el lienzo a la resolución real y re-rasteriza todos los textos (`RES_EVENT`).
2. **La resolución se redondeaba a cuartos (1, 1,25, 1,5…)**, así que casi siempre el lienzo no coincidía con la
   ventana y se reescalaba un poco. Ahora se usa la escala exacta (`computeRes`).
3. **Medio píxel:** textos e imágenes centrados caían en coordenadas fraccionarias y se filtraban bilinealmente.
   Se activa `roundPixels` en el renderizador.
4. **El escudo de "Mi club" se generaba a 64 px** y se mostraba a 140 (más de 300 reales): ahora se genera a 256 px
   con un diseño nuevo (escudo blanco, rayo y siglas).

> Los escudos de los equipos (`src/assets/pack/emblems`) son de 160 px y en el menú se ven a ~210-300 px reales
> en pantallas grandes: siguen un poco suavizados. La única solución es bajar versiones más grandes de la wiki
> (`tools/wiki/emblems.py`).

## Fallos de lógica encontrados y corregidos

- **Mismo equipo en los dos lados.** En el menú se podía elegir el mismo equipo como TÚ y RIVAL (y "rival al azar"
  podía sacar tu propio equipo). Ahora al elegir el equipo que está en el otro lado se intercambian, las flechas
  saltan al que está enfrente y el azar lo excluye.
- **Reiniciar partido sin confirmar** desde la pausa borraba el partido con un clic. Ahora reiniciar y abandonar
  piden confirmación en un diálogo (antes abandonar solo cambiaba el rótulo del botón 2,5 s).
- **Fichajes volvía siempre a Mi club** aunque se hubiera entrado desde el menú. Ahora vuelve a donde se vino
  (`from`), también con Esc.
- **Pulsar una carta de la colección sin hueco elegido no hacía nada.** Ahora, si hay hueco vacío, la mete; si
  no, avisa de que primero hay que elegir hueco; si ya está en el 16, lo dice.
- **Portería sin portero.** En el partido, el portero es siempre el jugador del primer hueco (`MatchPlayer.isGK`).
  Mi club y Formación permitían poner ahí a un jugador de campo sin ningún aviso; ahora se avisa en rojo
  ("Sin portero en la portería") y se marcan en rojo los que están fuera de su puesto.
- **El botón de "10 tiradas" aparecía activo aunque no hubiera monedas** hasta el primer refresco: ahora se
  comprueba al crear la pantalla y antes de tirar.
- **El "Final del partido" no decía quién marcó**: ahora salen los goleadores con el minuto bajo cada equipo.

## Calidad de vida añadida

- **Barra superior común** en todas las pantallas: botón de volver a la izquierda (con Esc), título, monedas y
  acciones a la derecha. Antes cada pantalla tenía el "Menú" en un sitio.
- **Menú:** cada equipo tiene tarjeta con media, estrellas, formación y su jugador estrella; segmento "eligiendo
  para TÚ/RIVAL"; la tecla **R** saca un rival al azar; al pasar por un escudo se ve su media.
- **Mi club:** botón **Auto-alinear** (mejor jugador por hueco de la formación, con un portero en el banquillo),
  filtro por rareza además de por puesto, etiquetas TITULAR/BANQUILLO en las cartas, ordenado por media, media de
  cada jugador en la ficha.
- **Formación:** botón **Mejor once**, media y ATA/MED/DEF del once en vivo (cambian al hacer cambios), media
  del jugador en la ficha, media del rival en la cabecera, **Enter** para jugar.
- **Fichajes:** teclas **1** y **0** para tirar, el ahorro de la tirada de diez en el botón, resumen de la suerte
  al final de cada tirada.
- **Avisos no intrusivos** (`toast`) en vez de silencios.
- Botones con pista de tecla (⏎, Esc) y estados seleccionado/desactivado claros.

## Ideas para más adelante (no hechas)

- Buscador de equipos por nombre en el menú (requiere un campo de texto DOM sobre el lienzo).
- Favoritos / últimos equipos usados.
- Arrastrar y soltar en Formación y Mi club en vez de pulsar dos veces.
- Historial de partidos y racha en Mi club (victorias, goles).
- Vender repetidos / cuadernos sobrantes por monedas.
- Un modo "liga" con calendario, aprovechando que ya hay 198 equipos y recompensas.
