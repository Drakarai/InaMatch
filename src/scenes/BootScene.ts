import Phaser from 'phaser';
import { audio } from '../audio/engine';
import { TEAMS } from '../data';
import { makeFxTextures } from '../gfx/fx';
import { bootPack } from '../gfx/pack';
import { makeBall, makeEmblem, makePlayerSprite } from '../gfx/placeholders';

export class BootScene extends Phaser.Scene {
  constructor() {
    super('boot');
  }

  preload(): void {
    this.load.on(Phaser.Loader.Events.FILE_LOAD_ERROR, (file: Phaser.Loader.File) => {
      console.warn(`[pack] no se pudo cargar ${file.key}, se usará el gráfico provisional`);
    });
    for (const { key, url } of bootPack) this.load.image(key, url);
    // los sprites son pixel art: escalado nítido. Escudos y retratos (los de Victory Road) se suavizan.
    this.load.on(Phaser.Loader.Events.FILE_COMPLETE, (key: string) => {
      const pixel = key.startsWith('sprite:');
      this.textures.get(key).setFilter(pixel ? Phaser.Textures.FilterMode.NEAREST : Phaser.Textures.FilterMode.LINEAR);
    });
  }

  create(): void {
    for (const team of TEAMS) {
      makeEmblem(this, team);
      for (const p of team.players) {
        makePlayerSprite(this, p, team);
      }
    }
    makeBall(this);
    makeFxTextures(this);
    audio.init(this.game);
    this.scene.start('menu');
  }
}
