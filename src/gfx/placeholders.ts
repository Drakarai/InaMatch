// Gráficos provisionales generados por código. Se usan solo cuando el
// paquete de sprites (public/assets/pack/) no trae la imagen correspondiente.

import Phaser from 'phaser';
import { FONT, hex } from '../config';
import type { PlayerData, TeamData } from '../data/types';

export const SPRITE_W = 36;
export const SPRITE_H = 48;

export const texKey = {
  sprite: (playerId: string) => `sprite:${playerId}`,
  portrait: (playerId: string) => `portrait:${playerId}`,
  emblem: (teamId: string) => `emblem:${teamId}`,
};

function darken(color: number, f: number): number {
  const c = Phaser.Display.Color.IntegerToColor(color);
  return Phaser.Display.Color.GetColor(c.red * f, c.green * f, c.blue * f);
}

/** Muñeco chibi de frente, al estilo de los sprites de campo de IE3. */
function drawChibi(g: Phaser.GameObjects.Graphics, p: PlayerData, team: TeamData, scale = 1): void {
  const s = scale;
  const skin = hex(p.look?.skin ?? '#f1c79b');
  const hair = hex(p.look?.hair ?? '#3a2a1a');
  const shirt = hex(p.position === 'GK' ? team.colors.gkShirt : team.colors.shirt);
  const shorts = hex(team.colors.shorts);
  const outline = 0x1a1a22;

  // piernas y botas
  g.fillStyle(skin).fillRect(12 * s, 36 * s, 5 * s, 7 * s).fillRect(19 * s, 36 * s, 5 * s, 7 * s);
  g.fillStyle(outline).fillRect(11 * s, 43 * s, 7 * s, 4 * s).fillRect(18 * s, 43 * s, 7 * s, 4 * s);
  // pantalón
  g.fillStyle(shorts).fillRoundedRect(10 * s, 30 * s, 16 * s, 8 * s, 2 * s);
  // brazos
  g.fillStyle(skin).fillRoundedRect(5 * s, 22 * s, 5 * s, 10 * s, 2 * s).fillRoundedRect(26 * s, 22 * s, 5 * s, 10 * s, 2 * s);
  // camiseta
  g.fillStyle(shirt).fillRoundedRect(8 * s, 20 * s, 20 * s, 13 * s, 4 * s);
  g.fillStyle(darken(shirt, 0.75)).fillRect(8 * s, 30 * s, 20 * s, 2 * s);
  // cabeza (grande, estilo chibi)
  g.fillStyle(hair).fillCircle(18 * s, 12 * s, 12 * s);
  g.fillStyle(skin).fillEllipse(18 * s, 15 * s, 18 * s, 15 * s);
  g.fillStyle(hair).fillEllipse(18 * s, 7 * s, 22 * s, 9 * s);
  // ojos
  g.fillStyle(outline).fillRect(13 * s, 14 * s, 3 * s, 4 * s).fillRect(20 * s, 14 * s, 3 * s, 4 * s);
  g.fillStyle(0xffffff).fillRect(13 * s, 14 * s, 1 * s, 1 * s).fillRect(20 * s, 14 * s, 1 * s, 1 * s);
}

export function makePlayerSprite(scene: Phaser.Scene, p: PlayerData, team: TeamData): void {
  const key = texKey.sprite(p.id);
  if (scene.textures.exists(key)) return;
  const g = scene.make.graphics({}, false);
  drawChibi(g, p, team);
  g.generateTexture(key, SPRITE_W, SPRITE_H);
  g.destroy();
}

export function makePortrait(scene: Phaser.Scene, p: PlayerData, team: TeamData): void {
  const key = texKey.portrait(p.id);
  if (scene.textures.exists(key)) return;
  const size = 96;
  const g = scene.make.graphics({}, false);
  const accent = hex(team.colors.accent);
  g.fillStyle(darken(accent, 0.55)).fillRoundedRect(0, 0, size, size, 10);
  g.fillStyle(accent).fillRoundedRect(4, 4, size - 8, size - 8, 8);
  g.fillStyle(0xffffff, 0.12).fillRect(4, 4, size - 8, 30);
  // busto: la cabeza del chibi a escala
  const bust = scene.make.graphics({}, false);
  drawChibi(bust, p, team, 2.6);
  const rt = scene.make.renderTexture({ width: size, height: size }, false);
  rt.draw(g, 0, 0);
  rt.draw(bust, size / 2 - 18 * 2.6, 8);
  const label = scene.make.text(
    { text: String(p.number), style: { fontFamily: FONT, fontSize: '18px', color: '#ffffff', stroke: '#000000', strokeThickness: 4 } },
    false,
  );
  rt.draw(label, 8, size - 28);
  rt.saveTexture(key);
  g.destroy();
  bust.destroy();
  label.destroy();
}

export function makeEmblem(scene: Phaser.Scene, team: TeamData): void {
  const key = texKey.emblem(team.id);
  if (scene.textures.exists(key)) return;
  const size = 64;
  const g = scene.make.graphics({}, false);
  const accent = hex(team.colors.accent);
  // escudo
  g.fillStyle(0xffffff).fillRoundedRect(6, 4, 52, 34, 6).fillTriangle(6, 30, 58, 30, 32, 60);
  g.fillStyle(accent).fillRoundedRect(10, 8, 44, 28, 4).fillTriangle(10, 30, 54, 30, 32, 54);
  g.fillStyle(hex(team.colors.shirt)).fillRect(10, 20, 44, 6);
  const rt = scene.make.renderTexture({ width: size, height: size }, false);
  rt.draw(g, 0, 0);
  const label = scene.make.text(
    { text: team.short, style: { fontFamily: FONT, fontSize: '15px', color: '#ffffff', stroke: '#000000', strokeThickness: 3 } },
    false,
  );
  rt.draw(label, size / 2 - label.width / 2, 12);
  rt.saveTexture(key);
  g.destroy();
  label.destroy();
}

export function makeBall(scene: Phaser.Scene): void {
  if (scene.textures.exists('ball')) return;
  const g = scene.make.graphics({}, false);
  g.fillStyle(0xffffff).fillCircle(7, 7, 7);
  g.fillStyle(0x222222).fillCircle(7, 7, 2.6).fillCircle(2.5, 4, 1.5).fillCircle(11.5, 4, 1.5).fillCircle(4, 11.5, 1.5).fillCircle(10, 11.5, 1.5);
  g.lineStyle(1, 0x333333).strokeCircle(7, 7, 7);
  g.generateTexture('ball', 14, 14);
  g.destroy();
}
