import Phaser from 'phaser';
import { RARITY, type Rarity } from '../club/pool';
import { ELEMENT_COLOR, ELEMENT_LABEL } from '../data/elements';
import type { MoveData, MoveKind } from '../data/types';
import { dim } from './theme';
import { text } from './widgets';

export const KIND_LABEL: Record<MoveKind, string> = { shoot: 'TIRO', dribble: 'REGATE', block: 'BLOQUEO', catch: 'PARADA' };

/**
 * Cuaderno de supertécnica: tapas del color de su afinidad, lomo a la izquierda, nombre, tipo, potencia y coste,
 * y la rareza en el marco y las estrellas. (x, y) es el centro.
 */
export function drawNotebook(scene: Phaser.Scene, x: number, y: number, move: MoveData, rarity: Rarity, w = 128, h = 172): Phaser.GameObjects.Container {
  const c = scene.add.container(x, y);
  const r = RARITY[rarity];
  const el = ELEMENT_COLOR[move.element];
  const g = scene.add.graphics();
  g.fillStyle(0x000000, 0.45).fillRoundedRect(-w / 2 + 4, -h / 2 + 5, w, h, 8);
  // tapa
  g.fillStyle(dim(el, 0.35)).fillRoundedRect(-w / 2, -h / 2, w, h, 8);
  g.fillStyle(0xffffff, 0.06);
  for (let i = -h; i < h; i += 14) g.fillRect(-w / 2 + 14, -h / 2 + Math.max(0, i), w - 14, 2);
  // lomo
  g.fillStyle(dim(el, 0.6)).fillRoundedRect(-w / 2, -h / 2, 14, h, { tl: 8, bl: 8, tr: 0, br: 0 });
  g.lineStyle(2, 0x000000, 0.35).lineBetween(-w / 2 + 14, -h / 2, -w / 2 + 14, h / 2);
  // etiqueta del título
  g.fillStyle(0xfff6d8).fillRoundedRect(-w / 2 + 20, -h / 2 + 30, w - 28, 58, 4);
  g.lineStyle(2, el).strokeRoundedRect(-w / 2 + 20, -h / 2 + 30, w - 28, 58, 4);
  // marco de rareza
  g.lineStyle(rarity >= 3 ? 4 : 3, r.color).strokeRoundedRect(-w / 2, -h / 2, w, h, 8);
  c.add(g);
  c.add(text(scene, 7, -h / 2 + 16, KIND_LABEL[move.kind], 11, '#ffffff', { fontStyle: 'bold', strokeThickness: 3 }).setOrigin(0.5));
  const name = text(scene, 7, -h / 2 + 59, move.name, 14, '#1b2433', { fontStyle: 'bold', align: 'center', wordWrap: { width: w - 34 }, strokeThickness: 0 }).setOrigin(0.5);
  for (let s = 14; name.height > 52 && s > 9; ) name.setFontSize(--s);
  c.add(name);
  c.add(text(scene, 7, 14, String(move.power), 30, '#ffffff', { fontStyle: 'bold', strokeThickness: 5 }).setOrigin(0.5));
  c.add(text(scene, 7, 38, `${ELEMENT_LABEL[move.element]} · TP ${move.tp}${move.long ? ' · lejos' : ''}`, 10, '#e3e9f2', { strokeThickness: 2 }).setOrigin(0.5));
  c.add(text(scene, 7, h / 2 - 26, '★'.repeat(rarity), 15, r.css, { strokeThickness: 3 }).setOrigin(0.5));
  c.add(text(scene, 7, h / 2 - 10, 'CUADERNO', 9, r.css, { fontStyle: 'bold', strokeThickness: 2 }).setOrigin(0.5));
  c.setSize(w, h);
  return c;
}
