# Sprites originales

Deja aquí las imágenes **con el nombre exacto de la lista de abajo** y el juego las usará en lugar
de los dibujos provisionales. No hay que tocar código ni ningún archivo de configuración.

```
src/assets/pack/
  sprites/     muñeco en el campo        → sprites/mark-evans.png
  portraits/   retrato (ficha y duelos)  → portraits/mark-evans.png (todos sus equipos)
                                           portraits/ie3-inazuma-japan/mark-evans.webp (solo ese equipo)
  emblems/     escudo del equipo         → emblems/ie3-inazuma-japan.png
```

- Formatos: `.png` (recomendado), `.webp`, `.gif` o `.jpg`.
- **Sprite de campo**: un solo fotograma del jugador de frente, parado, con fondo transparente.
  Se escala a 46 px de alto con escalado nítido, así que vale el tamaño original de la DS.
- **Retrato**: cuadrado, con o sin fondo. Los de Victory Road de cada equipo ya están (los baja
  `tools/wiki/sprites.py`); uno puesto directamente en `portraits/` vale para todos los equipos del jugador
  que no tengan el suyo.
- **Escudo**: cuadrado con fondo transparente.
- Lo que no pongas se sigue dibujando por código (el muñeco en pixel art parecido a cada jugador);
  puedes ir poco a poco.
- Un sprite de campo puesto aquí se usa en todos los equipos del jugador, con la ropa que traiga dibujada.

Esta lista se regenera con `python3 -I tools/pack_readme.py`.

## Nombres de archivo

### Sallys

Escudo: `emblems/ie1-ichibangai-sally-s.png`

| Jugador | Archivo |
|---|---|
| 1 · Suzanne Yuma (GK) | `suzanne-yuma.png` |
| 2 · T. Fielding ({{Media (DF) | `t-fielding-media.png` |
| 3 · A. Lovely ({{Media (DF) | `a-lovely-media.png` |
| 4 · Louis Hillside (DF) | `louis-hillside.png` |
| 5 · Ness Sheldon (DF) | `ness-sheldon.png` |
| 6 · Lizzy Squirrel (MF) | `lizzy-squirrel.png` |
| 7 · Kippy Jones (MF) | `kippy-jones.png` |
| 8 · F. Riversong ({{Media (MF) | `f-riversong-media.png` |
| 9 · Samantha Moonlight (FW) | `samantha-moonlight.png` |
| 10 · Mitch Sandstone (MF) | `mitch-sandstone.png` |
| 11 · Eddie Prentice (FW) | `eddie-prentice.png` |
| 12 · Alf Holmes (FW) | `alf-holmes.png` |
| 13 · Ian Stager (DF) | `ian-stager.png` |
| 14 · Fred Crumb (DF) | `fred-crumb.png` |
| 15 · Doug Baughan (FW) | `doug-baughan.png` |
| 16 · Pip Daltry (DF) | `pip-daltry.png` |

### Inazuma Eleven

Escudo: `emblems/ie1-inazuma-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · Seymour Hillman (GK) | `seymour-hillman.png` |
| 2 · Charles Island (DF) | `charles-island.png` |
| 3 · Garret Hairtown (DF) | `garret-hairtown.png` |
| 4 · Arthur Sweet (DF) | `arthur-sweet.png` |
| 5 · Peter Mildred (MF) | `peter-mildred.png` |
| 6 · Josh Nathaniel (MF) | `josh-nathaniel.png` |
| 7 · Edward Gladstone (MF) | `edward-gladstone.png` |
| 8 · Tyler Thomas (MF) | `tyler-thomas.png` |
| 9 · Joseph Yosemite (FW) | `joseph-yosemite.png` |
| 10 · Ian Suffolk (MF) | `ian-suffolk.png` |
| 11 · Constant Builder (FW) | `constant-builder.png` |
| 12 · Ted Poe (FW) | `ted-poe.png` |
| 13 · Marshall Heart (FW) | `marshall-heart.png` |
| 14 · Dom Foreman (MF) | `dom-foreman.png` |
| 15 · Slot MacHines (DF) | `slot-machines.png` |
| 16 · Bill Steakspear (DF) | `bill-steakspear.png` |

### Inazuma Kids FC

Escudo: `emblems/ie1-inazuma-kfc.png`

| Jugador | Archivo |
|---|---|
| 1 · Herman Muller (GK) | `herman-muller.png` |
| 2 · Keth Claus (DF) | `keth-claus.png` |
| 3 · Robert Silver (DF) | `robert-silver.png` |
| 4 · Izzy Island (DF) | `izzy-island.png` |
| 5 · Sothern Newman (DF) | `sothern-newman.png` |
| 6 · Irwin Hall (MF) | `irwin-hall.png` |
| 7 · Taylor Higgins (MF) | `taylor-higgins.png` |
| 8 · Jamie Cool (MF) | `jamie-cool.png` |
| 9 · Hans Randall (FW) | `hans-randall.png` |
| 10 · Michael Riverside (MF) | `michael-riverside.png` |
| 11 · Millie Moonlight (FW) | `millie-moonlight.png` |
| 12 · Karl Blue (MF) | `karl-blue.png` |
| 13 · Theakston Plank (FW) | `theakston-plank.png` |
| 14 · Ken Cake (FW) | `ken-cake.png` |
| 15 · Mitch Grumble (MF) | `mitch-grumble.png` |
| 16 · Bart Grantham (DF) | `bart-grantham.png` |

### Instituto Umbrella

Escudo: `emblems/ie1-kasamino.png`

| Jugador | Archivo |
|---|---|
| 1 · Joe Ingram (GK) | `joe-ingram.png` |
| 2 · Kendall Sefton (DF) | `kendall-sefton.png` |
| 3 · Jason Strike (DF) | `jason-strike.png` |
| 4 · Norman Porter (DF) | `norman-porter.png` |
| 5 · Maxwell Claus (DF) | `maxwell-claus.png` |
| 6 · Bruce Chaney (MF) | `bruce-chaney.png` |
| 7 · Leroy Rhymes (MF) | `leroy-rhymes.png` |
| 8 · Mildford Scott (MF) | `mildford-scott.png` |
| 9 · Lou Edmonds (FW) | `lou-edmonds.png` |
| 10 · Cameron Morefield (MF) | `cameron-morefield.png` |
| 11 · Greg Bernard (FW) | `greg-bernard.png` |
| 12 · Peter Banker (MF) | `peter-banker.png` |
| 13 · Saul Tunk (MF) | `saul-tunk.png` |
| 14 · Alan Most (DF) | `alan-most.png` |
| 15 · Paul Caperock (DF) | `paul-caperock.png` |
| 16 · Julius Molehill (DF) | `julius-molehill.png` |

### Instituto Kirkwood

Escudo: `emblems/ie1-kidokawa-seishuu.png`

| Jugador | Archivo |
|---|---|
| 1 · Axel Blaze (FW) | `axel-blaze.png` |
| 2 · John Neville (GK) | `john-neville.png` |
| 3 · Malcolm Night (DF) | `malcolm-night.png` |
| 4 · Alfred Meenan (DF) | `alfred-meenan.png` |
| 5 · Dan Mirthful (DF) | `dan-mirthful.png` |
| 6 · Ricky Clover (DF) | `ricky-clover.png` |
| 7 · Toby Damian (MF) | `toby-damian.png` |
| 8 · York Nashmith (MF) | `york-nashmith.png` |
| 9 · Zachary Moore (MF) | `zachary-moore.png` |
| 10 · Marvin Murdock (FW) | `marvin-murdock.png` |
| 11 · Thomas Murdock (FW) | `thomas-murdock.png` |
| 12 · Tyler Murdock (FW) | `tyler-murdock.png` |
| 13 · Simon Calier (MF) | `simon-calier.png` |
| 14 · Brody Gloom (MF) | `brody-gloom.png` |
| 15 · Victor Talis (MF) | `victor-talis.png` |
| 16 · Eren Middleton (DF) | `eren-middleton.png` |

### Instituto Brain

Escudo: `emblems/ie1-mikage-sennou.png`

| Jugador | Archivo |
|---|---|
| 1 · Thomas Feldt (GK) | `thomas-feldt.png` |
| 2 · Harry Leading (DF) | `harry-leading.png` |
| 3 · Terry Stronger (DF) | `terry-stronger.png` |
| 4 · Philip Marvel (DF) | `philip-marvel.png` |
| 5 · Noel Good (DF) | `noel-good.png` |
| 6 · Tyron Rock (MF) | `tyron-rock.png` |
| 7 · Francis Tell (MF) | `francis-tell.png` |
| 8 · Samuel Buster (MF) | `samuel-buster.png` |
| 9 · Jonathan Seller (FW) | `jonathan-seller.png` |
| 10 · Victor Kind (MF) | `victor-kind.png` |
| 11 · Neil Turner (FW) | `neil-turner.png` |
| 12 · Reg Underwood (MF) | `reg-underwood.png` |
| 13 · Patrick Stiller (MF) | `patrick-stiller.png` |
| 14 · Charles Oughtry (MF) | `charles-oughtry.png` |
| 15 · Clive Mooney (FW) | `clive-mooney.png` |
| 16 · Neil Waters (DF) | `neil-waters.png` |

### Instituto Wild

Escudo: `emblems/ie1-nose.png`

| Jugador | Archivo |
|---|---|
| 1 · Charlie Boardfield (GK) | `charlie-boardfield.png` |
| 2 · Hugo Tallgeese (MF) | `hugo-tallgeese.png` |
| 3 · Wilson Fishman (DF) | `wilson-fishman.png` |
| 4 · Peter Johnson (DF) | `peter-johnson.png` |
| 5 · Leonard O'Shea (DF) | `leonard-o-shea.png` |
| 6 · Cham Lion (MF) | `cham-lion.png` |
| 7 · Steve Eagle (MF) | `steve-eagle.png` |
| 8 · Bruce Monkey (MF) | `bruce-monkey.png` |
| 9 · Gary Lancaster (FW) | `gary-lancaster.png` |
| 10 · Harry Snake (FW) | `harry-snake.png` |
| 11 · Adrian Speed (FW) | `adrian-speed.png` |
| 12 · Alan Coe (MF) | `alan-coe.png` |
| 13 · Philip Anders (FW) | `philip-anders.png` |
| 14 · Rocky Rackham (DF) | `rocky-rackham.png` |
| 15 · Matt Mouseman (MF) | `matt-mouseman.png` |
| 16 · Chad Bullford (DF) | `chad-bullford.png` |

### Instituto Occult

Escudo: `emblems/ie1-occult.png`

| Jugador | Archivo |
|---|---|
| 1 · Nathan Jones (GK) | `nathan-jones.png` |
| 2 · Russell Walk (DF) | `russell-walk.png` |
| 3 · Jason Jones (DF) | `jason-jones.png` |
| 4 · Ken Furan (DF) | `ken-furan.png` |
| 5 · Jerry Fulton (DF) | `jerry-fulton.png` |
| 6 · Ray Mannings (MF) | `ray-mannings.png` |
| 7 · Robert Mayer (MF) | `robert-mayer.png` |
| 8 · Alexander Brave (MF) | `alexander-brave.png` |
| 9 · Johan Tassman (FW) | `johan-tassman.png` |
| 10 · Troy Moon (MF) | `troy-moon.png` |
| 11 · Burt Wolf (MF) | `burt-wolf.png` |
| 12 · Rob Crombie (DF) | `rob-crombie.png` |
| 13 · Chuck Dollman (FW) | `chuck-dollman.png` |
| 14 · Uxley Allen (FW) | `uxley-allen.png` |
| 15 · Phil Noir (FW) | `phil-noir.png` |
| 16 · Mick Askley (MF) | `mick-askley.png` |

### Instituto Raimon

Escudo: `emblems/ie1-raimon.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Mark Evans (GK) | `mark-evans-endou-b.png` |
| 3 · Nathan Swift (DF) | `nathan-swift.png` |
| 4 · Jack Wallside (DF) | `jack-wallside.png` |
| 5 · Jim Wraith (DF) | `jim-wraith.png` |
| 6 · Tod Ironside (DF) | `tod-ironside.png` |
| 7 · Steve Grim (MF) | `steve-grim.png` |
| 8 · Tim Saunders (MF) | `tim-saunders.png` |
| 9 · Sam Kincaid (MF) | `sam-kincaid.png` |
| 10 · Maxwell Carson (FW) | `maxwell-carson.png` |
| 11 · Axel Blaze (FW) | `axel-blaze.png` |
| 12 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 13 · William Glass (FW) | `william-glass.png` |
| 14 · Bobby Shearer (DF) | `bobby-shearer.png` |
| 15 · Jude Sharp (MF) | `jude-sharp.png` |
| 16 · Erik Eagle (MF) | `erik-eagle.png` |

### Instituto Farm

Escudo: `emblems/ie1-senbayama.png`

| Jugador | Archivo |
|---|---|
| 1 · Albert Green (GK) | `albert-green.png` |
| 2 · Seward Hayseed (DF) | `seward-hayseed.png` |
| 3 · Kent Work (DF) | `kent-work.png` |
| 4 · Mark Hillvalley (DF) | `mark-hillvalley.png` |
| 5 · Herb Sherman (DF) | `herb-sherman.png` |
| 6 · Joe Small (MF) | `joe-small.png` |
| 7 · Ike Steiner (MF) | `ike-steiner.png` |
| 8 · Orville Newman (MF) | `orville-newman.png` |
| 9 · Tom Walters (MF) | `tom-walters.png` |
| 10 · Daniel Dawson (MF) | `daniel-dawson.png` |
| 11 · Stuart Racoonfur (FW) | `stuart-racoonfur.png` |
| 12 · Lorne Mower (DF) | `lorne-mower.png` |
| 13 · Homer Grower (DF) | `homer-grower.png` |
| 14 · Rolf Howells (DF) | `rolf-howells.png` |
| 15 · Luke Lively (DF) | `luke-lively.png` |
| 16 · Ben Nevis (DF) | `ben-nevis.png` |

### Instituto Shuriken

Escudo: `emblems/ie1-sengoku-igajima.png`

| Jugador | Archivo |
|---|---|
| 1 · Morgan Sanders (GK) | `morgan-sanders.png` |
| 2 · Newton Flust (DF) | `newton-flust.png` |
| 3 · Jim Hillfort (DF) | `jim-hillfort.png` |
| 4 · Galen Thunderbird (DF) | `galen-thunderbird.png` |
| 5 · Finn Stoned (DF) | `finn-stoned.png` |
| 6 · Phil Wingate (MF) | `phil-wingate.png` |
| 7 · Jez Shell (MF) | `jez-shell.png` |
| 8 · Jupiter Jumper (MF) | `jupiter-jumper.png` |
| 9 · Sam Samurai (FW) | `sam-samurai.png` |
| 10 · Hank Sullivan (MF) | `hank-sullivan.png` |
| 11 · Sail Bluesea (FW) | `sail-bluesea.png` |
| 12 · John Reynolds (FW) | `john-reynolds.png` |
| 13 · Dan Hopper (DF) | `dan-hopper.png` |
| 14 · Cal Trops (MF) | `cal-trops.png` |
| 15 · Winston Falls (MF) | `winston-falls.png` |
| 16 · Kevin Castle (GK) | `kevin-castle.png` |

### Instituto Otaku

Escudo: `emblems/ie1-shuuyou-meito-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Sam Idol (GK) | `sam-idol.png` |
| 2 · Marcus Train (DF) | `marcus-train.png` |
| 3 · Light Nobel (MF) | `light-nobel.png` |
| 4 · Walter Valiant (MF) | `walter-valiant.png` |
| 5 · Spencer Gates (DF) | `spencer-gates.png` |
| 6 · Josh Spear (FW) | `josh-spear.png` |
| 7 · Gaby Farmer (FW) | `gaby-farmer.png` |
| 8 · A. Woodbridge (MF) | `a-woodbridge.png` |
| 9 · Gus Gamer (FW) | `gus-gamer.png` |
| 10 · Mark Gambling (FW) | `mark-gambling.png` |
| 11 · Theodore Master (FW) | `theodore-master.png` |
| 12 · Ham Signalman (MF) | `ham-signalman.png` |
| 13 · Bill Formby (DF) | `bill-formby.png` |
| 14 · Grant Eldorado (FW) | `grant-eldorado.png` |
| 15 · Mike Vox (DF) | `mike-vox.png` |
| 16 · Ollie Webb (DF) | `ollie-webb.png` |

### Royal Academy

Escudo: `emblems/ie1-teikoku-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Joseph King (GK) | `joseph-king.png` |
| 2 · Peter Drent (DF) | `peter-drent.png` |
| 3 · Ben Simmons (DF) | `ben-simmons.png` |
| 4 · Alan Master (MF) | `alan-master.png` |
| 5 · Gus Martin (DF) | `gus-martin.png` |
| 6 · Herman Waldon (MF) | `herman-waldon.png` |
| 7 · John Bloom (MF) | `john-bloom.png` |
| 8 · Derek Swing (MF) | `derek-swing.png` |
| 9 · Daniel Hatch (FW) | `daniel-hatch.png` |
| 10 · Jude Sharp (MF) | `jude-sharp.png` |
| 11 · David Samford (FW) | `david-samford.png` |
| 12 · Bob Carlton (DF) | `bob-carlton.png` |
| 13 · Cliff Tomlinson (FW) | `cliff-tomlinson.png` |
| 14 · Jim Lawrenson (FW) | `jim-lawrenson.png` |
| 15 · Barry Potts (MF) | `barry-potts.png` |
| 16 · Steve Ingham (FW) | `steve-ingham.png` |

### Instituto Zeus

Escudo: `emblems/ie1-zeus.png`

| Jugador | Archivo |
|---|---|
| 1 · Paul Siddon (GK) | `paul-siddon.png` |
| 2 · Apollo Light (DF) | `apollo-light.png` |
| 3 · Jeff Iron (DF) | `jeff-iron.png` |
| 4 · Lane War (DF) | `lane-war.png` |
| 5 · Danny Wood (DF) | `danny-wood.png` |
| 6 · Artie Mishman (MF) | `artie-mishman.png` |
| 7 · Arion Matlock (MF) | `arion-matlock.png` |
| 8 · Wesley Knox (MF) | `wesley-knox.png` |
| 9 · Jonas Demetrius (FW) | `jonas-demetrius.png` |
| 10 · Byron Love (MF) | `byron-love.png` |
| 11 · Henry House (MF) | `henry-house.png` |
| 12 · Iggy Russ (GK) | `iggy-russ.png` |
| 13 · Gus Heeley (FW) | `gus-heeley.png` |
| 14 · Harry Closs (DF) | `harry-closs.png` |
| 15 · Andy Chronic (DF) | `andy-chronic.png` |
| 16 · Ned Yousef (MF) | `ned-yousef.png` |

### Caos

Escudo: `emblems/ie2-chaos.png`

| Jugador | Archivo |
|---|---|
| 1 · Grant Cook (GK) | `grant-cook.png` |
| 2 · Bonnie Sparks (DF) | `bonnie-sparks.png` |
| 3 · Claire Lesnow (DF) | `claire-lesnow.png` |
| 4 · Albert Denver (DF) | `albert-denver.png` |
| 5 · Ben Blowton (MF) | `ben-blowton.png` |
| 6 · Ethan Whitering (MF) | `ethan-whitering.png` |
| 7 · Dawson Foxx (MF) | `dawson-foxx.png` |
| 8 · Ving Rice (MF) | `ving-rice.png` |
| 9 · Claude Beacons (FW) | `claude-beacons.png` |
| 10 · Nigel August (FW) | `nigel-august.png` |
| 11 · Bryce Whitingale (FW) | `bryce-whitingale.png` |

### Emperadores Oscuros (con capa)

Escudo: `emblems/ie2-dark-emperors-cloaked.png`

| Jugador | Archivo |
|---|---|
| 1 · Seymour Hillman (GK) | `seymour-hillman.png` |
| 2 · Charles Island (DF) | `charles-island.png` |
| 3 · Garret Hairtown (DF) | `garret-hairtown.png` |
| 4 · Arthur Sweet (DF) | `arthur-sweet.png` |
| 5 · Peter Mildred (DF) | `peter-mildred.png` |
| 6 · Josh Nathaniel (MF) | `josh-nathaniel.png` |
| 7 · Edward Gladstone (MF) | `edward-gladstone.png` |
| 8 · Tyler Thomas (MF) | `tyler-thomas.png` |
| 9 · Joseph Yosemite (MF) | `joseph-yosemite.png` |
| 10 · Ian Suffolk (FW) | `ian-suffolk.png` |
| 11 · Constant Builder (FW) | `constant-builder.png` |

### Emperadores Oscuros

Escudo: `emblems/ie2-dark-emperors.png`

| Jugador | Archivo |
|---|---|
| 1 · Thomas Feldt (GK) | `thomas-feldt.png` |
| 2 · Malcolm Night (DF) | `malcolm-night.png` |
| 3 · Sam Kincaid (MF) | `sam-kincaid.png` |
| 4 · Jim Wraith (DF) | `jim-wraith.png` |
| 5 · Tod Ironside (DF) | `tod-ironside.png` |
| 6 · Steve Grim (MF) | `steve-grim.png` |
| 7 · Tim Saunders (MF) | `tim-saunders.png` |
| 8 · Maxwell Carson (MF) | `maxwell-carson.png` |
| 9 · Shadow Cimmerian (FW) | `shadow-cimmerian.png` |
| 10 · Nathan Swift (FW) | `nathan-swift.png` |
| 11 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 12 · Godric Wyles (MF) | `godric-wyles.png` |

### Polvo de Diamantes

Escudo: `emblems/ie2-diamond-dust.png`

| Jugador | Archivo |
|---|---|
| 1 · Ben North (GK) | `ben-north.png` |
| 2 · Alan Downhill (DF) | `alan-downhill.png` |
| 3 · Claire Lesnow (DF) | `claire-lesnow.png` |
| 4 · Albert Denver (DF) | `albert-denver.png` |
| 5 · Lucy Hailstone (MF) | `lucy-hailstone.png` |
| 6 · Brad Coldwater (MF) | `brad-coldwater.png` |
| 7 · Dawson Foxx (MF) | `dawson-foxx.png` |
| 8 · Ving Rice (MF) | `ving-rice.png` |
| 9 · Bernie White (FW) | `bernie-white.png` |
| 10 · Bryce Whitingale (FW) | `bryce-whitingale.png` |
| 11 · Denzel Freezer (FW) | `denzel-freezer.png` |

### Épsilon Plus

Escudo: `emblems/ie2-epsilon-kai.png`

| Jugador | Archivo |
|---|---|
| 1 · Zeke Valanche (GK) | `zeke-valanche.png` |
| 2 · Craven Kenville (DF) | `craven-kenville.png` |
| 3 · Anna Mole (DF) | `anna-mole.png` |
| 4 · Kayson Wattever (DF) | `kayson-wattever.png` |
| 5 · Mike Tytan (DF) | `mike-tytan.png` |
| 6 · Mads Hatter (MF) | `mads-hatter.png` |
| 7 · Karen Ripton (MF) | `karen-ripton.png` |
| 8 · Yakker Plantsworm (MF) | `yakker-plantsworm.png` |
| 9 · Carrie McCuring (FW) | `carrie-mccuring.png` |
| 10 · Ronny Metcalf (MF) | `ronny-metcalf.png` |
| 11 · Dave Quagmire (FW) | `dave-quagmire.png` |
| 12 · Dave Quagmire (FW) | `dave-quagmire-desarm-cc.png` |

### Épsilon

Escudo: `emblems/ie2-epsilon.png`

| Jugador | Archivo |
|---|---|
| 1 · Dave Quagmire (GK) | `dave-quagmire.png` |
| 2 · Craven Kenville (DF) | `craven-kenville.png` |
| 3 · Anna Mole (DF) | `anna-mole.png` |
| 4 · Kayson Wattever (DF) | `kayson-wattever.png` |
| 5 · Mike Tytan (DF) | `mike-tytan.png` |
| 6 · Mads Hatter (MF) | `mads-hatter.png` |
| 7 · Karen Ripton (MF) | `karen-ripton.png` |
| 8 · Yakker Plantsworm (MF) | `yakker-plantsworm.png` |
| 9 · Carrie McCuring (FW) | `carrie-mccuring.png` |
| 10 · Ronny Metcalf (FW) | `ronny-metcalf.png` |
| 11 · Zeke Valanche (FW) | `zeke-valanche.png` |

### Tormenta de Géminis

Escudo: `emblems/ie2-gemini-storm.png`

| Jugador | Archivo |
|---|---|
| 1 · Gordon Star (GK) | `gordon-star.png` |
| 2 · Connor Shuttle (DF) | `connor-shuttle.png` |
| 3 · Jim Landing (DF) | `jim-landing.png` |
| 4 · Grant Icewater (DF) | `grant-icewater.png` |
| 5 · Charles Riverboat (DF) | `charles-riverboat.png` |
| 6 · Pat Box (MF) | `pat-box.png` |
| 7 · Gregory Saturn (MF) | `gregory-saturn.png` |
| 8 · Izzy Jupiter (MF) | `izzy-jupiter.png` |
| 9 · Rhona Countdown (FW) | `rhona-countdown.png` |
| 10 · Jordan Greenway (MF) | `jordan-greenway.png` |
| 11 · Dylan Bluemoon (FW) | `dylan-bluemoon.png` |

### Instituto Alpino

Escudo: `emblems/ie2-hakuren.png`

| Jugador | Archivo |
|---|---|
| 1 · Adam Ropes (GK) | `adam-ropes.png` |
| 2 · Joaquine Downtown (DF) | `joaquine-downtown.png` |
| 3 · Milton Bindings (DF) | `milton-bindings.png` |
| 4 · Spike Gleeson (DF) | `spike-gleeson.png` |
| 5 · Sean Snowfield (MF) | `sean-snowfield.png` |
| 6 · Kerry Bootgaiter (MF) | `kerry-bootgaiter.png` |
| 7 · Maddox Rock (MF) | `maddox-rock.png` |
| 8 · Robert Skipolson (MF) | `robert-skipolson.png` |
| 9 · Shawn Froste (FW) | `shawn-froste.png` |
| 10 · Roland Climbstein (FW) | `roland-climbstein.png` |
| 11 · Quentin Rackner (FW) | `quentin-rackner.png` |
| 12 · Trent Peggs (GK) | `trent-peggs.png` |
| 13 · Martin Ursus (DF) | `martin-ursus.png` |
| 14 · Pete Bogg (MF) | `pete-bogg.png` |
| 15 · Gem Strata (DF) | `gem-strata.png` |
| 16 · Horace Onlign (FW) | `horace-onlign.png` |

### Mar de Árboles

Escudo: `emblems/ie2-jukai-team.png`

| Jugador | Archivo |
|---|---|
| 1 · Cam Mando (GK) | `cam-mando.png` |
| 2 · Harry Boufante (DF) | `harry-boufante.png` |
| 3 · Todd Stuhl (DF) | `todd-stuhl.png` |
| 4 · Aspen Blewit (DF) | `aspen-blewit.png` |
| 5 · Marismus Oregon (DF) | `marismus-oregon.png` |
| 6 · Garjan Cypress (MF) | `garjan-cypress.png` |
| 7 · Judas Deathcap (MF) | `judas-deathcap.png` |
| 8 · Chase Faithfull (MF) | `chase-faithfull.png` |
| 9 · Chris Ticker (FW) | `chris-ticker.png` |
| 10 · Roy Daring (FW) | `roy-daring.png` |
| 11 · Scaber Enoki (FW) | `scaber-enoki.png` |

### Robots Guardias

Escudo: `emblems/ie2-keibi-machines.png`

| Jugador | Archivo |
|---|---|
| 1 · Robot S (GK) | `robot-s.png` |
| 2 · Robot P (DF) | `robot-p.png` |
| 3 · Robot T (DF) | `robot-t.png` |
| 4 · Robot V (DF) | `robot-v.png` |
| 5 · Robot C (DF) | `robot-c.png` |
| 6 · Robot O (MF) | `robot-o.png` |
| 7 · Robot B (MF) | `robot-b.png` |
| 8 · Robot G (MF) | `robot-g.png` |
| 9 · Robot K (FW) | `robot-k.png` |
| 10 · Robot F (FW) | `robot-f.png` |
| 11 · Robot L (FW) | `robot-l.png` |

### Instituto Claustro Sagrado

Escudo: `emblems/ie2-manyuuji.png`

| Jugador | Archivo |
|---|---|
| 1 · Crane Kik (GK) | `crane-kik.png` |
| 2 · Parry Waxon (DF) | `parry-waxon.png` |
| 3 · Bri Spark (DF) | `bri-spark.png` |
| 4 · Max Fortune (DF) | `max-fortune.png` |
| 5 · Brendan Water (DF) | `brendan-water.png` |
| 6 · Junior Fardream (MF) | `junior-fardream.png` |
| 7 · Ian Telektual (MF) | `ian-telektual.png` |
| 8 · Lee Dinglite (MF) | `lee-dinglite.png` |
| 9 · Marshall Artz (FW) | `marshall-artz.png` |
| 10 · Tyke Wando (FW) | `tyke-wando.png` |
| 11 · Dirk Artz (FW) | `dirk-artz.png` |
| 12 · Scott Banyan (DF) | `scott-banyan.png` |
| 13 · Earnest Bookworm (GK) | `earnest-bookworm.png` |
| 14 · Ollie Gami (DF) | `ollie-gami.png` |
| 15 · Roman Kandel (MF) | `roman-kandel.png` |
| 16 · Don Ation (FW) | `don-ation.png` |

### Triple C de Osaka

Escudo: `emblems/ie2-osaka-gals-ccc.png`

| Jugador | Archivo |
|---|---|
| 1 · Daisy Fields (GK) | `daisy-fields.png` |
| 2 · Alexia Sand (DF) | `alexia-sand.png` |
| 3 · Hellen Hearth (DF) | `hellen-hearth.png` |
| 4 · Rose Pinkpetal (DF) | `rose-pinkpetal.png` |
| 5 · Esther Greenland (DF) | `esther-greenland.png` |
| 6 · Bela Bluebells (MF) | `bela-bluebells.png` |
| 7 · Natalie Sunrise (MF) | `natalie-sunrise.png` |
| 8 · Hillary Bush (MF) | `hillary-bush.png` |
| 9 · Mary Moor (MF) | `mary-moor.png` |
| 10 · Lily Willow (FW) | `lily-willow.png` |
| 11 · Dell Closeout (GK) | `dell-closeout.png` |
| 12 · Amy Spires (DF) | `amy-spires.png` |
| 13 · Peony Cash (MF) | `peony-cash.png` |
| 14 · Gayle Revel (MF) | `gayle-revel.png` |
| 15 · Janine Brook (GK) | `janine-brook.png` |
| 16 · Sue's mum (GK) | `sue-s-mum.png` |

### Instituto Mary Times

Escudo: `emblems/ie2-oumihara.png`

| Jugador | Archivo |
|---|---|
| 1 · Rocky Black (GK) | `rocky-black.png` |
| 2 · Chad Taylor (DF) | `chad-taylor.png` |
| 3 · Victor Hills (DF) | `victor-hills.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 5 · Hector Redding (DF) | `hector-redding.png` |
| 6 · Mackenzie Fordline (MF) | `mackenzie-fordline.png` |
| 7 · Cadence Soundtown (MF) | `cadence-soundtown.png` |
| 8 · Dora Delight (MF) | `dora-delight.png` |
| 9 · Tom Contented (MF) | `tom-contented.png` |
| 10 · Joston Easton (FW) | `joston-easton.png` |
| 11 · Spring Millpond (FW) | `spring-millpond.png` |
| 12 · Gaston Cooley (GK) | `gaston-cooley.png` |
| 13 · Bevan Breakfast (DF) | `bevan-breakfast.png` |
| 14 · Jack Griddle (MF) | `jack-griddle.png` |
| 15 · Stan Andagi (MF) | `stan-andagi.png` |
| 16 · Coral Talent (FW) | `coral-talent.png` |

### Prominence

Escudo: `emblems/ie2-prominence.png`

| Jugador | Archivo |
|---|---|
| 1 · Grant Cook (GK) | `grant-cook.png` |
| 2 · Bonnie Sparks (DF) | `bonnie-sparks.png` |
| 3 · Val Flamewood (DF) | `val-flamewood.png` |
| 4 · Sean Ashford (DF) | `sean-ashford.png` |
| 5 · Ben Blowton (MF) | `ben-blowton.png` |
| 6 · Ethan Whitering (MF) | `ethan-whitering.png` |
| 7 · Brenda Firequest (MF) | `brenda-firequest.png` |
| 8 · Sam Bournes (MF) | `sam-bournes.png` |
| 9 · Jim Flareson (FW) | `jim-flareson.png` |
| 10 · Claude Beacons (FW) | `claude-beacons.png` |
| 11 · Nigel August (FW) | `nigel-august.png` |

### Raimon II

Escudo: `emblems/ie2-second-raimon.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 3 · Jack Wallside (DF) | `jack-wallside.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 5 · Darren LaChance (GK) | `darren-lachance.png` |
| 6 · Scott Banyan (DF) | `scott-banyan.png` |
| 6 · Scott Banyan (DF) | `scott-banyan-kogure-cc.png` |
| 7 · Suzette Hartland (FW) | `suzette-hartland.png` |
| 8 · Victoria Vanguard (MF) | `victoria-vanguard.png` |
| 9 · Shawn Froste (FW) | `shawn-froste-fubuki-cc.png` |
| 9 · Shawn Froste (DF) | `shawn-froste.png` |
| 9 · Shawn Froste (FW) | `shawn-froste-fubuki.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 12 · William Glass (FW) | `william-glass.png` |
| 13 · Bobby Shearer (DF) | `bobby-shearer.png` |
| 14 · Jude Sharp (MF) | `jude-sharp.png` |
| 16 · Erik Eagle (MF) | `erik-eagle.png` |
| 76 · Eugene Conwell (FW) | `eugene-conwell.png` |

### Royal Academy Redux

Escudo: `emblems/ie2-shin-teikoku-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Joseph King (GK) | `joseph-king.png` |
| 2 · Rowan Beltzer (DF) | `rowan-beltzer.png` |
| 3 · Blade Healen (DF) | `blade-healen.png` |
| 4 · Argie Bargie (DF) | `argie-bargie.png` |
| 5 · Lee Bamboo (DF) | `lee-bamboo.png` |
| 6 · Eton Messer (MF) | `eton-messer.png` |
| 7 · Jonah Spark (MF) | `jonah-spark.png` |
| 8 · Sue Sparrow (MF) | `sue-sparrow.png` |
| 9 · Riley Jamm (FW) | `riley-jamm.png` |
| 10 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 11 · David Samford (FW) | `david-samford.png` |
| 12 · Jimbo Cellar (GK) | `jimbo-cellar.png` |
| 13 · Zenn Wildhorse (FW) | `zenn-wildhorse.png` |
| 14 · Dawson Little (DF) | `dawson-little.png` |
| 15 · Cosimo Beck (MF) | `cosimo-beck.png` |
| 16 · Maston Color (MF) | `maston-color.png` |

### Servicio Secreto

Escudo: `emblems/ie2-sp-fixers.png`

| Jugador | Archivo |
|---|---|
| 1 · Ken Ironwall (GK) | `ken-ironwall.png` |
| 2 · Timothy Western (DF) | `timothy-western.png` |
| 3 · Wallace Hammond (DF) | `wallace-hammond.png` |
| 4 · Shirley Stevens (DF) | `shirley-stevens.png` |
| 5 · Ian Smith (DF) | `ian-smith.png` |
| 6 · Taylor Firepool (MF) | `taylor-firepool.png` |
| 7 · Marge Fielding (MF) | `marge-fielding.png` |
| 8 · Marshall Firsthand (MF) | `marshall-firsthand.png` |
| 9 · Holly Mirror (FW) | `holly-mirror.png` |
| 10 · Victoria Vanguard (MF) | `victoria-vanguard.png` |
| 11 · Joe Kenneddy (FW) | `joe-kenneddy.png` |
| 12 · Ian Sights (GK) | `ian-sights.png` |
| 13 · Greene Beray (DF) | `greene-beray.png` |
| 14 · Ryan Tappin (MF) | `ryan-tappin.png` |
| 15 · Linda Shadey (FW) | `linda-shadey.png` |
| 16 · Sid Safehouse (DF) | `sid-safehouse.png` |

### Génesis

Escudo: `emblems/ie2-the-genesis.png`

| Jugador | Archivo |
|---|---|
| 1 · Nelson Rockwell (GK) | `nelson-rockwell.png` |
| 2 · Gail Baker (DF) | `gail-baker.png` |
| 3 · Kim Powell (DF) | `kim-powell.png` |
| 4 · Zack Cummings (DF) | `zack-cummings.png` |
| 5 · Hunt Mercer (DF) | `hunt-mercer.png` |
| 6 · Connor Murray (MF) | `connor-murray.png` |
| 7 · Katie Brown (MF) | `katie-brown.png` |
| 8 · Ashton Malone (MF) | `ashton-malone.png` |
| 9 · Wilbur Watkins (FW) | `wilbur-watkins.png` |
| 10 · Isabelle Trick (MF) | `isabelle-trick.png` |
| 11 · Xavier Foster (FW) | `xavier-foster.png` |

### Instituto Fauxshore

Escudo: `emblems/ie2-yokato.png`

| Jugador | Archivo |
|---|---|
| 1 · Darren LaChance (GK) | `darren-lachance.png` |
| 2 · Drancis Fake (DF) | `drancis-fake.png` |
| 3 · Mick Mishap (DF) | `mick-mishap.png` |
| 4 · Louis Leave (DF) | `louis-leave.png` |
| 5 · Maurice Badgame (DF) | `maurice-badgame.png` |
| 6 · Cannon Random (MF) | `cannon-random.png` |
| 7 · Ulric Richmen (MF) | `ulric-richmen.png` |
| 8 · Dany Destiny (DF) | `dany-destiny.png` |
| 8 · Dave Fate (FW) | `dave-fate.png` |
| 9 · Spencer Duskplay (MF) | `spencer-duskplay.png` |
| 10 · Jonathan Luckyman (FW) | `jonathan-luckyman.png` |
| 11 · Joe Poker (FW) | `joe-poker.png` |
| 12 · Wiley Cracker (GK) | `wiley-cracker.png` |
| 13 · Mark Failing (FW) | `mark-failing.png` |
| 14 · Alton Cotts (MF) | `alton-cotts.png` |
| 15 · Mike Passing (FW) | `mike-passing.png` |
| 16 · Knowle Bathers (GK) | `knowle-bathers.png` |

### Jóvenes Inazuma

Escudo: `emblems/ie2-young-inazuma.png`

| Jugador | Archivo |
|---|---|
| 1 · Seymour Hillman (GK) | `seymour-hillman.png` |
| 2 · Charles Island (DF) | `charles-island.png` |
| 3 · Garret Hairtown (DF) | `garret-hairtown.png` |
| 4 · Arthur Sweet (DF) | `arthur-sweet.png` |
| 5 · Peter Mildred (MF) | `peter-mildred.png` |
| 6 · Josh Nathaniel (MF) | `josh-nathaniel.png` |
| 7 · Edward Gladstone (MF) | `edward-gladstone.png` |
| 8 · Tyler Thomas (MF) | `tyler-thomas.png` |
| 9 · Joseph Yosemite (FW) | `joseph-yosemite.png` |
| 10 · Ian Suffolk (MF) | `ian-suffolk.png` |
| 11 · Constant Builder (FW) | `constant-builder.png` |
| 12 · David Evans (GK) | `david-evans.png` |

### Big Waves

Escudo: `emblems/ie3-big-waves.png`

| Jugador | Archivo |
|---|---|
| 1 · Gene Whalon (GK) | `gene-whalon.png` |
| 2 · David Waterman (DF) | `david-waterman.png` |
| 3 · Sonny Shore (DF) | `sonny-shore.png` |
| 4 · Kjell Snapper (DF) | `kjell-snapper.png` |
| 5 · Ken Crackham (DF) | `ken-crackham.png` |
| 6 · Shawn Princeton (MF) | `shawn-princeton.png` |
| 7 · Matt Fischer (MF) | `matt-fischer.png` |
| 8 · Hank Tennyson (MF) | `hank-tennyson.png` |
| 9 · Dolph Hensen (MF) | `dolph-hensen.png` |
| 10 · Hamilton Reith (FW) | `hamilton-reith.png` |
| 11 · Joe Dawes (FW) | `joe-dawes.png` |
| 12 · Quincy Horace (GK) | `quincy-horace.png` |
| 13 · Holly Summers (MF) | `holly-summers.png` |
| 14 · Derek Rabson (MF) | `derek-rabson.png` |
| 15 · Barack Daniels (DF) | `barack-daniels.png` |
| 16 · Bruce Marlin (FW) | `bruce-marlin.png` |

### Brocken Brigade

Escudo: `emblems/ie3-brockenborg.png`

| Jugador | Archivo |
|---|---|
| 1 · Thorsten Welger (GK) | `thorsten-welger.png` |
| 2 · Alexander Hausen (DF) | `alexander-hausen.png` |
| 3 · Heinrich Farber (DF) | `heinrich-farber.png` |
| 4 · Kurt Zawel (DF) | `kurt-zawel.png` |
| 5 · Lukas Schmidt (DF) | `lukas-schmidt.png` |
| 6 · Theodor Ulrich (MF) | `theodor-ulrich.png` |
| 7 · Jan Oster (MF) | `jan-oster.png` |
| 8 · Niklas Kuster (MF) | `niklas-kuster.png` |
| 9 · Jonas Polk (MF) | `jonas-polk.png` |
| 10 · Maximilian Müller (FW) | `maximilian-m-ller.png` |
| 11 · Peter Naumann (FW) | `peter-naumann.png` |
| 12 · Gerhard Enders (GK) | `gerhard-enders.png` |
| 13 · Erwin Völz (FW) | `erwin-v-lz.png` |
| 14 · Jens Hoffman (FW) | `jens-hoffman.png` |
| 15 · Ernst Fliedner (MF) | `ernst-fliedner.png` |
| 16 · Emmanuel Ewerz (DF) | `emmanuel-ewerz.png` |

### Leones del Desierto

Escudo: `emblems/ie3-desert-lion.png`

| Jugador | Archivo |
|---|---|
| 1 · Nasir Mustafa (GK) | `nasir-mustafa.png` |
| 2 · Faraz Farooq (DF) | `faraz-farooq.png` |
| 3 · Bilal Kalil (DF) | `bilal-kalil.png` |
| 4 · Jamila Wali (DF) | `jamila-wali.png` |
| 5 · Musa Sylla (DF) | `musa-sylla.png` |
| 6 · Yusuf Massoud (MF) | `yusuf-massoud.png` |
| 7 · Sulayk Sulaiman (MF) | `sulayk-sulaiman.png` |
| 8 · Sayid Armand (MF) | `sayid-armand.png` |
| 9 · Mansur Jasim (MF) | `mansur-jasim.png` |
| 10 · Zack Abdulla (FW) | `zack-abdulla.png` |
| 11 · Majdi Ismail (FW) | `majdi-ismail.png` |
| 12 · Talal Hamad (GK) | `talal-hamad.png` |
| 13 · Hasan Ahmed (DF) | `hasan-ahmed.png` |
| 14 · Khalfan Jibril (DF) | `khalfan-jibril.png` |
| 15 · Rajab Ismail (MF) | `rajab-ismail.png` |
| 16 · Adel Siddique (FW) | `adel-siddique.png` |

### Dragones de Fuego

Escudo: `emblems/ie3-fire-dragon.png`

| Jugador | Archivo |
|---|---|
| 1 · Jeongsu Cho (GK) | `jeongsu-cho.png` |
| 2 · Umi Hwang (DF) | `umi-hwang.png` |
| 3 · Dooyoon Hong (DF) | `dooyoon-hong.png` |
| 4 · Minho Cho (DF) | `minho-cho.png` |
| 5 · Songhwan Ko (DF) | `songhwan-ko.png` |
| 6 · Paekyeong Park (MF) | `paekyeong-park.png` |
| 7 · Changsu Choi (MF) | `changsu-choi.png` |
| 8 · Eunyeong Kim (MF) | `eunyeong-kim.png` |
| 9 · Byron Love (MF) | `byron-love.png` |
| 10 · Claude Beacons (FW) | `claude-beacons.png` |
| 11 · Bryce Whitingale (FW) | `bryce-whitingale.png` |
| 12 · Chi-Won Ho (GK) | `chi-won-ho.png` |
| 13 · Dong-Hyun Seul (DF) | `dong-hyun-seul.png` |
| 14 · Jung-Hoon Yi (MF) | `jung-hoon-yi.png` |
| 15 · Sung-Jin Noh (FW) | `sung-jin-noh.png` |
| 16 · Joon-Ho Ja (MF) | `joon-ho-ja.png` |

### Inazuma Japón

Escudo: `emblems/ie3-inazuma-japan.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Nathan Swift (DF) | `nathan-swift.png` |
| 3 · Jack Wallside (DF) | `jack-wallside.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 6 · Scott Banyan (DF) | `scott-banyan.png` |
| 7 · Archer Hawkins (DF) | `archer-hawkins.png` |
| 8 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 9 · Shawn Froste (FW) | `shawn-froste.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 11 · Austin Hobbes (FW) | `austin-hobbes.png` |
| 12 · Thor Stoutberg (MF) | `thor-stoutberg.png` |
| 14 · Jude Sharp (MF) | `jude-sharp.png` |
| 16 · David Samford (FW) | `david-samford.png` |
| 17 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 18 · Xavier Foster (FW) | `xavier-foster.png` |
| 20 · Darren LaChance (GK) | `darren-lachance.png` |

### Knights of Queen

Escudo: `emblems/ie3-knights-of-queen.png`

| Jugador | Archivo |
|---|---|
| 1 · Freddy McQueen (GK) | `freddy-mcqueen.png` |
| 2 · Jonny Gascoigne (DF) | `jonny-gascoigne.png` |
| 3 · David Buckingham (DF) | `david-buckingham.png` |
| 4 · Lance Rawton (DF) | `lance-rawton.png` |
| 5 · Edge Ripper (DF) | `edge-ripper.png` |
| 6 · Peter Cole (MF) | `peter-cole.png` |
| 7 · Gary Mane (MF) | `gary-mane.png` |
| 8 · Paul Appleton (MF) | `paul-appleton.png` |
| 9 · Eric Purpleton (MF) | `eric-purpleton.png` |
| 10 · Edgar Partinus (FW) | `edgar-partinus.png` |
| 11 · Phillip Owen (FW) | `phillip-owen.png` |
| 12 · Servilius Jeeves (GK) | `servilius-jeeves.png` |
| 13 · Martin Squall (DF) | `martin-squall.png` |
| 14 · Nick Woodgate (FW) | `nick-woodgate.png` |
| 15 · Mikey Richards (MF) | `mikey-richards.png` |
| 16 · Sirius Pounding (MF) | `sirius-pounding.png` |

### Los Pequeños Gigantes

Escudo: `emblems/ie3-little-gigant.png`

| Jugador | Archivo |
|---|---|
| 1 · Hector Helio (GK) | `hector-helio.png` |
| 2 · Zephyr Vitesse (DF) | `zephyr-vitesse.png` |
| 3 · Walter Mountain (DF) | `walter-mountain.png` |
| 4 · Jimi Gaines (DF) | `jimi-gaines.png` |
| 5 · Ian Ferrum (DF) | `ian-ferrum.png` |
| 6 · Quint Hampton (MF) | `quint-hampton.png` |
| 7 · Yasir Haddad (MF) | `yasir-haddad.png` |
| 8 · Keith Ryan (MF) | `keith-ryan.png` |
| 9 · Maximino Cruz (MF) | `maximino-cruz.png` |
| 10 · Gareth Flare (FW) | `gareth-flare.png` |
| 11 · Drago Hill (FW) | `drago-hill.png` |
| 12 · Keenan DiFortune (GK) | `keenan-difortune.png` |
| 13 · Jarell Mangrove (DF) | `jarell-mangrove.png` |
| 14 · Vic Vitrum (MF) | `vic-vitrum.png` |
| 15 · Li Leung (MF) | `li-leung.png` |
| 16 · Jazzy Hedgeer (FW) | `jazzy-hedgeer.png` |

### Dark Team

Escudo: `emblems/ie3-makai-gundan-z.png`

| Jugador | Archivo |
|---|---|
| 1 · Astaroth (GK) | `astaroth.png` |
| 2 · Bael (DF) | `bael.png` |
| 3 · Abigor (DF) | `abigor.png` |
| 4 · Behemoth (DF) | `behemoth.png` |
| 5 · Belial (DF) | `belial.png` |
| 6 · Malphas (MF) | `malphas.png` |
| 7 · Glasya (MF) | `glasya.png` |
| 8 · Arachne (MF) | `arachne.png` |
| 9 · Jezebeth (MF) | `jezebeth.png` |
| 10 · Thanatos (FW) | `thanatos.png` |
| 11 · Destra (FW) | `destra.png` |

### Neo Japón

Escudo: `emblems/ie3-neo-japan.png`

| Jugador | Archivo |
|---|---|
| 1 · Joseph King (GK) | `joseph-king.png` |
| 2 · Alan Master (MF) | `alan-master.png` |
| 3 · Zack Cummings (DF) | `zack-cummings.png` |
| 4 · Argie Bargie (DF) | `argie-bargie.png` |
| 5 · Daniel Hatch (FW) | `daniel-hatch.png` |
| 6 · Neil Turner (FW) | `neil-turner.png` |
| 7 · Sail Bluesea (FW) | `sail-bluesea.png` |
| 8 · Johan Tassman (FW) | `johan-tassman.png` |
| 9 · Wilbur Watkins (FW) | `wilbur-watkins.png` |
| 10 · Dave Quagmire (MF) | `dave-quagmire.png` |
| 11 · Zeke Valanche (FW) | `zeke-valanche.png` |
| 12 · Ethan Whitering (MF) | `ethan-whitering.png` |
| 13 · Henry House (MF) | `henry-house.png` |
| 14 · Tyler Murdock (FW) | `tyler-murdock.png` |
| 15 · Jonas Demetrius (FW) | `jonas-demetrius.png` |
| 16 · Mark Hillvalley (DF) | `mark-hillvalley.png` |

### Equipo Ogro

Escudo: `emblems/ie3-ogre.png`

| Jugador | Archivo |
|---|---|
| 1 · Lars Luceafăr (GK) | `lars-luceaf-r.png` |
| 2 · Lump Trungus (DF) | `lump-trungus.png` |
| 3 · Bump Trungus (DF) | `bump-trungus.png` |
| 4 · Radd Ischer (DF) | `radd-ischer.png` |
| 5 · Jynx Jenkins (DF) | `jynx-jenkins.png` |
| 6 · Oni Triumvir (MF) | `oni-triumvir.png` |
| 7 · Drachen Gunther (MF) | `drachen-gunther.png` |
| 8 · Ichabod Stark (MF) | `ichabod-stark.png` |
| 9 · Escavan Malice (FW) | `escavan-malice.png` |
| 10 · Bash Lancer (FW) | `bash-lancer.png` |
| 11 · Mystral Callous (FW) | `mystral-callous.png` |

### Orfeo

Escudo: `emblems/ie3-orpheus.png`

| Jugador | Archivo |
|---|---|
| 1 · Gigi Blasi (GK) | `gigi-blasi.png` |
| 2 · Vento Galliano (DF) | `vento-galliano.png` |
| 3 · Otto Nobili (DF) | `otto-nobili.png` |
| 4 · Anton Graziuso (DF) | `anton-graziuso.png` |
| 5 · Marco Maserati (DF) | `marco-maserati.png` |
| 6 · Angelo Gabrini (MF) | `angelo-gabrini.png` |
| 7 · Hidetoshi Nakata (MF) | `hidetoshi-nakata.png` |
| 8 · Giorgio Giannini (MF) | `giorgio-giannini.png` |
| 9 · Dante Diavolo (MF) | `dante-diavolo.png` |
| 10 · Paolo Bianchi (FW) | `paolo-bianchi.png` |
| 11 · Raffaele Generani (FW) | `raffaele-generani.png` |
| 12 · Daniele Sanctis (GK) | `daniele-sanctis.png` |
| 13 · o (MF) | `o.png` |
| 14 · Alessandro Rossa (MF) | `alessandro-rossa.png` |
| 15 · Giuseppe Cannavaro (DF) | `giuseppe-cannavaro.png` |
| 16 · Gianluca Zanardi (MF) | `gianluca-zanardi.png` |

### Mega Inazuma Eleven

Escudo: `emblems/ie3-real-inazuma.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Nathan Swift (DF) | `nathan-swift.png` |
| 3 · Jack Wallside (DF) | `jack-wallside.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 5 · Scott Banyan (DF) | `scott-banyan.png` |
| 6 · Thor Stoutberg (MF) | `thor-stoutberg.png` |
| 7 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 9 · Shawn Froste (FW) | `shawn-froste.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 11 · Austin Hobbes (FW) | `austin-hobbes.png` |
| 12 · Darren LaChance (GK) | `darren-lachance.png` |
| 13 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 14 · Jude Sharp (MF) | `jude-sharp.png` |
| 15 · Archer Hawkins (DF) | `archer-hawkins.png` |
| 16 · David Samford (FW) | `david-samford.png` |
| 20 · Xavier Foster (FW) | `xavier-foster.png` |

### Los Rojos

Escudo: `emblems/ie3-red-matador.png`

| Jugador | Archivo |
|---|---|
| 1 · Fermín Sánchez (GK) | `ferm-n-s-nchez.png` |
| 2 · José Costa (DF) | `jos-costa.png` |
| 3 · José López (DF) | `jos-l-pez.png` |
| 4 · Antonio Gallego (DF) | `antonio-gallego.png` |
| 5 · Queraldo Naval (DF) | `queraldo-naval.png` |
| 6 · Juan Nadal (MF) | `juan-nadal.png` |
| 7 · Igor Ferreira (MF) | `igor-ferreira.png` |
| 8 · Miguel Pereira (MF) | `miguel-pereira.png` |
| 9 · Pedro Moreno (MF) | `pedro-moreno.png` |
| 10 · Samuel Mayo (FW) | `samuel-mayo.png` |
| 11 · Davi Peroqué (FW) | `davi-peroqu.png` |
| 12 · Juan Espindola (GK) | `juan-espindola.png` |
| 13 · Isaac César (FW) | `isaac-c-sar.png` |
| 14 · Laudelino Castor (DF) | `laudelino-castor.png` |
| 15 · Carlos Arroyo (MF) | `carlos-arroyo.png` |
| 16 · Federico Rubiera (FW) | `federico-rubiera.png` |

### Grifos de la Rosa

Escudo: `emblems/ie3-rose-griffon.png`

| Jugador | Archivo |
|---|---|
| 1 · Roger Pialat (GK) | `roger-pialat.png` |
| 2 · Pierre Godin (DF) | `pierre-godin.png` |
| 3 · Michaël Aron (DF) | `micha-l-aron.png` |
| 4 · Francis Poujol (DF) | `francis-poujol.png` |
| 5 · Kevin Pinot (DF) | `kevin-pinot.png` |
| 6 · Roland Pérec (MF) | `roland-p-rec.png` |
| 7 · Romuald Huysmans (MF) | `romuald-huysmans.png` |
| 8 · Stéphane Hinault (MF) | `st-phane-hinault.png` |
| 9 · Julien Rousseau (MF) | `julien-rousseau.png` |
| 10 · Jérôme Hervaud (FW) | `j-r-me-hervaud.png` |
| 11 · Alain Favreau (FW) | `alain-favreau.png` |
| 12 · Émile Lazare (GK) | `mile-lazare.png` |
| 13 · André Pinson (DF) | `andr-pinson.png` |
| 14 · Jean Gutain (DF) | `jean-gutain.png` |
| 15 · Claude Moreau (MF) | `claude-moreau.png` |
| 16 · Michel Morland (FW) | `michel-morland.png` |

### Zoolan Team

Escudo: `emblems/ie3-team-garshield.png`

| Jugador | Archivo |
|---|---|
| 1 · Cyril Fox (GK) | `cyril-fox.png` |
| 2 · Jacques Allemand (DF) | `jacques-allemand.png` |
| 3 · Phil A. Minion (DF) | `phil-a-minion.png` |
| 4 · Buddy Plains (DF) | `buddy-plains.png` |
| 5 · Dean Goddard (DF) | `dean-goddard.png` |
| 6 · Cecil Crowley (MF) | `cecil-crowley.png` |
| 7 · Seth Hedges (MF) | `seth-hedges.png` |
| 8 · Niccolo Mantegna (MF) | `niccolo-mantegna.png` |
| 9 · Damien Crawford (MF) | `damien-crawford.png` |
| 10 · Avinash Chowdhury (FW) | `avinash-chowdhury.png` |
| 11 · Sedgley Scofield (FW) | `sedgley-scofield.png` |
| 12 · Grizzler Bruin (GK) | `grizzler-bruin.png` |
| 13 · Ian C. Wincy (DF) | `ian-c-wincy.png` |
| 14 · Bandy Horsman (MF) | `bandy-horsman.png` |
| 15 · Ali Caiman (FW) | `ali-caiman.png` |
| 16 · Chris Ellis (DF) | `chris-ellis.png` |

### Equipo D

Escudo: `emblems/ie3-team-k.png`

| Jugador | Archivo |
|---|---|
| 1 · Indigo Lazuli (GK) | `indigo-lazuli.png` |
| 2 · Roseo Diamante (DF) | `roseo-diamante.png` |
| 3 · Azubel Turchese (DF) | `azubel-turchese.png` |
| 4 · Nello Agata (DF) | `nello-agata.png` |
| 5 · Azzurro Zaffiro (DF) | `azzurro-zaffiro.png` |
| 6 · Beldio Smeraldo (MF) | `beldio-smeraldo.png` |
| 7 · Rosso Granato (MF) | `rosso-granato.png` |
| 8 · Giallo Topazio (MF) | `giallo-topazio.png` |
| 9 · Violetto Ametista (FW) | `violetto-ametista.png` |
| 10 · Giulio Acuto (MF) | `giulio-acuto.png` |
| 11 · Bianco Perla (FW) | `bianco-perla.png` |
| 12 · Grigio Quarzo (GK) | `grigio-quarzo.png` |
| 13 · Pardo Berillo (DF) | `pardo-berillo.png` |
| 14 · Marrone Corniola (MF) | `marrone-corniola.png` |
| 15 · Amaranto Rubino (MF) | `amaranto-rubino.png` |
| 16 · Avorio Opale (FW) | `avorio-opale.png` |

### Sky Team

Escudo: `emblems/ie3-tenkuu-no-shito.png`

| Jugador | Archivo |
|---|---|
| 1 · Anorel (GK) | `anorel.png` |
| 2 · Nenel (DF) | `nenel.png` |
| 3 · Genel (DF) | `genel.png` |
| 4 · Ekadel (DF) | `ekadel.png` |
| 5 · Lephiel (DF) | `lephiel.png` |
| 6 · Sachinel (MF) | `sachinel.png` |
| 7 · Wenel (MF) | `wenel.png` |
| 8 · Nuel (MF) | `nuel.png` |
| 9 · Ientel (MF) | `ientel.png` |
| 10 · Gaiel (FW) | `gaiel.png` |
| 11 · Sanctus (FW) | `sanctus.png` |

### Los Emperadores

Escudo: `emblems/ie3-the-empire.png`

| Jugador | Archivo |
|---|---|
| 1 · Jorge Ortega (GK) | `jorge-ortega.png` |
| 2 · Thiago Torres (DF) | `thiago-torres.png` |
| 3 · Julio Acosta (DF) | `julio-acosta.png` |
| 4 · Grande Díaz (DF) | `grande-d-az.png` |
| 5 · Ramón Martínez (DF) | `ram-n-mart-nez.png` |
| 6 · Esteban Carlos (MF) | `esteban-carlos.png` |
| 7 · Sergio Pérez (MF) | `sergio-p-rez.png` |
| 8 · Roberto Torres (MF) | `roberto-torres.png` |
| 9 · Pablo Castillo (MF) | `pablo-castillo.png` |
| 10 · Leone Badigo (FW) | `leone-badigo.png` |
| 11 · Diego Oro (FW) | `diego-oro.png` |
| 12 · Lionel Cruz (GK) | `lionel-cruz.png` |
| 13 · Mario Saviola (FW) | `mario-saviola.png` |
| 14 · Hernán Tévez (DF) | `hern-n-t-vez.png` |
| 15 · Herman Samuel (MF) | `herman-samuel.png` |
| 16 · Ricardo Agüero (FW) | `ricardo-ag-ero.png` |

### Caimanes del Cabo

Escudo: `emblems/ie3-the-great-horn.png`

| Jugador | Archivo |
|---|---|
| 1 · Zolani Baloi (GK) | `zolani-baloi.png` |
| 2 · Dakarai Furman (DF) | `dakarai-furman.png` |
| 3 · Jake Fana (DF) | `jake-fana.png` |
| 4 · Masego Molelo (DF) | `masego-molelo.png` |
| 5 · Cassius Tobler (DF) | `cassius-tobler.png` |
| 6 · Anton Nortje (MF) | `anton-nortje.png` |
| 7 · Adam Marunga (MF) | `adam-marunga.png` |
| 8 · Siyabonga Mahlangu (MF) | `siyabonga-mahlangu.png` |
| 9 · Reggie Ines (MF) | `reggie-ines.png` |
| 10 · Nathan Tswane (FW) | `nathan-tswane.png` |
| 11 · Melisizwe Zamani (FW) | `melisizwe-zamani.png` |
| 12 · Kennedy McCarthy (DF) | `kennedy-mccarthy.png` |
| 13 · Moeneeb Booysen (DF) | `moeneeb-booysen.png` |
| 14 · Herschel De Villiers (FW) | `herschel-de-villiers.png` |
| 15 · Hugh Makebe (GK) | `hugh-makebe.png` |
| 16 · Themba Sepeng (MF) | `themba-sepeng.png` |

### Os Reis

Escudo: `emblems/ie3-the-kingdom.png`

| Jugador | Archivo |
|---|---|
| 1 · Falcão Da Silva (GK) | `falc-o-da-silva.png` |
| 2 · Carlos Lagarto (DF) | `carlos-lagarto.png` |
| 3 · Antonio Bagre (DF) | `antonio-bagre.png` |
| 4 · Monstro Ximenes (DF) | `monstro-ximenes.png` |
| 5 · Formiga Clemens (DF) | `formiga-clemens.png` |
| 6 · Presa Passos (MF) | `presa-passos.png` |
| 7 · Borboleta Barboza (MF) | `borboleta-barboza.png` |
| 8 · Coruja Cerezo (MF) | `coruja-cerezo.png` |
| 9 · Leonardo Almeida (MF) | `leonardo-almeida.png` |
| 10 · Mac Robingo (FW) | `mac-robingo.png` |
| 11 · Gato Carvalho (FW) | `gato-carvalho.png` |
| 12 · Xavier Ribeiro (GK) | `xavier-ribeiro.png` |
| 13 · Ulisses Nogueira (DF) | `ulisses-nogueira.png` |
| 14 · Gervasio Oliveira (DF) | `gervasio-oliveira.png` |
| 15 · Tigre Mendes (MF) | `tigre-mendes.png` |
| 16 · Grillo Santos (FW) | `grillo-santos.png` |

### Unicorn

Escudo: `emblems/ie3-unicorn.png`

| Jugador | Archivo |
|---|---|
| 1 · Billy Dash (GK) | `billy-dash.png` |
| 2 · Ted Bryant (DF) | `ted-bryant.png` |
| 3 · Tony Strider (DF) | `tony-strider.png` |
| 4 · Drake Dynamo (DF) | `drake-dynamo.png` |
| 5 · Bobby Shearer (DF) | `bobby-shearer.png` |
| 6 · Steve Woodmark (MF) | `steve-woodmark.png` |
| 7 · Erik Eagle (MF) | `erik-eagle.png` |
| 8 · Shane Pierce (MF) | `shane-pierce.png` |
| 9 · Mark Krueger (MF) | `mark-krueger.png` |
| 10 · Dylan Keats (FW) | `dylan-keats.png` |
| 11 · Gabriel Jax (FW) | `gabriel-jax.png` |
| 12 · Alex Hawke (GK) | `alex-hawke.png` |
| 13 · Corey Washington (DF) | `corey-washington.png` |
| 14 · Bob Bobbins (DF) | `bob-bobbins.png` |
| 15 · Petie Pooma (MF) | `petie-pooma.png` |
| 16 · Norbert Poindexter (FW) | `norbert-poindexter.png` |
