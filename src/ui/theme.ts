import Phaser from 'phaser';
import { DISPLAY, FONT, GAME_H, GAME_W, RES, RES_EVENT, hex } from '../config';
import type { Position, TeamData } from '../data/types';
import { Button } from './widgets';

/**
 * Estilo de InaMatch, versión "estadio": noche azul profunda con focos, paneles redondeados de cristal
 * oscuro, amarillo rayo para lo principal, cian para lo que está seleccionado y coral para lo peligroso.
 */
export const THEME = {
  night: 0x070d18,
  deep: 0x0b1322,
  panel: 0x101b2f,
  panelLight: 0x1a2942,
  line: 0x2a3b5a,
  glow: 0x7fb2ff,
  yellow: 0xffd23f,
  yellowCss: '#ffd23f',
  cyan: 0x3ad1ff,
  cyanCss: '#3ad1ff',
  coral: 0xff5a6e,
  coralCss: '#ff8f9a',
  orange: 0xff8a3d,
  green: 0x46d68c,
  ink: '#0b1a2e',
  text: '#eef3fa',
  home: 0x2f7bff,
  away: 0xff3b4e,
  homeCss: '#7fb2ff',
  awayCss: '#ff8f9a',
  muted: '#8a97aa',
};

/** Color de cada demarcación, en las chapas de los jugadores. */
export const POS_COLOR: Record<Position, number> = {
  GK: 0xf2a33a,
  DF: 0x3d8bff,
  MF: 0x3cc47a,
  FW: 0xff4d5e,
};

export const pt = (x: number, y: number) => new Phaser.Geom.Point(x, y);

/** Paralelogramo inclinado hacia la derecha: (x, y) es la esquina de arriba a la izquierda del rectángulo. */
export function slant(x: number, y: number, w: number, h: number, skew = h * 0.28): Phaser.Geom.Point[] {
  return [pt(x + skew, y), pt(x + w, y), pt(x + w - skew, y + h), pt(x, y + h)];
}

/** Mezcla un color con la noche para usarlo de fondo sin que se coma el texto. */
export function dim(color: number | string, amount = 0.62): number {
  const from = Phaser.Display.Color.ValueToColor(typeof color === 'string' ? hex(color) : color);
  const c = Phaser.Display.Color.Interpolate.ColorWithColor(from, Phaser.Display.Color.ValueToColor(THEME.night), 100, amount * 100);
  return Phaser.Display.Color.GetColor(c.r, c.g, c.b);
}

/** Aclara un color (0-1). */
export function lighten(color: number, amount: number): number {
  const c = Phaser.Display.Color.ValueToColor(color).clone().lighten(Math.round(amount * 100));
  return c.color;
}

/** Color que se lee bien sobre otro: tinta oscura sobre colores claros, blanco sobre oscuros. */
export function inkOn(color: number): string {
  const c = Phaser.Display.Color.ValueToColor(color);
  return (c.red * 299 + c.green * 587 + c.blue * 114) / 1000 > 150 ? THEME.ink : '#ffffff';
}

/** Un foco de luz suave: círculos concéntricos con poca opacidad (WebGL no tiene degradados radiales). */
export function glow(g: Phaser.GameObjects.Graphics, x: number, y: number, r: number, color: number, alpha = 0.18, steps = 10): void {
  for (let i = steps; i >= 1; i--) {
    g.fillStyle(color, (alpha / steps) * 1.6);
    g.fillCircle(x, y, (r * i) / steps);
  }
}

/**
 * Fondo de estadio de noche: degradado, focos de color a los lados, haces de luz diagonales, una rejilla
 * muy fina y una viñeta abajo. Los dos colores son los de los equipos (o los del tema).
 */
export function stadiumBackdrop(scene: Phaser.Scene, left: number = THEME.home, right: number = THEME.coral, area = { x: 0, y: 0, w: GAME_W, h: GAME_H }): Phaser.GameObjects.Graphics {
  const { x, y, w, h } = area;
  const g = scene.add.graphics();
  g.fillGradientStyle(THEME.deep, THEME.deep, THEME.night, THEME.night, 1, 1, 1, 1).fillRect(x, y, w, h);
  glow(g, x + w * 0.12, y - h * 0.1, h * 0.9, left, 0.26);
  glow(g, x + w * 0.9, y + h * 0.05, h * 0.8, right, 0.2);
  // haces de luz de los focos
  g.fillStyle(0xffffff, 0.022);
  for (let i = 0; i < 5; i++) {
    const bx = x + w * (0.1 + i * 0.2);
    g.fillPoints([pt(bx - 30, y), pt(bx + 30, y), pt(bx + 260, y + h), pt(bx + 120, y + h)], true);
  }
  // rejilla fina
  g.lineStyle(1, 0xffffff, 0.025);
  for (let gx = x; gx <= x + w; gx += 40) g.lineBetween(gx, y, gx, y + h);
  for (let gy = y; gy <= y + h; gy += 40) g.lineBetween(x, gy, x + w, gy);
  // viñeta abajo
  g.fillGradientStyle(0x000000, 0x000000, 0x000000, 0x000000, 0, 0, 0.5, 0.5).fillRect(x, y + h * 0.6, w, h * 0.4);
  return g;
}

export interface PanelOptions {
  accent?: number;
  alpha?: number;
  radius?: number;
  /** Sin la barrita de color de arriba. */
  plain?: boolean;
  fill?: number;
}

/** Panel de cristal oscuro, redondeado, con borde luminoso y una barrita de color arriba a la izquierda. */
export function cardPanel(g: Phaser.GameObjects.Graphics, x: number, y: number, w: number, h: number, o: PanelOptions = {}): void {
  const r = o.radius ?? 14;
  const accent = o.accent ?? THEME.yellow;
  g.fillStyle(0x000000, 0.45).fillRoundedRect(x + 2, y + 8, w, h, r);
  g.fillStyle(o.fill ?? THEME.panel, o.alpha ?? 0.92).fillRoundedRect(x, y, w, h, r);
  g.fillStyle(0xffffff, 0.035).fillRoundedRect(x, y, w, Math.min(60, h * 0.35), { tl: r, tr: r, bl: 0, br: 0 });
  g.lineStyle(1, 0xffffff, 0.1).strokeRoundedRect(x + 0.5, y + 0.5, w - 1, h - 1, r);
  if (!o.plain) {
    g.fillStyle(accent).fillRoundedRect(x + 18, y - 2, 64, 4, 2);
    g.fillStyle(accent, 0.45).fillRoundedRect(x + 88, y - 2, 14, 4, 2);
  }
}

/** Panel oscuro con la esquina cortada (estilo anterior); ahora pinta el panel redondeado. */
export function themePanel(g: Phaser.GameObjects.Graphics, x: number, y: number, w: number, h: number, accent: number = THEME.yellow, alpha = 0.92): void {
  cardPanel(g, x, y, w, h, { accent, alpha });
}

/** Título de sección: texto en cursiva con una barrita de color delante. */
export function sectionTitle(scene: Phaser.Scene, x: number, y: number, label: string, color = THEME.yellow, size = 16): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const g = scene.add.graphics().fillStyle(color).fillRoundedRect(0, -8, 4, 16, 2);
  const t = scene.add.text(12, 0, label, {
    fontFamily: FONT,
    fontSize: `${size}px`,
    fontStyle: 'italic bold',
    color: THEME.text,
  });
  t.setOrigin(0, 0.5);
  c.add([g, t]);
  return c;
}

/** Etiqueta pequeña redondeada (demarcación, temporada, "EN EL 16"...). Devuelve el contenedor con su ancho en `width`. */
export function chip(scene: Phaser.Scene, x: number, y: number, label: string, color: number, opts: { size?: number; h?: number; padX?: number; textColor?: string; alpha?: number; icon?: string } = {}): Phaser.GameObjects.Container {
  const size = opts.size ?? 11;
  const h = opts.h ?? 20;
  const padX = opts.padX ?? 9;
  const c = scene.add.container(x, y);
  const t = scene.add.text(0, 0, label, { fontFamily: FONT, fontSize: `${size}px`, fontStyle: 'bold', color: opts.textColor ?? inkOn(color) }).setOrigin(0, 0.5);
  let w = t.width + padX * 2;
  let tx = padX;
  let icon: Phaser.GameObjects.Image | null = null;
  if (opts.icon && scene.textures.exists(opts.icon)) {
    icon = scene.add.image(padX + (h - 6) / 2, 0, opts.icon).setDisplaySize(h - 6, h - 6);
    tx += h - 2;
    w += h - 2;
  }
  t.setX(tx);
  const g = scene.add.graphics().fillStyle(color, opts.alpha ?? 1).fillRoundedRect(0, -h / 2, w, h, h / 2);
  c.add(g);
  if (icon) c.add(icon);
  c.add(t);
  c.setSize(w, h);
  return c;
}

/** Fila de estrellas (0,5 a 5) pintada con formas, para la media de un equipo. */
export function starRow(scene: Phaser.Scene, x: number, y: number, stars: number, size = 10, color = THEME.yellow): Phaser.GameObjects.Graphics {
  const g = scene.add.graphics();
  const star = (cx: number, cy: number, r: number, fill: number, alpha: number) => {
    const pts: Phaser.Geom.Point[] = [];
    for (let i = 0; i < 10; i++) {
      const a = -Math.PI / 2 + (i * Math.PI) / 5;
      const rr = i % 2 ? r * 0.45 : r;
      pts.push(pt(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr));
    }
    g.fillStyle(fill, alpha).fillPoints(pts, true);
  };
  for (let i = 0; i < 5; i++) {
    const cx = x + i * (size * 2.2) + size;
    star(cx, y, size, 0x000000, 0.35);
    const v = stars - i;
    if (v >= 1) star(cx, y, size * 0.88, color, 1);
    else if (v >= 0.5) {
      // media estrella: la mitad izquierda
      star(cx, y, size * 0.88, color, 0.35);
      const pts: Phaser.Geom.Point[] = [];
      for (let k = 0; k < 10; k++) {
        const a = -Math.PI / 2 + (k * Math.PI) / 5;
        const rr = k % 2 ? size * 0.88 * 0.45 : size * 0.88;
        pts.push(pt(Math.min(cx, cx + Math.cos(a) * rr), y + Math.sin(a) * rr));
      }
      g.fillStyle(color).fillPoints(pts, true);
    } else star(cx, y, size * 0.88, color, 0.18);
  }
  return g;
}

/** El rayo de InaMatch, como logo. */
export function boltLogo(g: Phaser.GameObjects.Graphics, x: number, y: number, s = 1, color = THEME.yellow): void {
  const p = [
    [12, 0],
    [24, 0],
    [16, 16],
    [26, 16],
    [6, 42],
    [11, 22],
    [0, 22],
  ];
  g.fillStyle(0x000000, 0.4).fillPoints(p.map(([px, py]) => pt(x + px * s + 2 * s, y + py * s + 3 * s)), true);
  g.fillStyle(color).fillPoints(p.map(([px, py]) => pt(x + px * s, y + py * s)), true);
}

export interface TopBarOptions {
  title: string;
  subtitle?: string;
  /** Botón de volver, a la izquierda del título. */
  back?: { label: string; onClick: () => void };
  /** Icono del título: clave de textura (escudo) o nada para el rayo. */
  icon?: string;
  accent?: number;
}

export const TOP_BAR_H = 64;

/** Barra de arriba, igual en todas las pantallas: título a la izquierda (con botón de volver) y sitio a la derecha. */
export function topBar(scene: Phaser.Scene, o: TopBarOptions): Phaser.GameObjects.Container {
  const c = scene.add.container(0, 0).setDepth(100);
  const g = scene.add.graphics();
  g.fillStyle(THEME.night, 0.82).fillRect(0, 0, GAME_W, TOP_BAR_H);
  g.fillStyle(0xffffff, 0.03).fillRect(0, 0, GAME_W, TOP_BAR_H / 2);
  g.lineStyle(1, 0xffffff, 0.1).lineBetween(0, TOP_BAR_H, GAME_W, TOP_BAR_H);
  g.fillStyle(o.accent ?? THEME.yellow).fillRect(0, TOP_BAR_H - 2, 180, 2);
  c.add(g);
  let x = 24;
  if (o.back) {
    const b = scene.add.container(x + 18, TOP_BAR_H / 2);
    const bg = scene.add.graphics();
    const draw = (hover: boolean) => {
      bg.clear().fillStyle(hover ? THEME.yellow : THEME.panelLight, 1).fillRoundedRect(-18, -18, 36, 36, 10);
      bg.lineStyle(1, 0xffffff, hover ? 0 : 0.15).strokeRoundedRect(-18, -18, 36, 36, 10);
      bg.lineStyle(3, hover ? hex(THEME.ink) : 0xffffff).beginPath().moveTo(4, -8).lineTo(-5, 0).lineTo(4, 8).strokePath();
    };
    draw(false);
    const lbl = scene.add.text(26, 0, o.back.label, { fontFamily: FONT, fontSize: '13px', fontStyle: 'bold', color: THEME.muted }).setOrigin(0, 0.5);
    b.add([bg, lbl]);
    const zone = scene.add.zone(-18, -18, 36 + 10 + lbl.width, 36).setOrigin(0).setInteractive({ useHandCursor: true });
    zone.on('pointerover', () => (draw(true), lbl.setColor(THEME.text)));
    zone.on('pointerout', () => (draw(false), lbl.setColor(THEME.muted)));
    zone.on('pointerdown', o.back.onClick);
    b.add(zone);
    c.add(b);
    x += 36 + 10 + lbl.width + 22;
  }
  if (o.icon && scene.textures.exists(o.icon)) {
    c.add(scene.add.image(x + 20, TOP_BAR_H / 2, o.icon).setDisplaySize(40, 40));
    x += 52;
  } else if (!o.back) {
    const lg = scene.add.graphics();
    boltLogo(lg, x, 11, 1);
    c.add(lg);
    x += 36;
  }
  const title = scene.add
    .text(x, o.subtitle ? TOP_BAR_H / 2 - 9 : TOP_BAR_H / 2, o.title, { fontFamily: DISPLAY, fontSize: '30px', color: THEME.yellowCss })
    .setOrigin(0, 0.5)
    .setLetterSpacing(1);
  c.add(title);
  if (o.subtitle) {
    c.add(scene.add.text(x + 1, TOP_BAR_H / 2 + 13, o.subtitle, { fontFamily: FONT, fontSize: '13px', fontStyle: 'italic', color: THEME.muted }).setOrigin(0, 0.5));
  }
  return c;
}

/** Ficha de monedas para la barra de arriba (x es el borde derecho). */
export function coinChip(scene: Phaser.Scene, x: number, y: number, coins: number): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const t = scene.add.text(0, 0, String(coins), { fontFamily: FONT, fontSize: '16px', fontStyle: 'bold', color: THEME.yellowCss }).setOrigin(1, 0.5);
  const w = t.width + 44;
  const g = scene.add.graphics();
  g.fillStyle(THEME.panelLight, 1).fillRoundedRect(-w, -16, w, 32, 16);
  g.lineStyle(1, THEME.yellow, 0.5).strokeRoundedRect(-w, -16, w, 32, 16);
  g.fillStyle(THEME.yellow).fillCircle(-w + 16, 0, 8);
  g.fillStyle(0xffb000).fillCircle(-w + 16, 0, 5);
  t.setX(-12);
  c.add([g, t]);
  c.setSize(w, 32);
  return c;
}

/** Fondo de pantalla con el color de un equipo: el fondo de estadio con su color de foco. */
export function teamBackdrop(scene: Phaser.Scene, team: TeamData, area = { x: 0, y: 0, w: GAME_W, h: GAME_H }): Phaser.GameObjects.Graphics {
  return stadiumBackdrop(scene, hex(team.colors.shirt), hex(team.colors.accent), area);
}

export interface ConfirmOptions {
  title: string;
  body?: string;
  ok?: string;
  cancel?: string;
  danger?: boolean;
  onOk: () => void;
  onCancel?: () => void;
}

/** Diálogo de confirmación sobre un fondo oscuro. Se cierra solo al elegir. */
export function confirmDialog(scene: Phaser.Scene, o: ConfirmOptions, depth = 500): Phaser.GameObjects.Container {
  const W = 420;
  const H = o.body ? 190 : 150;
  const x = GAME_W / 2 - W / 2;
  const y = GAME_H / 2 - H / 2;
  const c = scene.add.container(0, 0).setDepth(depth);
  const back = scene.add.rectangle(GAME_W / 2, GAME_H / 2, GAME_W, GAME_H, 0x000000, 0.62).setInteractive();
  c.add(back);
  const g = scene.add.graphics();
  cardPanel(g, x, y, W, H, { accent: o.danger ? THEME.coral : THEME.yellow, alpha: 0.98 });
  c.add(g);
  c.add(scene.add.text(x + 24, y + 30, o.title, { fontFamily: FONT, fontSize: '20px', fontStyle: 'italic bold', color: THEME.text }).setOrigin(0, 0.5));
  if (o.body) c.add(scene.add.text(x + 24, y + 58, o.body, { fontFamily: FONT, fontSize: '14px', color: THEME.muted, wordWrap: { width: W - 48 }, lineSpacing: 3 }));
  const close = (fn?: () => void) => {
    c.destroy();
    fn?.();
  };
  c.add(new Button(scene, x + W - 92, y + H - 38, o.ok ?? 'Sí', () => close(o.onOk), { w: 140, h: 42, variant: o.danger ? 'danger' : 'primary' }));
  c.add(new Button(scene, x + W - 250, y + H - 38, o.cancel ?? 'Cancelar', () => close(o.onCancel), { w: 140, h: 42, variant: 'secondary' }));
  scene.input.keyboard?.once('keydown-ESC', () => c.active && close(o.onCancel));
  return c;
}

/** Aviso breve abajo en el centro, que se va solo. */
export function toast(scene: Phaser.Scene, message: string, color = THEME.yellow, ms = 1800): void {
  const t = scene.add.text(0, 0, message, { fontFamily: FONT, fontSize: '15px', fontStyle: 'bold', color: inkOn(color) }).setOrigin(0.5);
  const w = t.width + 36;
  const c = scene.add.container(GAME_W / 2, GAME_H - 46).setDepth(600).setAlpha(0);
  const g = scene.add.graphics().fillStyle(color).fillRoundedRect(-w / 2, -18, w, 36, 18);
  c.add([g, t]);
  scene.tweens.add({ targets: c, alpha: 1, y: GAME_H - 56, duration: 180 });
  scene.time.delayedCall(ms, () => scene.tweens.add({ targets: c, alpha: 0, duration: 250, onComplete: () => c.destroy() }));
}

/** Amplía la cámara principal de la escena para que el juego (1280x720) llene el lienzo a resolución real. */
export function fitCamera(scene: Phaser.Scene): void {
  const fit = () => scene.cameras.main.setZoom(RES).centerOn(GAME_W / 2, GAME_H / 2);
  fit();
  // si cambia la resolución (ventana redimensionada), se vuelve a ajustar
  scene.events.on(RES_EVENT, fit);
  scene.events.once(Phaser.Scenes.Events.SHUTDOWN, () => scene.events.off(RES_EVENT, fit));
}
