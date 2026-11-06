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

### Barcelona Orb

Escudo: `emblems/ares-barcelona-orb.png`

| Jugador | Archivo |
|---|---|
| 1 · Salvador Castell (GK) | `salvador-castell.png` |
| 2 · Antoni Valls (DF) | `antoni-valls.png` |
| 3 · Jordi Belloch (DF) | `jordi-belloch.png` |
| 4 · Gerard Carbonell (DF) | `gerard-carbonell.png` |
| 5 · Carles Ripoll (DF) | `carles-ripoll.png` |
| 6 · Josep Anglesola (MF) | `josep-anglesola.png` |
| 7 · Xavi Casals (MF) | `xavi-casals.png` |
| 8 · Ronaldo Ramallets (MF) | `ronaldo-ramallets.png` |
| 9 · Leo Segarra (FW) | `leo-segarra.png` |
| 10 · Sergi Hernández (MF) | `sergi-hern-ndez.png` |
| 11 · Joan Asensi (FW) | `joan-asensi.png` |
| 12 · Augusto Gomez (MF) | `augusto-gomez.png` |
| 13 · Geraldo Enrique (FW) | `geraldo-enrique.png` |
| 14 · Alessio Ganonti (MF) | `alessio-ganonti.png` |

### Academia Alia

Escudo: `emblems/ares-eisei-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Dave Quagmire (GK) | `dave-quagmire.png` |
| 2 · Grant Icewater (DF) | `grant-icewater.png` |
| 3 · Claire Lesnow (DF) | `claire-lesnow.png` |
| 4 · Jordan Greenway (MF) | `jordan-greenway.png` |
| 5 · Ben Blowton (MF) | `ben-blowton.png` |
| 6 · Isabelle Trick (MF) | `isabelle-trick.png` |
| 7 · Nigel August (FW) | `nigel-august.png` |
| 8 · Claude Beacons (FW) | `claude-beacons.png` |
| 9 · Bryce Whitingale (FW) | `bryce-whitingale.png` |
| 10 · Xavier Foster (FW) | `xavier-foster.png` |
| 11 · Xavier Schiller (FW) | `xavier-schiller.png` |
| 12 · Ronny Metcalf (MF) | `ronny-metcalf.png` |
| 13 · Zeke Valanche (FW) | `zeke-valanche.png` |
| 14 · Bonnie Sparks (DF) | `bonnie-sparks.png` |
| 15 · Aquilina Schiller (MF) | `aquilina-schiller.png` |

### Instituto Alpino (Ares)

Escudo: `emblems/ares-hakuren-ares.png`

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
| 10 · Aiden Froste (FW) | `aiden-froste.png` |
| 11 · Quentin Rackner (FW) | `quentin-rackner.png` |
| 12 · Roland Climbstein (FW) | `roland-climbstein.png` |
| 15 · Robert Cottontail (GK) | `robert-cottontail.png` |
| 16 · Mila Simmering (MF) | `mila-simmering.png` |
| 17 · Bunny Cottontail (FW) | `bunny-cottontail.png` |
| 19 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |

### Raimon Isla Remota

Escudo: `emblems/ares-inakuni-raimon.png`

| Jugador | Archivo |
|---|---|
| 1 · Sandra Fischer (GK) | `sandra-fischer.png` |
| 2 · Kiko Calavento (DF) | `kiko-calavento.png` |
| 3 · Trevor Cook (DF) | `trevor-cook.png` |
| 4 · Nino Nango (MF) | `nino-nango.png` |
| 5 · Cliff Parker (DF) | `cliff-parker.png` |
| 6 · Maxime Dassier (MF) | `maxime-dassier.png` |
| 7 · Valentin Eisner (MF) | `valentin-eisner.png` |
| 8 · César Montalbán (MF) | `c-sar-montalb-n.png` |
| 9 · Adriano Donati (FW) | `adriano-donati.png` |
| 10 · Sonny Wright (FW) | `sonny-wright.png` |
| 11 · Basile Hardy (FW) | `basile-hardy.png` |
| 12 · Rolland Bowlby (GK) | `rolland-bowlby.png` |
| 13 · Mister Yi (FW) | `mister-yi.png` |
| 14 · Dean Rush (MF) | `dean-rush.png` |
| 15 · Regina Mulgrave (GK) | `regina-mulgrave.png` |
| 16 · Aurelia Dingle (MF) | `aurelia-dingle.png` |

### Instituto Kirkwood (Ares)

Escudo: `emblems/ares-kidokawa-seishuu-ares.png`

| Jugador | Archivo |
|---|---|
| 1 · Trice Topper (GK) | `trice-topper.png` |
| 2 · Malcolm Night (DF) | `malcolm-night.png` |
| 3 · Alfred Meenan (DF) | `alfred-meenan.png` |
| 4 · Dan Mirthful (DF) | `dan-mirthful.png` |
| 5 · Ricky Clover (DF) | `ricky-clover.png` |
| 6 · Toby Damian (MF) | `toby-damian.png` |
| 7 · York Nashmith (MF) | `york-nashmith.png` |
| 8 · Zachary Moore (MF) | `zachary-moore.png` |
| 9 · Marvin Murdock (FW) | `marvin-murdock.png` |
| 10 · Thomas Murdock (FW) | `thomas-murdock.png` |
| 11 · Tyler Murdock (FW) | `tyler-murdock.png` |
| 15 · Seth Nichols (DF) | `seth-nichols.png` |
| 16 · Lynn Tambelle (DF) | `lynn-tambelle.png` |
| 17 · Axel Blaze (FW) | `axel-blaze.png` |
| 23 · Hilary Prentice (MF) | `hilary-prentice.png` |
| 24 · Jodi Green (DF) | `jodi-green.png` |

### Instituto Colina Verde

Escudo: `emblems/ares-midorigaoka.png`

| Jugador | Archivo |
|---|---|
| 1 · Wryn Twincrest (GK) | `wryn-twincrest.png` |
| 2 · Garvin Cliffmarch (DF) | `garvin-cliffmarch.png` |
| 3 · Therion Daywick (DF) | `therion-daywick.png` |
| 4 · Sylvar Verdis (DF) | `sylvar-verdis.png` |
| 5 · Orphion Ordain (DF) | `orphion-ordain.png` |
| 6 · Corwin Lumen (MF) | `corwin-lumen.png` |
| 7 · Aurel Ashdown (MF) | `aurel-ashdown.png` |
| 8 · Aveline Morrin (MF) | `aveline-morrin.png` |
| 9 · Merrick Seawell (FW) | `merrick-seawell.png` |
| 10 · Griffit Valiance (FW) | `griffit-valiance.png` |
| 11 · Corin Cainver (FW) | `corin-cainver.png` |
| 12 · Galad Worden (MF) | `galad-worden.png` |
| 13 · Alaric Durnham (MF) | `alaric-durnham.png` |
| 14 · Plumian Whitlock (MF) | `plumian-whitlock.png` |
| 15 · Queintas Quillmere (DF) | `queintas-quillmere.png` |
| 16 · Tarvon Runnel (MF) | `tarvon-runnel.png` |

### Instituto Brain (Ares)

Escudo: `emblems/ares-mikage-sennou-ares.png`

| Jugador | Archivo |
|---|---|
| 1 · Gideon Poe (GK) | `gideon-poe.png` |
| 2 · Harry Leading (DF) | `harry-leading.png` |
| 3 · Terry Stronger (DF) | `terry-stronger.png` |
| 4 · Philip Marvel (DF) | `philip-marvel.png` |
| 5 · Noel Good (DF) | `noel-good.png` |
| 6 · Electra Faraday (MF) | `electra-faraday.png` |
| 7 · Francis Tell (MF) | `francis-tell.png` |
| 8 · Darren Gouger (MF) | `darren-gouger.png` |
| 9 · Jonathan Seller (FW) | `jonathan-seller.png` |
| 10 · Victor Kind (MF) | `victor-kind.png` |
| 11 · Neil Turner (FW) | `neil-turner.png` |
| 12 · Des Pott (MF) | `des-pott.png` |
| 13 · Jethro Mackin (MF) | `jethro-mackin.png` |

### Instituto Bastión

Escudo: `emblems/ares-minodouzan.png`

| Jugador | Archivo |
|---|---|
| 1 · Knox Loxley (GK) | `knox-loxley.png` |
| 2 · Björn Brocken (DF) | `bj-rn-brocken.png` |
| 3 · Lunk Ironbrow (DF) | `lunk-ironbrow.png` |
| 4 · Hefton Bulk (DF) | `hefton-bulk.png` |
| 5 · Barry Cade (DF) | `barry-cade.png` |
| 6 · Rick Wall (MF) | `rick-wall.png` |
| 7 · Ivor Shield (MF) | `ivor-shield.png` |
| 8 · Rocky Hardcastle (MF) | `rocky-hardcastle.png` |
| 9 · Waldo Gibbons (FW) | `waldo-gibbons.png` |
| 10 · Sebastian Fortwright (MF) | `sebastian-fortwright.png` |
| 11 · Iggy Motte (FW) | `iggy-motte.png` |
| 12 · Corbin Brickham (DF) | `corbin-brickham.png` |
| 13 · Helena Harwood (GK) | `helena-harwood.png` |
| 14 · Dane Upchurch (FW) | `dane-upchurch.png` |
| 15 · Warden Watchford (MF) | `warden-watchford.png` |
| 15 · Jack Wallside (DF) | `jack-wallside.png` |

### Academia Plenilunio

Escudo: `emblems/ares-outei-tsukinomiya.png`

| Jugador | Archivo |
|---|---|
| 1 · Duske Grayling (GK) | `duske-grayling.png` |
| 2 · Solomon Owle (DF) | `solomon-owle.png` |
| 3 · Oleander Meadows (DF) | `oleander-meadows.png` |
| 4 · Piers Thornton (DF) | `piers-thornton.png` |
| 5 · Bud Bloome (DF) | `bud-bloome.png` |
| 6 · Reid Rivers (DF) | `reid-rivers.png` |
| 7 · Willow Proude (MF) | `willow-proude.png` |
| 8 · Wolfe Redwood (MF) | `wolfe-redwood.png` |
| 9 · Raven Vale (MF) | `raven-vale.png` |
| 10 · Heath Moore (FW) | `heath-moore.png` |
| 11 · Leif Bolt (FW) | `leif-bolt.png` |
| 13 · Lucas Star (MF) | `lucas-star.png` |
| 21 · Lucian Skye (MF) | `lucian-skye.png` |
| 22 · Solren Dawnwright (GK) | `solren-dawnwright.png` |
| 23 · Elior March (DF) | `elior-march.png` |
| 24 · Raylon Highmoor (MF) | `raylon-highmoor.png` |
| 25 · Fedrin Fennley (DF) | `fedrin-fennley.png` |

### Academia Polaris

Escudo: `emblems/ares-seishou-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Mickey Way (GK) | `mickey-way.png` |
| 2 · Kotono Tomio (DF) | `kotono-tomio.png` |
| 3 · Cygnus Starkey (DF) | `cygnus-starkey.png` |
| 4 · Ari Zimmerman (DF) | `ari-zimmerman.png` |
| 5 · Acker Reese (DF) | `acker-reese.png` |
| 6 · Jimmy Nigh (MF) | `jimmy-nigh.png` |
| 7 · Caesar Pike (MF) | `caesar-pike.png` |
| 8 · Oliver Golightly (MF) | `oliver-golightly.png` |
| 9 · Oscar Pio (MF) | `oscar-pio.png` |
| 10 · Eddy O'Ryan (MF) | `eddy-o-ryan.png` |
| 11 · Elliot Ember (FW) | `elliot-ember.png` |
| 12 · Holt Northam (DF) | `holt-northam.png` |
| 13 · Braveon Halvors (FW) | `braveon-halvors.png` |
| 14 · Konrad Hardin (GK) | `konrad-hardin.png` |
| 15 · Aren Yarrow (MF) | `aren-yarrow.png` |
| 16 · Jude Sharp (MF) | `jude-sharp.png` |

### Royal Academy (Ares)

Escudo: `emblems/ares-teikoku-gakuen-ares.png`

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
| 11 · David Samford (FW) | `david-samford.png` |
| 12 · Nathan Swift (DF) | `nathan-swift.png` |
| 13 · Grotley Bogwash (GK) | `grotley-bogwash.png` |
| 14 · Ray Dark (MF) | `ray-dark.png` |
| 15 · Emperio N. Guinn (DF) | `emperio-n-guinn.png` |
| 19 · Caleb Stonewall (MF) | `caleb-stonewall.png` |

### Instituto Ribera

Escudo: `emblems/ares-tonegawa-tousen.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Billy Miller (DF) | `billy-miller.png` |
| 3 · Jack Sawyer (MF) | `jack-sawyer.png` |
| 4 · Meriwether Beaumont (DF) | `meriwether-beaumont.png` |
| 5 · Burleigh Carpenter (DF) | `burleigh-carpenter.png` |
| 6 · Luke Blank (MF) | `luke-blank.png` |
| 7 · Gaffer Mason (MF) | `gaffer-mason.png` |
| 8 · Dan Bowsun (DF) | `dan-bowsun.png` |
| 9 · Giles Farmer (MF) | `giles-farmer.png` |
| 10 · Pacey Hawker (FW) | `pacey-hawker.png` |
| 11 · Neville Merchant (FW) | `neville-merchant.png` |
| 12 · Eamond Everwing (FW) | `eamond-everwing.png` |
| 13 · Frey Fielding (MF) | `frey-fielding.png` |
| 14 · Tobin Harveston (MF) | `tobin-harveston.png` |
| 15 · Everest Brightwell (DF) | `everest-brightwell.png` |
| 18 · Kia Tanner (MF) | `kia-tanner.png` |

### Instituto Zeus (Ares)

Escudo: `emblems/ares-zeus-ares.png`

| Jugador | Archivo |
|---|---|
| 1 · Ross Siddon (GK) | `ross-siddon.png` |
| 2 · Apollo Light (DF) | `apollo-light.png` |
| 3 · Hadrian Diesel (DF) | `hadrian-diesel.png` |
| 4 · Lane War (DF) | `lane-war.png` |
| 5 · Danny Wood (DF) | `danny-wood.png` |
| 6 · Artie Mishman (MF) | `artie-mishman.png` |
| 7 · Arion Matlock (MF) | `arion-matlock.png` |
| 8 · Wesley Knox (MF) | `wesley-knox.png` |
| 9 · Jonas Demetrius (FW) | `jonas-demetrius.png` |
| 10 · Byron Love (MF) | `byron-love.png` |
| 11 · Percy Hurst (FW) | `percy-hurst.png` |
| 12 · Deirdre Staples (FW) | `deirdre-staples.png` |
| 13 · Alexander Scrivener (GK) | `alexander-scrivener.png` |

### Chrono Storm

Escudo: `emblems/cs-chrono-storm.png`

| Jugador | Archivo |
|---|---|
| 3 · Gabriel Garcia (DF) | `gabriel-garcia.png` |
| 5 · Jean-Pierre Lapin (GK) | `jean-pierre-lapin.png` |
| 6 · Sol Daystar (FW) | `sol-daystar.png` |
| 7 · Fei Rune (FW) | `fei-rune.png` |
| 8 · Arion Sherwind (MF) | `arion-sherwind.png` |
| 9 · Riccardo Di Rigo (MF) | `riccardo-di-rigo.png` |
| 10 · Victor Blade (FW) | `victor-blade.png` |
| 11 · Zanark Avalonic (FW) | `zanark-avalonic.png` |
| 12 · Bailong (FW) | `bailong.png` |
| 15 · Sor (DF) | `sor.png` |
| 16 · Ryoma Nishiki (MF) | `ryoma-nishiki.png` |
| 78 · Goldie Lemmon (DF) | `goldie-lemmon.png` |

### Desesperdidos

Escudo: `emblems/cs-destructchers.png`

| Jugador | Archivo |
|---|---|
| 1 · Lotus (GK) | `lotus.png` |
| 2 · Magnol (DF) | `magnol.png` |
| 3 · Tulip (DF) | `tulip.png` |
| 4 · Argyr (DF) | `argyr.png` |
| 5 · Laven (MF) | `laven.png` |
| 6 · Viol (MF) | `viol.png` |
| 7 · Dandy (MF) | `dandy.png` |
| 8 · Chamomile (MF) | `chamomile.png` |
| 9 · Orchid (MF) | `orchid.png` |
| 10 · Aster (FW) | `aster.png` |
| 11 · Gentian (FW) | `gentian.png` |
| 12 · Flora (FW) | `flora.png` |
| 13 · Flora (FW) | `flora-cs-fran-mm.png` |
| 14 · Sterne (FW) | `sterne.png` |

### El Dorado Equipo 02

Escudo: `emblems/cs-el-dorado-team-02.png`

| Jugador | Archivo |
|---|---|
| 1 · Romeo (GK) | `romeo.png` |
| 1 · Mecha-Mark (GK) | `mecha-mark.png` |
| 3 · Wanli Changcheng (DF) | `wanli-changcheng.png` |
| 3 · Kilo (DF) | `kilo.png` |
| 4 · Papa (DF) | `papa.png` |
| 6 · Alpha (FW) | `alpha.png` |
| 7 · November (MF) | `november.png` |
| 8 · Beta (FW) | `beta.png` |
| 9 · Riccardo Di Rigo (MF) | `riccardo-di-rigo.png` |
| 10 · Gamma (FW) | `gamma.png` |
| 11 · Mike (FW) | `mike.png` |
| 15 · Aitor Cazador (DF) | `aitor-cazador.png` |
| 17 · Michael Ballzack (FW) | `michael-ballzack.png` |
| 99 · Zanark Avalonic (FW) | `zanark-avalonic.png` |

### Gar

Escudo: `emblems/cs-garu.png`

| Jugador | Archivo |
|---|---|
| 1 · Chitoh (GK) | `chitoh.png` |
| 2 · Kazach (DF) | `kazach.png` |
| 3 · Fumh (DF) | `fumh.png` |
| 4 · Gumille (DF) | `gumille.png` |
| 5 · Yurkeh (MF) | `yurkeh.png` |
| 6 · Rokah (MF) | `rokah.png` |
| 7 · Pinoh (MF) | `pinoh.png` |
| 8 · Tahk (MF) | `tahk.png` |
| 9 · Fei Rune (FW) | `fei-rune.png` |
| 10 · Dekih (FW) | `dekih.png` |
| 11 · Yuh (FW) | `yuh.png` |
| 12 · Bhabass (GK) | `bhabass.png` |
| 13 · Sheenai (DF) | `sheenai.png` |
| 14 · Tessell (MF) | `tessell.png` |
| 15 · Chikka (MF) | `chikka.png` |
| 16 · Mahrsa (FW) | `mahrsa.png` |

### Gir

Escudo: `emblems/cs-giru.png`

| Jugador | Archivo |
|---|---|
| 1 · Bhufa (GK) | `bhufa.png` |
| 2 · Zohtan (DF) | `zohtan.png` |
| 3 · Mustah (DF) | `mustah.png` |
| 4 · Mohrir (DF) | `mohrir.png` |
| 5 · Ghimus (MF) | `ghimus.png` |
| 6 · Tzeikh (MF) | `tzeikh.png` |
| 7 · Miehd (MF) | `miehd.png` |
| 8 · Mehr (MF) | `mehr.png` |
| 9 · Ghiris (MF) | `ghiris.png` |
| 10 · Chell (FW) | `chell.png` |
| 11 · Zetoh (FW) | `zetoh.png` |
| 12 · Enimaux (GK) | `enimaux.png` |
| 13 · Darehn (DF) | `darehn.png` |
| 14 · Mabhi (MF) | `mabhi.png` |
| 15 · Nahrje (MF) | `nahrje.png` |
| 16 · Veneth (FW) | `veneth.png` |

### Inazuma Japón Legendario

Escudo: `emblems/cs-inazuma-legend-japan.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Nathan Swift (DF) | `nathan-swift.png` |
| 3 · Jack Wallside (DF) | `jack-wallside.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 8 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 9 · Shawn Froste (FW) | `shawn-froste.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 14 · Jude Sharp (MF) | `jude-sharp.png` |
| 16 · David Samford (FW) | `david-samford.png` |
| 17 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 18 · Xavier Foster (FW) | `xavier-foster.png` |

### Ejército de Terracota

Escudo: `emblems/cs-karakuri-bingmayong.png`

| Jugador | Archivo |
|---|---|
| 1 · Guan Yu (DF) | `guan-yu.png` |
| 2 · Zhang Fei (FW) | `zhang-fei.png` |
| 3 · Terracotta Warrior 1 (GK) | `terracotta-warrior-1.png` |
| 4 · Terracotta Warrior 2 (DF) | `terracotta-warrior-2.png` |
| 5 · Terracotta Warrior 3 (DF) | `terracotta-warrior-3.png` |
| 6 · Terracotta Warrior 4 (DF) | `terracotta-warrior-4.png` |
| 7 · Terracotta Warrior 5 (MF) | `terracotta-warrior-5.png` |
| 8 · Terracotta Warrior 6 (MF) | `terracotta-warrior-6.png` |
| 9 · Terracotta Warrior 7 (MF) | `terracotta-warrior-7.png` |
| 10 · Terracotta Warrior 8 (MF) | `terracotta-warrior-8.png` |
| 11 · Terracotta Warrior 9 (MF) | `terracotta-warrior-9.png` |
| 12 · Terracotta Warrior 10 (MF) | `terracotta-warrior-10.png` |
| 13 · Terracotta Warrior 11 (FW) | `terracotta-warrior-11.png` |

### Cascada Perfecta

Escudo: `emblems/cs-perfect-cascade.png`

| Jugador | Archivo |
|---|---|
| 1 · Vee Wai (GK) | `vee-wai.png` |
| 2 · Dee Vee (DF) | `dee-vee.png` |
| 3 · Ayt Bee (DF) | `ayt-bee.png` |
| 4 · En Sicks (DF) | `en-sicks.png` |
| 5 · Wun Ell (MF) | `wun-ell.png` |
| 6 · Zed Kyu (MF) | `zed-kyu.png` |
| 7 · Kay Zirro (MF) | `kay-zirro.png` |
| 8 · Cee Eff (MF) | `cee-eff.png` |
| 9 · Ar Ecks (MF) | `ar-ecks.png` |
| 10 · Em Tee (FW) | `em-tee.png` |
| 11 · Ough Cee (FW) | `ough-cee.png` |
| 12 · Jay Yuu (GK) | `jay-yuu.png` |
| 13 · Faiv Ess (DF) | `faiv-ess.png` |
| 14 · Tu Eigh (MF) | `tu-eigh.png` |
| 15 · Aye Nort (FW) | `aye-nort.png` |
| 16 · Ji Tenn (FW) | `ji-tenn.png` |

### Protocolo Omega 2.0

Escudo: `emblems/cs-protocol-omega-2-0.png`

| Jugador | Archivo |
|---|---|
| 1 · Hotel (GK) | `hotel.png` |
| 2 · Oscar (DF) | `oscar.png` |
| 3 · Kilo (DF) | `kilo.png` |
| 4 · Golf (DF) | `golf.png` |
| 5 · Foxtrot (MF) | `foxtrot.png` |
| 6 · Lima (MF) | `lima.png` |
| 7 · November (MF) | `november.png` |
| 8 · India (MF) | `india.png` |
| 9 · Juliet (FW) | `juliet.png` |
| 10 · Beta (FW) | `beta.png` |
| 11 · Mike (FW) | `mike.png` |
| 12 · Uniform (GK) | `uniform.png` |
| 13 · Tango (DF) | `tango.png` |
| 14 · Zulu (MF) | `zulu.png` |
| 15 · X-Ray (FW) | `x-ray.png` |
| 16 · Delta (FW) | `delta.png` |

### Protocolo Omega 3.0

Escudo: `emblems/cs-protocol-omega-3-0.png`

| Jugador | Archivo |
|---|---|
| 1 · Romeo (GK) | `romeo.png` |
| 2 · Oscar (DF) | `oscar.png` |
| 3 · Kilo (DF) | `kilo.png` |
| 4 · Papa (DF) | `papa.png` |
| 5 · Quebec (MF) | `quebec.png` |
| 6 · Lima (MF) | `lima.png` |
| 7 · November (MF) | `november.png` |
| 8 · Sierra (MF) | `sierra.png` |
| 9 · Juliet (FW) | `juliet.png` |
| 10 · Gamma (FW) | `gamma.png` |
| 11 · Mike (FW) | `mike.png` |
| 12 · Romeo (GK) | `romeo-cs-lugic.png` |
| 13 · Papa (DF) | `papa-cs-galling.png` |
| 14 · Quebec (MF) | `quebec-cs-bahamus.png` |
| 15 · Sierra (MF) | `sierra-cs-dhanna.png` |
| 16 · Gamma (FW) | `gamma-cs-gamma.png` |

### Protocolo Omega

Escudo: `emblems/cs-protocol-omega.png`

| Jugador | Archivo |
|---|---|
| 2 · Hotel (GK) | `hotel.png` |
| 3 · Oscar (DF) | `oscar.png` |
| 4 · Echo (DF) | `echo.png` |
| 5 · Golf (DF) | `golf.png` |
| 6 · Charlie (MF) | `charlie.png` |
| 7 · Lima (MF) | `lima.png` |
| 8 · Bravo (MF) | `bravo.png` |
| 9 · India (MF) | `india.png` |
| 10 · Beta (FW) | `beta.png` |
| 10 · Juliet (FW) | `juliet.png` |
| 11 · Alpha (FW) | `alpha.png` |
| 12 · Mike (FW) | `mike.png` |
| 13 · Uniform (GK) | `uniform.png` |
| 14 · Tango (DF) | `tango.png` |
| 15 · Zulu (MF) | `zulu.png` |
| 16 · X-Ray (FW) | `x-ray.png` |

### Banda del Ciervo Blanco

Escudo: `emblems/cs-shiroshika-gumi.png`

| Jugador | Archivo |
|---|---|
| 1 · Norimaru Gazen (GK) | `norimaru-gazen.png` |
| 2 · Sokichi Kitagami (DF) | `sokichi-kitagami.png` |
| 3 · Hoichiro Ashiguro (DF) | `hoichiro-ashiguro.png` |
| 4 · Hanbee Yabe (DF) | `hanbee-yabe.png` |
| 5 · Ikkatsu Kano (MF) | `ikkatsu-kano.png` |
| 6 · Denbee Asama (MF) | `denbee-asama.png` |
| 7 · Ginji Santetsu (MF) | `ginji-santetsu.png` |
| 8 · Denrai Ochimura (MF) | `denrai-ochimura.png` |
| 9 · Senji Kudo (MF) | `senji-kudo.png` |
| 10 · Taian Inaba (FW) | `taian-inaba.png` |
| 11 · Korin Maebayashi (FW) | `korin-maebayashi.png` |
| 12 · Mikimaru Ujiki (GK) | `mikimaru-ujiki.png` |
| 13 · Doshin Yomoyama (DF) | `doshin-yomoyama.png` |
| 14 · Tenkei Yazu (MF) | `tenkei-yazu.png` |
| 15 · Hokuro Ayabe (FW) | `hokuro-ayabe.png` |
| 16 · Kaburo Hayama (FW) | `kaburo-hayama.png` |

### Futboloides

Escudo: `emblems/cs-soccer-robots.png`

| Jugador | Archivo |
|---|---|
| 1 · FB-101X (GK) | `fb-101x.png` |
| 2 · FB-102X (DF) | `fb-102x.png` |
| 3 · FB-103X (DF) | `fb-103x.png` |
| 4 · FB-104X (DF) | `fb-104x.png` |
| 5 · FB-105X (MF) | `fb-105x.png` |
| 6 · FB-106X (MF) | `fb-106x.png` |
| 7 · FB-107X (MF) | `fb-107x.png` |
| 8 · FB-108X (MF) | `fb-108x.png` |
| 9 · FB-109X (FW) | `fb-109x.png` |
| 10 · FB-110X (FW) | `fb-110x.png` |
| 11 · FB-111X (FW) | `fb-111x.png` |

### Instituto Raimon (Chrono Stones)

Escudo: `emblems/cs-team-raimon.png`

| Jugador | Archivo |
|---|---|
| 3 · Gabriel Garcia (DF) | `gabriel-garcia.png` |
| 8 · Arion Sherwind (MF) | `arion-sherwind.png` |
| 9 · Riccardo Di Rigo (MF) | `riccardo-di-rigo.png` |
| 10 · Victor Blade (FW) | `victor-blade.png` |
| 11 · Fei Rune (FW) | `fei-rune.png` |
| 12 · Sol Daystar (FW) | `sol-daystar-cs-amemiya-mm.png` |
| 13 · Bailong (FW) | `bailong-cs-hakuryuu-mm.png` |
| 14 · Ryoma Nishiki (MF) | `ryoma-nishiki.png` |
| 14 · Fei Rune (FW) | `fei-rune-cs-fei-mmbig.png` |
| 15 · Fei Rune (FW) | `fei-rune-cs-fei-mmtyranno.png` |
| 16 · Gorota (DF) | `gorota.png` |
| 18 · Sol Daystar (FW) | `sol-daystar.png` |
| 19 · Bailong (FW) | `bailong.png` |
| 20 · Jean-Pierre Lapin (GK) | `jean-pierre-lapin.png` |
| 21 · Sor (DF) | `sor.png` |
| 78 · Goldie Lemmon (DF) | `goldie-lemmon.png` |

### Los Arions

Escudo: `emblems/cs-tenmas.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 5 · Biggsy (GK) | `biggsy.png` |
| 6 · Smiley (DF) | `smiley.png` |
| 7 · Skinny (DF) | `skinny.png` |
| 8 · Smarty (DF) | `smarty.png` |
| 8 · Arion Sherwind (MF) | `arion-sherwind.png` |
| 9 · Chunky (DF) | `chunky.png` |
| 10 · Tiny (MF) | `tiny.png` |
| 10 · Vladimir Blade (FW) | `vladimir-blade.png` |
| 11 · Hairy (MF) | `hairy.png` |
| 11 · Fei Rune (FW) | `fei-rune.png` |
| 12 · Spikey (MF) | `spikey.png` |
| 13 · Creepy (FW) | `creepy.png` |

### Ragnah

Escudo: `emblems/cs-the-lagoon.png`

| Jugador | Archivo |
|---|---|
| 1 · Hippos Kohlt (GK) | `hippos-kohlt.png` |
| 2 · Anas Eidah (DF) | `anas-eidah.png` |
| 3 · Djung Hamstah (DF) | `djung-hamstah.png` |
| 4 · Ewa Mouton (DF) | `ewa-mouton.png` |
| 5 · Sus Swihn (DF) | `sus-swihn.png` |
| 6 · Katya Felis (MF) | `katya-felis.png` |
| 7 · Macah Psitta (MF) | `macah-psitta.png` |
| 8 · Mehr (MF) | `mehr.png` |
| 9 · Ghiris (MF) | `ghiris.png` |
| 10 · Simeon Ayp (FW) | `simeon-ayp.png` |
| 11 · Kyon Canis (FW) | `kyon-canis.png` |
| 12 · Siid Sinapis (GK) | `siid-sinapis.png` |
| 13 · Pelta Chincha (DF) | `pelta-chincha.png` |
| 14 · Folie Vora (MF) | `folie-vora.png` |
| 15 · Lieva Snoshu (MF) | `lieva-snoshu.png` |
| 16 · Russo Rosmarus (FW) | `russo-rosmarus.png` |

### Aullido Lunar

Escudo: `emblems/cs-tsukigami-no-ichizoku.png`

| Jugador | Archivo |
|---|---|
| 1 · Lee Canthrup (GK) | `lee-canthrup.png` |
| 2 · Gerald Fuss (DF) | `gerald-fuss.png` |
| 3 · Kym Errer (DF) | `kym-errer.png` |
| 4 · Hunter O'Mann (MF) | `hunter-o-mann.png` |
| 5 · Mona Selene (MF) | `mona-selene.png` |
| 6 · Lou Garrou (MF) | `lou-garrou.png` |
| 7 · Al Woo (MF) | `al-woo.png` |
| 8 · Sylvester Bullet (MF) | `sylvester-bullet.png` |
| 9 · Terri Ann Thrope (FW) | `terri-ann-thrope.png` |
| 10 · Wolfram Vulpeen (FW) | `wolfram-vulpeen.png` |
| 11 · Luke Kayon (FW) | `luke-kayon.png` |
| 12 · Wolfram Vulpeen (FW) | `wolfram-vulpeen-cs-garshah-mm.png` |

### Nosfanáticos

Escudo: `emblems/cs-vamptym.png`

| Jugador | Archivo |
|---|---|
| 1 · Vince Sizor (GK) | `vince-sizor.png` |
| 2 · Ron Innwater (DF) | `ron-innwater.png` |
| 3 · Holly Waters (DF) | `holly-waters.png` |
| 4 · Turner Fogg (DF) | `turner-fogg.png` |
| 5 · Sid Viper (MF) | `sid-viper.png` |
| 6 · Dave Walker (MF) | `dave-walker.png` |
| 7 · Porphyria Filia (MF) | `porphyria-filia.png` |
| 8 · Hugh Mumford (MF) | `hugh-mumford.png` |
| 9 · Desmodus Drakul (MF) | `desmodus-drakul.png` |
| 10 · Woodrow Stake (FW) | `woodrow-stake.png` |
| 11 · Nora Flexion (FW) | `nora-flexion.png` |
| 12 · Desmodus Drakul (MF) | `desmodus-drakul-cs-vamp-mm.png` |

### Zan

Escudo: `emblems/cs-zan.png`

| Jugador | Archivo |
|---|---|
| 1 · Feduhm (GK) | `feduhm.png` |
| 2 · Tsync (DF) | `tsync.png` |
| 3 · Driss (DF) | `driss.png` |
| 4 · Ludeau (DF) | `ludeau.png` |
| 5 · Dios (MF) | `dios.png` |
| 6 · Grigham (MF) | `grigham.png` |
| 7 · Zatang (MF) | `zatang.png` |
| 8 · Rodh (MF) | `rodh.png` |
| 9 · Djibz (MF) | `djibz.png` |
| 10 · Zanark Avalonic (FW) | `zanark-avalonic.png` |
| 11 · Garreau (MF) | `garreau.png` |
| 12 · Steiyah (GK) | `steiyah.png` |
| 13 · Mhadoor (DF) | `mhadoor.png` |
| 14 · Heyze (MF) | `heyze.png` |
| 15 · Kuhrach (MF) | `kuhrach.png` |
| 16 · Torhm (FW) | `torhm.png` |

### Zanark Domain

Escudo: `emblems/cs-zanark-domain.png`

| Jugador | Archivo |
|---|---|
| 1 · Eka (GK) | `eka.png` |
| 2 · Dva (DF) | `dva.png` |
| 3 · Tyrah (DF) | `tyrah.png` |
| 4 · Catvari (DF) | `catvari.png` |
| 5 · Panca (MF) | `panca.png` |
| 6 · Sas (MF) | `sas.png` |
| 7 · Sapta (MF) | `sapta.png` |
| 8 · Asta (MF) | `asta.png` |
| 9 · Navan (FW) | `navan.png` |
| 10 · Zanark Avalonic (FW) | `zanark-avalonic.png` |
| 11 · Dasan (FW) | `dasan.png` |
| 12 · Sata (GK) | `sata.png` |
| 13 · Sahasra (DF) | `sahasra.png` |
| 14 · Ayuta (MF) | `ayuta.png` |
| 15 · Laksha (FW) | `laksha.png` |
| 16 · Niyuta (FW) | `niyuta.png` |

### Edad Dorada

Escudo: `emblems/go-akizora-challengers.png`

| Jugador | Archivo |
|---|---|
| 1 · Chuck Pumpkins (GK) | `chuck-pumpkins.png` |
| 2 · Scott Banyan (DF) | `scott-banyan.png` |
| 3 · Filbert Chestnut (DF) | `filbert-chestnut.png` |
| 4 · Gadish Oldman (DF) | `gadish-oldman.png` |
| 5 · Autumn Leaf (DF) | `autumn-leaf.png` |
| 6 · Skeeter Hawk (MF) | `skeeter-hawk.png` |
| 7 · Guy-Jean Harvestman (MF) | `guy-jean-harvestman.png` |
| 8 · Hal Löwén (MF) | `hal-l-w-n.png` |
| 9 · Jacko Lantern (MF) | `jacko-lantern.png` |
| 10 · Bobine Apples (FW) | `bobine-apples.png` |
| 11 · Sibylle Equinox (FW) | `sibylle-equinox.png` |

### Oscuridad Ancestral

Escudo: `emblems/go-ancient-dark.png`

| Jugador | Archivo |
|---|---|
| 1 · Nero Night (GK) | `nero-night.png` |
| 2 · Morris Moore (DF) | `morris-moore.png` |
| 3 · Jet Onyx (DF) | `jet-onyx.png` |
| 4 · Cole Ebony (DF) | `cole-ebony.png` |
| 5 · Blake Obscura (DF) | `blake-obscura.png` |
| 6 · Shady Shwartz (MF) | `shady-shwartz.png` |
| 7 · Goth Grimshaw (MF) | `goth-grimshaw.png` |
| 8 · Duff Dooley (MF) | `duff-dooley.png` |
| 9 · Tynan Crowe (MF) | `tynan-crowe.png` |
| 10 · Tezcat (FW) | `tezcat.png` |
| 11 · Yang (FW) | `yang.png` |

### Colegio Ultramegahiedra

Escudo: `emblems/go-aoba-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Clem Attish (GK) | `clem-attish.png` |
| 2 · Tyrian Purpel (MF) | `tyrian-purpel.png` |
| 3 · Pike Pollack (DF) | `pike-pollack.png` |
| 4 · Martin Blando (DF) | `martin-blando.png` |
| 5 · Keane Gardner (DF) | `keane-gardner.png` |
| 6 · Shaun Bonce (MF) | `shaun-bonce.png` |
| 7 · Penn Minim (MF) | `penn-minim.png` |
| 8 · Brook Bold (MF) | `brook-bold.png` |
| 9 · Francis Tuffnot (DF) | `francis-tuffnot.png` |
| 10 · Joshua Bleak (FW) | `joshua-bleak.png` |
| 11 · Hayden Whyrl (FW) | `hayden-whyrl.png` |
| 12 · Matt Durer (GK) | `matt-durer.png` |
| 13 · Nixon Earlnight (DF) | `nixon-earlnight.png` |
| 14 · Jack Balance (MF) | `jack-balance.png` |
| 15 · Skylar Lepton (DF) | `skylar-lepton.png` |
| 16 · Tarquin Orchards (FW) | `tarquin-orchards.png` |

### Instituto Universal

Escudo: `emblems/go-arakumo-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Ringo Saturn (GK) | `ringo-saturn.png` |
| 2 · Terran Gaea (DF) | `terran-gaea.png` |
| 3 · Auberon Ouranos (DF) | `auberon-ouranos.png` |
| 4 · Manning Moon (DF) | `manning-moon.png` |
| 5 · Crateris Mercury (DF) | `crateris-mercury.png` |
| 6 · Nix Pluto (MF) | `nix-pluto.png` |
| 7 · Deimos Mars (MF) | `deimos-mars.png` |
| 8 · Triton Nettuno (FW) | `triton-nettuno.png` |
| 9 · Neith Venus (MF) | `neith-venus.png` |
| 10 · Callis Jove (MF) | `callis-jove.png` |
| 11 · Sol Daystar (FW) | `sol-daystar.png` |
| 12 · Astro Ceres (GK) | `astro-ceres.png` |
| 13 · Chiron Vestal (FW) | `chiron-vestal.png` |
| 14 · Xeno Eris (MF) | `xeno-eris.png` |
| 15 · Namak Haumea (DF) | `namak-haumea.png` |
| 16 · Mac Emake (DF) | `mac-emake.png` |

### Cuerno Demoníaco

Escudo: `emblems/go-demon-s-horn.png`

| Jugador | Archivo |
|---|---|
| 1 · Xavier Shotwell (GK) | `xavier-shotwell.png` |
| 2 · Crimson Wiseman (DF) | `crimson-wiseman.png` |
| 3 · Linder Loper (DF) | `linder-loper.png` |
| 4 · Locke Saflowe (DF) | `locke-saflowe.png` |
| 5 · Cirrus Whisp (MF) | `cirrus-whisp.png` |
| 6 · Sandy Dryhill (MF) | `sandy-dryhill.png` |
| 7 · Romeo Fitzroy (MF) | `romeo-fitzroy.png` |
| 8 · Dryden Zephyr (MF) | `dryden-zephyr.png` |
| 9 · Harry Dwind (FW) | `harry-dwind.png` |
| 10 · Bracknell Forge (FW) | `bracknell-forge.png` |
| 11 · Damien Blackloch (FW) | `damien-blackloch.png` |
| 12 · Brutus Nastion (GK) | `brutus-nastion.png` |
| 13 · Linden Haregrove (DF) | `linden-haregrove.png` |
| 14 · Nate Gobby (DF) | `nate-gobby.png` |
| 15 · Keith Wellington (DF) | `keith-wellington.png` |
| 16 · Reggie Alldark (MF) | `reggie-alldark.png` |

### Dragon Link

Escudo: `emblems/go-dragonlink.png`

| Jugador | Archivo |
|---|---|
| 1 · Quentin Cinquedea (GK) | `quentin-cinquedea.png` |
| 2 · Aimé Quintet (DF) | `aim-quintet.png` |
| 3 · Eljas Viisi (DF) | `eljas-viisi.png` |
| 4 · Pentra Chek (MF) | `pentra-chek.png` |
| 5 · Federigo Cinco (MF) | `federigo-cinco.png` |
| 6 · Ferdinand Delafünfe (MF) | `ferdinand-delaf-nfe.png` |
| 7 · Quinque Flores (FW) | `quinque-flores.png` |
| 8 · Jacques Cinquini (FW) | `jacques-cinquini.png` |
| 9 · Fivier Saviola (MF) | `fivier-saviola.png` |
| 10 · David Quintola (FW) | `david-quintola.png` |
| 11 · Erik Pentona (FW) | `erik-pentona.png` |
| 12 · Leonidas Epsilon (GK) | `leonidas-epsilon.png` |
| 13 · George Wu (MF) | `george-wu.png` |
| 14 · Geert Vandevijf (FW) | `geert-vandevijf.png` |
| 15 · Folke Fem (MF) | `folke-fem.png` |
| 16 · Naji Khamsa (DF) | `naji-khamsa.png` |

### Colegio de Empollones

Escudo: `emblems/go-eito-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Par Scal (GK) | `par-scal.png` |
| 2 · Tez La (DF) | `tez-la.png` |
| 3 · Aris Tottle (DF) | `aris-tottle.png` |
| 4 · Archie Medes (DF) | `archie-medes.png` |
| 5 · Socrat Eiss (DF) | `socrat-eiss.png` |
| 6 · Ian Stein (MF) | `ian-stein.png` |
| 7 · Ed Ison (MF) | `ed-ison.png` |
| 8 · Mitchell Angelio (MF) | `mitchell-angelio.png` |
| 9 · Moe Sart (FW) | `moe-sart.png` |
| 10 · Dave Inchy (MF) | `dave-inchy.png` |
| 11 · Frank Lyn (FW) | `frank-lyn.png` |
| 12 · Cooper Nikos (GK) | `cooper-nikos.png` |
| 13 · Leo Gally (DF) | `leo-gally.png` |
| 14 · Desmond Cartes (MF) | `desmond-cartes.png` |
| 15 · Connor Fuschius (MF) | `connor-fuschius.png` |
| 16 · Dar Wynne (FW) | `dar-wynne.png` |

### Academia Militar Mar de Luna

Escudo: `emblems/go-gassan-kunimitsu.png`

| Jugador | Archivo |
|---|---|
| 1 · Alessandro il Grande (GK) | `alessandro-il-grande.png` |
| 2 · Gene Ghiskhan (DF) | `gene-ghiskhan.png` |
| 3 · Attila Hun (DF) | `attila-hun.png` |
| 4 · Sun Tzu (DF) | `sun-tzu.png` |
| 5 · Arty Xerxes (DF) | `arty-xerxes.png` |
| 6 · Darius Cyrus (MF) | `darius-cyrus.png` |
| 7 · Jerry Onimo (MF) | `jerry-onimo.png` |
| 8 · Leon Ohnepart (MF) | `leon-ohnepart.png` |
| 9 · Robert Lee (FW) | `robert-lee.png` |
| 10 · Doug McArthur (FW) | `doug-mcarthur.png` |
| 11 · Nobby Naga (FW) | `nobby-naga.png` |
| 12 · Salvador Addin (GK) | `salvador-addin.png` |
| 13 · Otto Bismark (DF) | `otto-bismark.png` |
| 14 · Jean Darc (DF) | `jean-darc.png` |
| 15 · Bobby Bruce (FW) | `bobby-bruce.png` |
| 16 · Hanny Bawl (FW) | `hanny-bawl.png` |

### Instituto Espejismo

Escudo: `emblems/go-genei-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Abram Cadabra (GK) | `abram-cadabra.png` |
| 2 · Jaymes Randie (DF) | `jaymes-randie.png` |
| 3 · Daffyd Blayne (DF) | `daffyd-blayne.png` |
| 4 · Al Kazam (DF) | `al-kazam.png` |
| 5 · Sigfryd Roi (DF) | `sigfryd-roi.png` |
| 6 · Dave Coppfielder (MF) | `dave-coppfielder.png` |
| 7 · Launce Berton (MF) | `launce-berton.png` |
| 8 · Ledger Demain (MF) | `ledger-demain.png` |
| 9 · Harrold Houdini (MF) | `harrold-houdini.png` |
| 10 · Hocus Sesame (FW) | `hocus-sesame.png` |
| 11 · Pocus Sesame (FW) | `pocus-sesame.png` |
| 12 · Pen Teller (GK) | `pen-teller.png` |
| 13 · Petey Sorcar (DF) | `petey-sorcar.png` |
| 14 · Trump Loyal (MF) | `trump-loyal.png` |
| 15 · Daren Blakh (FW) | `daren-blakh.png` |
| 16 · Billy Lingsoo (FW) | `billy-lingsoo.png` |

### Instituto Alpino (GO)

Escudo: `emblems/go-hakuren-go.png`

| Jugador | Archivo |
|---|---|
| 1 · Wolfe Whyte (GK) | `wolfe-whyte.png` |
| 2 · Sascha Kotch (DF) | `sascha-kotch.png` |
| 3 · Guy l'Acier (DF) | `guy-l-acier.png` |
| 4 · Matther Horne (DF) | `matther-horne.png` |
| 5 · Iggie Loo (DF) | `iggie-loo.png` |
| 6 · Bob Sled (MF) | `bob-sled.png` |
| 7 · Blain Chills (MF) | `blain-chills.png` |
| 8 · Art Tundra (MF) | `art-tundra.png` |
| 9 · Borel Aurora (MF) | `borel-aurora.png` |
| 10 · Njord Snio (FW) | `njord-snio.png` |
| 11 · Yule Hoarfrost (FW) | `yule-hoarfrost.png` |
| 12 · Suno Aisu (GK) | `suno-aisu.png` |
| 13 · Himesh Himalaya (DF) | `himesh-himalaya.png` |
| 14 · Blake Wintry (MF) | `blake-wintry.png` |
| 15 · Fritz Brisk (MF) | `fritz-brisk.png` |
| 16 · Grisley Bear (FW) | `grisley-bear.png` |

### Royal Academy (GO)

Escudo: `emblems/go-henkaku-no-teikoku.png`

| Jugador | Archivo |
|---|---|
| 1 · Preston Princeton (GK) | `preston-princeton.png` |
| 2 · Dracon Yale (DF) | `dracon-yale.png` |
| 3 · Duke Dartmouth (DF) | `duke-dartmouth.png` |
| 4 · Cameron Cambridge (DF) | `cameron-cambridge.png` |
| 5 · Earl Eton (MF) | `earl-eton.png` |
| 6 · Caesar Cornell (MF) | `caesar-cornell.png` |
| 7 · Hampton Harvard (MF) | `hampton-harvard.png` |
| 8 · Baron Oxford (DF) | `baron-oxford.png` |
| 9 · Sterling Stanford (MF) | `sterling-stanford.png` |
| 10 · Colby Columbia (FW) | `colby-columbia.png` |
| 11 · Rex Remington (FW) | `rex-remington.png` |
| 12 · Fred Featherstonhaugh (GK) | `fred-featherstonhaugh.png` |
| 13 · Arthur Ascot (DF) | `arthur-ascot.png` |
| 14 · Stuart St John (DF) | `stuart-st-john.png` |
| 15 · Wenceslas Wales (FW) | `wenceslas-wales.png` |
| 16 · Yorick York (MF) | `yorick-york.png` |

### Inazuma Kids FC (GO)

Escudo: `emblems/go-inazuma-kfc-go.png`

| Jugador | Archivo |
|---|---|
| 1 · Vivian Doosley (GK) | `vivian-doosley.png` |
| 2 · Sean Muller (DF) | `sean-muller.png` |
| 3 · Abe Roof (DF) | `abe-roof.png` |
| 4 · Buck Tucker (DF) | `buck-tucker.png` |
| 5 · Edward Headwood (DF) | `edward-headwood.png` |
| 6 · Ricky Shea (MF) | `ricky-shea.png` |
| 7 · Felix Higgins (MF) | `felix-higgins.png` |
| 8 · Warren Cool (FW) | `warren-cool.png` |
| 9 · Keeley Hall (MF) | `keeley-hall.png` |
| 10 · Walt Riverside (MF) | `walt-riverside.png` |
| 11 · Elizabeth Buble (FW) | `elizabeth-buble.png` |
| 12 · Titch Allhare (GK) | `titch-allhare.png` |
| 13 · Puck Fishley (DF) | `puck-fishley.png` |
| 14 · Reed Maind (MF) | `reed-maind.png` |
| 15 · Jacqueline Rabbit (FW) | `jacqueline-rabbit.png` |
| 16 · Bert Trapper (DF) | `bert-trapper.png` |

### Academia Cala Pirata

Escudo: `emblems/go-kaiou-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Ishmael Ahab (GK) | `ishmael-ahab.png` |
| 2 · Octavus Kraken (DF) | `octavus-kraken.png` |
| 3 · Roger Jolly (DF) | `roger-jolly.png` |
| 4 · Sinbad Saylor (DF) | `sinbad-saylor.png` |
| 5 · Rob Crusoe (DF) | `rob-crusoe.png` |
| 6 · Cheung Po (MF) | `cheung-po.png` |
| 7 · William Kidd (MF) | `william-kidd.png` |
| 8 · Santelmo Phyre (MF) | `santelmo-phyre.png` |
| 9 · Dakkar Nemo (MF) | `dakkar-nemo.png` |
| 10 · Davy Jones (FW) | `davy-jones.png` |
| 11 · Calico Corsair (FW) | `calico-corsair.png` |
| 12 · Nick Tofobia (GK) | `nick-tofobia.png` |
| 13 · Marley Hookson (MF) | `marley-hookson.png` |
| 14 · Bart Black (DF) | `bart-black.png` |
| 15 · Frank Drake (DF) | `frank-drake.png` |
| 16 · Barnabas Rossa (FW) | `barnabas-rossa.png` |

### Instituto Kirkwood (GO)

Escudo: `emblems/go-kidokawa-seishuu-go.png`

| Jugador | Archivo |
|---|---|
| 1 · Strom Boojum (GK) | `strom-boojum.png` |
| 2 · Dock Hickory (DF) | `dock-hickory.png` |
| 3 · Bourne Birch (DF) | `bourne-birch.png` |
| 4 · Flynt Pine (DF) | `flynt-pine.png` |
| 5 · Trent Poplar (DF) | `trent-poplar.png` |
| 6 · River Willows (MF) | `river-willows.png` |
| 7 · Beck Heath (MF) | `beck-heath.png` |
| 8 · Brook Linden (MF) | `brook-linden.png` |
| 9 · Bay Laurel (MF) | `bay-laurel.png` |
| 10 · Langford Ash (FW) | `langford-ash.png` |
| 11 · Escott Aspen (FW) | `escott-aspen.png` |
| 12 · Maxwell Mahogany (GK) | `maxwell-mahogany.png` |
| 13 · Bradford Ash (FW) | `bradford-ash.png` |
| 14 · Calder Elm (FW) | `calder-elm.png` |
| 15 · Laike Alder (DF) | `laike-alder.png` |
| 16 · Tahoma Sequoia (MF) | `tahoma-sequoia.png` |

### Orden de los Caballeros Templarios

Escudo: `emblems/go-kuro-no-kishidan.png`

| Jugador | Archivo |
|---|---|
| 1 · Lance Speares (GK) | `lance-speares.png` |
| 2 · Clay Moor (DF) | `clay-moor.png` |
| 3 · Nun Chuck (DF) | `nun-chuck.png` |
| 4 · Dirk Anlace (DF) | `dirk-anlace.png` |
| 5 · Spike Stiletto (DF) | `spike-stiletto.png` |
| 6 · Jack Knife (MF) | `jack-knife.png` |
| 7 · Bilbo Baton (MF) | `bilbo-baton.png` |
| 8 · Bayonet Gunne (MF) | `bayonet-gunne.png` |
| 9 · Howie Itzer (FW) | `howie-itzer.png` |
| 10 · Victor Blade (FW) | `victor-blade.png` |
| 11 · Flam Berger (FW) | `flam-berger.png` |
| 12 · Matt Chetty (GK) | `matt-chetty.png` |
| 13 · Harold Shields (FW) | `harold-shields.png` |
| 14 · Hal Byrd (MF) | `hal-byrd.png` |
| 15 · Morgan Stern (DF) | `morgan-stern.png` |
| 16 · Roman Ballista (MF) | `roman-ballista.png` |

### Colegio Poderosa Fe

Escudo: `emblems/go-mannouzaka.png`

| Jugador | Archivo |
|---|---|
| 1 · Aum Nirvana (GK) | `aum-nirvana.png` |
| 2 · Adamant Walhalla (DF) | `adamant-walhalla.png` |
| 3 · Omega Elysium (DF) | `omega-elysium.png` |
| 4 · Fürimmer Jung (DF) | `f-rimmer-jung.png` |
| 5 · Zenith Shangrila (DF) | `zenith-shangrila.png` |
| 6 · Optimum Limbo (MF) | `optimum-limbo.png` |
| 7 · Panacea Utopia (MF) | `panacea-utopia.png` |
| 8 · Acme Rapture (MF) | `acme-rapture.png` |
| 9 · Ultima Nextworld (FW) | `ultima-nextworld.png` |
| 10 · Maxim Millennium (FW) | `maxim-millennium.png` |
| 11 · Infinity Beyond (FW) | `infinity-beyond.png` |
| 12 · Apex Paradiso (GK) | `apex-paradiso.png` |
| 13 · Pearl Gates (FW) | `pearl-gates.png` |
| 14 · Perpetuo Xanadu (MF) | `perpetuo-xanadu.png` |
| 15 · Sempiterno Bliss (MF) | `sempiterno-bliss.png` |
| 16 · Myriad Arcadia (DF) | `myriad-arcadia.png` |

### Colmillos del Norte

Escudo: `emblems/go-northern-fang.png`

| Jugador | Archivo |
|---|---|
| 1 · Brutus Nastion (GK) | `brutus-nastion.png` |
| 2 · Linder Loper (DF) | `linder-loper.png` |
| 3 · Jude Osbourne (DF) | `jude-osbourne.png` |
| 4 · Locke Saflowe (DF) | `locke-saflowe.png` |
| 5 · Nate Gobby (DF) | `nate-gobby.png` |
| 6 · Reggie Alldark (MF) | `reggie-alldark.png` |
| 7 · Bill Froger (MF) | `bill-froger.png` |
| 8 · Romeo Fitzroy (MF) | `romeo-fitzroy.png` |
| 9 · Caesar Lionheart (MF) | `caesar-lionheart.png` |
| 10 · Stan Roller (FW) | `stan-roller.png` |
| 11 · Bracknell Forge (FW) | `bracknell-forge.png` |

### Equipo B del Instituto Raimon (GO)

Escudo: `emblems/go-raimon-2gun.png`

| Jugador | Archivo |
|---|---|
| 1 · Montaña Tábano (GK) | `monta-a-t-bano.png` |
| 2 · Tom Gato (DF) | `tom-gato.png` |
| 3 · Joaquín Coronado (DF) | `joaqu-n-coronado.png` |
| 4 · Conant Ó Briain (DF) | `conant-briain.png` |
| 5 · Sirius Starsky (DF) | `sirius-starsky.png` |
| 6 · Shunsuke Aoyama (MF) | `shunsuke-aoyama.png` |
| 7 · Bucky Woodchuck (MF) | `bucky-woodchuck.png` |
| 8 · Punkie Mahican (MF) | `punkie-mahican.png` |
| 9 · Hugues Baudet (MF) | `hugues-baudet.png` |
| 10 · Jagur Meister (FW) | `jagur-meister.png` |
| 11 · Friedrich Schiller (FW) | `friedrich-schiller.png` |
| 12 · Adarn Shame (GK) | `adarn-shame.png` |
| 13 · Ota Shape (DF) | `ota-shape.png` |
| 14 · Nogo Sarikid (MF) | `nogo-sarikid.png` |

### Colegio Monte Olimpo

Escudo: `emblems/go-seidouzan.png`

| Jugador | Archivo |
|---|---|
| 1 · Theo Divine (GK) | `theo-divine.png` |
| 2 · Mnemo Pool (DF) | `mnemo-pool.png` |
| 3 · Perses Destroyer (DF) | `perses-destroyer.png` |
| 4 · Iapetus Pierce (DF) | `iapetus-pierce.png` |
| 5 · Phoebus Moonlight (DF) | `phoebus-moonlight.png` |
| 6 · Rae Godmother (MF) | `rae-godmother.png` |
| 7 · Hyperion Wise (MF) | `hyperion-wise.png` |
| 8 · Cronus Fourseasons (MF) | `cronus-fourseasons.png` |
| 9 · Oceanus Worldstream (MF) | `oceanus-worldstream.png` |
| 10 · Coeus Heavens (FW) | `coeus-heavens.png` |
| 11 · Tet Aqua (FW) | `tet-aqua.png` |
| 12 · Eos Dawn (GK) | `eos-dawn.png` |
| 13 · Pallas Brandish (DF) | `pallas-brandish.png` |
| 14 · Themis Law (MF) | `themis-law.png` |
| 15 · Atlas Carrier (FW) | `atlas-carrier.png` |
| 16 · Orion Hunter (MF) | `orion-hunter.png` |

### Instituto Raimon (GO)

Escudo: `emblems/go-shinsei-raimon.png`

| Jugador | Archivo |
|---|---|
| 1 · Samguk Han (GK) | `samguk-han.png` |
| 2 · Subaru Honda (DF) | `subaru-honda.png` |
| 3 · Gabriel Garcia (DF) | `gabriel-garcia.png` |
| 4 · Wanli Changcheng (DF) | `wanli-changcheng.png` |
| 5 · Jean-Pierre Lapin (DF) | `jean-pierre-lapin.png` |
| 6 · Adé Kébé (MF) | `ad-k-b.png` |
| 7 · Eugene Peabody (MF) | `eugene-peabody.png` |
| 8 · Arion Sherwind (MF) | `arion-sherwind.png` |
| 9 · Riccardo Di Rigo (MF) | `riccardo-di-rigo.png` |
| 10 · Victor Blade (FW) | `victor-blade.png` |
| 11 · Michael Ballzack (FW) | `michael-ballzack.png` |
| 12 · Shunsuke Aoyama (MF) | `shunsuke-aoyama.png` |
| 13 · Hugues Baudet (MF) | `hugues-baudet.png` |
| 14 · Ryoma Nishiki (MF) | `ryoma-nishiki.png` |
| 15 · Aitor Cazador (DF) | `aitor-cazador.png` |
| 16 · Lucian Dark (FW) | `lucian-dark.png` |

### Garras del Sur

Escudo: `emblems/go-southern-claw.png`

| Jugador | Archivo |
|---|---|
| 1 · Xavier Shotwell (GK) | `xavier-shotwell.png` |
| 2 · Crimson Wiseman (DF) | `crimson-wiseman.png` |
| 3 · Linden Haregrove (DF) | `linden-haregrove.png` |
| 4 · Jared Dapplegrey (DF) | `jared-dapplegrey.png` |
| 5 · Keith Wellington (DF) | `keith-wellington.png` |
| 6 · Cirrus Whisp (MF) | `cirrus-whisp.png` |
| 7 · Gamal Everlast (MF) | `gamal-everlast.png` |
| 8 · Sandy Dryhill (MF) | `sandy-dryhill.png` |
| 9 · Dryden Zephyr (MF) | `dryden-zephyr.png` |
| 10 · Solomon Roundhay (FW) | `solomon-roundhay.png` |
| 11 · Harry Dwind (FW) | `harry-dwind.png` |

### Colegio Concertado Vía Láctea

Escudo: `emblems/go-tengawara.png`

| Jugador | Archivo |
|---|---|
| 1 · Starbuck Rogers (GK) | `starbuck-rogers.png` |
| 2 · Worff Chewback (DF) | `worff-chewback.png` |
| 3 · Dart H. Cylon (DF) | `dart-h-cylon.png` |
| 4 · Scotty O'Brien (DF) | `scotty-o-brien.png` |
| 5 · Billy-Lee Adarma (MF) | `billy-lee-adarma.png` |
| 6 · Zaphod Riker (MF) | `zaphod-riker.png` |
| 7 · Cyber Dalekman (MF) | `cyber-dalekman.png` |
| 8 · Lucas Skywalk (MF) | `lucas-skywalk.png` |
| 9 · Jimmy Kyrk (FW) | `jimmy-kyrk.png` |
| 10 · Harkness Torchwood (FW) | `harkness-torchwood.png` |
| 11 · Jean-Luc Janeway (FW) | `jean-luc-janeway.png` |
| 12 · Wesley Sheridan (GK) | `wesley-sheridan.png` |
| 13 · Sithri Peon (DF) | `sithri-peon.png` |
| 14 · Isaac Binks (DF) | `isaac-binks.png` |
| 15 · Carl Rissian (MF) | `carl-rissian.png` |
| 16 · Robert Affett (FW) | `robert-affett.png` |

### Luz Eterna

Escudo: `emblems/go-unlimited-shining.png`

| Jugador | Archivo |
|---|---|
| 1 · Albion Lumina (GK) | `albion-lumina.png` |
| 2 · Candido Glow (DF) | `candido-glow.png` |
| 3 · Dwight Whittaker (DF) | `dwight-whittaker.png` |
| 4 · Beamer Daye (DF) | `beamer-daye.png` |
| 5 · Chandler Blanc (DF) | `chandler-blanc.png` |
| 6 · Beacon Noor (MF) | `beacon-noor.png` |
| 7 · Dawntavius Spectrum (MF) | `dawntavius-spectrum.png` |
| 8 · Brighton Spark (MF) | `brighton-spark.png` |
| 9 · Laban Lux (MF) | `laban-lux.png` |
| 10 · Bailong (FW) | `bailong.png` |
| 11 · Filbert Weissman (FW) | `filbert-weissman.png` |

### Equipo Zero

Escudo: `emblems/go-zero.png`

| Jugador | Archivo |
|---|---|
| 1 · Albion Lumina (GK) | `albion-lumina.png` |
| 2 · Dwight Whittaker (DF) | `dwight-whittaker.png` |
| 3 · Candido Glow (DF) | `candido-glow.png` |
| 4 · Beamer Daye (DF) | `beamer-daye.png` |
| 5 · Blake Obscura (DF) | `blake-obscura.png` |
| 6 · Yang (FW) | `yang.png` |
| 7 · Tynan Crowe (MF) | `tynan-crowe.png` |
| 8 · Shady Shwartz (MF) | `shady-shwartz.png` |
| 9 · Dawntavius Spectrum (MF) | `dawntavius-spectrum.png` |
| 10 · Bailong (FW) | `bailong.png` |
| 11 · Tezcat (FW) | `tezcat.png` |
| 12 · Glaucous Gull (FW) | `glaucous-gull.png` |
| 13 · Ashley Silverwood (DF) | `ashley-silverwood.png` |
| 14 · Pinkus Mountbatten (MF) | `pinkus-mountbatten.png` |
| 15 · Flint Charcoal (MF) | `flint-charcoal.png` |
| 16 · Gus Martin (DF) | `gus-martin.png` |

### Big Bang

Escudo: `emblems/gx-big-bang.png`

| Jugador | Archivo |
|---|---|
| 1 · Strem Goozer (GK) | `strem-goozer.png` |
| 2 · Fow Tudas (DF) | `fow-tudas.png` |
| 3 · Cherio Pardon (DF) | `cherio-pardon.png` |
| 4 · Bambaros Tower (DF) | `bambaros-tower.png` |
| 5 · Zartan Walder (DF) | `zartan-walder.png` |
| 6 · Zyne Hanging (DF) | `zyne-hanging.png` |
| 7 · Madison Barada (DF) | `madison-barada.png` |
| 8 · Bindal Hermit (MF) | `bindal-hermit.png` |
| 9 · Astro Justin (MF) | `astro-justin.png` |
| 10 · Circulus (FW) | `circulus.png` |
| 11 · Joss Fool (MF) | `joss-fool.png` |

### Big Waves (GO)

Escudo: `emblems/gx-big-waves-go.png`

| Jugador | Archivo |
|---|---|
| 1 · Jude Gordon (GK) | `jude-gordon.png` |
| 2 · Owe Noyster (DF) | `owe-noyster.png` |
| 3 · Whaly Walker (DF) | `whaly-walker.png` |
| 4 · Sunny Fishton (DF) | `sunny-fishton.png` |
| 5 · Clem Chowdry (DF) | `clem-chowdry.png` |
| 6 · Oscar Squidows (MF) | `oscar-squidows.png` |
| 7 · Marsha Ark (MF) | `marsha-ark.png` |
| 8 · Cole (MF) | `cole.png` |
| 9 · Amanda Ray (MF) | `amanda-ray.png` |
| 10 · Lob Stark (FW) | `lob-stark.png` |
| 11 · Octa (FW) | `octa.png` |
| 12 · Orlando Sherman (MF) | `orlando-sherman.png` |

### Earth Eleven

Escudo: `emblems/gx-earth-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · Terry Archibald (GK) | `terry-archibald.png` |
| 2 · Trina Verdure (DF) | `trina-verdure.png` |
| 3 · Keenan Sharpe (DF) | `keenan-sharpe.png` |
| 4 · Zippy Lerner (DF) | `zippy-lerner.png` |
| 5 · Frank Foreman (DF) | `frank-foreman.png` |
| 6 · Buddy Fury (MF) | `buddy-fury.png` |
| 7 · Cerise Blossom (MF) | `cerise-blossom.png` |
| 8 · Arion Sherwind (MF) | `arion-sherwind.png` |
| 9 · Riccardo Di Rigo (MF) | `riccardo-di-rigo.png` |
| 10 · Victor Blade (FW) | `victor-blade.png` |
| 11 · Falco Flashman (FW) | `falco-flashman.png` |
| 14 · Buddy Fury (MF) | `buddy-fury-gx-kusaka-b.png` |
| 15 · Maneuver Gibbs (FW) | `maneuver-gibbs.png` |
| 16 · Falco Flashman (FW) | `falco-flashman-gx-matatagi-p.png` |
| 18 · Zack Avalon (FW) | `zack-avalon.png` |
| 20 · Jean-Pierre Lapin (GK) | `jean-pierre-lapin.png` |

### Falam Medius

Escudo: `emblems/gx-faram-dite.png`

| Jugador | Archivo |
|---|---|
| 1 · Argon Bulgess (GK) | `argon-bulgess.png` |
| 2 · Xenon Reith (DF) | `xenon-reith.png` |
| 3 · Ogar Circes (DF) | `ogar-circes.png` |
| 4 · Radon Mons (DF) | `radon-mons.png` |
| 5 · Selenia (MF) | `selenia.png` |
| 6 · Rondula Flehl (MF) | `rondula-flehl.png` |
| 7 · Neon (MF) | `neon.png` |
| 8 · Ruger Baran (FW) | `ruger-baran.png` |
| 9 · Gandares Baran (FW) | `gandares-baran.png` |
| 10 · Bala Gasgula (FW) | `bala-gasgula.png` |
| 11 · Brimstone (FW) | `brimstone.png` |
| 12 · Ray Dark (FW) | `ray-dark.png` |

### Dragones de Fuego (GO)

Escudo: `emblems/gx-fire-dragon-go.png`

| Jugador | Archivo |
|---|---|
| 1 · Do-Hyeon Nam (GK) | `do-hyeon-nam.png` |
| 2 · Shinjae Choi (DF) | `shinjae-choi.png` |
| 3 · Noh-Bae (DF) | `noh-bae.png` |
| 4 · Yongjin Seo (DF) | `yongjin-seo.png` |
| 5 · Ujin Shin (DF) | `ujin-shin.png` |
| 6 · Gunwoo Yang (MF) | `gunwoo-yang.png` |
| 7 · Jihun Song (MF) | `jihun-song.png` |
| 8 · Hwang (MF) | `hwang.png` |
| 9 · Soyeon Sim (FW) | `soyeon-sim.png` |
| 10 · Jun-Yeong Lee (FW) | `jun-yeong-lee.png` |
| 11 · Joo-Won (FW) | `joo-won.png` |
| 12 · Changsu Choi (MF) | `changsu-choi.png` |

### Los Magmavís

Escudo: `emblems/gx-gurdon-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · Aoba Gyr (GK) | `aoba-gyr.png` |
| 2 · Mayon (DF) | `mayon.png` |
| 3 · Merapil Sekretair (DF) | `merapil-sekretair.png` |
| 4 · Mistis (MF) | `mistis.png` |
| 5 · Nevado (MF) | `nevado.png` |
| 6 · Etna (MF) | `etna.png` |
| 7 · Proman (MF) | `proman.png` |
| 8 · Cotopax (FW) | `cotopax.png` |
| 9 · Vesuvian (FW) | `vesuvian.png` |
| 10 · Tair (FW) | `tair.png` |
| 11 · Nyira (FW) | `nyira.png` |
| 12 · Caldera Dorne (MF) | `caldera-dorne.png` |

### Inside Silver

Escudo: `emblems/gx-inside-silver.png`

| Jugador | Archivo |
|---|---|
| 1 · Ezra Gin (GK) | `ezra-gin.png` |
| 2 · Silva Gin (DF) | `silva-gin.png` |
| 3 · Argus Gin (DF) | `argus-gin.png` |
| 4 · Micah Gin (DF) | `micah-gin.png` |
| 5 · Maxter Gin (DF) | `maxter-gin.png` |
| 6 · Casey Gin (MF) | `casey-gin.png` |
| 7 · Consy Gin (MF) | `consy-gin.png` |
| 8 · Shari Gin (MF) | `shari-gin.png` |
| 9 · Colin Gin (FW) | `colin-gin.png` |
| 10 · Nathas Gin (FW) | `nathas-gin.png` |
| 11 · Zane Gin (FW) | `zane-gin.png` |

### Flota Ixar

Escudo: `emblems/gx-ixal-fleet.png`

| Jugador | Archivo |
|---|---|
| 1 · Phobos (GK) | `phobos.png` |
| 2 · Aegir Cepheid (DF) | `aegir-cepheid.png` |
| 3 · Meteo Garnet (DF) | `meteo-garnet.png` |
| 4 · Deimos Lepton (DF) | `deimos-lepton.png` |
| 5 · Ymir Catena (DF) | `ymir-catena.png` |
| 6 · Sinope Linea (DF) | `sinope-linea.png` |
| 7 · Tarvos Boson (MF) | `tarvos-boson.png` |
| 8 · Dione (MF) | `dione.png` |
| 9 · Despina (FW) | `despina.png` |
| 10 · Ozrock Boldar (FW) | `ozrock-boldar.png` |
| 11 · Loge Colles (FW) | `loge-colles.png` |

### Muay Tigers

Escudo: `emblems/gx-mach-tiger.png`

| Jugador | Archivo |
|---|---|
| 1 · Udom (GK) | `udom.png` |
| 2 · Yuth Poonlarp (DF) | `yuth-poonlarp.png` |
| 3 · Napa (DF) | `napa.png` |
| 4 · Naid Sirisukha (DF) | `naid-sirisukha.png` |
| 5 · Sulada (MF) | `sulada.png` |
| 6 · Suchart (MF) | `suchart.png` |
| 7 · Nawarat (MF) | `nawarat.png` |
| 8 · Mei (MF) | `mei.png` |
| 9 · Bak (MF) | `bak.png` |
| 10 · Kaolan (MF) | `kaolan.png` |
| 11 · Thanakorn Jaa (FW) | `thanakorn-jaa.png` |
| 12 · Rashiri Saran (GK) | `rashiri-saran.png` |

### Sombras Terribles

Escudo: `emblems/gx-osoroshii-kage.png`

| Jugador | Archivo |
|---|---|
| 1 · Osoroshii Kage 1 (GK) | `osoroshii-kage-1.png` |
| 2 · Osoroshii Kage 2 (DF) | `osoroshii-kage-2.png` |
| 3 · Osoroshii Kage 3 (DF) | `osoroshii-kage-3.png` |
| 4 · Osoroshii Kage 4 (DF) | `osoroshii-kage-4.png` |
| 5 · Osoroshii Kage 5 (DF) | `osoroshii-kage-5.png` |
| 6 · Osoroshii Kage 6 (MF) | `osoroshii-kage-6.png` |
| 7 · Osoroshii Kage 7 (MF) | `osoroshii-kage-7.png` |
| 8 · Osoroshii Kage 8 (MF) | `osoroshii-kage-8.png` |
| 9 · Osoroshii Kage 9 (MF) | `osoroshii-kage-9.png` |
| 10 · Osoroshii Kage 10 (FW) | `osoroshii-kage-10.png` |
| 11 · Osoroshii Kage 11 (FW) | `osoroshii-kage-11.png` |

### Los Fertilia

Escudo: `emblems/gx-ratoniik-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · Ceram (GK) | `ceram.png` |
| 2 · Romborina Drohn (DF) | `romborina-drohn.png` |
| 3 · Heterocera (DF) | `heterocera.png` |
| 4 · Formiga (MF) | `formiga.png` |
| 5 · Mantodea (MF) | `mantodea.png` |
| 6 · Lepidoptera (MF) | `lepidoptera.png` |
| 7 · Vespa (FW) | `vespa.png` |
| 8 · Caelif (MF) | `caelif.png` |
| 9 · Lucan (MF) | `lucan.png` |
| 10 · Banda Crix (MF) | `banda-crix.png` |
| 11 · Schisto (FW) | `schisto.png` |
| 15 · Elater Clicka (FW) | `elater-clicka.png` |
| 15 · Sect Pheromona (DF) | `sect-pheromona.png` |
| 16 · Theraphos Tranchla (FW) | `theraphos-tranchla.png` |
| 21 · Banda Crix Junior (MF) | `banda-crix-junior.png` |

### Los Sílice

Escudo: `emblems/gx-sandorius-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · B'adaen (GK) | `b-adaen.png` |
| 2 · G'ob (DF) | `g-ob.png` |
| 3 · A'ddah (DF) | `a-ddah.png` |
| 4 · R'adji (DF) | `r-adji.png` |
| 5 · A'kra (DF) | `a-kra.png` |
| 6 · N'ameeb (DF) | `n-ameeb.png` |
| 7 · K'aran Uogu (MF) | `k-aran-uogu.png` |
| 8 · K'al (FW) | `k-al.png` |
| 9 · S'haha (FW) | `s-haha.png` |
| 10 · S'harqiyah (FW) | `s-harqiyah.png` |
| 11 · A'tac (FW) | `a-tac.png` |
| 12 · Zundar Zand (FW) | `zundar-zand.png` |

### Los Naiadi

Escudo: `emblems/gx-sazanaara-eleven.png`

| Jugador | Archivo |
|---|---|
| 1 · Van Tarel (GK) | `van-tarel.png` |
| 2 · Squalcha (DF) | `squalcha.png` |
| 3 · Sog (DF) | `sog.png` |
| 4 · Tinkel Urmia (MF) | `tinkel-urmia.png` |
| 5 · Plink Powai (MF) | `plink-powai.png` |
| 6 · Puddel (MF) | `puddel.png` |
| 7 · Sploosh Saroma (MF) | `sploosh-saroma.png` |
| 8 · Droplit (MF) | `droplit.png` |
| 9 · Plip Batur (FW) | `plip-batur.png` |
| 10 · Serban (FW) | `serban.png` |
| 11 · Plunk (FW) | `plunk.png` |
| 12 · Porco Umir (MF) | `porco-umir.png` |

### Los Cimitarras

Escudo: `emblems/gx-shamshir.png`

| Jugador | Archivo |
|---|---|
| 1 · Sultan (GK) | `sultan.png` |
| 2 · Shakir Zahir (DF) | `shakir-zahir.png` |
| 3 · Asad Gheisari (DF) | `asad-gheisari.png` |
| 4 · Batal (DF) | `batal.png` |
| 5 · Qamar Sadir (DF) | `qamar-sadir.png` |
| 6 · Khalil Haddaoui (MF) | `khalil-haddaoui.png` |
| 7 · Nazim (MF) | `nazim.png` |
| 8 · Tamir (MF) | `tamir.png` |
| 9 · Rashid (MF) | `rashid.png` |
| 10 · Said (FW) | `said.png` |
| 11 · Qasim Batal (FW) | `qasim-batal.png` |
| 12 · Marshi Amir (DF) | `marshi-amir.png` |

### Storm Wolves

Escudo: `emblems/gx-storm-wolf.png`

| Jugador | Archivo |
|---|---|
| 1 · Aleksei Karimov (GK) | `aleksei-karimov.png` |
| 2 · Server (DF) | `server.png` |
| 3 · Mirjalor Afonin (DF) | `mirjalor-afonin.png` |
| 4 · Yuri (DF) | `yuri.png` |
| 5 · Kenja Jo'rayev (DF) | `kenja-jo-rayev.png` |
| 6 · Leonid Mirzayev (MF) | `leonid-mirzayev.png` |
| 7 · Rustan (MF) | `rustan.png` |
| 8 · Aaron (MF) | `aaron.png` |
| 9 · Maksim Alimatov (FW) | `maksim-alimatov.png` |
| 10 · Dilshod (FW) | `dilshod.png` |
| 11 · Zafar (FW) | `zafar.png` |
| 12 · Nikolai Gagarin (FW) | `nikolai-gagarin.png` |

### Supernova

Escudo: `emblems/gx-supernova.png`

| Jugador | Archivo |
|---|---|
| 1 · Ashvina Bharani (GK) | `ashvina-bharani.png` |
| 2 · Hastar Savitar (DF) | `hastar-savitar.png` |
| 3 · Apas Mulan (DF) | `apas-mulan.png` |
| 4 · Soma Lobi (DF) | `soma-lobi.png` |
| 5 · Rudra Ardo (DF) | `rudra-ardo.png` |
| 6 · Bhaga Guni (DF) | `bhaga-guni.png` |
| 7 · Mitra Jeshu (MF) | `mitra-jeshu.png` |
| 8 · Indra Vayu (MF) | `indra-vayu.png` |
| 9 · Bass Danish (MF) | `bass-danish.png` |
| 10 · Ashley Sarpala (MF) | `ashley-sarpala.png` |
| 11 · Arculus Orbes (FW) | `arculus-orbes.png` |

### Sallys

Escudo: `emblems/ie1-ichibangai-sally-s.png`

| Jugador | Archivo |
|---|---|
| 1 · Suzanne Yuma (GK) | `suzanne-yuma.png` |
| 2 · T. Fielding (DF) | `t-fielding.png` |
| 3 · A. Lovely (DF) | `a-lovely.png` |
| 4 · Louis Hillside (DF) | `louis-hillside.png` |
| 5 · Ness Sheldon (DF) | `ness-sheldon.png` |
| 6 · Lizzy Squirrel (MF) | `lizzy-squirrel.png` |
| 7 · Kippy Jones (MF) | `kippy-jones.png` |
| 8 · F. Riversong (MF) | `f-riversong.png` |
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

### Royal Academy NEW

Escudo: `emblems/ie2-new-teikoku-gakuen.png`

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
| 12 · Bob Carlton (GK) | `bob-carlton.png` |
| 13 · Cliff Tomlinson (FW) | `cliff-tomlinson.png` |
| 14 · Jim Lawrenson (FW) | `jim-lawrenson.png` |
| 15 · Barry Potts (MF) | `barry-potts.png` |
| 16 · Steve Ingham (FW) | `steve-ingham.png` |

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
| 16 · Señora Hartland (GK) | `se-ora-hartland.png` |

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

### Ases Africanos

Escudo: `emblems/ie3-africa-daihyou.png`

| Jugador | Archivo |
|---|---|
| 1 · Zolani Baloi (GK) | `zolani-baloi.png` |
| 2 · Zephyr Vitesse (DF) | `zephyr-vitesse.png` |
| 3 · Jimi Gaines (DF) | `jimi-gaines.png` |
| 4 · Masego Molelo (DF) | `masego-molelo.png` |
| 5 · Cassius Tobler (DF) | `cassius-tobler.png` |
| 6 · Quint Hampton (MF) | `quint-hampton.png` |
| 7 · Maximino Cruz (MF) | `maximino-cruz.png` |
| 8 · Adam Marunga (MF) | `adam-marunga.png` |
| 9 · Anton Nortje (MF) | `anton-nortje.png` |
| 10 · Drago Hill (FW) | `drago-hill.png` |
| 11 · Melisizwe Zamani (FW) | `melisizwe-zamani.png` |
| 12 · Herschel De Villiers (FW) | `herschel-de-villiers.png` |
| 13 · Hector Helio (GK) | `hector-helio.png` |
| 14 · Ian Ferrum (DF) | `ian-ferrum.png` |
| 15 · Yasir Haddad (MF) | `yasir-haddad.png` |
| 16 · Reggie Ines (MF) | `reggie-ines.png` |

### Ases Asiáticos

Escudo: `emblems/ie3-asia-daihyou.png`

| Jugador | Archivo |
|---|---|
| 1 · Nasir Mustafa (GK) | `nasir-mustafa.png` |
| 2 · Sayid Armand (MF) | `sayid-armand.png` |
| 3 · Yusuf Massoud (MF) | `yusuf-massoud.png` |
| 4 · Ken Crackham (DF) | `ken-crackham.png` |
| 5 · Kjell Snapper (DF) | `kjell-snapper.png` |
| 6 · Bilal Kalil (DF) | `bilal-kalil.png` |
| 7 · Dolph Hensen (MF) | `dolph-hensen.png` |
| 8 · Zack Abdulla (FW) | `zack-abdulla.png` |
| 9 · Byron Love (MF) | `byron-love.png` |
| 10 · Changsu Choi (MF) | `changsu-choi.png` |
| 11 · Hamilton Reith (FW) | `hamilton-reith.png` |
| 12 · Gene Whalon (GK) | `gene-whalon.png` |
| 13 · Umi Hwang (DF) | `umi-hwang.png` |
| 14 · Claude Beacons (FW) | `claude-beacons.png` |
| 15 · Bryce Whitingale (FW) | `bryce-whitingale.png` |
| 16 · Dooyoon Hong (DF) | `dooyoon-hong.png` |

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

### Ángel Oscuro

Escudo: `emblems/ie3-dark-angel.png`

| Jugador | Archivo |
|---|---|
| 1 · Astaroth (GK) | `astaroth.png` |
| 2 · Behemoth (DF) | `behemoth.png` |
| 3 · Bael (DF) | `bael.png` |
| 4 · Nenel (DF) | `nenel.png` |
| 5 · Lephiel (DF) | `lephiel.png` |
| 6 · Malphas (MF) | `malphas.png` |
| 7 · Thanatos (FW) | `thanatos.png` |
| 8 · Gaiel (FW) | `gaiel.png` |
| 9 · Wenel (MF) | `wenel.png` |
| 10 · Destra (FW) | `destra.png` |
| 11 · Sanctus (FW) | `sanctus.png` |

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

### Ases Europeos

Escudo: `emblems/ie3-europe-daihyou.png`

| Jugador | Archivo |
|---|---|
| 1 · Gigi Blasi (GK) | `gigi-blasi.png` |
| 2 · Pierre Godin (DF) | `pierre-godin.png` |
| 3 · Lance Rawton (DF) | `lance-rawton.png` |
| 4 · Marco Maserati (DF) | `marco-maserati.png` |
| 5 · Lukas Schmidt (DF) | `lukas-schmidt.png` |
| 6 · Alexander Hausen (DF) | `alexander-hausen.png` |
| 7 · Paolo Bianchi (FW) | `paolo-bianchi.png` |
| 8 · Julien Rousseau (MF) | `julien-rousseau.png` |
| 9 · Samuel Mayo (FW) | `samuel-mayo.png` |
| 10 · Edgar Partinus (FW) | `edgar-partinus.png` |
| 11 · Phillip Owen (FW) | `phillip-owen.png` |
| 12 · Roland Pérec (MF) | `roland-p-rec.png` |
| 13 · Fermín Sánchez (GK) | `ferm-n-s-nchez.png` |
| 14 · Raffaele Generani (FW) | `raffaele-generani.png` |
| 15 · Miguel Pereira (MF) | `miguel-pereira.png` |
| 16 · Jonas Polk (MF) | `jonas-polk.png` |

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

### Ases Sudamericanos

Escudo: `emblems/ie3-nanbei-daihyou.png`

| Jugador | Archivo |
|---|---|
| 1 · Jorge Ortega (GK) | `jorge-ortega.png` |
| 2 · Julio Acosta (DF) | `julio-acosta.png` |
| 3 · Ramón Martínez (DF) | `ram-n-mart-nez.png` |
| 4 · Pablo Castillo (MF) | `pablo-castillo.png` |
| 5 · Roberto Torres (MF) | `roberto-torres.png` |
| 6 · Thiago Torres (DF) | `thiago-torres.png` |
| 7 · Leone Badigo (FW) | `leone-badigo.png` |
| 8 · Sergio Pérez (MF) | `sergio-p-rez.png` |
| 9 · Mac Robingo (FW) | `mac-robingo.png` |
| 10 · Coruja Cerezo (MF) | `coruja-cerezo.png` |
| 11 · Gato Carvalho (FW) | `gato-carvalho.png` |
| 12 · Leonardo Almeida (MF) | `leonardo-almeida.png` |
| 13 · Presa Passos (MF) | `presa-passos.png` |
| 14 · Formiga Clemens (DF) | `formiga-clemens.png` |
| 15 · Carlos Lagarto (DF) | `carlos-lagarto.png` |
| 16 · Falcão Da Silva (GK) | `falc-o-da-silva.png` |

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

### Pruebas de Selección - Equipo A

Escudo: `emblems/ie3-nippon-daihyou-kouho-a.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 3 · Jack Wallside (DF) | `jack-wallside.png` |
| 4 · Hurley Kane (DF) | `hurley-kane.png` |
| 7 · Archer Hawkins (DF) | `archer-hawkins.png` |
| 8 · Paul Peabody (DF) | `paul-peabody.png` |
| 9 · Shawn Froste (FW) | `shawn-froste.png` |
| 12 · Thor Stoutberg (MF) | `thor-stoutberg.png` |
| 16 · David Samford (FW) | `david-samford.png` |
| 17 · Kevin Dragonfly (FW) | `kevin-dragonfly.png` |
| 18 · Xavier Foster (FW) | `xavier-foster.png` |
| 19 · Marvin Murdock (FW) | `marvin-murdock.png` |
| 22 · Maxwell Carson (FW) | `maxwell-carson.png` |

### Pruebas de Selección - Equipo B

Escudo: `emblems/ie3-nippon-daihyou-kouho-b.png`

| Jugador | Archivo |
|---|---|
| 2 · Nathan Swift (DF) | `nathan-swift.png` |
| 5 · Tod Ironside (DF) | `tod-ironside.png` |
| 6 · Scott Banyan (DF) | `scott-banyan.png` |
| 8 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 11 · Austin Hobbes (FW) | `austin-hobbes.png` |
| 13 · Jordan Greenway (MF) | `jordan-greenway.png` |
| 14 · Jude Sharp (MF) | `jude-sharp.png` |
| 20 · Darren LaChance (GK) | `darren-lachance.png` |
| 21 · Peter Drent (DF) | `peter-drent.png` |
| 21 · Shadow Cimmerian (FW) | `shadow-cimmerian.png` |
| 22 · Maxwell Carson (FW) | `maxwell-carson.png` |
| 23 · Isaac Glass (FW) | `isaac-glass.png` |

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
| 13 · Enrico Oliviero (MF) | `enrico-oliviero.png` |
| 14 · Alessandro Rossa (MF) | `alessandro-rossa.png` |
| 15 · Giuseppe Cannavaro (DF) | `giuseppe-cannavaro.png` |
| 16 · Gianluca Zanardi (MF) | `gianluca-zanardi.png` |

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

### Ases Internacionales

Escudo: `emblems/ie3-sekai-daihyou.png`

| Jugador | Archivo |
|---|---|
| 1 · Hector Helio (GK) | `hector-helio.png` |
| 2 · Bilal Kalil (DF) | `bilal-kalil.png` |
| 3 · Alexander Hausen (DF) | `alexander-hausen.png` |
| 4 · Masego Molelo (DF) | `masego-molelo.png` |
| 5 · Thiago Torres (DF) | `thiago-torres.png` |
| 6 · Changsu Choi (MF) | `changsu-choi.png` |
| 7 · Dolph Hensen (MF) | `dolph-hensen.png` |
| 8 · Mac Robingo (FW) | `mac-robingo.png` |
| 9 · Paolo Bianchi (FW) | `paolo-bianchi.png` |
| 10 · Mark Krueger (MF) | `mark-krueger.png` |
| 11 · Edgar Partinus (FW) | `edgar-partinus.png` |
| 12 · Miguel Pereira (MF) | `miguel-pereira.png` |
| 13 · Julien Rousseau (MF) | `julien-rousseau.png` |
| 14 · Byron Love (MF) | `byron-love.png` |
| 15 · Gigi Blasi (GK) | `gigi-blasi.png` |
| 16 · Jimi Gaines (DF) | `jimi-gaines.png` |

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

### Ejército del Fénix Árabe

Escudo: `emblems/orion-arab-no-hi-no-tori-gundan.png`

| Jugador | Archivo |
|---|---|
| 1 · Falcon (GK) | `falcon.png` |
| 2 · Osprey Al-Bahar (DF) | `osprey-al-bahar.png` |
| 3 · Merlin Al-Yaman (DF) | `merlin-al-yaman.png` |
| 4 · Kestrel Al-Sahir (DF) | `kestrel-al-sahir.png` |
| 5 · Buzzard Al-Sahma (MF) | `buzzard-al-sahma.png` |
| 6 · Griffon Al-Qahir (MF) | `griffon-al-qahir.png` |
| 7 · Shrike Al-Jazzar (MF) | `shrike-al-jazzar.png` |
| 8 · Hawke Al-Bazzar (MF) | `hawke-al-bazzar.png` |
| 9 · Condor (FW) | `condor.png` |
| 10 · Perry Al-Surah (FW) | `perry-al-surah.png` |
| 11 · Robin Al-Ahmar (MF) | `robin-al-ahmar.png` |
| 14 · Harris Al-Suhra (MF) | `harris-al-suhra.png` |
| 14 · Anqa Qushchi (GK) | `anqa-qushchi.png` |
| 15 · Roc Nasr (GK) | `roc-nasr.png` |
| 16 · Eagle Al-Suhra (MF) | `eagle-al-suhra.png` |

### Bailarines Eternos

Escudo: `emblems/orion-eternal-dancers.png`

| Jugador | Archivo |
|---|---|
| 1 · Bolero Salimov (GK) | `bolero-salimov.png` |
| 2 · Kizomba Zakharov (DF) | `kizomba-zakharov.png` |
| 3 · Rumba Mansurov (DF) | `rumba-mansurov.png` |
| 4 · Merengue Muratov (DF) | `merengue-muratov.png` |
| 5 · Chacha Goncharov (DF) | `chacha-goncharov.png` |
| 6 · Hulan Nazarova (MF) | `hulan-nazarova.png` |
| 7 · Polkan Ismailov (MF) | `polkan-ismailov.png` |
| 8 · Jazzar Belikov (MF) | `jazzar-belikov.png` |
| 9 · Limbo Zakharov (MF) | `limbo-zakharov.png` |
| 10 · Samba Sokolov (MF) | `samba-sokolov.png` |
| 11 · Tango (FW) | `tango.png` |
| 14 · Cancan Popov (FW) | `cancan-popov.png` |
| 14 · Ballet Burkhanov (FW) | `ballet-burkhanov.png` |
| 15 · Carrie Ogrova (GK) | `carrie-ogrova.png` |
| 16 · Bhangra Makarov (MF) | `bhangra-makarov.png` |

### Guardianes de la Reina

Escudo: `emblems/orion-guardians-of-queen.png`

| Jugador | Archivo |
|---|---|
| 1 · Clorinda Luzzago (GK) | `clorinda-luzzago.png` |
| 2 · Camilla Gonzaga (DF) | `camilla-gonzaga.png` |
| 3 · Bellamante Medici (DF) | `bellamante-medici.png` |
| 4 · Bellona Orsini (DF) | `bellona-orsini.png` |
| 5 · Zerbino Savelli (MF) | `zerbino-savelli.png` |
| 6 · Dardinello Foscari (MF) | `dardinello-foscari.png` |
| 7 · Medoro Gritti (MF) | `medoro-gritti.png` |
| 8 · Grandazzo (MF) | `grandazzo.png` |
| 9 · Brandimarte Ruffo (FW) | `brandimarte-ruffo.png` |
| 10 · Dodone Barberini (FW) | `dodone-barberini.png` |
| 11 · Orlando (FW) | `orlando.png` |
| 12 · Oliviero Albizzi (GK) | `oliviero-albizzi.png` |
| 13 · Fantaghirò Petrucci (MF) | `fantaghir-petrucci.png` |
| 14 · Rinaldo Torelli (DF) | `rinaldo-torelli.png` |
| 15 · Marfisa Corsi (MF) | `marfisa-corsi.png` |
| 16 · Ruggiero Spinola (DF) | `ruggiero-spinola.png` |

### Inazuma Japón (Orion)

Escudo: `emblems/orion-inazuma-japan-orion.png`

| Jugador | Archivo |
|---|---|
| 1 · Mark Evans (GK) | `mark-evans.png` |
| 2 · Billy Miller (DF) | `billy-miller.png` |
| 3 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 4 · Shawn Froste (FW) | `shawn-froste.png` |
| 5 · Jude Sharp (MF) | `jude-sharp.png` |
| 6 · Nathan Swift (DF) | `nathan-swift.png` |
| 7 · Valentin Eisner (MF) | `valentin-eisner.png` |
| 8 · Sonny Wright (FW) | `sonny-wright.png` |
| 9 · Xavier Schiller (FW) | `xavier-schiller.png` |
| 10 · Axel Blaze (FW) | `axel-blaze.png` |
| 11 · Elliot Ember (FW) | `elliot-ember.png` |
| 12 · Adriano Donati (FW) | `adriano-donati.png` |
| 13 · Lucas Star (MF) | `lucas-star.png` |
| 13 · Lucas Star (MF) | `lucas-star-ok-hikaru.png` |
| 14 · Heath Moore (FW) | `heath-moore.png` |
| 15 · Xavier Foster (FW) | `xavier-foster.png` |
| 16 · Byron Love (MF) | `byron-love.png` |
| 17 · Cliff Parker (DF) | `cliff-parker.png` |

### Gigantes Invencibles

Escudo: `emblems/orion-muteki-no-giant.png`

| Jugador | Archivo |
|---|---|
| 1 · Salvador Castell (GK) | `salvador-castell.png` |
| 2 · Manuel Gutiérrez (DF) | `manuel-guti-rrez.png` |
| 3 · Dani Ramos (DF) | `dani-ramos.png` |
| 4 · Miguel Hontiveros (DF) | `miguel-hontiveros.png` |
| 5 · Álvaro Meléndez (MF) | `lvaro-mel-ndez.png` |
| 6 · Andrés Alonso (MF) | `andr-s-alonso.png` |
| 7 · José Mari González (MF) | `jos-mari-gonz-lez.png` |
| 8 · Chicho Muñoz (MF) | `chicho-mu-oz.png` |
| 9 · Leo Segarra (FW) | `leo-segarra.png` |
| 10 · Sergi Hernández (MF) | `sergi-hern-ndez.png` |
| 11 · Joan Asensi (FW) | `joan-asensi.png` |
| 14 · Raúl Parejo (MF) | `ra-l-parejo.png` |
| 14 · Pepe Ballester (FW) | `pepe-ballester.png` |
| 15 · Marcos Canales (MF) | `marcos-canales.png` |

### Navy Invader

Escudo: `emblems/orion-navy-invader.png`

| Jugador | Archivo |
|---|---|
| 1 · Bigman (GK) | `bigman.png` |
| 2 · Charmer (DF) | `charmer.png` |
| 3 · Scuba (DF) | `scuba.png` |
| 4 · Smokestack (DF) | `smokestack.png` |
| 5 · Judge (DF) | `judge.png` |
| 6 · Hunter (DF) | `hunter.png` |
| 7 · Yoga (MF) | `yoga.png` |
| 8 · Cobra (DF) | `cobra.png` |
| 9 · Mop (MF) | `mop.png` |
| 10 · Moai (FW) | `moai.png` |
| 11 · Hellion (FW) | `hellion.png` |
| 12 · Howler (GK) | `howler.png` |
| 15 · Wizard (MF) | `wizard.png` |
| 15 · René Gadé (FW) | `ren-gad.png` |
| 16 · Switch (FW) | `switch.png` |

### Olé de Samba

Escudo: `emblems/orion-ol-de-samba.png`

| Jugador | Archivo |
|---|---|
| 1 · Gonçalo (GK) | `gon-alo.png` |
| 2 · Bernardo (DF) | `bernardo.png` |
| 3 · Maceió (DF) | `macei.png` |
| 4 · João (DF) | `jo-o.png` |
| 5 · Luís (MF) | `lu-s.png` |
| 6 · Belo (MF) | `belo.png` |
| 7 · Igaçu (MF) | `iga-u.png` |
| 8 · Manaus (MF) | `manaus.png` |
| 9 · André (MF) | `andr.png` |
| 10 · Alegre (FW) | `alegre.png` |
| 11 · Rio (FW) | `rio.png` |
| 14 · Belém (DF) | `bel-m.png` |
| 14 · Cristiano Dabola (DF) | `cristiano-dabola.png` |
| 17 · Paulo (MF) | `paulo.png` |

### Chispas Perfectas

Escudo: `emblems/orion-perfect-spark.png`

| Jugador | Archivo |
|---|---|
| 1 · Gregory Fortin (GK) | `gregory-fortin.png` |
| 2 · Leonid Largov (DF) | `leonid-largov.png` |
| 3 · Boris Kaprichyov (DF) | `boris-kaprichyov.png` |
| 4 · Nikolai Glisanderov (DF) | `nikolai-glisanderov.png` |
| 5 · Igor Pitsikatov (MF) | `igor-pitsikatov.png` |
| 6 · Michael Vivacer (MF) | `michael-vivacer.png` |
| 7 · Konstantin Furyozov (MF) | `konstantin-furyozov.png` |
| 8 · Dmitri (MF) | `dmitri.png` |
| 9 · Alexander Allegrov (MF) | `alexander-allegrov.png` |
| 10 · Anton Kolosalyov (FW) | `anton-kolosalyov.png` |
| 11 · Yuri (FW) | `yuri.png` |
| 14 · Molev Misterioski (FW) | `molev-misterioski.png` |
| 15 · Marat Stakatov (MF) | `marat-stakatov.png` |
| 16 · Martemeli Prestov (MF) | `martemeli-prestov.png` |
| 16 · Martemeli Prestov (MF) | `martemeli-prestov-ok-lus.png` |
| 17 · Oleg Animatov (MF) | `oleg-animatov.png` |

### Bisonte Rojo

Escudo: `emblems/orion-red-bison.png`

| Jugador | Archivo |
|---|---|
| 1 · Park (GK) | `park.png` |
| 2 · Hwang Bull-gim (DF) | `hwang-bull-gim.png` |
| 3 · Kim Bull-bit (DF) | `kim-bull-bit.png` |
| 4 · Suna Bey-bull (DF) | `suna-bey-bull.png` |
| 5 · Han Bull-dang (DF) | `han-bull-dang.png` |
| 6 · Yeon Bull-say (MF) | `yeon-bull-say.png` |
| 7 · Lee Bull-gae (MF) | `lee-bull-gae.png` |
| 8 · Seok Tel-bull (MF) | `seok-tel-bull.png` |
| 9 · Shin Bull-kot (MF) | `shin-bull-kot.png` |
| 10 · Baek Bull-wo (FW) | `baek-bull-wo.png` |
| 11 · Lee San-bull (FW) | `lee-san-bull.png` |
| 12 · Ho Bull-tong (FW) | `ho-bull-tong.png` |
| 13 · Son Bull-gong (MF) | `son-bull-gong.png` |
| 14 · Harh Bull-gull (DF) | `harh-bull-gull.png` |
| 15 · An Min-su (MF) | `an-min-su.png` |

### Eclipse de Orión

Escudo: `emblems/orion-shadow-of-orion.png`

| Jugador | Archivo |
|---|---|
| 1 · Procyon (GK) | `procyon.png` |
| 2 · Tabit (DF) | `tabit.png` |
| 3 · Meissa (DF) | `meissa.png` |
| 4 · Saiph (DF) | `saiph.png` |
| 5 · Alnitak (MF) | `alnitak.png` |
| 6 · Alnilam (MF) | `alnilam.png` |
| 7 · Mintaka (MF) | `mintaka.png` |
| 8 · Bellatrix (MF) | `bellatrix.png` |
| 9 · Rigel (MF) | `rigel.png` |
| 10 · Jade Beor (FW) | `jade-beor.png` |
| 11 · Betelgeuse (FW) | `betelgeuse.png` |
| 14 · Sirius (DF) | `sirius.png` |
| 15 · Kappa (MF) | `kappa.png` |
| 17 · Hatysa (MF) | `hatysa.png` |

### Demonios Brillantes

Escudo: `emblems/orion-shining-satans.png`

| Jugador | Archivo |
|---|---|
| 1 · Pazuza Ross (GK) | `pazuza-ross.png` |
| 2 · Carlam Buer (DF) | `carlam-buer.png` |
| 3 · Damon Gorgon (DF) | `damon-gorgon.png` |
| 4 · Mortam Malius (DF) | `mortam-malius.png` |
| 5 · Dante Dusias (DF) | `dante-dusias.png` |
| 6 · Beel Zebub (MF) | `beel-zebub.png` |
| 7 · Malik Sinn (MF) | `malik-sinn.png` |
| 8 · Ian Qubus (MF) | `ian-qubus.png` |
| 9 · Beryl (MF) | `beryl.png` |
| 10 · Serge (FW) | `serge.png` |
| 11 · Aster Roth (FW) | `aster-roth.png` |
| 13 · Lu Jiver (MF) | `lu-jiver.png` |
| 14 · Zagan Barbatos (MF) | `zagan-barbatos.png` |
| 14 · Beryl (MF) | `beryl-ok-satan-mc.png` |
| 15 · Grant Grimoire (DF) | `grant-grimoire.png` |
| 16 · Baz Azel (GK) | `baz-azel.png` |

### Tropa Acrobática del Fútbol

Escudo: `emblems/orion-soccer-zatsugidan.png`

| Jugador | Archivo |
|---|---|
| 1 · Bruce Lau (GK) | `bruce-lau.png` |
| 2 · Cindy Fong (DF) | `cindy-fong.png` |
| 3 · Michelle Luo (DF) | `michelle-luo.png` |
| 4 · Sammo Tong (DF) | `sammo-tong.png` |
| 5 · David Liang (MF) | `david-liang.png` |
| 6 · Donnie Yang (MF) | `donnie-yang.png` |
| 7 · Bolo Cheung (MF) | `bolo-cheung.png` |
| 8 · Jackie Tan (MF) | `jackie-tan.png` |
| 9 · Jimmy Wongfu (MF) | `jimmy-wongfu.png` |
| 10 · Jet Long (FW) | `jet-long.png` |
| 11 · Stephen Chang (FW) | `stephen-chang.png` |
| 14 · Mars Hung (MF) | `mars-hung.png` |
| 14 · Wilson Ip (GK) | `wilson-ip.png` |
| 15 · Gordon Siu (DF) | `gordon-siu.png` |
| 15 · Lucy Wongfu (MF) | `lucy-wongfu.png` |

### Star Unicorn

Escudo: `emblems/orion-star-unicorn.png`

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

### Academia IA

Escudo: `emblems/vr-ai-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Eugenio Provost (GK) | `eugenio-provost.png` |
| 2 · Pradip Lurning (DF) | `pradip-lurning.png` |
| 3 · Talim Muskel (DF) | `talim-muskel.png` |
| 4 · Synthian Volkel (DF) | `synthian-volkel.png` |
| 5 · Randon Datta (DF) | `randon-datta.png` |
| 6 · Chayce Golana (DF) | `chayce-golana.png` |
| 7 · Annalisa Cubon (MF) | `annalisa-cubon.png` |
| 8 · Cleo Balbot (MF) | `cleo-balbot.png` |
| 9 · Reubel Kauntless (MF) | `reubel-kauntless.png` |
| 10 · Obert Deance (FW) | `obert-deance.png` |
| 11 · Zuzu Intel (FW) | `zuzu-intel.png` |
| 12 · Bren Techner (GK) | `bren-techner.png` |
| 13 · Cognus Sention (DF) | `cognus-sention.png` |
| 14 · Manila Brickit (FW) | `manila-brickit.png` |
| 15 · Nettie Neuralyn (DF) | `nettie-neuralyn.png` |
| 16 · Deacon Pewter (DF) | `deacon-pewter.png` |

### Secundaria Crosswind-Fauxshore

Escudo: `emblems/vr-batten-yokato.png`

| Jugador | Archivo |
|---|---|
| 1 · Mayen Harmet (GK) | `mayen-harmet.png` |
| 2 · Vinda Koral (DF) | `vinda-koral.png` |
| 3 · Susen Faircourt (DF) | `susen-faircourt.png` |
| 4 · Yarkin Cittey (DF) | `yarkin-cittey.png` |
| 5 · Budan Ashwell (MF) | `budan-ashwell.png` |
| 6 · Benton Zellner (MF) | `benton-zellner.png` |
| 7 · Hathea Calmell (MF) | `hathea-calmell.png` |
| 8 · Froclan Junn (MF) | `froclan-junn.png` |
| 9 · Ebiss Marlowe (MF) | `ebiss-marlowe.png` |
| 10 · Vashan Morell (FW) | `vashan-morell.png` |
| 11 · Itor Sheerman (FW) | `itor-sheerman.png` |
| 12 · Trevin Seabourne (DF) | `trevin-seabourne.png` |
| 13 · Jory Jinx (FW) | `jory-jinx.png` |
| 14 · Clementine Weston (MF) | `clementine-weston.png` |
| 15 · Orfreya Newcomb (DF) | `orfreya-newcomb.png` |
| 16 · Jakob Serveraw (GK) | `jakob-serveraw.png` |

### Destructores

Escudo: `emblems/vr-destroyers.png`

| Jugador | Archivo |
|---|---|
| 1 · Garruk Vynce (GK) | `garruk-vynce.png` |
| 2 · Xyron Madric (DF) | `xyron-madric.png` |
| 3 · Arden Drax (DF) | `arden-drax.png` |
| 4 · Simen Thorne (DF) | `simen-thorne.png` |
| 5 · Denowar Krell (MF) | `denowar-krell.png` |
| 6 · Prisca Grav (MF) | `prisca-grav.png` |
| 7 · Grenadier Deton (MF) | `grenadier-deton.png` |
| 8 · Declan Jaxor (MF) | `declan-jaxor.png` |
| 9 · Nebula Raime (FW) | `nebula-raime.png` |
| 10 · Keines Elvain (FW) | `keines-elvain.png` |
| 11 · Vector Vernam (FW) | `vector-vernam.png` |
| 12 · Zyphar Doar (DF) | `zyphar-doar.png` |
| 13 · Machina Dex (DF) | `machina-dex.png` |
| 14 · Rourik Bhatt (MF) | `rourik-bhatt.png` |
| 18 · Menox Kessler (FW) | `menox-kessler.png` |
| 20 · Crysis Murdok (GK) | `crysis-murdok.png` |

### Guardianas

Escudo: `emblems/vr-gatekeepers.png`

| Jugador | Archivo |
|---|---|
| 1 · Amara Myles (GK) | `amara-myles.png` |
| 2 · Vivian Calder (DF) | `vivian-calder.png` |
| 3 · Zora Selwick (DF) | `zora-selwick.png` |
| 4 · Ivy Celeste (DF) | `ivy-celeste.png` |
| 5 · Julietta Belamy (DF) | `julietta-belamy.png` |
| 6 · Jackie Mulligan (MF) | `jackie-mulligan.png` |
| 7 · Kendra Pierce (MF) | `kendra-pierce.png` |
| 8 · Trixie Bren (MF) | `trixie-bren.png` |
| 9 · Arwena Lark (FW) | `arwena-lark.png` |
| 10 · Lindalyn Berny (FW) | `lindalyn-berny.png` |
| 11 · Mira Lysander (FW) | `mira-lysander.png` |
| 12 · Keira Donnell (DF) | `keira-donnell.png` |
| 13 · Cecily Noire (DF) | `cecily-noire.png` |
| 14 · Norah Queensby (MF) | `norah-queensby.png` |
| 18 · Cressida Octavia (FW) | `cressida-octavia.png` |
| 20 · Catalina Riven (GK) | `catalina-riven.png` |

### Instituto Alpino (Victory Road)

Escudo: `emblems/vr-hakuren-victory-road.png`

| Jugador | Archivo |
|---|---|
| 1 · Gael Vehemaint (GK) | `gael-vehemaint.png` |
| 2 · Targan Snowbringer (DF) | `targan-snowbringer.png` |
| 3 · Berta Brunche (DF) | `berta-brunche.png` |
| 4 · Mateo Potensio (DF) | `mateo-potensio.png` |
| 5 · Ivar Trialton (DF) | `ivar-trialton.png` |
| 6 · Anastasia Mingler (MF) | `anastasia-mingler.png` |
| 7 · Hail Homestead (MF) | `hail-homestead.png` |
| 8 · Fergat Silverpine (MF) | `fergat-silverpine.png` |
| 9 · Arlo Galbrash (FW) | `arlo-galbrash.png` |
| 10 · Lev Langvil (FW) | `lev-langvil.png` |
| 11 · Wren Habilton (FW) | `wren-habilton.png` |
| 12 · Fifi Frostkin (GK) | `fifi-frostkin.png` |
| 13 · Yetzy Klaus (DF) | `yetzy-klaus.png` |
| 14 · Elon Entremet (DF) | `elon-entremet.png` |
| 15 · Zain Blizzard (MF) | `zain-blizzard.png` |
| 16 · Bayard Boreas (FW) | `bayard-boreas.png` |

### Secundaria Northbright

Escudo: `emblems/vr-hokuyou-gakuen.png`

| Jugador | Archivo |
|---|---|
| 1 · Milo Rankin (GK) | `milo-rankin.png` |
| 2 · Peake Fletcher (DF) | `peake-fletcher.png` |
| 3 · Sentry Scarborough (DF) | `sentry-scarborough.png` |
| 4 · Autry Rogers (DF) | `autry-rogers.png` |
| 5 · Bodhi Field (MF) | `bodhi-field.png` |
| 6 · Chase Winthrop (MF) | `chase-winthrop.png` |
| 7 · Hawky Savard (MF) | `hawky-savard.png` |
| 8 · Taliesin Greenhunt (MF) | `taliesin-greenhunt.png` |
| 9 · Ivan Mercer (MF) | `ivan-mercer.png` |
| 10 · Erdem Barath (FW) | `erdem-barath.png` |
| 11 · Nikas Himmelstein (FW) | `nikas-himmelstein.png` |
| 12 · Hugh Pronghorn (FW) | `hugh-pronghorn.png` |
| 13 · Everett Shipman (MF) | `everett-shipman.png` |
| 14 · Armin Marshall (GK) | `armin-marshall.png` |
| 15 · Conley Quiver (DF) | `conley-quiver.png` |
| 16 · Denzel Harvest (FW) | `denzel-harvest.png` |

### Instituto Lawcrest

Escudo: `emblems/vr-houreikan.png`

| Jugador | Archivo |
|---|---|
| 1 · Rufery Faire (GK) | `rufery-faire.png` |
| 2 · Willard Headdon (DF) | `willard-headdon.png` |
| 3 · Eames Rapport (DF) | `eames-rapport.png` |
| 4 · Gusto Reitonly (DF) | `gusto-reitonly.png` |
| 5 · Normon Peeveton (DF) | `normon-peeveton.png` |
| 6 · Prudence Witt (MF) | `prudence-witt.png` |
| 7 · Dion Arbiter (MF) | `dion-arbiter.png` |
| 8 · Cordelia Collison (MF) | `cordelia-collison.png` |
| 9 · Norwin Naeve (FW) | `norwin-naeve.png` |
| 10 · Faust Fennrick (FW) | `faust-fennrick.png` |
| 11 · Adamas Quarell (FW) | `adamas-quarell.png` |
| 12 · Brie Brillante (GK) | `brie-brillante.png` |
| 13 · Kieran Knavenly (DF) | `kieran-knavenly.png` |
| 14 · Alzen Wasruff (DF) | `alzen-wasruff.png` |
| 15 · Fabricius Cator (MF) | `fabricius-cator.png` |
| 16 · Recco Rectenwald (FW) | `recco-rectenwald.png` |

### Instituto Visión Noble

Escudo: `emblems/vr-ijinmei-bundou.png`

| Jugador | Archivo |
|---|---|
| 1 · Chat Baltauk (GK) | `chat-baltauk.png` |
| 2 · Elric Spiech (DF) | `elric-spiech.png` |
| 3 · Habib Liomont (DF) | `habib-liomont.png` |
| 4 · Histrion Etcher (DF) | `histrion-etcher.png` |
| 5 · Nelvin Dustrie (MF) | `nelvin-dustrie.png` |
| 6 · Keepie Upshire (MF) | `keepie-upshire.png` |
| 7 · Jorna Privinski (MF) | `jorna-privinski.png` |
| 8 · Marcelline Memoir (MF) | `marcelline-memoir.png` |
| 9 · Staton Folhard (MF) | `staton-folhard.png` |
| 10 · Aurelio Auditus (FW) | `aurelio-auditus.png` |
| 11 · Wilhelmina Goforth (FW) | `wilhelmina-goforth.png` |
| 12 · Basil Wanderbilt (FW) | `basil-wanderbilt.png` |
| 13 · Odell Farley (DF) | `odell-farley.png` |
| 14 · Viki Devine (MF) | `viki-devine.png` |
| 15 · Horatio Tickner (DF) | `horatio-tickner.png` |
| 16 · Barney Snellman (GK) | `barney-snellman.png` |

### Secundaria Stormridge

Escudo: `emblems/vr-keizen-arashiyama.png`

| Jugador | Archivo |
|---|---|
| 1 · Kiona Blackwell (GK) | `kiona-blackwell.png` |
| 2 · Lennox Portsman (DF) | `lennox-portsman.png` |
| 3 · Kaz Bloomfield (DF) | `kaz-bloomfield.png` |
| 4 · Govin Castlehoven (DF) | `govin-castlehoven.png` |
| 5 · Floramira Pagotta (MF) | `floramira-pagotta.png` |
| 6 · Alistar Montero (MF) | `alistar-montero.png` |
| 7 · Elijah Singleton (MF) | `elijah-singleton.png` |
| 8 · Rohan Snatchett (MF) | `rohan-snatchett.png` |
| 9 · Umbren Lightwood (FW) | `umbren-lightwood.png` |
| 10 · Blaine Westbrook (FW) | `blaine-westbrook.png` |
| 11 · Marinus Courier (FW) | `marinus-courier.png` |
| 12 · Drexel Kixley (DF) | `drexel-kixley.png` |
| 13 · Volk Lorius (MF) | `volk-lorius.png` |
| 14 · Dawsey Geistfeld (FW) | `dawsey-geistfeld.png` |
| 15 · Rael Abbeybogy (MF) | `rael-abbeybogy.png` |
| 16 · Zelane Whitlow (GK) | `zelane-whitlow.png` |

### Academia Orchid

Escudo: `emblems/vr-meiran-gakuin.png`

| Jugador | Archivo |
|---|---|
| 1 · Lilia Charmont (GK) | `lilia-charmont.png` |
| 2 · Talia Jester (GK) | `talia-jester.png` |
| 3 · Evelyn Hale (DF) | `evelyn-hale.png` |
| 4 · Margie Frostveil (DF) | `margie-frostveil.png` |
| 5 · Selene Trance (MF) | `selene-trance.png` |
| 6 · Galia Flair (MF) | `galia-flair.png` |
| 7 · Eliza Florence (MF) | `eliza-florence.png` |
| 8 · Adelina Gearhart (FW) | `adelina-gearhart.png` |
| 9 · Clarisse Luxe (FW) | `clarisse-luxe.png` |
| 10 · Elyse Reign (MF) | `elyse-reign.png` |
| 11 · Celina Lavelle (FW) | `celina-lavelle.png` |
| 12 · Elara Silvane (DF) | `elara-silvane.png` |
| 13 · Kiyora Asakiri (MF) | `kiyora-asakiri.png` |
| 14 · Lenora Graves (FW) | `lenora-graves.png` |
| 15 · Liliane Alban (FW) | `liliane-alban.png` |
| 16 · Amara Winslow (DF) | `amara-winslow.png` |

### Vendedores de South Cirrus

Escudo: `emblems/vr-nagumohara-shopkeepers.png`

| Jugador | Archivo |
|---|---|
| 1 · Terra Hillcroft (GK) | `terra-hillcroft.png` |
| 2 · Marlin Sharkey (DF) | `marlin-sharkey.png` |
| 3 · Mirina Mackrell (DF) | `mirina-mackrell.png` |
| 4 · Alvaro Ventura (DF) | `alvaro-ventura.png` |
| 5 · Yelena Poplawska (DF) | `yelena-poplawska.png` |
| 6 · Lorcan Oxfield (MF) | `lorcan-oxfield.png` |
| 7 · Cinnamon Dougherty (MF) | `cinnamon-dougherty.png` |
| 8 · Primavera Bluefield (MF) | `primavera-bluefield.png` |
| 9 · Gibson Forte (FW) | `gibson-forte.png` |
| 10 · Love Stirling (FW) | `love-stirling.png` |
| 11 · Sheila Threadwell (FW) | `sheila-threadwell.png` |
| 12 · He Liu (GK) | `he-liu.png` |
| 13 · Brandy Ryehart (FW) | `brandy-ryehart.png` |
| 14 · Newman Wiford (MF) | `newman-wiford.png` |
| 15 · Vera Presswell (MF) | `vera-presswell.png` |
| 16 · Pattie Whitfield (DF) | `pattie-whitfield.png` |

### Secundaria South Cirrus

Escudo: `emblems/vr-nagumohara.png`

| Jugador | Archivo |
|---|---|
| 1 · Alix La Fontaine (GK) | `alix-la-fontaine.png` |
| 2 · Cade Shelby (DF) | `cade-shelby.png` |
| 3 · Cedric Freud (MF) | `cedric-freud.png` |
| 7 · Destin Billows (MF) | `destin-billows.png` |
| 8 · Winsor Compete (DF) | `winsor-compete.png` |
| 8 · Thierry Reyes (MF) | `thierry-reyes.png` |
| 9 · Charis Benzaie (DF) | `charis-benzaie.png` |
| 10 · Raika Shinohara (FW) | `raika-shinohara.png` |
| 10 · Maine Alsop (MF) | `maine-alsop.png` |
| 11 · Briar Bloomhurst (FW) | `briar-bloomhurst.png` |
| 11 · Dario Highton (MF) | `dario-highton.png` |
| 12 · Amelia Rainwalker (DF) | `amelia-rainwalker.png` |
| 13 · Marisol Cavallo (DF) | `marisol-cavallo.png` |
| 14 · Meridia Althoff (DF) | `meridia-althoff.png` |
| 15 · Tai Richter (MF) | `tai-richter.png` |
| 16 · Davin Bullock (MF) | `davin-bullock.png` |

### Instituto Twinford

Escudo: `emblems/vr-nikogawa.png`

| Jugador | Archivo |
|---|---|
| 1 · Ronan Strongwood (FW) | `ronan-strongwood.png` |
| 2 · Lila Glosswood (DF) | `lila-glosswood.png` |
| 3 · Rowland Brightwood (DF) | `rowland-brightwood.png` |
| 4 · Tristan Brookwood (DF) | `tristan-brookwood.png` |
| 5 · Lachlan Hartwood (MF) | `lachlan-hartwood.png` |
| 6 · Nathaniel Whitewood (MF) | `nathaniel-whitewood.png` |
| 7 · Orin Wildwood (MF) | `orin-wildwood.png` |
| 8 · Calvin Sixwood (MF) | `calvin-sixwood.png` |
| 9 · Iris Nightwood (MF) | `iris-nightwood.png` |
| 10 · Vearn Dashwood (FW) | `vearn-dashwood.png` |
| 11 · Asher Norwood (FW) | `asher-norwood.png` |
| 12 · Emory Plainwood (DF) | `emory-plainwood.png` |
| 13 · Maris Hollowwood (DF) | `maris-hollowwood.png` |
| 14 · Hobie Chartwood (GK) | `hobie-chartwood.png` |
| 15 · Lydia Trailwood (MF) | `lydia-trailwood.png` |
| 16 · Alden Songwood (GK) | `alden-songwood.png` |

### Academia West Manor

Escudo: `emblems/vr-nishinomiya.png`

| Jugador | Archivo |
|---|---|
| 1 · Dax Prescott (GK) | `dax-prescott.png` |
| 2 · Edvan Trodden (DF) | `edvan-trodden.png` |
| 3 · Drever Olflaire (DF) | `drever-olflaire.png` |
| 4 · Looke Raundoff (DF) | `looke-raundoff.png` |
| 5 · Rutheo Wheyston (DF) | `rutheo-wheyston.png` |
| 6 · Ernesta Beauregard (MF) | `ernesta-beauregard.png` |
| 7 · Laymark Starwyn (MF) | `laymark-starwyn.png` |
| 8 · Moby Tidbitt (MF) | `moby-tidbitt.png` |
| 9 · Edgard Loathe (MF) | `edgard-loathe.png` |
| 10 · Flanko Midspringle (FW) | `flanko-midspringle.png` |
| 11 · Berdy Caster (FW) | `berdy-caster.png` |
| 12 · Chicory Bellflower (MF) | `chicory-bellflower.png` |
| 13 · Aysen DeMacon (FW) | `aysen-demacon.png` |
| 14 · Breppo Terrey (MF) | `breppo-terrey.png` |
| 15 · Frie Sorbet (DF) | `frie-sorbet.png` |
| 16 · Eddi Losse (GK) | `eddi-losse.png` |

### Instituto Raimon (Victory Road)

Escudo: `emblems/vr-ouja-raimon.png`

| Jugador | Archivo |
|---|---|
| 1 · Zander Warmington (GK) | `zander-warmington.png` |
| 2 · Viorain Maleby (DF) | `viorain-maleby.png` |
| 3 · Clement Mariner (DF) | `clement-mariner.png` |
| 4 · Boone Wretman (DF) | `boone-wretman.png` |
| 5 · Jazmine Carmine (MF) | `jazmine-carmine.png` |
| 6 · Colton Sharps (MF) | `colton-sharps.png` |
| 7 · Maddock Jackson (MF) | `maddock-jackson.png` |
| 8 · Eleanor Estrella (MF) | `eleanor-estrella.png` |
| 9 · Darian Moonward (MF) | `darian-moonward.png` |
| 10 · Harper Evans (FW) | `harper-evans.png` |
| 11 · Talon Lewis (FW) | `talon-lewis.png` |
| 12 · Nino Gamberini (FW) | `nino-gamberini.png` |
| 13 · Hortensia Raintree (DF) | `hortensia-raintree.png` |
| 14 · Milan McGrath (DF) | `milan-mcgrath.png` |
| 15 · Kaeo Springfield (MF) | `kaeo-springfield.png` |
| 20 · Matilda Shadebough (GK) | `matilda-shadebough.png` |

### Plathos

Escudo: `emblems/vr-platos.png`

| Jugador | Archivo |
|---|---|
| 1 · Ash Barnes (GK) | `ash-barnes.png` |
| 2 · Miles Euclid (DF) | `miles-euclid.png` |
| 3 · Hector Thareos (DF) | `hector-thareos.png` |
| 4 · Rhea Loriandrin (DF) | `rhea-loriandrin.png` |
| 5 · Saros Algebra (DF) | `saros-algebra.png` |
| 6 · Eosram Reeves (MF) | `eosram-reeves.png` |
| 7 · Eon McKeane (MF) | `eon-mckeane.png` |
| 8 · Dariusius Henletos (MF) | `dariusius-henletos.png` |
| 9 · Torin Sandels (MF) | `torin-sandels.png` |
| 10 · Orpheus Clayridge (FW) | `orpheus-clayridge.png` |
| 11 · Victorio Cryptix (FW) | `victorio-cryptix.png` |
| 12 · Niana Cooke (DF) | `niana-cooke.png` |
| 13 · Gilia Dandrel (MF) | `gilia-dandrel.png` |
| 14 · Nikolaos Menandros (MF) | `nikolaos-menandros.png` |
| 16 · Hugo Severian (FW) | `hugo-severian.png` |
| 20 · Pharos Radris (GK) | `pharos-radris.png` |

### Goleadores del Callejón

Escudo: `emblems/vr-rojiura-backkicks.png`

| Jugador | Archivo |
|---|---|
| 1 · Cobb Hightail (GK) | `cobb-hightail.png` |
| 2 · June Davidson (DF) | `june-davidson.png` |
| 3 · Moray Delmar (DF) | `moray-delmar.png` |
| 4 · Jazzmine Skylark (DF) | `jazzmine-skylark.png` |
| 5 · Caius Rushford (MF) | `caius-rushford.png` |
| 6 · Noctis Dunn (MF) | `noctis-dunn.png` |
| 7 · Veril Golding (MF) | `veril-golding.png` |
| 8 · Frederick Brandt (FW) | `frederick-brandt.png` |
| 9 · Bogdan Berglund (FW) | `bogdan-berglund.png` |
| 10 · Holden Monday (MF) | `holden-monday.png` |
| 11 · Saburo Mizuki (FW) | `saburo-mizuki.png` |
| 12 · Jaxon Taggart (GK) | `jaxon-taggart.png` |
| 13 · Anson Barker (MF) | `anson-barker.png` |
| 14 · Deor Rummond (FW) | `deor-rummond.png` |
| 15 · Drako Bonner (DF) | `drako-bonner.png` |
| 16 · Chancer Cosgrave (DF) | `chancer-cosgrave.png` |

### Royal Academy (Victory Road)

Escudo: `emblems/vr-senjutsu-no-teikoku.png`

| Jugador | Archivo |
|---|---|
| 1 · Ashlan Panoptos (GK) | `ashlan-panoptos.png` |
| 2 · Hudson Headland (DF) | `hudson-headland.png` |
| 3 · Vex Frieden (DF) | `vex-frieden.png` |
| 4 · Asten Royds (DF) | `asten-royds.png` |
| 5 · Ruelle Neurivieu (DF) | `ruelle-neurivieu.png` |
| 6 · Theon Stillcliffe (MF) | `theon-stillcliffe.png` |
| 7 · Ciel Natcherall (MF) | `ciel-natcherall.png` |
| 8 · Kaien Spiradawn (FW) | `kaien-spiradawn.png` |
| 9 · Kyo Seestar (FW) | `kyo-seestar.png` |
| 10 · Syd Faircrest (MF) | `syd-faircrest.png` |
| 11 · Solan Brightmoor (FW) | `solan-brightmoor.png` |
| 12 · Lenox Grinder (FW) | `lenox-grinder.png` |
| 13 · Ophelia Ennercourt (FW) | `ophelia-ennercourt.png` |
| 14 · Riggs Fornstrut (MF) | `riggs-fornstrut.png` |
| 15 · Leticia Legatus (GK) | `leticia-legatus.png` |
| 16 · Arran Realis (DF) | `arran-realis.png` |

### Secundaria Solaria-Zeus

Escudo: `emblems/vr-tenshou-zeus.png`

| Jugador | Archivo |
|---|---|
| 1 · Garci Stormdale (GK) | `garci-stormdale.png` |
| 2 · Patrie Ambrosia (DF) | `patrie-ambrosia.png` |
| 3 · Garrick Loventhal (DF) | `garrick-loventhal.png` |
| 4 · Sampa Eonius (DF) | `sampa-eonius.png` |
| 5 · Kenard Montemar (DF) | `kenard-montemar.png` |
| 6 · Atol Lasalle (MF) | `atol-lasalle.png` |
| 7 · Revea Ristair (MF) | `revea-ristair.png` |
| 8 · Harald Monet (MF) | `harald-monet.png` |
| 9 · Ciro Zealon (MF) | `ciro-zealon.png` |
| 10 · Thaddeus Bellefax (FW) | `thaddeus-bellefax.png` |
| 11 · Riza Nagivar (FW) | `riza-nagivar.png` |
| 12 · Cate Heckel (MF) | `cate-heckel.png` |
| 13 · Iskandar Tarusian (GK) | `iskandar-tarusian.png` |
| 14 · Orisa Namir (MF) | `orisa-namir.png` |
| 15 · Burke Forzane (DF) | `burke-forzane.png` |
| 16 · Kazimir Stormblade (FW) | `kazimir-stormblade.png` |

### Secundaria Internacional Eastwind

Escudo: `emblems/vr-toufuu-ikokukan.png`

| Jugador | Archivo |
|---|---|
| 1 · Martino Leone (GK) | `martino-leone.png` |
| 2 · Jenny Okutba (DF) | `jenny-okutba.png` |
| 3 · Gigy Maharaja (DF) | `gigy-maharaja.png` |
| 4 · Robart Anderson (MF) | `robart-anderson.png` |
| 5 · Maribelle Flanmir (MF) | `maribelle-flanmir.png` |
| 6 · Toyo Yamanouchi (MF) | `toyo-yamanouchi.png` |
| 7 · Ming Chow (MF) | `ming-chow.png` |
| 8 · Judie Cassios (DF) | `judie-cassios.png` |
| 9 · Joey Beat (FW) | `joey-beat.png` |
| 10 · Kai Yoshizaki (FW) | `kai-yoshizaki.png` |
| 11 · Sikuvot Shivan (FW) | `sikuvot-shivan.png` |
| 12 · Olson Carchis (FW) | `olson-carchis.png` |
| 13 · Mengmeng Wang (MF) | `mengmeng-wang.png` |
| 14 · Kain Vijet (DF) | `kain-vijet.png` |
| 15 · Kaos Dao (GK) | `kaos-dao.png` |
| 16 · Edmond Pias (DF) | `edmond-pias.png` |

### Gaviotas FC

Escudo: `emblems/vr-umi-kamome-soccer-club.png`

| Jugador | Archivo |
|---|---|
| 1 · Garrison Hayfield (GK) | `garrison-hayfield.png` |
| 2 · Kean Aimes (FW) | `kean-aimes.png` |
| 3 · Plume Hathaway (MF) | `plume-hathaway.png` |
| 4 · Carlton Lawstrom (MF) | `carlton-lawstrom.png` |
| 5 · Imogen Greenbourne (MF) | `imogen-greenbourne.png` |
| 6 · Jewel Tremaine (MF) | `jewel-tremaine.png` |
| 7 · Peridot Runehart (MF) | `peridot-runehart.png` |
| 8 · Summers Laughlin (MF) | `summers-laughlin.png` |
| 9 · Swae Talltree (DF) | `swae-talltree.png` |
| 10 · Chilton Churner (DF) | `chilton-churner.png` |
| 11 · Seon Gulliver (DF) | `seon-gulliver.png` |
| 12 · Reamond Lockhard (FW) | `reamond-lockhard.png` |
| 13 · Beryl Granger (FW) | `beryl-granger.png` |
| 14 · Quip Netley (MF) | `quip-netley.png` |
| 15 · Kata Caballo (GK) | `kata-caballo.png` |
| 20 · Asuna Sugami (FW) | `asuna-sugami.png` |

### Zanark Outsiders

Escudo: `emblems/vr-zanark-strangers.png`

| Jugador | Archivo |
|---|---|
| 1 · Dave Quagmire (GK) | `dave-quagmire.png` |
| 2 · Cao Cao (DF) | `cao-cao.png` |
| 3 · Grisley Bear (FW) | `grisley-bear.png` |
| 4 · Panca (MF) | `panca.png` |
| 5 · Ryoma Nishiki (MF) | `ryoma-nishiki.png` |
| 6 · Zanark Avalonic (FW) | `zanark-avalonic.png` |
| 7 · Sapta (MF) | `sapta.png` |
| 8 · Caleb Stonewall (MF) | `caleb-stonewall.png` |
| 9 · Bash Lancer (FW) | `bash-lancer.png` |
| 10 · Hurricane Zeta (FW) | `hurricane-zeta.png` |
| 11 · Destra (FW) | `destra.png` |
| 12 · Gail Baker (DF) | `gail-baker.png` |
| 13 · Arachne (MF) | `arachne.png` |
| 14 · Lars Luceafăr (GK) | `lars-luceaf-r.png` |
| 15 · Baron Oxford (DF) | `baron-oxford.png` |
| 16 · Venom Braggard (DF) | `venom-braggard.png` |
