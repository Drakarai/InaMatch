import Phaser from 'phaser';
import { sfx } from '../audio/sfx';
import { COLORS, DISPLAY, FONT, PORTRAIT } from '../config';
import { THEME, inkOn, slant } from './theme';

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

/** Texto sin borde, para dentro de los paneles (más limpio). */
export function label(scene: Phaser.Scene, x: number, y: number, value: string, size = 14, color: string = THEME.text, extra: Phaser.Types.GameObjects.Text.TextStyle = {}): Phaser.GameObjects.Text {
  return scene.add.text(x, y, value, { fontFamily: FONT, fontSize: `${size}px`, color, ...extra });
}

/** Rótulo grande con la letra de marcador (títulos de pantalla, marcadores, avisos del partido). */
export function display(
  scene: Phaser.Scene,
  x: number,
  y: number,
  value: string,
  size = 40,
  color = '#ffd23f',
  extra: Phaser.Types.GameObjects.Text.TextStyle = {},
): Phaser.GameObjects.Text {
  return text(scene, x, y, value, size, color, {
    strokeThickness: Math.max(4, Math.round(size / 7)),
    shadow: { offsetX: 0, offsetY: Math.max(2, Math.round(size / 14)), color: '#000000', blur: 0, fill: true, stroke: true },
    ...extra,
    fontFamily: DISPLAY,
    fontStyle: 'normal',
  }).setLetterSpacing(Math.round(size / 24));
}

export type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'accent' | 'ghost';

export interface ButtonOptions {
  w?: number;
  h?: number;
  /** Color concreto; si no, el de la variante. */
  color?: number;
  variant?: ButtonVariant;
  size?: number;
  sub?: string; // texto pequeño a la derecha (p. ej. coste de TP)
  textColor?: string;
  /** Pista de teclado, a la derecha (p. ej. "⏎"). */
  hint?: string;
  /** Icono (texto) antes del rótulo. */
  icon?: string;
  radius?: number;
}

// función y no tabla: widgets y theme se importan mutuamente, y THEME aún no existe al evaluar este módulo
const variantColor = (v: ButtonVariant): number =>
  ({ primary: THEME.yellow, secondary: THEME.panelLight, danger: THEME.coral, accent: THEME.cyan, ghost: 0x000000 })[v];

/** Botón redondeado con volumen: cara clara arriba, canto oscuro abajo y borde luminoso al pasar el ratón. */
export class Button extends Phaser.GameObjects.Container {
  private bg: Phaser.GameObjects.Graphics;
  private label: Phaser.GameObjects.Text;
  private bw: number;
  private bh: number;
  private color: number;
  private variant: ButtonVariant;
  private radius: number;
  private enabled = true;
  private selected = false;

  constructor(scene: Phaser.Scene, x: number, y: number, caption: string, onClick: () => void, opts: ButtonOptions = {}) {
    super(scene, x, y);
    this.bw = opts.w ?? 200;
    this.bh = opts.h ?? 46;
    this.variant = opts.variant ?? (opts.color === undefined ? 'secondary' : 'primary');
    // el color antiguo de la interfaz (azul) se convierte en el estilo secundario
    const legacy = opts.color === COLORS.ui || opts.color === COLORS.panelBg || opts.color === COLORS.panelDark;
    this.color = opts.color !== undefined && !legacy ? opts.color : variantColor(this.variant);
    if (opts.color === COLORS.uiRed) this.color = THEME.coral;
    if (legacy) this.variant = 'secondary';
    this.radius = opts.radius ?? Math.min(12, this.bh / 2);
    this.bg = scene.add.graphics();
    const ink = opts.textColor ?? (this.variant === 'secondary' || this.variant === 'ghost' ? '#ffffff' : inkOn(this.color));
    const size = opts.size ?? 18;
    const cap = opts.icon ? `${opts.icon}  ${caption}` : caption;
    this.label = text(scene, 0, 0, cap, size, ink, { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0.5);
    this.add([this.bg, this.label]);
    if (opts.sub) {
      const sub = text(scene, this.bw / 2 - 12, this.bh / 2 - 4, opts.sub, 12, ink === '#ffffff' ? '#ffe28a' : THEME.ink, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(1, 1).setAlpha(0.85);
      this.add(sub);
    }
    if (opts.hint) {
      const hint = text(scene, this.bw / 2 - 10, 0, opts.hint, 11, ink, { fontStyle: 'bold', strokeThickness: 0 }).setOrigin(1, 0.5).setAlpha(0.6);
      this.add(hint);
    }
    this.draw(false);
    // en el móvil el área táctil es algo mayor que el botón (al menos 48 de alto), centrada en él
    this.setSize(PORTRAIT ? Math.max(this.bw, 48) : this.bw, PORTRAIT ? Math.max(this.bh, 48) : this.bh);
    this.setInteractive({ useHandCursor: true })
      .on('pointerover', () => {
        if (!this.enabled) return;
        this.draw(true);
        scene.tweens.add({ targets: this, scale: 1.03, duration: 90 });
      })
      .on('pointerout', () => {
        this.draw(false);
        scene.tweens.add({ targets: this, scale: 1, duration: 90 });
      })
      .on('pointerdown', (_p: Phaser.Input.Pointer, _x: number, _y: number, ev: Phaser.Types.Input.EventData) => {
        ev.stopPropagation();
        if (!this.enabled) return;
        sfx.click();
        scene.tweens.add({ targets: this, scale: 0.97, duration: 60, yoyo: true });
        onClick();
      });
    scene.add.existing(this);
  }

  setEnabled(on: boolean): this {
    this.enabled = on;
    this.setAlpha(on ? 1 : 0.4);
    return this;
  }

  /** Marcado como el elegido (pestañas): borde cian. */
  setSelected(on: boolean): this {
    this.selected = on;
    this.draw(false);
    return this;
  }

  setCaption(caption: string): this {
    this.label.setText(caption);
    return this;
  }

  private draw(hover: boolean): void {
    const w = this.bw;
    const h = this.bh;
    const r = this.radius;
    const g = this.bg.clear();
    const base = Phaser.Display.Color.ValueToColor(this.color);
    const ghost = this.variant === 'ghost';
    const fill = ghost ? 0xffffff : hover ? base.clone().lighten(10).color : this.color;
    const edge = base.clone().darken(ghost ? 0 : 22).color;
    if (!ghost) g.fillStyle(0x000000, 0.4).fillRoundedRect(-w / 2 + 1, -h / 2 + 5, w, h, r);
    // canto de abajo (volumen) y cara
    if (!ghost) g.fillStyle(edge).fillRoundedRect(-w / 2, -h / 2 + 3, w, h, r);
    g.fillStyle(fill, ghost ? (hover ? 0.14 : 0.07) : 1).fillRoundedRect(-w / 2, -h / 2, w, h - 3, r);
    if (!ghost) g.fillStyle(0xffffff, hover ? 0.22 : 0.14).fillRoundedRect(-w / 2 + 2, -h / 2 + 2, w - 4, (h - 3) * 0.45, { tl: r, tr: r, bl: 2, br: 2 });
    const border = this.selected ? THEME.cyan : hover ? 0xffffff : this.variant === 'secondary' || ghost ? 0xffffff : 0x000000;
    g.lineStyle(this.selected ? 2 : 1, border, this.selected ? 1 : hover ? 0.7 : this.variant === 'secondary' || ghost ? 0.14 : 0.25).strokeRoundedRect(-w / 2, -h / 2, w, h - 3, r);
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
    const lbl = text(scene, 0, -1, label, 12, '#ffe9a8', { fontStyle: 'italic bold', strokeThickness: 0 }).setOrigin(0, 0.5);
    this.num = text(scene, barW + 66, -1, '', 14, '#ffffff', { strokeThickness: 0 }).setOrigin(1, 0.5);
    this.add([this.g, lbl, this.num]);
    scene.add.existing(this);
  }

  set(value: number, max: number): void {
    const ratio = max > 0 ? Phaser.Math.Clamp(value / max, 0, 1) : 0;
    const x0 = 24;
    const fill = ratio < 0.25 ? 0xe2463b : this.color;
    this.g.clear();
    this.g.fillStyle(0x000000, 0.55).fillRoundedRect(x0, -6, this.barW, 11, 5);
    if (ratio > 0) this.g.fillStyle(fill).fillRoundedRect(x0 + 1, -5, Math.max(8, (this.barW - 2) * ratio), 9, 4);
    this.g.fillStyle(0xffffff, 0.25).fillRect(x0 + 5, -4, Math.max(0, (this.barW - 10) * ratio), 2);
    this.num.setText(`${Math.round(value)}`);
  }
}

/** Barra horizontal sencilla con rótulo a la izquierda y valor a la derecha (medias, atributos). */
export function meter(scene: Phaser.Scene, x: number, y: number, w: number, value: number, max: number, color: number, caption?: string, valueText?: string): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const g = scene.add.graphics();
  const ratio = Phaser.Math.Clamp(value / max, 0, 1);
  g.fillStyle(0x000000, 0.5).fillRoundedRect(0, -4, w, 8, 4);
  g.fillStyle(color).fillRoundedRect(0, -4, Math.max(8, w * ratio), 8, 4);
  g.fillStyle(0xffffff, 0.25).fillRect(4, -3, Math.max(0, w * ratio - 8), 2);
  c.add(g);
  if (caption) c.add(label(scene, -8, 0, caption, 12, THEME.muted, { fontStyle: 'italic bold' }).setOrigin(1, 0.5));
  if (valueText !== undefined) c.add(label(scene, w + 8, 0, valueText, 13, THEME.text, { fontStyle: 'bold' }).setOrigin(0, 0.5));
  return c;
}

export function wait(scene: Phaser.Scene, ms: number): Promise<void> {
  return new Promise((resolve) => scene.time.delayedCall(ms, resolve));
}

/** Reduce el tamaño de letra hasta que el texto quepa en `maxW` (sin bajar de `minSize`). */
export function fitWidth(t: Phaser.GameObjects.Text, maxW: number, minSize: number): Phaser.GameObjects.Text {
  let size = parseInt(String(t.style.fontSize), 10);
  while (t.width > maxW && size > minSize) t.setFontSize(--size);
  return t;
}

export { slant };
