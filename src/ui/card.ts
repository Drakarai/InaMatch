import Phaser from 'phaser';
import { RARITY, type Card } from '../club/pool';
import { getTeam } from '../data';
import { ELEMENT_COLOR } from '../data/elements';
import type { PlayerData } from '../data/types';
import { portraitsOf } from '../gfx/pack';
import { portraitKey } from '../gfx/placeholders';
import { POS_COLOR, THEME, slant } from './theme';
import { text } from './widgets';

/** El jugador de una carta, con su equipo de origen (para el retrato y los rasgos). */
export function cardPlayer(card: Card): PlayerData {
  // sin dorsal: el retrato de reserva no lo pinta
  return { ...card.player, number: 0, origin: card.origin, originId: card.player.id };
}

/** Carga los retratos de Victory Road de unas cartas y avisa al terminar. */
export function loadCardPortraits(scene: Phaser.Scene, cards: Card[], done: () => void): void {
  const todo = portraitsOf(cards.map((c) => ({ team: c.origin, id: c.player.id }))).filter((e) => !scene.textures.exists(e.key));
  if (!todo.length) return done();
  for (const { key, url } of todo) scene.load.image(key, url);
  scene.load.once(Phaser.Loader.Events.COMPLETE, done);
  scene.load.start();
}

const stars = (n: number) => '★'.repeat(n);

/**
 * Carta de jugador: retrato, nombre, demarcación, afinidad y rareza (color del marco y estrellas).
 * (x, y) es el centro.
 */
export function drawCard(scene: Phaser.Scene, x: number, y: number, card: Card, w = 130, h = 176): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const r = RARITY[card.rarity];
  const p = card.player;
  const g = scene.add.graphics();
  g.fillStyle(0x000000, 0.45).fillRoundedRect(-w / 2 + 4, -h / 2 + 5, w, h, 10);
  g.fillStyle(THEME.panel).fillRoundedRect(-w / 2, -h / 2, w, h, 10);
  g.fillStyle(r.color, 0.25).fillRoundedRect(-w / 2, -h / 2, w, h * 0.62, { tl: 10, tr: 10, bl: 0, br: 0 });
  g.lineStyle(card.rarity >= 3 ? 4 : 3, r.color).strokeRoundedRect(-w / 2, -h / 2, w, h, 10);
  c.add(g);
  // el retrato de reserva (sin Victory Road) se dibuja con la equipación de Mi club
  const club = getTeam('club');
  const face = scene.add.image(0, -h / 2 + h * 0.33, portraitKey(scene, cardPlayer(card), club));
  const side = Math.min(w - 16, h * 0.56);
  face.setDisplaySize(side, side);
  c.add(face);
  // demarcación y afinidad
  const chip = scene.add.graphics();
  chip.fillStyle(POS_COLOR[p.position]).fillPoints(slant(-w / 2 + 6, -h / 2 + 6, 36, 18, 5), true);
  c.add(chip);
  c.add(text(scene, -w / 2 + 24, -h / 2 + 15, p.position, 11, '#ffffff', { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5));
  c.add(scene.add.circle(w / 2 - 14, -h / 2 + 15, 7, ELEMENT_COLOR[p.element]).setStrokeStyle(2, 0xffffff));
  // nombre, rareza
  const name = text(scene, 0, h / 2 - 50, p.name, 14, '#ffffff', { fontStyle: 'italic bold', align: 'center', wordWrap: { width: w - 10 } }).setOrigin(0.5);
  for (let s = 14; name.height > 36 && s > 9; ) name.setFontSize(--s);
  c.add(name);
  c.add(text(scene, 0, h / 2 - 26, stars(card.rarity), 15, r.css, { strokeThickness: 3 }).setOrigin(0.5));
  c.add(text(scene, 0, h / 2 - 10, r.name, 10, r.css, { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5));
  c.setSize(w, h);
  return c;
}
