// Gráficos provisionales generados por código. Se usan solo cuando el
// paquete de sprites (src/assets/pack/) no trae la imagen correspondiente.

import Phaser from 'phaser';
import { FONT, hex } from '../config';
import { lookOf, type Look } from '../data/looks';
import type { PlayerData, TeamData } from '../data/types';

export const SPRITE_W = 36;
export const SPRITE_H = 48;

export const texKey = {
  /** Con equipo: el sprite con su equipación. Sin equipo: el del paquete (src/assets/pack/sprites/<id>). */
  sprite: (playerId: string, teamId?: string) => (teamId ? `sprite:${teamId}:${playerId}` : `sprite:${playerId}`),
  /** Con equipo: el retrato de Victory Road de ese equipo (src/assets/pack/portraits/<equipo>/<id>). */
  portrait: (playerId: string, teamId?: string) => (teamId ? `portrait:${teamId}:${playerId}` : `portrait:${playerId}`),
  emblem: (teamId: string) => `emblem:${teamId}`,
};

/** Textura del jugador en el campo: la del paquete si la hay; si no, la dibujada con su equipación. */
export function spriteKey(scene: Phaser.Scene, p: PlayerData, team: TeamData): string {
  const pack = texKey.sprite(p.id);
  if (scene.textures.exists(pack)) return pack;
  makePlayerSprite(scene, p, team);
  return texKey.sprite(p.id, team.id);
}

/** Retrato del jugador: el de Victory Road de su equipo, el genérico del paquete o uno dibujado. */
export function portraitKey(scene: Phaser.Scene, p: PlayerData, team: TeamData): string {
  for (const key of [texKey.portrait(p.id, team.id), texKey.portrait(p.id)]) if (scene.textures.exists(key)) return key;
  makePortrait(scene, p, team);
  return `portrait-gen:${team.id}:${p.id}`;
}

export function darken(color: number, f: number): number {
  const c = Phaser.Display.Color.IntegerToColor(color);
  return Phaser.Display.Color.GetColor(c.red * f, c.green * f, c.blue * f);
}

// ------------------------------------------------------------------ sprite de campo

/** Cabeza genérica (22x20) para quien no tiene retrato: pelo corto y cara. */
const DEFAULT_HEAD = [
  '......................',
  '.......########.......',
  '.....############.....',
  '....##############....',
  '...################...',
  '...################...',
  '...################...',
  '..##################..',
  '..###ssss####ssss###..',
  '..##ssssssssssssss##..',
  '..#ssssssssssssssss#..',
  '..#ssssssssssssssss#..',
  '..sssseessssssseesss..',
  '..sssseessssssseesss..',
  '...ssssssssssssssss...',
  '...ssssssssssssssss...',
  '....ssssssssssssss....',
  '.....ssssssssssss.....',
  '.......ssssssss.......',
  '.........ssss.........',
];

/** Cuerpo de frente, piernas abiertas como en los partidos de IE3 (26 de ancho). */
const BODY = [
  '..........CccC............',
  '......ssssCSSCssss........',
  '.....ssssssSSssssss.......',
  '....tssssssssssssssst.....',
  '....ttssssssssssssstt.....',
  '....kkssssssssssssskk.....',
  '....kk.ppppppppppp.kk.....',
  '.......pppppppppppp.......',
  '......ppppp..ppppppp......',
  '.....kkkk......kkkk.......',
  '.....kkk........kkk.......',
  '....ccc.........ccc.......',
  '....ccc..........ccc......',
  '...bbbb..........bbbb.....',
  '...bbbb..........bbbb.....',
];

export const SPRITE_PX = { w: 26, h: 33 };

type RGB = [number, number, number];
const rgb = (c: number): RGB => [(c >> 16) & 255, (c >> 8) & 255, c & 255];
const shadeRgb = (c: RGB, f: number): RGB => [Math.min(255, c[0] * f), Math.min(255, c[1] * f), Math.min(255, c[2] * f)];

function genericLook(p: PlayerData): Look {
  return { hair: p.look?.hair ?? '#3a2a1a', skin: p.look?.skin ?? '#f1c79b', eyes: '#2a1a14', head: DEFAULT_HEAD };
}

/**
 * Muñeco en pixel art parecido al jugador: la cabeza sale de su retrato de Victory Road (silueta del pelo,
 * piel, ojos y accesorio, en src/data/looks.json) y el cuerpo lleva la equipación de su equipo.
 */
function drawPixelSprite(p: PlayerData, team: TeamData): ImageData {
  const look = lookOf(team.id, p.id) ?? genericLook(p);
  const { w: W, h: H } = SPRITE_PX;
  const img = new ImageData(W, H);
  const put = (x: number, y: number, c: RGB) => {
    if (x < 0 || y < 0 || x >= W || y >= H) return;
    const i = (y * W + x) * 4;
    img.data[i] = c[0];
    img.data[i + 1] = c[1];
    img.data[i + 2] = c[2];
    img.data[i + 3] = 255;
  };
  const skin = rgb(hex(look.skin));
  const hair = rgb(hex(look.hair));
  const eyes = rgb(hex(look.eyes));
  const acc = look.accessory ? rgb(hex(look.accessory)) : hair;
  const shirt = rgb(hex(p.position === 'GK' ? team.colors.gkShirt : team.colors.shirt));
  const shorts = rgb(hex(team.colors.shorts));
  const trim = rgb(hex(team.colors.accent));
  const socks = p.position === 'GK' ? shirt : shorts;
  // cuerpo
  const bodyY = 18;
  const bodyPal: Record<string, RGB> = { s: shirt, S: trim, C: trim, c: socks, t: shadeRgb(shirt, 0.78), k: skin, p: shorts, b: [36, 36, 44] };
  BODY.forEach((row, y) => [...row].forEach((ch, x) => ch in bodyPal && put(x, bodyY + y, ch === 'C' && y === 0 ? trim : ch === 'c' && y < 3 ? trim : bodyPal[ch])));
  // cabeza
  const head = look.head.length ? look.head : DEFAULT_HEAD;
  const hasEyes = head.some((r) => r.includes('e'));
  const at = (x: number, y: number) => head[y]?.[x] ?? '.';
  head.forEach((row, y) =>
    [...row].forEach((ch, x) => {
      const px = x + 2;
      if (ch === '#') {
        // brillo arriba, sombra abajo
        const up = at(x, y - 1) === '.';
        const down = at(x, y + 1) === 's' || at(x, y + 1) === 'e';
        put(px, y, up ? shadeRgb(hair, 1.25) : down ? shadeRgb(hair, 0.72) : hair);
      } else if (ch === 'a') put(px, y, at(x, y - 1) === 'a' ? acc : shadeRgb(acc, 1.2));
      else if (ch === 's') put(px, y, at(x, y - 1) === '#' || at(x, y - 1) === 'a' ? shadeRgb(skin, 0.86) : skin);
      else if (ch === 'e') put(px, y, at(x, y - 1) === 'e' ? eyes : [250, 250, 250]);
    }),
  );
  if (!hasEyes) {
    // ojos por defecto: en la fila de cara más ancha por encima del centro
    let best = 12;
    let bestW = 0;
    for (let y = 9; y < 15; y++) {
      const w = [...(head[y] ?? '')].filter((c) => c === 's').length;
      if (w > bestW) [best, bestW] = [y, w];
    }
    const row = head[best] ?? '';
    const xs = [...row].map((c, i) => (c === 's' ? i : -1)).filter((i) => i >= 0);
    if (xs.length > 6) {
      const mid = Math.round((xs[0] + xs[xs.length - 1]) / 2);
      for (const ex of [mid - 4, mid + 3]) {
        put(ex + 2, best, eyes);
        put(ex + 3, best, eyes);
        put(ex + 2, best + 1, eyes);
        put(ex + 3, best + 1, [250, 250, 250]);
      }
    }
  }
  // contorno oscuro alrededor de todo
  const filled = (x: number, y: number) => x >= 0 && y >= 0 && x < W && y < H && img.data[(y * W + x) * 4 + 3] === 255;
  const edge: [number, number][] = [];
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (!filled(x, y) && (filled(x - 1, y) || filled(x + 1, y) || filled(x, y - 1) || filled(x, y + 1))) edge.push([x, y]);
  for (const [x, y] of edge) put(x, y, [28, 20, 22]);
  return img;
}

export function makePlayerSprite(scene: Phaser.Scene, p: PlayerData, team: TeamData): void {
  const key = texKey.sprite(p.id, team.id);
  if (scene.textures.exists(key)) return;
  const tex = scene.textures.createCanvas(key, SPRITE_PX.w, SPRITE_PX.h);
  if (!tex) return;
  tex.getContext().putImageData(drawPixelSprite(p, team), 0, 0);
  tex.refresh();
  tex.setFilter(Phaser.Textures.FilterMode.NEAREST);
}

/** Retrato de reserva para quien no tiene el de Victory Road: la cabeza del sprite en grande. */
export function makePortrait(scene: Phaser.Scene, p: PlayerData, team: TeamData): void {
  const key = `portrait-gen:${team.id}:${p.id}`;
  if (scene.textures.exists(key)) return;
  const size = 96;
  const tex = scene.textures.createCanvas(key, size, size);
  if (!tex) return;
  const ctx = tex.getContext();
  const accent = Phaser.Display.Color.IntegerToColor(hex(team.colors.accent));
  ctx.fillStyle = accent.rgba;
  ctx.fillRect(0, 0, size, size);
  const sprite = document.createElement('canvas');
  sprite.width = SPRITE_PX.w;
  sprite.height = SPRITE_PX.h;
  sprite.getContext('2d')!.putImageData(drawPixelSprite(p, team), 0, 0);
  ctx.imageSmoothingEnabled = false;
  // la cabeza (22x20) ocupa el retrato
  ctx.drawImage(sprite, 1, 0, 24, 24, 0, 0, size, size);
  ctx.fillStyle = '#ffffff';
  ctx.font = `bold 18px ${FONT}`;
  ctx.strokeStyle = '#000000';
  ctx.lineWidth = 4;
  ctx.strokeText(String(p.number), 8, size - 10);
  ctx.fillText(String(p.number), 8, size - 10);
  tex.refresh();
  tex.setFilter(Phaser.Textures.FilterMode.NEAREST);
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
