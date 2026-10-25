import Phaser from 'phaser';
import { COLORS, FONT } from '../config';

export function text(
  scene: Phaser.Scene,
  x: number,
  y: number,
  value: string,
  size = 18,
  color = '#ffffff',
  extra: Phaser.Types.GameObjects.Text.TextStyle = {},
): Phaser.GameObjects.Text {
  return scene.add.text(x, y, value, {
    fontFamily: FONT,
    fontSize: `${size}px`,
    color,
    stroke: '#0b1a2e',
    strokeThickness: Math.max(2, Math.round(size / 6)),
    ...extra,
  });
}

export interface ButtonOptions {
  w?: number;
  h?: number;
  color?: number;
  size?: number;
  sub?: string; // texto pequeño a la derecha (p. ej. coste de TP)
}

/** Botón con forma de "pestaña" como los de la pantalla táctil de IE3. */
export class Button extends Phaser.GameObjects.Container {
  private bg: Phaser.GameObjects.Graphics;
  private label: Phaser.GameObjects.Text;
  private bw: number;
  private bh: number;
  private color: number;
  private enabled = true;

  constructor(scene: Phaser.Scene, x: number, y: number, caption: string, onClick: () => void, opts: ButtonOptions = {}) {
    super(scene, x, y);
    this.bw = opts.w ?? 200;
    this.bh = opts.h ?? 48;
    this.color = opts.color ?? COLORS.ui;
    this.bg = scene.add.graphics();
    this.label = text(scene, 0, 0, caption, opts.size ?? 20).setOrigin(0.5);
    this.add([this.bg, this.label]);
    if (opts.sub) {
      const sub = text(scene, this.bw / 2 - 10, this.bh / 2 - 6, opts.sub, 14, '#ffe28a').setOrigin(1, 1);
      this.add(sub);
    }
    this.draw(false);
    this.setSize(this.bw, this.bh);
    this.setInteractive({ useHandCursor: true })
      .on('pointerover', () => this.enabled && this.draw(true))
      .on('pointerout', () => this.draw(false))
      .on('pointerdown', (_p: Phaser.Input.Pointer, _x: number, _y: number, ev: Phaser.Types.Input.EventData) => {
        ev.stopPropagation();
        if (this.enabled) onClick();
      });
    scene.add.existing(this);
  }

  setEnabled(on: boolean): this {
    this.enabled = on;
    this.setAlpha(on ? 1 : 0.45);
    return this;
  }

  setCaption(caption: string): this {
    this.label.setText(caption);
    return this;
  }

  private draw(hover: boolean): void {
    const w = this.bw;
    const h = this.bh;
    const g = this.bg.clear();
    g.fillStyle(0x0b1a2e, 0.6).fillRoundedRect(-w / 2 + 3, -h / 2 + 4, w, h, 10);
    g.fillStyle(hover ? Phaser.Display.Color.ValueToColor(this.color).lighten(15).color : this.color).fillRoundedRect(-w / 2, -h / 2, w, h, 10);
    g.fillStyle(0xffffff, 0.18).fillRoundedRect(-w / 2 + 3, -h / 2 + 3, w - 6, h / 2 - 3, 8);
    g.lineStyle(2, 0xffffff, 0.85).strokeRoundedRect(-w / 2, -h / 2, w, h, 10);
  }
}

/** Barra de FP/TP con número, como en el panel de duelo. */
export class StatBar extends Phaser.GameObjects.Container {
  private g: Phaser.GameObjects.Graphics;
  private num: Phaser.GameObjects.Text;

  constructor(
    scene: Phaser.Scene,
    x: number,
    y: number,
    label: string,
    private color: number,
    private barW = 150,
  ) {
    super(scene, x, y);
    this.g = scene.add.graphics();
    const lbl = text(scene, 0, -1, label, 12, '#ffe9a8').setOrigin(0, 0.5);
    this.num = text(scene, barW + 66, -1, '', 14).setOrigin(1, 0.5);
    this.add([this.g, lbl, this.num]);
    scene.add.existing(this);
  }

  set(value: number, max: number): void {
    const ratio = max > 0 ? Phaser.Math.Clamp(value / max, 0, 1) : 0;
    const x0 = 24;
    this.g.clear();
    this.g.fillStyle(0x0b1a2e).fillRoundedRect(x0, -6, this.barW, 10, 3);
    const fill = ratio < 0.25 ? 0xe2463b : this.color;
    this.g.fillStyle(fill).fillRoundedRect(x0 + 1, -5, Math.max(0, (this.barW - 2) * ratio), 8, 3);
    this.num.setText(`${Math.round(value)}`);
  }
}

export function panelFrame(g: Phaser.GameObjects.Graphics, x: number, y: number, w: number, h: number, fill = COLORS.panelBg): void {
  g.fillStyle(0x0b1a2e, 0.5).fillRoundedRect(x + 3, y + 4, w, h, 10);
  g.fillStyle(fill).fillRoundedRect(x, y, w, h, 10);
  g.lineStyle(2, COLORS.panelLine).strokeRoundedRect(x, y, w, h, 10);
}

export function wait(scene: Phaser.Scene, ms: number): Promise<void> {
  return new Promise((resolve) => scene.time.delayedCall(ms, resolve));
}
