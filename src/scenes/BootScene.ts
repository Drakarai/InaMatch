import Phaser from 'phaser';
import { TEAMS } from '../data';
import { makeBall, makeEmblem, makePlayerSprite, makePortrait, texKey } from '../gfx/placeholders';

// Paquete de sprites: basta con dejar las imágenes en src/assets/pack/ con el id
// del jugador o del equipo como nombre (sprites/mark-evans.png, emblems/ie3-desert-lion.png...).
// Vite las mete en el juego al compilar; lo que falte se dibuja por código.
const packFiles = import.meta.glob<string>('../assets/pack/{sprites,portraits,emblems}/*.{png,webp,gif,jpg,jpeg}', {
  eager: true,
  query: '?url',
  import: 'default',
});

const KEY_BY_FOLDER: Record<string, (id: string) => string> = {
  sprites: texKey.sprite,
  portraits: texKey.portrait,
  emblems: texKey.emblem,
};

export class BootScene extends Phaser.Scene {
  constructor() {
    super('boot');
  }

  preload(): void {
    this.load.on(Phaser.Loader.Events.FILE_LOAD_ERROR, (file: Phaser.Loader.File) => {
      console.warn(`[pack] no se pudo cargar ${file.key}, se usará el gráfico provisional`);
    });
    for (const [path, url] of Object.entries(packFiles)) {
      const match = path.match(/\/(sprites|portraits|emblems)\/([^/]+)\.\w+$/);
      if (match) this.load.image(KEY_BY_FOLDER[match[1]](match[2].toLowerCase()), url);
    }
    // sprites y retratos son pixel art: escalado nítido. Los escudos (los de Victory Road) se suavizan.
    this.load.on(Phaser.Loader.Events.FILE_COMPLETE, (key: string) => {
      const emblem = key.startsWith(texKey.emblem(''));
      this.textures.get(key).setFilter(emblem ? Phaser.Textures.FilterMode.LINEAR : Phaser.Textures.FilterMode.NEAREST);
    });
  }

  create(): void {
    for (const team of TEAMS) {
      makeEmblem(this, team);
      for (const p of team.players) {
        makePlayerSprite(this, p, team);
        makePortrait(this, p, team);
      }
    }
    makeBall(this);
    this.scene.start('menu');
  }
}
