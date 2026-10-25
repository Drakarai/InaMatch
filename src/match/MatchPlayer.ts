import Phaser from 'phaser';
import { FONT, GAME_SPEED } from '../config';
import { movesOf } from '../data';
import type { MoveData, PlayerData, TeamData } from '../data/types';
import type { Fighter } from '../engine/rules';
import { texKey } from '../gfx/placeholders';

export type Side = 0 | 1; // 0 = jugador humano (ataca hacia arriba), 1 = CPU (ataca hacia abajo)

export interface Vec {
  x: number;
  y: number;
}

const SPRITE_HEIGHT = 46;

export class MatchPlayer {
  readonly sprite: Phaser.GameObjects.Image;
  readonly shadow: Phaser.GameObjects.Ellipse;
  readonly ring: Phaser.GameObjects.Ellipse;
  readonly tag: Phaser.GameObjects.Text;
  readonly moves: MoveData[];
  readonly maxFp: number;
  readonly maxTp: number;
  fp: number;
  tp: number;

  /** Recorrido dibujado por el jugador humano (o destino fijo al recibir un pase). */
  path: Vec[] = [];
  manual = false;
  stunnedUntil = 0;
  facing: Vec;
  moving = false;

  constructor(
    scene: Phaser.Scene,
    readonly data: PlayerData,
    readonly team: TeamData,
    readonly side: Side,
    readonly slot: number,
  ) {
    this.maxFp = data.fp;
    this.maxTp = data.tp;
    this.fp = data.fp;
    this.tp = data.tp;
    this.moves = movesOf(data.moves);
    this.facing = { x: 0, y: side === 0 ? -1 : 1 };
    this.shadow = scene.add.ellipse(0, 0, 26, 9, 0x000000, 0.28);
    const ringColor = side === 0 ? 0x4fa3ff : 0xff5a6a;
    this.ring = scene.add.ellipse(0, 0, 30, 11).setStrokeStyle(2, ringColor, 0.9);
    this.sprite = scene.add.image(0, 0, texKey.sprite(data.id));
    this.sprite.setScale(SPRITE_HEIGHT / this.sprite.height);
    this.tag = scene.add
      .text(0, 0, data.short, {
        fontFamily: FONT,
        fontSize: '12px',
        color: '#ffffff',
        backgroundColor: side === 0 ? '#2d5fb8' : '#a8283a',
        padding: { x: 4, y: 1 },
      })
      .setOrigin(0.5, 0)
      .setVisible(false);
  }

  get x(): number {
    return this.sprite.x;
  }

  get y(): number {
    return this.sprite.y;
  }

  get isGK(): boolean {
    return this.slot === 0;
  }

  setPos(x: number, y: number): void {
    this.sprite.setPosition(x, y);
  }

  speed(withBall: boolean): number {
    const base = 70 + this.data.stats.speed * 2.2;
    const tired = 0.8 + 0.2 * (this.fp / this.maxFp);
    return base * tired * (withBall ? 0.85 : 1) * GAME_SPEED;
  }

  isStunned(now: number): boolean {
    return now < this.stunnedUntil;
  }

  fighter(): Fighter {
    return { stats: this.data.stats, element: this.data.element, fp: this.fp, maxFp: this.maxFp };
  }

  /** Se mueve hacia `target`; devuelve true si ha llegado. */
  moveTowards(target: Vec, speed: number, dt: number): boolean {
    const dx = target.x - this.x;
    const dy = target.y - this.y;
    const dist = Math.hypot(dx, dy);
    const step = speed * dt;
    if (dist <= Math.max(step, 2)) {
      this.setPos(target.x, target.y);
      this.moving = false;
      return true;
    }
    this.facing = { x: dx / dist, y: dy / dist };
    this.setPos(this.x + this.facing.x * step, this.y + this.facing.y * step);
    this.moving = true;
    return false;
  }

  /** Sincroniza sombra, aro y profundidad con la posición del sprite. */
  syncVisuals(now: number, showTag: boolean): void {
    const feet = this.y + 21;
    this.shadow.setPosition(this.x, feet);
    this.ring.setPosition(this.x, feet);
    this.tag.setPosition(this.x, feet + 6).setVisible(showTag);
    const depth = feet;
    this.shadow.setDepth(depth - 2);
    this.ring.setDepth(depth - 1);
    this.sprite.setDepth(depth);
    this.tag.setDepth(10000);
    // pequeño bote al correr
    const bob = this.moving ? Math.abs(Math.sin(now * 14)) * 2 : 0;
    this.sprite.setOrigin(0.5, 0.5 + bob / this.sprite.height);
    this.sprite.setFlipX(this.facing.x < -0.3);
    // derribado: tumbado en el suelo y parpadea justo antes de levantarse
    const down = this.stunnedUntil - now;
    if (down > 0) {
      this.sprite.setAngle(this.facing.x < 0 ? -90 : 90);
      this.sprite.setAlpha(down < 0.6 && Math.floor(now * 12) % 2 ? 0.4 : 1);
    } else {
      this.sprite.setAngle(0);
      this.sprite.setAlpha(1);
    }
  }
}
