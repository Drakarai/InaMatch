import Phaser from 'phaser';
import { ELEMENT_COLOR } from '../data/elements';
import type { Element, MoveKind } from '../data/types';
import { sfx, techSfx } from '../audio/sfx';
import { DEPTH, GROUND, angleOf, cleanup, flash, lighten, particles, ring, shake, wait } from './fxkit';
import { SHAPES } from './fxshapes';

/**
 * Efectos especiales de las supertécnicas, dibujados por código sobre el campo.
 * Cada técnica tiene su receta en src/data/movefx.json (tools/zukan/recipes.py, a partir de los
 * vídeos de la enciclopedia oficial): una forma con su variante ("dragon:wyvern", "hand:majin"...),
 * capas que la acompañan y los colores reales del vídeo. Las formas nuevas están en fxshapes.ts.
 */
export type FxName =
  | 'penguin'
  | 'dragon'
  | 'bird'
  | 'beast'
  | 'hand'
  | 'punch'
  | 'wall'
  | 'shield'
  | 'sword'
  | 'meteor'
  | 'tornado'
  | 'ice'
  | 'fire'
  | 'lightning'
  | 'water'
  | 'flower'
  | 'earth'
  | 'dark'
  | 'light'
  | 'clone'
  | 'wind'
  | 'impact';

export interface FxOptions {
  element: Element;
  kind: MoveKind;
  /** Hacia dónde va la acción (hacia la portería rival al tirar, hacia el tiro al parar). */
  dir: { x: number; y: number };
  /** Textura del jugador, para los efectos que lo duplican. */
  texture?: string;
  scale?: number;
}

/** Colores propios de los efectos de elemento; el resto toma el de la afinidad de la técnica. */
const PALETTE: Partial<Record<FxName, [number, number]>> = {
  fire: [0xff5a1a, 0xffd23f],
  ice: [0x8fe3ff, 0xffffff],
  lightning: [0xfff06a, 0x7fd8ff],
  water: [0x2f8fff, 0xbfe9ff],
  flower: [0xff7fc0, 0xfff0f6],
  earth: [0xa8743a, 0xe8c890],
  dark: [0x9a3cff, 0x2a0040],
  light: [0xfff0a0, 0xffffff],
  meteor: [0xffe07a, 0xa88cff],
  hand: [0xffc93c, 0xfff6c8],
};

/** Partícula propia de cada efecto (para la estela del balón y la animación de la técnica). */
const PARTICLE: Record<string, string> = {
  fire: 'fx-flame',
  ice: 'fx-flake',
  lightning: 'fx-spark',
  water: 'fx-bubble',
  flower: 'fx-petal',
  meteor: 'fx-star',
  light: 'fx-star',
  bird: 'fx-feather',
  penguin: 'fx-penguin',
  earth: 'fx-rock',
  wall: 'fx-rock',
  rocks: 'fx-rock',
  stars: 'fx-star',
  comet: 'fx-star',
  hearts: 'fx-heart',
  notes: 'fx-note',
  confetti: 'fx-petal',
  fireworks: 'fx-star',
  wings: 'fx-feather',
  butterfly: 'fx-petal',
  bubbles: 'fx-bubble',
};

export function fxParticle(recipe: FxRecipe): { key: string; additive: boolean } {
  const key = PARTICLE[baseOf(recipe.fx)] ?? 'fx-glow';
  return { key, additive: !['fx-penguin', 'fx-rock', 'fx-petal', 'fx-feather'].includes(key) };
}

export function fxColors(recipe: FxRecipe, element: Element): [number, number] {
  const [c1, c2] = fxPalette(recipe, element);
  return [c1, c2];
}

function colors(name: FxName, element: Element): number[] {
  const own = PALETTE[name];
  if (own) return [...own];
  const base = ELEMENT_COLOR[element];
  return [base, Phaser.Display.Color.ValueToColor(base).lighten(35).color];
}

// ------------------------------------------------------------------ texturas

/** Texturas de partículas, dibujadas una vez al arrancar. */
export function makeFxTextures(scene: Phaser.Scene): void {
  const make = (key: string, w: number, h: number, draw: (g: Phaser.GameObjects.Graphics) => void) => {
    if (scene.textures.exists(key)) return;
    const g = scene.make.graphics({}, false);
    draw(g);
    g.generateTexture(key, w, h);
    g.destroy();
  };
  make('fx-glow', 32, 32, (g) => {
    for (let r = 16; r > 0; r -= 1) g.fillStyle(0xffffff, 0.06 + (1 - r / 16) * 0.12).fillCircle(16, 16, r);
  });
  make('fx-spark', 8, 28, (g) => {
    g.fillStyle(0xffffff, 0.5).fillEllipse(4, 14, 8, 28);
    g.fillStyle(0xffffff).fillEllipse(4, 14, 3, 22);
  });
  make('fx-flame', 24, 32, (g) => {
    g.fillStyle(0xffffff, 0.35).fillTriangle(12, 0, 2, 22, 22, 22).fillCircle(12, 22, 10);
    g.fillStyle(0xffffff, 0.9).fillTriangle(12, 8, 6, 22, 18, 22).fillCircle(12, 23, 6);
  });
  make('fx-shard', 14, 24, (g) => {
    g.fillStyle(0xffffff, 0.85).fillTriangle(7, 0, 0, 24, 14, 24);
    g.fillStyle(0xffffff).fillTriangle(7, 2, 5, 22, 8, 22);
  });
  make('fx-petal', 14, 9, (g) => {
    g.fillStyle(0xffffff).fillEllipse(7, 4.5, 14, 9);
  });
  make('fx-star', 20, 20, (g) => {
    const pts = Array.from({ length: 10 }, (_, i) => {
      const a = -Math.PI / 2 + (i * Math.PI) / 5;
      const r = i % 2 ? 4 : 10;
      return new Phaser.Geom.Point(10 + Math.cos(a) * r, 10 + Math.sin(a) * r);
    });
    g.fillStyle(0xffffff).fillPoints(pts, true);
  });
  make('fx-feather', 10, 26, (g) => {
    g.fillStyle(0xffffff, 0.9).fillEllipse(5, 13, 10, 26);
    g.lineStyle(1, 0xd0d8e8).lineBetween(5, 2, 5, 26);
  });
  make('fx-flake', 18, 18, (g) => {
    g.lineStyle(2, 0xffffff);
    for (let i = 0; i < 3; i++) {
      const a = (i * Math.PI) / 3;
      g.lineBetween(9 - Math.cos(a) * 8, 9 - Math.sin(a) * 8, 9 + Math.cos(a) * 8, 9 + Math.sin(a) * 8);
    }
  });
  make('fx-rock', 16, 16, (g) => {
    g.fillStyle(0xffffff).fillPoints([2, 6, 7, 1, 14, 4, 15, 11, 9, 15, 3, 13].reduce<Phaser.Geom.Point[]>((acc, v, i, a) => (i % 2 ? acc : [...acc, new Phaser.Geom.Point(v, a[i + 1])]), []), true);
    g.fillStyle(0x000000, 0.25).fillTriangle(9, 15, 15, 11, 8, 8);
  });
  make('fx-bubble', 20, 20, (g) => {
    g.lineStyle(2, 0xffffff, 0.9).strokeCircle(10, 10, 8);
    g.fillStyle(0xffffff, 0.8).fillCircle(7, 7, 2.5);
  });
  make('fx-heart', 20, 18, (g) => {
    g.fillStyle(0xffffff).fillCircle(6, 6, 5.5).fillCircle(14, 6, 5.5).fillTriangle(1, 8, 19, 8, 10, 18);
  });
  make('fx-note', 16, 22, (g) => {
    g.fillStyle(0xffffff).fillEllipse(5, 18, 9, 7).fillRect(8, 2, 2.5, 16).fillTriangle(10, 2, 16, 6, 10, 9);
  });
  make('fx-penguin', 24, 30, (g) => {
    g.fillStyle(0x10141c).fillEllipse(12, 17, 20, 26);
    g.fillStyle(0xffffff).fillEllipse(12, 19, 12, 18);
    g.fillStyle(0xffffff).fillCircle(8, 9, 2.6).fillCircle(16, 9, 2.6);
    g.fillStyle(0x000000).fillCircle(8.5, 9, 1.2).fillCircle(15.5, 9, 1.2);
    g.fillStyle(0xffa21f).fillTriangle(9, 12, 15, 12, 12, 16);
    g.fillStyle(0xffa21f).fillEllipse(8, 29, 6, 3).fillEllipse(16, 29, 6, 3);
  });
}

// ------------------------------------------------------------------ efectos

export type FxFn = (scene: Phaser.Scene, x: number, y: number, o: FxOptions, c: number[], variant: string) => Promise<void>;

/** Receta del efecto de una técnica. */
export interface FxRecipe {
  /** Forma principal, con variante opcional: "fire", "dragon:wyvern"... */
  fx: string;
  /** Efectos que acompañan a la principal, a la vez y algo más pequeños. */
  layers?: string[];
  /** Colores sacados del vídeo de la técnica (#rrggbb). */
  colors?: string[];
}

const fire: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  ring(scene, x, y + 18, c1, 80, 600, 8);
  const pillar = particles(scene, x, y + 16, 'fx-flame', {
    speedY: { min: -360, max: -200 },
    speedX: { min: -50, max: 50 },
    scale: { start: 2.4, end: 0.3 },
    alpha: { start: 1, end: 0 },
    tint: [c2, c1, 0xff2a00],
    lifespan: 700,
    frequency: 10,
    quantity: 4,
    emitting: true,
  });
  const embers = particles(scene, x, y, 'fx-glow', { speed: { min: 80, max: 260 }, scale: { start: 0.5, end: 0 }, tint: [c2, c1], lifespan: 700, gravityY: -120 });
  embers.explode(40);
  flash(scene, x, y, c1, 120);
  await wait(scene, 700);
  pillar.stop();
  cleanup(scene, 900, pillar, embers);
};

const ice: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const frost = scene.add.graphics({ x, y: y + 18 }).setDepth(GROUND);
  frost.fillStyle(c1, 0.35).fillEllipse(0, 0, 150, 70);
  for (let i = 0; i < 12; i++) {
    const a = (i / 12) * Math.PI * 2;
    frost.lineStyle(2, c2, 0.8).lineBetween(0, 0, Math.cos(a) * 80, Math.sin(a) * 38);
  }
  frost.setScale(0.2);
  scene.tweens.add({ targets: frost, scale: 1, duration: 260, ease: 'Back.out' });
  scene.tweens.add({ targets: frost, alpha: 0, delay: 800, duration: 400, onComplete: () => frost.destroy() });
  // cristales que brotan alrededor
  const crystals: Phaser.GameObjects.Image[] = [];
  for (let i = 0; i < 9; i++) {
    const a = (i / 9) * Math.PI * 2;
    const cx = x + Math.cos(a) * 48;
    const cy = y + 14 + Math.sin(a) * 22;
    const s = scene.add.image(cx, cy, 'fx-shard').setTint(i % 2 ? c1 : c2).setOrigin(0.5, 1).setDepth(cy).setScale(0.3, 0);
    s.setAngle(Math.cos(a) * 25);
    scene.tweens.add({ targets: s, scaleY: 2.2 + (i % 3) * 0.5, scaleX: 1.2, duration: 220, delay: i * 25, ease: 'Back.out' });
    crystals.push(s);
  }
  const flakes = particles(scene, x, y - 40, 'fx-flake', { speed: { min: 40, max: 160 }, scale: { start: 1, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [c1, c2], lifespan: 1000, rotate: { min: 0, max: 360 }, gravityY: 60 });
  flakes.explode(30);
  flash(scene, x, y, c2, 110);
  await wait(scene, 750);
  crystals.forEach((s) => scene.tweens.add({ targets: s, alpha: 0, scaleY: 0, duration: 250, onComplete: () => s.destroy() }));
  cleanup(scene, 1100, flakes);
};

/** Rayo quebrado del cielo al punto. */
function bolt(scene: Phaser.Scene, x: number, y: number, color: number, height = 340): void {
  const g = scene.add.graphics().setDepth(DEPTH);
  const pts: Phaser.Math.Vector2[] = [];
  let px = x + Phaser.Math.Between(-40, 40);
  for (let i = 0; i <= 8; i++) {
    const t = i / 8;
    pts.push(new Phaser.Math.Vector2(i === 8 ? x : px, y - height * (1 - t)));
    px += Phaser.Math.Between(-28, 28);
  }
  g.lineStyle(12, color, 0.35).strokePoints(pts);
  g.lineStyle(4, 0xffffff, 1).strokePoints(pts);
  scene.tweens.add({ targets: g, alpha: 0, duration: 260, delay: 80, onComplete: () => g.destroy() });
}

const lightning: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  for (let i = 0; i < 4; i++) scene.time.delayedCall(i * 110, () => bolt(scene, x + Phaser.Math.Between(-20, 20), y, i % 2 ? c2 : c1));
  const sparks = particles(scene, x, y, 'fx-spark', { speed: { min: 200, max: 480 }, scale: { start: 0.9, end: 0 }, tint: [c1, c2, 0xffffff], lifespan: 380, rotate: { onEmit: () => Phaser.Math.Between(0, 360) } });
  scene.time.delayedCall(120, () => sparks.explode(36));
  ring(scene, x, y + 18, c1, 90, 450, 7);
  scene.time.delayedCall(120, () => {
    flash(scene, x, y, c1, 160, 260);
    shake(scene, 140, 0.007);
  });
  await wait(scene, 650);
  cleanup(scene, 500, sparks);
};

const water: FxFn = async (scene, x, y, o, [c1, c2]) => {
  for (let i = 0; i < 3; i++) scene.time.delayedCall(i * 130, () => ring(scene, x, y + 18, i % 2 ? c2 : c1, 70 + i * 28, 650, 6));
  const drops = particles(scene, x, y + 10, 'fx-glow', { speed: { min: 220, max: 460 }, angle: { min: 230, max: 310 }, scale: { start: 1.4, end: 0.4 }, alpha: { start: 0.95, end: 0.2 }, tint: [c1, c2, 0xffffff], lifespan: 1000, gravityY: 700 });
  drops.explode(80);
  const bubbles = particles(scene, x, y, 'fx-bubble', { speed: { min: 20, max: 90 }, speedY: { min: -120, max: -40 }, scale: { start: 0.6, end: 1.2 }, alpha: { start: 0.9, end: 0 }, tint: c2, lifespan: 1100, blendMode: 'NORMAL' });
  bubbles.explode(16);
  // ola que avanza en la dirección del jugador
  const wave = scene.add.graphics({ x, y }).setDepth(DEPTH);
  const a = angleOf(o.dir);
  wave.setRotation(a + Math.PI / 2);
  wave.fillStyle(c1, 0.75).fillEllipse(0, 0, 200, 56);
  wave.fillStyle(c2, 0.9).fillEllipse(0, -12, 160, 22);
  wave.lineStyle(3, 0xffffff, 0.9).strokeEllipse(0, -12, 160, 22);
  scene.tweens.add({ targets: wave, x: x + o.dir.x * 160, y: y + o.dir.y * 160, alpha: 0, scaleX: 1.6, duration: 700, ease: 'Quad.out', onComplete: () => wave.destroy() });
  await wait(scene, 700);
  cleanup(scene, 600, drops, bubbles);
};

const flower: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const petals = particles(scene, x, y, 'fx-petal', {
    speed: { min: 60, max: 220 },
    scale: { start: 1.2, end: 0.4 },
    alpha: { start: 1, end: 0 },
    tint: [c1, c2, 0xffb0d8],
    lifespan: 1300,
    rotate: { start: 0, end: 540 },
    gravityY: 40,
    blendMode: 'NORMAL',
  });
  petals.explode(70);
  // remolino de pétalos girando alrededor del jugador
  const swirl: Phaser.GameObjects.Image[] = [];
  for (let i = 0; i < 16; i++) swirl.push(scene.add.image(x, y, 'fx-petal').setTint(i % 2 ? c1 : c2).setDepth(DEPTH));
  const s = { t: 0 };
  scene.tweens.add({
    targets: s,
    t: 1,
    duration: 900,
    onUpdate: () =>
      swirl.forEach((p, i) => {
        const a = s.t * Math.PI * 4 + (i / swirl.length) * Math.PI * 2;
        const r = 30 + s.t * 60;
        p.setPosition(x + Math.cos(a) * r, y - s.t * 40 + Math.sin(a) * r * 0.45).setAngle(a * 57).setAlpha(1 - s.t);
      }),
    onComplete: () => swirl.forEach((p) => p.destroy()),
  });
  flash(scene, x, y, c1, 90);
  await wait(scene, 800);
  cleanup(scene, 800, petals);
};

const earth: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const cracks = scene.add.graphics({ x, y: y + 18 }).setDepth(GROUND);
  cracks.lineStyle(4, 0x2a1a0a, 0.9);
  for (let i = 0; i < 9; i++) {
    let a = (i / 9) * Math.PI * 2;
    let px = 0;
    let py = 0;
    cracks.beginPath().moveTo(0, 0);
    for (let k = 0; k < 4; k++) {
      a += Phaser.Math.FloatBetween(-0.4, 0.4);
      px += Math.cos(a) * 22;
      py += Math.sin(a) * 11;
      cracks.lineTo(px, py);
    }
    cracks.strokePath();
  }
  scene.tweens.add({ targets: cracks, alpha: 0, delay: 900, duration: 400, onComplete: () => cracks.destroy() });
  const rocks = particles(scene, x, y + 12, 'fx-rock', { speed: { min: 160, max: 360 }, angle: { min: 200, max: 340 }, scale: { min: 0.8, max: 1.8 }, tint: [c1, c2, 0x6a4a2a], lifespan: 900, gravityY: 800, rotate: { start: 0, end: 360 }, blendMode: 'NORMAL' });
  rocks.explode(26);
  const dust = particles(scene, x, y + 16, 'fx-glow', { speed: { min: 40, max: 140 }, scale: { start: 1.4, end: 2.6 }, alpha: { start: 0.5, end: 0 }, tint: c2, lifespan: 900, blendMode: 'NORMAL' });
  dust.explode(18);
  ring(scene, x, y + 18, c1, 110, 550, 9);
  shake(scene, 220, 0.01);
  await wait(scene, 700);
  cleanup(scene, 700, rocks, dust);
};

const dark: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const vortex = scene.add.graphics({ x, y }).setDepth(DEPTH - 1);
  for (let arm = 0; arm < 5; arm++) {
    vortex.lineStyle(7, arm % 2 ? c1 : 0x000000, 0.75).beginPath();
    for (let t = 0; t < 1; t += 0.05) {
      const a = arm * ((Math.PI * 2) / 5) + t * Math.PI * 2.2;
      const r = 8 + t * 95;
      const px = Math.cos(a) * r;
      const py = Math.sin(a) * r * 0.55;
      if (t === 0) vortex.moveTo(px, py);
      else vortex.lineTo(px, py);
    }
    vortex.strokePath();
  }
  vortex.fillStyle(c2, 0.9).fillEllipse(0, 0, 40, 22);
  vortex.setScale(0.2).setAlpha(0);
  scene.tweens.add({ targets: vortex, scale: 1, alpha: 1, duration: 260 });
  scene.tweens.add({ targets: vortex, rotation: -Math.PI * 2, duration: 1000 });
  scene.tweens.add({ targets: vortex, alpha: 0, delay: 750, duration: 300, onComplete: () => vortex.destroy() });
  // partículas oscuras que se tragan hacia el centro
  const pull = particles(scene, x, y, 'fx-glow', {
    emitZone: { type: 'edge', source: new Phaser.Geom.Circle(0, 0, 110), quantity: 32 },
    moveToX: 0,
    moveToY: 0,
    scale: { start: 0.9, end: 0.1 },
    tint: [c1, 0x5a00a0],
    lifespan: 500,
    frequency: 25,
    quantity: 2,
    emitting: true,
  });
  pull.setPosition(x, y);
  // ojos rojos
  const eyes = scene.add.graphics({ x, y: y - 70 }).setDepth(DEPTH);
  eyes.fillStyle(0xff2030).fillEllipse(-16, 0, 14, 6).fillEllipse(16, 0, 14, 6);
  eyes.setAlpha(0);
  scene.tweens.add({ targets: eyes, alpha: 1, duration: 200, delay: 250, yoyo: true, hold: 300, onComplete: () => eyes.destroy() });
  await wait(scene, 850);
  pull.stop();
  cleanup(scene, 600, pull);
};

const light: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const beam = scene.add.graphics({ x, y }).setDepth(DEPTH - 1);
  for (let i = 0; i < 6; i++) beam.fillStyle(i % 2 ? c1 : c2, 0.12).fillRect(-50 + i * 7, -520, 100 - i * 14, 540);
  beam.setScale(0.1, 1).setAlpha(0);
  scene.tweens.add({ targets: beam, scaleX: 1, alpha: 1, duration: 220, ease: 'Cubic.out' });
  scene.tweens.add({ targets: beam, alpha: 0, scaleX: 0.3, delay: 700, duration: 300, onComplete: () => beam.destroy() });
  const rays = scene.add.graphics({ x, y }).setDepth(DEPTH - 1);
  for (let i = 0; i < 12; i++) {
    const a = (i / 12) * Math.PI * 2;
    rays.fillStyle(c1, 0.25).fillTriangle(0, 0, Math.cos(a - 0.08) * 150, Math.sin(a - 0.08) * 150, Math.cos(a + 0.08) * 150, Math.sin(a + 0.08) * 150);
  }
  rays.setScale(0.3);
  scene.tweens.add({ targets: rays, scale: 1.1, rotation: 0.6, alpha: 0, duration: 950, onComplete: () => rays.destroy() });
  const feathers = particles(scene, x, y - 160, 'fx-feather', { speedX: { min: -80, max: 80 }, speedY: { min: 20, max: 90 }, scale: { start: 1, end: 0.6 }, alpha: { start: 1, end: 0 }, tint: [0xffffff, c2], lifespan: 1300, rotate: { min: -40, max: 40 }, blendMode: 'NORMAL' });
  feathers.explode(16);
  const stars = particles(scene, x, y, 'fx-star', { speed: { min: 60, max: 220 }, scale: { start: 0.9, end: 0 }, tint: [c1, c2], lifespan: 800 });
  stars.explode(26);
  flash(scene, x, y, c2, 150);
  await wait(scene, 800);
  cleanup(scene, 900, feathers, stars);
};

const meteor: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  const falls: Promise<void>[] = [];
  for (let i = 0; i < 6; i++) {
    falls.push(
      new Promise((resolve) => {
        const sx = x + 240 + Phaser.Math.Between(-60, 60);
        const sy = y - 340 + Phaser.Math.Between(-40, 40);
        const tx = x + Phaser.Math.Between(-60, 60);
        const ty = y + Phaser.Math.Between(-20, 20);
        const star = scene.add.image(sx, sy, 'fx-star').setTint(i % 2 ? c1 : c2).setDepth(DEPTH).setScale(2.6);
        const trail = particles(scene, sx, sy, 'fx-glow', { scale: { start: 1.8, end: 0 }, alpha: { start: 0.9, end: 0 }, tint: [c1, c2, 0xffffff], lifespan: 380, frequency: 10, quantity: 2, emitting: true });
        trail.startFollow(star);
        scene.tweens.add({
          targets: star,
          x: tx,
          y: ty,
          angle: 360,
          duration: 380,
          delay: i * 90,
          ease: 'Quad.in',
          onComplete: () => {
            trail.stop();
            star.destroy();
            ring(scene, tx, ty + 16, c1, 60, 450, 6);
            flash(scene, tx, ty, c2, 90, 300);
            cleanup(scene, 400, trail);
            resolve();
          },
        });
      }),
    );
  }
  const twinkle = particles(scene, x, y - 60, 'fx-star', { speed: { min: 20, max: 120 }, scale: { start: 0.6, end: 0 }, tint: [c1, c2, 0xffffff], lifespan: 900 });
  twinkle.explode(30);
  await Promise.all(falls);
  shake(scene, 150, 0.006);
  cleanup(scene, 900, twinkle);
};

/** Embudo de viento girando: anillos apilados que se ensanchan hacia arriba y rayas que dan vueltas. */
const tornado: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const g = scene.add.graphics().setDepth(DEPTH);
  const s = { t: 0 };
  const H = 210;
  scene.tweens.add({
    targets: s,
    t: 1,
    duration: 1000,
    onUpdate: () => {
      const grow = Math.min(1, s.t * 4);
      const fade = s.t > 0.8 ? (1 - s.t) / 0.2 : 1;
      g.clear();
      for (let i = 0; i < 9; i++) {
        const h = i / 8;
        const r = (16 + h * 78) * grow;
        const cy = y + 16 - h * H * grow;
        g.fillStyle(c1, 0.16 * fade).fillEllipse(x + Math.sin(s.t * 12 + i) * 6, cy, r * 2, r * 0.5);
        g.lineStyle(3, i % 2 ? c2 : c1, 0.75 * fade).strokeEllipse(x + Math.sin(s.t * 12 + i) * 6, cy, r * 2, r * 0.5);
      }
      // rayas que giran por la superficie del embudo
      for (let k = 0; k < 14; k++) {
        const h = (k * 0.137 + s.t * 1.5) % 1;
        const a = s.t * Math.PI * 10 + k * 2.1;
        const r = (16 + h * 78) * grow;
        const cy = y + 16 - h * H * grow;
        const px = x + Math.cos(a) * r;
        const py = cy + Math.sin(a) * r * 0.25;
        const front = Math.sin(a) > 0;
        g.lineStyle(front ? 4 : 2, 0xffffff, (front ? 0.95 : 0.4) * fade).lineBetween(px, py, px - Math.sin(a) * 22, py + Math.cos(a) * 5);
      }
    },
    onComplete: () => g.destroy(),
  });
  const dust = particles(scene, x, y + 16, 'fx-glow', { speed: { min: 60, max: 180 }, angle: { min: 180, max: 360 }, scale: { start: 1, end: 2 }, alpha: { start: 0.45, end: 0 }, tint: c2, lifespan: 800 });
  dust.explode(24);
  ring(scene, x, y + 18, c1, 90, 800, 6);
  await wait(scene, 900);
  ring(scene, x + o.dir.x * 60, y + o.dir.y * 60 + 18, c2, 60, 400, 4);
  cleanup(scene, 900, dust);
};

const wind: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const a = angleOf(o.dir);
  const lines = particles(scene, x, y, 'fx-spark', {
    emitZone: { type: 'random', source: new Phaser.Geom.Rectangle(-120, -60, 240, 120), quantity: 1 },
    speed: { min: 500, max: 800 },
    angle: (a * 180) / Math.PI + 180,
    rotate: (a * 180) / Math.PI + 90,
    scale: { start: 1.2, end: 0.6 },
    alpha: { start: 0.9, end: 0 },
    tint: [c1, c2, 0xffffff],
    lifespan: 260,
    frequency: 10,
    quantity: 2,
    emitting: true,
  });
  // arcos de viento alrededor
  const arcs = scene.add.graphics({ x, y }).setDepth(DEPTH);
  for (let i = 0; i < 3; i++) {
    arcs.lineStyle(4 - i, i ? c2 : c1, 0.8).beginPath();
    arcs.arc(0, 0, 40 + i * 18, a + Math.PI * 0.6, a + Math.PI * 1.4);
    arcs.strokePath();
  }
  scene.tweens.add({ targets: arcs, scale: 1.8, alpha: 0, duration: 600, onComplete: () => arcs.destroy() });
  await wait(scene, 600);
  lines.stop();
  cleanup(scene, 400, lines);
};

const impact: FxFn = async (scene, x, y, _o, [c1, c2]) => {
  for (let i = 0; i < 3; i++) scene.time.delayedCall(i * 90, () => ring(scene, x, y, i % 2 ? c2 : c1, 80 + i * 30, 450, 8, DEPTH));
  const sparks = particles(scene, x, y, 'fx-spark', { speed: { min: 260, max: 520 }, scale: { start: 1, end: 0 }, tint: [c1, c2, 0xffffff], lifespan: 400, rotate: { onEmit: () => Phaser.Math.Between(0, 360) } });
  sparks.explode(40);
  flash(scene, x, y, c1, 150);
  shake(scene, 120, 0.006);
  await wait(scene, 550);
  cleanup(scene, 500, sparks);
};

/** Mano gigante (Mano celestial, Mano mágica...): se alza delante del jugador. */
const hand: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const g = scene.add.graphics().setDepth(DEPTH);
  const draw = (alpha: number) => {
    g.clear();
    // dedos
    const fingers = [
      [-46, -96, 20, 70],
      [-22, -118, 21, 90],
      [2, -124, 21, 96],
      [26, -112, 20, 84],
    ];
    for (const [fx, fy, w, h] of fingers) {
      g.fillStyle(c1, 0.35 * alpha).fillRoundedRect(fx - 4, fy - 4, w + 8, h + 8, 12);
      g.fillStyle(c2, 0.9 * alpha).fillRoundedRect(fx, fy, w, h, 10);
    }
    // pulgar y palma
    g.fillStyle(c2, 0.9 * alpha).fillRoundedRect(46, -46, 22, 56, 10);
    g.fillStyle(c1, 0.35 * alpha).fillRoundedRect(-54, -40, 112, 96, 26);
    g.fillStyle(c2, 0.95 * alpha).fillRoundedRect(-50, -36, 104, 88, 24);
    g.lineStyle(3, Phaser.Display.Color.ValueToColor(c1).darken(25).color, alpha).strokeRoundedRect(-50, -36, 104, 88, 24);
    for (const [fx, fy, w, h] of fingers) g.strokeRoundedRect(fx, fy, w, h, 10);
    g.strokeRoundedRect(46, -46, 22, 56, 10);
    g.lineStyle(3, c1, alpha).strokeCircle(2, 6, 22);
  };
  draw(1);
  const hx = x + o.dir.x * 40;
  const hy = y + o.dir.y * 40 - 30;
  g.setPosition(hx, hy + 60).setScale(0.25).setAlpha(0);
  scene.tweens.add({ targets: g, y: hy, scale: 1, alpha: 1, duration: 320, ease: 'Back.out' });
  const rays = scene.add.graphics({ x: hx, y: hy }).setDepth(DEPTH - 1);
  for (let i = 0; i < 16; i++) {
    const a = (i / 16) * Math.PI * 2;
    rays.fillStyle(c1, 0.22).fillTriangle(0, 0, Math.cos(a - 0.1) * 190, Math.sin(a - 0.1) * 190, Math.cos(a + 0.1) * 190, Math.sin(a + 0.1) * 190);
  }
  rays.setScale(0.2);
  scene.tweens.add({ targets: rays, scale: 1, rotation: 0.5, duration: 900 });
  scene.tweens.add({ targets: [g, rays], alpha: 0, delay: 900, duration: 300, onComplete: () => (g.destroy(), rays.destroy()) });
  scene.time.delayedCall(300, () => {
    flash(scene, hx, hy, c1, 170);
    shake(scene, 140, 0.006);
  });
  await wait(scene, 900);
};

/** Puño gigante que sale disparado hacia el balón. */
const punch: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const a = angleOf(o.dir);
  const g = scene.add.graphics({ x, y: y - 10 }).setDepth(DEPTH).setRotation(a);
  g.fillStyle(c1, 0.4).fillRoundedRect(-40, -40, 84, 80, 22);
  g.fillStyle(c2).fillRoundedRect(-34, -34, 72, 68, 20);
  g.lineStyle(3, c1);
  for (let i = 0; i < 3; i++) g.lineBetween(20, -24 + i * 17, 36, -24 + i * 17);
  g.fillStyle(c1).fillRect(-70, -18, 38, 36);
  g.setScale(0.3);
  scene.tweens.add({ targets: g, x: x + o.dir.x * 110, y: y - 10 + o.dir.y * 110, scale: 1.3, duration: 220, ease: 'Quad.out' });
  scene.time.delayedCall(220, () => {
    ring(scene, x + o.dir.x * 130, y + o.dir.y * 130, c1, 90, 400, 8, DEPTH);
    flash(scene, x + o.dir.x * 130, y + o.dir.y * 130, c2, 130);
    shake(scene, 160, 0.008);
  });
  scene.tweens.add({ targets: g, alpha: 0, delay: 650, duration: 250, onComplete: () => g.destroy() });
  await wait(scene, 800);
};

/** Muro que sale del suelo (El muro, Muro de hierro...). */
const wall: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const perp = { x: -o.dir.y, y: o.dir.x };
  const cx = x + o.dir.x * 46;
  const cy = y + o.dir.y * 46;
  const blocks: Phaser.GameObjects.Graphics[] = [];
  for (let col = -3; col <= 3; col++) {
    for (let row = 0; row < 3; row++) {
      const bx = cx + perp.x * col * 28;
      const by = cy + perp.y * col * 28 + 18;
      const b = scene.add.graphics({ x: bx, y: by + 40 }).setDepth(by + 30);
      b.fillStyle(row % 2 ? c1 : Phaser.Display.Color.ValueToColor(c1).darken(15).color).fillRect(-14, -26, 28, 26);
      b.lineStyle(2, 0x000000, 0.35).strokeRect(-14, -26, 28, 26);
      b.fillStyle(c2, 0.4).fillRect(-14, -26, 28, 5);
      b.setAlpha(0);
      scene.tweens.add({ targets: b, y: by - row * 26, alpha: 1, duration: 260, delay: (Math.abs(col) + row) * 40, ease: 'Back.out' });
      blocks.push(b);
    }
  }
  const dust = particles(scene, cx, cy + 18, 'fx-glow', { speed: { min: 40, max: 160 }, angle: { min: 180, max: 360 }, scale: { start: 1.2, end: 2.4 }, alpha: { start: 0.5, end: 0 }, tint: c2, lifespan: 800, blendMode: 'NORMAL' });
  dust.explode(24);
  shake(scene, 260, 0.008);
  await wait(scene, 850);
  blocks.forEach((b, i) => scene.tweens.add({ targets: b, alpha: 0, y: b.y + 30, duration: 300, delay: i * 8, onComplete: () => b.destroy() }));
  cleanup(scene, 600, dust);
};

/** Escudo o red de energía en forma de panal. */
const shield: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const g = scene.add.graphics({ x: x + o.dir.x * 30, y: y + o.dir.y * 30 - 10 }).setDepth(DEPTH);
  const hexR = 16;
  for (let q = -4; q <= 4; q++) {
    for (let r = -3; r <= 3; r++) {
      const hx = q * hexR * 1.5;
      const hy = (r + (q % 2 ? 0.5 : 0)) * hexR * 1.73;
      if (hx * hx + hy * hy * 1.4 > 80 * 80) continue;
      const pts = Array.from({ length: 6 }, (_, i) => new Phaser.Geom.Point(hx + Math.cos((i * Math.PI) / 3) * hexR * 0.92, hy + Math.sin((i * Math.PI) / 3) * hexR * 0.92));
      g.fillStyle(c1, 0.18).fillPoints(pts, true);
      g.lineStyle(2, c2, 0.85).strokePoints(pts, true);
    }
  }
  g.setScale(0.1).setAlpha(0);
  scene.tweens.add({ targets: g, scale: 1, alpha: 1, duration: 280, ease: 'Back.out' });
  scene.tweens.add({ targets: g, alpha: 0.5, duration: 120, yoyo: true, repeat: 2, delay: 300 });
  scene.tweens.add({ targets: g, alpha: 0, scale: 1.2, delay: 900, duration: 250, onComplete: () => g.destroy() });
  ring(scene, x, y + 18, c1, 90, 600, 5);
  await wait(scene, 900);
};

/** Espada de luz que aparece y corta en arco. */
const sword: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const a = angleOf(o.dir);
  const blade = scene.add.graphics({ x, y: y - 20 }).setDepth(DEPTH);
  blade.fillStyle(c1, 0.35).fillTriangle(-10, 0, 10, 0, 0, -170);
  blade.fillStyle(c2).fillTriangle(-5, 0, 5, 0, 0, -160);
  blade.fillStyle(c1).fillRect(-22, -2, 44, 8).fillRect(-4, 6, 8, 22);
  blade.setRotation(a - Math.PI * 0.2).setScale(0.2);
  scene.tweens.add({ targets: blade, scale: 1, duration: 200, ease: 'Back.out' });
  scene.tweens.add({ targets: blade, rotation: a + Math.PI * 1.1, duration: 300, delay: 280, ease: 'Cubic.inOut' });
  // estela del corte
  scene.time.delayedCall(330, () => {
    const slash = scene.add.graphics({ x, y: y - 20 }).setDepth(DEPTH);
    slash.lineStyle(26, c1, 0.35).beginPath().arc(0, 0, 130, a - Math.PI * 0.6, a + Math.PI * 0.7).strokePath();
    slash.lineStyle(8, 0xffffff, 0.95).beginPath().arc(0, 0, 130, a - Math.PI * 0.6, a + Math.PI * 0.7).strokePath();
    scene.tweens.add({ targets: slash, alpha: 0, scale: 1.15, duration: 380, onComplete: () => slash.destroy() });
    flash(scene, x + o.dir.x * 80, y + o.dir.y * 80, c2, 120);
    shake(scene, 120, 0.006);
  });
  const sparks = particles(scene, x, y - 20, 'fx-spark', { speed: { min: 200, max: 420 }, scale: { start: 0.8, end: 0 }, tint: [c1, c2], lifespan: 380 });
  scene.time.delayedCall(360, () => sparks.explode(28));
  scene.tweens.add({ targets: blade, alpha: 0, delay: 700, duration: 200, onComplete: () => blade.destroy() });
  await wait(scene, 850);
  cleanup(scene, 500, sparks);
};

/** Cuerpo de dragón que serpentea y se lanza hacia delante. */
const dragon: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const n = 18;
  const segs: Phaser.GameObjects.Graphics[] = [];
  for (let i = 0; i < n; i++) {
    const r = 22 - i * 0.9;
    const s = scene.add.graphics().setDepth(DEPTH + (n - i));
    s.fillStyle(c1, 0.45).fillCircle(0, 0, r + 6);
    s.fillStyle(i % 2 ? c2 : c1, 0.95).fillCircle(0, 0, r);
    s.fillStyle(0xffffff, 0.5).fillCircle(-r * 0.3, -r * 0.3, r * 0.3);
    segs.push(s);
  }
  // cabeza con cuernos y ojos
  const head = scene.add.graphics().setDepth(DEPTH + n + 1);
  head.fillStyle(c1).fillEllipse(0, 0, 54, 38);
  head.fillStyle(c2).fillTriangle(-14, -16, -30, -38, -4, -18).fillTriangle(14, -16, 30, -38, 4, -18);
  head.fillStyle(0xffffff).fillEllipse(-11, -4, 10, 6).fillEllipse(11, -4, 10, 6);
  head.fillStyle(0xff2a2a).fillCircle(-11, -4, 2.5).fillCircle(11, -4, 2.5);
  head.fillStyle(0xffffff).fillTriangle(-12, 12, -6, 20, 0, 12).fillTriangle(0, 12, 6, 20, 12, 12);
  const perp = { x: -o.dir.y, y: o.dir.x };
  const path = (t: number) => {
    // nace del suelo detrás del jugador, sube en espiral y sale disparado hacia delante
    const along = -60 + t * 360;
    const wave = Math.sin(t * Math.PI * 3) * 60 * (1 - t * 0.6);
    return { x: x + o.dir.x * along + perp.x * wave, y: y - 40 - Math.sin(t * Math.PI) * 90 + o.dir.y * along + perp.y * wave };
  };
  const s = { t: 0 };
  scene.tweens.add({
    targets: s,
    t: 1,
    duration: 1000,
    ease: 'Sine.inOut',
    onUpdate: () => {
      const hp = path(s.t);
      const prev = path(Math.max(0, s.t - 0.02));
      head.setPosition(hp.x, hp.y).setRotation(Math.atan2(hp.y - prev.y, hp.x - prev.x) + Math.PI / 2);
      segs.forEach((g, i) => {
        const p = path(Math.max(0, s.t - (i + 1) * 0.025));
        g.setPosition(p.x, p.y).setAlpha(s.t - (i + 1) * 0.025 > 0 ? 1 - s.t * 0.4 : 0);
      });
    },
    onComplete: () => {
      const end = path(1);
      flash(scene, end.x, end.y, c2, 160);
      [...segs, head].forEach((g) => scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() }));
    },
  });
  const scales = particles(scene, x, y, 'fx-glow', { speed: { min: 20, max: 80 }, scale: { start: 0.7, end: 0 }, tint: [c1, c2], lifespan: 500, frequency: 20, emitting: true });
  scales.startFollow(head);
  shake(scene, 200, 0.004);
  await wait(scene, 1050);
  scales.stop();
  cleanup(scene, 600, scales);
};

/** Ave enorme (fénix, águila, pegaso...) que bate las alas y vuela hacia delante. */
const bird: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const b = scene.add.container(x, y - 60).setDepth(DEPTH);
  const wings = [-1, 1].map((side) => {
    const w = scene.add.graphics();
    w.fillStyle(c1, 0.5).fillTriangle(0, 0, side * 130, -70, side * 110, 20);
    w.fillStyle(c2, 0.9).fillTriangle(0, 0, side * 120, -60, side * 90, 10);
    for (let i = 0; i < 4; i++) w.fillStyle(c1, 0.8).fillTriangle(side * (40 + i * 22), 4, side * (60 + i * 22), 30 + i * 4, side * (50 + i * 22), 2);
    return w;
  });
  const body = scene.add.graphics();
  body.fillStyle(c2).fillEllipse(0, 0, 30, 56);
  body.fillStyle(c1).fillTriangle(-12, 22, 12, 22, 0, 70);
  body.fillStyle(c2).fillCircle(0, -32, 14);
  body.fillStyle(0xffc020).fillTriangle(-5, -40, 5, -40, 0, -58);
  b.add([...wings, body]);
  b.setRotation(angleOf(o.dir) + Math.PI / 2).setScale(0.2).setAlpha(0);
  scene.tweens.add({ targets: b, scale: 1, alpha: 1, duration: 260, ease: 'Back.out' });
  scene.tweens.add({ targets: wings, scaleY: 0.35, duration: 150, yoyo: true, repeat: 3, delay: 150 });
  scene.tweens.add({ targets: b, x: x + o.dir.x * 260, y: y - 60 + o.dir.y * 260, alpha: 0, delay: 500, duration: 500, ease: 'Quad.in', onComplete: () => b.destroy() });
  const feathers = particles(scene, x, y - 60, 'fx-feather', { speed: { min: 60, max: 200 }, scale: { start: 1, end: 0.4 }, alpha: { start: 1, end: 0 }, tint: [c1, c2], lifespan: 1000, rotate: { min: 0, max: 360 }, gravityY: 80 });
  feathers.explode(24);
  flash(scene, x, y - 60, c2, 140);
  await wait(scene, 1000);
  cleanup(scene, 800, feathers);
};

/** Bestia: rugido (onda), ojos que brillan y tres zarpazos. */
const beast: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const eyes = scene.add.graphics({ x, y: y - 80 }).setDepth(DEPTH);
  eyes.fillStyle(c2).fillTriangle(-40, -6, -10, -12, -16, 6).fillTriangle(40, -6, 10, -12, 16, 6);
  eyes.setAlpha(0).setScale(0.6);
  scene.tweens.add({ targets: eyes, alpha: 1, scale: 1.3, duration: 220, yoyo: true, hold: 300, onComplete: () => eyes.destroy() });
  for (let i = 0; i < 3; i++) scene.time.delayedCall(80 + i * 60, () => ring(scene, x, y - 20, c1, 100 + i * 30, 420, 7, DEPTH));
  scene.time.delayedCall(380, () => {
    const a = angleOf(o.dir);
    const claws = scene.add.graphics({ x: x + o.dir.x * 70, y: y - 10 + o.dir.y * 70 }).setDepth(DEPTH).setRotation(a);
    for (let i = -1; i <= 1; i++) {
      claws.lineStyle(10, c1, 0.5).lineBetween(-50, i * 22 - 30, 50, i * 22 + 30);
      claws.lineStyle(4, 0xffffff).lineBetween(-50, i * 22 - 30, 50, i * 22 + 30);
    }
    scene.tweens.add({ targets: claws, alpha: 0, scale: 1.2, duration: 350, onComplete: () => claws.destroy() });
    shake(scene, 160, 0.008);
  });
  await wait(scene, 800);
};

/** Pingüinos que salen del suelo y vuelan con el balón (Pingüino emperador). */
const penguin: FxFn = async (scene, x, y, o) => {
  const birds: Phaser.GameObjects.Image[] = [];
  for (let i = 0; i < 6; i++) {
    const a = (i / 6) * Math.PI * 2;
    const px = x + Math.cos(a) * 46;
    const py = y + 14 + Math.sin(a) * 20;
    const p = scene.add.image(px, py + 20, 'fx-penguin').setDepth(DEPTH).setScale(0).setOrigin(0.5, 1);
    scene.tweens.add({ targets: p, y: py, scale: 1.5, duration: 260, delay: i * 50, ease: 'Back.out' });
    birds.push(p);
  }
  ring(scene, x, y + 18, 0x3a6aff, 80, 500, 6);
  await wait(scene, 600);
  birds.forEach((p, i) => {
    const off = (i - 2.5) * 14;
    scene.tweens.add({
      targets: p,
      x: x + o.dir.x * 300 - o.dir.y * off,
      y: y + o.dir.y * 300 + o.dir.x * off,
      angle: (angleOf(o.dir) * 180) / Math.PI + 90,
      duration: 420,
      delay: i * 30,
      ease: 'Quad.in',
      onComplete: () => p.destroy(),
    });
  });
  await wait(scene, 450);
};

/** Imágenes repetidas del jugador que se abren en abanico y vuelven (ilusiones, fintas). */
const clone: FxFn = async (scene, x, y, o, [c1, c2]) => {
  const copies: Phaser.GameObjects.Image[] = [];
  if (o.texture) {
    for (let i = 0; i < 5; i++) {
      const c = scene.add.image(x, y, o.texture).setScale(o.scale ?? 1).setTint(i % 2 ? c1 : c2).setAlpha(0.6).setDepth(DEPTH);
      const a = ((i - 2) / 2) * 1.2 + angleOf(o.dir) + Math.PI / 2;
      scene.tweens.add({ targets: c, x: x + Math.cos(a) * 70, y: y + Math.sin(a) * 40, duration: 260, yoyo: true, hold: 260, ease: 'Sine.out', onComplete: () => c.destroy() });
      copies.push(c);
    }
  }
  const glitter = particles(scene, x, y, 'fx-star', { speed: { min: 40, max: 160 }, scale: { start: 0.7, end: 0 }, tint: [c1, c2], lifespan: 700 });
  glitter.explode(24);
  ring(scene, x, y + 18, c1, 70, 600, 4);
  await wait(scene, 800);
  cleanup(scene, 500, glitter);
};

const EFFECTS: Record<FxName, FxFn> = {
  penguin,
  dragon,
  bird,
  beast,
  hand,
  punch,
  wall,
  shield,
  sword,
  meteor,
  tornado,
  ice,
  fire,
  lightning,
  water,
  flower,
  earth,
  dark,
  light,
  clone,
  wind,
  impact,
};

const baseOf = (name: string) => name.split(':')[0];

function lookup(name: string): FxFn {
  return SHAPES[name] ?? SHAPES[baseOf(name)] ?? EFFECTS[baseOf(name) as FxName] ?? impact;
}

/** Paleta de una técnica: los colores de su vídeo, completados con los de su forma o su afinidad. */
/** Elementos con su color natural: aquí el color del vídeo (gradas, cielo...) despista más que ayuda. */
const NATURAL = new Set(['fire', 'ice', 'water', 'earth', 'lightning']);

export function fxPalette(recipe: FxRecipe, element: Element): number[] {
  const base = colors(baseOf(recipe.fx) as FxName, element);
  if (NATURAL.has(baseOf(recipe.fx))) return [...base, lighten(base[base.length - 1], 30)];
  // del más vivo al más apagado: el primero es el color principal del efecto
  const vivid = (c: number) => {
    const { s: sat, v } = Phaser.Display.Color.RGBToHSV((c >> 16) & 255, (c >> 8) & 255, c & 255) as { s: number; v: number };
    return sat * v;
  };
  const own = (recipe.colors ?? []).map((c) => parseInt(c.slice(1), 16)).sort((a, b) => vivid(b) - vivid(a));
  // los colores muy oscuros no se ven sobre el césped
  const pal = (own.length ? own : base).map((c) => {
    const { v } = Phaser.Display.Color.RGBToHSV((c >> 16) & 255, (c >> 8) & 255, c & 255) as { v: number };
    return v < 0.55 ? lighten(c, 30) : c;
  });
  while (pal.length < 3) pal.push(Phaser.Display.Color.ValueToColor(pal[pal.length - 1]).lighten(30).color);
  return pal;
}

/** Reproduce el efecto de una supertécnica en (x, y) del mundo. Se resuelve cuando ha terminado lo principal. */
export async function playFx(scene: Phaser.Scene, recipe: FxRecipe, x: number, y: number, o: FxOptions): Promise<void> {
  const pal = fxPalette(recipe, o.element);
  const run = (name: string) => lookup(name)(scene, x, y, o, pal, name.split(':')[1] ?? '');
  techSfx(recipe.fx);
  (recipe.layers ?? []).forEach((l, i) => techSfx(l, 0.12 + i * 0.14));
  const extras = (recipe.layers ?? []).map((l, i) => new Promise<void>((r) => scene.time.delayedCall(120 + i * 140, () => run(l).then(r))));
  await Promise.all([run(recipe.fx), ...extras]);
}

/** La técnica ha perdido: lo que quedaba de ella salta en pedazos. */
export function fxBreak(scene: Phaser.Scene, recipe: FxRecipe, x: number, y: number, element: Element): void {
  const [c1, c2] = fxPalette(recipe, element);
  sfx.shatter();
  const shards = particles(scene, x, y, 'fx-shard', { speed: { min: 120, max: 340 }, scale: { start: 1, end: 0.2 }, alpha: { start: 1, end: 0 }, tint: [c1, c2, 0x9aa4b4], lifespan: 700, rotate: { min: 0, max: 360 }, gravityY: 500, blendMode: 'NORMAL' });
  shards.explode(28);
  const crack = scene.add.graphics({ x, y }).setDepth(DEPTH);
  crack.lineStyle(3, 0xffffff, 0.9);
  for (let i = 0; i < 6; i++) {
    const a = (i / 6) * Math.PI * 2 + 0.3;
    crack.lineBetween(0, 0, Math.cos(a) * 30, Math.sin(a) * 30).lineBetween(Math.cos(a) * 30, Math.sin(a) * 30, Math.cos(a + 0.4) * 50, Math.sin(a + 0.4) * 50);
  }
  scene.tweens.add({ targets: crack, alpha: 0, duration: 450, onComplete: () => crack.destroy() });
  cleanup(scene, 900, shards);
}

/** Estela que sigue al balón de un tiro con supertécnica. Devuelve cómo pararla. */
export function fxTrail(scene: Phaser.Scene, recipe: FxRecipe, target: Phaser.GameObjects.Components.Transform, element: Element): () => void {
  const [c1, c2] = fxPalette(recipe, element);
  const { key: tex, additive } = fxParticle(recipe);
  const normal = !additive;
  const trail = particles(scene, 0, 0, tex, {
    speed: { min: 10, max: 60 },
    scale: { start: tex === 'fx-glow' ? 1.6 : tex === 'fx-penguin' ? 1.1 : 1, end: 0.1 },
    alpha: { start: 0.95, end: 0 },
    tint: tex === 'fx-penguin' ? 0xffffff : [c1, c2],
    lifespan: tex === 'fx-penguin' ? 500 : 380,
    frequency: tex === 'fx-penguin' ? 70 : 14,
    quantity: tex === 'fx-penguin' ? 1 : 2,
    rotate: { min: 0, max: 360 },
    blendMode: normal ? 'NORMAL' : 'ADD',
    emitting: true,
  });
  const core = particles(scene, 0, 0, 'fx-glow', { scale: { start: 1.3, end: 0 }, tint: c2, lifespan: 220, frequency: 16, emitting: true });
  trail.startFollow(target);
  core.startFollow(target);
  return () => {
    trail.stop();
    core.stop();
    cleanup(scene, 700, trail, core);
  };
}
