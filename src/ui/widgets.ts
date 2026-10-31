import Phaser from 'phaser';
import { sfx } from '../audio/sfx';
import { COLORS, FONT } from '../config';
import { THEME, slant, themePanel } from './theme';

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
  textColor?: string;
}

/** Botón inclinado, como los rótulos del anime. El amarillo (THEME.yellow) lleva el texto oscuro. */
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
    const dark = opts.textColor ?? (this.color === THEME.yellow ? THEME.ink : '#ffffff');
    this.label = text(scene, 0, 0, caption, opts.size ?? 20, dark, {
      fontStyle: 'italic bold',
      strokeThickness: dark === '#ffffff' ? Math.max(2, Math.round((opts.size ?? 20) / 7)) : 0,
    }).setOrigin(0.5);
    this.add([this.bg, this.label]);
    if (opts.sub) {
      const sub = text(scene, this.bw / 2 - 16, this.bh / 2 - 5, opts.sub, 13, '#ffe28a', { fontStyle: 'bold' }).setOrigin(1, 1);
      this.add(sub);
    }
    this.draw(false);
    this.setSize(this.bw, this.bh);
    this.setInteractive({ useHandCursor: true })
      .on('pointerover', () => this.enabled && this.draw(true))
      .on('pointerout', () => this.draw(false))
      .on('pointerdown', (_p: Phaser.Input.Pointer, _x: number, _y: number, ev: Phaser.Types.Input.EventData) => {
        ev.stopPropagation();
        if (!this.enabled) return;
        sfx.click();
        onClick();
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
    const skew = Math.min(14, h * 0.3);
    const g = this.bg.clear();
    const fill = hover ? Phaser.Display.Color.ValueToColor(this.color).lighten(14).color : this.color;
    g.fillStyle(0x000000, 0.5).fillPoints(slant(-w / 2 + 4, -h / 2 + 5, w, h, skew), true);
    g.fillStyle(fill).fillPoints(slant(-w / 2, -h / 2, w, h, skew), true);
    g.fillStyle(0xffffff, hover ? 0.3 : 0.2).fillPoints(slant(-w / 2 + skew * 0.5 + 3, -h / 2 + 3, w - skew - 6, h * 0.36, skew * 0.36), true);
    g.fillStyle(0x000000, 0.18).fillPoints(slant(-w / 2 - 1, h / 2 - 5, w - skew + 2, 5, 1), true);
    if (hover) g.lineStyle(2, 0xffffff, 0.9).strokePoints(slant(-w / 2, -h / 2, w, h, skew), true);
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
    const lbl = text(scene, 0, -1, label, 12, '#ffe9a8', { fontStyle: 'italic bold' }).setOrigin(0, 0.5);
    this.num = text(scene, barW + 66, -1, '', 14).setOrigin(1, 0.5);
    this.add([this.g, lbl, this.num]);
    scene.add.existing(this);
  }

  set(value: number, max: number): void {
    const ratio = max > 0 ? Phaser.Math.Clamp(value / max, 0, 1) : 0;
    const x0 = 24;
    const fill = ratio < 0.25 ? 0xe2463b : this.color;
    this.g.clear();
    this.g.fillStyle(0x000000, 0.55).fillPoints(slant(x0, -6, this.barW, 11, 4), true);
    if (ratio > 0) this.g.fillStyle(fill).fillPoints(slant(x0 + 1, -5, Math.max(6, (this.barW - 2) * ratio), 9, 3), true);
    this.g.fillStyle(0xffffff, 0.25).fillRect(x0 + 4, -5, Math.max(0, (this.barW - 8) * ratio), 2);
    this.num.setText(`${Math.round(value)}`);
  }
}

/** Panel del juego. El color de relleno se ignora salvo para teñir el filo: todos van con el estilo oscuro. */
export function panelFrame(g: Phaser.GameObjects.Graphics, x: number, y: number, w: number, h: number, accent: number = THEME.yellow): void {
  themePanel(g, x, y, w, h, accent === COLORS.panelBg || accent === COLORS.panelDark ? THEME.yellow : accent);
}

export function wait(scene: Phaser.Scene, ms: number): Promise<void> {
  return new Promise((resolve) => scene.time.delayedCall(ms, resolve));
}
