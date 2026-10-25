import Phaser from 'phaser';
import { TEAMS } from '../data';
import { makeBall, makeEmblem, makePlayerSprite, makePortrait, texKey } from '../gfx/placeholders';

/**
 * Formato de public/assets/pack/manifest.json (todas las rutas relativas a esa carpeta):
 * {
 *   "players": { "mark-evans": { "sprite": "sprites/mark.png", "portrait": "portraits/mark.png" } },
 *   "emblems": { "inazuma-national": "emblems/inazuma.png" }
 * }
 * Lo que falte se sustituye por gráficos provisionales.
 */
interface PackManifest {
  players?: Record<string, { sprite?: string; portrait?: string }>;
  emblems?: Record<string, string>;
}

const PACK = 'assets/pack/';

export class BootScene extends Phaser.Scene {
  constructor() {
    super('boot');
  }

  preload(): void {
    // Si no hay paquete de sprites el json falla al cargar y seguimos con los provisionales
    this.load.on(Phaser.Loader.Events.FILE_LOAD_ERROR, (file: Phaser.Loader.File) => {
      console.info(`[pack] no se pudo cargar ${file.src}, se usará el gráfico provisional`);
    });
    this.load.json('pack-manifest', `${PACK}manifest.json`);
  }

  create(): void {
    const manifest = (this.cache.json.get('pack-manifest') ?? {}) as PackManifest;
    let queued = 0;
    for (const [id, files] of Object.entries(manifest.players ?? {})) {
      if (files.sprite) {
        this.load.image(texKey.sprite(id), PACK + files.sprite);
        queued++;
      }
      if (files.portrait) {
        this.load.image(texKey.portrait(id), PACK + files.portrait);
        queued++;
      }
    }
    for (const [teamId, file] of Object.entries(manifest.emblems ?? {})) {
      this.load.image(texKey.emblem(teamId), PACK + file);
      queued++;
    }
    if (queued === 0) {
      this.finish();
      return;
    }
    this.load.once(Phaser.Loader.Events.COMPLETE, () => this.finish());
    this.load.start();
  }

  private finish(): void {
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
