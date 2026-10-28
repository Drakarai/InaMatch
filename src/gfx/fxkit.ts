import Phaser from 'phaser';

/**
 * Piezas comunes de los efectos de las supertécnicas: partículas, aros, destellos y un pequeño
 * lenguaje para dibujar siluetas (una ballena, un tren, un torii...) y hacerlas aparecer.
 */

/** Por encima de los jugadores (su profundidad es su y) y de las marcas del suelo. */
export const DEPTH = 8000;
export const GROUND = -5;

export interface Dir {
  x: number;
  y: number;
}

type Obj = Phaser.GameObjects.GameObject & { destroy: () => void };

export const pt = (x: number, y: number) => new Phaser.Geom.Point(x, y);

/** Borra lo creado al cabo de `ms`. */
export function cleanup(scene: Phaser.Scene, ms: number, ...objs: Obj[]): void {
  scene.time.delayedCall(ms, () => objs.forEach((o) => o.active && o.destroy()));
}

export function wait(scene: Phaser.Scene, ms: number): Promise<void> {
  return new Promise((r) => scene.time.delayedCall(ms, r));
}

export function particles(scene: Phaser.Scene, x: number, y: number, key: string, config: Phaser.Types.GameObjects.Particles.ParticleEmitterConfig, depth = DEPTH) {
  const e = scene.add.particles(x, y, key, { emitting: false, blendMode: 'NORMAL', ...config });
  e.setDepth(depth);
  return e;
}

/** Explosión de partículas de una vez que se borra sola. */
export function puff(scene: Phaser.Scene, x: number, y: number, key: string, count: number, config: Phaser.Types.GameObjects.Particles.ParticleEmitterConfig, depth = DEPTH): void {
  const e = particles(scene, x, y, key, config, depth);
  e.explode(count);
  cleanup(scene, ((config.lifespan as number) ?? 800) + 300, e);
}

/** Aro que se expande y se desvanece (en el suelo, salvo que se pida otra profundidad). */
export function ring(scene: Phaser.Scene, x: number, y: number, color: number, radius: number, ms = 500, width = 6, depth = GROUND, flat = 0.55): void {
  const g = scene.add.graphics({ x, y }).setDepth(depth);
  const state = { t: 0 };
  scene.tweens.add({
    targets: state,
    t: 1,
    duration: ms,
    ease: 'Cubic.out',
    onUpdate: () => {
      g.clear().lineStyle(width * (1 - state.t) + 1, color, 1 - state.t);
      g.strokeEllipse(0, 0, radius * 2 * state.t, radius * 2 * flat * state.t);
    },
    onComplete: () => g.destroy(),
  });
}

/** Resplandor grande y breve. */
export function flash(scene: Phaser.Scene, x: number, y: number, color: number, size: number, ms = 350): void {
  const img = scene.add.image(x, y, 'fx-glow').setTint(color).setBlendMode('ADD').setDepth(DEPTH).setScale(size / 32);
  scene.tweens.add({ targets: img, scale: (size * 1.6) / 32, alpha: 0, duration: ms, onComplete: () => img.destroy() });
}

/** Fogonazo que tiñe toda la pantalla. */
export function screenFlash(scene: Phaser.Scene, color = 0xffffff, ms = 160): void {
  // mezclado con blanco y a media opacidad, para no tapar el campo con un color plano
  const c = Phaser.Display.Color.ValueToColor(lighten(color, 45));
  const cam = scene.cameras.main;
  cam.flashEffect.alpha = 0.5;
  cam.flash(ms, c.red, c.green, c.blue, true);
}

export function shake(scene: Phaser.Scene, ms = 160, power = 0.006): void {
  scene.cameras.main.shake(ms, power);
}

export function angleOf(dir: Dir): number {
  return Math.atan2(dir.y, dir.x);
}

export function lighten(color: number, amount: number): number {
  return Phaser.Display.Color.ValueToColor(color).lighten(amount).color;
}

export function darken(color: number, amount: number): number {
  return Phaser.Display.Color.ValueToColor(color).darken(amount).color;
}

/** Anima un valor de 0 a 1 llamando a `draw(t)` en cada fotograma. */
export function animate(scene: Phaser.Scene, ms: number, draw: (t: number) => void, ease = 'Linear'): Promise<void> {
  const s = { t: 0 };
  return new Promise((resolve) =>
    scene.tweens.add({ targets: s, t: 1, duration: ms, ease, onUpdate: () => draw(s.t), onComplete: () => (draw(1), resolve()) }),
  );
}

// ------------------------------------------------------------------ siluetas

/**
 * Silueta descrita como lista de piezas. El color es un índice de la paleta de la técnica
 * (0, 1, 2...) o un color fijo (0xRRGGBB). El origen (0, 0) es la base del dibujo.
 * - ['e', x, y, ancho, alto, color, alfa?]: elipse
 * - ['c', x, y, radio, color, alfa?]: círculo
 * - ['r', x, y, ancho, alto, color, alfa?]: rectángulo (x, y es la esquina de arriba a la izquierda)
 * - ['R', x, y, ancho, alto, radio, color, alfa?]: rectángulo redondeado
 * - ['p', color, x1, y1, x2, y2, ...]: polígono relleno
 * - ['l', color, grosor, x1, y1, x2, y2, ...]: línea quebrada
 * - ['o', x, y, radio, color, grosor]: circunferencia
 */
export type Part =
  | ['e', number, number, number, number, number, number?]
  | ['c', number, number, number, number, number?]
  | ['r', number, number, number, number, number, number?]
  | ['R', number, number, number, number, number, number, number?]
  | ['p', number, ...number[]]
  | ['l', number, number, ...number[]]
  | ['o', number, number, number, number, number];

function col(c: number, pal: number[]): number {
  return c < 16 ? (pal[c] ?? pal[pal.length - 1] ?? 0xffffff) : c;
}

export function drawFigure(g: Phaser.GameObjects.Graphics, parts: Part[], pal: number[]): void {
  for (const p of parts) {
    switch (p[0]) {
      case 'e':
        g.fillStyle(col(p[5], pal), p[6] ?? 1).fillEllipse(p[1], p[2], p[3], p[4]);
        break;
      case 'c':
        g.fillStyle(col(p[4], pal), p[5] ?? 1).fillCircle(p[1], p[2], p[3]);
        break;
      case 'r':
        g.fillStyle(col(p[5], pal), p[6] ?? 1).fillRect(p[1], p[2], p[3], p[4]);
        break;
      case 'R':
        g.fillStyle(col(p[6], pal), p[7] ?? 1).fillRoundedRect(p[1], p[2], p[3], p[4], p[5]);
        break;
      case 'p': {
        const v = p.slice(2) as number[];
        const pts: Phaser.Geom.Point[] = [];
        for (let i = 0; i + 1 < v.length; i += 2) pts.push(pt(v[i], v[i + 1]));
        g.fillStyle(col(p[1], pal)).fillPoints(pts, true);
        break;
      }
      case 'l': {
        const v = p.slice(3) as number[];
        const pts: Phaser.Math.Vector2[] = [];
        for (let i = 0; i + 1 < v.length; i += 2) pts.push(new Phaser.Math.Vector2(v[i], v[i + 1]));
        g.lineStyle(p[2], col(p[1], pal)).strokePoints(pts);
        break;
      }
      case 'o':
        g.lineStyle(p[5], col(p[4], pal)).strokeCircle(p[1], p[2], p[3]);
        break;
    }
  }
}

export interface SummonOptions {
  scale?: number;
  /** Cómo entra: crece desde el suelo, cae del cielo, aparece de golpe o se funde. */
  enter?: 'rise' | 'drop' | 'zoom' | 'fade';
  /** Cómo se va: se desvanece, embiste hacia delante, sube o se encoge. */
  exit?: 'fade' | 'charge' | 'up' | 'shrink';
  hold?: number;
  dir?: Dir;
  depth?: number;
  /** Gira la silueta hacia la dirección de la acción (para criaturas que vuelan o embisten). */
  face?: boolean;
  /** Late (crece y encoge) mientras está quieta. */
  pulse?: boolean;
  /** Se refleja si la acción va hacia la izquierda. */
  flip?: boolean;
}

/** Hace aparecer una silueta, la mantiene y la hace desaparecer. */
export async function summon(scene: Phaser.Scene, x: number, y: number, parts: Part[], pal: number[], o: SummonOptions = {}): Promise<Phaser.GameObjects.Graphics> {
  const scale = o.scale ?? 1;
  const dir = o.dir ?? { x: 0, y: -1 };
  const g = scene.add.graphics({ x, y }).setDepth(o.depth ?? DEPTH);
  drawFigure(g, parts, pal);
  const sx = o.flip && dir.x < 0 ? -scale : scale;
  if (o.face) g.setRotation(angleOf(dir) + Math.PI / 2);
  const enter = o.enter ?? 'zoom';
  if (enter === 'rise') {
    g.setScale(sx, 0.05).setY(y + 20);
    await new Promise<void>((r) => scene.tweens.add({ targets: g, scaleY: scale, y, duration: 320, ease: 'Back.out', onComplete: () => r() }));
  } else if (enter === 'drop') {
    g.setScale(sx, scale).setY(y - 420).setAlpha(0.6);
    await new Promise<void>((r) => scene.tweens.add({ targets: g, y, alpha: 1, duration: 300, ease: 'Quad.in', onComplete: () => r() }));
    shake(scene, 200, 0.01);
  } else if (enter === 'fade') {
    g.setScale(sx, scale).setAlpha(0);
    await new Promise<void>((r) => scene.tweens.add({ targets: g, alpha: 1, duration: 260, onComplete: () => r() }));
  } else {
    g.setScale(sx * 0.2, scale * 0.2).setAlpha(0);
    await new Promise<void>((r) => scene.tweens.add({ targets: g, scaleX: sx, scaleY: scale, alpha: 1, duration: 280, ease: 'Back.out', onComplete: () => r() }));
  }
  if (o.pulse) scene.tweens.add({ targets: g, scaleX: sx * 1.06, scaleY: scale * 1.06, duration: 140, yoyo: true, repeat: 1 });
  await wait(scene, o.hold ?? 380);
  const exit = o.exit ?? 'fade';
  const out: Phaser.Types.Tweens.TweenBuilderConfig = { targets: g, alpha: 0, duration: 300, onComplete: () => g.destroy() };
  if (exit === 'charge') Object.assign(out, { x: x + dir.x * 300, y: y + dir.y * 300, duration: 360, ease: 'Quad.in' });
  if (exit === 'up') Object.assign(out, { y: y - 160, duration: 380 });
  if (exit === 'shrink') Object.assign(out, { scaleX: 0, scaleY: 0, duration: 260, ease: 'Back.in' });
  scene.tweens.add(out);
  await wait(scene, (out.duration as number) * 0.6);
  return g;
}

/** Rayo recto de energía que sale en la dirección `dir` (lanzas, láseres, haces de luz). */
export function beam(scene: Phaser.Scene, x: number, y: number, dir: Dir, colors: number[], length = 320, width = 22, ms = 520): Promise<void> {
  const g = scene.add.graphics({ x, y }).setDepth(DEPTH).setRotation(angleOf(dir));
  return animate(
    scene,
    ms,
    (t) => {
      const grow = Math.min(1, t * 3);
      const fade = t > 0.6 ? (1 - t) / 0.4 : 1;
      const len = length * grow;
      g.clear();
      g.fillStyle(colors[0], 0.35 * fade).fillRect(0, -width, len, width * 2);
      g.fillStyle(colors[1] ?? colors[0], 0.8 * fade).fillRect(0, -width * 0.5, len, width);
      g.fillStyle(0xffffff, fade).fillRect(0, -width * 0.18, len, width * 0.36);
      g.fillStyle(0xffffff, fade).fillTriangle(len, -width * 0.6, len + width * 1.4, 0, len, width * 0.6);
      if (t >= 1) g.destroy();
    },
    'Cubic.out',
  );
}

/** Rayos que salen de un punto (fogonazo de manga). */
export function rays(scene: Phaser.Scene, x: number, y: number, colors: number[], count = 14, length = 170, ms = 650, depth = DEPTH - 1): void {
  const g = scene.add.graphics({ x, y }).setDepth(depth);
  for (let i = 0; i < count; i++) {
    const a = (i / count) * Math.PI * 2 + Math.random() * 0.2;
    const l = length * (0.7 + Math.random() * 0.5);
    g.fillStyle(colors[i % colors.length], 0.55).fillTriangle(0, 0, Math.cos(a - 0.06) * l, Math.sin(a - 0.06) * l, Math.cos(a + 0.06) * l, Math.sin(a + 0.06) * l);
  }
  g.setScale(0.2);
  scene.tweens.add({ targets: g, scale: 1.1, alpha: 0, rotation: 0.4, duration: ms, ease: 'Cubic.out', onComplete: () => g.destroy() });
}

/** Líneas de velocidad hacia atrás de la dirección de la acción. */
export function speedLines(scene: Phaser.Scene, x: number, y: number, dir: Dir, colors: number[], ms = 600): Promise<void> {
  const a = angleOf(dir);
  const e = particles(scene, x, y, 'fx-spark', {
    emitZone: { type: 'random', source: new Phaser.Geom.Rectangle(-140, -80, 280, 160), quantity: 1 },
    speed: { min: 700, max: 1000 },
    angle: (a * 180) / Math.PI + 180,
    rotate: (a * 180) / Math.PI + 90,
    scale: { start: 1.4, end: 0.8 },
    alpha: { start: 0.9, end: 0 },
    tint: [...colors, 0xffffff],
    lifespan: 220,
    frequency: 8,
    quantity: 3,
    emitting: true,
  });
  return wait(scene, ms).then(() => {
    e.stop();
    cleanup(scene, 400, e);
  });
}
