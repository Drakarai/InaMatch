import Phaser from 'phaser';
import { audio } from '../audio/engine';
import { TEAMS } from '../data';
import { makeFxTextures } from '../gfx/fx';
import { bootPack } from '../gfx/pack';
import { makeBall, makeEmblem } from '../gfx/placeholders';
import { ensureClub } from '../club/club';
import { applyClubCrest } from '../club/crests';
import { fitCamera } from '../ui/theme';

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
      const pixel = key.startsWith('sprite:') || key.startsWith('vsprite:');
      this.textures.get(key).setFilter(pixel ? Phaser.Textures.FilterMode.NEAREST : Phaser.Textures.FilterMode.LINEAR);
    });
  }

  create(): void {
    fitCamera(this);
    for (const team of TEAMS) makeEmblem(this, team);
    makeBall(this);
    makeFxTextures(this);
    audio.init(this.game);
    // "Mi club": la primera vez se reparte la plantilla inicial (hace falta la lista de ojeadores)
    const loading = this.add.text(640, 360, '', {}).setVisible(false); // la pantalla de carga es la de index.html
    // los sprites dibujados de los jugadores no se cargan aquí: los de cada partido, antes de empezar (ensureSprites)
    ensureClub()
      .then((save) => new Promise<void>((resolve) => applyClubCrest(this, save.crest, resolve)))
      .catch((err) => console.warn('[club] no se pudo preparar el club', err))
      .then(() => {
        loading.destroy();
        document.getElementById('splash')?.classList.add('done');
        this.scene.start('menu');
      });
  }
}
