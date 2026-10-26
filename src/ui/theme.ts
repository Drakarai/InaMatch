import Phaser from 'phaser';
import { hex } from '../config';
import type { Position, TeamData } from '../data/types';

/**
 * Estilo propio de InaMatch: noche azul oscura, amarillo rayo, formas inclinadas como los rótulos
 * del anime y los colores de cada equipo de fondo.
 */
export const THEME = {
  night: 0x0a1120,
  panel: 0x101a2c,
  panelLight: 0x1a2840,
  line: 0x2c3d5c,
  yellow: 0xffd23f,
  ink: '#0b1a2e',
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

/** Panel oscuro con la esquina de arriba a la derecha cortada y un filo de color arriba. */
export function themePanel(g: Phaser.GameObjects.Graphics, x: number, y: number, w: number, h: number, accent: number = THEME.yellow, alpha = 0.9): void {
  const cut = Math.min(22, h / 4);
  const shape = [pt(x, y), pt(x + w - cut, y), pt(x + w, y + cut), pt(x + w, y + h), pt(x, y + h)];
  g.fillStyle(0x000000, 0.35).fillPoints(shape.map((p) => pt(p.x + 4, p.y + 5)), true);
  g.fillStyle(THEME.panel, alpha).fillPoints(shape, true);
  g.lineStyle(1, THEME.line, 0.9).strokePoints(shape, true);
  g.fillStyle(accent).fillRect(x, y, Math.min(120, w * 0.4), 3);
}

/** Título de sección: texto en cursiva con una barrita de color delante. */
export function sectionTitle(scene: Phaser.Scene, x: number, y: number, label: string, color = THEME.yellow): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const g = scene.add.graphics().fillStyle(color).fillPoints(slant(0, -8, 10, 16, 4), true);
  const t = scene.add.text(16, 0, label, {
    fontFamily: '"Trebuchet MS", Arial, sans-serif',
    fontSize: '16px',
    fontStyle: 'italic bold',
    color: '#ffffff',
  });
  t.setOrigin(0, 0.5);
  c.add([g, t]);
  return c;
}

/**
 * Fondo de pantalla con el color de un equipo: banda diagonal, líneas de velocidad desde un punto
 * y trama de puntos, como una viñeta.
 */
export function teamBackdrop(
  scene: Phaser.Scene,
  team: TeamData,
  area = { x: 0, y: 0, w: scene.scale.width, h: scene.scale.height },
  focus = { x: area.x + area.w * 0.25, y: area.y + area.h * 0.35 },
): Phaser.GameObjects.Graphics {
  const { x, y, w, h } = area;
  const g = scene.add.graphics();
  g.fillStyle(THEME.night).fillRect(x, y, w, h);
  g.fillStyle(dim(team.colors.shirt, 0.7)).fillPoints([pt(x, y), pt(x + w * 0.62, y), pt(x + w * 0.38, y + h), pt(x, y + h)], true);
  g.fillStyle(dim(team.colors.accent, 0.55), 0.8).fillPoints([pt(x + w * 0.62, y), pt(x + w * 0.66, y), pt(x + w * 0.42, y + h), pt(x + w * 0.38, y + h)], true);
  g.lineStyle(2, hex(team.colors.accent), 0.1);
  for (let i = 0; i < 36; i++) {
    const a = (i / 36) * Math.PI * 2;
    const r0 = 120 + (i % 3) * 30;
    g.lineBetween(focus.x + Math.cos(a) * r0, focus.y + Math.sin(a) * r0, focus.x + Math.cos(a) * 1400, focus.y + Math.sin(a) * 1400);
  }
  for (let yy = y + h * 0.55; yy < y + h; yy += 14) {
    const r = ((yy - (y + h * 0.55)) / (h * 0.45)) * 2.4;
    g.fillStyle(0x000000, 0.25);
    for (let xx = x + (Math.round(yy / 14) % 2 ? 7 : 0); xx < x + w; xx += 14) g.fillCircle(xx, yy, r);
  }
  return g;
}
