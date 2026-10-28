import Phaser from 'phaser';
import type { FxFn, FxOptions } from './fx';
import {
  DEPTH,
  GROUND,
  type Dir,
  type Part,
  angleOf,
  animate,
  beam,
  cleanup,
  darken,
  drawFigure,
  flash,
  lighten,
  particles,
  pt,
  puff,
  rays,
  ring,
  screenFlash,
  shake,
  speedLines,
  summon,
  wait,
} from './fxkit';

/**
 * Formas y variantes de los efectos de las supertécnicas, sacadas de sus vídeos en la enciclopedia
 * oficial (zukan.inazuma.jp). Cada una recibe la paleta de su técnica (`c`, colores del vídeo) y la
 * variante (`v`). Las que no están aquí usan los efectos básicos de fx.ts.
 */

type Ctx = { scene: Phaser.Scene; x: number; y: number; o: FxOptions; c: number[]; v: string };
const fx = (fn: (k: Ctx) => Promise<void>): FxFn => (scene, x, y, o, c, v) => fn({ scene, x, y, o, c, v });

/** Punto a `d` píxeles por delante del jugador. */
const ahead = (k: Ctx, d: number, lift = 0) => ({ x: k.x + k.o.dir.x * d, y: k.y + k.o.dir.y * d - lift });
const perp = (d: Dir): Dir => ({ x: -d.y, y: d.x });
const DEG = 180 / Math.PI;

// ================================================================ siluetas

/** Mano abierta, dedos hacia arriba. */
function handParts(skin: number, line: number): Part[] {
  const f: Part[] = [];
  const fingers = [
    [-46, -150, 20, 72],
    [-22, -172, 21, 92],
    [2, -178, 21, 98],
    [26, -164, 20, 86],
  ];
  for (const [x, y, w, h] of fingers) f.push(['R', x - 4, y - 4, w + 8, h + 8, 12, line], ['R', x, y, w, h, 10, skin]);
  f.push(['R', 44, -100, 26, 60, 12, line], ['R', 48, -96, 20, 52, 10, skin]);
  f.push(['R', -54, -96, 112, 100, 28, line], ['R', -50, -92, 104, 92, 26, skin]);
  f.push(['l', line, 3, -20, -40, 0, -24, 22, -42]);
  return f;
}

/** Puño cerrado mirando hacia arriba. */
function fistParts(skin: number, line: number): Part[] {
  return [
    ['R', -46, -96, 92, 96, 26, line],
    ['R', -42, -92, 84, 88, 24, skin],
    ['l', line, 3, -26, -92, -26, -62],
    ['l', line, 3, -6, -92, -6, -62],
    ['l', line, 3, 14, -92, 14, -62],
    ['R', -50, -60, 30, 40, 12, skin],
    ['r', -30, 0, 60, 30, line],
  ];
}

/** Majin (Mano mágica): torso musculoso con el pelo en llamas. */
function majinParts(body: number, hair: number): Part[] {
  return [
    ['p', hair, -60, -250, -40, -320, -20, -270, 0, -340, 20, -270, 40, -320, 60, -250],
    ['e', 0, -240, 90, 80, body],
    ['c', -18, -246, 7, 0xffffff],
    ['c', 18, -246, 7, 0xffffff],
    ['c', -18, -246, 3, 0x000000],
    ['c', 18, -246, 3, 0x000000],
    ['p', body, -110, -200, 110, -200, 80, -60, -80, -60],
    ['e', -120, -170, 80, 70, body],
    ['e', 120, -170, 80, 70, body],
    ['e', -150, -110, 50, 90, body],
    ['e', 150, -110, 50, 90, body],
    ['l', darken(body, 30), 3, -40, -160, 0, -140, 40, -160],
    ['l', darken(body, 30), 3, -30, -120, -30, -80],
    ['l', darken(body, 30), 3, 30, -120, 30, -80],
  ];
}

function birdParts(body: number, wing: number, tail: number, kind: string): Part[] {
  const p: Part[] = [];
  // alas desplegadas
  p.push(['p', wing, 0, -60, -170, -150, -200, -90, -120, -60, -150, -30, -60, -30]);
  p.push(['p', wing, 0, -60, 170, -150, 200, -90, 120, -60, 150, -30, 60, -30]);
  p.push(['p', lighten(wing, 25), -10, -60, -150, -130, -110, -70]);
  p.push(['p', lighten(wing, 25), 10, -60, 150, -130, 110, -70]);
  // cola
  if (kind === 'phoenix' || kind === 'fire' || kind === 'darkphoenix') {
    p.push(['p', tail, -20, -20, -60, 70, -10, 30, 0, 90, 10, 30, 60, 70, 20, -20]);
  } else p.push(['p', tail, -22, -20, -30, 30, 0, 18, 30, 30, 22, -20]);
  p.push(['e', 0, -40, 44, 80, body]);
  p.push(['c', 0, -88, 22, body]);
  p.push(['p', 0xffb020, -8, -96, 8, -96, 0, -120]);
  p.push(['c', -8, -92, 4, 0xffffff], ['c', 8, -92, 4, 0xffffff]);
  return p;
}

/** Caballo con alas (pegaso) o con cuerno (unicornio). */
function horseParts(body: number, mane: number, horn: boolean): Part[] {
  const p: Part[] = [
    ['e', 0, -70, 150, 70, body],
    ['p', body, 50, -90, 90, -160, 120, -150, 90, -80],
    ['e', 110, -160, 56, 36, body],
    ['p', mane, 60, -100, 80, -170, 100, -170, 70, -90],
    ['r', -60, -50, 14, 50, body],
    ['r', -30, -50, 14, 50, body],
    ['r', 30, -50, 14, 50, body],
    ['r', 56, -50, 14, 50, body],
    ['p', mane, -75, -80, -130, -40, -110, -90],
    ['c', 118, -166, 4, 0x000000],
  ];
  if (horn) p.push(['p', 0xfff0a0, 108, -176, 118, -176, 140, -230]);
  else p.push(['p', mane, -20, -100, -120, -190, -60, -110], ['p', mane, 20, -100, -40, -200, 10, -110]);
  return p;
}

function beastHeadParts(fur: number, dark: number, kind: string): Part[] {
  const p: Part[] = [];
  if (kind === 'wolf') {
    p.push(['p', fur, -60, -40, -80, -170, -40, -120, 0, -150, 40, -120, 80, -170, 60, -40]);
    p.push(['p', lighten(fur, 30), -30, -40, 0, 20, 30, -40, 0, -70]);
  } else {
    // tigre
    p.push(['e', 0, -80, 170, 150, fur]);
    p.push(['p', fur, -70, -130, -60, -180, -30, -140], ['p', fur, 70, -130, 60, -180, 30, -140]);
    for (const s of [-1, 1]) {
      p.push(['l', dark, 6, s * 80, -100, s * 50, -90]);
      p.push(['l', dark, 6, s * 84, -70, s * 50, -66]);
      p.push(['l', dark, 6, s * 30, -150, s * 22, -120]);
    }
    p.push(['e', 0, -40, 90, 60, lighten(fur, 40)]);
  }
  p.push(['p', 0xffe040, -40, -100, -14, -96, -22, -84], ['p', 0xffe040, 40, -100, 14, -96, 22, -84]);
  // boca abierta con colmillos
  p.push(['e', 0, -30, 70, 44, 0x400010]);
  p.push(['p', 0xffffff, -26, -46, -18, -46, -22, -24], ['p', 0xffffff, 26, -46, 18, -46, 22, -24]);
  p.push(['p', 0xffffff, -20, -12, -12, -12, -16, -30], ['p', 0xffffff, 20, -12, 12, -12, 16, -30]);
  return p;
}

// ================================================================ fuego

const fireBreath = fx(async (k) => {
  const a = angleOf(k.o.dir) * DEG;
  const e = particles(k.scene, k.x, k.y - 10, 'fx-flame', {
    speed: { min: 380, max: 620 },
    angle: { min: a - 14, max: a + 14 },
    scale: { start: 0.8, end: 3 },
    alpha: { start: 1, end: 0 },
    tint: [k.c[1], k.c[0], 0xffffff],
    lifespan: 520,
    frequency: 8,
    quantity: 4,
    emitting: true,
  });
  await wait(k.scene, 650);
  e.stop();
  cleanup(k.scene, 700, e);
});

const fireBurst = fx(async (k) => {
  rays(k.scene, k.x, k.y - 10, [k.c[0], k.c[1], 0xffffff], 18, 190);
  puff(k.scene, k.x, k.y, 'fx-flame', 50, { speed: { min: 200, max: 420 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 600 });
  flash(k.scene, k.x, k.y, k.c[1], 160);
  shake(k.scene, 140, 0.006);
  await wait(k.scene, 600);
});

/** Bola de fuego enorme que sale disparada (cometa, Bomba acrobática...). */
const fireComet = fx(async (k) => {
  const ball = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH);
  ball.fillStyle(0xff2a00, 0.45).fillCircle(0, 0, 34).fillStyle(0xff7a1a, 0.9).fillCircle(0, 0, 26).fillStyle(0xffd23f).fillCircle(0, 0, 17).fillStyle(0xfff6d0).fillCircle(0, 0, 9);
  ball.setScale(0.3);
  k.scene.tweens.add({ targets: ball, scale: 1.3, duration: 300, ease: 'Back.out' });
  const tail = particles(k.scene, k.x, k.y - 20, 'fx-flame', { speed: { min: 20, max: 80 }, scale: { start: 2.6, end: 0.2 }, alpha: { start: 1, end: 0 }, tint: [0xff5a1a, 0xffd23f, 0xff2a00], lifespan: 450, frequency: 10, quantity: 3, emitting: true });
  tail.startFollow(ball);
  flash(k.scene, k.x, k.y - 20, 0xff7a1a, 140);
  await wait(k.scene, 300);
  const to = ahead(k, 320, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: ball, x: to.x, y: to.y, scale: 1.8, duration: 520, ease: 'Quad.in', onComplete: () => r() }));
  tail.stop();
  ball.destroy();
  cleanup(k.scene, 600, tail);
});

const fireDash = fx(async (k) => {
  const done = speedLines(k.scene, k.x, k.y, k.o.dir, [k.c[0], k.c[1]], 650);
  const e = particles(k.scene, k.x, k.y, 'fx-flame', { speed: { min: 40, max: 120 }, angle: { min: angleOf(k.o.dir) * DEG + 160, max: angleOf(k.o.dir) * DEG + 200 }, scale: { start: 2.2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 500, frequency: 10, quantity: 3, emitting: true });
  const s = { t: 0 };
  k.scene.tweens.add({ targets: s, t: 1, duration: 650, onUpdate: () => e.setPosition(k.x + k.o.dir.x * 160 * s.t, k.y + k.o.dir.y * 160 * s.t) });
  await done;
  e.stop();
  cleanup(k.scene, 600, e);
});

const fireExplosion = fx(async (k) => {
  const at = ahead(k, 40);
  screenFlash(k.scene, k.c[1], 120);
  flash(k.scene, at.x, at.y, 0xffffff, 220, 400);
  puff(k.scene, at.x, at.y, 'fx-flame', 70, { speed: { min: 150, max: 460 }, scale: { start: 3, end: 0.4 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1], 0xff2a00], lifespan: 750 });
  puff(k.scene, at.x, at.y, 'fx-glow', 24, { speed: { min: 30, max: 120 }, scale: { start: 2.5, end: 4 }, alpha: { start: 0.5, end: 0 }, tint: 0x555555, lifespan: 1100 });
  ring(k.scene, at.x, at.y + 16, k.c[0], 140, 600, 10);
  shake(k.scene, 300, 0.014);
  await wait(k.scene, 750);
});

const fireGeyser = fx(async (k) => {
  for (let i = 0; i < 3; i++) {
    const at = ahead(k, 50 + i * 60);
    const side = perp(k.o.dir);
    const px = at.x + side.x * (i - 1) * 36;
    const py = at.y + side.y * (i - 1) * 36;
    k.scene.time.delayedCall(i * 120, () => {
      ring(k.scene, px, py + 10, k.c[0], 40, 400, 5);
      puff(k.scene, px, py, 'fx-flame', 40, { speedY: { min: -520, max: -300 }, speedX: { min: -40, max: 40 }, scale: { start: 2.2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[1], k.c[0]], lifespan: 650 });
    });
  }
  await wait(k.scene, 900);
});

const fireHands = fx(async (k) => {
  const side = perp(k.o.dir);
  const balls = [-1, 1].map((s) => k.scene.add.image(k.x + side.x * 50 * s, k.y - 30 + side.y * 50 * s, 'fx-glow').setTint(k.c[0]).setScale(0.5).setDepth(DEPTH).setBlendMode('ADD'));
  const flames = balls.map((b) => {
    const e = particles(k.scene, b.x, b.y, 'fx-flame', { speedY: { min: -160, max: -60 }, scale: { start: 1.6, end: 0.2 }, tint: [k.c[0], k.c[1]], lifespan: 420, frequency: 20, quantity: 2, emitting: true });
    e.startFollow(b);
    return e;
  });
  k.scene.tweens.add({ targets: balls, scale: 2.2, duration: 380 });
  await wait(k.scene, 400);
  const to = ahead(k, 40, 30);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: balls, x: to.x, y: to.y, duration: 220, ease: 'Quad.in', onComplete: () => r() }));
  flames.forEach((e) => e.stop());
  balls.forEach((b) => b.destroy());
  flash(k.scene, to.x, to.y, k.c[1], 170);
  puff(k.scene, to.x, to.y, 'fx-flame', 40, { speed: { min: 150, max: 360 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 550 });
  cleanup(k.scene, 600, ...flames);
  await wait(k.scene, 350);
});

/** Espiral de llamas que envuelve el balón y sube (Tornado de fuego, Torbellino de fuego...). */
const fireSpin = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const e = particles(k.scene, k.x, k.y, 'fx-flame', { speed: { min: 10, max: 40 }, scale: { start: 1.8, end: 0.2 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 380, frequency: 12, quantity: 2, emitting: true });
  await animate(k.scene, 900, (t) => {
    g.clear();
    for (let arm = 0; arm < 2; arm++) {
      g.lineStyle(12, arm ? k.c[1] : k.c[0], 0.85 * (1 - t * 0.6)).beginPath();
      for (let s = 0; s <= 1; s += 0.04) {
        const a = arm * Math.PI + s * Math.PI * 4 + t * Math.PI * 6;
        const r = 30 + s * 40;
        const px = k.x + Math.cos(a) * r;
        const py = k.y + 10 - s * 170 * Math.min(1, t * 2) + Math.sin(a) * r * 0.3;
        if (s === 0) g.moveTo(px, py);
        else g.lineTo(px, py);
      }
      g.strokePath();
    }
    const a = t * Math.PI * 8;
    e.setPosition(k.x + Math.cos(a) * 50, k.y - t * 150 + Math.sin(a) * 15);
  });
  g.destroy();
  e.stop();
  cleanup(k.scene, 500, e);
  flash(k.scene, k.x, k.y - 150, k.c[1], 150);
});

/** Remolino de fuego en el suelo (Dúo magma, Baile de llamas). */
const fireSwirl = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y + 14 }).setDepth(GROUND);
  await animate(k.scene, 850, (t) => {
    g.clear();
    for (let arm = 0; arm < 4; arm++) {
      g.lineStyle(14 * (1 - t * 0.5), arm % 2 ? k.c[1] : k.c[0], 0.8 * (t > 0.7 ? (1 - t) / 0.3 : 1)).beginPath();
      for (let s = 0; s <= 1; s += 0.05) {
        const a = arm * (Math.PI / 2) + s * Math.PI * 1.6 + t * Math.PI * 3;
        const r = 10 + s * 110 * Math.min(1, t * 2.5);
        if (s === 0) g.moveTo(Math.cos(a) * r, Math.sin(a) * r * 0.5);
        else g.lineTo(Math.cos(a) * r, Math.sin(a) * r * 0.5);
      }
      g.strokePath();
    }
  });
  g.destroy();
  puff(k.scene, k.x, k.y, 'fx-flame', 30, { speedY: { min: -300, max: -120 }, speedX: { min: -120, max: 120 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 600 });
});

/** Gran tormenta de fuego (Tormenta de fuego, Fuego total): pilar enorme y remolino. */
const fireStorm = fx(async (k) => {
  void fireSwirl(k.scene, k.x, k.y, k.o, k.c, '');
  const e = particles(k.scene, k.x, k.y + 10, 'fx-flame', { speedY: { min: -600, max: -320 }, speedX: { min: -90, max: 90 }, scale: { start: 3.4, end: 0.4 }, alpha: { start: 1, end: 0 }, tint: [k.c[1], k.c[0], 0xff2a00], lifespan: 800, frequency: 6, quantity: 5, emitting: true });
  flash(k.scene, k.x, k.y - 40, k.c[1], 200, 500);
  shake(k.scene, 400, 0.008);
  await wait(k.scene, 900);
  e.stop();
  cleanup(k.scene, 900, e);
});

const fireTrail = fx(async (k) => {
  for (let i = 0; i < 8; i++) {
    const at = ahead(k, 20 + i * 30);
    k.scene.time.delayedCall(i * 60, () => puff(k.scene, at.x, at.y + 10, 'fx-flame', 10, { speedY: { min: -240, max: -100 }, speedX: { min: -30, max: 30 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 550 }));
  }
  await wait(k.scene, 800);
});

const fireZigzag = fx(async (k) => {
  const side = perp(k.o.dir);
  for (let i = 0; i < 8; i++) {
    const at = ahead(k, 20 + i * 30);
    const s = (i % 2 ? 1 : -1) * 40;
    k.scene.time.delayedCall(i * 60, () => puff(k.scene, at.x + side.x * s, at.y + side.y * s + 10, 'fx-flame', 10, { speedY: { min: -260, max: -100 }, speedX: { min: -30, max: 30 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 550 }));
  }
  await wait(k.scene, 700);
  await fireExplosion(k.scene, k.x + k.o.dir.x * 200, k.y + k.o.dir.y * 200, k.o, k.c, '');
});

/** Sol enorme (Llamarada atómica, Llamarada infernal). */
const sun = fx(async (k) => {
  const at = ahead(k, 20, 90);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  g.fillStyle(k.c[0], 0.35).fillCircle(0, 0, 90);
  g.fillStyle(k.c[1] ?? k.c[0], 0.7).fillCircle(0, 0, 70);
  g.fillStyle(0xfff4c0).fillCircle(0, 0, 52);
  for (let i = 0; i < 16; i++) {
    const a = (i / 16) * Math.PI * 2;
    g.fillStyle(k.c[0], 0.7).fillTriangle(Math.cos(a - 0.15) * 70, Math.sin(a - 0.15) * 70, Math.cos(a + 0.15) * 70, Math.sin(a + 0.15) * 70, Math.cos(a) * 110, Math.sin(a) * 110);
  }
  g.setScale(0.1);
  k.scene.tweens.add({ targets: g, scale: 1, angle: 40, duration: 380, ease: 'Back.out' });
  const e = particles(k.scene, at.x, at.y, 'fx-flame', { speed: { min: 60, max: 180 }, scale: { start: 1.8, end: 0.2 }, alpha: { start: 1, end: 0 }, tint: [k.c[0], k.c[1]], lifespan: 600, frequency: 15, quantity: 3, emitting: true });
  await wait(k.scene, 650);
  e.stop();
  const to = ahead(k, 320, 20);
  k.scene.tweens.add({ targets: g, x: to.x, y: to.y, scale: 0.4, alpha: 0, duration: 380, ease: 'Quad.in', onComplete: () => g.destroy() });
  cleanup(k.scene, 700, e);
  await wait(k.scene, 380);
});

// ================================================================ impactos

const impactVariant = fx(async (k) => {
  const big = k.v === 'giant' ? 1.6 : k.v === 'small' ? 0.6 : 1;
  const at = k.v === 'dive' ? { x: k.x, y: k.y } : ahead(k, 30);
  const c = k.v === 'fire' ? [0xff5a1a, 0xffd23f] : k.v === 'spark' ? [0xffe040, 0xffffff] : k.c;
  if (k.v === 'dive') {
    const streak = k.scene.add.image(at.x, at.y - 360, 'fx-spark').setTint(c[0]).setScale(3, 8).setDepth(DEPTH).setBlendMode('ADD');
    await new Promise<void>((r) => k.scene.tweens.add({ targets: streak, y: at.y, duration: 260, ease: 'Quad.in', onComplete: () => (streak.destroy(), r()) }));
  }
  if (k.v === 'ball') {
    const ball = k.scene.add.graphics({ x: at.x, y: at.y - 30 }).setDepth(DEPTH);
    ball.fillStyle(0xffffff).fillCircle(0, 0, 60).lineStyle(4, 0x222222).strokeCircle(0, 0, 60);
    ball.fillStyle(0x222222).fillPoints([pt(0, -18), pt(17, -6), pt(11, 15), pt(-11, 15), pt(-17, -6)], true);
    for (let i = 0; i < 5; i++) {
      const a = -Math.PI / 2 + (i / 5) * Math.PI * 2;
      ball.fillStyle(0x222222).fillCircle(Math.cos(a) * 46, Math.sin(a) * 46, 11);
    }
    ball.setScale(0.1);
    await new Promise<void>((r) => k.scene.tweens.add({ targets: ball, scale: 1.4, angle: 200, duration: 380, ease: 'Back.out', onComplete: () => r() }));
    k.scene.tweens.add({ targets: ball, alpha: 0, scale: 1.8, duration: 300, onComplete: () => ball.destroy() });
  }
  if (k.v === 'goalpost') {
    const post = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    post.fillStyle(0xffffff).fillRect(-90, -120, 10, 120).fillRect(80, -120, 10, 120).fillRect(-90, -124, 180, 10);
    post.lineStyle(1, 0xcfd8e0, 0.8);
    for (let i = -80; i < 80; i += 14) post.lineBetween(i, -114, i, 0);
    post.setAlpha(0);
    k.scene.tweens.add({ targets: post, alpha: 1, x: at.x + perp(k.o.dir).x * 80, duration: 420, yoyo: true, hold: 200, onComplete: () => post.destroy() });
    await wait(k.scene, 500);
  }
  if (k.v === 'kick' || k.v === 'spin') {
    const g = k.scene.add.graphics({ x: at.x, y: at.y - 20 }).setDepth(DEPTH);
    for (let i = 0; i < (k.v === 'spin' ? 3 : 1); i++) {
      g.lineStyle(10 - i * 2, i ? c[1] ?? 0xffffff : 0xffffff, 0.9).beginPath();
      g.arc(0, 0, 50 + i * 16, angleOf(k.o.dir) - 2, angleOf(k.o.dir) + 1.2);
      g.strokePath();
    }
    k.scene.tweens.add({ targets: g, angle: k.v === 'spin' ? 540 : 120, scale: 1.5, alpha: 0, duration: 520, onComplete: () => g.destroy() });
  }
  if (k.v === 'dust') puff(k.scene, at.x, at.y + 10, 'fx-glow', 30, { speed: { min: 40, max: 200 }, scale: { start: 2, end: 4 }, alpha: { start: 0.6, end: 0 }, tint: [0xd8b880, 0xbfa070], lifespan: 900 });
  for (let i = 0; i < 3; i++) k.scene.time.delayedCall(i * 90, () => ring(k.scene, at.x, at.y, i % 2 ? c[1] ?? c[0] : c[0], (80 + i * 30) * big, 450, 8, DEPTH));
  puff(k.scene, at.x, at.y, 'fx-spark', Math.round(40 * big), { speed: { min: 260, max: 520 * big }, scale: { start: 1, end: 0 }, tint: [c[0], c[1] ?? c[0], 0xffffff], lifespan: 400, rotate: { onEmit: () => Phaser.Math.Between(0, 360) } });
  if (k.v === 'fire') puff(k.scene, at.x, at.y, 'fx-flame', 40, { speed: { min: 150, max: 380 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: c, lifespan: 600 });
  flash(k.scene, at.x, at.y, c[0], 150 * big);
  shake(k.scene, 120 * big, 0.006 * big);
  await wait(k.scene, 550);
});

/** Lluvia de golpes alrededor del balón (Chut de los 100 toques). */
const barrage = fx(async (k) => {
  const at = ahead(k, 30, 20);
  for (let i = 0; i < 9; i++) {
    k.scene.time.delayedCall(i * 70, () => {
      const px = at.x + Phaser.Math.Between(-50, 50);
      const py = at.y + Phaser.Math.Between(-40, 40);
      const s = k.scene.add.image(px, py, 'fx-star').setTint(i % 2 ? k.c[0] : 0xffe040).setScale(3).setDepth(DEPTH);
      k.scene.tweens.add({ targets: s, scale: 0, angle: 90, duration: 260, onComplete: () => s.destroy() });
      ring(k.scene, px, py, 0xffffff, 30, 220, 4, DEPTH);
    });
  }
  await wait(k.scene, 700);
  await impactVariant(k.scene, k.x, k.y, k.o, k.c, 'giant');
});

// ================================================================ luz

const lightBeam = fx(async (k) => {
  flash(k.scene, k.x, k.y - 10, k.c[0], 140);
  await beam(k.scene, k.x, k.y - 10, k.o.dir, [k.c[0], k.c[1], 0xffffff], 360, 26, 600);
});

const lightFlash = fx(async (k) => {
  rays(k.scene, k.x, k.y - 20, [0xffffff, k.c[0]], 20, 260, 600);
  k.scene.time.delayedCall(250, () => screenFlash(k.scene, 0xffffff, 260));
  await wait(k.scene, 650);
});

/** Aureola dorada en el cielo y una columna de luz que baja (Zona sagrada). */
const lightHalo = fx(async (k) => {
  const at = ahead(k, 40);
  const halo = k.scene.add.graphics({ x: at.x, y: at.y - 170 }).setDepth(DEPTH);
  halo.lineStyle(10, k.c[0], 0.6).strokeEllipse(0, 0, 160, 50);
  halo.lineStyle(4, 0xffffff).strokeEllipse(0, 0, 150, 44);
  halo.setScale(0.2).setAlpha(0);
  k.scene.tweens.add({ targets: halo, scale: 1, alpha: 1, duration: 320, ease: 'Back.out' });
  await wait(k.scene, 350);
  const col = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH - 1);
  col.fillStyle(k.c[0], 0.25).fillRect(-70, -170, 140, 190);
  col.fillStyle(0xffffff, 0.5).fillRect(-30, -170, 60, 190);
  col.setScale(1, 0).setY(at.y - 170);
  k.scene.tweens.add({ targets: col, scaleY: 1, y: at.y, duration: 260 });
  puff(k.scene, at.x, at.y, 'fx-star', 20, { speed: { min: 30, max: 120 }, scale: { start: 0.8, end: 0 }, tint: [0xffffff, k.c[0]], lifespan: 800 });
  await wait(k.scene, 500);
  k.scene.tweens.add({ targets: [halo, col], alpha: 0, duration: 300, onComplete: () => (halo.destroy(), col.destroy()) });
});

const lightRays = fx(async (k) => {
  rays(k.scene, k.x, k.y - 20, [0xffffff, k.c[0], k.c[1]], 22, 280, 800);
  flash(k.scene, k.x, k.y - 20, 0xffffff, 200, 500);
  await wait(k.scene, 700);
});

// ================================================================ viento y tornados

/** Embudo de viento (dibujado), con color y partículas según la variante. */
function funnel(k: Ctx, cx: number, cy: number, ms = 1000, scale = 1): Promise<void> {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const H = 210 * scale;
  return animate(k.scene, ms, (t) => {
    const grow = Math.min(1, t * 4);
    const fade = t > 0.8 ? (1 - t) / 0.2 : 1;
    g.clear();
    for (let i = 0; i < 9; i++) {
      const h = i / 8;
      const r = (16 + h * 78) * grow * scale;
      const y = cy + 16 - h * H * grow;
      const wob = Math.sin(t * 12 + i) * 6;
      g.fillStyle(k.c[0], 0.16 * fade).fillEllipse(cx + wob, y, r * 2, r * 0.5);
      g.lineStyle(3, i % 2 ? k.c[1] ?? k.c[0] : k.c[0], 0.75 * fade).strokeEllipse(cx + wob, y, r * 2, r * 0.5);
    }
    for (let s = 0; s < 14; s++) {
      const h = (s * 0.137 + t * 1.5) % 1;
      const a = t * Math.PI * 10 + s * 2.1;
      const r = (16 + h * 78) * grow * scale;
      const y = cy + 16 - h * H * grow;
      const px = cx + Math.cos(a) * r;
      const py = y + Math.sin(a) * r * 0.25;
      const front = Math.sin(a) > 0;
      g.lineStyle(front ? 4 : 2, 0xffffff, (front ? 0.95 : 0.4) * fade).lineBetween(px, py, px - Math.sin(a) * 22, py + Math.cos(a) * 5);
    }
    if (t >= 1) g.destroy();
  });
}

const tornadoV = fx(async (k0) => {
  const tint: Record<string, number[]> = { white: [0xe8f4ff, 0xffffff], blue: [0x2f6fff, 0x8fd0ff], poison: [0xa060ff, 0xd090ff], sand: [0xd8b880, 0xf0d8a8], leaves: [0x8ab040, 0xc89a40] };
  const k = tint[k0.v] ? { ...k0, c: tint[k0.v] } : k0;
  const leaf = k.v === 'leaves' ? 'fx-petal' : k.v === 'sand' ? 'fx-rock' : k.v === 'poison' ? 'fx-glow' : null;
  if (leaf) {
    const e = particles(k.scene, k.x, k.y - 60, leaf, { speed: { min: 60, max: 220 }, scale: { start: 1, end: 0.4 }, alpha: { start: 0.9, end: 0 }, tint: k.v === 'leaves' ? [0xc87a2a, 0x8a5a20, 0xe8a040] : k.c, lifespan: 900, rotate: { min: 0, max: 360 }, frequency: 30, quantity: 2, emitting: true });
    k.scene.time.delayedCall(900, () => e.stop());
    cleanup(k.scene, 1900, e);
  }
  ring(k.scene, k.x, k.y + 18, k.c[0], 90, 800, 6);
  await funnel(k, k.x, k.y);
});

const tornadoDouble = fx(async (k) => {
  const s = perp(k.o.dir);
  void funnel(k, k.x + s.x * 60, k.y + s.y * 60, 1000, 0.8);
  await funnel(k, k.x - s.x * 60, k.y - s.y * 60, 1000, 0.8);
});

/** Anillos de viento girando en horizontal alrededor del jugador (Giro bobina, Superpeonza). */
const tornadoSpiral = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  await animate(k.scene, 950, (t) => {
    const fade = t > 0.8 ? (1 - t) / 0.2 : 1;
    g.clear();
    for (let i = 0; i < 5; i++) {
      const r = 40 + i * 16 + t * 30;
      const y = k.y - 10 - i * 12;
      g.lineStyle(4, i % 2 ? 0xffffff : k.c[0], 0.8 * fade).beginPath();
      g.arc(k.x, y, r, t * 18 + i, t * 18 + i + 4.2);
      g.strokePath();
    }
  });
  g.destroy();
  ring(k.scene, k.x, k.y + 18, 0xffffff, 120, 450, 6);
});

const windDash = fx(async (k) => {
  await speedLines(k.scene, k.x, k.y, k.o.dir, [k.c[0], 0xffffff], 650);
});

const speedlinesFx = fx(async (k) => {
  await speedLines(k.scene, k.x, k.y, k.o.dir, [k.c[0], k.c[1], 0xffffff], 700);
});

/** Nube de arena, polvo o veneno que lo tapa todo. */
const sandstorm = fx(async (k) => {
  const tint = k.v === 'poison' ? [0xa060ff, 0x7a30d0, 0xc090ff] : [0xd8b880, 0xbfa070, 0xe8d0a0];
  const e = particles(k.scene, k.x, k.y, 'fx-glow', { speed: { min: 60, max: 240 }, scale: { start: 2, end: 5 }, alpha: { start: 0.55, end: 0 }, tint, lifespan: 1100, frequency: 20, quantity: 4, emitting: true });
  if (k.v === 'vortex') void funnel({ ...k, c: tint }, k.x, k.y, 1000, 1);
  await wait(k.scene, 900);
  e.stop();
  cleanup(k.scene, 1200, e);
});

// ================================================================ oscuridad

const darkCurse = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH - 1);
  g.fillStyle(0x200008, 0.6).fillCircle(0, 0, 150);
  g.fillStyle(0xc0103a, 0.5).fillCircle(0, 0, 100);
  g.setScale(0.2).setAlpha(0);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 1, duration: 280 });
  for (let i = 0; i < 3; i++) {
    k.scene.time.delayedCall(250 + i * 120, () => {
      const s = k.scene.add.graphics({ x: k.x + Phaser.Math.Between(-40, 40), y: k.y - 20 + Phaser.Math.Between(-30, 30) }).setDepth(DEPTH);
      s.lineStyle(6, 0x000000).lineBetween(-60, -30, 60, 30);
      s.lineStyle(2, 0xff2050).lineBetween(-60, -30, 60, 30);
      k.scene.tweens.add({ targets: s, alpha: 0, duration: 300, onComplete: () => s.destroy() });
    });
  }
  await wait(k.scene, 750);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
});

const darkGravity = fx(async (k) => {
  const at = ahead(k, 40);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH - 1);
  await animate(k.scene, 900, (t) => {
    g.clear();
    g.fillStyle(k.c[0], 0.25 * (1 - t * 0.5)).fillEllipse(0, 0, 220, 110);
    for (let i = 0; i < 4; i++) {
      const r = ((t * 2 + i / 4) % 1) * 110;
      g.lineStyle(3, k.c[1] ?? k.c[0], 1 - r / 110).strokeEllipse(0, 0, r * 2, r);
    }
    g.fillStyle(k.c[0], 0.3).fillEllipse(0, -60, 200 * (1 - t * 0.3), 140);
  });
  g.destroy();
  shake(k.scene, 200, 0.007);
});

const darkHole = fx(async (k) => {
  const at = ahead(k, 50, 20);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  const pull = particles(k.scene, at.x, at.y, 'fx-glow', { emitZone: { type: 'edge', source: new Phaser.Geom.Circle(0, 0, 140), quantity: 30 }, moveToX: 0, moveToY: 0, scale: { start: 0.9, end: 0.1 }, tint: [k.c[0], k.c[1] ?? k.c[0]], lifespan: 450, frequency: 20, quantity: 2, emitting: true });
  pull.setPosition(at.x, at.y);
  await animate(k.scene, 1000, (t) => {
    const grow = Math.min(1, t * 3);
    g.clear();
    for (let i = 0; i < 3; i++) {
      g.lineStyle(8 - i * 2, i === 1 ? 0xffffff : k.c[i % k.c.length], 0.8).beginPath();
      g.arc(0, 0, (46 + i * 12) * grow, t * 10 + i, t * 10 + i + 4.5);
      g.strokePath();
    }
    g.fillStyle(0x000000).fillCircle(0, 0, 38 * grow);
  });
  pull.stop();
  g.destroy();
  cleanup(k.scene, 500, pull);
  flash(k.scene, at.x, at.y, k.c[0], 120);
});

/** Orbe oscuro que se carga con chispas y sale disparado (Tornado oscuro, Astro remate...). */
const darkOrb = fx(async (k) => {
  const at = ahead(k, 20, 20);
  const orb = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  orb.fillStyle(k.c[0], 0.35).fillCircle(0, 0, 46);
  orb.fillStyle(k.c[1] ?? k.c[0], 0.8).fillCircle(0, 0, 32);
  orb.fillStyle(0xffffff, 0.9).fillCircle(0, 0, 14);
  orb.setScale(0.1);
  k.scene.tweens.add({ targets: orb, scale: 1.3, duration: 500, ease: 'Cubic.out' });
  const arcs = k.scene.add.graphics().setDepth(DEPTH);
  await animate(k.scene, 520, () => {
    arcs.clear().lineStyle(2, 0xffffff, 0.8);
    for (let i = 0; i < 3; i++) {
      const a = Math.random() * Math.PI * 2;
      arcs.lineBetween(at.x, at.y, at.x + Math.cos(a) * 70, at.y + Math.sin(a) * 70);
    }
  });
  arcs.destroy();
  const to = ahead(k, 320, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: orb, x: to.x, y: to.y, duration: 320, ease: 'Quad.in', onComplete: () => r() }));
  flash(k.scene, to.x, to.y, k.c[0], 160);
  orb.destroy();
});

const darkRift = fx(async (k) => {
  const at = ahead(k, 50, 10);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH).setRotation(angleOf(k.o.dir) + 0.6);
  await animate(k.scene, 800, (t) => {
    const open = Math.sin(Math.min(1, t * 1.3) * Math.PI);
    g.clear();
    g.fillStyle(k.c[0], 0.6).fillEllipse(0, 0, 220, 50 * open + 4);
    g.fillStyle(0x000000).fillEllipse(0, 0, 200, 34 * open + 2);
    g.lineStyle(2, 0xffffff, open).strokeEllipse(0, 0, 204, 36 * open + 2);
  });
  g.destroy();
});

/** Espiral blanca y negra (Carga negativa, Lluvia oscura). */
const darkSpiral = fx(async (k) => {
  const at = ahead(k, 30, 20);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  for (let arm = 0; arm < 6; arm++) {
    g.lineStyle(12, arm % 2 ? 0xffffff : 0x111111, 0.95).beginPath();
    for (let s = 0; s <= 1; s += 0.05) {
      const a = arm * (Math.PI / 3) + s * Math.PI * 2;
      const r = 10 + s * 100;
      if (s === 0) g.moveTo(Math.cos(a) * r, Math.sin(a) * r);
      else g.lineTo(Math.cos(a) * r, Math.sin(a) * r);
    }
    g.strokePath();
  }
  g.setScale(0.1);
  k.scene.tweens.add({ targets: g, scale: 1, duration: 300 });
  k.scene.tweens.add({ targets: g, angle: -540, duration: 1000 });
  await wait(k.scene, 800);
  k.scene.tweens.add({ targets: g, alpha: 0, scale: 1.4, duration: 250, onComplete: () => g.destroy() });
});

const darkWarp = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH - 1);
  await animate(k.scene, 900, (t) => {
    g.clear();
    for (let i = 0; i < 6; i++) {
      const r = ((t * 1.5 + i / 6) % 1) * 140;
      g.lineStyle(10, i % 2 ? k.c[0] : lighten(k.c[0], 40), (1 - r / 140) * 0.8).strokeCircle(0, 0, r);
    }
    g.fillStyle(0x000000, Math.sin(t * Math.PI)).fillCircle(0, 0, 24);
  });
  g.destroy();
});

const darkHand = fx(async (k) => {
  const at = ahead(k, 50);
  puff(k.scene, at.x, at.y - 40, 'fx-glow', 24, { speed: { min: 30, max: 100 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.6, end: 0 }, tint: [k.c[0], 0x200030], lifespan: 900 });
  await summon(k.scene, at.x, at.y + 30, handParts(darken(k.c[0], 10), 0x100018), k.c, { scale: 0.9, enter: 'rise', exit: 'shrink', hold: 350, dir: k.o.dir, face: true });
});

// ================================================================ rayos

function bolt(scene: Phaser.Scene, x: number, y: number, color: number, height = 340, width = 12): void {
  const g = scene.add.graphics().setDepth(DEPTH);
  const pts: Phaser.Math.Vector2[] = [];
  let px = x + Phaser.Math.Between(-40, 40);
  for (let i = 0; i <= 8; i++) {
    pts.push(new Phaser.Math.Vector2(i === 8 ? x : px, y - height * (1 - i / 8)));
    px += Phaser.Math.Between(-28, 28);
  }
  g.lineStyle(width, color, 0.4).strokePoints(pts);
  g.lineStyle(width / 3, 0xffffff, 1).strokePoints(pts);
  scene.tweens.add({ targets: g, alpha: 0, duration: 260, delay: 80, onComplete: () => g.destroy() });
}

function arcs(scene: Phaser.Scene, x: number, y: number, r: number, color: number, ms: number): Promise<void> {
  const g = scene.add.graphics().setDepth(DEPTH);
  return animate(scene, ms, (t) => {
    g.clear();
    if (t >= 1) return g.destroy();
    for (let i = 0; i < 4; i++) {
      let a = Math.random() * Math.PI * 2;
      g.lineStyle(3, i % 2 ? color : 0xffffff, 0.9).beginPath().moveTo(x + Math.cos(a) * r * 0.3, y + Math.sin(a) * r * 0.3);
      for (let s = 1; s <= 4; s++) {
        a += Phaser.Math.FloatBetween(-0.5, 0.5);
        g.lineTo(x + Math.cos(a) * r * (0.3 + s * 0.18), y + Math.sin(a) * r * (0.3 + s * 0.18));
      }
      g.strokePath();
    }
  });
}

const lightningBig = fx(async (k) => {
  const at = ahead(k, 40);
  screenFlash(k.scene, k.c[0], 120);
  bolt(k.scene, at.x, at.y, k.c[0], 460, 30);
  k.scene.time.delayedCall(120, () => bolt(k.scene, at.x + 20, at.y, k.c[1] ?? k.c[0], 420, 18));
  ring(k.scene, at.x, at.y + 16, k.c[0], 140, 500, 10);
  flash(k.scene, at.x, at.y, 0xffffff, 200, 350);
  shake(k.scene, 250, 0.012);
  puff(k.scene, at.x, at.y, 'fx-spark', 40, { speed: { min: 250, max: 520 }, scale: { start: 1, end: 0 }, tint: [k.c[0], 0xffffff], lifespan: 380 });
  await wait(k.scene, 650);
});

const lightningBarrier = fx(async (k) => {
  const at = ahead(k, 30, 20);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  g.fillStyle(k.c[0], 0.2).fillCircle(0, 0, 90).lineStyle(4, lighten(k.c[0], 30), 0.9).strokeCircle(0, 0, 90);
  g.setScale(0.1);
  k.scene.tweens.add({ targets: g, scale: 1, duration: 260, ease: 'Back.out' });
  await arcs(k.scene, at.x, at.y, 100, k.c[0], 700);
  k.scene.tweens.add({ targets: g, alpha: 0, scale: 1.2, duration: 250, onComplete: () => g.destroy() });
});

const lightningOrb = fx(async (k) => {
  const at = ahead(k, 20, 20);
  const orb = k.scene.add.image(at.x, at.y, 'fx-glow').setTint(k.c[0]).setScale(0.5).setDepth(DEPTH).setBlendMode('ADD');
  k.scene.tweens.add({ targets: orb, scale: 3.2, duration: 450 });
  await arcs(k.scene, at.x, at.y, 80, k.c[0], 500);
  const to = ahead(k, 320, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: orb, x: to.x, y: to.y, duration: 280, ease: 'Quad.in', onComplete: () => r() }));
  orb.destroy();
  bolt(k.scene, to.x, to.y, k.c[0], 300, 14);
  flash(k.scene, to.x, to.y, k.c[0], 160);
});

const lightningHand = fx(async (k) => {
  await arcs(k.scene, k.x, k.y - 30, 70, k.c[0], 450);
  flash(k.scene, k.x, k.y - 30, k.c[0], 120);
  await beam(k.scene, k.x, k.y - 30, k.o.dir, [k.c[0], 0xffffff], 220, 18, 420);
});

const lightningZigzag = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const side = perp(k.o.dir);
  const pts: Phaser.Math.Vector2[] = [];
  for (let i = 0; i <= 8; i++) {
    const s = (i % 2 ? 1 : -1) * 34;
    pts.push(new Phaser.Math.Vector2(k.x + k.o.dir.x * i * 32 + side.x * s, k.y + 10 + k.o.dir.y * i * 32 + side.y * s));
  }
  await animate(k.scene, 600, (t) => {
    const n = Math.max(2, Math.ceil(pts.length * Math.min(1, t * 2)));
    g.clear().lineStyle(12, k.c[0], 0.5 * (1 - t)).strokePoints(pts.slice(0, n));
    g.lineStyle(4, 0xffffff, 1 - t).strokePoints(pts.slice(0, n));
  });
  g.destroy();
  puff(k.scene, pts[8].x, pts[8].y, 'fx-spark', 30, { speed: { min: 200, max: 420 }, scale: { start: 1, end: 0 }, tint: [k.c[0], 0xffffff], lifespan: 350 });
});

// ================================================================ manos

/**
 * Mano gigante con su estilo: Mano celestial (amarilla con llamas y rayos), Mano mágica (con el Majin
 * detrás), Mano diabólica (demonio morado), Mano celestial X (brazos en cruz), Millón de manos...
 */
const handV = fx(async (k) => {
  const at = ahead(k, 46);
  const skin = k.v === 'demon' ? 0xb050ff : k.v === 'spirit' || k.v === 'x' ? 0xff4060 : k.v === 'deity' ? 0xffc040 : k.c[0];
  const line = darken(skin, 35);
  const behind: Promise<unknown>[] = [];
  if (k.v === 'majin' || k.v === 'deity' || k.v === 'demon') {
    const body = k.v === 'demon' ? 0x9a40e0 : k.v === 'deity' ? 0xe0a030 : 0xff7a40;
    const hair = k.v === 'demon' ? 0x401060 : k.v === 'deity' ? 0xfff0a0 : 0xff2a10;
    const parts = majinParts(body, hair);
    if (k.v === 'deity') parts.unshift(['p', 0xff4040, -170, -220, 170, -220, 210, -20, -210, -20]);
    if (k.v === 'demon') parts.push(['p', 0x401060, -40, -280, -70, -340, -20, -270], ['p', 0x401060, 40, -280, 70, -340, 20, -270]);
    behind.push(summon(k.scene, k.x - k.o.dir.x * 50, k.y + 30, parts, k.c, { scale: 1.15, enter: 'rise', exit: 'fade', hold: 650, depth: DEPTH - 2 }));
  }
  if (k.v === 'god' || k.v === 'omega') rays(k.scene, at.x, at.y - 60, [k.c[0], k.c[1] ?? 0xffffff], 16, 200, 900, DEPTH - 1);
  if (k.v === 'god') for (let i = 0; i < 3; i++) k.scene.time.delayedCall(150 + i * 140, () => bolt(k.scene, at.x + Phaser.Math.Between(-60, 60), at.y - 40, 0xffe040, 240, 10));
  if (k.v === 'x') {
    const xg = k.scene.add.graphics({ x: at.x, y: at.y - 60 }).setDepth(DEPTH + 1);
    xg.fillStyle(0xff2040, 0.85).fillRect(-120, -10, 240, 20).setRotation(0.7);
    const xg2 = k.scene.add.graphics({ x: at.x, y: at.y - 60 }).setDepth(DEPTH + 1);
    xg2.fillStyle(0xff2040, 0.85).fillRect(-120, -10, 240, 20).setRotation(-0.7);
    k.scene.tweens.add({ targets: [xg, xg2], alpha: 0, scale: 1.4, delay: 450, duration: 300, onComplete: () => (xg.destroy(), xg2.destroy()) });
  }
  if (k.v === 'many') {
    for (let i = 0; i < 6; i++) {
      const s = perp(k.o.dir);
      const off = (i - 2.5) * 34;
      k.scene.time.delayedCall(i * 70, () => void summon(k.scene, at.x + s.x * off, at.y + s.y * off + 10, handParts(i % 2 ? skin : lighten(skin, 25), line), k.c, { scale: 0.45, enter: 'zoom', exit: 'fade', hold: 400 - i * 40, dir: k.o.dir, face: true }));
    }
    await wait(k.scene, 900);
    return;
  }
  const dome = k.v === 'dome' || k.v === 'deity';
  if (dome) {
    const d = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH - 1);
    d.fillStyle(k.c[0], 0.25).fillEllipse(0, -40, 240, 200).lineStyle(4, 0xffffff, 0.7).strokeEllipse(0, -40, 240, 200);
    d.setScale(0.1);
    k.scene.tweens.add({ targets: d, scale: 1, duration: 300, delay: 300, ease: 'Back.out' });
    k.scene.tweens.add({ targets: d, alpha: 0, delay: 950, duration: 250, onComplete: () => d.destroy() });
  }
  k.scene.time.delayedCall(300, () => {
    flash(k.scene, at.x, at.y - 60, skin, 170);
    shake(k.scene, 140, 0.006);
  });
  await Promise.all([summon(k.scene, at.x, at.y + 20, handParts(skin, line), k.c, { scale: behind.length ? 0.75 : 1, enter: 'rise', exit: 'fade', hold: 500, dir: k.o.dir, face: true, pulse: true }), ...behind]);
});

/** Puño gigante con su variante (cohete, doble, ráfaga, eléctrico, de fuego...). */
const punchV = fx(async (k) => {
  const skin = k.v === 'electric' ? 0x6fd8ff : k.v === 'fire' ? 0xff7a30 : k.c[0];
  const line = darken(skin, 35);
  const parts = fistParts(skin, line);
  const at = ahead(k, 60);
  if (k.v === 'barrage') {
    for (let i = 0; i < 7; i++) {
      const s = perp(k.o.dir);
      const off = Phaser.Math.Between(-50, 50);
      k.scene.time.delayedCall(i * 60, () => void summon(k.scene, at.x + s.x * off, at.y + s.y * off, parts, k.c, { scale: 0.45, enter: 'zoom', exit: 'charge', hold: 40, dir: k.o.dir, face: true }));
    }
    await wait(k.scene, 700);
  } else if (k.v === 'double') {
    const s = perp(k.o.dir);
    await Promise.all([-1, 1].map((d) => summon(k.scene, k.x + s.x * 50 * d, k.y + s.y * 50 * d, parts, k.c, { scale: 0.7, enter: 'zoom', exit: 'charge', hold: 160, dir: k.o.dir, face: true })));
  } else if (k.v === 'dive') {
    await summon(k.scene, at.x, at.y + 40, parts, k.c, { scale: 0.9, enter: 'drop', exit: 'fade', hold: 200 });
  } else if (k.v === 'upper') {
    const g = await summon(k.scene, at.x, at.y + 30, parts, k.c, { scale: 0.9, enter: 'rise', exit: 'up', hold: 120 });
    void g;
    rays(k.scene, at.x, at.y - 80, [0xffffff, k.c[0]], 12, 160);
  } else {
    const trail = k.v === 'rocket' ? particles(k.scene, k.x, k.y, 'fx-flame', { speed: 40, scale: { start: 2, end: 0.2 }, tint: [0xff6a20, 0xffd23f], lifespan: 350, frequency: 15, quantity: 2, emitting: true }) : null;
    const g = k.scene.add.graphics({ x: k.x, y: k.y - 10 }).setDepth(DEPTH).setRotation(angleOf(k.o.dir) + Math.PI / 2);
    drawFigure(g, parts, k.c);
    g.setScale(k.v === 'giant' ? 0.6 : 0.3);
    trail?.startFollow(g);
    await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: at.x + k.o.dir.x * 60, y: at.y + k.o.dir.y * 60 - 10, scale: k.v === 'giant' ? 1.8 : 1.2, duration: 260, ease: 'Quad.out', onComplete: () => r() }));
    trail?.stop();
    if (trail) cleanup(k.scene, 400, trail);
    k.scene.tweens.add({ targets: g, alpha: 0, delay: 250, duration: 250, onComplete: () => g.destroy() });
  }
  const hit = ahead(k, 130);
  ring(k.scene, hit.x, hit.y, skin, 100, 420, 8, DEPTH);
  flash(k.scene, hit.x, hit.y, k.v === 'electric' ? 0xffffff : skin, 150);
  if (k.v === 'electric') void arcs(k.scene, hit.x, hit.y, 90, 0x6fd8ff, 400);
  if (k.v === 'fire') puff(k.scene, hit.x, hit.y, 'fx-flame', 40, { speed: { min: 150, max: 360 }, scale: { start: 2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [0xff6a20, 0xffd23f], lifespan: 550 });
  shake(k.scene, 160, 0.008);
  await wait(k.scene, 350);
});

// ================================================================ copias

/** Copias del jugador (ilusiones, ninjas, imágenes residuales) o del balón. */
const cloneV = fx(async (k) => {
  if (k.v === 'balls') {
    const at = ahead(k, 30, 20);
    for (let i = 0; i < 4; i++) {
      const b = k.scene.add.image(at.x, at.y, 'ball').setScale(2.2).setDepth(DEPTH).setTint(i % 2 ? 0xffffff : k.c[0]);
      const a = angleOf(k.o.dir) + (i - 1.5) * 0.35;
      k.scene.tweens.add({ targets: b, x: at.x + Math.cos(a) * 200, y: at.y + Math.sin(a) * 200, alpha: 0, duration: 650, onComplete: () => b.destroy() });
    }
    flash(k.scene, at.x, at.y, k.c[0], 120);
    await wait(k.scene, 650);
    return;
  }
  if (!k.o.texture) return;
  const n = k.v === 'double' ? 2 : k.v === 'triple' ? 3 : k.v === 'ring' ? 6 : 5;
  const dark = k.v === 'dark';
  const copies: Phaser.GameObjects.Image[] = [];
  for (let i = 0; i < n; i++) {
    const c = k.scene.add.image(k.x, k.y, k.o.texture).setScale(k.o.scale ?? 1).setDepth(DEPTH).setAlpha(0.75);
    if (dark) c.setTint(0x5020a0);
    else if (k.v !== 'triple' && k.v !== 'double') c.setTint(i % 2 ? k.c[0] : lighten(k.c[0], 40));
    let tx: number;
    let ty: number;
    if (k.v === 'ring') {
      const a = (i / n) * Math.PI * 2;
      tx = k.x + Math.cos(a) * 80;
      ty = k.y + Math.sin(a) * 40;
    } else if (k.v === 'afterimage') {
      tx = k.x - k.o.dir.x * (i + 1) * 26;
      ty = k.y - k.o.dir.y * (i + 1) * 26;
      c.setAlpha(0.6 - i * 0.1);
    } else {
      const a = (i / (n - 1) - 0.5) * 1.6 + angleOf(k.o.dir) + Math.PI / 2;
      tx = k.x + Math.cos(a) * 70;
      ty = k.y + Math.sin(a) * 40;
    }
    k.scene.tweens.add({ targets: c, x: tx, y: ty, duration: 240, yoyo: k.v !== 'afterimage', hold: 300, ease: 'Sine.out', onComplete: () => k.scene.tweens.add({ targets: c, alpha: 0, duration: 200, onComplete: () => c.destroy() }) });
    copies.push(c);
  }
  if (dark) puff(k.scene, k.x, k.y, 'fx-glow', 20, { speed: { min: 30, max: 120 }, scale: { start: 1.4, end: 3 }, alpha: { start: 0.6, end: 0 }, tint: [0x5020a0, 0x200040], lifespan: 900 });
  ring(k.scene, k.x, k.y + 18, k.c[0], 80, 600, 4);
  await wait(k.scene, 800);
});

// ================================================================ hielo

const iceBall = fx(async (k) => {
  const at = ahead(k, 30, 20);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  for (let i = 0; i < 10; i++) {
    const a = (i / 10) * Math.PI * 2;
    g.fillStyle(i % 2 ? 0xbfefff : 0x7fd0ff, 0.85).fillTriangle(0, 0, Math.cos(a - 0.3) * 50, Math.sin(a - 0.3) * 50, Math.cos(a) * 80, Math.sin(a) * 80);
  }
  g.fillStyle(0xffffff, 0.8).fillCircle(0, 0, 30);
  g.setScale(0.1);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scale: 1, angle: 90, duration: 360, ease: 'Back.out', onComplete: () => r() }));
  puff(k.scene, at.x, at.y, 'fx-flake', 30, { speed: { min: 60, max: 200 }, scale: { start: 1, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [0xbfefff, 0xffffff], lifespan: 900, rotate: { min: 0, max: 360 } });
  const to = ahead(k, 320, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: to.x, y: to.y, duration: 340, ease: 'Quad.in', onComplete: () => r() }));
  g.destroy();
  flash(k.scene, to.x, to.y, 0xbfefff, 150);
});

/** Ventisca que sale disparada y un copo de nieve gigante (Ventisca eterna). */
const iceBlizzard = fx(async (k) => {
  const a = angleOf(k.o.dir) * DEG;
  const e = particles(k.scene, k.x, k.y - 10, 'fx-flake', { speed: { min: 400, max: 700 }, angle: { min: a - 12, max: a + 12 }, scale: { start: 1.6, end: 0.5 }, alpha: { start: 1, end: 0 }, tint: [0xffffff, 0xbfefff, k.c[0]], lifespan: 550, rotate: { min: 0, max: 360 }, frequency: 6, quantity: 4, emitting: true });
  const at = ahead(k, 200, 20);
  const flake = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  flake.lineStyle(8, 0xffffff);
  for (let i = 0; i < 6; i++) {
    const r = (i / 6) * Math.PI * 2;
    const ex = Math.cos(r) * 90;
    const ey = Math.sin(r) * 90;
    flake.lineBetween(0, 0, ex, ey);
    flake.lineBetween(ex * 0.6, ey * 0.6, ex * 0.6 + Math.cos(r + 0.7) * 30, ey * 0.6 + Math.sin(r + 0.7) * 30);
    flake.lineBetween(ex * 0.6, ey * 0.6, ex * 0.6 + Math.cos(r - 0.7) * 30, ey * 0.6 + Math.sin(r - 0.7) * 30);
  }
  flake.setScale(0).setAlpha(0.9);
  k.scene.tweens.add({ targets: flake, scale: 1, angle: 60, delay: 350, duration: 400, ease: 'Back.out' });
  await wait(k.scene, 900);
  e.stop();
  k.scene.tweens.add({ targets: flake, alpha: 0, scale: 1.3, duration: 300, onComplete: () => flake.destroy() });
  cleanup(k.scene, 700, e);
});

/** Bloque de hielo que encierra lo que tiene delante (Ángel de nieve, Bloque de hielo). */
const iceBlock = fx(async (k) => {
  const at = ahead(k, 70);
  const parts: Part[] = [
    ['p', 0x9fdcff, -60, 0, -70, -120, 0, -150, 70, -120, 60, 0],
    ['p', 0xd8f4ff, -40, -10, -50, -110, 0, -134, 0, -10],
    ['l', 0xffffff, 3, -30, -100, 10, -60, 40, -90],
    ['l', 0xffffff, 2, -20, -40, 20, -20],
  ];
  if (k.v === 'cube') parts.splice(0, 2, ['r', -60, -120, 120, 120, 0x9fdcff, 0.9], ['p', 0xd8f4ff, -60, -120, -30, -150, 90, -150, 60, -120]);
  puff(k.scene, at.x, at.y - 60, 'fx-flake', 24, { speed: { min: 60, max: 180 }, scale: { start: 1, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [0xffffff, 0xbfefff], lifespan: 800, rotate: { min: 0, max: 360 } });
  await summon(k.scene, at.x, at.y + 20, parts, k.c, { scale: 1, enter: 'rise', exit: 'fade', hold: 500 });
});

/** Pinchos de hielo que salen del suelo hacia delante (Rompehielos). */
const iceGround = fx(async (k) => {
  for (let i = 0; i < 7; i++) {
    const at = ahead(k, 30 + i * 32);
    k.scene.time.delayedCall(i * 60, () => {
      const s = k.scene.add.image(at.x, at.y + 16, 'fx-shard').setTint(i % 2 ? 0x9fdcff : 0xffffff).setOrigin(0.5, 1).setDepth(at.y + 16).setScale(1.4, 0);
      k.scene.tweens.add({ targets: s, scaleY: 3 + (i % 3), duration: 180, ease: 'Back.out' });
      k.scene.tweens.add({ targets: s, alpha: 0, delay: 700, duration: 250, onComplete: () => s.destroy() });
    });
  }
  const frost = k.scene.add.graphics({ x: k.x, y: k.y + 16 }).setDepth(GROUND).setRotation(angleOf(k.o.dir));
  frost.fillStyle(0xbfefff, 0.4).fillRect(0, -30, 260, 60);
  k.scene.tweens.add({ targets: frost, alpha: 0, delay: 800, duration: 300, onComplete: () => frost.destroy() });
  await wait(k.scene, 950);
});

// ================================================================ aura, estrellas, escudos

/** Aura de energía alrededor del jugador (Chut granada, Remate en espiral, Psicorremate...). */
const auraV = fx(async (k) => {
  const at = ahead(k, 20, 10);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH - 1);
  const c0 = k.c[0];
  await animate(k.scene, 800, (t) => {
    const fade = t > 0.75 ? (1 - t) / 0.25 : 1;
    g.clear();
    if (k.v === 'hex' || k.v === 'crystal') {
      for (let i = 0; i < (k.v === 'hex' ? 7 : 10); i++) {
        const a = (i / 7) * Math.PI * 2 + t * 2;
        const r = i === 0 ? 0 : 40;
        const pts = Array.from({ length: 6 }, (_, j) => pt(Math.cos(a) * r + Math.cos((j * Math.PI) / 3) * 22, Math.sin(a) * r + Math.sin((j * Math.PI) / 3) * 22));
        g.fillStyle(c0, 0.35 * fade).fillPoints(pts, true).lineStyle(2, 0xffffff, 0.8 * fade).strokePoints(pts, true);
      }
    } else if (k.v === 'ring') {
      for (let i = 0; i < 3; i++) g.lineStyle(10, i === 1 ? 0xffffff : c0, (1 - i * 0.2) * fade).strokeCircle(0, 0, 30 + i * 18 + t * 30);
    } else if (k.v === 'spiral') {
      g.lineStyle(10, c0, 0.8 * fade).beginPath();
      for (let s = 0; s <= 1; s += 0.03) {
        const a = s * Math.PI * 5 + t * 10;
        const r = s * 90;
        if (s === 0) g.moveTo(Math.cos(a) * r, Math.sin(a) * r);
        else g.lineTo(Math.cos(a) * r, Math.sin(a) * r);
      }
      g.strokePath();
    } else {
      // llama de aura (azul, verde, psíquica)
      for (let i = 0; i < 12; i++) {
        const a = (i / 12) * Math.PI * 2;
        const r = 50 + Math.sin(t * 20 + i) * 10;
        g.fillStyle(i % 2 ? c0 : lighten(c0, 30), 0.5 * fade).fillTriangle(Math.cos(a - 0.3) * 30, Math.sin(a - 0.3) * 30, Math.cos(a + 0.3) * 30, Math.sin(a + 0.3) * 30, Math.cos(a) * r * 1.5, Math.sin(a) * r * 1.5 - 20);
      }
      g.fillStyle(0xffffff, 0.7 * fade).fillCircle(0, 0, 24);
    }
  });
  g.destroy();
  flash(k.scene, at.x, at.y, c0, 140);
});

/** Estrellas: constelación en triángulo, en cruz o en círculo. */
const starsV = fx(async (k) => {
  const at = ahead(k, 50, 40);
  const n = k.v === 'triangle' ? 3 : k.v === 'cross' ? 5 : k.v === 'ring' ? 10 : 8;
  const pos = Array.from({ length: n }, (_, i) => {
    if (k.v === 'triangle') {
      const a = -Math.PI / 2 + (i / 3) * Math.PI * 2;
      return { x: at.x + Math.cos(a) * 90, y: at.y + Math.sin(a) * 70 };
    }
    if (k.v === 'cross') return [{ x: 0, y: 0 }, { x: 0, y: -90 }, { x: 0, y: 90 }, { x: -70, y: 0 }, { x: 70, y: 0 }].map((p) => ({ x: at.x + p.x, y: at.y + p.y }))[i];
    const a = (i / n) * Math.PI * 2;
    return { x: at.x + Math.cos(a) * 90, y: at.y + Math.sin(a) * 50 };
  });
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const stars = pos.map((p, i) => {
    const s = k.scene.add.image(p.x, p.y, 'fx-star').setTint(i % 2 ? k.c[0] : 0xffffff).setScale(0).setDepth(DEPTH + 1);
    k.scene.tweens.add({ targets: s, scale: 2.2, angle: 180, delay: i * 70, duration: 260, ease: 'Back.out' });
    return s;
  });
  await wait(k.scene, n * 70 + 200);
  if (k.v === 'triangle') g.fillStyle(k.c[0], 0.3).fillPoints(pos.map((p) => pt(p.x, p.y)), true);
  g.lineStyle(3, 0xffffff, 0.9);
  if (k.v === 'cross') g.lineBetween(pos[1].x, pos[1].y, pos[2].x, pos[2].y).lineBetween(pos[3].x, pos[3].y, pos[4].x, pos[4].y);
  else pos.forEach((p, i) => g.lineBetween(p.x, p.y, pos[(i + 1) % n].x, pos[(i + 1) % n].y));
  await wait(k.scene, 400);
  if (k.v === 'cross') {
    screenFlash(k.scene, k.c[0], 160);
    flash(k.scene, at.x, at.y, 0xffffff, 220);
  }
  k.scene.tweens.add({ targets: [g, ...stars], alpha: 0, duration: 300, onComplete: () => [g, ...stars].forEach((o) => o.destroy()) });
});

const shieldV = fx(async (k) => {
  const at = ahead(k, 40, 10);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  const c0 = k.c[0];
  if (k.v === 'bubble') g.fillStyle(c0, 0.2).fillCircle(0, -20, 80).lineStyle(3, 0xffffff, 0.8).strokeCircle(0, -20, 80).fillStyle(0xffffff, 0.6).fillEllipse(-30, -60, 30, 16);
  else if (k.v === 'dome') g.fillStyle(c0, 0.3).fillEllipse(0, -30, 260, 200).lineStyle(5, lighten(c0, 40), 0.9).strokeEllipse(0, -30, 260, 200);
  else if (k.v === 'panels') {
    for (let i = -2; i <= 2; i++) g.fillStyle(c0, 0.35).fillRect(i * 50 - 22, -110 + Math.abs(i) * 10, 44, 100).lineStyle(2, 0xffffff, 0.8).strokeRect(i * 50 - 22, -110 + Math.abs(i) * 10, 44, 100);
  } else if (k.v === 'rings') for (let i = 0; i < 4; i++) g.lineStyle(8, i % 2 ? 0xffffff : c0, 0.8).strokeCircle(0, -20, 30 + i * 20);
  else {
    // aura (Escudo corporal, Bloque dureza)
    g.fillStyle(c0, 0.4).fillEllipse(0, -30, 150, 170);
    g.fillStyle(0xffffff, 0.35).fillEllipse(0, -30, 90, 110);
  }
  g.setScale(0.1).setAlpha(0);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 1, duration: 280, ease: 'Back.out' });
  k.scene.tweens.add({ targets: g, alpha: 0.55, duration: 110, yoyo: true, repeat: 2, delay: 320 });
  await wait(k.scene, 850);
  flash(k.scene, at.x, at.y - 20, c0, 160);
  k.scene.tweens.add({ targets: g, alpha: 0, scale: 1.2, duration: 250, onComplete: () => g.destroy() });
});

// ================================================================ criaturas

const beastV = fx(async (k) => {
  if (k.v === 'jaws') {
    const at = ahead(k, 70, 20);
    const top = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    const bot = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    for (const [g, s] of [[top, -1], [bot, 1]] as const) {
      g.fillStyle(k.c[0], 0.9).fillEllipse(0, s * 50, 200, 70);
      for (let i = -3; i <= 3; i++) g.fillStyle(0xffffff).fillTriangle(i * 24 - 10, s * 24, i * 24 + 10, s * 24, i * 24, s * -6);
    }
    top.setY(at.y - 50);
    bot.setY(at.y + 50);
    await new Promise<void>((r) => k.scene.tweens.add({ targets: top, y: at.y, duration: 380, ease: 'Back.in', onComplete: () => r() }));
    k.scene.tweens.add({ targets: bot, y: at.y, duration: 1 });
    shake(k.scene, 200, 0.01);
    flash(k.scene, at.x, at.y, k.c[0], 160);
    k.scene.tweens.add({ targets: [top, bot], alpha: 0, delay: 200, duration: 250, onComplete: () => (top.destroy(), bot.destroy()) });
    await wait(k.scene, 350);
    return;
  }
  if (k.v === 'claw') {
    const a = angleOf(k.o.dir);
    const claws = k.scene.add.graphics({ x: k.x + k.o.dir.x * 70, y: k.y - 10 + k.o.dir.y * 70 }).setDepth(DEPTH).setRotation(a);
    for (let i = -1; i <= 1; i++) claws.lineStyle(12, k.c[0], 0.6).lineBetween(-60, i * 24 - 34, 60, i * 24 + 34).lineStyle(4, 0xffffff).lineBetween(-60, i * 24 - 34, 60, i * 24 + 34);
    claws.setScale(0.3);
    k.scene.tweens.add({ targets: claws, scale: 1.2, duration: 160 });
    k.scene.tweens.add({ targets: claws, alpha: 0, delay: 350, duration: 300, onComplete: () => claws.destroy() });
    shake(k.scene, 160, 0.008);
    await wait(k.scene, 650);
    return;
  }
  const kind = k.v === 'wolf' ? 'wolf' : 'tiger';
  const fur = k.v === 'wolf' ? 0x9a90c8 : k.v === 'thunder' ? 0x8090b0 : 0xf0a040;
  for (let i = 0; i < 3; i++) k.scene.time.delayedCall(300 + i * 70, () => ring(k.scene, k.x, k.y - 80, fur, 120 + i * 30, 420, 7, DEPTH - 1));
  if (k.v === 'thunder') void arcs(k.scene, k.x, k.y - 90, 110, 0x7fd8ff, 800);
  await summon(k.scene, k.x - k.o.dir.x * 20, k.y - 20, beastHeadParts(fur, 0x201010, kind), k.c, { scale: 0.85, enter: 'zoom', exit: 'charge', hold: 450, dir: k.o.dir, depth: DEPTH - 1, pulse: true });
});

const birdV = fx(async (k) => {
  const v = k.v || 'eagle';
  const colorsBy: Record<string, [number, number, number]> = {
    phoenix: [0xffc040, 0xff5a1a, 0xff2a00],
    fire: [0xffc040, 0xff5a1a, 0xff2a00],
    darkphoenix: [0x8030ff, 0xb060ff, 0x4a10a0],
    condor: [0x40d090, 0x20a070, 0x108050],
    eagle: [0xf0e0b0, 0xd8a040, 0x806030],
    hawk: [0xc08050, 0x8a5a30, 0x5a3a20],
    pegasus: [0xeaf6ff, 0x8fd0ff, 0x4fa0ff],
  };
  const [body, wing, tail] = colorsBy[v] ?? [k.c[0], k.c[1] ?? k.c[0], k.c[0]];
  const parts = v === 'pegasus' ? horseParts(body, wing, false) : birdParts(body, wing, tail, v);
  const e = particles(k.scene, k.x, k.y - 60, v === 'phoenix' || v === 'fire' ? 'fx-flame' : 'fx-feather', { speed: { min: 60, max: 200 }, scale: { start: 1.2, end: 0.3 }, alpha: { start: 1, end: 0 }, tint: [body, wing], lifespan: 800, rotate: { min: 0, max: 360 } });
  e.explode(30);
  cleanup(k.scene, 1200, e);
  await summon(k.scene, k.x, k.y - 20, parts, k.c, { scale: v === 'pegasus' ? 0.9 : 0.85, enter: 'zoom', exit: 'charge', hold: 380, dir: k.o.dir, face: v !== 'pegasus', flip: v === 'pegasus', depth: DEPTH });
});

const horse = fx(async (k) => {
  ring(k.scene, k.x, k.y + 16, 0xd090ff, 90, 500, 5);
  await summon(k.scene, k.x, k.y + 10, horseParts(0xf0d8ff, 0xc070ff, true), k.c, { scale: 0.9, enter: 'zoom', exit: 'charge', hold: 400, dir: k.o.dir, flip: true });
});

/** Dragón con alas (guiverno), rey dragón musculoso o dragón que sale de la tierra. */
const dragonV = fx(async (k) => {
  const c0 = k.v === 'red' ? 0xe0302a : k.v === 'earth' ? 0x4a80c8 : k.v === 'king' ? 0x3a70e0 : 0x3a90e0;
  const wing = k.v === 'wyvern' || k.v === 'king' ? 0xe0803a : lighten(c0, 25);
  const head: Part[] = [
    ['p', c0, -70, 0, -60, -90, -20, -140, 30, -130, 80, -90, 90, -40, 60, 0],
    ['p', lighten(c0, 30), -40, -20, 60, -20, 50, -60, -30, -60],
    ['p', 0xffffff, -50, -10, -40, -10, -45, -30],
    ['p', 0xffffff, -20, -10, -10, -10, -15, -30],
    ['p', 0xffffff, 10, -10, 20, -10, 15, -30],
    ['p', 0xfff0a0, -20, -140, -50, -190, -5, -150],
    ['p', 0xfff0a0, 20, -138, 30, -190, 40, -130],
    ['c', 20, -100, 9, 0xffe040],
    ['c', 20, -100, 4, 0x000000],
  ];
  const wings: Part[] = k.v === 'wyvern' || k.v === 'king'
    ? [
        ['p', wing, -20, -100, -230, -220, -190, -60, -120, -90, -80, -40],
        ['p', wing, 60, -100, 270, -220, 230, -60, 160, -90, 120, -40],
        ['l', darken(wing, 30), 3, -20, -100, -200, -200],
        ['l', darken(wing, 30), 3, 60, -100, 240, -200],
      ]
    : [];
  const body: Part[] = k.v === 'king' ? [['e', 10, 40, 180, 140, c0], ['e', 10, 50, 110, 90, lighten(c0, 30)]] : [];
  if (k.v === 'earth') {
    puff(k.scene, k.x, k.y + 10, 'fx-rock', 30, { speed: { min: 160, max: 360 }, angle: { min: 200, max: 340 }, scale: { min: 0.8, max: 1.8 }, tint: [0xa8743a, 0x6a4a2a], lifespan: 900, gravityY: 800, rotate: { start: 0, end: 360 } });
    shake(k.scene, 300, 0.01);
  }
  const roar = (n: number) => {
    for (let i = 0; i < n; i++) k.scene.time.delayedCall(250 + i * 80, () => ring(k.scene, k.x, k.y - 80, c0, 130 + i * 30, 420, 6, DEPTH - 1));
  };
  roar(3);
  if (k.v === 'king') void arcs(k.scene, k.x, k.y - 80, 140, 0x7fd8ff, 800);
  await summon(k.scene, k.x - k.o.dir.x * 20, k.y + (k.v === 'earth' ? 40 : -10), [...wings, ...body, ...head], k.c, { scale: 0.8, enter: k.v === 'earth' ? 'rise' : 'zoom', exit: 'charge', hold: 450, dir: k.o.dir, flip: true, depth: DEPTH, pulse: true });
  // aliento de energía hacia delante
  await beam(k.scene, k.x, k.y - 30, k.o.dir, [c0, lighten(c0, 40), 0xffffff], 300, 26, 420);
});

/** Pingüinos dibujados con la paleta de la técnica (rojos, morados, con casco espacial...). */
const penguinV = fx(async (k) => {
  const body = k.v === 'red' ? 0xd02020 : k.v === 'purple' ? 0x8030d0 : 0x1a2030;
  const parts: Part[] = [
    ['e', 0, -26, 40, 52, body],
    ['e', 0, -22, 26, 38, 0xffffff],
    ['c', -7, -42, 4, 0xffffff],
    ['c', 7, -42, 4, 0xffffff],
    ['c', -6, -42, 2, 0x000000],
    ['c', 6, -42, 2, 0x000000],
    ['p', 0xffa21f, -6, -36, 6, -36, 0, -28],
    ['e', -8, 0, 12, 5, 0xffa21f],
    ['e', 8, 0, 12, 5, 0xffa21f],
  ];
  if (k.v === 'space') parts.push(['o', 0, -36, 28, 0xbfefff, 3]);
  if (k.v === 'space') puff(k.scene, k.x, k.y - 40, 'fx-star', 30, { speed: { min: 40, max: 160 }, scale: { start: 0.8, end: 0 }, tint: [0xffffff, 0x8fd0ff], lifespan: 900 });
  if (k.v === 'purple') void darkWarp(k.scene, k.x, k.y, k.o, [0x8030d0, 0xc070ff], '');
  ring(k.scene, k.x, k.y + 18, body === 0x1a2030 ? 0x3a6aff : body, 80, 500, 6);
  const birds: Promise<Phaser.GameObjects.Graphics>[] = [];
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2;
    const px = k.x + Math.cos(a) * 50;
    const py = k.y + 14 + Math.sin(a) * 22;
    birds.push(summon(k.scene, px, py, parts, k.c, { scale: 1.3, enter: 'rise', exit: 'charge', hold: 380 + i * 30, dir: k.o.dir, face: true, depth: DEPTH }));
  }
  await Promise.all(birds);
});

const whale = fx(async (k) => {
  const at = ahead(k, 60);
  void waveCrash(k, 0.8);
  const parts: Part[] = [
    ['e', 0, -60, 240, 110, 0x203050],
    ['e', 0, -40, 200, 60, 0xf0f4f8],
    ['p', 0x203050, 110, -60, 170, -110, 160, -40],
    ['e', -60, -40, 120, 30, 0xffffff],
    ['c', -70, -78, 7, 0xffffff],
    ['c', -70, -78, 3, 0x000000],
    ['p', 0xffffff, -110, -40, -100, -40, -105, -55],
    ['p', 0xffffff, -90, -40, -80, -40, -85, -55],
    ['p', 0xffffff, -70, -40, -60, -40, -65, -55],
  ];
  await summon(k.scene, at.x, at.y + 30, parts, k.c, { scale: 0.9, enter: 'rise', exit: 'charge', hold: 450, dir: k.o.dir, flip: true });
});

const shark = fx(async (k) => {
  const at = ahead(k, 60);
  void waveCrash(k, 0.8);
  const parts: Part[] = [
    ['p', 0x4a6a90, -140, -40, -40, -90, 90, -70, 150, -40, 90, -20, -40, -10],
    ['p', 0x4a6a90, -20, -80, 10, -140, 30, -76],
    ['p', 0x4a6a90, 130, -40, 180, -90, 170, -20],
    ['p', 0xe8eef4, -130, -38, -40, -20, 80, -30, 100, -40],
    ['p', 0x300010, -140, -40, -100, -50, -110, -26],
    ['c', -100, -62, 4, 0x000000],
  ];
  await summon(k.scene, at.x, at.y + 20, parts, k.c, { scale: 1, enter: 'rise', exit: 'charge', hold: 380, dir: k.o.dir, flip: true });
});

const snake = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const side = perp(k.o.dir);
  await animate(k.scene, 800, (t) => {
    g.clear();
    const head = t * 300;
    for (let s = 0; s < 14; s++) {
      const d = head - s * 14;
      if (d < 0) break;
      const w = Math.sin(d / 30) * 30;
      g.fillStyle(s % 2 ? k.c[0] : lighten(k.c[0], 30), 0.9).fillCircle(k.x + k.o.dir.x * d + side.x * w, k.y - 10 + k.o.dir.y * d + side.y * w, 16 - s * 0.7);
    }
    if (t >= 1) g.destroy();
  });
});

const unicorn = horse;

// ================================================================ muros y tierra

const wallV = fx(async (k) => {
  const at = ahead(k, 60);
  const rock = k.v === 'iron' ? 0x8a929a : 0xc09a60;
  const dark = darken(rock, 25);
  let parts: Part[];
  if (k.v === 'mountain') parts = [['p', 0x8a8070, -160, 0, -40, -200, 0, -170, 60, -230, 170, 0], ['p', 0xffffff, -40, -200, -10, -150, 20, -180, 60, -230, 80, -190, 30, -170]];
  else if (k.v === 'iron') parts = [['r', -130, -120, 260, 120, rock], ...[-90, -30, 30, 90].map((x) => ['r', x - 2, -120, 4, 120, dark] as Part), ['r', -130, -122, 260, 8, lighten(rock, 30)], ...[-110, -50, 10, 70].map((x) => ['c', x + 20, -100, 4, dark] as Part)];
  else if (k.v === 'stone') parts = [['r', -130, -140, 260, 140, 0x7a8a6a], ...[0, 1, 2, 3].flatMap((r) => [-1, 0, 1].map((c) => ['R', c * 80 - 38 + (r % 2) * 20, -136 + r * 34, 76, 30, 4, 0x9aa88a] as Part))];
  else if (k.v === 'pillars') {
    for (let i = 0; i < 6; i++) {
      const a = (i / 6) * Math.PI * 2;
      const px = at.x + Math.cos(a) * 70;
      const py = at.y + Math.sin(a) * 34;
      k.scene.time.delayedCall(i * 60, () => void summon(k.scene, px, py + 10, [['R', -18, -110, 36, 110, 6, rock], ['r', -18, -110, 36, 10, lighten(rock, 25)]], k.c, { scale: 1, enter: 'rise', exit: 'fade', hold: 500 - i * 50, depth: py + 20 }));
    }
    puff(k.scene, at.x, at.y + 10, 'fx-glow', 30, { speed: { min: 40, max: 160 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.5, end: 0 }, tint: 0xd8c090, lifespan: 900 });
    shake(k.scene, 300, 0.008);
    await wait(k.scene, 950);
    return;
  } else parts = [['p', rock, -140, 0, -150, -90, -100, -150, -30, -130, 20, -170, 90, -140, 150, -100, 140, 0], ['p', dark, -100, -20, -80, -110, -40, -40], ['p', dark, 40, -30, 70, -120, 100, -40], ['p', lighten(rock, 25), -100, -150, -30, -130, 20, -170, -20, -150]];
  puff(k.scene, at.x, at.y + 10, 'fx-glow', 30, { speed: { min: 40, max: 200 }, angle: { min: 180, max: 360 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.5, end: 0 }, tint: 0xd8c090, lifespan: 900 });
  shake(k.scene, 300, 0.008);
  await summon(k.scene, at.x, at.y + 20, parts, k.c, { scale: k.v === 'mountain' ? 1 : 0.9, enter: 'rise', exit: 'fade', hold: 550, depth: at.y + 40 });
});

/** Pinchos de roca que salen del suelo (Dientes de roca, Gran seísmo). */
const earthSpikes = fx(async (k) => {
  for (let i = 0; i < 7; i++) {
    const at = ahead(k, 30 + i * 34);
    const s = perp(k.o.dir);
    const off = Phaser.Math.Between(-30, 30);
    k.scene.time.delayedCall(i * 60, () => {
      void summon(k.scene, at.x + s.x * off, at.y + s.y * off + 16, [['p', 0xa8743a, -22, 0, 0, -90 - (i % 3) * 20, 22, 0], ['p', 0xd8b080, -6, -10, 0, -80 - (i % 3) * 20, 8, -10]], k.c, { scale: 1, enter: 'rise', exit: 'fade', hold: 400, depth: at.y + 30 });
      puff(k.scene, at.x, at.y + 10, 'fx-rock', 6, { speed: { min: 100, max: 240 }, angle: { min: 220, max: 320 }, tint: [0xa8743a, 0x6a4a2a], lifespan: 600, gravityY: 700 });
    });
  }
  shake(k.scene, 400, 0.009);
  await wait(k.scene, 1000);
});

/** Losa de tierra que se levanta y se voltea (Escudo protector). */
const earthSlab = fx(async (k) => {
  const at = ahead(k, 60);
  const g = k.scene.add.graphics({ x: at.x, y: at.y + 10 }).setDepth(at.y + 40);
  g.fillStyle(0x8a5a30).fillEllipse(0, -60, 200, 120).fillStyle(0xb07a40).fillEllipse(0, -66, 180, 96);
  g.setScale(1, 0.1);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scaleY: 1, duration: 300, ease: 'Back.out', onComplete: () => r() }));
  shake(k.scene, 200, 0.008);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scaleY: -1, duration: 300, onComplete: () => r() }));
  flash(k.scene, at.x, at.y - 40, 0xffd060, 160);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
  await wait(k.scene, 200);
});

/** Rocas flotando alrededor (Disparo con rebotes, Remate de Gaia) o bola de tierra (Bola de fango). */
const rocksV = fx(async (k) => {
  if (k.v === 'ball') {
    const at = ahead(k, 20, 10);
    const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    g.fillStyle(0x8a5a30).fillCircle(0, 0, 50).fillStyle(0xb07a40).fillCircle(-10, -10, 30).fillStyle(0x6a4a2a).fillCircle(20, 14, 10);
    g.setScale(0.2);
    k.scene.tweens.add({ targets: g, scale: 1.4, angle: 360, duration: 500 });
    await wait(k.scene, 500);
    const to = ahead(k, 300, 10);
    await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: to.x, y: to.y, angle: 720, duration: 380, ease: 'Quad.in', onComplete: () => r() }));
    g.destroy();
    flash(k.scene, to.x, to.y, 0xffd060, 180);
    return;
  }
  const rocks = Array.from({ length: 7 }, (_, i) => {
    const a = (i / 7) * Math.PI * 2;
    const r = k.scene.add.image(k.x + Math.cos(a) * 90, k.y - 60 + Math.sin(a) * 40, 'fx-rock').setTint(i % 2 ? 0xa8743a : 0xc8a070).setScale(0).setDepth(DEPTH);
    k.scene.tweens.add({ targets: r, scale: 3 + (i % 3), y: r.y - 30, angle: 90, duration: 400, delay: i * 40, ease: 'Back.out' });
    return r;
  });
  await wait(k.scene, 700);
  rocks.forEach((r) => k.scene.tweens.add({ targets: r, x: k.x + k.o.dir.x * 260, y: k.y + k.o.dir.y * 260, alpha: 0, scale: 1, duration: 320, ease: 'Quad.in', onComplete: () => r.destroy() }));
  await wait(k.scene, 320);
  flash(k.scene, k.x + k.o.dir.x * 260, k.y + k.o.dir.y * 260, k.c[0], 160);
});

/** Pie gigante que baja del cielo (Apisonadora, Super pisotón de sumo). */
const foot = fx(async (k) => {
  const at = ahead(k, 60);
  await summon(k.scene, at.x, at.y + 20, [['R', -50, -220, 100, 160, 30, 0xf0c040], ['e', 0, -50, 180, 80, 0xf0c040], ['e', 0, -50, 150, 50, 0xffe080], ...[-60, -30, 0, 30, 60].map((x) => ['c', x, -88, 14, 0xf0c040] as Part)], k.c, { scale: 0.9, enter: 'drop', exit: 'fade', hold: 250 });
  puff(k.scene, at.x, at.y + 10, 'fx-glow', 30, { speed: { min: 60, max: 220 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.5, end: 0 }, tint: 0xd8c090, lifespan: 900 });
  ring(k.scene, at.x, at.y + 16, 0xd8c090, 160, 600, 10);
});

const giant = fx(async (k) => {
  if (!k.o.texture) return;
  const c = k.scene.add.image(k.x, k.y + 20, k.o.texture).setOrigin(0.5, 1).setScale(k.o.scale ?? 1).setDepth(DEPTH).setAlpha(0.85);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: c, scale: (k.o.scale ?? 1) * 4, duration: 450, ease: 'Back.out', onComplete: () => r() }));
  shake(k.scene, 200, 0.01);
  await impactVariant(k.scene, k.x, k.y, k.o, k.c, 'giant');
  k.scene.tweens.add({ targets: c, alpha: 0, duration: 250, onComplete: () => c.destroy() });
});

// ================================================================ armas

const swordV = fx(async (k) => {
  const a = angleOf(k.o.dir);
  const color = k.v === 'fire' ? 0xff6a20 : k.v === 'excalibur' ? 0x40e0d0 : k.c[0];
  if (k.v === 'axe') {
    await summon(k.scene, k.x + k.o.dir.x * 60, k.y + 10, [['r', -6, -160, 12, 160, 0x8a5a30], ['p', 0xc8d0d8, 6, -160, 70, -180, 80, -110, 6, -120], ['l', 0xffffff, 3, 70, -180, 80, -110]], k.c, { scale: 0.9, enter: 'drop', exit: 'fade', hold: 200 });
    await impactVariant(k.scene, k.x, k.y, k.o, [0xffe040, 0xffffff], 'spark');
    return;
  }
  if (k.v === 'scythe') {
    const g = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH);
    g.lineStyle(30, color, 0.4).beginPath().arc(0, 0, 110, a - 1.2, a + 1.2).strokePath();
    g.lineStyle(10, 0xffffff, 0.9).beginPath().arc(0, 0, 110, a - 1.2, a + 1.2).strokePath();
    g.setScale(0.3).setAlpha(0);
    k.scene.tweens.add({ targets: g, scale: 1.2, alpha: 1, angle: 90, duration: 300, ease: 'Cubic.out' });
    k.scene.tweens.add({ targets: g, alpha: 0, delay: 400, duration: 250, onComplete: () => g.destroy() });
    await wait(k.scene, 650);
    return;
  }
  const len = k.v === 'giant' ? 260 : 190;
  const blade = k.scene.add.graphics({ x: k.x, y: k.y - 10 }).setDepth(DEPTH);
  blade.fillStyle(color, 0.35).fillTriangle(-18, 0, 18, 0, 0, -len);
  blade.fillStyle(lighten(color, 40)).fillTriangle(-8, 0, 8, 0, 0, -len + 10);
  blade.fillStyle(0xfff0a0).fillRect(-30, -2, 60, 10).fillRect(-5, 8, 10, 26);
  if (k.v === 'fire') {
    const e = particles(k.scene, k.x, k.y - 80, 'fx-flame', { speed: { min: 20, max: 80 }, scale: { start: 1.8, end: 0.2 }, tint: [0xff6a20, 0xffd23f], lifespan: 400, frequency: 15, quantity: 2, emitting: true });
    k.scene.time.delayedCall(700, () => e.stop());
    cleanup(k.scene, 1200, e);
  }
  if (k.v === 'excalibur') ring(k.scene, k.x, k.y - 10, 0xffe040, 80, 700, 6, DEPTH - 1, 1);
  blade.setRotation(a + Math.PI / 2).setScale(0.2);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: blade, scale: 1, duration: 300, ease: 'Back.out', onComplete: () => r() }));
  await wait(k.scene, 200);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: blade, x: k.x + k.o.dir.x * 260, y: k.y - 10 + k.o.dir.y * 260, alpha: 0, duration: 320, ease: 'Quad.in', onComplete: () => r() }));
  blade.destroy();
  const hit = ahead(k, 260);
  flash(k.scene, hit.x, hit.y, color, 180);
  puff(k.scene, hit.x, hit.y, 'fx-spark', 30, { speed: { min: 200, max: 420 }, scale: { start: 1, end: 0 }, tint: [color, 0xffffff], lifespan: 380 });
});

/** Siete espadas de luz en abanico que salen volando (Círculo de espadas). */
const swords = fx(async (k) => {
  const list = Array.from({ length: 7 }, (_, i) => {
    const a = -Math.PI / 2 + (i - 3) * 0.32;
    const g = k.scene.add.graphics({ x: k.x + Math.cos(a) * 100, y: k.y - 40 + Math.sin(a) * 70 }).setDepth(DEPTH);
    g.fillStyle(0xfff0a0, 0.5).fillTriangle(-8, 0, 8, 0, 0, -70).fillStyle(0xffffff).fillTriangle(-3, 0, 3, 0, 0, -64).fillStyle(0xffd040).fillRect(-12, 0, 24, 5);
    g.setRotation(a + Math.PI / 2).setScale(0);
    k.scene.tweens.add({ targets: g, scale: 1, delay: i * 60, duration: 220, ease: 'Back.out' });
    return g;
  });
  rays(k.scene, k.x, k.y - 40, [0xfff0a0, 0xffffff], 16, 200, 900);
  await wait(k.scene, 700);
  list.forEach((g, i) => k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 300, y: k.y + k.o.dir.y * 300, rotation: angleOf(k.o.dir) + Math.PI / 2, alpha: 0, delay: i * 30, duration: 320, ease: 'Quad.in', onComplete: () => g.destroy() }));
  await wait(k.scene, 500);
});

/** Lanza de energía (Flecha divina, Lanza letal, Aguijón). */
const spear = fx(async (k) => {
  const color = k.v === 'red' ? 0xff2040 : k.c[0];
  flash(k.scene, k.x, k.y - 10, color, 140);
  await beam(k.scene, k.x, k.y - 10, k.o.dir, [color, lighten(color, 30), 0xffffff], 340, 16, 520);
});

/** Media luna de energía que sale disparada (Corte giratorio, Corte volcánico, Luna creciente...). */
const crescent = fx(async (k) => {
  const color = k.v === 'fire' ? 0xff6a20 : k.v === 'demon' ? 0xa040ff : k.v === 'moon' ? 0xe0e8ff : k.c[0];
  const g = k.scene.add.graphics({ x: k.x, y: k.y - (k.v === 'ground' ? 0 : 20) }).setDepth(DEPTH).setRotation(angleOf(k.o.dir));
  // media luna: arco exterior hacia delante y arco interior desplazado hacia atrás
  const moonShape = (r: number, thick: number) => {
    const pts: Phaser.Geom.Point[] = [];
    for (let a = -1.25; a <= 1.25; a += 0.1) pts.push(pt(Math.cos(a) * r, Math.sin(a) * r));
    for (let a = 1.1; a >= -1.1; a -= 0.1) pts.push(pt(Math.cos(a) * r * 0.85 - thick, Math.sin(a) * r * 0.85));
    return pts;
  };
  g.fillStyle(color, 0.55).fillPoints(moonShape(100, 26), true);
  g.fillStyle(0xffffff, 0.95).fillPoints(moonShape(92, 12), true);
  if (k.v === 'demon') g.fillStyle(0x200030).fillTriangle(20, -30, 40, -20, 24, -10).fillTriangle(20, 30, 40, 20, 24, 10);
  if (k.v === 'fire') {
    const e = particles(k.scene, k.x, k.y, 'fx-flame', { speed: 40, scale: { start: 2, end: 0.2 }, tint: [0xff6a20, 0xffd23f], lifespan: 400, frequency: 12, quantity: 3, emitting: true });
    e.startFollow(g);
    k.scene.time.delayedCall(560, () => e.stop());
    cleanup(k.scene, 1000, e);
  }
  g.setScale(0.3);
  k.scene.tweens.add({ targets: g, scale: 1, duration: 220, ease: 'Back.out' });
  await wait(k.scene, 240);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scale: 1.3, x: k.x + k.o.dir.x * 300, y: g.y + k.o.dir.y * 300, duration: 650, ease: 'Quad.in', onComplete: () => r() }));
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 200, onComplete: () => g.destroy() });
  flash(k.scene, g.x, g.y, color, 140);
});

/** Taladro gigante girando (Destrozataladros). */
const drill = fx(async (k) => {
  const at = ahead(k, 70, 20);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH).setRotation(angleOf(k.o.dir) - Math.PI / 2);
  const draw = (t: number) => {
    g.clear().fillStyle(0xb8c0c8).fillTriangle(-50, 0, 50, 0, 0, 140);
    g.lineStyle(4, 0x6a7078);
    for (let i = 0; i < 5; i++) {
      const y = ((i * 28 + t * 200) % 140);
      const w = 50 * (1 - y / 140);
      g.lineBetween(-w, y, w, y + 14);
    }
    g.fillStyle(0x8a929a).fillRect(-56, -30, 112, 30);
  };
  await animate(k.scene, 800, draw);
  puff(k.scene, at.x, at.y, 'fx-spark', 30, { speed: { min: 200, max: 400 }, scale: { start: 1, end: 0 }, tint: [0xffe040, 0xffffff], lifespan: 350 });
  g.destroy();
});

/** Misil con humo (Remate misil). */
const missile = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH).setRotation(angleOf(k.o.dir) + Math.PI / 2);
  drawFigure(g, [['R', -14, -60, 28, 90, 12, 0xe0e4e8], ['p', 0xd02020, -14, -50, 14, -50, 0, -80], ['p', 0xd02020, -14, 20, -30, 40, -14, 30], ['p', 0xd02020, 14, 20, 30, 40, 14, 30]], k.c);
  const smoke = particles(k.scene, k.x, k.y, 'fx-glow', { speed: { min: 10, max: 40 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.6, end: 0 }, tint: 0xdddddd, lifespan: 600, frequency: 15, quantity: 2, emitting: true });
  const fire = particles(k.scene, k.x, k.y, 'fx-flame', { speed: 30, scale: { start: 1.6, end: 0.2 }, tint: [0xff6a20, 0xffd23f], lifespan: 250, frequency: 12, quantity: 2, emitting: true });
  smoke.startFollow(g);
  fire.startFollow(g);
  const to = ahead(k, 340, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: to.x, y: to.y, duration: 600, ease: 'Quad.in', onComplete: () => r() }));
  smoke.stop();
  fire.stop();
  g.destroy();
  cleanup(k.scene, 800, smoke, fire);
  await fireExplosion(k.scene, to.x - k.o.dir.x * 40, to.y - k.o.dir.y * 40, k.o, [0xff6a20, 0xffd23f], '');
});

// ================================================================ cielo y espacio

const meteorV = fx(async (k) => {
  if (k.v === 'belt') {
    const at = ahead(k, 40, 60);
    const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    await animate(k.scene, 900, (t) => {
      g.clear().lineStyle(4, 0xb060ff, 0.6).strokeEllipse(0, 0, 260, 70);
      for (let i = 0; i < 9; i++) {
        const a = (i / 9) * Math.PI * 2 + t * 4;
        g.fillStyle(i % 2 ? 0xb8a080 : 0x8a7050).fillCircle(Math.cos(a) * 130, Math.sin(a) * 35, 10 + (i % 3) * 3);
      }
      if (t >= 1) g.destroy();
    });
    await meteorV(k.scene, k.x, k.y, k.o, k.c, 'single');
    return;
  }
  const big = k.v === 'big';
  const n = big || k.v === 'single' ? 1 : 6;
  const falls: Promise<void>[] = [];
  for (let i = 0; i < n; i++) {
    falls.push(
      new Promise((resolve) => {
        const tx = (n === 1 ? ahead(k, 80).x : k.x + Phaser.Math.Between(-60, 60));
        const ty = (n === 1 ? ahead(k, 80).y : k.y + Phaser.Math.Between(-20, 20));
        const sx = tx + 260;
        const sy = ty - 380;
        const rock = k.scene.add.graphics({ x: sx, y: sy }).setDepth(DEPTH);
        const r = big ? 46 : 18;
        rock.fillStyle(0xff6a20, 0.5).fillCircle(0, 0, r * 1.5).fillStyle(0x6a4a3a).fillCircle(0, 0, r).fillStyle(0x8a6a5a).fillCircle(-r * 0.3, -r * 0.3, r * 0.5);
        const trail = particles(k.scene, sx, sy, 'fx-flame', { speed: 30, scale: { start: big ? 3.5 : 1.8, end: 0.2 }, alpha: { start: 0.9, end: 0 }, tint: [0xff6a20, 0xffd23f], lifespan: 400, frequency: 10, quantity: 3, emitting: true });
        trail.startFollow(rock);
        k.scene.tweens.add({
          targets: rock,
          x: tx,
          y: ty,
          duration: big ? 600 : 380,
          delay: i * 90,
          ease: 'Quad.in',
          onComplete: () => {
            trail.stop();
            rock.destroy();
            cleanup(k.scene, 500, trail);
            ring(k.scene, tx, ty + 16, 0xff6a20, big ? 160 : 60, 500, big ? 12 : 6);
            flash(k.scene, tx, ty, 0xffd060, big ? 260 : 90, 400);
            if (big) {
              screenFlash(k.scene, 0xffffff, 200);
              shake(k.scene, 350, 0.016);
            }
            resolve();
          },
        });
      }),
    );
  }
  await Promise.all(falls);
});

/** Planeta gigante que cae (Robo planeta) o la Tierra vista desde el espacio (Tiro galáctico). */
const planet = fx(async (k) => {
  const earth = k.v === 'earth';
  const parts: Part[] = earth
    ? [['c', 0, -110, 110, 0x2a6ad0], ['e', -30, -140, 80, 50, 0x40a050], ['e', 40, -80, 60, 40, 0x40a050], ['e', -10, -60, 50, 20, 0xffffff, 0.6], ['o', 0, -110, 112, 0x8fd0ff, 6]]
    : [['c', 0, -110, 110, 0xb07a50], ['e', -30, -140, 70, 40, 0x8a5a3a], ['e', 40, -80, 50, 30, 0x8a5a3a], ['e', 0, -110, 300, 40, 0xe0c090, 0.6]];
  puff(k.scene, k.x, k.y - 150, 'fx-star', 30, { speed: { min: 40, max: 160 }, scale: { start: 0.8, end: 0 }, tint: [0xffffff, 0xa88cff], lifespan: 900 });
  await summon(k.scene, ahead(k, 70).x, ahead(k, 70).y + 60, parts, k.c, { scale: 0.8, enter: earth ? 'zoom' : 'drop', exit: 'fade', hold: 350 });
  if (!earth) await fireExplosion(k.scene, k.x, k.y, k.o, [0xff6a20, 0xffd23f], '');
});

const moon = fx(async (k) => {
  const at = { x: k.x, y: k.y - 140 };
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH - 2);
  g.fillStyle(0xfff4c0, 0.25).fillCircle(0, 0, 110).fillStyle(0xfff0a0).fillCircle(0, 0, 80).fillStyle(0xe8d880).fillCircle(-24, -10, 16).fillCircle(20, 24, 10);
  g.setScale(0.2).setAlpha(0);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 1, duration: 400, ease: 'Cubic.out' });
  await wait(k.scene, 800);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 300, onComplete: () => g.destroy() });
});

/** Cometa con estela cian y estrellas (Tiro del cometa). */
const comet = fx(async (k) => {
  const head = k.scene.add.image(k.x, k.y - 20, 'fx-glow').setTint(0x8ff0ff).setScale(2.4).setDepth(DEPTH).setBlendMode('ADD');
  const tail = particles(k.scene, k.x, k.y - 20, 'fx-star', { speed: { min: 20, max: 80 }, scale: { start: 1.2, end: 0 }, tint: [0x8ff0ff, 0xffffff, 0xffe080], lifespan: 600, frequency: 12, quantity: 2, emitting: true });
  tail.startFollow(head);
  const to = ahead(k, 330, 20);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: head, x: to.x, y: to.y, duration: 700, ease: 'Sine.in', onComplete: () => r() }));
  tail.stop();
  head.destroy();
  flash(k.scene, to.x, to.y, 0x8ff0ff, 170);
  cleanup(k.scene, 800, tail);
});

/** Portal: túnel de rejilla verde (Agujero de gusano) o agujero al espacio en el suelo (Lanza de Odín). */
const portal = fx(async (k) => {
  const at = ahead(k, 40);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(k.v === 'space' ? GROUND : DEPTH);
  const grid = k.v === 'grid';
  await animate(k.scene, 900, (t) => {
    const grow = Math.min(1, t * 3);
    const fade = t > 0.8 ? (1 - t) / 0.2 : 1;
    g.clear();
    if (grid) {
      for (let i = 0; i < 6; i++) g.lineStyle(3, 0x40ff80, 0.8 * fade).strokeCircle(0, -20, (20 + ((i * 20 + t * 120) % 120)) * grow);
      for (let i = 0; i < 12; i++) {
        const a = (i / 12) * Math.PI * 2;
        g.lineBetween(0, -20, Math.cos(a) * 140 * grow, -20 + Math.sin(a) * 140 * grow);
      }
    } else {
      g.fillStyle(0x0a0820, fade).fillEllipse(0, 0, 220 * grow, 110 * grow);
      g.lineStyle(6, 0x8040ff, fade).strokeEllipse(0, 0, 220 * grow, 110 * grow);
      for (let i = 0; i < 12; i++) g.fillStyle(0xffffff, fade).fillCircle(Math.cos(i * 2.1) * 90 * grow, Math.sin(i * 2.1) * 40 * grow, 2);
    }
  });
  g.destroy();
});

const aurora = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH - 2);
  await animate(k.scene, 1000, (t) => {
    const fade = Math.sin(t * Math.PI);
    g.clear();
    for (let i = 0; i < 18; i++) {
      const x = k.x - 180 + i * 20;
      const h = 120 + Math.sin(i * 0.8 + t * 6) * 40;
      g.fillStyle(i % 3 ? 0x40ffb0 : 0x40c0ff, 0.55 * fade).fillRect(x, k.y - 80 - h, 20, h);
      g.fillStyle(0xffffff, 0.35 * fade).fillRect(x + 7, k.y - 80 - h, 4, h * 0.7);
    }
  });
  g.destroy();
});

const rainbow = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y }).setDepth(DEPTH - 1).setRotation(angleOf(k.o.dir) + Math.PI / 2);
  const bands = [0xff3030, 0xff9a20, 0xffe020, 0x40d040, 0x3090ff, 0x8040e0];
  await animate(k.scene, 900, (t) => {
    g.clear();
    const end = Math.PI * Math.min(1, t * 1.6);
    bands.forEach((c, i) => {
      g.lineStyle(10, c, 0.85 * (t > 0.8 ? (1 - t) / 0.2 : 1)).beginPath();
      g.arc(0, -150, 150 - i * 10, Math.PI, Math.PI + end);
      g.strokePath();
    });
  });
  g.destroy();
});

const fireworks = fx(async (k) => {
  for (let i = 0; i < 5; i++) {
    k.scene.time.delayedCall(i * 150, () => {
      const px = k.x + Phaser.Math.Between(-120, 120);
      const py = k.y - 120 + Phaser.Math.Between(-60, 30);
      puff(k.scene, px, py, 'fx-star', 26, { speed: { min: 80, max: 200 }, scale: { start: 0.9, end: 0 }, tint: [[0xff4060, 0x40ff80, 0x40a0ff, 0xffe040][i % 4], 0xffffff], lifespan: 700, gravityY: 120 });
    });
  }
  await wait(k.scene, 950);
});

// ================================================================ edificios y objetos

const towerV = fx(async (k) => {
  let parts: Part[];
  if (k.v === 'eiffel') parts = [['p', 0x8a6a4a, -70, 0, -10, -260, 10, -260, 70, 0, 40, 0, 0, -120, -40, 0], ['r', -40, -100, 80, 8, 0x8a6a4a], ['r', -24, -170, 48, 6, 0x8a6a4a], ['r', -3, -300, 6, 40, 0x8a6a4a]];
  else if (k.v === 'osaka') parts = [['r', -20, -260, 40, 220, 0xd08040], ['r', -40, -60, 80, 60, 0xb06030], ['r', -34, -230, 68, 30, 0xff4040], ['r', -4, -300, 8, 40, 0xd08040], ['r', -40, -130, 80, 10, 0xffe060]];
  else parts = [['p', 0xe8dcc0, -40, 0, -10, -240, 40, -236, 40, 0], ...[0, 1, 2, 3, 4].map((i) => ['r', -36 + i * 6, -40 - i * 44, 76, 6, 0xc8b898] as Part)];
  rays(k.scene, k.x, k.y - 150, [0xffffff, k.c[0]], 12, 200, 900, DEPTH - 3);
  await summon(k.scene, k.x - k.o.dir.x * 30, k.y + 10, parts, k.c, { scale: 0.8, enter: 'rise', exit: 'fade', hold: 550, depth: DEPTH - 2 });
});

const colosseum = fx(async (k) => {
  const parts: Part[] = [['e', 0, -40, 300, 120, 0xc0a070], ['e', 0, -40, 230, 70, 0x8a6a40]];
  for (let i = -6; i <= 6; i++) parts.push(['R', i * 22 - 7, -90 + Math.abs(i) * 3, 14, 30, 6, 0x5a4020]);
  await summon(k.scene, ahead(k, 60).x, ahead(k, 60).y + 40, parts, k.c, { scale: 0.9, enter: 'rise', exit: 'fade', hold: 500 });
  await impactVariant(k.scene, k.x, k.y, k.o, [0xffe040, 0xffffff], '');
});

const torii = fx(async (k) => {
  const parts: Part[] = [['r', -90, -190, 18, 190, 0xd02020], ['r', 72, -190, 18, 190, 0xd02020], ['p', 0xd02020, -130, -200, 130, -200, 120, -180, -120, -180], ['r', -110, -160, 220, 12, 0xd02020], ['r', -140, -212, 280, 12, 0x201010]];
  void darkHole(k.scene, k.x, k.y, k.o, [0xa040ff, 0x6020c0], '');
  await summon(k.scene, ahead(k, 60).x, ahead(k, 60).y + 30, parts, k.c, { scale: 0.8, enter: 'fade', exit: 'fade', hold: 600, depth: DEPTH - 2 });
});

const clock = fx(async (k) => {
  const at = ahead(k, 40, 60);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  if (k.v === 'freeze') k.scene.cameras.main.flash(300, 120, 160, 255);
  await animate(k.scene, 1000, (t) => {
    g.clear().fillStyle(0xd8a030).fillCircle(0, 0, 80).fillStyle(0xfff8e8).fillCircle(0, 0, 68);
    g.fillStyle(0xd8a030).fillRect(-8, -100, 16, 20);
    for (let i = 0; i < 12; i++) g.fillStyle(0x333333).fillCircle(Math.cos((i / 12) * Math.PI * 2) * 56, Math.sin((i / 12) * Math.PI * 2) * 56, 3);
    const h = -Math.PI / 2 + t * Math.PI * (k.v === 'freeze' ? 0.3 : 4);
    g.lineStyle(5, 0x222222).lineBetween(0, 0, Math.cos(h) * 50, Math.sin(h) * 50);
    g.lineStyle(3, 0x222222).lineBetween(0, 0, Math.cos(h / 12) * 34, Math.sin(h / 12) * 34);
    g.setScale(Math.min(1, t * 4)).setAlpha(t > 0.85 ? (1 - t) / 0.15 : 1);
  });
  g.destroy();
});

const train = fx(async (k) => {
  const s = perp(k.o.dir);
  const lights = k.scene.add.graphics({ x: k.x - s.x * 90, y: k.y - 20 }).setDepth(DEPTH);
  lights.fillStyle(0x222222).fillRect(-4, -60, 8, 80).fillStyle(0xff2020).fillCircle(-16, -60, 10).fillCircle(16, -60, 10);
  k.scene.tweens.add({ targets: lights, alpha: 0.3, duration: 120, yoyo: true, repeat: 3 });
  await wait(k.scene, 450);
  lights.destroy();
  const parts: Part[] = [['R', -70, -120, 140, 120, 14, 0xd8dce0], ['r', -60, -100, 120, 40, 0x304060], ['r', -70, -50, 140, 12, 0x2060c0], ['c', -40, -20, 10, 0xffffa0], ['c', 40, -20, 10, 0xffffa0]];
  await summon(k.scene, k.x - k.o.dir.x * 60, k.y + 10, parts, k.c, { scale: 0.9, enter: 'zoom', exit: 'charge', hold: 120, dir: k.o.dir });
  shake(k.scene, 250, 0.012);
});

const skull = fx(async (k) => {
  const parts: Part[] = [
    ['e', 0, -110, 200, 190, 0xe8e0f0],
    ['r', -60, -40, 120, 50, 0xe8e0f0],
    ['e', -42, -120, 56, 60, 0x200030],
    ['e', 42, -120, 56, 60, 0x200030],
    ['c', -42, -120, 10, 0xff2030],
    ['c', 42, -120, 10, 0xff2030],
    ['p', 0x200030, -12, -70, 12, -70, 0, -90],
    ...[-40, -20, 0, 20, 40].map((x) => ['r', x - 8, -40, 16, 26, 0xc8c0d0] as Part),
  ];
  puff(k.scene, k.x, k.y - 60, 'fx-glow', 24, { speed: { min: 30, max: 120 }, scale: { start: 1.6, end: 3 }, alpha: { start: 0.6, end: 0 }, tint: [0x8030d0, 0x300050], lifespan: 900 });
  await summon(k.scene, ahead(k, 50).x, ahead(k, 50).y + 20, parts, k.c, { scale: 0.8, enter: 'zoom', exit: 'fade', hold: 550, pulse: true });
});

const keys = fx(async (k) => {
  const at = ahead(k, 40, 30);
  const list = Array.from({ length: 4 }, (_, i) => {
    const a = (i / 4) * Math.PI * 2 + Math.PI / 4;
    const g = k.scene.add.graphics({ x: at.x + Math.cos(a) * 120, y: at.y + Math.sin(a) * 80 }).setDepth(DEPTH);
    g.lineStyle(6, 0xffd040).strokeCircle(0, -30, 14).fillStyle(0xffd040).fillRect(-3, -16, 6, 46).fillRect(3, 18, 12, 5).fillRect(3, 26, 9, 5);
    g.setRotation(a + Math.PI / 2);
    return g;
  });
  await new Promise<void>((r) => k.scene.tweens.add({ targets: list, x: at.x, y: at.y, duration: 450, ease: 'Back.in', onComplete: () => r() }));
  list.forEach((g) => g.destroy());
  ring(k.scene, at.x, at.y, 0xffd040, 80, 400, 6, DEPTH, 1);
  flash(k.scene, at.x, at.y, 0xffd040, 180);
  await wait(k.scene, 300);
});

const cape = fx(async (k) => {
  const s = perp(k.o.dir);
  const g = k.scene.add.graphics({ x: k.x + s.x * 40, y: k.y - 40 }).setDepth(DEPTH);
  g.fillStyle(0xd01818).fillPoints([pt(0, -40), pt(90, -30), pt(100, 60), pt(10, 50)], true);
  g.fillStyle(0xff4040).fillPoints([pt(0, -40), pt(40, -36), pt(50, 50), pt(10, 50)], true);
  g.setScale(0.2, 1);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scaleX: 1, duration: 250, yoyo: true, hold: 300, onComplete: () => r() }));
  g.destroy();
});

const fan = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 30 }).setDepth(DEPTH);
  g.fillStyle(0x8a5a30).fillRect(-6, 0, 12, 140);
  g.fillStyle(0xf0e8d0).fillCircle(0, -60, 90).lineStyle(6, 0xd02020).strokeCircle(0, -60, 90);
  g.fillStyle(0xd02020).fillCircle(0, -60, 30);
  g.setRotation(angleOf(k.o.dir) - 1.2).setScale(0.6);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, rotation: angleOf(k.o.dir) + 1.2, duration: 380, ease: 'Cubic.inOut', onComplete: () => r() }));
  void speedLines(k.scene, k.x + k.o.dir.x * 120, k.y + k.o.dir.y * 120, k.o.dir, [0xffffff, 0xd8e8ff], 500);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
  await wait(k.scene, 500);
});

const surfboard = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y + 16 }).setDepth(k.y + 10).setRotation(angleOf(k.o.dir));
  g.fillStyle(0xffffff).fillEllipse(0, 0, 120, 34).fillStyle(0x3090ff).fillRect(-50, -3, 100, 6);
  const e = particles(k.scene, k.x, k.y + 16, 'fx-glow', { speed: { min: 20, max: 80 }, scale: { start: 1, end: 2 }, alpha: { start: 0.5, end: 0 }, tint: 0xd8c090, lifespan: 500, frequency: 20, quantity: 2, emitting: true });
  e.startFollow(g);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 140, y: k.y + 16 + k.o.dir.y * 140, duration: 600, ease: 'Sine.inOut', onComplete: () => r() }));
  e.stop();
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 200, onComplete: () => g.destroy() });
  cleanup(k.scene, 700, e);
});

/** Balón con cara enfadada (Balón galgo), sandía (Bola falsa) o bomba (Bomba falsa). */
const ballFace = fx(async (k) => {
  const at = ahead(k, 30, 10);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  if (k.v === 'bomb') g.fillStyle(0x222222).fillCircle(0, 0, 40).fillStyle(0x666666).fillRect(-6, -52, 12, 14).lineStyle(3, 0xd8b080).lineBetween(0, -52, 14, -66);
  else if (k.v === 'melon') {
    g.fillStyle(0x2a8a3a).fillCircle(0, 0, 40);
    for (let i = -2; i <= 2; i++) g.lineStyle(5, 0x14501e).beginPath().arc(i * 14, 0, 40, -1.2, 1.2).strokePath();
  } else {
    g.fillStyle(0xffffff).fillCircle(0, 0, 40).lineStyle(3, 0x222222).strokeCircle(0, 0, 40);
    g.fillStyle(0xff2020).fillTriangle(-26, -12, -8, -6, -20, 4).fillTriangle(26, -12, 8, -6, 20, 4);
  }
  g.setScale(0.2);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scale: 1.4, duration: 300, ease: 'Back.out', onComplete: () => r() }));
  k.scene.tweens.add({ targets: g, angle: 20, duration: 80, yoyo: true, repeat: 3 });
  await wait(k.scene, 400);
  g.destroy();
  if (k.v === 'bomb') await fireExplosion(k.scene, at.x, at.y, k.o, [0xff6a20, 0xffd23f], '');
});
const fakeball = fx(async (k) => ballFace(k.scene, k.x, k.y, k.o, k.c, k.v === 'bomb' ? 'bomb' : 'melon'));
const dogball = fx(async (k) => ballFace(k.scene, k.x, k.y, k.o, k.c, 'dog'));

/** Balón que gira envuelto en anillos (Pared solitaria, Súper elástico). */
const ballspin = fx(async (k) => {
  const at = ahead(k, 30, 10);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  const color = k.v === 'cyan' ? 0x40f0e0 : 0xffffff;
  await animate(k.scene, 800, (t) => {
    g.clear();
    for (let i = 0; i < 3; i++) g.lineStyle(5, color, 0.8 * (1 - t * 0.6)).strokeEllipse(0, 0, 90 + i * 20, 30 + i * 8);
    g.setRotation(t * 12);
  });
  g.destroy();
  flash(k.scene, at.x, at.y, color, 120);
});

/** Bola gigante sobre la que se rueda (Equilibrismo, Superarmadillo, Armadillo circense). */
const ballride = fx(async (k) => {
  const armadillo = k.v === 'armadillo';
  const g = k.scene.add.graphics({ x: k.x, y: k.y }).setDepth(DEPTH);
  if (armadillo) {
    g.fillStyle(0x8a7a6a).fillCircle(0, 0, 44);
    for (let i = -2; i <= 2; i++) g.lineStyle(4, 0x5a4a3a).beginPath().arc(i * 16, 0, 44, -1.2, 1.2).strokePath();
  } else g.fillStyle(0xffffff).fillCircle(0, 0, 44).lineStyle(4, 0x222222).strokeCircle(0, 0, 44).fillStyle(0x222222).fillCircle(0, 0, 14);
  const dust = particles(k.scene, k.x, k.y + 30, 'fx-glow', { speed: { min: 20, max: 80 }, scale: { start: 1.2, end: 2.4 }, alpha: { start: 0.5, end: 0 }, tint: 0xd8c090, lifespan: 500, frequency: 20, quantity: 2, emitting: true });
  dust.startFollow(g, 0, 30);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 220, y: k.y + k.o.dir.y * 220, angle: 720, duration: 700, ease: 'Quad.in', onComplete: () => r() }));
  dust.stop();
  g.destroy();
  cleanup(k.scene, 600, dust);
});

const wheel = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 10 }).setDepth(DEPTH);
  g.lineStyle(14, 0xff6a20, 0.8).strokeCircle(0, 0, 50).lineStyle(6, 0xffd23f).strokeCircle(0, 0, 50);
  const e = particles(k.scene, k.x, k.y, 'fx-flame', { speed: 40, scale: { start: 2, end: 0.2 }, tint: [0xff6a20, 0xffd23f], lifespan: 350, frequency: 12, quantity: 3, emitting: true });
  e.startFollow(g);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 260, y: k.y - 10 + k.o.dir.y * 260, angle: 900, duration: 650, ease: 'Quad.in', onComplete: () => r() }));
  e.stop();
  g.destroy();
  cleanup(k.scene, 500, e);
});

const yoyo = fx(async (k) => {
  const at = ahead(k, 150, 10);
  const b = k.scene.add.image(k.x, k.y - 10, 'ball').setScale(2).setDepth(DEPTH);
  const line = k.scene.add.graphics().setDepth(DEPTH - 1);
  await animate(k.scene, 800, (t) => {
    const s = Math.sin(t * Math.PI);
    b.setPosition(k.x + (at.x - k.x) * s, k.y - 10 + (at.y - k.y + 10) * s).setAngle(t * 900);
    line.clear().lineStyle(2, 0xffffff, 0.8).lineBetween(k.x, k.y - 10, b.x, b.y);
  });
  b.destroy();
  line.destroy();
});

const vine = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  await animate(k.scene, 800, (t) => {
    g.clear().lineStyle(8, 0x3a8a2a).beginPath();
    for (let s = 0; s <= 1; s += 0.05) {
      const px = k.x - 120 + s * 240;
      const py = k.y - 200 + Math.sin(s * Math.PI) * 140 * Math.min(1, t * 2) + Math.sin(s * 10 + t * 6) * 6;
      if (s === 0) g.moveTo(px, py);
      else g.lineTo(px, py);
    }
    g.strokePath();
    for (let i = 0; i < 6; i++) g.fillStyle(0x50b030).fillEllipse(k.x - 100 + i * 40, k.y - 200 + Math.sin((i / 6) * Math.PI) * 140 * Math.min(1, t * 2), 18, 10);
    if (t >= 1) g.destroy();
  });
});

const bush = fx(async (k) => {
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2;
    const px = k.x + Math.cos(a) * 80;
    const py = k.y + Math.sin(a) * 36;
    k.scene.time.delayedCall(i * 60, () => void summon(k.scene, px, py + 10, [['c', 0, -30, 34, 0x2a8a2a], ['c', -24, -18, 24, 0x3aa03a], ['c', 24, -18, 24, 0x3aa03a], ['c', 0, -48, 20, 0x50c050]], k.c, { scale: 1, enter: 'rise', exit: 'shrink', hold: 400, depth: py + 20 }));
  }
  puff(k.scene, k.x, k.y - 20, 'fx-petal', 30, { speed: { min: 60, max: 200 }, scale: { start: 1, end: 0.4 }, tint: [0x3aa03a, 0x7ad040], lifespan: 900, rotate: { min: 0, max: 360 } });
  await wait(k.scene, 900);
});

const mole = fx(async (k) => {
  const mound = k.scene.add.graphics({ x: k.x, y: k.y + 14 }).setDepth(GROUND + 1);
  mound.fillStyle(0x8a5a30).fillEllipse(0, 0, 110, 46).fillStyle(0xb07a40).fillEllipse(0, -8, 70, 26).fillStyle(0x6a4020).fillEllipse(0, 6, 60, 14);
  const dirt = particles(k.scene, k.x, k.y + 10, 'fx-rock', { speed: { min: 100, max: 240 }, angle: { min: 220, max: 320 }, scale: { start: 1.6, end: 0.6 }, tint: [0x8a5a30, 0x6a4a2a], lifespan: 600, gravityY: 700, frequency: 25, quantity: 3, emitting: true });
  dirt.startFollow(mound);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: mound, x: k.x + k.o.dir.x * 200, y: k.y + 14 + k.o.dir.y * 200, duration: 700, onComplete: () => r() }));
  dirt.stop();
  puff(k.scene, mound.x, mound.y, 'fx-rock', 20, { speed: { min: 160, max: 320 }, angle: { min: 220, max: 320 }, tint: [0x8a5a30, 0x6a4a2a], lifespan: 700, gravityY: 700 });
  rays(k.scene, mound.x, mound.y - 30, [0xffe040, 0xffffff], 10, 120);
  mound.destroy();
  cleanup(k.scene, 600, dirt);
});

// ================================================================ telas, música, naturaleza

const web = fx(async (k) => {
  const at = ahead(k, 50);
  const g = k.scene.add.graphics({ x: at.x, y: at.y + (k.v === 'spider' ? -40 : 10) }).setDepth(k.v === 'spider' ? DEPTH : GROUND + 1);
  const flat = k.v === 'spider' ? 1 : 0.5;
  await animate(k.scene, 800, (t) => {
    const r = 120 * Math.min(1, t * 2);
    g.clear().lineStyle(2, 0xffffff, 0.9);
    for (let i = 0; i < 10; i++) {
      const a = (i / 10) * Math.PI * 2;
      g.lineBetween(0, 0, Math.cos(a) * r, Math.sin(a) * r * flat);
    }
    for (let ring2 = 1; ring2 <= 4; ring2++) {
      const pts = Array.from({ length: 11 }, (_, i) => new Phaser.Math.Vector2(Math.cos((i / 10) * Math.PI * 2) * r * (ring2 / 4), Math.sin((i / 10) * Math.PI * 2) * r * (ring2 / 4) * flat));
      g.strokePoints(pts);
    }
    if (k.v === 'spider') for (let i = 0; i < 6; i++) g.fillStyle(0xff2040).fillTriangle(Math.cos(i) * r * 0.6 - 6, Math.sin(i) * r * 0.6, Math.cos(i) * r * 0.6 + 6, Math.sin(i) * r * 0.6, Math.cos(i) * r * 0.9, Math.sin(i) * r * 0.9);
    g.setAlpha(t > 0.85 ? (1 - t) / 0.15 : 1);
  });
  g.destroy();
});

const ribbon = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  await animate(k.scene, 900, (t) => {
    g.clear().lineStyle(8, 0xff3050, t > 0.8 ? (1 - t) / 0.2 : 1).beginPath();
    for (let s = 0; s <= 1; s += 0.02) {
      const a = s * Math.PI * 4 + t * 8;
      const r = 40 + s * 60;
      const px = k.x + Math.cos(a) * r;
      const py = k.y - 40 + Math.sin(a) * r * 0.5 - s * 60 * t;
      if (s === 0) g.moveTo(px, py);
      else g.lineTo(px, py);
    }
    g.strokePath();
  });
  g.destroy();
});

const hearts = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 30 }).setDepth(DEPTH - 1);
  g.fillStyle(0xff80c0, 0.35).fillCircle(0, 0, 130);
  g.setScale(0.2);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 0.6, duration: 300 });
  puff(k.scene, k.x, k.y - 30, 'fx-heart', 26, { speed: { min: 60, max: 200 }, scale: { start: 1.6, end: 0.6 }, alpha: { start: 1, end: 0 }, tint: [0xff4090, 0xff90c0, 0xffffff], lifespan: 1000, gravityY: -60 });
  await wait(k.scene, 900);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
});

const notes = fx(async (k) => {
  for (let i = 0; i < 3; i++) k.scene.time.delayedCall(i * 150, () => ring(k.scene, k.x, k.y - 30, 0x8fd0ff, 120, 600, 4, DEPTH, 1));
  puff(k.scene, k.x, k.y - 30, 'fx-note', 20, { speed: { min: 60, max: 180 }, scale: { start: 1.6, end: 0.8 }, alpha: { start: 1, end: 0 }, tint: [0x8fd0ff, 0xffffff], lifespan: 1000, rotate: { min: -30, max: 30 } });
  await wait(k.scene, 900);
});

const bubbles = fx(async (k) => {
  if (k.v === 'giant') {
    const at = ahead(k, 40, 30);
    const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
    g.fillStyle(0xff90c0, 0.85).fillCircle(0, 0, 60).fillStyle(0xffffff, 0.6).fillEllipse(-20, -24, 30, 16);
    g.setScale(0.2);
    await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scale: 2.2, duration: 600, ease: 'Sine.in', onComplete: () => r() }));
    g.destroy();
    puff(k.scene, at.x, at.y, 'fx-bubble', 30, { speed: { min: 150, max: 360 }, scale: { start: 1.4, end: 0.4 }, tint: [0xff90c0, 0xffffff], lifespan: 600 });
    shake(k.scene, 160, 0.008);
    return;
  }
  const tint = k.v === 'pink' ? [0xff90e0, 0xffc0f0, 0xffffff] : [0x8fd0ff, 0xffffff];
  const e = particles(k.scene, k.x, k.y - 30, 'fx-bubble', { speed: { min: 20, max: 120 }, scale: { start: 1, end: 2.4 }, alpha: { start: 0.9, end: 0 }, tint, lifespan: 1200, frequency: 30, quantity: 3, emitting: true });
  await wait(k.scene, 900);
  e.stop();
  cleanup(k.scene, 1300, e);
});

const confetti = fx(async (k) => {
  puff(k.scene, k.x, k.y - 30, 'fx-petal', 60, { speed: { min: 120, max: 320 }, scale: { start: 1.2, end: 0.6 }, alpha: { start: 1, end: 0 }, tint: [0xff4060, 0x40ff80, 0x40a0ff, 0xffe040, 0xff80ff], lifespan: 1100, rotate: { min: 0, max: 720 }, gravityY: 200 });
  await wait(k.scene, 700);
});

const butterfly = fx(async (k) => {
  const parts: Part[] = [
    ['e', -80, -120, 150, 120, 0x40c0ff],
    ['e', 80, -120, 150, 120, 0x40c0ff],
    ['e', -60, -50, 100, 80, 0xff70d0],
    ['e', 60, -50, 100, 80, 0xff70d0],
    ['c', -90, -130, 22, 0x1a1030],
    ['c', 90, -130, 22, 0x1a1030],
    ['e', 0, -90, 18, 120, 0x1a1030],
  ];
  const g = await summon(k.scene, k.x, k.y - 10, parts, k.c, { scale: 0.8, enter: 'zoom', exit: 'fade', hold: 500, depth: DEPTH - 1 });
  void g;
  puff(k.scene, k.x, k.y - 60, 'fx-star', 24, { speed: { min: 60, max: 200 }, scale: { start: 0.8, end: 0 }, tint: [0xffffff, 0xff70d0, 0x40c0ff], lifespan: 800 });
});

const flowerRose = fx(async (k) => {
  const at = ahead(k, 30, 30);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  for (let i = 0; i < 8; i++) {
    const a = (i / 8) * Math.PI * 2;
    g.fillStyle(i % 2 ? 0xff3060 : 0xd01848).fillEllipse(Math.cos(a) * 24, Math.sin(a) * 24, 50, 40);
  }
  g.fillStyle(0xff6080).fillCircle(0, 0, 22);
  g.setScale(0.1);
  k.scene.tweens.add({ targets: g, scale: 1.4, angle: 90, duration: 450, ease: 'Back.out' });
  puff(k.scene, at.x, at.y, 'fx-petal', 50, { speed: { min: 80, max: 260 }, scale: { start: 1.3, end: 0.4 }, alpha: { start: 1, end: 0 }, tint: [0xff3060, 0xff90c0, 0xffffff], lifespan: 1100, rotate: { start: 0, end: 540 } });
  await wait(k.scene, 800);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
});

const dna = fx(async (k) => {
  const g = k.scene.add.graphics().setDepth(DEPTH);
  const s = perp(k.o.dir);
  await animate(k.scene, 900, (t) => {
    g.clear();
    const len = 300 * Math.min(1, t * 1.5);
    for (let d = 0; d < len; d += 10) {
      const w = Math.sin(d / 24 + t * 8) * 30;
      const ax = k.x + k.o.dir.x * d + s.x * w;
      const ay = k.y - 20 + k.o.dir.y * d + s.y * w;
      const bx = k.x + k.o.dir.x * d - s.x * w;
      const by = k.y - 20 + k.o.dir.y * d - s.y * w;
      g.fillStyle(0xff4040).fillCircle(ax, ay, 5).fillStyle(0x40a0ff).fillCircle(bx, by, 5);
      if (d % 30 === 0) g.lineStyle(2, 0xffffff, 0.7).lineBetween(ax, ay, bx, by);
    }
    g.setAlpha(t > 0.85 ? (1 - t) / 0.15 : 1);
  });
  g.destroy();
});

const wisps = fx(async (k) => {
  const list = Array.from({ length: 6 }, (_, i) => k.scene.add.image(k.x, k.y, 'fx-glow').setTint(i % 2 ? 0xa040ff : 0xd080ff).setScale(1.4).setDepth(DEPTH).setBlendMode('ADD'));
  await animate(k.scene, 1000, (t) => {
    list.forEach((w, i) => {
      const a = t * Math.PI * 4 + (i / 6) * Math.PI * 2;
      w.setPosition(k.x + Math.cos(a) * 80, k.y - 40 + Math.sin(a) * 40 - t * 30).setAlpha(Math.sin(t * Math.PI));
    });
  });
  list.forEach((w) => w.destroy());
});

const ghosthands = fx(async (k) => {
  const at = ahead(k, 50);
  void darkWarp(k.scene, at.x, at.y + 20, k.o, [0x8030d0, 0xc070ff], '');
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2;
    k.scene.time.delayedCall(i * 70, () => void summon(k.scene, at.x + Math.cos(a) * 60, at.y + Math.sin(a) * 28 + 20, handParts(0x9050e0, 0x401070), k.c, { scale: 0.4, enter: 'rise', exit: 'shrink', hold: 450 }));
  }
  await wait(k.scene, 950);
});

const shadowhand = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y + 14 }).setDepth(GROUND + 1).setRotation(angleOf(k.o.dir) + Math.PI / 2);
  drawFigure(g, handParts(0x000000, 0x000000), k.c);
  g.setScale(0.6, 0.3).setAlpha(0.7);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 160, y: k.y + 14 + k.o.dir.y * 160, scaleY: 0.9, duration: 650, onComplete: () => r() }));
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
});

const gravity = fx(async (k) => {
  await darkGravity(k.scene, k.x, k.y, k.o, [0x4060ff, 0xa040ff], '');
});

const scan = fx(async (k) => {
  const at = ahead(k, 60);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  await animate(k.scene, 900, (t) => {
    g.clear();
    const fade = t > 0.8 ? (1 - t) / 0.2 : 1;
    if (k.v === 'grid') {
      g.lineStyle(2, 0x40ff80, 0.7 * fade);
      for (let i = -5; i <= 5; i++) g.lineBetween(i * 24, -60, i * 24, 60).lineBetween(-120, i * 12, 120, i * 12);
    } else {
      for (let i = 1; i <= 3; i++) g.lineStyle(2, 0x40ff80, 0.8 * fade).strokeCircle(0, 0, i * 30);
      g.lineStyle(3, 0x40ff80, fade).lineBetween(0, 0, Math.cos(t * 12) * 90, Math.sin(t * 12) * 90);
    }
    g.lineStyle(3, 0xff4040, fade).strokeCircle(0, 0, 18).lineBetween(-30, 0, 30, 0).lineBetween(0, -30, 0, 30);
  });
  g.destroy();
});

const lasers = fx(async (k) => {
  const at = ahead(k, 80);
  const g = k.scene.add.graphics().setDepth(DEPTH);
  await animate(k.scene, 800, (t) => {
    g.clear().lineStyle(3, 0xff2020, t > 0.8 ? (1 - t) / 0.2 : 1);
    for (let i = 0; i < 6; i++) {
      const a = i * 0.9 + t * 2;
      g.lineBetween(at.x - Math.cos(a) * 160, at.y - Math.sin(a) * 90, at.x + Math.cos(a) * 160, at.y + Math.sin(a) * 90);
    }
  });
  g.destroy();
  await fireExplosion(k.scene, k.x + k.o.dir.x * 40, k.y + k.o.dir.y * 40, k.o, [0xff4020, 0xffd060], '');
});

const digital = fx(async (k) => {
  for (let i = 0; i < 14; i++) {
    k.scene.time.delayedCall(i * 40, () => {
      const c = k.scene.add.rectangle(k.x + Phaser.Math.Between(-60, 60), k.y - 30 + Phaser.Math.Between(-60, 40), 14, 14, 0x40ffb0, 0.8).setDepth(DEPTH);
      k.scene.tweens.add({ targets: c, alpha: 0, y: c.y - 30, duration: 500, onComplete: () => c.destroy() });
    });
  }
  if (k.o.texture) {
    const ghost = k.scene.add.image(k.x, k.y, k.o.texture).setScale(k.o.scale ?? 1).setTint(0x40ffb0).setAlpha(0.7).setDepth(DEPTH);
    k.scene.tweens.add({ targets: ghost, x: k.x + k.o.dir.x * 120, y: k.y + k.o.dir.y * 120, alpha: 0, duration: 700, onComplete: () => ghost.destroy() });
  }
  await wait(k.scene, 800);
});

const runes = fx(async (k) => {
  const g = k.scene.add.graphics({ x: k.x, y: k.y + 14 }).setDepth(GROUND + 1);
  await animate(k.scene, 1000, (t) => {
    g.clear();
    const fade = t > 0.8 ? (1 - t) / 0.2 : 1;
    g.lineStyle(4, 0x40ffb0, fade).strokeEllipse(0, 0, 260, 130).strokeEllipse(0, 0, 200, 100);
    for (let i = 0; i < 8; i++) {
      const a = (i / 8) * Math.PI * 2 + t * 2;
      g.fillStyle(0xffe040, fade).fillRect(Math.cos(a) * 115 - 5, Math.sin(a) * 57 - 5, 10, 10);
    }
    const tri = [0, 1, 2].map((i) => pt(Math.cos((i / 3) * Math.PI * 2 - t) * 100, Math.sin((i / 3) * Math.PI * 2 - t) * 50));
    g.lineStyle(2, 0x40ffb0, fade).strokePoints(tri, true);
  });
  g.destroy();
});

/** Triángulo de energía (Triángulo letal) o camino en Z (Triángulo Z). */
const triangle = fx(async (k) => {
  if (k.v === 'z') {
    const g = k.scene.add.graphics().setDepth(DEPTH);
    const s = perp(k.o.dir);
    const p = (d: number, w: number) => new Phaser.Math.Vector2(k.x + k.o.dir.x * d + s.x * w, k.y - 20 + k.o.dir.y * d + s.y * w);
    const pts = [p(0, -60), p(0, 60), p(150, -60), p(150, 60)];
    await animate(k.scene, 600, (t) => {
      g.clear().lineStyle(14, 0xff6a20, 0.7 * (1 - t * 0.5)).strokePoints(pts.slice(0, Math.max(2, Math.ceil(t * 4))));
      g.lineStyle(5, 0xffffff, 1 - t * 0.5).strokePoints(pts.slice(0, Math.max(2, Math.ceil(t * 4))));
    });
    g.destroy();
    return;
  }
  const at = ahead(k, 40, 70);
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH);
  const tri = [0, 1, 2].map((i) => pt(Math.cos(-Math.PI / 2 + (i / 3) * Math.PI * 2) * 100, Math.sin(-Math.PI / 2 + (i / 3) * Math.PI * 2) * 100));
  g.fillStyle(0x6a10b0, 0.4).fillPoints(tri, true).lineStyle(6, 0xc060ff).strokePoints(tri, true);
  g.lineStyle(3, 0xffffff, 0.8).strokeCircle(0, 0, 36).fillStyle(0xc060ff).fillCircle(0, 0, 12);
  g.setScale(0.1).setAlpha(0);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 1, angle: 360, duration: 500, ease: 'Cubic.out' });
  await wait(k.scene, 700);
  const to = ahead(k, 300, 20);
  k.scene.tweens.add({ targets: g, x: to.x, y: to.y, scale: 0.3, alpha: 0, duration: 300, ease: 'Quad.in', onComplete: () => g.destroy() });
  await wait(k.scene, 300);
  flash(k.scene, to.x, to.y, 0xc060ff, 180);
});

/** Cruz de luz (Pase cruzado) o X roja (Disparo X). */
const cross = fx(async (k) => {
  const at = ahead(k, 60, 20);
  const color = k.v === 'x' ? 0xff2030 : 0xffd040;
  const g = k.scene.add.graphics({ x: at.x, y: at.y }).setDepth(DEPTH).setRotation(k.v === 'x' ? Math.PI / 4 : 0);
  g.fillStyle(color, 0.5).fillRect(-140, -16, 280, 32).fillRect(-16, -140, 32, 280);
  g.fillStyle(0xffffff).fillRect(-140, -5, 280, 10).fillRect(-5, -140, 10, 280);
  g.setScale(0.1);
  await new Promise<void>((r) => k.scene.tweens.add({ targets: g, scale: 1, duration: 260, ease: 'Back.out', onComplete: () => r() }));
  flash(k.scene, at.x, at.y, color, 200);
  await wait(k.scene, 250);
  k.scene.tweens.add({ targets: g, alpha: 0, scale: 1.3, duration: 250, onComplete: () => g.destroy() });
});

/** Rayos rojos que llueven hacia delante (Diluvio letal). */
const redRays = fx(async (k) => {
  for (let i = 0; i < 6; i++) {
    k.scene.time.delayedCall(i * 80, () => {
      const s = perp(k.o.dir);
      const off = (i - 2.5) * 30;
      void beam(k.scene, k.x + s.x * off, k.y - 20 + s.y * off, k.o.dir, [0xff2030, 0xff6070], 300, 10, 450);
    });
  }
  await wait(k.scene, 950);
});

const wingsV = fx(async (k) => {
  const color = k.v === 'devil' ? 0x1a1030 : k.v === 'gold' ? 0xffd040 : 0xffffff;
  const edge = k.v === 'devil' ? 0x6030a0 : k.v === 'gold' ? 0xfff0a0 : 0xd0e8ff;
  const wing = (s: number): Part[] =>
    k.v === 'devil'
      ? [['p', color, 0, -60, s * 150, -150, s * 130, -90, s * 160, -60, s * 110, -40, s * 120, -10, 0, -30]]
      : [['p', color, 0, -50, s * 70, -140, s * 160, -150, s * 150, -90, s * 120, -40, 0, -20], ['p', edge, s * 20, -60, s * 140, -130, s * 110, -70]];
  if (k.v !== 'devil') puff(k.scene, k.x, k.y - 60, 'fx-feather', 24, { speed: { min: 40, max: 160 }, scale: { start: 1, end: 0.5 }, alpha: { start: 1, end: 0 }, tint: [color, edge], lifespan: 1000, rotate: { min: 0, max: 360 } });
  if (k.v === 'gold' || k.v === 'angel') rays(k.scene, k.x, k.y - 60, [0xffffff, edge], 14, 200, 800, DEPTH - 2);
  await summon(k.scene, k.x, k.y - 10, [...wing(-1), ...wing(1)], k.c, { scale: 0.9, enter: 'zoom', exit: 'fade', hold: 500, depth: DEPTH - 1 });
});

const charge = fx(async (k) => {
  const done = speedLines(k.scene, k.x, k.y, k.o.dir, [k.c[0], 0xffffff], 650);
  if (k.v === 'bull') await summon(k.scene, k.x, k.y - 10, [['e', 0, -60, 120, 100, 0x6a3a20], ['p', 0xf0e0c0, -50, -90, -110, -140, -40, -100], ['p', 0xf0e0c0, 50, -90, 110, -140, 40, -100], ['e', 0, -30, 60, 40, 0x8a5a40], ['c', -30, -80, 6, 0xff2020], ['c', 30, -80, 6, 0xff2020]], k.c, { scale: 0.8, enter: 'zoom', exit: 'charge', hold: 200, dir: k.o.dir });
  else if (k.v === 'roller') await summon(k.scene, k.x, k.y + 10, [['r', -70, -110, 140, 70, 0xf0c020], ['r', -50, -150, 60, 40, 0x304050], ['e', 0, -20, 170, 50, 0x6a6a6a], ['r', -85, -40, 170, 40, 0x8a8a8a]], k.c, { scale: 0.8, enter: 'zoom', exit: 'charge', hold: 200, dir: k.o.dir });
  else {
    const g = k.scene.add.graphics({ x: k.x, y: k.y - 20 }).setDepth(DEPTH - 1);
    g.fillStyle(k.c[0], 0.5).fillEllipse(0, 0, 110, 140).fillStyle(0xffffff, 0.4).fillEllipse(0, 0, 60, 80);
    k.scene.tweens.add({ targets: g, x: k.x + k.o.dir.x * 160, y: k.y - 20 + k.o.dir.y * 160, alpha: 0, duration: 600, onComplete: () => g.destroy() });
  }
  await done;
  await impactVariant(k.scene, k.x + k.o.dir.x * 100, k.y + k.o.dir.y * 100, k.o, k.c, '');
});

const slide = fx(async (k) => {
  const back = angleOf(k.o.dir) * DEG + 180;
  const e = particles(k.scene, k.x, k.y + 14, 'fx-glow', { speed: { min: 40, max: 140 }, angle: { min: back - 30, max: back + 30 }, scale: { start: 1.4, end: 2.6 }, alpha: { start: 0.6, end: 0 }, tint: 0xd8c090, lifespan: 600, frequency: 15, quantity: 3, emitting: true });
  const s = { t: 0 };
  k.scene.tweens.add({ targets: s, t: 1, duration: 550, onUpdate: () => e.setPosition(k.x + k.o.dir.x * 140 * s.t, k.y + 14 + k.o.dir.y * 140 * s.t) });
  if (k.v === 'quick') void speedLines(k.scene, k.x, k.y, k.o.dir, [0xffffff, 0x8fd0ff], 500);
  if (k.v === 'flip') void cloneV(k.scene, k.x, k.y, k.o, k.c, 'afterimage');
  await wait(k.scene, 600);
  e.stop();
  cleanup(k.scene, 700, e);
  await impactVariant(k.scene, k.x + k.o.dir.x * 140, k.y + k.o.dir.y * 140, k.o, k.c, 'small');
});

// ================================================================ agua

/** Ola gigante que rompe hacia delante (Remate tsunami, Muralla tsunami). */
function waveCrash(k: Ctx, scale = 1): Promise<void> {
  const g = k.scene.add.graphics({ x: k.x, y: k.y }).setDepth(DEPTH - 1).setRotation(angleOf(k.o.dir) + Math.PI / 2);
  return animate(k.scene, 900, (t) => {
    g.clear();
    const h = 200 * scale * Math.sin(Math.min(1, t * 1.4) * Math.PI * 0.5);
    const fwd = -t * 120 * scale;
    g.fillStyle(0x2f8fff, 0.75).fillPoints([pt(-150 * scale, 30), pt(-150 * scale, -h * 0.6 + fwd), pt(-40 * scale, -h + fwd), pt(80 * scale, -h * 0.8 + fwd), pt(150 * scale, -h * 0.4 + fwd), pt(150 * scale, 30)], true);
    g.fillStyle(0xbfe9ff, 0.9).fillPoints([pt(-40 * scale, -h + fwd), pt(80 * scale, -h * 0.8 + fwd), pt(60 * scale, -h * 0.7 + fwd), pt(-30 * scale, -h * 0.85 + fwd)], true);
    g.setAlpha(t > 0.8 ? (1 - t) / 0.2 : 1);
    if (t >= 1) g.destroy();
  });
}

const waterV = fx(async (k) => {
  if (k.v === 'wave') {
    puff(k.scene, k.x, k.y - 40, 'fx-glow', 40, { speed: { min: 100, max: 300 }, angle: { min: 200, max: 340 }, scale: { start: 1, end: 0.3 }, tint: [0xbfe9ff, 0xffffff], lifespan: 800, gravityY: 500 });
    await waveCrash(k, 1);
    return;
  }
  if (k.v === 'geyser') {
    const at = ahead(k, 50);
    ring(k.scene, at.x, at.y + 10, 0x2f8fff, 60, 500, 6);
    puff(k.scene, at.x, at.y, 'fx-glow', 70, { speedY: { min: -600, max: -300 }, speedX: { min: -60, max: 60 }, scale: { start: 1.6, end: 0.6 }, alpha: { start: 0.95, end: 0.2 }, tint: [0x2f8fff, 0xbfe9ff, 0xffffff], lifespan: 900, gravityY: 600 });
    await wait(k.scene, 900);
    return;
  }
  if (k.v === 'typhoon') {
    await funnel({ ...k, c: [0x2f8fff, 0xbfe9ff] }, k.x, k.y, 1000, 1.2);
    return;
  }
  // arrecife: mar de fondo con burbujas y corales
  const g = k.scene.add.graphics({ x: k.x, y: k.y - 40 }).setDepth(DEPTH - 2);
  g.fillStyle(0x1a8ab0, 0.4).fillCircle(0, 0, 160);
  for (let i = 0; i < 6; i++) g.fillStyle(i % 2 ? 0xff7a8a : 0xffa060, 0.8).fillTriangle(-140 + i * 50, 100, -120 + i * 50, 40, -100 + i * 50, 100);
  g.setScale(0.2).setAlpha(0);
  k.scene.tweens.add({ targets: g, scale: 1, alpha: 1, duration: 300 });
  puff(k.scene, k.x, k.y, 'fx-bubble', 30, { speedY: { min: -200, max: -60 }, speedX: { min: -60, max: 60 }, scale: { start: 0.8, end: 1.6 }, alpha: { start: 1, end: 0 }, tint: 0xffffff, lifespan: 1100 });
  await wait(k.scene, 900);
  k.scene.tweens.add({ targets: g, alpha: 0, duration: 250, onComplete: () => g.destroy() });
});

// ================================================================ registro

/**
 * Formas por nombre, o "forma:variante" cuando la variante tiene su propio dibujo. Las variantes que
 * solo cambian el color usan la forma base con la paleta del vídeo.
 */
export const SHAPES: Record<string, FxFn> = {
  'fire:breath': fireBreath,
  'fire:burst': fireBurst,
  'fire:comet': fireComet,
  'fire:dash': fireDash,
  'fire:explosion': fireExplosion,
  'fire:geyser': fireGeyser,
  'fire:hands': fireHands,
  'fire:spin': fireSpin,
  'fire:storm': fireStorm,
  'fire:sun': sun,
  'fire:swirl': fireSwirl,
  'fire:trail': fireTrail,
  'fire:zigzag': fireZigzag,
  impact: impactVariant,
  barrage,
  'light:beam': lightBeam,
  'light:flash': lightFlash,
  'light:halo': lightHalo,
  'light:rays': lightRays,
  tornado: tornadoV,
  'tornado:double': tornadoDouble,
  'tornado:spiral': tornadoSpiral,
  'wind:dash': windDash,
  speedlines: speedlinesFx,
  sandstorm,
  'dark:curse': darkCurse,
  'dark:gravity': darkGravity,
  'dark:hand': darkHand,
  'dark:hole': darkHole,
  'dark:orb': darkOrb,
  'dark:rift': darkRift,
  'dark:spiral': darkSpiral,
  'dark:warp': darkWarp,
  'lightning:barrier': lightningBarrier,
  'lightning:big': lightningBig,
  'lightning:hand': lightningHand,
  'lightning:orb': lightningOrb,
  'lightning:zigzag': lightningZigzag,
  hand: handV,
  punch: punchV,
  clone: cloneV,
  'ice:ball': iceBall,
  'ice:blizzard': iceBlizzard,
  'ice:block': iceBlock,
  'ice:cube': iceBlock,
  'ice:ground': iceGround,
  aura: auraV,
  stars: starsV,
  'shield:aura': shieldV,
  'shield:bubble': shieldV,
  'shield:dome': shieldV,
  'shield:panels': shieldV,
  'shield:rings': shieldV,
  beast: beastV,
  bird: birdV,
  unicorn,
  whale,
  shark,
  snake,
  dragon: dragonV,
  'dragon:blue': dragonV,
  'dragon:red': dragonV,
  penguin: penguinV,
  wall: wallV,
  'earth:spikes': earthSpikes,
  'earth:slab': earthSlab,
  rocks: rocksV,
  foot,
  giant,
  sword: swordV,
  swords,
  spear,
  crescent,
  drill,
  missile,
  meteor: meteorV,
  planet,
  moon,
  sun,
  comet,
  portal,
  aurora,
  rainbow,
  fireworks,
  tower: towerV,
  colosseum,
  torii,
  clock,
  train,
  skull,
  keys,
  cape,
  fan,
  surfboard,
  fakeball,
  dogball,
  ballspin,
  ballride,
  wheel,
  yoyo,
  vine,
  bush,
  mole,
  web,
  ribbon,
  hearts,
  notes,
  bubbles,
  confetti,
  butterfly,
  'flower:rose': flowerRose,
  dna,
  wisps,
  ghosthands,
  shadowhand,
  gravity,
  scan,
  lasers,
  digital,
  runes,
  triangle,
  cross,
  rays: redRays,
  wings: wingsV,
  charge,
  slide,
  'water:wave': waterV,
  'water:geyser': waterV,
  'water:typhoon': waterV,
  'water:reef': waterV,
};
