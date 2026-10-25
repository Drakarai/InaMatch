import Phaser from 'phaser';
import { GAME_H, GAME_W, hex } from '../config';
import { TEAMS } from '../data';
import { texKey } from '../gfx/placeholders';
import { defaultLineup } from '../engine/lineup';
import { Button, panelFrame, text } from '../ui/widgets';

export function drawBackdrop(scene: Phaser.Scene): void {
  const g = scene.add.graphics();
  g.fillGradientStyle(0x1d4f8f, 0x1d4f8f, 0x0d2547, 0x0d2547).fillRect(0, 0, GAME_W, GAME_H);
  g.fillStyle(0xffffff, 0.04);
  for (let i = -GAME_H; i < GAME_W; i += 80) g.fillTriangle(i, GAME_H, i + 40, GAME_H, i + 40 + GAME_H, 0).fillTriangle(i, GAME_H, i + GAME_H, 0, i + 40 + GAME_H, 0);
}

export class MenuScene extends Phaser.Scene {
  private home = 0;
  private away = 1;

  constructor() {
    super('menu');
  }

  create(): void {
    drawBackdrop(this);
    text(this, GAME_W / 2, 90, 'InaMatch', 84, '#ffd23f', { strokeThickness: 12, stroke: '#0b1a2e' }).setOrigin(0.5);
    text(this, GAME_W / 2, 160, 'Partidos al estilo Inazuma Eleven 3', 24, '#d8e8ff').setOrigin(0.5);

    // por defecto, Inazuma Japón contra los Leones del Desierto (o el primer rival disponible)
    this.home = Math.max(0, TEAMS.findIndex((t) => t.id === 'inazuma-japan'));
    const desert = TEAMS.findIndex((t) => t.id === 'desert-lion');
    this.away = desert >= 0 && desert !== this.home ? desert : (this.home + 1) % TEAMS.length;
    this.selector(GAME_W / 2 - 260, 360, 'Tu equipo', () => this.home, (v) => (this.home = v));
    text(this, GAME_W / 2, 360, 'VS', 64, '#ffffff', { strokeThickness: 10 }).setOrigin(0.5);
    this.selector(GAME_W / 2 + 260, 360, 'Rival', () => this.away, (v) => (this.away = v));

    new Button(this, GAME_W / 2, 580, 'Formación  ▶', () => this.next(), { w: 320, h: 64, size: 28, color: 0xe2552c });

    text(
      this,
      GAME_W / 2,
      GAME_H - 26,
      'Proyecto de fans sin ánimo de lucro. Inazuma Eleven es una marca de LEVEL-5.',
      14,
      '#9fb8d8',
    ).setOrigin(0.5);
  }

  private selector(x: number, y: number, title: string, get: () => number, set: (v: number) => void): void {
    const g = this.add.graphics();
    panelFrame(g, x - 170, y - 130, 340, 260);
    text(this, x, y - 105, title, 22, '#ffe28a').setOrigin(0.5);
    const emblem = this.add.image(x, y - 10, texKey.emblem(TEAMS[get()].id));
    const name = text(this, x, y + 80, '', 26).setOrigin(0.5);
    const refresh = () => {
      const team = TEAMS[get()];
      emblem.setTexture(texKey.emblem(team.id)).setDisplaySize(120, 120);
      name.setText(team.name);
      name.setColor(Phaser.Display.Color.IntegerToColor(hex(team.colors.shirt)).lighten(30).rgba);
    };
    const step = (d: number) => {
      set((get() + d + TEAMS.length) % TEAMS.length);
      refresh();
    };
    new Button(this, x - 135, y - 10, '◀', () => step(-1), { w: 44, h: 64 });
    new Button(this, x + 135, y - 10, '▶', () => step(1), { w: 44, h: 64 });
    refresh();
  }

  private next(): void {
    const home = TEAMS[this.home];
    const away = TEAMS[this.away];
    this.scene.start('formation', { home: defaultLineup(home), away: defaultLineup(away) });
  }
}
