# Sprites originales

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

### Big Waves

Escudo: `emblems/big-waves.png`

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

### Brockenborg

Escudo: `emblems/brockenborg.png`

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

Escudo: `emblems/desert-lion.png`

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

Escudo: `emblems/fire-dragon.png`

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

Escudo: `emblems/inazuma-japan.png`

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

Escudo: `emblems/knights-of-queen.png`

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

### Little Gigant

Escudo: `emblems/little-gigant.png`

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

### Makai Gundan Z

Escudo: `emblems/makai-gundan-z.png`

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

Escudo: `emblems/neo-japan.png`

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

Escudo: `emblems/ogre.png`

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

Escudo: `emblems/orpheus.png`

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

### Real Inazuma

Escudo: `emblems/real-inazuma.png`

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

Escudo: `emblems/red-matador.png`

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

### Rose Griffon

Escudo: `emblems/rose-griffon.png`

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

### Team Garshield

Escudo: `emblems/team-garshield.png`

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

### Team K

Escudo: `emblems/team-k.png`

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

### Tenkuu no Shito

Escudo: `emblems/tenkuu-no-shito.png`

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

Escudo: `emblems/the-empire.png`

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

### The Great Horn

Escudo: `emblems/the-great-horn.png`

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

### The Kingdom

Escudo: `emblems/the-kingdom.png`

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

Escudo: `emblems/unicorn.png`

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
